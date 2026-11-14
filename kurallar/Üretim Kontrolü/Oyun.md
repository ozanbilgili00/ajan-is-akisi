---
tür: üretilmiş-parça
kaynak: Kurallar/Üretim Kontrolü.md
kaynak-sürüm: 1.3
kaynak-özet: b6bdd028b3e2
---

# Üretim Kontrolü: Oyun

> **Elle düzenlenmez.** Bu dosya `Kurallar/Üretim Kontrolü.md` kaynağından `~/.claude/hooks/uretim_bol.py` ile üretilir; değişiklik kaynağa yapılır, parçalar oturum başında kendiliğinden yenilenir.
>
> **Kimler okur:** Unity ve diğer oyun motoru projeleri (`OYUN`). Platform maddeleri burada değil: iOS'a çıkıyorsa Apple.md içindeki O kategorisi, Android'e çıkıyorsa Android.md içindeki AN kategorisi de okunur.
> **Nasıl okunur:** tamamını değil. Önce dizine bak; fazın kontrol kapısındaki kimliklerin metnini aşağıda bul. Profil, önem, aşama ve fazlara yayma kuralları [[Kurallar/Üretim Kontrolü/Yöntem|Yöntem]] notunda.


69 madde. Her kademenin başlığı kimin için olduğunu söyler; projene uymayan kademeyi atla.


## Dizin


**Kademe A · Her oyun** (69 madde)

| Kimlik | Madde | Önem | Zaman | Profil |
|---|---|---|---|---|
| A-01 | Git ve uzak yedek | 🔴 | 🏁 | Hepsi |
| A-02 | `.gitignore` doğru | 🟠 | 🏁 | Hepsi |
| A-03 | Kilit dosyası (lockfile) ve sürüm sabitleme | 🟠 | 🏁 | Hepsi |
| A-04 | README | 🟡 | 🚀 | Hepsi |
| A-05 | Dal ve commit düzeni | 🟢 | 📈 | Hepsi |
| B-01 | Ortam değişkenleri ve yapılandırma ayrımı | 🔴 | 🏁 | BULUT WEB-S WEB-API OYUN ARAÇ YZ |
| B-04 | Feature flag | 🟢 | 📈 | BULUT WEB-API OYUN |
| B-05 | Debug kodunun prod'a sızmaması | 🟠 | 🚀 | Hepsi |
| C-01 | Sürekli entegrasyon (CI) | 🟠 | 🚀 | Hepsi |
| C-03 | Tekrarlanabilir build | 🟡 | 🚀 | Hepsi |
| C-06 | Sürümleme ve CHANGELOG | 🟡 | 🚀 | Hepsi |
| D-01 | Birim testleri | 🟠 | 🚀 | Hepsi |
| D-05 | Lint ve biçimlendirme | 🟡 | 🏁 | Hepsi |
| D-06 | Tip güvenliği ve derleyici uyarıları | 🟠 | 🏁 | Hepsi |
| D-07 | Statik analiz ve güvenlik taraması | 🟡 | 🚀 | Hepsi |
| D-09 | Kod incelemesi | 🟢 | 📈 | Hepsi |
| E-01 | Kimlik doğrulama (authentication) | 🔴 | 🏁 | BULUT WEB-API OYUN |
| F-01 | Sır taraması (git geçmişi dahil) | 🔴 | 🏁 | Hepsi |
| F-11 | Bağımlılık güvenliği | 🟠 | 🚀 | Hepsi |
| F-13 | Şifreleme (aktarımda ve depoda) | 🟠 | 🏁 | Hepsi |
| F-17 | İstemci/uygulama bütünlüğü | 🟢 | 📈 | BULUT OYUN |
| G-01 | Gizlilik politikası | 🔴 | 🚀 | BULUT WEB-API OYUN YZ (mağazaya çıkan her uygulama) |
| G-02 | Apple gizlilik bildirimleri | 🔴 | 🚀 | YEREL BULUT OYUN |
| G-03 | İzin açıklamaları | 🟠 | 🚀 | YEREL BULUT OYUN |
| G-04 | Veri minimizasyonu ve hassas veri | 🟠 | 🏁 | Hepsi |
| G-07 | Lisanslar ve kullanım şartları | 🟠 | 🚀 | Hepsi |
| G-08 | Yaş sınırı ve içerik | 🟡 | 🚀 | BULUT WEB-API OYUN |
| H-01 | Veri modeli tasarımı | 🟠 | 🏁 | Hepsi (veri tutan) |
| H-02 | Zaman damgaları ve saat dilimi | 🟠 | 🏁 | Hepsi (veri tutan) |
| H-03 | Migration (şema geçişi) | 🔴 | 🏁 | Hepsi (kalıcı veri tutan) |
| H-08 | Tutarlılık: transaction ve race condition | 🟠 | 🏁 | BULUT WEB-API OYUN |
| H-12 | Veri bütünlüğü doğrulaması | 🟡 | 🚀 | Hepsi (veri tutan) |
| I-03 | Görsel ve medya optimizasyonu | 🟡 | 🚀 | BULUT WEB-S WEB-API OYUN |
| J-01 | Performans bütçesi | 🟡 | 🚀 | Hepsi |
| J-04 | Ana thread ve takılmalar | 🟠 | 🚀 | YEREL BULUT OYUN |
| J-05 | Bellek ve sızıntı | 🟠 | 🚀 | YEREL BULUT OYUN ARAÇ |
| J-06 | Enerji ve pil | 🟡 | 🚀 | YEREL BULUT OYUN |
| J-07 | Açılış süresi | 🟡 | 🚀 | YEREL BULUT OYUN |
| J-09 | Oyun performansı | 🟠 | 🚀 | OYUN |
| K-01 | Timeout | 🟠 | 🏁 | Hepsi (ağ kullanan) |
| K-02 | Retry ve üstel geri çekilme | 🟠 | 🚀 | BULUT WEB-API OYUN |
| K-07 | WebSocket / gerçek zamanlı | 🟠 | 🚀 | BULUT WEB-API OYUN |
| K-08 | Bildirimler (push / yerel) | 🟡 | 🚀 | YEREL BULUT OYUN |
| L-01 | Yapılandırılmış loglama | 🟡 | 🚀 | Hepsi |
| L-02 | Loglarda kişisel veri / sır yok | 🔴 | 🏁 | Hepsi |
| L-03 | Hata takibi / crash raporlama | 🟠 | 🚀 | BULUT WEB-S WEB-API OYUN (YEREL için MetricKit/Xcode Organizer yeterli olabilir) |
| L-09 | Ürün analitiği | 🟢 | 📈 | BULUT WEB-S WEB-API OYUN |
| M-02 | Zorunlu güncelleme (mobil) | 🟠 | 🏁 | BULUT OYUN |
| M-03 | Kill switch | 🟡 | 🚀 | BULUT WEB-API OYUN YZ |
| N-01 | Erişilebilirlik | 🟠 | 🏁 | YEREL BULUT WEB-S WEB-API OYUN |
| N-02 | Yerelleştirme ve Türkçe'ye özgü sorunlar | 🟠 | 🏁 | Hepsi (kullanıcıya metin gösteren) |
| N-03 | Boş, yükleme ve hata durumları | 🟠 | 🚀 | YEREL BULUT WEB-S WEB-API OYUN |
| N-04 | İnternet yokken davranış | 🟠 | 🏁 | BULUT WEB-S WEB-API OYUN |
| N-06 | Duyarlı (responsive) düzen ve cihaz çeşitliliği | 🟡 | 🚀 | Hepsi (UI olan) |
| N-08 | Onboarding ve ilk kullanım | 🟡 | 🚀 | YEREL BULUT WEB-S WEB-API OYUN |
| N-10 | Haptik, ses ve hareket | 🟢 | 📈 | YEREL BULUT OYUN |
| Q-01 | Kayıt sistemi | 🔴 | 🏁 | OYUN |
| Q-02 | Çok oyunculu yetki modeli | 🔴 | 🏁 | OYUN (çevrimiçi) |
| Q-03 | Ağ performansı ve gecikme | 🟠 | 🚀 | OYUN (çevrimiçi) |
| Q-04 | Girdi ve kontroller | 🟡 | 🚀 | OYUN |
| Q-05 | Build ve asset yönetimi | 🟡 | 🚀 | OYUN |
| R-04 | Bağımlılık güncelleme | 🟡 | 📈 | Hepsi |
| R-07 | Teknik borç kaydı | 🟢 | 📈 | Hepsi |
| U-01 | Açılış 2 saniyeden uzun | 🟠 | 🚀 | MAĞAZA OYUN |
| U-06 | İlk değer anına (time-to-value) ulaşmak çok uzun | 🟠 | 🚀 | MAĞAZA WEB-S WEB-API OYUN |
| U-11 | Hata mesajı yok veya anlamsız | 🟠 | 🚀 | Hepsi (UI olan) |
| U-13 | Dokunma hedefleri küçük | 🟠 | 🚀 | MAĞAZA WEB-S WEB-API OYUN |
| U-18 | Uygulama boyutu 200 MB üstü | 🟡 | 🚀 | MAĞAZA OYUN |
| X-15 | İstemci tarafı güven testi | 🟠 | 🚀 | BULUT OYUN GELİR |

---

## Kademe A · Her oyun

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

#### B-04 · Feature flag · 🟢 · 📈 · BULUT WEB-API OYUN
- **Ne/Neden:** Yarım özelliği kapalı göndermek, sorunlu özelliği yeni sürüm çıkarmadan kapatmak.
- **Kontrol:** Remote Config, LaunchDarkly, kendi flag tablosu veya en azından derleme bayrağı.
- **Geçer:** Riskli özellikler uzaktan kapatılabiliyor.

#### B-05 · Debug kodunun prod'a sızmaması · 🟠 · 🚀 · Hepsi
- **Ne/Neden:** Test menüleri, sahte veri, `print`/`console.log` ile hassas veri, devre dışı güvenlik kontrolleri yayına çıkmamalı.
- **Kontrol:** `grep -rnE '#if DEBUG|isDebug|TODO|FIXME|HACK|console\.log|print\('`; debug-only kodun `#if DEBUG` veya `import.meta.env.DEV` ile korunması.
- **Geçer:** Release derlemesinde debug davranışı yok.

### C. CI/CD ve teslimat

#### C-01 · Sürekli entegrasyon (CI) · 🟠 · 🚀 · Hepsi
- **Ne/Neden:** Her push'ta derleme + test + lint otomatik koşmalı. "Bende çalışıyordu" sorununu bitirir.
- **Kontrol:** `.github/workflows/`, Xcode Cloud, Vercel build; hangi adımlar koşuyor.
- **Geçer:** Push/PR'da en az derleme ve testler otomatik çalışıyor, kırmızıysa birleştirme yapılmıyor.

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

### E. Kimlik doğrulama ve yetkilendirme

#### E-01 · Kimlik doğrulama (authentication) · 🔴 · 🏁 · BULUT WEB-API OYUN
- **Ne/Neden:** "Bu kullanıcı kim?" Kendi şifre sistemini yazmak yerine kanıtlanmış sağlayıcı (Firebase Auth, Sign in with Apple, Auth.js, Clerk, Supabase Auth).
- **Kontrol:** Şifreler düz metin veya zayıf hash (MD5/SHA1) ile mi saklanıyor; localStorage'da "giriş" sadece istemci tarafı mı (bu **güvenlik değildir**, sadece kullanıcı arayüzüdür).
- **Geçer:** Kimlik sunucu tarafında doğrulanıyor; şifre varsa bcrypt/argon2; istemci tarafı sahte auth "güvenlik" diye sunulmuyor.

### F. API ve uygulama güvenliği

#### F-01 · Sır taraması (git geçmişi dahil) · 🔴 · 🏁 · Hepsi
- **Ne/Neden:** Silinen anahtar git geçmişinde yaşamaya devam eder.
- **Kontrol:** `gitleaks detect` veya `git log -p | grep -nE 'AKIA[0-9A-Z]{16}|sk_(live|test)_|sk-ant-|sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{35}|-----BEGIN (RSA |EC )?PRIVATE KEY|ghp_[A-Za-z0-9]{36}|xox[bp]-'`. Bulunanları **maskele**.
- **Düzeltme sırası (sır bulunursa):** 1) Anahtarı sağlayıcıda **iptal et ve yenisini üret (rotate)**. 2) Yeni anahtarı `.env` / secret manager'a (Vercel env, GitHub Secrets, Google Secret Manager, 1Password, iOS'ta sunucu tarafı) koy. 3) Koddan kaldır. 4) Gerekirse geçmişi `git filter-repo` / BFG ile temizle (**yıkıcı**, kullanıcı onayı şart; uzak repo zorla push gerektirir). Sadece 3. adım yetmez.
- **Geçer:** Geçmişte ve çalışma ağacında gizli anahtar yok; varsa iptal edilip yenilenmiş. Veritabanı kimlik bilgileri (DB credentials, connection string) kodda değil.

#### F-11 · Bağımlılık güvenliği · 🟠 · 🚀 · Hepsi
- **Kontrol:** `npm audit --omit=dev` (veya `pnpm audit`, `pip-audit`, `bundle audit`), GitHub Dependabot alerts, bilinen CVE'ler (osv.dev, `osv-scanner`), **kullanılmayan paketler** (`npx depcheck`, `knip`), terk edilmiş/az bilinen paketler, `postinstall` script'leri, typosquatting, lockfile kullanımı (A-03), düzenli güncelleme (R-04).
- **Geçer:** Yüksek/kritik açık yok; kullanılmayan paket yok; bağımlılık sayısı makul.

#### F-13 · Şifreleme (aktarımda ve depoda) · 🟠 · 🏁 · Hepsi
- **Kontrol:** Tüm ağ trafiği HTTPS/WSS (iOS ATS istisnası `NSAllowsArbitraryLoads` var mı); hassas yerel veri için iOS Data Protection (`.completeFileProtection`), Keychain; sağlık/regl/finans gibi hassas veride ekstra şifreleme ihtiyacı.
- **Geçer:** Düz HTTP yok; hassas veri korumalı sınıfta veya şifreli.

#### F-17 · İstemci/uygulama bütünlüğü · 🟢 · 📈 · BULUT OYUN
- **Kontrol:** Firebase App Check / App Attest; oyunlarda istemciye güvenilmemesi (skor, envanter sunucuda doğrulanır).
- **Geçer:** Sahte istemciler arka uca kolayca erişemiyor.

### G. Gizlilik ve yasal uyum

#### G-01 · Gizlilik politikası · 🔴 · 🚀 · BULUT WEB-API OYUN YZ (mağazaya çıkan her uygulama)
- **Ne/Neden:** App Store ve Google Play zorunlu kılar; KVKK aydınlatma metni gerekir.
- **Kontrol:** Erişilebilir URL; uygulama içinden bağlantı; toplanan verilerle tutarlılık.
- **Geçer:** Güncel politika var ve gerçek davranışla örtüşüyor.

#### G-02 · Apple gizlilik bildirimleri · 🔴 · 🚀 · YEREL BULUT OYUN
- **Kontrol:** `PrivacyInfo.xcprivacy` (required-reason API'leri: UserDefaults, dosya zaman damgası, disk alanı, sistem açılış süresi), üçüncü parti SDK manifestleri, App Store Connect "App Privacy" etiketleri, ATT (`NSUserTrackingUsageDescription`) gerekiyorsa.
- **Geçer:** Manifest var ve kullanılan API'leri kapsıyor; etiketler doğru.

#### G-03 · İzin açıklamaları · 🟠 · 🚀 · YEREL BULUT OYUN
- **Kontrol:** `Info.plist` → `NS*UsageDescription` (konum, kamera, fotoğraf, bildirim, sağlık, mikrofon); metin neden istendiğini açıkça söylüyor mu; izin gerektiğinde mi isteniyor (açılışta topluca değil); reddedilince uygulama çalışmaya devam ediyor mu.
- **Geçer:** Her izin için anlamlı Türkçe/İngilizce açıklama; ret durumu ele alınmış.

#### G-04 · Veri minimizasyonu ve hassas veri · 🟠 · 🏁 · Hepsi
- **Ne/Neden:** Gereksiz veri toplama risktir. Sağlık (regl döngüsü), konum, finans, çocuk verisi özel nitelikli veridir.
- **Kontrol:** Hangi veri toplanıyor, neden; hassas veri buluta gidiyor mu; analitik/crash araçlarına kişisel veri sızıyor mu.
- **Geçer:** Toplanan her verinin gerekçesi var; hassas veri cihazda veya şifreli.

#### G-07 · Lisanslar ve kullanım şartları · 🟠 · 🚀 · Hepsi
- **Kontrol:** Açık kaynak bağımlılık lisansları (GPL'in kapalı uygulamaya etkisi), font lisansları, Unity Asset Store/Sketchfab/Poly Haven model lisansları (CC-BY ise atıf), veri kaynakları (TMDB atıf zorunluluğu, kamu verisi kullanım şartları), görsel/ikon lisansları, yapay zekâ ile üretilmiş içerik.
- **Geçer:** Her dış varlığın lisansı biliniyor; atıf gerekenler "Hakkında/Teşekkürler" ekranında.

#### G-08 · Yaş sınırı ve içerik · 🟡 · 🚀 · BULUT WEB-API OYUN
- **Kontrol:** Kullanıcı üretimli içerik varsa App Store Guideline 1.2 (raporlama, engelleme, filtre); yaş derecelendirmesi doğru mu.
- **Geçer:** Kullanıcı içeriği için şikâyet/engelleme mekanizması var.

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

#### H-08 · Tutarlılık: transaction ve race condition · 🟠 · 🏁 · BULUT WEB-API OYUN
- **Ne/Neden:** İki kişi aynı anda aynı veriyi değiştirince (sayaç, bakiye, stok, ortak liste) veri bozulmamalı.
- **Kontrol:** Firestore `runTransaction` / `FieldValue.increment`, SQL transaction, oku-değiştir-yaz kalıpları, optimistic locking.
- **Geçer:** Eşzamanlı yazma riski olan yerler atomik.

#### H-12 · Veri bütünlüğü doğrulaması · 🟡 · 🚀 · Hepsi (veri tutan)
- **Kontrol:** Bozuk/eksik veri okununca uygulama çöküyor mu (decode hatası → `try?` ile sessiz kayıp mı, kullanıcıya bilgi mi); localStorage'ın elle bozulması; JSON şema doğrulaması.
- **Geçer:** Bozuk veri uygulamayı çökertmiyor ve sessizce silinmiyor.

### I. Depolama, dosyalar ve CDN

#### I-03 · Görsel ve medya optimizasyonu · 🟡 · 🚀 · BULUT WEB-S WEB-API OYUN
- **Kontrol:** Yükleme öncesi yeniden boyutlandırma/sıkıştırma, modern formatlar (WebP/AVIF/HEIC), thumbnail, `loading="lazy"`, Unity texture sıkıştırma (ASTC).
- **Geçer:** Ham büyük görseller kullanıcıya gönderilmiyor.

### J. Performans ve ölçek

#### J-01 · Performans bütçesi · 🟡 · 🚀 · Hepsi
- **Ne/Neden:** "Hızlı" ölçülebilir olmalı: açılış süresi, ilk etkileşim, API p95 gecikmesi, FPS.
- **Geçer:** Hedef sayılar yazılı ve ölçülüyor.

#### J-04 · Ana thread ve takılmalar · 🟠 · 🚀 · YEREL BULUT OYUN
- **Kontrol:** Ana thread'de ağ/disk/JSON işlemi; SwiftUI'da `body` içinde pahalı hesap; büyük listelerde `LazyVStack`/`List`; Instruments Hangs/Time Profiler (Xcode MCP `profile_hangs`, `profile_swiftui`).
- **Geçer:** 250 ms üstü takılma yok; kaydırma akıcı.

#### J-05 · Bellek ve sızıntı · 🟠 · 🚀 · YEREL BULUT OYUN ARAÇ
- **Kontrol:** Retain cycle (`[weak self]`), kapanmayan observer/timer/listener (Firestore `addSnapshotListener` kaldırılıyor mu), Leaks (Xcode MCP `detect_leaks`, `profile_memory`); Node'da büyüyen bellek; Unity'de GC baskısı.
- **Geçer:** Uzun kullanımda bellek sabit; sızıntı yok.

#### J-06 · Enerji ve pil · 🟡 · 🚀 · YEREL BULUT OYUN
- **Kontrol:** Gereksiz konum güncellemesi (pusula/kıble: `headingFilter`, `distanceFilter`), sürekli timer, arka plan işi, yüksek FPS'in gereksiz yerde tutulması (Xcode MCP `profile_energy`).
- **Geçer:** Ekran kapalıyken/arka planda gereksiz iş yok.

#### J-07 · Açılış süresi · 🟡 · 🚀 · YEREL BULUT OYUN
- **Kontrol:** Soğuk açılış (Xcode MCP `profile_launch`); açılışta senkron ağır iş, gereksiz SDK başlatma.
- **Geçer:** Soğuk açılış < 1-2 sn (oyunda yükleme ekranıyla makul).

#### J-09 · Oyun performansı · 🟠 · 🚀 · OYUN
- **Kontrol:** Hedef cihazda FPS (30/60), draw call, batching, LOD, occlusion culling, GC allocation/frame, shader varyant sayısı, Profiler.
- **Geçer:** En zayıf hedef cihazda hedef FPS sabit.

### K. Asenkron işler, kuyruklar ve gerçek zamanlı iletişim

#### K-01 · Timeout · 🟠 · 🏁 · Hepsi (ağ kullanan)
- **Ne/Neden:** Timeout'suz istek sonsuza kadar bekler ve UI'yi/kaynakları kilitler.
- **Kontrol:** `URLSession` `timeoutIntervalForRequest`, `fetch` + `AbortController`, DB sorgu timeout'u, harici API çağrıları.
- **Geçer:** Her dış çağrının makul bir timeout'u var.

#### K-02 · Retry ve üstel geri çekilme · 🟠 · 🚀 · BULUT WEB-API OYUN
- **Kontrol:** Geçici hatalarda (ağ, 429, 5xx) yeniden deneme var mı; exponential backoff + jitter; deneme üst sınırı; 4xx hatalar yeniden denenmiyor mu; tekrar denenen işlem idempotent mi (H-09).
- **Geçer:** Geçici hatalar sınırlı ve geri çekilmeli şekilde yeniden deneniyor.

#### K-07 · WebSocket / gerçek zamanlı · 🟠 · 🚀 · BULUT WEB-API OYUN
- **Kontrol:** Kopunca otomatik yeniden bağlanma + backoff; yeniden bağlanınca kaçırılan olayların alınması; kimlik doğrulama (bağlantı açılırken token); heartbeat/ping; mesaj boyutu ve hız sınırı; dinleyicilerin ekran kapanınca kapatılması (Firestore listener dahil).
- **Geçer:** Bağlantı kopması ve geri gelmesi veri kaybı olmadan ele alınıyor.

#### K-08 · Bildirimler (push / yerel) · 🟡 · 🚀 · YEREL BULUT OYUN
- **Kontrol:** İzin doğru anda isteniyor; APNs anahtarı/sertifika süresi; token yenilemesi; yerel bildirimlerde 64 adet sınırı (iOS) ve saat dilimi değişimi; bildirime tıklayınca doğru ekrana gitme.
- **Geçer:** Bildirimler güvenilir, doğru zamanda ve doğru hedefe.

### L. Gözlemlenebilirlik (loglama, izleme, alarm, hata takibi)

#### L-01 · Yapılandırılmış loglama · 🟡 · 🚀 · Hepsi
- **Kontrol:** iOS: `os.Logger` (subsystem/category), `print` yerine. Sunucu: JSON log, seviye (debug/info/warn/error), istek kimliği (request ID). Log yeterli bağlam içeriyor mu.
- **Geçer:** Bir hatayı loglardan geriye doğru izleyebiliyorsun.

#### L-02 · Loglarda kişisel veri / sır yok · 🔴 · 🏁 · Hepsi
- **Kontrol:** Şunlar **asla** loglanmamalı: token'lar (access/refresh/session), şifreler, API anahtarları, `Authorization` / `Cookie` başlıkları, ödeme bilgileri. Mümkün olduğunca maskele: e-posta (`o***@gmail.com`), telefon, sağlık verisi, konum. Tüm istek/yanıt gövdesini olduğu gibi loglayan middleware var mı; `os.Logger` için `privacy: .private`; hata takip araçlarına (Sentry/Crashlytics) giden "breadcrumb" ve istek başlıkları (Sentry `sendDefaultPii: false`, `beforeSend` ile temizleme).
- **Geçer:** Loglarda sır yok; kişisel veri maskeli.

#### L-03 · Hata takibi / crash raporlama · 🟠 · 🚀 · BULUT WEB-S WEB-API OYUN (YEREL için MetricKit/Xcode Organizer yeterli olabilir)
- **Kontrol:** Sentry, Firebase Crashlytics, Xcode Organizer crash logları, MetricKit, Unity Cloud Diagnostics; dSYM/source map yükleniyor mu (yoksa stack trace okunmaz); kullanıcıya görünmeyen hatalar (yakalanıp yutulan `catch {}`) raporlanıyor mu.
- **Geçer:** Üretimdeki çökmeler ve hatalar okunabilir stack trace ile görülüyor.

#### L-09 · Ürün analitiği · 🟢 · 📈 · BULUT WEB-S WEB-API OYUN
- **Kontrol:** Hangi özellik kullanılıyor; gizlilik dostu mu (TelemetryDeck, Plausible, PostHog); kişisel veri göndermeden; onay (G-06).
- **Geçer:** Karar vermeye yetecek kadar, gizliliği bozmayacak kadar az veri.

### M. Dayanıklılık ve felaket kurtarma

#### M-02 · Zorunlu güncelleme (mobil) · 🟠 · 🏁 · BULUT OYUN
- **Ne/Neden:** Mobilde eski sürümler yıllarca yaşar. Uyumsuz API veya güvenlik açığı için eski sürümü "lütfen güncelleyin" ekranıyla durdurabilmelisin. **İlk sürüme eklenmeli**, sonradan eklenemez (eski sürümler kontrolü bilmez).
- **Kontrol:** Remote Config/uzak JSON ile `minimumVersion` kontrolü.
- **Geçer:** İlk sürümden itibaren minimum sürüm kontrolü var.

#### M-03 · Kill switch · 🟡 · 🚀 · BULUT WEB-API OYUN YZ
- **Ne/Neden:** Sorunlu veya pahalı bir özelliği deploy etmeden anında kapatmak (B-04 ile ilişkili).
- **Geçer:** Riskli özellikler uzaktan kapatılabiliyor.

### N. Kullanıcı deneyimi ve erişilebilirlik

#### N-01 · Erişilebilirlik · 🟠 · 🏁 · YEREL BULUT WEB-S WEB-API OYUN
- **Kontrol:** iOS: VoiceOver etiketleri (`accessibilityLabel`, sadece ikon olan butonlar), Dynamic Type (sabit font boyutu yok, en büyük boyutta taşma), Reduce Motion, renk kontrastı (WCAG AA 4.5:1), sadece renkle bilgi verilmemesi, dokunma alanı ≥ 44pt. Web: semantik HTML, `alt`, klavye ile gezinme, focus görünürlüğü, `aria-*`, axe/Lighthouse erişilebilirlik puanı.
- **Geçer:** VoiceOver/klavye ile ana akış tamamlanabiliyor; en büyük yazı boyutunda düzen bozulmuyor.

#### N-02 · Yerelleştirme ve Türkçe'ye özgü sorunlar · 🟠 · 🏁 · Hepsi (kullanıcıya metin gösteren)
- **Kontrol:** Metinler String Catalog (`Localizable.xcstrings`) / i18n dosyasında mı, kodda sabit mi; tarih/sayı/para biçimi `Locale` ile mi (`1.234,56 ₺`); çoğul kuralları; **Türkçe İ/ı sorunu** (`"i".uppercased()` → `"I"` değil `"İ"`; `toLocaleUpperCase('tr-TR')`, `uppercased(with: Locale(identifier: "tr_TR"))`; büyük/küçük harf duyarsız arama ve sıralamada `localizedStandardCompare`/`Intl.Collator('tr')`); dosya adı ve URL'de Türkçe karakter; uzun metinlerde (Almanca vb.) taşma.
- **Geçer:** Metinler yerelleştirme altyapısında; Türkçe büyük/küçük harf ve sıralama doğru.

#### N-03 · Boş, yükleme ve hata durumları · 🟠 · 🚀 · YEREL BULUT WEB-S WEB-API OYUN
- **Kontrol:** Her veri ekranında: ilk açılış (boş durum + yönlendirme), yükleniyor (iskelet/gösterge), hata (anlaşılır mesaj + "tekrar dene"), kısmi veri. Hata mesajı teknik değil ("Error 500" yerine "Bağlantı kurulamadı").
- **Geçer:** Hiçbir ekran boş beyaz sayfa veya sonsuz döngü göstermiyor.

#### N-04 · İnternet yokken davranış · 🟠 · 🏁 · BULUT WEB-S WEB-API OYUN
- **Kontrol:** Uçak modunda uygulamayı aç ve ana akışı dene. Çevrimdışı göstergesi, kuyruğa alınan yazmalar, önbellekten okuma, yavaş ağda (Network Link Conditioner / DevTools "Slow 3G") davranış.
- **Geçer:** Çevrimdışıyken çökme veya sessiz veri kaybı yok; kullanıcı durumu biliyor.

#### N-06 · Duyarlı (responsive) düzen ve cihaz çeşitliliği · 🟡 · 🚀 · Hepsi (UI olan)
- **Kontrol:** Web: 320 px genişlikte yatay kaydırma yok, dokunmatik hedefler. iOS: en küçük iPhone (SE), en büyük, iPad (destekleniyorsa), yatay mod, Dynamic Island/çentik, güvenli alanlar. Oyun: farklı en-boy oranları, çentik.
- **Geçer:** Desteklenen en küçük ve en büyük ekranda düzen bozulmuyor.

#### N-08 · Onboarding ve ilk kullanım · 🟡 · 🚀 · YEREL BULUT WEB-S WEB-API OYUN
- **Geçer:** Yeni kullanıcı açıklamaya ihtiyaç duymadan ilk değerli işi yapabiliyor; izinler bağlamında isteniyor.

#### N-10 · Haptik, ses ve hareket · 🟢 · 📈 · YEREL BULUT OYUN
- **Kontrol:** Reduce Motion'a saygı, sessiz modda ses çalmama, haptiklerin aşırı kullanılmaması.
- **Geçer:** Sistem tercihlerine uyuluyor.

### Q. Platform: Oyun (Unity)

#### Q-01 · Kayıt sistemi · 🔴 · 🏁 · OYUN
- **Kontrol:** Kayıt dosyası sürümlü (H-03); yazma sırasında çökme/kapanmada bozulmama (önce geçici dosyaya yaz, sonra değiştir); bulut kaydı varsa çakışma (H-10); PlayerPrefs'e büyük/kritik veri konmaması.
- **Geçer:** Kayıt bozulmaya ve sürüm değişimine dayanıklı.

#### Q-02 · Çok oyunculu yetki modeli · 🔴 · 🏁 · OYUN (çevrimiçi)
- **Ne/Neden:** Sunucu/host otoritesi mi, istemci otoritesi mi? İstemciye güvenmek hileye açıktır.
- **Kontrol:** Netcode for GameObjects/Mirror/Photon/Fishnet; kritik durum (can, skor, envanter, kapı/ilerleme) kimde; host ayrılınca (host migration) ne oluyor; bağlantı kopması ve yeniden katılma; lobi/relay servisi (Unity Relay/Lobby) ve kota.
- **Geçer:** Kritik durum otoritede; kopma ve yeniden bağlanma ele alınmış.

#### Q-03 · Ağ performansı ve gecikme · 🟠 · 🚀 · OYUN (çevrimiçi)
- **Kontrol:** Tick hızı, bant genişliği/oyuncu, interpolasyon, gecikme telafisi, yüksek ping (200 ms+) ve paket kaybı simülasyonu.
- **Geçer:** Kötü ağda oynanabilir kalıyor.

#### Q-04 · Girdi ve kontroller · 🟡 · 🚀 · OYUN
- **Kontrol:** Dokunmatik kontroller farklı ekranlarda, oyun kumandası desteği, duraklatma (uygulama arka plana gidince), kontrol ayarları.
- **Geçer:** Hedef cihazlarda kontroller rahat; arka plana gidince oyun duruyor.

#### Q-05 · Build ve asset yönetimi · 🟡 · 🚀 · OYUN
- **Kontrol:** Addressables/asset paketleri, kullanılmayan asset'ler, build boyutu (O-05), platform bazlı sıkıştırma, IL2CPP + stripping ayarları, `Resources/` klasörünün şişmesi.
- **Geçer:** Build boyutu ve yükleme süresi kontrol altında.

### R. Operasyon, maliyet ve bakım

#### R-04 · Bağımlılık güncelleme · 🟡 · 📈 · Hepsi
- **Kontrol:** Dependabot/Renovate; `npm outdated`; büyük sürüm geride kalma; Xcode/Unity/Node LTS sürüm yaşam sonu.
- **Geçer:** Güncellemeler düzenli ve otomatik öneriliyor.

#### R-07 · Teknik borç kaydı · 🟢 · 📈 · Hepsi
- **Kontrol:** `TODO/FIXME/HACK` sayısı ve yaşı; bilinen geçici çözümler belgeli mi.
- **Geçer:** Bilinçli borç kayıtlı (`Yapılacaklar.md`), kod içi TODO'lar kontrol altında.

### U. Yayınlamadan önce düzeltilecek ürün sorunları (ilk deneyim)

> Profil: `MAĞAZA` (ve kullanıcıya açılan her `WEB-S`/`WEB-API`/`OYUN`). Bu sorunlar inceleme reddi değil ama **ilk gün kullanıcı kaybı** demektir. "Yayın hazırlığı" fazında, mümkünse daha önce "İlk deneyim" fazında çözülür.

#### U-01 · Açılış 2 saniyeden uzun · 🟠 · 🚀 · MAĞAZA OYUN
- **Düzeltme:** Splash/startup süresini ölç (J-07, Xcode MCP `profile_launch`); ağır işleri (SDK başlatma, veri taşıma, ağ, büyük görsel) ilk kareden **sonraya** ertele; ilk ekranı önbellekten göster. Splash ekranını yapay olarak uzatma.
- **Geçer:** Soğuk açılışta ilk kullanılabilir ekran < 2 sn (orta seviye cihazda).

#### U-06 · İlk değer anına (time-to-value) ulaşmak çok uzun · 🟠 · 🚀 · MAĞAZA WEB-S WEB-API OYUN
- **Düzeltme:** Kullanıcıyı "aha anı"na (ilk film önerisi, ilk kıble yönü, ilk oyun turu) mümkün olduğunca hızlı götür; o ana kadarki adım sayısını say ve azalt. Oyunda ilk 30 saniyede oynanış.
- **Geçer:** İlk değer anı tanımlı, adım sayısı ve süresi ölçülmüş.

#### U-11 · Hata mesajı yok veya anlamsız · 🟠 · 🚀 · Hepsi (UI olan)
- **Düzeltme:** Hatanın ne olduğunu ve kullanıcının **ne yapabileceğini** yaz ("Bağlantı kurulamadı. İnternetini kontrol edip tekrar dene." + Tekrar Dene butonu). "Bir sorun oluştu" tek başına yetmez; hata kodu gerekiyorsa küçük ikincil metin olarak (N-03, W-11).
- **Geçer:** Her hata mesajı bir sonraki adımı söylüyor.

#### U-13 · Dokunma hedefleri küçük · 🟠 · 🚀 · MAĞAZA WEB-S WEB-API OYUN
- **Düzeltme:** Dokunma alanları en az 44×44 pt (Apple) / 48×48 dp (Android); butonlar arası boşluk; küçük ikonlarda `contentShape` veya padding ile alan büyütme (N-01).
- **Geçer:** En küçük cihazda yanlış dokunma olmadan tüm kontroller kullanılabiliyor.

#### U-18 · Uygulama boyutu 200 MB üstü · 🟡 · 🚀 · MAĞAZA OYUN
- **Düzeltme:** Büyük asset, video, görsel ve paket bağımlılıklarını analiz et (App Thinning Size Report, Unity Build Report); gereksizleri kaldır, görselleri sıkıştır (I-03), isteğe bağlı içeriği sonradan indir (On-Demand Resources / Background Assets / Addressables). Hücresel ağda 200 MB üstü indirmede kullanıcıya ek onay sorulur ve indirme vazgeçme oranı artar (O-05, Q-05).
- **Geçer:** İndirme boyutu bilinçli; büyük içerik isteğe bağlı.

### X. Saldırgan gibi test (kendi uygulamanda güvenlik testi)

> Profil: `BULUT`, `WEB-API` (ve sunucusu olan `OYUN`). **Yalnızca yetkili olduğun kendi uygulamanda**, tercihen staging ortamında (B-03) ve test hesaplarıyla yapılır. Üretim verisine zarar verecek, başkasının hesabına dokunacak veya hizmeti düşürecek test yapılmaz. Ajan her testi önce kullanıcıya listeler, onay alır, sonuçları `Kontrol.md`'ye yazar. Bulunan açıklar 🔴 olarak ilgili maddeye bağlanır. Araçlar: tarayıcı DevTools, `curl`, Burp Suite Community / OWASP ZAP (yerel proxy), Firebase Rules Playground / emülatör.

#### X-15 · İstemci tarafı güven testi · 🟠 · 🚀 · BULUT OYUN GELİR
- **Nasıl:** İstemci kodunda değiştirilebilecek değerleri değiştir: premium bayrağı (`UserDefaults`/localStorage `isPremium`), skor, fiyat, indirim, stok; proxy ile isteği düzenle. Firebase'de istemcinin yazabildiği alanları kurallar dışında dene.
- **Geçer:** Sunucu/kurallar değiştirilmiş değeri kabul etmiyor (V-11, F-17, Q-02).
