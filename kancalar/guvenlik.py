#!/usr/bin/env python3
"""Güvenlik kancası (PreToolUse). Kural kaynağı: vault Kurallar/İş Akışı/Güvenlik Hattı.md, Bölüm 6.

Karar: deny (her zaman yasak) · ask (Ozan onaylar; alt ajanda deny) · sessiz (karışmaz).
Amaç kazayı önlemek; kasıtlı atlatmaya karşı bir kale değildir (tırnak içindeki metne bakmaz).
Hata verirse hiçbir şeyi engellemez. Günlük: ~/.claude/state/guvenlik.log
"""
import json
import os
import re
import subprocess
import sys
from datetime import datetime

LOG = os.path.expanduser("~/.claude/state/guvenlik.log")
SIR_DOSYA = re.compile(
    r"(^|/)(\.env(\.(?!example$|sample$|template$|dist$)[\w.-]+)?"
    r"|id_(rsa|ed25519|ecdsa)|[\w.-]+\.(pem|p8|p12|keystore|jks)"
    r"|service[-_]?account[\w.-]*\.json|credentials\.json|\.netrc|\.npmrc)$", re.I)
SIR_KLASOR = re.compile(r"/\.(ssh|aws|gnupg)/")
ENV_TOKEN = r"(?<![\w.-])\.env(\.(?!example\b|sample\b|template\b|dist\b)[\w-]+)?(?![\w.-])"
OKUYAN = r"\b(cat|less|more|head|tail|bat|nl|strings|xxd|od|hexdump|base64|pbcopy|sed|awk|grep|rg|sort|tac|open|code|printenv)\b"

# (desen, karar, açıklama). Tırnak içleri ve heredoc gövdeleri silinmiş komuta uygulanır.
BASH = [
    (r"--no-verify\b|\bgit\s+commit\b[^|;&]*\s-[a-mo-zA-Z]*n[a-zA-Z]*(\s|$)", "deny", "commit kancası atlatılamaz (--no-verify)"),
    (r"\b(HUSKY|SKIP|LEFTHOOK|PRE_COMMIT_ALLOW_NO_CONFIG)=", "deny", "commit kancasını kapatan ortam değişkeni"),
    (r"\bgit\b(?:\s+-[cC]\s+\S+)*\s+config\b[^|;&]*core\.hooksPath", "deny", "git kanca yolu değiştirilemez"),
    (r"\brm\s+-[a-zA-Z]*[rR][a-zA-Z]*\s+(~|\$HOME|/)(/)?(\s|$)", "deny", "ana dizin ya da kök silinemez"),
    (r"\b(curl|wget)\b[^|;&]*\|\s*(sudo\s+)?(ba|z)?sh\b", "ask", "internetten indirilen betik doğrudan çalıştırılıyor"),
    (r"\bgit\b(?:\s+-[cC]\s+\S+)*\s+push\b[^|;&]*(\s--force\b|\s--force-with-lease\b|\s-[a-zA-Z]*f[a-zA-Z]*(\s|$))", "ask", "zorla push"),
    (r"\bgit\b(?:\s+-[cC]\s+\S+)*\s+push\b[^|;&]*\s--delete\b", "ask", "uzak dal siliniyor"),
    (r"\bsupabase\s+(db\s+(push|reset)[^|;&]*|migration\s+(up|repair)[^|;&]*--linked|functions\s+(deploy|delete)|secrets\s+(set|unset)|projects\s+(create|delete)|branches\s+(delete|merge))", "ask", "Supabase canlı yazma"),
    (r"\bfirebase\s+(deploy|hosting:channel:deploy|functions:(delete|config:set|secrets:set)|firestore:delete|database:(set|update|remove|push)|auth:import|use\s+--add)", "ask", "Firebase canlı yazma"),
    (r"\bvercel\b[^|;&]*(\s--prod\b|\s(deploy|promote|rollback|remove|rm|alias|domains|dns)\b|\senv\s+(add|rm|pull)\b)", "ask", "Vercel canlı yazma ya da sır çekme"),
    (r"\bgh\s+(repo\s+(delete|create|edit|rename|archive)|secret\s+(set|delete)|variable\s+(set|delete)|release\s+(create|delete)|workflow\s+run|api\b[^|;&]*(-X|--method)\s*(POST|PUT|PATCH|DELETE))", "ask", "GitHub'da yazma"),
    (r"\b(npm|pnpm|yarn|bun)\s+publish\b|\bcargo\s+publish\b|\btwine\s+upload\b|\bpod\s+trunk\s+push\b", "ask", "paket yayınlama"),
    (r"\b(ssh|scp|sftp|rsync)\b[^|;&]*\s[\w.-]+@[\w.-]+", "ask", "uzak sunucuya bağlantı"),
    (r"\b(psql|pg_dump|pg_restore|mysql|mongosh)\b[^|;&]*(postgres(ql)?|mysql|mongodb(\+srv)?)://(?![^/\s]*(localhost|127\.0\.0\.1|host\.docker\.internal))", "ask", "uzak veritabanına bağlantı"),
    (r"\bxcrun\s+(altool|notarytool)\b|\bfastlane\s+(deliver|pilot|release|upload)", "ask", "mağazaya gönderim"),
    (r"\bdocker\s+push\b|\bdocker\s+compose\b[^|;&]*-H\s|\bkubectl\s+(apply|delete)\b|\bterraform\s+(apply|destroy)\b", "ask", "canlı altyapı değişikliği"),
]
MCP_SALT_OKUNUR = re.compile(r"__(get|list|search|count|aggregate|filter|read|query|web_fetch|generate_typescript_types|validate|developerknowledge)", re.I)
SQL_YAZAN = re.compile(r"\b(insert|update|delete|drop|alter|create|truncate|grant|revoke|copy|call|do|vacuum|reindex|comment|refresh)\b", re.I)


def log(s):
    try:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} {s}\n")
    except OSError:
        pass


def karar(tur, neden, alt_ajan, arac):
    if tur == "ask" and alt_ajan:
        tur, neden = "deny", neden + ". Alt ajan canlıya yazamaz ve dışarıya gönderemez; dur ve yöneticiye raporla"
    neden = f"[Güvenlik Hattı] {neden}."
    if tur == "deny":
        neden += " Başka yoldan deneme; gerekiyorsa Ozan'a sor."
    log(f"{tur.upper()} {'alt-ajan' if alt_ajan else 'ana'} {arac}: {neden}")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
          "permissionDecision": tur, "permissionDecisionReason": neden}}, ensure_ascii=False))
    sys.exit(0)


def ciplak(cmd):
    """Heredoc gövdelerini ve tırnak içlerini siler (commit mesajı, echo metni yanlış alarm vermesin)."""
    cmd = re.sub(r"<<-?\s*(['\"]?)(\w+)\1.*?^\s*\2\s*$", " ", cmd, flags=re.S | re.M)
    cmd = re.sub(r"'[^']*'", "''", cmd)
    cmd = re.sub(r'"(?:\\.|[^"\\])*"', '""', cmd)
    return cmd


def repo_dizini(cmd, cwd):
    m = re.search(r"\bgit\s+-C\s+(\"[^\"]+\"|'[^']+'|\S+)", cmd) or re.match(r"\s*cd\s+(\"[^\"]+\"|'[^']+'|\S+)\s*(&&|;)", cmd)
    if m:
        d = os.path.expanduser(m.group(1).strip("\"'"))
        return d if os.path.isabs(d) else os.path.join(cwd, d)
    return cwd


def sir_tara(dizin):
    """Commit öncesi: sahnelenmiş ve sahnelenmemiş değişikliklerde gitleaks. Bulgu satırlarını döndürür."""
    import shutil
    gl = shutil.which("gitleaks") or "/opt/homebrew/bin/gitleaks"
    if not os.path.exists(gl) or not os.path.isdir(dizin):
        return None
    bulgular = []
    for ek in (["--staged"], []):
        try:
            r = subprocess.run([gl, "protect", "--redact", "--no-banner", "--exit-code", "9", "-v"] + ek,
                               cwd=dizin, capture_output=True, text=True, timeout=40)
        except (OSError, subprocess.TimeoutExpired):
            return None
        if r.returncode == 9:
            dosya = re.findall(r"^File:\s+(.+)$", r.stdout, re.M)
            satir = re.findall(r"^Line:\s+(\d+)$", r.stdout, re.M)
            kural = re.findall(r"^RuleID:\s+(.+)$", r.stdout, re.M)
            for i, d in enumerate(dosya):
                bulgular.append(f"{d}:{satir[i] if i < len(satir) else '?'} ({kural[i] if i < len(kural) else 'sır'})")
    return sorted(set(bulgular))


def main():
    data = json.load(sys.stdin)
    arac = data.get("tool_name", "")
    girdi = data.get("tool_input") or {}
    alt_ajan = bool(data.get("agent_id") or data.get("agent_type"))
    cwd = data.get("cwd") or os.getcwd()

    if arac in ("Read", "Edit", "Write", "NotebookEdit"):
        yol = girdi.get("file_path") or girdi.get("notebook_path") or ""
        if SIR_DOSYA.search(yol) or SIR_KLASOR.search(yol):
            if arac == "Read" or alt_ajan:
                karar("deny", f"sır dosyası {'okunamaz' if arac == 'Read' else 'değiştirilemez'}: {os.path.basename(yol)}. "
                      "Değişken adları gerekiyorsa Ozan `! cut -d= -f1 <dosya>` çalıştırsın", alt_ajan, arac)
            karar("ask", f"sır dosyasına yazılıyor: {os.path.basename(yol)}", alt_ajan, arac)
        return

    if arac == "Grep":
        yol = girdi.get("path") or ""
        if SIR_DOSYA.search(yol) or SIR_KLASOR.search(yol):
            karar("deny", f"sır dosyası aranamaz: {os.path.basename(yol)}", alt_ajan, arac)
        return

    if arac.startswith("mcp__"):
        canli = re.match(r"mcp__(supabase|plugin_firebase_firebase|plugin_vercel_vercel)__", arac)
        if not canli:
            return
        if alt_ajan:
            karar("deny", "canlı sisteme erişen araç alt ajana kapalı; dur ve yöneticiye raporla", alt_ajan, arac)
        if arac.endswith("__execute_sql"):
            if SQL_YAZAN.search(girdi.get("query") or ""):
                karar("ask", "canlı veritabanında yazan SQL", alt_ajan, arac)
            return
        if not MCP_SALT_OKUNUR.search(arac):
            karar("ask", f"canlıda yazma: {arac.split('__')[-1]}", alt_ajan, arac)
        return

    if arac != "Bash":
        return
    cmd = girdi.get("command") or ""
    c = ciplak(cmd)

    for parca in re.split(r"&&|\|\||;|\n", c):
        if re.search(ENV_TOKEN, parca) and re.search(OKUYAN, parca) and not re.search(r"\bcut\s+-d\s*=\s+-f\s*1\b", parca):
            karar("deny", ".env içeriği okunamaz. Değişken adları için yalnız `cut -d= -f1 .env` kullanılabilir", alt_ajan, arac)
    if re.search(r"\b(cat|less|head|tail|bat|base64|pbcopy|scp|cp)\b[^|;&]*(/\.ssh/|/\.aws/|/\.gnupg/|\.pem\b|\.p8\b|\.p12\b|id_rsa|id_ed25519)", c):
        karar("deny", "anahtar dosyası okunamaz ya da kopyalanamaz", alt_ajan, arac)

    for desen, tur, aciklama in BASH:
        if re.search(desen, c):
            karar(tur, aciklama, alt_ajan, arac)
    if alt_ajan and re.search(r"\bgit\b(?:\s+-[cC]\s+\S+)*\s+push\b|\bgh\s+pr\s+(create|merge|close)\b", c):
        karar("deny", "alt ajan push, PR ve birleştirme yapamaz; dur ve yöneticiye raporla", alt_ajan, arac)

    if re.search(r"\bgit\b[^|;&]*\scommit\b", c):
        bulgu = sir_tara(repo_dizini(cmd, cwd))
        if bulgu:
            karar("deny", "commit durduruldu, değişikliklerde olası sır var: " + "; ".join(bulgu[:8]) +
                  ". Gerçek sırsa kaldır ve Ozan'a haber ver (anahtar yenilenmeli). Yanlış alarmsa Ozan'a göster; "
                  "onayıyla `.gitleaksignore` ya da satır sonuna `gitleaks:allow` eklenir", alt_ajan, arac)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # kanca hatası işi kilitlemesin
        log(f"HATA {type(e).__name__}: {e}")
    sys.exit(0)
