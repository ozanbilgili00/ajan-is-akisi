# Ajan iş akışı

Claude Code'da ana oturumun (Opus), alt ajanların (Haiku, Sonnet) ve Gemini'nin iş bölümünü, projeye göre hattı ve güvenlik kapılarını tanımlayan kurallar; bunları zorlayan kancalar ve ajan tanımları.

> Kişisel kurulumdan çıkarıldı: kurallarda "Ozan" kullanıcı adıdır, yollar `~/Desktop/hafıza/hafıza` (Obsidian vault) ve `~/.claude` altındadır. Başka makineye alırken yolları uyarla.

## İçerik

| Klasör | Ne |
|---|---|
| `kurallar/Ajan İş Akışı.md` | Ana kural: roller, ajan açma kararı, Gemini şartları, iş tanımı şablonu, aksilikler |
| `kurallar/İş Akışı/` | Proje türüne göre hat (Web ve Sunucu, Apple, Oyun, Araç ve MCP, Araştırma ve Belge) ve **Güvenlik Hattı** (GS0-GS3) |
| `kurallar/Üretim Kontrolü.md` | 278 maddelik üretim kontrol listesinin kaynağı; tamamı okunmaz |
| `kurallar/Üretim Kontrolü/` | Kaynaktan üretilmiş tür parçaları (Web, Apple, Android, Oyun, Araç, ek modüller). Elle düzenlenmez |
| `ajanlar/` | `~/.claude/agents/` tanımları: `mekanik`, `uygulayici-haiku`, `uygulayici`, `test-yazari`, `guvenlik-denetcisi` |
| `kancalar/` | `guvenlik.py` (sır okuma ve kanca atlatmayı engeller, canlı yazmaları sordurur), `uretim_bol.py` (parçaları üretir), `olcum.py` (ajan ölçümü), `hafiza.py` (oturum başı bağlamı) |
| `sablonlar/` | İş tanımı, güvenlik notu, proje şablonu |
| `CLAUDE.md.ornek` | Kuralları oturumlara bağlayan genel talimat örneği |

## Kurulum (özet)

1. `kurallar/` → vault'taki `Kurallar/`, `sablonlar/` → `Şablonlar/`.
2. `ajanlar/*.md` → `~/.claude/agents/`, `kancalar/*.py` → `~/.claude/hooks/`.
3. `~/.claude/settings.json`: `PreToolUse` için `python3 ~/.claude/hooks/guvenlik.py` (matcher: `Bash|Read|Edit|Write|NotebookEdit|Grep|mcp__supabase__.*|mcp__plugin_firebase_firebase__.*|mcp__plugin_vercel_vercel__.*`), `SubagentStop` için `python3 ~/.claude/hooks/olcum.py kaydet`, `SessionStart` için `python3 ~/.claude/hooks/hafiza.py context`.
4. `CLAUDE.md.ornek` içeriğini `~/.claude/CLAUDE.md` dosyasına uyarla.
5. Gitleaks kurulu olmalı (`guvenlik.py` commit öncesi tarar).

`settings.json` bu depoda yoktur: izin listeleri kişiseldir.
