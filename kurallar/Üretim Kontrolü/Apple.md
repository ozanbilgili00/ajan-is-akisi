---
tür: üretilmiş-parça
kaynak: Kurallar/Üretim Kontrolü.md
kaynak-sürüm: 1.3
kaynak-özet: b6bdd028b3e2
---

# Üretim Kontrolü: Apple

> **Elle düzenlenmez.** Bu dosya `Kurallar/Üretim Kontrolü.md` kaynağından `~/.claude/hooks/uretim_bol.py` ile üretilir; değişiklik kaynağa yapılır, parçalar oturum başında kendiliğinden yenilenir.
>
> **Kimler okur:** iOS ve macOS uygulamaları (`YEREL`, `BULUT`).
> **Nasıl okunur:** tamamını değil. Önce dizine bak; fazın kontrol kapısındaki kimliklerin metnini aşağıda bul. Profil, önem, aşama ve fazlara yayma kuralları [[Kurallar/Üretim Kontrolü/Yöntem|Yöntem]] notunda.


129 madde. Her kademenin başlığı kimin için olduğunu söyler; projene uymayan kademeyi atla.


## Dizin


**Kademe A · Her uygulama** (61 madde)

| Kimlik | Madde | Önem | Zaman | Profil |
|---|---|---|---|---|
| A-01 | Git ve uzak yedek | 🔴 | 🏁 | Hepsi |
| A-02 | `.gitignore` doğru | 🟠 | 🏁 | Hepsi |
| A-03 | Kilit dosyası (lockfile) ve sürüm sabitleme | 🟠 | 🏁 | Hepsi |
| A-04 | README | 🟡 | 🚀 | Hepsi |
| A-05 | Dal ve commit düzeni | 🟢 | 📈 | Hepsi |
| B-05 | Debug kodunun prod'a sızmaması | 🟠 | 🚀 | Hepsi |
| C-01 | Sürekli entegrasyon (CI) | 🟠 | 🚀 | Hepsi |
| C-03 | Tekrarlanabilir build | 🟡 | 🚀 | Hepsi |
| C-06 | Sürümleme ve CHANGELOG | 🟡 | 🚀 | Hepsi |
| D-01 | Birim testleri | 🟠 | 🚀 | Hepsi |
| D-03 | UI / uçtan uca testler | 🟡 | 📈 | YEREL BULUT WEB-S WEB-API |
| D-04 | Snapshot / görsel regresyon | 🟢 | 📈 | YEREL BULUT WEB-S |
| D-05 | Lint ve biçimlendirme | 🟡 | 🏁 | Hepsi |
| D-06 | Tip güvenliği ve derleyici uyarıları | 🟠 | 🏁 | Hepsi |
| D-07 | Statik analiz ve güvenlik taraması | 🟡 | 🚀 | Hepsi |
| D-09 | Kod incelemesi | 🟢 | 📈 | Hepsi |
| F-01 | Sır taraması (git geçmişi dahil) | 🔴 | 🏁 | Hepsi |
| F-11 | Bağımlılık güvenliği | 🟠 | 🚀 | Hepsi |
| F-13 | Şifreleme (aktarımda ve depoda) | 🟠 | 🏁 | Hepsi |
| G-02 | Apple gizlilik bildirimleri | 🔴 | 🚀 | YEREL BULUT OYUN |
| G-03 | İzin açıklamaları | 🟠 | 🚀 | YEREL BULUT OYUN |
| G-04 | Veri minimizasyonu ve hassas veri | 🟠 | 🏁 | Hepsi |
| G-05 | Veri dışa aktarma ve taşınabilirlik | 🟡 | 🚀 | YEREL BULUT WEB-API |
| G-07 | Lisanslar ve kullanım şartları | 🟠 | 🚀 | Hepsi |
| H-01 | Veri modeli tasarımı | 🟠 | 🏁 | Hepsi (veri tutan) |
| H-02 | Zaman damgaları ve saat dilimi | 🟠 | 🏁 | Hepsi (veri tutan) |
| H-03 | Migration (şema geçişi) | 🔴 | 🏁 | Hepsi (kalıcı veri tutan) |
| H-04 | Yedekleme | 🔴 | 🚀 | BULUT WEB-API YEREL |
| H-12 | Veri bütünlüğü doğrulaması | 🟡 | 🚀 | Hepsi (veri tutan) |
| I-05 | Yerel depolama sınırları | 🟡 | 🏁 | WEB-S YEREL |
| J-01 | Performans bütçesi | 🟡 | 🚀 | Hepsi |
| J-04 | Ana thread ve takılmalar | 🟠 | 🚀 | YEREL BULUT OYUN |
| J-05 | Bellek ve sızıntı | 🟠 | 🚀 | YEREL BULUT OYUN ARAÇ |
| J-06 | Enerji ve pil | 🟡 | 🚀 | YEREL BULUT OYUN |
| J-07 | Açılış süresi | 🟡 | 🚀 | YEREL BULUT OYUN |
| K-01 | Timeout | 🟠 | 🏁 | Hepsi (ağ kullanan) |
| K-04 | Arka plan işleri (background jobs) | 🟡 | 🚀 | WEB-API BULUT YEREL |
| K-08 | Bildirimler (push / yerel) | 🟡 | 🚀 | YEREL BULUT OYUN |
| L-01 | Yapılandırılmış loglama | 🟡 | 🚀 | Hepsi |
| L-02 | Loglarda kişisel veri / sır yok | 🔴 | 🏁 | Hepsi |
| L-03 | Hata takibi / crash raporlama | 🟠 | 🚀 | BULUT WEB-S WEB-API OYUN (YEREL için MetricKit/Xcode Organizer yeterli olabilir) |
| M-06 | Uygulama içi veri koruması (yerel) | 🟠 | 🏁 | YEREL |
| N-01 | Erişilebilirlik | 🟠 | 🏁 | YEREL BULUT WEB-S WEB-API OYUN |
| N-02 | Yerelleştirme ve Türkçe'ye özgü sorunlar | 🟠 | 🏁 | Hepsi (kullanıcıya metin gösteren) |
| N-03 | Boş, yükleme ve hata durumları | 🟠 | 🚀 | YEREL BULUT WEB-S WEB-API OYUN |
| N-05 | Karanlık mod ve tema | 🟡 | 🚀 | YEREL BULUT WEB-S WEB-API |
| N-06 | Duyarlı (responsive) düzen ve cihaz çeşitliliği | 🟡 | 🚀 | Hepsi (UI olan) |
| N-08 | Onboarding ve ilk kullanım | 🟡 | 🚀 | YEREL BULUT WEB-S WEB-API OYUN |
| N-09 | Geri alınabilirlik ve onay | 🟡 | 🚀 | YEREL BULUT WEB-S WEB-API |
| N-10 | Haptik, ses ve hareket | 🟢 | 📈 | YEREL BULUT OYUN |
| O-01 | İmzalama, sertifika ve profiller | 🟠 | 🚀 | YEREL BULUT OYUN |
| O-02 | App Store İnceleme Kuralları | 🔴 | 🚀 | YEREL BULUT OYUN |
| O-03 | Minimum OS ve API uyumluluğu | 🟡 | 🏁 | YEREL BULUT OYUN |
| O-04 | Swift 6 eşzamanlılık güvenliği | 🟠 | 🏁 | YEREL BULUT |
| O-05 | Uygulama boyutu | 🟢 | 📈 | YEREL BULUT OYUN |
| O-06 | Widget, Live Activity ve uzantılar | 🟡 | 🚀 | YEREL BULUT |
| O-07 | macOS'e özgü | 🟡 | 🚀 | YEREL ARAÇ |
| O-08 | TestFlight ve yayın süreci | 🟡 | 🚀 | YEREL BULUT OYUN |
| R-04 | Bağımlılık güncelleme | 🟡 | 📈 | Hepsi |
| R-07 | Teknik borç kaydı | 🟢 | 📈 | Hepsi |
| U-11 | Hata mesajı yok veya anlamsız | 🟠 | 🚀 | Hepsi (UI olan) |

**Kademe B · Buluta ya da dış API'ye bağlı uygulama (`BULUT`)** (68 madde)

| Kimlik | Madde | Önem | Zaman | Profil |
|---|---|---|---|---|
| B-01 | Ortam değişkenleri ve yapılandırma ayrımı | 🔴 | 🏁 | BULUT WEB-S WEB-API OYUN ARAÇ YZ |
| B-02 | İstemciye giden sırlar | 🔴 | 🏁 | BULUT WEB-S YZ |
| B-03 | Staging / test ortamı | 🟠 | 🚀 | BULUT WEB-API |
| B-04 | Feature flag | 🟢 | 📈 | BULUT WEB-API OYUN |
| C-02 | Sürekli dağıtım (CD) | 🟡 | 📈 | WEB-S WEB-API BULUT ARAÇ |
| C-07 | Rollback (geri alma) | 🟠 | 🚀 | WEB-S WEB-API BULUT |
| D-02 | Entegrasyon testleri | 🟡 | 🚀 | BULUT WEB-API |
| E-01 | Kimlik doğrulama (authentication) | 🔴 | 🏁 | BULUT WEB-API OYUN |
| E-02 | Yetkilendirme (authorization) sunucu tarafında | 🔴 | 🏁 | BULUT WEB-API |
| E-03 | Oturum ve token yönetimi | 🟠 | 🚀 | BULUT WEB-API |
| E-04 | Hesap güvenliği | 🟡 | 🚀 | BULUT WEB-API |
| E-05 | Hesap silme | 🔴 | 🚀 | BULUT WEB-API |
| E-06 | Paylaşım ve davet güvenliği | 🟠 | 🏁 | BULUT WEB-API |
| F-02 | Girdi doğrulama | 🔴 | 🏁 | BULUT WEB-API WEB-S |
| F-06 | Rate limiting | 🟠 | 🚀 | BULUT WEB-API YZ |
| F-07 | API güvenliği genel | 🟠 | 🚀 | WEB-API BULUT |
| F-09 | Dosya yükleme güvenliği | 🟠 | 🚀 | BULUT WEB-API |
| F-12 | BaaS güvenlik kuralları (Firebase/Supabase) | 🔴 | 🏁 | BULUT |
| F-15 | Asgari yetki (least privilege) | 🟡 | 🚀 | BULUT WEB-API ARAÇ |
| F-16 | Denetim kaydı (audit log) | 🟢 | 📈 | WEB-API BULUT |
| F-17 | İstemci/uygulama bütünlüğü | 🟢 | 📈 | BULUT OYUN |
| F-18 | Webhook güvenliği | 🔴 | 🚀 | WEB-API BULUT GELİR |
| F-20 | Hassas uç noktaların korunması | 🟠 | 🚀 | WEB-API BULUT |
| G-01 | Gizlilik politikası | 🔴 | 🚀 | BULUT WEB-API OYUN YZ (mağazaya çıkan her uygulama) |
| G-08 | Yaş sınırı ve içerik | 🟡 | 🚀 | BULUT WEB-API OYUN |
| H-05 | Geri yükleme testi | 🟠 | 🚀 | BULUT WEB-API |
| H-06 | Index ve sorgu verimliliği | 🟡 | 📈 | BULUT WEB-API |
| H-07 | Sayfalama | 🟡 | 🚀 | BULUT WEB-API |
| H-08 | Tutarlılık: transaction ve race condition | 🟠 | 🏁 | BULUT WEB-API OYUN |
| H-09 | Idempotency (tekrar güvenliği) | 🟠 | 🚀 | BULUT WEB-API |
| H-10 | Çevrimdışı senkron ve çakışma çözümü | 🟠 | 🏁 | BULUT |
| H-11 | Silme stratejisi ve veri saklama süresi | 🟡 | 🚀 | BULUT WEB-API |
| I-01 | Nesne depolama (S3 / Firebase Storage / Vercel Blob / R2) | 🟠 | 🚀 | BULUT WEB-API |
| I-02 | Yetim dosya temizliği | 🟢 | 📈 | BULUT WEB-API |
| I-03 | Görsel ve medya optimizasyonu | 🟡 | 🚀 | BULUT WEB-S WEB-API OYUN |
| J-02 | Önbellek (cache) | 🟡 | 📈 | BULUT WEB-S WEB-API |
| J-03 | Önbellek geçersiz kılma (cache invalidation) | 🟠 | 📈 | BULUT WEB-S WEB-API |
| K-02 | Retry ve üstel geri çekilme | 🟠 | 🚀 | BULUT WEB-API OYUN |
| K-03 | Circuit breaker ve kısmi çalışma (graceful degradation) | 🟡 | 📈 | BULUT WEB-API |
| K-06 | Zamanlanmış işler (cron) | 🟡 | 🚀 | WEB-API BULUT |
| K-07 | WebSocket / gerçek zamanlı | 🟠 | 🚀 | BULUT WEB-API OYUN |
| L-04 | Monitoring (metrik izleme) | 🟡 | 📈 | WEB-API BULUT |
| L-05 | Alarm (alerting) | 🟠 | 🚀 | WEB-API BULUT |
| L-09 | Ürün analitiği | 🟢 | 📈 | BULUT WEB-S WEB-API OYUN |
| L-10 | Güvenlik olaylarının loglanması | 🟡 | 🚀 | WEB-API BULUT |
| M-01 | Felaket kurtarma planı (RPO/RTO) | 🟡 | 🚀 | BULUT WEB-API |
| M-02 | Zorunlu güncelleme (mobil) | 🟠 | 🏁 | BULUT OYUN |
| M-03 | Kill switch | 🟡 | 🚀 | BULUT WEB-API OYUN YZ |
| M-05 | Bağımlı servis listesi ve tek hata noktası | 🟡 | 🚀 | BULUT WEB-API |
| N-04 | İnternet yokken davranış | 🟠 | 🏁 | BULUT WEB-S WEB-API OYUN |
| N-07 | Deep link ve URL'ler | 🟢 | 📈 | BULUT WEB-S WEB-API |
| R-01 | Maliyet ve bütçe alarmı | 🔴 | 🚀 | BULUT WEB-API YZ |
| R-08 | SaaS harcama takibi ve otomasyonu | 🟠 | 🚀 | BULUT WEB-API YZ GELİR |
| R-02 | Alan adı, SSL ve sertifika takvimi | 🟠 | 🚀 | WEB-S WEB-API BULUT |
| R-03 | Hesap sahipliği ve erişim | 🟠 | 🚀 | BULUT WEB-API |
| R-05 | Runbook ve operasyon notları | 🟡 | 🚀 | BULUT WEB-API |
| R-06 | Altyapı kod olarak (IaC) ve yapılandırma kaydı | 🟢 | 📈 | BULUT WEB-API |
| U-02 | Değer göstermeden kayıt istemek | 🟠 | 🏁 | MAĞAZA BULUT WEB-API |
| U-10 | İnternet gidince beyaz ekran | 🔴 | 🚀 | MAĞAZA BULUT WEB-S WEB-API |
| U-17 | Hesap silme yok veya bulunmuyor | 🔴 | 🚀 | MAĞAZA BULUT |
| X-04 | IDOR / bozuk erişim kontrolü testi | 🔴 | 🚀 | BULUT WEB-API |
| X-05 | Kimlik doğrulama atlatma testi | 🔴 | 🚀 | BULUT WEB-API |
| X-06 | Yetki yükseltme testi | 🔴 | 🚀 | BULUT WEB-API |
| X-07 | Brute force ve rate limit testi | 🟠 | 🚀 | BULUT WEB-API YZ |
| X-08 | Dosya yükleme güvenliği testi | 🟠 | 🚀 | BULUT WEB-API |
| X-11 | Oturum ele geçirme kontrolleri | 🟠 | 🚀 | WEB-API BULUT |
| X-14 | Hata mesajlarından bilgi sızması testi | 🟠 | 🚀 | WEB-API BULUT |
| X-15 | İstemci tarafı güven testi | 🟠 | 🚀 | BULUT OYUN GELİR |

---

## Kademe A · Her uygulama

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

#### D-03 · UI / uçtan uca testler · 🟡 · 📈 · YEREL BULUT WEB-S WEB-API
- **Ne/Neden:** En önemli 2-3 kullanıcı yolu (onboarding, ana işlem, kayıt) otomatik denenmeli.
- **Kontrol:** XCUITest, Playwright/Cypress.
- **Geçer:** Ana kullanıcı yolu otomatik testli.

#### D-04 · Snapshot / görsel regresyon · 🟢 · 📈 · YEREL BULUT WEB-S
- **Ne/Neden:** Tasarım değişikliklerinin istemeden bozulmasını yakalar.
- **Kontrol:** swift-snapshot-testing, Playwright screenshot karşılaştırma.
- **Geçer:** Kritik ekranların referans görüntüsü var.

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

#### F-11 · Bağımlılık güvenliği · 🟠 · 🚀 · Hepsi
- **Kontrol:** `npm audit --omit=dev` (veya `pnpm audit`, `pip-audit`, `bundle audit`), GitHub Dependabot alerts, bilinen CVE'ler (osv.dev, `osv-scanner`), **kullanılmayan paketler** (`npx depcheck`, `knip`), terk edilmiş/az bilinen paketler, `postinstall` script'leri, typosquatting, lockfile kullanımı (A-03), düzenli güncelleme (R-04).
- **Geçer:** Yüksek/kritik açık yok; kullanılmayan paket yok; bağımlılık sayısı makul.

#### F-13 · Şifreleme (aktarımda ve depoda) · 🟠 · 🏁 · Hepsi
- **Kontrol:** Tüm ağ trafiği HTTPS/WSS (iOS ATS istisnası `NSAllowsArbitraryLoads` var mı); hassas yerel veri için iOS Data Protection (`.completeFileProtection`), Keychain; sağlık/regl/finans gibi hassas veride ekstra şifreleme ihtiyacı.
- **Geçer:** Düz HTTP yok; hassas veri korumalı sınıfta veya şifreli.

### G. Gizlilik ve yasal uyum

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

#### G-05 · Veri dışa aktarma ve taşınabilirlik · 🟡 · 🚀 · YEREL BULUT WEB-API
- **Ne/Neden:** Kullanıcı verisini alabilmeli (KVKK hakkı; ayrıca çevrimdışı uygulamada cihaz değişimi için tek kurtuluş).
- **Geçer:** Dışa aktarma (JSON/CSV) veya iCloud yedeği ile veri taşınabiliyor.

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

#### H-04 · Yedekleme · 🔴 · 🚀 · BULUT WEB-API YEREL
- **Kontrol:** Sunucu: otomatik DB yedeği (Firestore scheduled backups / PITR, Postgres yedekleri), saklama süresi, farklı bölge. Yerel uygulama: iCloud yedeğine dahil mi (`isExcludedFromBackup`), dışa aktarma (G-05).
- **Geçer:** Otomatik yedek var ve saklama süresi tanımlı.

#### H-12 · Veri bütünlüğü doğrulaması · 🟡 · 🚀 · Hepsi (veri tutan)
- **Kontrol:** Bozuk/eksik veri okununca uygulama çöküyor mu (decode hatası → `try?` ile sessiz kayıp mı, kullanıcıya bilgi mi); localStorage'ın elle bozulması; JSON şema doğrulaması.
- **Geçer:** Bozuk veri uygulamayı çökertmiyor ve sessizce silinmiyor.

### I. Depolama, dosyalar ve CDN

#### I-05 · Yerel depolama sınırları · 🟡 · 🏁 · WEB-S YEREL
- **Ne/Neden:** localStorage ~5 MB ile sınırlıdır, senkron çalışır ve tarayıcı tarafından silinebilir (Safari ITP 7 gün kuralı). Büyük veya kritik veri için IndexedDB, mümkünse sunucu. iOS'ta `Caches/` dizini sistem tarafından silinebilir.
- **Kontrol:** localStorage'a yazılan veri boyutu, `QuotaExceededError` yakalanıyor mu, kalıcı veri doğru dizinde mi (`Application Support`, `Documents`).
- **Geçer:** Kritik veri silinebilir bir yerde değil; kota hatası ele alınmış.

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

### K. Asenkron işler, kuyruklar ve gerçek zamanlı iletişim

#### K-01 · Timeout · 🟠 · 🏁 · Hepsi (ağ kullanan)
- **Ne/Neden:** Timeout'suz istek sonsuza kadar bekler ve UI'yi/kaynakları kilitler.
- **Kontrol:** `URLSession` `timeoutIntervalForRequest`, `fetch` + `AbortController`, DB sorgu timeout'u, harici API çağrıları.
- **Geçer:** Her dış çağrının makul bir timeout'u var.

#### K-04 · Arka plan işleri (background jobs) · 🟡 · 🚀 · WEB-API BULUT YEREL
- **Ne/Neden:** E-posta, bildirim, rapor, görsel işleme gibi uzun işler istek içinde yapılmamalı.
- **Kontrol:** Sunucu: Vercel Cron/Queues, Cloud Functions tetikleyicileri, BullMQ. iOS: `BGTaskScheduler`, `BGAppRefreshTask`, background modes'un gerçekten gerekip gerekmediği.
- **Geçer:** Uzun işler arka planda; iOS arka plan modları sadece gerekenler.

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

### M. Dayanıklılık ve felaket kurtarma

#### M-06 · Uygulama içi veri koruması (yerel) · 🟠 · 🏁 · YEREL
- **Ne/Neden:** Sunucusuz uygulamada veri tek kopyadır; uygulama silinirse veya cihaz değişirse gider.
- **Kontrol:** iCloud yedeğe dahil mi, CloudKit senkron seçeneği, dışa/içe aktarma (G-05), migration hatasında veriyi silmek yerine korumaya alma (H-03).
- **Geçer:** Kullanıcının veriyi kaybetmeden cihaz değiştirmesinin en az bir yolu var.

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

#### N-05 · Karanlık mod ve tema · 🟡 · 🚀 · YEREL BULUT WEB-S WEB-API
- **Kontrol:** Sabit renkler (`Color.white`, `#fff`) yerine semantik renkler/asset catalog/CSS değişkenleri; her iki modda kontrast.
- **Geçer:** İki modda da okunaklı ve tutarlı.

#### N-06 · Duyarlı (responsive) düzen ve cihaz çeşitliliği · 🟡 · 🚀 · Hepsi (UI olan)
- **Kontrol:** Web: 320 px genişlikte yatay kaydırma yok, dokunmatik hedefler. iOS: en küçük iPhone (SE), en büyük, iPad (destekleniyorsa), yatay mod, Dynamic Island/çentik, güvenli alanlar. Oyun: farklı en-boy oranları, çentik.
- **Geçer:** Desteklenen en küçük ve en büyük ekranda düzen bozulmuyor.

#### N-08 · Onboarding ve ilk kullanım · 🟡 · 🚀 · YEREL BULUT WEB-S WEB-API OYUN
- **Geçer:** Yeni kullanıcı açıklamaya ihtiyaç duymadan ilk değerli işi yapabiliyor; izinler bağlamında isteniyor.

#### N-09 · Geri alınabilirlik ve onay · 🟡 · 🚀 · YEREL BULUT WEB-S WEB-API
- **Kontrol:** Yıkıcı işlemlerde onay veya "geri al"; form verisinin yanlışlıkla kaybolması (sayfadan çıkınca uyarı, taslak saklama).
- **Geçer:** Kullanıcı tek dokunuşla geri dönülmez veri kaybı yaşamıyor.

#### N-10 · Haptik, ses ve hareket · 🟢 · 📈 · YEREL BULUT OYUN
- **Kontrol:** Reduce Motion'a saygı, sessiz modda ses çalmama, haptiklerin aşırı kullanılmaması.
- **Geçer:** Sistem tercihlerine uyuluyor.

### O. Platform: iOS / macOS

#### O-01 · İmzalama, sertifika ve profiller · 🟠 · 🚀 · YEREL BULUT OYUN
- **Kontrol:** Otomatik imzalama, Team ID, sertifika/provisioning bitiş tarihleri, APNs anahtarı, gereksiz entitlement yok (`*.entitlements`), App Groups/Keychain Sharing tutarlı.
- **Geçer:** Release arşivi temiz makinede imzalanıp yüklenebiliyor.

#### O-02 · App Store İnceleme Kuralları · 🔴 · 🚀 · YEREL BULUT OYUN
- **Kontrol:** 2.1 (eksiksiz, çökmesiz, placeholder içerik yok), 4.2 (yeterli işlevsellik, web sarmalayıcı değil), 5.1.1 (veri toplama ve hesap silme), 4.8 (üçüncü taraf girişte Sign in with Apple veya eşdeğer gizlilik odaklı giriş), 3.1 (dijital içerik satışında IAP zorunluluğu), inceleme için demo hesap, metadata'da yanıltıcı ifade yok, sağlık iddialarında tıbbi uyarı (regl/sağlık uygulamaları için önemli). **Ayrıntılı gönderim öncesi liste: Bölüm T.**
- **Geçer:** Bilinen ret nedenlerinin hiçbiri yok; T kategorisi tamam.

#### O-03 · Minimum OS ve API uyumluluğu · 🟡 · 🏁 · YEREL BULUT OYUN
- **Kontrol:** Deployment target; yeni API'ler `if #available` ile korunmuş mu; en düşük desteklenen sürümde simülatörde test.
- **Geçer:** Desteklenen en eski OS'te çalışıyor.

#### O-04 · Swift 6 eşzamanlılık güvenliği · 🟠 · 🏁 · YEREL BULUT
- **Kontrol:** `@MainActor` izolasyonu, `Sendable` uyarıları, `nonisolated(unsafe)`/`@unchecked Sendable` kullanımı (gerekçeli mi), ana actor dışı kapanışta UI erişimi (çökme nedeni), `Task` iptali.
- **Geçer:** Strict concurrency'de uyarı yok; `unsafe` kaçışlar gerekçeli.

#### O-05 · Uygulama boyutu · 🟢 · 📈 · YEREL BULUT OYUN
- **Kontrol:** IPA boyutu (App Thinning raporu), gereksiz büyük asset, kullanılmayan framework; 200 MB hücresel indirme sınırı (oyunlar için önemli).
- **Geçer:** Boyut makul ve büyük asset'ler gerekçeli/isteğe bağlı indirilebilir.

#### O-06 · Widget, Live Activity ve uzantılar · 🟡 · 🚀 · YEREL BULUT
- **Kontrol:** Uzantı ile uygulama arasında App Group paylaşımı, timeline yenileme bütçesi, uzantıda bellek sınırı, Live Activity süre ve güncelleme sınırları.
- **Geçer:** Uzantılar kendi kısıtları içinde güvenilir çalışıyor.

#### O-07 · macOS'e özgü · 🟡 · 🚀 · YEREL ARAÇ
- **Kontrol:** Sandbox ve entitlement'lar, notarization, Hardened Runtime, erişilebilirlik/ekran kaydı gibi TCC izinleri, menü çubuğu uygulamasında giriş sırasında başlatma (`SMAppService`), Sparkle/güncelleme mekanizması (Mac App Store dışı ise).
- **Geçer:** Notarize edilmiş, izinleri açıklanmış, güncellenebilir.

#### O-08 · TestFlight ve yayın süreci · 🟡 · 🚀 · YEREL BULUT OYUN
- **Geçer:** Her yayından önce TestFlight'ta gerçek cihazda en az bir tur; "Test edilecekler" notu yazılı.

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


---

## Kademe B · Buluta ya da dış API'ye bağlı uygulama (`BULUT`)

### B. Ortam ve yapılandırma

#### B-01 · Ortam değişkenleri ve yapılandırma ayrımı · 🔴 · 🏁 · BULUT WEB-S WEB-API OYUN ARAÇ YZ
- **Ne/Neden:** Ayar ve sırlar koddan ayrı olmalı; dev/staging/prod farklı değerlerle çalışabilmeli.
- **Kontrol:** `.env.example` var mı; kodda sabit URL/anahtar (`grep -rnE 'https?://[^"]*(api|prod)|sk_live|AIza|apiKey\s*[:=]'`); Xcode'da `.xcconfig` veya build configuration kullanımı; Vite'ta sadece `VITE_` önekli değişkenlerin istemciye gittiğinin farkında olunması.
- **Geçer:** Tüm ayarlar tek yerden okunuyor; `.env.example` güncel; prod sırrı istemci paketine girmiyor.

#### B-02 · İstemciye giden sırlar · 🔴 · 🏁 · BULUT WEB-S YZ
- **Ne/Neden:** Mobil uygulamaya veya web paketine konan her şey **herkese açıktır**. Ücretli API anahtarları (OpenAI, Anthropic, TMDB yazma anahtarı, Stripe secret) istemcide olmamalı.
- **Kontrol:** `dist/` veya build çıktısında anahtar araması; Swift kaynaklarında string anahtar; `Info.plist` içinde gizli değer.
- **Geçer:** İstemcide sadece herkese açık olması tasarlanmış anahtarlar var (Firebase web config, TMDB okuma anahtarı gibi) ve bunlar kurallar/kota ile korunuyor; ücretli anahtarlar bir sunucu veya proxy arkasında.

#### B-03 · Staging / test ortamı · 🟠 · 🚀 · BULUT WEB-API
- **Ne/Neden:** Değişiklik gerçek kullanıcı verisine dokunmadan önce denenebilmeli.
- **Kontrol:** Ayrı Firebase projesi veya emülatör (`firebase.json` → `emulators`), ayrı veritabanı, preview deploy (Vercel preview); geliştirme sırasında prod'a yazılıyor mu.
- **Geçer:** Geliştirme ve test, prod verisinden ayrı bir ortamda yapılıyor.

#### B-04 · Feature flag · 🟢 · 📈 · BULUT WEB-API OYUN
- **Ne/Neden:** Yarım özelliği kapalı göndermek, sorunlu özelliği yeni sürüm çıkarmadan kapatmak.
- **Kontrol:** Remote Config, LaunchDarkly, kendi flag tablosu veya en azından derleme bayrağı.
- **Geçer:** Riskli özellikler uzaktan kapatılabiliyor.

### C. CI/CD ve teslimat

#### C-02 · Sürekli dağıtım (CD) · 🟡 · 📈 · WEB-S WEB-API BULUT ARAÇ
- **Ne/Neden:** Dağıtım elle ve ezbere yapılırsa adım unutulur.
- **Kontrol:** Vercel otomatik deploy, `firebase deploy` script'i, TestFlight'a otomatik yükleme (fastlane / Xcode Cloud), npm publish workflow.
- **Geçer:** Dağıtım tek komut veya otomatik; adımlar belgeli.

#### C-07 · Rollback (geri alma) · 🟠 · 🚀 · WEB-S WEB-API BULUT
- **Ne/Neden:** Bozuk sürüm çıktığında dakikalar içinde önceki sürüme dönebilmek.
- **Kontrol:** Vercel "instant rollback", önceki deploy'u yeniden yayınlama, Firebase rules sürüm geçmişi; veritabanı migration'ının geri alınabilirliği (bkz. H-03). Mobilde gerçek rollback yoktur → kill switch / feature flag (M-03).
- **Geçer:** Geri dönüş yolu biliniyor ve en az bir kez denenmiş.

### D. Test ve kod kalitesi

#### D-02 · Entegrasyon testleri · 🟡 · 🚀 · BULUT WEB-API
- **Ne/Neden:** Bileşenler birlikte doğru çalışıyor mu (API + DB, uygulama + Firebase emülatörü, güvenlik kuralları).
- **Kontrol:** Emülatörle çalışan testler, Firestore rules testleri (`@firebase/rules-unit-testing`), API uç nokta testleri.
- **Geçer:** Kritik akışlar (giriş, veri yazma, yetkisiz erişimin reddi) testli.

### E. Kimlik doğrulama ve yetkilendirme

#### E-01 · Kimlik doğrulama (authentication) · 🔴 · 🏁 · BULUT WEB-API OYUN
- **Ne/Neden:** "Bu kullanıcı kim?" Kendi şifre sistemini yazmak yerine kanıtlanmış sağlayıcı (Firebase Auth, Sign in with Apple, Auth.js, Clerk, Supabase Auth).
- **Kontrol:** Şifreler düz metin veya zayıf hash (MD5/SHA1) ile mi saklanıyor; localStorage'da "giriş" sadece istemci tarafı mı (bu **güvenlik değildir**, sadece kullanıcı arayüzüdür).
- **Geçer:** Kimlik sunucu tarafında doğrulanıyor; şifre varsa bcrypt/argon2; istemci tarafı sahte auth "güvenlik" diye sunulmuyor.

#### E-02 · Yetkilendirme (authorization) sunucu tarafında · 🔴 · 🏁 · BULUT WEB-API
- **Ne/Neden:** "Bu kullanıcı bu veriye erişebilir mi?" kontrolü **istemcide değil**, sunucuda/güvenlik kurallarında olmalı. İstemci her zaman kandırılabilir.
- **Kontrol:** Her API ucunda sahiplik kontrolü (IDOR: başkasının `id`'sini yazınca veri geliyor mu); Firestore rules'ta `request.auth.uid` karşılaştırması; rol kontrolleri (patron/şef/çalışan gibi) sunucuda mı; **admin uçları ve admin işlemleri ayrı rol kontrolünden** geçiyor mu; kullanıcı kendi rolünü değiştirebiliyor mu (profil güncelleme isteğine `role: "admin"` eklemek, Firestore'da `users/{uid}.role` alanını kullanıcının yazabilmesi = **yetki yükseltme**); rol bilgisi istemciden mi geliyor (asla), yoksa sunucu/custom claims'den mi.
- **Geçer:** Başka kullanıcının verisine erişim ve kendi yetkisini yükseltme denemesi reddediliyor (test ile kanıtlı, bkz. X-04, X-06). Rol alanları sadece sunucu/admin tarafından yazılabiliyor.

#### E-03 · Oturum ve token yönetimi · 🟠 · 🚀 · BULUT WEB-API
- **Kontrol:**
  - Web oturum çerezi: `HttpOnly` (JS okuyamaz → XSS ile çalınamaz), `Secure` (sadece HTTPS), uygun `SameSite` (`Lax` varsayılan; çapraz site gerekiyorsa `None; Secure` + CSRF koruması), dar `Path`/`Domain`.
  - Token `localStorage`'da mı (XSS'te çalınır); iOS'ta Keychain'de mi (UserDefaults'ta değil).
  - Oturum süresi: hareketsizlik zaman aşımı + mutlak süre; refresh token rotasyonu.
  - Çıkışta oturum **sunucuda** geçersiz kılınıyor mu (sadece istemciden silmek yetmez); şifre değişince diğer oturumlar kapanıyor mu.
  - Girişte oturum kimliği yenileniyor mu (session fixation).
  - Hassas işlemlerde (şifre/e-posta değiştirme, hesap silme, ödeme yöntemi) **yeniden kimlik doğrulama** isteniyor mu (Firebase `reauthenticateWithCredential`).
  - JWT: imza algoritması sabit (`alg: none` kabul edilmiyor), `exp` kontrol ediliyor, gizli anahtar güçlü.
- **Geçer:** Token güvenli yerde, süreli, çıkışta sunucuda geçersiz; hassas işlemler yeniden doğrulama istiyor.

#### E-04 · Hesap güvenliği · 🟡 · 🚀 · BULUT WEB-API
- **Kontrol:** Giriş denemesi sınırı (bkz. F-06), başarısız girişlerin **güvenli şekilde loglanması** (şifre loglanmadan; IP, zaman, hesap kimliği — bkz. L-10), şifre sıfırlama akışının güvenliği (tek kullanımlık, süreli bağlantı), e-posta doğrulama, isteğe bağlı 2FA, kullanıcı numaralandırma ("bu e-posta kayıtlı değil" mesajı) yok; şifre saklanıyorsa sadece **bcrypt, scrypt veya Argon2** (E-01).
- **Geçer:** Brute force ve hesap ele geçirmeye karşı temel önlemler var.

#### E-05 · Hesap silme · 🔴 · 🚀 · BULUT WEB-API
- **Ne/Neden:** App Store **zorunlu kılar** (hesap oluşturulabiliyorsa uygulama içinden silinebilmeli). KVKK/GDPR de gerektirir.
- **Kontrol:** Uygulama içinde "Hesabı sil" var mı; silme gerçekten tüm veriyi (DB, Storage, Auth kaydı) kaldırıyor mu.
- **Geçer:** Uygulama içinden tam silme mümkün.

#### E-06 · Paylaşım ve davet güvenliği · 🟠 · 🏁 · BULUT WEB-API
- **Ne/Neden:** Eşleşme kodu, davet bağlantısı, paylaşılan alanlar (çift uygulaması, aile, ekip) tahmin edilebilir olmamalı.
- **Kontrol:** Kod uzunluğu ve rastgeleliği, süre sınırı, tek kullanımlık mı, deneme sınırı.
- **Geçer:** Davet/eşleşme kodları tahmin edilemez ve süreli.

### F. API ve uygulama güvenliği

#### F-02 · Girdi doğrulama · 🔴 · 🏁 · BULUT WEB-API WEB-S
- **Ne/Neden:** Kullanıcıdan gelen her veri (form, URL parametresi, API gövdesi, dosya) şema ile doğrulanmalı: tip, uzunluk, aralık, biçim.
- **Kontrol:** Zod/Valibot/Joi kullanımı, Firestore rules'ta alan doğrulaması (`request.resource.data.keys().hasOnly([...])`, tip ve boyut kontrolleri); **beklenmeyen alanlar ve tipler reddediliyor mu** (sayı yerine string, dizi yerine nesne, fazladan `isAdmin` alanı — mass assignment); `null`, boş string, çok uzun string, negatif sayı, emoji/Unicode, büyük JSON gövdesi denenmiş mi.
- **Geçer:** Tüm girdiler **sunucuda** şema ile doğrulanıyor, bilinmeyen alanlar atılıyor veya reddediliyor; istemci doğrulaması sadece kullanıcı deneyimi içindir.

#### F-06 · Rate limiting · 🟠 · 🚀 · BULUT WEB-API YZ
- **Ne/Neden:** Giriş, kayıt, şifre sıfırlama, e-posta/SMS gönderen ve ücretli API çağıran uçlar kötüye kullanılabilir (fatura patlaması).
- **Kontrol:** Middleware (Upstash ratelimit, express-rate-limit), Vercel Firewall kuralları, Firebase App Check, Cloud Functions için kota. Genel (hesaptan bağımsız) giriş kilidi varsa: IP değiştiren biri herkesi kilitleyebilir mi, kilidi açan yönetim işlemi ve kilitlenince bildirim var mı (Bizim Site F10).
- **Geçer:** Hassas ve pahalı uçlar IP/kullanıcı başına sınırlı.

#### F-07 · API güvenliği genel · 🟠 · 🚀 · WEB-API BULUT
- **Kontrol:** Hata yanıtlarında stack trace/iç bilgi sızıyor mu; gereksiz alanlar dönüyor mu (şifre hash, e-posta listesi); toplu veri çekme sınırı; HTTP metotları doğru mu; API sürümleme.
- **Geçer:** API sadece gerekeni döndürüyor, hata mesajları genel.

#### F-09 · Dosya yükleme güvenliği · 🟠 · 🚀 · BULUT WEB-API
- **Kontrol:**
  - Maksimum dosya boyutu sunucuda/kurallarda (Firebase Storage rules `request.resource.size < 5 * 1024 * 1024`).
  - İzin verilen türler **izin listesi** (whitelist) ile; yasak listesi (blacklist) değil.
  - Hem MIME type hem **dosya içeriği** (magic bytes) kontrolü; uzantıya ve istemcinin gönderdiği `Content-Type`'a güvenme. SVG'yi görsel sanma (içinde script olabilir).
  - Dosya adı kullanıcı girdisinden **doğrudan oluşturulmuyor**; sunucu UUID ile adlandırıyor (path traversal `../`, üzerine yazma).
  - Yükleme klasöründe çalıştırma kapalı (sunucu `.php`/`.js` gibi dosyaları çalıştırmıyor); dosyalar ayrı domain/bucket'tan, `Content-Disposition: attachment` ile sunuluyor.
  - Kullanıcı başına kota; EXIF/konum verisi temizleniyor (gizlilik).
  - Gerekirse antivirüs/malware taraması (ClamAV, bulut sağlayıcının taraması), özellikle başka kullanıcılarla paylaşılan dosyalarda.
- **Geçer:** Yüklemeler sınırlı, izin listesiyle ve içerikten doğrulanmış, sunucu adlandırmalı, çalıştırılamaz, kullanıcıya özel yolda.

#### F-12 · BaaS güvenlik kuralları (Firebase/Supabase) · 🔴 · 🏁 · BULUT
- **Ne/Neden:** Firestore/Storage/RTDB kuralları veritabanının tek kapısıdır. `allow read, write: if true;` veya `if request.auth != null;` tek başına **açık kapıdır** (her giriş yapan herkesin verisini okur).
- **Kontrol:** `firestore.rules`, `storage.rules`, `database.rules.json`; test modu süresi; koleksiyon bazlı sahiplik; alan doğrulama; liste sorgularının sınırlanması; Supabase'de RLS her tabloda açık mı.
- **Geçer:** Varsayılan red; her koleksiyon için sahiplik + şema doğrulaması; kurallar test edilmiş (D-02).

#### F-15 · Asgari yetki (least privilege) · 🟡 · 🚀 · BULUT WEB-API ARAÇ
- **Kontrol:** Servis hesaplarının yetkisi (Firebase Admin SDK her yerde mi kullanılıyor), API anahtarı kısıtlamaları (Google Cloud key restrictions: bundle ID / HTTP referrer), MCP sunucusunun dosya sistemi erişim kapsamı.
- **Geçer:** Her anahtar/hesap sadece ihtiyacı kadar yetkili.

#### F-16 · Denetim kaydı (audit log) · 🟢 · 📈 · WEB-API BULUT
- **Ne/Neden:** Yönetici işlemleri, rol değişiklikleri, silmeler kim tarafından ne zaman yapıldı.
- **Geçer:** Kritik yönetim işlemleri kayıt altında.

#### F-17 · İstemci/uygulama bütünlüğü · 🟢 · 📈 · BULUT OYUN
- **Kontrol:** Firebase App Check / App Attest; oyunlarda istemciye güvenilmemesi (skor, envanter sunucuda doğrulanır).
- **Geçer:** Sahte istemciler arka uca kolayca erişemiyor.

#### F-18 · Webhook güvenliği · 🔴 · 🚀 · WEB-API BULUT GELİR
- **Ne/Neden:** Ödeme (Stripe, RevenueCat, App Store Server Notifications), Git, form servisleri webhook gönderir. Doğrulanmayan webhook'a herkes "ödeme başarılı" yazabilir.
- **Kontrol:**
  - **İmza doğrulama:** sağlayıcının imzası (Stripe `Stripe-Signature`, RevenueCat authorization başlığı, App Store JWS imzalı bildirim) **ham gövde** üzerinden doğrulanıyor mu (JSON parse edildikten sonra doğrulama bozulur); karşılaştırma sabit zamanlı mı.
  - **Replay koruması:** zaman damgası toleransı (örn. 5 dk) + olay kimliği (`event.id`) daha önce işlendiyse atlama (idempotency, H-09).
  - Gövde boyutu sınırı; sadece beklenen olay türleri işleniyor.
  - Webhook yanıtı hızlı (2xx döndürüp ağır işi kuyruğa/arka plana atma, K-04); başarısız olursa sağlayıcının tekrar denemesine dayanıklı.
- **Geçer:** İmzasız veya eski/tekrarlanan webhook reddediliyor (X-09 ile test edilmiş).

#### F-20 · Hassas uç noktaların korunması · 🟠 · 🚀 · WEB-API BULUT
- **Ne/Neden:** Admin panelleri, debug uçları, seed/test endpoint'leri, `/api/internal/*`, Swagger/GraphQL introspection, `.git/`, `.env`, kaynak harita (source map) dosyaları üretimde "gizli URL" diye korumasız bırakılır. Gizlilik güvenlik değildir.
- **Kontrol:** Tüm route listesini çıkar ve her birinde kimlik + yetki kontrolü var mı bak (**API authentication** her uçta); `curl https://site/.env`, `/.git/config`, `/api/debug`; üretimde source map herkese açık mı; admin uçları için ek koruma (IP izin listesi, 2FA, ayrı alt alan).
- **Geçer:** Kimliksiz erişilebilen her uç bilinçli olarak açık; debug/test uçları üretimde yok.

### G. Gizlilik ve yasal uyum

#### G-01 · Gizlilik politikası · 🔴 · 🚀 · BULUT WEB-API OYUN YZ (mağazaya çıkan her uygulama)
- **Ne/Neden:** App Store ve Google Play zorunlu kılar; KVKK aydınlatma metni gerekir.
- **Kontrol:** Erişilebilir URL; uygulama içinden bağlantı; toplanan verilerle tutarlılık.
- **Geçer:** Güncel politika var ve gerçek davranışla örtüşüyor.

#### G-08 · Yaş sınırı ve içerik · 🟡 · 🚀 · BULUT WEB-API OYUN
- **Kontrol:** Kullanıcı üretimli içerik varsa App Store Guideline 1.2 (raporlama, engelleme, filtre); yaş derecelendirmesi doğru mu.
- **Geçer:** Kullanıcı içeriği için şikâyet/engelleme mekanizması var.

### H. Veri ve veritabanı

#### H-05 · Geri yükleme testi · 🟠 · 🚀 · BULUT WEB-API
- **Ne/Neden:** Denenmemiş yedek, yedek değildir.
- **Geçer:** En az bir kez yedekten ayrı bir ortama geri yükleme yapılmış ve süresi biliniyor.

#### H-06 · Index ve sorgu verimliliği · 🟡 · 📈 · BULUT WEB-API
- **Kontrol:** Sık sorgulanan alanlarda index; N+1 sorgu (döngü içinde sorgu); Firestore composite index'ler `firestore.indexes.json` içinde mi; tüm koleksiyonu çekip istemcide filtreleme.
- **Geçer:** Ana sorgular index'li; N+1 yok.

#### H-07 · Sayfalama · 🟡 · 🚀 · BULUT WEB-API
- **Kontrol:** Liste uçları/sorguları `limit` + cursor kullanıyor mu; sonsuz büyüyen listeler.
- **Geçer:** Hiçbir liste sınırsız veri çekmiyor.

#### H-08 · Tutarlılık: transaction ve race condition · 🟠 · 🏁 · BULUT WEB-API OYUN
- **Ne/Neden:** İki kişi aynı anda aynı veriyi değiştirince (sayaç, bakiye, stok, ortak liste) veri bozulmamalı.
- **Kontrol:** Firestore `runTransaction` / `FieldValue.increment`, SQL transaction, oku-değiştir-yaz kalıpları, optimistic locking.
- **Geçer:** Eşzamanlı yazma riski olan yerler atomik.

#### H-09 · Idempotency (tekrar güvenliği) · 🟠 · 🚀 · BULUT WEB-API
- **Ne/Neden:** Ağ kopup istek tekrarlanınca (veya kullanıcı butona iki kez basınca) iki kayıt/iki ödeme oluşmamalı.
- **Kontrol:** Idempotency key, istemci tarafı UUID ile oluşturma, buton kilitleme, webhook'ların tekrar işlenmesi.
- **Geçer:** Kritik yazma işlemleri tekrarlansa da tek sonuç veriyor.

#### H-10 · Çevrimdışı senkron ve çakışma çözümü · 🟠 · 🏁 · BULUT
- **Ne/Neden:** İki cihaz çevrimdışıyken aynı veriyi değiştirirse hangisi kazanır?
- **Kontrol:** Strateji tanımlı mı (son yazan kazanır, alan bazlı birleştirme, CRDT); Firestore offline persistence davranışı; CloudKit çakışma işleme.
- **Geçer:** Çakışma stratejisi bilinçli seçilmiş ve belgeli.

#### H-11 · Silme stratejisi ve veri saklama süresi · 🟡 · 🚀 · BULUT WEB-API
- **Kontrol:** Soft delete (`deletedAt`) mı hard delete mi; çöp kutusu/geri al; ilişkili verinin de silinmesi (yetim kayıt); eski verinin ne zaman temizlendiği.
- **Geçer:** Silme davranışı tutarlı; yanlışlıkla silmeye geri alma şansı var.

### I. Depolama, dosyalar ve CDN

#### I-01 · Nesne depolama (S3 / Firebase Storage / Vercel Blob / R2) · 🟠 · 🚀 · BULUT WEB-API
- **Kontrol:** Bucket herkese açık mı; yollar kullanıcıya özel mi (`users/{uid}/...`); storage kuralları; imzalı/süreli URL; büyük dosyalar DB'de mi (olmamalı).
- **Geçer:** Dosyalar kurallarla korunuyor; DB'de sadece referans.

#### I-02 · Yetim dosya temizliği · 🟢 · 📈 · BULUT WEB-API
- **Ne/Neden:** Kayıt silinince dosyası storage'da kalıyor mu (maliyet + gizlilik).
- **Geçer:** Silme işlemi dosyayı da siliyor veya periyodik temizlik var.

#### I-03 · Görsel ve medya optimizasyonu · 🟡 · 🚀 · BULUT WEB-S WEB-API OYUN
- **Kontrol:** Yükleme öncesi yeniden boyutlandırma/sıkıştırma, modern formatlar (WebP/AVIF/HEIC), thumbnail, `loading="lazy"`, Unity texture sıkıştırma (ASTC).
- **Geçer:** Ham büyük görseller kullanıcıya gönderilmiyor.

### J. Performans ve ölçek

#### J-02 · Önbellek (cache) · 🟡 · 📈 · BULUT WEB-S WEB-API
- **Kontrol:** Tekrarlanan pahalı istekler önbellekleniyor mu (HTTP cache, `URLCache`, React Query/SWR, Redis, Next.js cache, görsel cache); üçüncü parti API kotaları (TMDB) önbellek ile korunuyor mu.
- **Geçer:** Sık ve pahalı veri önbellekli.

#### J-03 · Önbellek geçersiz kılma (cache invalidation) · 🟠 · 📈 · BULUT WEB-S WEB-API
- **Ne/Neden:** Bayat veri göstermek, önbelleğin en sık hatasıdır.
- **Kontrol:** Her önbellek için TTL veya olay tabanlı temizleme; yazma sonrası ilgili cache temizleniyor mu; deploy sonrası eski JS paketi ile yeni API uyumsuzluğu; service worker eski sürümde takılıyor mu.
- **Geçer:** Her önbelleğin ne zaman geçersiz olduğu tanımlı.

### K. Asenkron işler, kuyruklar ve gerçek zamanlı iletişim

#### K-02 · Retry ve üstel geri çekilme · 🟠 · 🚀 · BULUT WEB-API OYUN
- **Kontrol:** Geçici hatalarda (ağ, 429, 5xx) yeniden deneme var mı; exponential backoff + jitter; deneme üst sınırı; 4xx hatalar yeniden denenmiyor mu; tekrar denenen işlem idempotent mi (H-09).
- **Geçer:** Geçici hatalar sınırlı ve geri çekilmeli şekilde yeniden deneniyor.

#### K-03 · Circuit breaker ve kısmi çalışma (graceful degradation) · 🟡 · 📈 · BULUT WEB-API
- **Ne/Neden:** Bir dış servis düştüğünde tüm uygulama çökmemeli; o bölüm "şu an kullanılamıyor" demeli, gerisi çalışmalı.
- **Geçer:** Dış servis hatası izole ediliyor; kullanıcı anlamlı mesaj görüyor.

#### K-06 · Zamanlanmış işler (cron) · 🟡 · 🚀 · WEB-API BULUT
- **Kontrol:** Cron çakışması (önceki iş bitmeden yenisi başlıyor mu), saat dilimi, başarısız olunca haber veriliyor mu, aynı iş iki kez çalışırsa sorun olur mu.
- **Geçer:** Cron işleri izleniyor ve tekrar güvenli.

#### K-07 · WebSocket / gerçek zamanlı · 🟠 · 🚀 · BULUT WEB-API OYUN
- **Kontrol:** Kopunca otomatik yeniden bağlanma + backoff; yeniden bağlanınca kaçırılan olayların alınması; kimlik doğrulama (bağlantı açılırken token); heartbeat/ping; mesaj boyutu ve hız sınırı; dinleyicilerin ekran kapanınca kapatılması (Firestore listener dahil).
- **Geçer:** Bağlantı kopması ve geri gelmesi veri kaybı olmadan ele alınıyor.

### L. Gözlemlenebilirlik (loglama, izleme, alarm, hata takibi)

#### L-04 · Monitoring (metrik izleme) · 🟡 · 📈 · WEB-API BULUT
- **Kontrol:** İstek sayısı, hata oranı, gecikme (p50/p95/p99), kaynak kullanımı; Vercel Analytics/Observability, Firebase Performance, Grafana.
- **Geçer:** Temel "altın sinyaller" (trafik, hata, gecikme, doygunluk) görünüyor.

#### L-05 · Alarm (alerting) · 🟠 · 🚀 · WEB-API BULUT
- **Ne/Neden:** Sorunu kullanıcıdan önce sen öğrenmelisin.
- **Kontrol:** Hata oranı artışı, servis çökmesi, bütçe aşımı (R-01), sertifika bitişi için bildirim (e-posta/push/Slack); alarm yorgunluğu (çok gürültü) var mı.
- **Geçer:** Kritik durumlar için az ama anlamlı alarm kurulu.

#### L-09 · Ürün analitiği · 🟢 · 📈 · BULUT WEB-S WEB-API OYUN
- **Kontrol:** Hangi özellik kullanılıyor; gizlilik dostu mu (TelemetryDeck, Plausible, PostHog); kişisel veri göndermeden; onay (G-06).
- **Geçer:** Karar vermeye yetecek kadar, gizliliği bozmayacak kadar az veri.

#### L-10 · Güvenlik olaylarının loglanması · 🟡 · 🚀 · WEB-API BULUT
- **Ne/Neden:** Bir saldırı veya hesap ele geçirme olduğunda ne olduğunu sonradan anlayabilmek.
- **Kontrol:** Loglananlar: başarısız/başarılı giriş, şifre sıfırlama, rol değişikliği, yetkisiz erişim denemesi (403), rate limit tetiklenmesi, webhook imza hatası, hesap silme. Her kayıtta zaman, kullanıcı kimliği, IP (gerekiyorsa kısaltılmış), işlem; **sır içermez** (L-02). Kısa sürede çok sayıda başarısız giriş gibi örüntüler için alarm (L-05). Yönetim işlemleri (kod ve şifre değiştirme, tüm cihazlardan çıkış) kalıcı kaydediliyor mu; deneme ve kilit tablolarının saklama süresi belgeyle aynı mı, temizliği gerçekten çalışıyor mu (Bizim Site F10).
- **Geçer:** Güvenlik olayları ayrı ve aranabilir şekilde kayıtlı.

### M. Dayanıklılık ve felaket kurtarma

#### M-01 · Felaket kurtarma planı (RPO/RTO) · 🟡 · 🚀 · BULUT WEB-API
- **Ne/Neden:** RPO = en fazla ne kadar veri kaybını göze alıyorsun; RTO = ne kadar sürede geri dönersin. Hesap kapatılırsa, bölge çökerse, DB silinirse ne yapılır?
- **Geçer:** RPO/RTO yazılı; senaryo başına 3-5 adımlık plan (bkz. R-05 runbook).

#### M-02 · Zorunlu güncelleme (mobil) · 🟠 · 🏁 · BULUT OYUN
- **Ne/Neden:** Mobilde eski sürümler yıllarca yaşar. Uyumsuz API veya güvenlik açığı için eski sürümü "lütfen güncelleyin" ekranıyla durdurabilmelisin. **İlk sürüme eklenmeli**, sonradan eklenemez (eski sürümler kontrolü bilmez).
- **Kontrol:** Remote Config/uzak JSON ile `minimumVersion` kontrolü.
- **Geçer:** İlk sürümden itibaren minimum sürüm kontrolü var.

#### M-03 · Kill switch · 🟡 · 🚀 · BULUT WEB-API OYUN YZ
- **Ne/Neden:** Sorunlu veya pahalı bir özelliği deploy etmeden anında kapatmak (B-04 ile ilişkili).
- **Geçer:** Riskli özellikler uzaktan kapatılabiliyor.

#### M-05 · Bağımlı servis listesi ve tek hata noktası · 🟡 · 🚀 · BULUT WEB-API
- **Ne/Neden:** Hangi dış servisler (Firebase, TMDB, harita, ödeme, LLM) düşerse ne olur? Ücretsiz katman sınırına takılınca ne olur?
- **Geçer:** Dış bağımlılık listesi ve her birinin düşme davranışı yazılı.

### N. Kullanıcı deneyimi ve erişilebilirlik

#### N-04 · İnternet yokken davranış · 🟠 · 🏁 · BULUT WEB-S WEB-API OYUN
- **Kontrol:** Uçak modunda uygulamayı aç ve ana akışı dene. Çevrimdışı göstergesi, kuyruğa alınan yazmalar, önbellekten okuma, yavaş ağda (Network Link Conditioner / DevTools "Slow 3G") davranış.
- **Geçer:** Çevrimdışıyken çökme veya sessiz veri kaybı yok; kullanıcı durumu biliyor.

#### N-07 · Deep link ve URL'ler · 🟢 · 📈 · BULUT WEB-S WEB-API
- **Kontrol:** Universal Links/URL scheme; web'de her ekranın paylaşılabilir URL'si, yenileyince (F5) 404 olmaması (SPA rewrite kuralı); geçersiz linkte düzgün davranış.
- **Geçer:** Paylaşılan bağlantılar doğru ekrana gidiyor.

### R. Operasyon, maliyet ve bakım

#### R-01 · Maliyet ve bütçe alarmı · 🔴 · 🚀 · BULUT WEB-API YZ
- **Ne/Neden:** Sonsuz döngüdeki bir listener, kötüye kullanılan API ucu veya sızan anahtar bir gecede büyük fatura çıkarabilir.
- **Kontrol:** Google Cloud/Firebase bütçe uyarısı, Vercel spend management, LLM sağlayıcısında aylık harcama sınırı; ücretsiz katman sınırları ve aşılınca ne olacağı; okuma/yazma sayısını patlatan kod (render içinde sorgu, listener tekrar kaydı).
- **Geçer:** Her ücretli hesapta bütçe uyarısı veya sert limit var.

#### R-08 · SaaS harcama takibi ve otomasyonu · 🟠 · 🚀 · BULUT WEB-API YZ GELİR
- **Ne/Neden:** Birden çok ücretli servis (Firebase/GCP, Vercel, OpenAI/Anthropic, RevenueCat, Sentry, e-posta/SMS, harita, domain) zamanla görünmez maliyet yığını olur; beklenmeyen kullanım (döngüye giren kod, kötüye kullanım, sızan anahtar) faturaya ancak ay sonunda yansır.
- **Kontrol:**
  - Tüm ücretli servislerin listesi: plan, aylık beklenen tutar, ödeme yöntemi, yenileme tarihi (Obsidian proje notunda tablo).
  - Her serviste **harcama limiti** (mümkünse sert limit; yoksa bütçe) belirlenmiş mi.
  - Belirli tutarlarda kademeli uyarı (%50 / %80 / %100 gibi) e-posta veya push ile.
  - **Beklenmeyen API kullanımı uyarısı:** günlük istek/token sayısı normalin X katına çıkınca bildirim (GCP budget + Pub/Sub, sağlayıcı kullanım uyarıları, kendi sayaç + cron).
  - Mümkünse günlük/haftalık/aylık otomatik maliyet raporu (cron ile sağlayıcı faturalama API'lerinden çekip e-posta/bildirim).
  - Kritik eşikte otomatik bildirim; gerekiyorsa otomatik kısıtlama (kill switch M-03, rate limit sıkılaştırma).
- **Geçer:** Hangi servise ne ödendiği biliniyor; anormal artış aynı gün fark ediliyor.

#### R-02 · Alan adı, SSL ve sertifika takvimi · 🟠 · 🚀 · WEB-S WEB-API BULUT
- **Kontrol:** Domain yenileme tarihi ve otomatik yenileme, SSL otomatik mi, Apple Developer üyeliği, APNs anahtarı, Google Play hesabı.
- **Geçer:** Bitiş tarihleri biliniyor; otomatik yenileme açık.

#### R-03 · Hesap sahipliği ve erişim · 🟠 · 🚀 · BULUT WEB-API
- **Ne/Neden:** Kritik hesaplar (Firebase, Vercel, domain, GitHub, App Store Connect) 2FA ile korunmalı; kurtarma kodları güvenli yerde; tek bir kişiye bağımlılık.
- **Geçer:** Tüm kritik hesaplarda 2FA; kurtarma kodları saklı.

#### R-05 · Runbook ve operasyon notları · 🟡 · 🚀 · BULUT WEB-API
- **Ne/Neden:** "Site çöktü / DB silindi / anahtar sızdı / fatura patladı" anında adım adım ne yapılacağı. Stres anında düşünmek yerine okumak.
- **Geçer:** En olası 3-5 olay için kısa runbook var (Obsidian proje notunda olabilir).

#### R-06 · Altyapı kod olarak (IaC) ve yapılandırma kaydı · 🟢 · 📈 · BULUT WEB-API
- **Kontrol:** Firebase rules/indexes/functions repoda mı (konsoldan elle düzenleme yok); `vercel.json`, Terraform; DNS kayıtlarının bir kopyası.
- **Geçer:** Altyapı yapılandırması repodan yeniden kurulabilir.

### U. Yayınlamadan önce düzeltilecek ürün sorunları (ilk deneyim)

> Profil: `MAĞAZA` (ve kullanıcıya açılan her `WEB-S`/`WEB-API`/`OYUN`). Bu sorunlar inceleme reddi değil ama **ilk gün kullanıcı kaybı** demektir. "Yayın hazırlığı" fazında, mümkünse daha önce "İlk deneyim" fazında çözülür.

#### U-02 · Değer göstermeden kayıt istemek · 🟠 · 🏁 · MAĞAZA BULUT WEB-API
- **Düzeltme:** Önce uygulamanın faydasını yaşat; kaydı mümkün olduğunca geç ve **gerekçeli** iste ("Verilerini kaybetmemek için hesap oluştur"). Anonim/misafir mod, sonradan hesaba bağlama (Firebase anonymous auth → link).
- **Geçer:** Kullanıcı kayıt olmadan uygulamanın ana değerini görebiliyor.

#### U-10 · İnternet gidince beyaz ekran · 🔴 · 🚀 · MAĞAZA BULUT WEB-S WEB-API
- **Düzeltme:** Çevrimdışı ve hata durumu tasarla; kullanıcıya bağlantının koptuğunu açıkça bildir; önbellekteki veriyi göster; bağlantı gelince otomatik yenile (N-04, W-01, W-10).
- **Geçer:** Uçak modunda hiçbir ekran boş/sonsuz yükleme göstermiyor.

#### U-17 · Hesap silme yok veya bulunmuyor · 🔴 · 🚀 · MAĞAZA BULUT
- **Düzeltme:** T-01, E-05.

### X. Saldırgan gibi test (kendi uygulamanda güvenlik testi)

> Profil: `BULUT`, `WEB-API` (ve sunucusu olan `OYUN`). **Yalnızca yetkili olduğun kendi uygulamanda**, tercihen staging ortamında (B-03) ve test hesaplarıyla yapılır. Üretim verisine zarar verecek, başkasının hesabına dokunacak veya hizmeti düşürecek test yapılmaz. Ajan her testi önce kullanıcıya listeler, onay alır, sonuçları `Kontrol.md`'ye yazar. Bulunan açıklar 🔴 olarak ilgili maddeye bağlanır. Araçlar: tarayıcı DevTools, `curl`, Burp Suite Community / OWASP ZAP (yerel proxy), Firebase Rules Playground / emülatör.

#### X-04 · IDOR / bozuk erişim kontrolü testi · 🔴 · 🚀 · BULUT WEB-API
- **Nasıl:** İki test hesabı aç (A ve B). A ile oturum açıkken B'nin kaynak ID'lerini (URL, API gövdesi, Firestore doküman yolu) kullanarak okuma/güncelleme/silme dene. Liste uçlarında filtre parametresini kaldır. Firestore'da istemci SDK ile başka kullanıcının koleksiyonunu doğrudan sorgula.
- **Geçer:** Tüm denemeler reddediliyor (E-02, F-12).

#### X-05 · Kimlik doğrulama atlatma testi · 🔴 · 🚀 · BULUT WEB-API
- **Nasıl:** Korumalı uçlara token'sız, süresi dolmuş, başka kullanıcının, imzası bozulmuş token ile istek; sadece istemcide gizlenen sayfalara doğrudan URL ile git; e-posta doğrulanmadan korumalı işlem; şifre sıfırlama bağlantısını iki kez kullan.
- **Geçer:** Her durumda 401/403 (E-01, E-03).

#### X-06 · Yetki yükseltme testi · 🔴 · 🚀 · BULUT WEB-API
- **Nasıl:** Normal kullanıcıyla admin uçlarını çağır; profil güncelleme isteğine `role`, `isAdmin`, `plan: "premium"`, `ownerId` gibi alanlar ekle; Firestore'da kendi kullanıcı dokümanının rol alanını yaz; çalışan rolüyle patron işlemi dene.
- **Geçer:** Hiçbiri başarılı olmuyor (E-02, F-02).

#### X-07 · Brute force ve rate limit testi · 🟠 · 🚀 · BULUT WEB-API YZ
- **Nasıl:** Staging'de giriş, şifre sıfırlama, davet kodu doğrulama, e-posta/SMS gönderen ve LLM çağıran uçlara kısa sürede çok istek (makul sayıda; hizmet dışı bırakma amaçlı değil).
- **Geçer:** Sınır devreye giriyor (429), hesap/IP bazlı yavaşlatma var, olay loglanıyor (F-06, L-10).

#### X-08 · Dosya yükleme güvenliği testi · 🟠 · 🚀 · BULUT WEB-API
- **Nasıl:** Sınırdan büyük dosya; uzantısı `.jpg` ama içi HTML/SVG/script; `../../evil.png` dosya adı; çok sayıda yükleme; başka kullanıcının storage yoluna yükleme.
- **Geçer:** Hepsi reddediliyor (F-09, I-01).

#### X-11 · Oturum ele geçirme kontrolleri · 🟠 · 🚀 · WEB-API BULUT
- **Nasıl:** Çerez bayraklarını DevTools'ta kontrol et (`HttpOnly`, `Secure`, `SameSite`); çıkış yaptıktan sonra eski token/çerezle istek; şifre değiştikten sonra diğer cihazdaki oturum; girişten önce ve sonra oturum kimliği değişiyor mu.
- **Geçer:** E-03 maddeleri doğrulanmış.

#### X-14 · Hata mesajlarından bilgi sızması testi · 🟠 · 🚀 · WEB-API BULUT
- **Nasıl:** Bozuk JSON, yanlış tip, olmayan ID, çok büyük gövde gönder; yanıtta stack trace, SQL sorgusu, dosya yolu, framework sürümü, iç IP var mı; `X-Powered-By` başlığı.
- **Geçer:** Hatalar genel mesaj + istek kimliği döndürüyor; detay sadece sunucu logunda (F-07).

#### X-15 · İstemci tarafı güven testi · 🟠 · 🚀 · BULUT OYUN GELİR
- **Nasıl:** İstemci kodunda değiştirilebilecek değerleri değiştir: premium bayrağı (`UserDefaults`/localStorage `isPremium`), skor, fiyat, indirim, stok; proxy ile isteği düzenle. Firebase'de istemcinin yazabildiği alanları kurallar dışında dene.
- **Geçer:** Sunucu/kurallar değiştirilmiş değeri kabul etmiyor (V-11, F-17, Q-02).
