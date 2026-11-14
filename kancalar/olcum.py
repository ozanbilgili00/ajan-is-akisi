#!/usr/bin/env python3
"""Ajan ölçümü.
  olcum.py kaydet   SubagentStop kancası: biten alt ajanın türünü, süresini ve token harcamasını
                    ~/.claude/state/ajan-olcum.jsonl dosyasına yazar.
  olcum.py ozet [gün]   Son N günün (varsayılan 30) ajan türüne göre özetini basar.
Bulgu sayısı ve denetim kararı otomatik ölçülemez; onları yönetici Günlük.md'ye yazar.
"""
import json, os, sys
from datetime import datetime, timedelta

OUT = os.path.expanduser("~/.claude/state/ajan-olcum.jsonl")


def transcript_ozeti(yol):
    o = {"girdi": 0, "onbellek_yazma": 0, "onbellek_okuma": 0, "cikti": 0, "tur": 0, "arac": 0, "model": "", "ilk": "", "son": ""}
    try:
        with open(yol, encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                ts = r.get("timestamp") or ""
                if ts:
                    o["ilk"] = o["ilk"] or ts
                    o["son"] = ts
                m = r.get("message") or {}
                if r.get("type") != "assistant" or not isinstance(m, dict):
                    continue
                u = m.get("usage") or {}
                o["girdi"] += u.get("input_tokens", 0) or 0
                o["onbellek_yazma"] += u.get("cache_creation_input_tokens", 0) or 0
                o["onbellek_okuma"] += u.get("cache_read_input_tokens", 0) or 0
                o["cikti"] += u.get("output_tokens", 0) or 0
                o["tur"] += 1
                o["model"] = m.get("model") or o["model"]
                o["arac"] += sum(1 for c in (m.get("content") or []) if isinstance(c, dict) and c.get("type") == "tool_use")
    except OSError:
        return None
    return o


def kaydet():
    d = json.load(sys.stdin)
    kayit = {"zaman": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "dizin": d.get("cwd", ""),
             "ajan": d.get("agent_type") or "?", "ajan_kimlik": d.get("agent_id") or "", "oturum": d.get("session_id", "")}
    yol = d.get("agent_transcript_path") or ""
    t = transcript_ozeti(yol) if yol else None
    if t:
        try:
            a = datetime.fromisoformat(t["ilk"].replace("Z", "+00:00")); b = datetime.fromisoformat(t["son"].replace("Z", "+00:00"))
            kayit["sure_sn"] = int((b - a).total_seconds())
        except ValueError:
            pass
        for k in ("model", "tur", "arac", "girdi", "onbellek_yazma", "onbellek_okuma", "cikti"):
            kayit[k] = t[k]
    else:
        kayit["not"] = "transcript yok; alanlar: " + ",".join(sorted(d.keys()))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "a", encoding="utf-8") as f:
        f.write(json.dumps(kayit, ensure_ascii=False) + "\n")


def ozet(gun):
    sinir = (datetime.now() - timedelta(days=gun)).strftime("%Y-%m-%d")
    g = {}
    try:
        for line in open(OUT, encoding="utf-8"):
            r = json.loads(line)
            if r["zaman"][:10] < sinir:
                continue
            a = g.setdefault(r["ajan"], {"n": 0, "cikti": 0, "taze": 0, "okuma": 0, "sure": 0, "arac": 0})
            a["n"] += 1; a["cikti"] += r.get("cikti", 0); a["taze"] += r.get("girdi", 0) + r.get("onbellek_yazma", 0)
            a["okuma"] += r.get("onbellek_okuma", 0); a["sure"] += r.get("sure_sn", 0); a["arac"] += r.get("arac", 0)
    except OSError:
        print("Henüz kayıt yok."); return
    print(f"Son {gun} gün · ajan başına ortalama (bin token)")
    print(f"{'ajan':22}{'iş':>4}{'çıktı':>8}{'taze girdi':>12}{'önbellek':>10}{'süre dk':>9}{'araç':>6}")
    for ad, a in sorted(g.items(), key=lambda x: -x[1]["n"]):
        n = a["n"]
        print(f"{ad:22}{n:>4}{a['cikti']/n/1000:>8.1f}{a['taze']/n/1000:>12.1f}{a['okuma']/n/1000:>10.1f}{a['sure']/n/60:>9.1f}{a['arac']/n:>6.0f}")


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1 and sys.argv[1] == "ozet":
            ozet(int(sys.argv[2]) if len(sys.argv) > 2 else 30)
        else:
            kaydet()
    except Exception:
        pass
    sys.exit(0)
