---
tür: üretilmiş-parça
kaynak: Kurallar/Üretim Kontrolü.md
kaynak-sürüm: 1.3
kaynak-özet: b6bdd028b3e2
---

# Üretim Kontrolü: Şablonlar ve Komutlar

> **Elle düzenlenmez.** Bu dosya `Kurallar/Üretim Kontrolü.md` kaynağından `~/.claude/hooks/uretim_bol.py` ile üretilir; değişiklik kaynağa yapılır, parçalar oturum başında kendiliğinden yenilenir.
>
> Kaynağın 4, 5 ve 6. bölümleri: proje kural dosyası şablonu, `Kontrol.md` şablonu ve salt okunur tarama komutları. Yalnız gerektiğinde okunur.

## 4. Proje kural dosyası şablonu

Ajan, değerlendirmeden sonra projenin kökünde `.claude/rules/uretim.md` dosyasını aşağıdaki şablonla yazar. Bu dosya **kısa** olmalıdır (~60-120 satır). Her oturumda yüklenir ve ajanların günlük kod yazarken uyacağı kalıcı kuralları içerir. Denetim sonuçları burada değil, Obsidian `Kontrol.md` dosyasında tutulur.

```markdown
# Üretim kuralları: <Proje Adı>

> Kaynak: ~/Desktop/hafıza/hafıza/Kurallar/Üretim Kontrolü.md (v1.0)
> Profil: <örn. BULUT + YZ> · Aşama: <Prototip/Beta/Yayında> · Son denetim: <YYYY-AA-GG>
> Denetim raporu: Obsidian → Projeler/<Ad>/Kontrol.md

## Bu projede geçerli olan maddeler
<Uygulanan maddelerin ID listesi, kategoriye göre tek satır: "Güvenlik: E-01 E-02 F-01 F-02 F-12 F-13 ...">

## Uygulanmayanlar ve gerekçe
<Tek satırda: "C-04 C-05 H-13 J-10 K-05 L-07 L-08: tek kullanıcılı, sunucusuz uygulama">

## Kod yazarken her zaman
<Projeye özel, somut, doğrulanabilir kurallar. Genel tavsiye değil. Örnekler:>
- Tarihleri UTC sakla; gün hesabını `Calendar` + kullanıcının saat dilimiyle yap (H-02).
- SwiftData modeline alan ekleyince yeni `VersionedSchema` + migration aşaması ekle, eski şemayla test et (H-03).
- Yeni Firestore koleksiyonu = `firestore.rules`'a sahiplik + şema kuralı + rules testi (F-12, D-02).
- Kullanıcıya görünen her metin `Localizable.xcstrings`'e (N-02).
- Her ağ çağrısında timeout ve kullanıcıya anlamlı hata durumu (K-01, N-03).
- Yeni izin = `Info.plist` açıklaması + `PrivacyInfo.xcprivacy` güncellemesi (G-02, G-03).

## Asla
- <örn. "İstemci koduna ücretli API anahtarı koyma (B-02)">
- <örn. "`try!`, kullanıcı verisine bağlı force unwrap yazma (D-06)">
- <örn. "Firestore rules'ta `if request.auth != null` tek başına yeterli değil (F-12)">
- <örn. "Loglara kişisel veya sağlık verisi yazma (L-02)">

## Faz kapıları
Fazlara dağılım `Plan.md`'de ("Kontrol kapısı" satırları). Her özellik fazında Özellik Bitti Tanımı (ana dosya §8.2) geçerlidir.

## Yayından önce kontrol
<Bu proje için 🔴/🟠 maddelerin kısa kontrol listesi; MAĞAZA ise W kırma testi (W-01 … W-30) ve T listesi>
- [ ] Testler yeşil (D-01)
- [ ] Migration eski sürüm verisiyle denendi (H-03)
- [ ] ...

## Komutlar
<Projeye özel: test, lint, build, sır taraması komutları>
```

**Şablon kuralları:**
- "Kod yazarken her zaman" ve "Asla" maddeleri **projenin gerçek koduna** göre yazılır (gerçek dosya, framework ve fonksiyon adlarıyla). Ana dosyadan genel cümle kopyalanmaz.
- Proje profili veya aşaması değişince (örn. backend eklendi, yayına çıkıldı) dosya yeniden üretilir.
- Proje kökünde zaten `CLAUDE.md` varsa ona tek satır eklenir: `Üretim kuralları: .claude/rules/uretim.md`.

## 5. Denetim raporu şablonu (Obsidian `Projeler/<Ad>/Kontrol.md`)

```markdown
---
denetim: YYYY-AA-GG
profil: [BULUT, YZ]
aşama: Beta
kaynak-sürüm: 1.0
---

# Üretim Kontrolü: <Ad>

## Özet
- ✅ <n> · ⚠️ <n> · ❌ <n> · ❓ <n> · ➖ <n>
- Yayın engeli (🔴 ❌/⚠️): <n>
- İlk yapılacaklar:
  1. <ID>: <tek cümle> (<dosya:satır>)
  2. ...

## Bulgular
| ID | Madde | Önem | Durum | Kanıt / Not |
|---|---|---|---|---|
| F-12 | Firebase kuralları | 🔴 | ❌ | `firestore.rules:4` `allow read: if request.auth != null` → herkes herkesi okuyor |
| H-03 | Migration | 🔴 | ⚠️ | VersionedSchema var, eski sürüm verisiyle test yok |
| C-05 | Kubernetes | 🟢 | ➖ | Tek servis, serverless |
| ... | | | | |

## Değişiklik geçmişi
- YYYY-AA-GG: ilk denetim
```

Kurallar:
- Tabloda **tüm** maddeler yer alır (➖ olanlar dahil), böylece neyin bilinçli olarak atlandığı görünür.
- Sonraki denetimlerde tablo güncellenir, değişen maddeler "Değişiklik geçmişi"ne tek satırla yazılır.
- 🔴/🟠 ve ❌/⚠️ maddeler `Yapılacaklar.md` dosyasında `[Üretim ID]` önekiyle takip edilir; çözülünce hem tablo hem görev güncellenir.

## 6. Hızlı tarama komutları (salt-okunur)

Ajan bunları proje kökünde çalıştırabilir. Çıktıdaki sırları **rapora yazmadan önce maskele**.

```bash
# Repo durumu
git rev-parse --is-inside-work-tree && git remote -v && git log -1 --format='%cd %s'

# İzlenen hassas dosyalar
git ls-files | grep -iE '\.env($|\.)|\.p8$|\.p12$|\.pem$|\.key$|serviceAccount|credentials'

# Çalışma ağacında olası sırlar (değeri yazdırmadan sadece dosya:satır)
grep -rnoE 'sk_(live|test)_|sk-ant-|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35}|ghp_[A-Za-z0-9]{36}|-----BEGIN [A-Z ]*PRIVATE KEY' \
  --exclude-dir={node_modules,.git,dist,build,DerivedData,Library} . | cut -d: -f1,2 | sort -u

# Git geçmişinde sırlar (gitleaks kuruluysa tercih et)
command -v gitleaks >/dev/null && gitleaks detect --no-banner --redact

# Debug kalıntıları ve borç
grep -rnE 'console\.log|print\(|debugPrint|TODO|FIXME|HACK' --include=*.{ts,tsx,js,jsx,swift,cs} \
  --exclude-dir={node_modules,.git,dist,build,Library} . | wc -l

# Riskli Swift kalıpları
grep -rnE 'try!|fatalError\(|as! ' --include=*.swift . | grep -v Tests | head -50

# Riskli web kalıpları
grep -rnE 'dangerouslySetInnerHTML|innerHTML\s*=|eval\(|new Function\(' --include=*.{ts,tsx,js,jsx} \
  --exclude-dir={node_modules,dist} .

# Firebase kuralları: geniş izinler
grep -nE 'if true|request\.auth != null;' firestore.rules storage.rules 2>/dev/null

# Bağımlılık açıkları
[ -f package.json ] && npm audit --omit=dev --audit-level=high

# iOS gizlilik ve izinler
find . -name 'PrivacyInfo.xcprivacy' -not -path '*/DerivedData/*' -not -path '*/.build/*'
grep -rn 'NSAllowsArbitraryLoads\|UsageDescription' --include=Info.plist . 2>/dev/null
grep -rln 'VersionedSchema\|SchemaMigrationPlan' --include=*.swift . 2>/dev/null

# TypeScript strict
grep -n '"strict"' tsconfig*.json 2>/dev/null
```
