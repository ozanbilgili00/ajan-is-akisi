---
tür: üretilmiş-parça
kaynak: Kurallar/Üretim Kontrolü.md
kaynak-sürüm: 1.3
kaynak-özet: b6bdd028b3e2
---

# Üretim Kontrolü: Araç

> **Elle düzenlenmez.** Bu dosya `Kurallar/Üretim Kontrolü.md` kaynağından `~/.claude/hooks/uretim_bol.py` ile üretilir; değişiklik kaynağa yapılır, parçalar oturum başında kendiliğinden yenilenir.
>
> **Kimler okur:** CLI, kütüphane, MCP sunucusu, betik, eklenti (`ARAÇ`).
> **Nasıl okunur:** tamamını değil. Önce dizine bak; fazın kontrol kapısındaki kimliklerin metnini aşağıda bul. Profil, önem, aşama ve fazlara yayma kuralları [[Kurallar/Üretim Kontrolü/Yöntem|Yöntem]] notunda.


39 madde. Her kademenin başlığı kimin için olduğunu söyler; projene uymayan kademeyi atla.


## Dizin


**Kademe A · Her araç** (39 madde)

| Kimlik | Madde | Önem | Zaman | Profil |
|---|---|---|---|---|
| A-01 | Git ve uzak yedek | 🔴 | 🏁 | Hepsi |
| A-02 | `.gitignore` doğru | 🟠 | 🏁 | Hepsi |
| A-03 | Kilit dosyası (lockfile) ve sürüm sabitleme | 🟠 | 🏁 | Hepsi |
| A-04 | README | 🟡 | 🚀 | Hepsi |
| A-05 | Dal ve commit düzeni | 🟢 | 📈 | Hepsi |
| B-01 | Ortam değişkenleri ve yapılandırma ayrımı | 🔴 | 🏁 | BULUT WEB-S WEB-API OYUN ARAÇ YZ |
| B-05 | Debug kodunun prod'a sızmaması | 🟠 | 🚀 | Hepsi |
| C-01 | Sürekli entegrasyon (CI) | 🟠 | 🚀 | Hepsi |
| C-02 | Sürekli dağıtım (CD) | 🟡 | 📈 | WEB-S WEB-API BULUT ARAÇ |
| C-03 | Tekrarlanabilir build | 🟡 | 🚀 | Hepsi |
| C-06 | Sürümleme ve CHANGELOG | 🟡 | 🚀 | Hepsi |
| D-01 | Birim testleri | 🟠 | 🚀 | Hepsi |
| D-05 | Lint ve biçimlendirme | 🟡 | 🏁 | Hepsi |
| D-06 | Tip güvenliği ve derleyici uyarıları | 🟠 | 🏁 | Hepsi |
| D-07 | Statik analiz ve güvenlik taraması | 🟡 | 🚀 | Hepsi |
| D-09 | Kod incelemesi | 🟢 | 📈 | Hepsi |
| F-01 | Sır taraması (git geçmişi dahil) | 🔴 | 🏁 | Hepsi |
| F-03 | Enjeksiyon (SQL / NoSQL / komut) | 🔴 | 🏁 | WEB-API ARAÇ |
| F-11 | Bağımlılık güvenliği | 🟠 | 🚀 | Hepsi |
| F-13 | Şifreleme (aktarımda ve depoda) | 🟠 | 🏁 | Hepsi |
| F-15 | Asgari yetki (least privilege) | 🟡 | 🚀 | BULUT WEB-API ARAÇ |
| G-04 | Veri minimizasyonu ve hassas veri | 🟠 | 🏁 | Hepsi |
| G-07 | Lisanslar ve kullanım şartları | 🟠 | 🚀 | Hepsi |
| H-01 | Veri modeli tasarımı | 🟠 | 🏁 | Hepsi (veri tutan) |
| H-02 | Zaman damgaları ve saat dilimi | 🟠 | 🏁 | Hepsi (veri tutan) |
| H-03 | Migration (şema geçişi) | 🔴 | 🏁 | Hepsi (kalıcı veri tutan) |
| H-12 | Veri bütünlüğü doğrulaması | 🟡 | 🚀 | Hepsi (veri tutan) |
| J-01 | Performans bütçesi | 🟡 | 🚀 | Hepsi |
| J-05 | Bellek ve sızıntı | 🟠 | 🚀 | YEREL BULUT OYUN ARAÇ |
| K-01 | Timeout | 🟠 | 🏁 | Hepsi (ağ kullanan) |
| L-01 | Yapılandırılmış loglama | 🟡 | 🚀 | Hepsi |
| L-02 | Loglarda kişisel veri / sır yok | 🔴 | 🏁 | Hepsi |
| M-04 | Graceful shutdown | 🟢 | 📈 | WEB-API ARAÇ |
| N-02 | Yerelleştirme ve Türkçe'ye özgü sorunlar | 🟠 | 🏁 | Hepsi (kullanıcıya metin gösteren) |
| N-06 | Duyarlı (responsive) düzen ve cihaz çeşitliliği | 🟡 | 🚀 | Hepsi (UI olan) |
| O-07 | macOS'e özgü | 🟡 | 🚀 | YEREL ARAÇ |
| R-04 | Bağımlılık güncelleme | 🟡 | 📈 | Hepsi |
| R-07 | Teknik borç kaydı | 🟢 | 📈 | Hepsi |
| U-11 | Hata mesajı yok veya anlamsız | 🟠 | 🚀 | Hepsi (UI olan) |

---

## Kademe A · Her araç

### A. Repo ve kaynak kontrolü

#### A-01 · Git ve uzak yedek · 🔴 · 🏁 · Hepsi
- **Ne/Neden:** Kod git'te değilse veya sadece tek bir diskte duruyorsa disk arızası her şeyi siler. Geri dönüş yapılamaz.
- **Kontrol:** `git rev-parse --is-inside-work-tree`, `git remote -v`, son push tarihi (`git log origin/HEAD -1 --format=%cd`).
- **Geçer:** Git var, uzak repo (GitHub vb.) var, ana dal son 1-2 haftada push edilmiş.

#### A-02 · `.gitignore` doğru · 🟠 · 🏁 · Hepsi
- **Ne/Neden:** Build çıktısı, `node_modules`, `DerivedData`, `Library/` (Unity), `.env`, `*.p8`, `GoogleService-Info.plist` (gerekiyorsa) repoya girmemeli.
- **Kontrol:** `.gitignore` içeriği; `git ls-files | grep -iE '\.env|\.p8|\.p12|\.pem|\.key|node_modules|DerivedData|xcuserdata|/Library/|/Temp/'`.
- **Geçer:** Hassas veya üretilen dosya izlenmiyor.

#### A-03 · Kilit dosyası (lockfile) ve sürüm sabitleme · 🟠 · 🏁 · Hepsi
- **Ne/Neden:** Aynı kod, farklı makinede farklı bağımlılık sürümüyle derlenip bozulmamalı.
- **Kontrol:** `package-lock.json` / `pnpm-lock.yaml` / `yarn.lock`, `Package.resolved`, `Packages/packages-lock.json` repoda mı; `package.json` içinde `*` veya `latest` var mı.
- **Geçer:** Kilit dosyası commit'li, joker sürüm yok.

#### A-04 · README · 🟡 · 🚀 · Hepsi
- **Ne/Neden:** Altı ay sonra sen veya bir ajan projeyi sıfırdan çalıştırabilmeli.
- **Kontrol:** README'de: ne olduğu, gereksinimler, kurulum, çalıştırma, test, ortam değişkenleri listesi, dağıtım.
- **Geçer:** Temiz bir makinede README'yi takip ederek proje çalışır.

#### A-05 · Dal ve commit düzeni · 🟢 · 📈 · Hepsi
- **Ne/Neden:** Ana dal her zaman çalışır durumda olmalı; anlamlı commit mesajları geri dönmeyi kolaylaştırır.
- **Kontrol:** `git log --oneline -20`; ana dala doğrudan kırık commit atılıyor mu; branch protection (GitHub).
- **Geçer:** Ana dal derleniyor; commit mesajları ne yapıldığını söylüyor.

### B. Ortam ve yapılandırma

#### B-01 · Ortam değişkenleri ve yapılandırma ayrımı · 🔴 · 🏁 · BULUT WEB-S WEB-API OYUN ARAÇ YZ
- **Ne/Neden:** Ayar ve sırlar koddan ayrı olmalı; dev/staging/prod farklı değerlerle çalışabilmeli.
- **Kontrol:** `.env.example` var mı; kodda sabit URL/anahtar (`grep -rnE 'https?://[^"]*(api|prod)|sk_live|AIza|apiKey\s*[:=]'`); Xcode'da `.xcconfig` veya build configuration kullanımı; Vite'ta sadece `VITE_` önekli değişkenlerin istemciye gittiğinin farkında olunması.
- **Geçer:** Tüm ayarlar tek yerden okunuyor; `.env.example` güncel; prod sırrı istemci paketine girmiyor.

#### B-05 · Debug kodunun prod'a sızmaması · 🟠 · 🚀 · Hepsi
- **Ne/Neden:** Test menüleri, sahte veri, `print`/`console.log` ile hassas veri, devre dışı güvenlik kontrolleri yayına çıkmamalı.
- **Kontrol:** `grep -rnE '#if DEBUG|isDebug|TODO|FIXME|HACK|console\.log|print\('`; debug-only kodun `#if DEBUG` veya `import.meta.env.DEV` ile korunması.
- **Geçer:** Release derlemesinde debug davranışı yok.

### C. CI/CD ve teslimat

#### C-01 · Sürekli entegrasyon (CI) · 🟠 · 🚀 · Hepsi
- **Ne/Neden:** Her push'ta derleme + test + lint otomatik koşmalı. "Bende çalışıyordu" sorununu bitirir.
- **Kontrol:** `.github/workflows/`, Xcode Cloud, Vercel build; hangi adımlar koşuyor.
- **Geçer:** Push/PR'da en az derleme ve testler otomatik çalışıyor, kırmızıysa birleştirme yapılmıyor.

#### C-02 · Sürekli dağıtım (CD) · 🟡 · 📈 · WEB-S WEB-API BULUT ARAÇ
- **Ne/Neden:** Dağıtım elle ve ezbere yapılırsa adım unutulur.
- **Kontrol:** Vercel otomatik deploy, `firebase deploy` script'i, TestFlight'a otomatik yükleme (fastlane / Xcode Cloud), npm publish workflow.
- **Geçer:** Dağıtım tek komut veya otomatik; adımlar belgeli.

#### C-03 · Tekrarlanabilir build · 🟡 · 🚀 · Hepsi
- **Ne/Neden:** Aynı commit her zaman aynı çıktıyı üretmeli.
- **Kontrol:** Node/Xcode/Unity sürümü sabit mi (`.nvmrc`, `engines`, `.xcode-version`, `ProjectVersion.txt`); build yerel ortama bağımlı mı.
- **Geçer:** Araç sürümleri belgeli/sabit.

#### C-06 · Sürümleme ve CHANGELOG · 🟡 · 🚀 · Hepsi
- **Ne/Neden:** Hangi sürümde ne değişti, hangi sürüme geri dönülecek, bilinmeli.
- **Kontrol:** Semver (`MAJOR.MINOR.PATCH`), iOS'ta `CFBundleShortVersionString` + artan build numarası, git tag, `CHANGELOG.md`.
- **Geçer:** Her yayın etiketli ve değişiklikleri yazılı.

### D. Test ve kod kalitesi

#### D-01 · Birim testleri · 🟠 · 🚀 · Hepsi
- **Ne/Neden:** İş mantığı (hesaplamalar, tarih işlemleri, dönüştürücüler, kurallar) testlenmeli; en çok hata buradan çıkar.
- **Kontrol:** Test hedefi var mı (`*Tests/`, `*.test.ts`, Unity Test Runner); testler geçiyor mu (çalıştır); kritik mantık (ödeme, döngü hesabı, namaz vakti, puanlama vb.) kapsanmış mı.
- **Geçer:** Kritik iş mantığının testi var ve yeşil.

#### D-05 · Lint ve biçimlendirme · 🟡 · 🏁 · Hepsi
- **Ne/Neden:** Tutarlı kod, erken hata yakalama.
- **Kontrol:** ESLint/Prettier, SwiftLint/swift-format, C# analyzers; CI'da koşuyor mu.
- **Geçer:** Lint yapılandırılmış ve sıfır hata.

#### D-06 · Tip güvenliği ve derleyici uyarıları · 🟠 · 🏁 · Hepsi
- **Ne/Neden:** Uyarılar gelecekteki hataların habercisi. Swift 6 strict concurrency, TypeScript `strict`.
- **Kontrol:** `tsconfig.json` → `"strict": true`; `any` sayısı; Swift Language Version 6 / strict concurrency; derlemede uyarı sayısı; Swift'te `try!`, `!` force unwrap, `fatalError` sayısı.
- **Geçer:** Strict mod açık, uyarı yok veya bilinçli olarak bastırılmış; kullanıcı verisine bağlı force unwrap yok.

#### D-07 · Statik analiz ve güvenlik taraması · 🟡 · 🚀 · Hepsi
- **Kontrol:** Xcode Analyze, `npm audit`, CodeQL, Semgrep, gitleaks (yerel çalıştır).
- **Geçer:** Yüksek/kritik bulgu yok veya kabul edilmiş.

#### D-09 · Kod incelemesi · 🟢 · 📈 · Hepsi
- **Ne/Neden:** Tek kişilik projede bile büyük değişiklikten önce `/code-review` veya ikinci bir göz.
- **Geçer:** Kritik değişiklikler incelemeden geçiyor.

### F. API ve uygulama güvenliği

#### F-01 · Sır taraması (git geçmişi dahil) · 🔴 · 🏁 · Hepsi
- **Ne/Neden:** Silinen anahtar git geçmişinde yaşamaya devam eder.
- **Kontrol:** `gitleaks detect` veya `git log -p | grep -nE 'AKIA[0-9A-Z]{16}|sk_(live|test)_|sk-ant-|sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{35}|-----BEGIN (RSA |EC )?PRIVATE KEY|ghp_[A-Za-z0-9]{36}|xox[bp]-'`. Bulunanları **maskele**.
- **Düzeltme sırası (sır bulunursa):** 1) Anahtarı sağlayıcıda **iptal et ve yenisini üret (rotate)**. 2) Yeni anahtarı `.env` / secret manager'a (Vercel env, GitHub Secrets, Google Secret Manager, 1Password, iOS'ta sunucu tarafı) koy. 3) Koddan kaldır. 4) Gerekirse geçmişi `git filter-repo` / BFG ile temizle (**yıkıcı**, kullanıcı onayı şart; uzak repo zorla push gerektirir). Sadece 3. adım yetmez.
- **Geçer:** Geçmişte ve çalışma ağacında gizli anahtar yok; varsa iptal edilip yenilenmiş. Veritabanı kimlik bilgileri (DB credentials, connection string) kodda değil.

#### F-03 · Enjeksiyon (SQL / NoSQL / komut) · 🔴 · 🏁 · WEB-API ARAÇ
- **Kontrol:** String birleştirerek sorgu (`"SELECT ... " + x`, template literal ile SQL), `exec`/`spawn` ile kullanıcı girdisi, `eval`, `new Function`.
- **Geçer:** Parametreli sorgu/ORM; kabuk komutlarına girdi kaçışlı veya argüman dizisiyle veriliyor.

#### F-11 · Bağımlılık güvenliği · 🟠 · 🚀 · Hepsi
- **Kontrol:** `npm audit --omit=dev` (veya `pnpm audit`, `pip-audit`, `bundle audit`), GitHub Dependabot alerts, bilinen CVE'ler (osv.dev, `osv-scanner`), **kullanılmayan paketler** (`npx depcheck`, `knip`), terk edilmiş/az bilinen paketler, `postinstall` script'leri, typosquatting, lockfile kullanımı (A-03), düzenli güncelleme (R-04).
- **Geçer:** Yüksek/kritik açık yok; kullanılmayan paket yok; bağımlılık sayısı makul.

#### F-13 · Şifreleme (aktarımda ve depoda) · 🟠 · 🏁 · Hepsi
- **Kontrol:** Tüm ağ trafiği HTTPS/WSS (iOS ATS istisnası `NSAllowsArbitraryLoads` var mı); hassas yerel veri için iOS Data Protection (`.completeFileProtection`), Keychain; sağlık/regl/finans gibi hassas veride ekstra şifreleme ihtiyacı.
- **Geçer:** Düz HTTP yok; hassas veri korumalı sınıfta veya şifreli.

#### F-15 · Asgari yetki (least privilege) · 🟡 · 🚀 · BULUT WEB-API ARAÇ
- **Kontrol:** Servis hesaplarının yetkisi (Firebase Admin SDK her yerde mi kullanılıyor), API anahtarı kısıtlamaları (Google Cloud key restrictions: bundle ID / HTTP referrer), MCP sunucusunun dosya sistemi erişim kapsamı.
- **Geçer:** Her anahtar/hesap sadece ihtiyacı kadar yetkili.

### G. Gizlilik ve yasal uyum

#### G-04 · Veri minimizasyonu ve hassas veri · 🟠 · 🏁 · Hepsi
- **Ne/Neden:** Gereksiz veri toplama risktir. Sağlık (regl döngüsü), konum, finans, çocuk verisi özel nitelikli veridir.
- **Kontrol:** Hangi veri toplanıyor, neden; hassas veri buluta gidiyor mu; analitik/crash araçlarına kişisel veri sızıyor mu.
- **Geçer:** Toplanan her verinin gerekçesi var; hassas veri cihazda veya şifreli.

#### G-07 · Lisanslar ve kullanım şartları · 🟠 · 🚀 · Hepsi
- **Kontrol:** Açık kaynak bağımlılık lisansları (GPL'in kapalı uygulamaya etkisi), font lisansları, Unity Asset Store/Sketchfab/Poly Haven model lisansları (CC-BY ise atıf), veri kaynakları (TMDB atıf zorunluluğu, kamu verisi kullanım şartları), görsel/ikon lisansları, yapay zekâ ile üretilmiş içerik.
- **Geçer:** Her dış varlığın lisansı biliniyor; atıf gerekenler "Hakkında/Teşekkürler" ekranında.

### H. Veri ve veritabanı

#### H-01 · Veri modeli tasarımı · 🟠 · 🏁 · Hepsi (veri tutan)
- **Kontrol:** Benzersiz kimlikler (UUID), ilişkiler, zorunlu alanlar, tekrarlı veri (denormalizasyon bilinçli mi), şema belgesi.
- **Geçer:** Model belgeli ve tutarlı.

#### H-02 · Zaman damgaları ve saat dilimi · 🟠 · 🏁 · Hepsi (veri tutan)
- **Ne/Neden:** Tarihler UTC saklanmalı, gösterirken yerel saate çevrilmeli. "Gün" kavramı (regl günü, namaz vakti, mesai günü) saat dilimi ve yaz saatiyle bozulur.
- **Kontrol:** `Date()` ile gün hesabı, `Calendar.current` kullanımı, JS `new Date('YYYY-MM-DD')`'nin UTC yorumu, `createdAt`/`updatedAt` alanları.
- **Geçer:** Saklama UTC; gün hesapları açık takvim + saat dilimiyle; testli (gece yarısı, DST geçişi).

#### H-03 · Migration (şema geçişi) · 🔴 · 🏁 · Hepsi (kalıcı veri tutan)
- **Ne/Neden:** Uygulama güncellenince eski kullanıcının verisi **kaybolmamalı**. Bu en sık ve en acı veri kaybı nedenidir.
- **Kontrol:** SwiftData `VersionedSchema` + `SchemaMigrationPlan`; Core Data model sürümleri; SQL migration dosyaları (Prisma/Drizzle migrations) commit'li mi; localStorage'da şema sürüm anahtarı ve dönüştürücü; Unity kayıt dosyasında sürüm alanı; Firestore'da eski biçimli dokümanların okunabilmesi.
- **Geçer:** Şema sürümlü; eski sürümden yeni sürüme geçiş gerçek veriyle denenmiş; migration geri alınabilir veya önce yedek alınıyor.

#### H-12 · Veri bütünlüğü doğrulaması · 🟡 · 🚀 · Hepsi (veri tutan)
- **Kontrol:** Bozuk/eksik veri okununca uygulama çöküyor mu (decode hatası → `try?` ile sessiz kayıp mı, kullanıcıya bilgi mi); localStorage'ın elle bozulması; JSON şema doğrulaması.
- **Geçer:** Bozuk veri uygulamayı çökertmiyor ve sessizce silinmiyor.

### J. Performans ve ölçek

#### J-01 · Performans bütçesi · 🟡 · 🚀 · Hepsi
- **Ne/Neden:** "Hızlı" ölçülebilir olmalı: açılış süresi, ilk etkileşim, API p95 gecikmesi, FPS.
- **Geçer:** Hedef sayılar yazılı ve ölçülüyor.

#### J-05 · Bellek ve sızıntı · 🟠 · 🚀 · YEREL BULUT OYUN ARAÇ
- **Kontrol:** Retain cycle (`[weak self]`), kapanmayan observer/timer/listener (Firestore `addSnapshotListener` kaldırılıyor mu), Leaks (Xcode MCP `detect_leaks`, `profile_memory`); Node'da büyüyen bellek; Unity'de GC baskısı.
- **Geçer:** Uzun kullanımda bellek sabit; sızıntı yok.

### K. Asenkron işler, kuyruklar ve gerçek zamanlı iletişim

#### K-01 · Timeout · 🟠 · 🏁 · Hepsi (ağ kullanan)
- **Ne/Neden:** Timeout'suz istek sonsuza kadar bekler ve UI'yi/kaynakları kilitler.
- **Kontrol:** `URLSession` `timeoutIntervalForRequest`, `fetch` + `AbortController`, DB sorgu timeout'u, harici API çağrıları.
- **Geçer:** Her dış çağrının makul bir timeout'u var.

### L. Gözlemlenebilirlik (loglama, izleme, alarm, hata takibi)

#### L-01 · Yapılandırılmış loglama · 🟡 · 🚀 · Hepsi
- **Kontrol:** iOS: `os.Logger` (subsystem/category), `print` yerine. Sunucu: JSON log, seviye (debug/info/warn/error), istek kimliği (request ID). Log yeterli bağlam içeriyor mu.
- **Geçer:** Bir hatayı loglardan geriye doğru izleyebiliyorsun.

#### L-02 · Loglarda kişisel veri / sır yok · 🔴 · 🏁 · Hepsi
- **Kontrol:** Şunlar **asla** loglanmamalı: token'lar (access/refresh/session), şifreler, API anahtarları, `Authorization` / `Cookie` başlıkları, ödeme bilgileri. Mümkün olduğunca maskele: e-posta (`o***@gmail.com`), telefon, sağlık verisi, konum. Tüm istek/yanıt gövdesini olduğu gibi loglayan middleware var mı; `os.Logger` için `privacy: .private`; hata takip araçlarına (Sentry/Crashlytics) giden "breadcrumb" ve istek başlıkları (Sentry `sendDefaultPii: false`, `beforeSend` ile temizleme).
- **Geçer:** Loglarda sır yok; kişisel veri maskeli.

### M. Dayanıklılık ve felaket kurtarma

#### M-04 · Graceful shutdown · 🟢 · 📈 · WEB-API ARAÇ
- **Kontrol:** `SIGTERM` gelince yeni istek almayı bırakıp mevcutları bitirme; DB bağlantılarını kapatma; MCP/CLI süreçlerinde temiz çıkış.
- **Geçer:** Kapanırken yarım iş/bozuk veri kalmıyor.

### N. Kullanıcı deneyimi ve erişilebilirlik

#### N-02 · Yerelleştirme ve Türkçe'ye özgü sorunlar · 🟠 · 🏁 · Hepsi (kullanıcıya metin gösteren)
- **Kontrol:** Metinler String Catalog (`Localizable.xcstrings`) / i18n dosyasında mı, kodda sabit mi; tarih/sayı/para biçimi `Locale` ile mi (`1.234,56 ₺`); çoğul kuralları; **Türkçe İ/ı sorunu** (`"i".uppercased()` → `"I"` değil `"İ"`; `toLocaleUpperCase('tr-TR')`, `uppercased(with: Locale(identifier: "tr_TR"))`; büyük/küçük harf duyarsız arama ve sıralamada `localizedStandardCompare`/`Intl.Collator('tr')`); dosya adı ve URL'de Türkçe karakter; uzun metinlerde (Almanca vb.) taşma.
- **Geçer:** Metinler yerelleştirme altyapısında; Türkçe büyük/küçük harf ve sıralama doğru.

#### N-06 · Duyarlı (responsive) düzen ve cihaz çeşitliliği · 🟡 · 🚀 · Hepsi (UI olan)
- **Kontrol:** Web: 320 px genişlikte yatay kaydırma yok, dokunmatik hedefler. iOS: en küçük iPhone (SE), en büyük, iPad (destekleniyorsa), yatay mod, Dynamic Island/çentik, güvenli alanlar. Oyun: farklı en-boy oranları, çentik.
- **Geçer:** Desteklenen en küçük ve en büyük ekranda düzen bozulmuyor.

### O. Platform: iOS / macOS

#### O-07 · macOS'e özgü · 🟡 · 🚀 · YEREL ARAÇ
- **Kontrol:** Sandbox ve entitlement'lar, notarization, Hardened Runtime, erişilebilirlik/ekran kaydı gibi TCC izinleri, menü çubuğu uygulamasında giriş sırasında başlatma (`SMAppService`), Sparkle/güncelleme mekanizması (Mac App Store dışı ise).
- **Geçer:** Notarize edilmiş, izinleri açıklanmış, güncellenebilir.

### R. Operasyon, maliyet ve bakım

#### R-04 · Bağımlılık güncelleme · 🟡 · 📈 · Hepsi
- **Kontrol:** Dependabot/Renovate; `npm outdated`; büyük sürüm geride kalma; Xcode/Unity/Node LTS sürüm yaşam sonu.
- **Geçer:** Güncellemeler düzenli ve otomatik öneriliyor.

#### R-07 · Teknik borç kaydı · 🟢 · 📈 · Hepsi
- **Kontrol:** `TODO/FIXME/HACK` sayısı ve yaşı; bilinen geçici çözümler belgeli mi.
- **Geçer:** Bilinçli borç kayıtlı (`Yapılacaklar.md`), kod içi TODO'lar kontrol altında.

### U. Yayınlamadan önce düzeltilecek ürün sorunları (ilk deneyim)

> Profil: `MAĞAZA` (ve kullanıcıya açılan her `WEB-S`/`WEB-API`/`OYUN`). Bu sorunlar inceleme reddi değil ama **ilk gün kullanıcı kaybı** demektir. "Yayın hazırlığı" fazında, mümkünse daha önce "İlk deneyim" fazında çözülür.

#### U-11 · Hata mesajı yok veya anlamsız · 🟠 · 🚀 · Hepsi (UI olan)
- **Düzeltme:** Hatanın ne olduğunu ve kullanıcının **ne yapabileceğini** yaz ("Bağlantı kurulamadı. İnternetini kontrol edip tekrar dene." + Tekrar Dene butonu). "Bir sorun oluştu" tek başına yetmez; hata kodu gerekiyorsa küçük ikincil metin olarak (N-03, W-11).
- **Geçer:** Her hata mesajı bir sonraki adımı söylüyor.
