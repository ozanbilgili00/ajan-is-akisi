#!/usr/bin/env python3
"""Obsidian hafıza köprüsü.

  hafiza.py context   SessionStart (startup/resume/clear/compact): ilgili projenin
                      notlarını Claude'un bağlamına ekler.
  hafiza.py log       PreCompact / SessionEnd: oturumdaki istekleri ve değişen
                      dosyaları projenin Günlük.md'sine otomatik yazar.
"""
import json
import os
import re
import sys
import unicodedata
from datetime import datetime

VAULT = os.path.expanduser("~/Desktop/hafıza/hafıza")
PROJ = os.path.join(VAULT, "Projeler")
STATE = os.path.expanduser("~/.claude/state/hafiza")
MAX_PLAN = 6000
GUNLUK_ENTRIES = 4


def nfc(s):
    return unicodedata.normalize("NFC", s)


def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return {}, text
    meta, key = {}, None
    for line in m.group(1).splitlines():
        item = re.match(r"^\s+-\s+(.*)$", line)
        if item and key:
            meta.setdefault(key, [])
            if isinstance(meta[key], list):
                meta[key].append(item.group(1).strip().strip("\"'"))
            continue
        kv = re.match(r"^([\w-]+):\s*(.*)$", line)
        if kv:
            key, val = kv.group(1), kv.group(2).strip()
            meta[key] = val.strip("\"'") if val else []
    return meta, text[m.end():]


def projects():
    """[(ad, klasör, ana_not_yolu, meta)]"""
    out = []
    if not os.path.isdir(PROJ):
        return out
    for name in sorted(os.listdir(PROJ)):
        d = os.path.join(PROJ, name)
        main = os.path.join(d, name + ".md")
        if not os.path.isfile(main):
            continue
        meta, _ = frontmatter(read(main))
        out.append((name, d, main, meta))
    return out


def roots(meta):
    y = meta.get("yol", [])
    y = y if isinstance(y, list) else [y]
    return [nfc(os.path.expanduser(p)).rstrip("/") for p in y if p]


def match(path, projs):
    """path'i içeren en uzun yol eşleşmesi."""
    path = nfc(os.path.abspath(os.path.expanduser(path)))
    best, blen = None, -1
    for p in projs:
        for r in roots(p[3]):
            if (path == r or path.startswith(r + "/")) and len(r) > blen:
                best, blen = p, len(r)
    return best


def open_todos(text):
    keep = [l for l in text.splitlines()
            if l.startswith("#") or re.match(r"^\s*- \[ \]", l)]
    # içi boş başlıkları at
    out = []
    for i, l in enumerate(keep):
        if l.startswith("#"):
            nxt = keep[i + 1] if i + 1 < len(keep) else "#"
            if nxt.startswith("#") and nxt.count("#") <= l.count("#"):
                continue
        out.append(l)
    return "\n".join(out).strip()


def last_entries(text, n):
    _, body = frontmatter(text)
    parts = re.split(r"(?m)^(?=## )", body)
    entries = [p.strip() for p in parts if p.startswith("## ")]
    return "\n\n".join(entries[:n])  # en yeni en üstte


IS_AKISI = os.path.join(VAULT, "Kurallar", "İş Akışı")
TURLER = ["Web ve Sunucu", "Apple Uygulaması", "Oyun", "Araç ve MCP", "Araştırma ve Belge"]


def is_akisi(plan_text):
    """Plan.md'deki '**İş akışı:**' satırından tür notlarını ve güvenlik sınıfını çıkarır."""
    m = re.search(r"\*\*İş akışı:\*\*\s*(.+)", nfc(plan_text))
    if not m:
        return ("\n## İş akışı\nBu projenin Plan.md dosyasında `**İş akışı:**` satırı yok. İlk plan, faz ya da ajan "
                f"işinden önce {IS_AKISI}/İş Akışı.md dosyasını oku, Bölüm 2'ye göre türü ve güvenlik sınıfını "
                "belirleyip satırı Plan.md profil bloğuna ekle.")
    satir = m.group(1).strip()
    turler = [t for t in TURLER if t in satir]
    gs = re.search(r"GS[0-3]", satir)
    out = [f"\n## İş akışı\n{satir}"]
    oku = [f"{IS_AKISI}/{t}.md" for t in turler]
    if oku:
        out.append("Plan, faz ya da ajan işinden önce oku (oturumda bir kez): " + " · ".join(oku))
    if gs and gs.group(0) in ("GS2", "GS3"):
        out.append(f"Güvenlik sınıfı {gs.group(0)}: {IS_AKISI}/Güvenlik Hattı.md dosyasını da oku ve Bölüm 3'teki "
                   "kapıları uygula. Canlıda yazma her seferinde Ozan'ın onayıyla.")
    else:
        out.append(f"İş bir güvenlik tetikleyicisine dokunuyorsa {IS_AKISI}/Güvenlik Hattı.md dosyasını oku.")
    return "\n".join(out)


def uretim_parcalari(plan_text):
    """Üretim Kontrolü parçalarını günceller ve projenin okuyacağı dosyaları söyler."""
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import uretim_bol
        uretim_bol.guncelle()
        tur, ek, profil_var = uretim_bol.parcalar(plan_text)
    except Exception:
        return ""
    if not tur and not ek:
        return ("\n## Üretim kontrolü\nBu projenin türü belirlenemedi. Hangi parçanın okunacağı: "
                f"{uretim_bol.HEDEF}/Rehber.md")
    out = ["\n## Üretim kontrolü\nKaynak dosyanın tamamını OKUMA. Bu projenin parçaları (önce dizin, sonra yalnız fazın kapısındaki kimlikler):"]
    out += [f"- {p}" for p in tur]
    if ek:
        out.append("Ek modüller (ilgili faza gelince): " + " · ".join(os.path.basename(p)[:-3] for p in ek))
    if not profil_var:
        out.append(f"Plan.md'de profil bloğu yok; ilk plan işinde {uretim_bol.HEDEF}/Yöntem.md Bölüm 0-1'e göre ekle (ek modüller ona göre belirlenir).")
    return "\n".join(out)


RULES = """Kurallar (ayrıntı ~/.claude/CLAUDE.md): Bu notlar senin kalıcı hafızan.
Anlamlı bir adım bitince ana notun "Şu an" ve "Sıradaki adım" kısmını, Yapılacaklar.md'yi
(biteni [x] yap, yeniyi ekle) ve Günlük.md'yi (en üste "## YYYY-AA-GG — başlık") güncelle.
Plan değişirse Plan.md'yi güncelle. Kısa ve öz yaz."""


def cmd_context(data):
    cwd = data.get("cwd") or os.getcwd()
    source = data.get("source", "startup")
    projs = projects()
    p = match(cwd, projs)
    lines = [f"# Obsidian hafıza (vault: {VAULT})"]
    if source == "compact":
        lines.append("Compact yapıldı. Aşağıdaki proje notları kaldığın yeri gösteriyor.")

    if p:
        name, d, main, meta = p
        lines.append(f"\n## Aktif proje: {name}  ({d})")
        lines.append(frontmatter(read(main))[1].strip())
        plan = frontmatter(read(os.path.join(d, "Plan.md")))[1].strip()
        lines.append(is_akisi(plan))
        lines.append(uretim_parcalari(plan))
        if plan:
            if len(plan) > MAX_PLAN:
                plan = plan[:MAX_PLAN] + "\n…(kısaltıldı, tamamı Plan.md'de)"
            lines.append("\n## Plan.md\n" + plan)
        todo = open_todos(read(os.path.join(d, "Yapılacaklar.md")))
        if todo:
            lines.append("\n## Açık yapılacaklar\n" + todo)
        g = last_entries(read(os.path.join(d, "Günlük.md")), GUNLUK_ENTRIES)
        if g:
            lines.append("\n## Son günlük kayıtları\n" + g)
        if os.path.isfile(os.path.join(d, "Arşiv.md")):
            lines.append(f"\n(Eski ayrıntılı notlar: {d}/Arşiv.md. Gerekince oku.)")
    else:
        lines.append("\nBu dizin bir projeye eşleşmedi. Kayıtlı projeler:")
        for name, d, main, meta in projs:
            yol = ", ".join(roots(meta)).replace(os.path.expanduser("~"), "~")
            lines.append(f"- {name} [{meta.get('durum', '?')}] {yol} → {main}")
        lines.append("Kullanıcı bunlardan biri üzerinde çalışmak isterse önce o projenin ana notunu, "
                     "Plan.md ve Yapılacaklar.md dosyalarını oku. Yeni proje başlarsa "
                     f"{VAULT}/Şablonlar/Proje dosyalarıyla Projeler/<Ad>/ klasörünü oluştur.")
    lines.append("\n" + RULES)
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": "\n".join(lines)}}))


def text_of(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(b.get("text", "") for b in content
                         if isinstance(b, dict) and b.get("type") == "text")
    return ""


def is_real_prompt(msg):
    c = msg.get("content")
    if isinstance(c, list) and any(isinstance(b, dict) and b.get("type") == "tool_result" for b in c):
        return None
    t = text_of(c).strip()
    if (not t or t.startswith(("<", "/", "Caveat:", "This session is being continued"))
            or "[Request interrupted" in t):
        return None
    return t


EDIT_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit",
              "mcp__filesystem__write_file", "mcp__filesystem__edit_file"}


def cmd_log(data, event):
    tp = data.get("transcript_path")
    sid = data.get("session_id", "x")
    if not tp or not os.path.isfile(tp):
        return
    os.makedirs(STATE, exist_ok=True)
    state_file = os.path.join(STATE, sid + ".json")
    try:
        done = json.load(open(state_file)).get("lines", 0)
    except Exception:
        done = 0

    prompts, files = [], []
    with open(tp, encoding="utf-8") as f:
        all_lines = f.readlines()
    for raw in all_lines[done:]:
        try:
            e = json.loads(raw)
        except ValueError:
            continue
        if e.get("isSidechain") or e.get("isMeta") or e.get("isCompactSummary"):
            continue
        msg = e.get("message") or {}
        if e.get("type") == "user":
            t = is_real_prompt(msg)
            if t:
                t = " ".join(t.split())
                prompts.append(t[:220] + ("…" if len(t) > 220 else ""))
        elif e.get("type") == "assistant" and isinstance(msg.get("content"), list):
            for b in msg["content"]:
                if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") in EDIT_TOOLS:
                    inp = b.get("input") or {}
                    fp = inp.get("file_path") or inp.get("path") or inp.get("notebook_path")
                    if fp and fp not in files:
                        files.append(fp)

    json.dump({"lines": len(all_lines)}, open(state_file, "w"))

    vault_n = nfc(VAULT)
    files = [f for f in files if not nfc(os.path.abspath(f)).startswith(vault_n)]
    if not prompts and not files:
        return

    projs = projects()
    groups = {}
    for fp in files:
        p = match(fp, projs)
        groups.setdefault(p[0] if p else None, []).append(fp)
    cwd_p = match(data.get("cwd") or "", projs)
    if cwd_p and cwd_p[0] not in groups:
        groups[cwd_p[0]] = []
    if not groups:
        groups[None] = []

    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    label = {"PreCompact": "compact öncesi", "SessionEnd": "oturum sonu"}.get(event, event)
    home = os.path.expanduser("~")
    for name, fl in groups.items():
        if name is None and not fl:
            continue
        entry = [f"## {stamp} · otomatik ({label})", f"<!-- oturum {sid} -->"]
        if prompts:
            entry.append("**İstekler:**")
            entry += [f"- {p}" for p in prompts[-12:]]
        if fl:
            entry.append("**Değişen dosyalar:**")
            entry += [f"- `{f.replace(home, '~')}`" for f in fl[:40]]
        block = "\n".join(entry) + "\n\n"
        target = (os.path.join(PROJ, name, "Günlük.md") if name
                  else os.path.join(VAULT, "Gelen Kutusu.md"))
        prepend(target, block, name or "Gelen Kutusu")


def prepend(path, block, title):
    text = read(path)
    if not text:
        text = f"# {title} — Günlük\n\nEn yeni kayıt en üstte.\n\n"
    m = re.search(r"(?m)^## ", text)
    i = m.start() if m else len(text)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text[:i] + block + text[i:])


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    mode = sys.argv[1] if len(sys.argv) > 1 else "context"
    try:
        if mode == "context":
            cmd_context(data)
        elif mode == "log":
            cmd_log(data, data.get("hook_event_name", ""))
    except Exception as ex:  # hook asla oturumu bozmasın
        print(f"hafiza hook hatası: {ex}", file=sys.stderr)


if __name__ == "__main__":
    main()
