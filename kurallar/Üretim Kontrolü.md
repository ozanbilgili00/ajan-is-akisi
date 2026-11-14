---
tür: ana-kural
sürüm: 1.3
güncellendi: 2026-11-10
---

# Üretim Kontrolü: Ana Kural Dosyası

> **Bu dosya kaynaktır, baştan sona okunmaz.** Proje türüne göre bölünmüş hali `Kurallar/Üretim Kontrolü/` klasöründedir ([[Kurallar/Üretim Kontrolü/Rehber|Rehber]]): Web, Apple, Android, Oyun, Araç ve ek modüller. Parçalar bu dosyadan `~/.claude/hooks/uretim_bol.py` ile üretilir ve oturum başında kendiliğinden yenilenir. Madde eklemek ya da değiştirmek için yalnız burası düzenlenir.

Bu dosya, her projenin "buzdağının altında" kalan konularını (altyapı, güvenlik, veri, gözlem, operasyon, kullanıcı deneyimi, mağaza incelemesi, paywall, ASO, büyüme) denetlemek için **ana kaynaktır**. Ajanlar bu dosyayı okur, projeye uyarlar, maddeleri **proje fazlarına yayar** (Bölüm 8) ve projenin kendi kural dosyasını üretir. Bu dosyanın kendisi projelere kopyalanmaz; projeye uyarlanmış özeti yazılır.

**Mutlak yol:** `~/Desktop/hafıza/hafıza/Kurallar/Üretim Kontrolü.md`

**Okuma tasarrufu:** Dosya uzundur. Her seferinde tamamını okuma. Önce Bölüm 0, 1, 2 ve 8'i oku. Maddeler için başlıkları listele (`grep -n '^#### ' "Üretim Kontrolü.md"`), sonra sadece o fazın maddelerini oku (`grep -n -A6 '^#### T-0' ...` veya satır aralığıyla).

**İçindekiler:** 0 Ajan talimatı · 1 Profiller · 2 Önem/zamanlama · 3 Kontrol maddeleri (A Repo · B Ortam · C CI/CD · D Test · E Kimlik · F Güvenlik · G Gizlilik · H Veri · I Depolama · J Performans · K Asenkron · L Gözlem · M Dayanıklılık · N UX · O iOS · P Web · Q Oyun · R Operasyon/maliyet · S Yapay zekâ · T Apple incelemesi · U Yayın öncesi ürün düzeltmeleri · V Paywall ve gelir · W Kırma testi · X Saldırgan gibi test · Y ASO ve mağaza sayfası · Z Büyüme ve metrikler) · 4 Proje kural şablonu · 5 Rapor şablonu · 6 Tarama komutları · 7 Bakım · 8 Fazlara yayma

---

## 0. Ajan talimatı: bu dosyayı bir projeye nasıl uygularsın

Bir projede "üretim kontrolü kur", "kontrol kurallarını yaz" veya "projeyi denetle" dendiğinde şu sırayı izle:

1. **Projeyi tanı.** Obsidian notunu (`Projeler/<Ad>/<Ad>.md`, `Plan.md`) oku. Sonra repoyu tara: dil ve çatı, paket dosyaları (`package.json`, `Package.swift`, `*.xcodeproj`, `Packages/manifest.json`), backend var mı, veri nerede tutuluyor, kimlik doğrulama var mı, dağıtım nasıl yapılıyor.
2. **Profil seç.** Bölüm 1'deki profillerden bir veya birkaçını seç. Bir proje birden fazla profile girebilir (örn. çevrimiçi co-op oyun = `OYUN` + `WEB-API`).
3. **Aşamayı belirle.** `Prototip`, `Beta` (TestFlight / kapalı test) veya `Yayında`. Önem seviyeleri aşamaya göre yorumlanır (Bölüm 2).
4. **Her maddeyi değerlendir.** Bölüm 3'teki her madde için:
   - Profil etiketi projeye uymuyorsa → `➖ Uygulanmaz` (tek satır gerekçe yaz).
   - Uyuyorsa → maddenin **Kontrol** satırındaki adımları gerçekten uygula, kanıt topla (`dosya:satır`, komut çıktısı) ve durum ver: `✅ Var` · `⚠️ Kısmi` · `❌ Yok` · `❓ Bilinmiyor`.
   - Emin değilsen tahmin etme, `❓` yaz ve neyin doğrulanması gerektiğini belirt.
5. **Fazlara yay.** Uygulanan maddeleri Bölüm 8'e göre `Plan.md` fazlarına "Kontrol kapısı" olarak dağıt. Faz sırasında ve sonunda bu kapılar kullanılır.
6. **Proje kural dosyasını yaz.** Bölüm 4'teki şablonla projenin köküne `.claude/rules/uretim.md` yaz. Claude Code bu klasördeki kuralları otomatik yükler. Proje köküne yazamıyorsan `CLAUDE.md` içine "Üretim kuralları" bölümü olarak ekle. Bu dosya *kalıcı kurallar* içerir ("şunu her zaman yap / asla yapma"), denetim sonucu içermez.
7. **Denetim raporunu yaz.** Bölüm 5'teki şablonla Obsidian'da `Projeler/<Ad>/Kontrol.md` oluştur veya güncelle. ❌ ve ⚠️ maddelerden 🔴/🟠 olanları `Yapılacaklar.md` dosyasına "Sonra" altına `- [ ] [Üretim <ID>] ...` olarak ekle. `Günlük.md` dosyasına kısa kayıt düş.
8. **Kullanıcıya özet ver.** Kritik bulgular, en çok etki edecek ilk 3-5 iş, `➖` sayısı.

### Ajanın uyması gereken sınırlar
- **Denetim salt-okunurdur.** Bulguyu düzeltmek için kod değiştirme, paket kurma veya yapılandırma değiştirme; önce kullanıcıya sor. İstisna: kullanıcı açıkça "düzelt" dediyse.
- **Bulunan sırları asla yazdırma.** Rapora sadece `dosya:satır` ve türünü yaz (`Firebase API key`, `Stripe secret` gibi), değeri `****` ile maskele. Sızan bir sır bulduysan bunu ilk sıraya koy ve anahtarın **iptal edilip yenilenmesi** gerektiğini söyle; sadece silmek yetmez, git geçmişinde kalır.
- **Yıkıcı komut çalıştırma.** Veritabanına yazma, deploy, `git push`, `firebase deploy`, `rm`, geçmişi yeniden yazma yasak.
- **Kodu dış servise gönderme.** Çevrimiçi tarayıcılara/yapay zekâ servislerine kod veya sır yükleme.
- **Abartma.** Kişisel, iki kullanıcılı bir uygulamaya Kubernetes önerme. Her öneri profil ve aşamayla orantılı olmalı. "Uygulanmaz" demek başarısızlık değildir.
- **Kanıt göster.** "Var" diyorsan nerede olduğunu, "Yok" diyorsan nereye baktığını yaz.

---

## 1. Profiller

| Etiket | Tanım | Tipik örnek |
|---|---|---|
| `YEREL` | Sunucusu olmayan, veriyi cihazda tutan iOS/macOS uygulaması (SwiftData, UserDefaults, dosya) | Çevrimdışı takip uygulaması, pusula, menü çubuğu aracı |
| `BULUT` | Mobil/masaüstü uygulama + BaaS (Firebase, Supabase, CloudKit) veya üçüncü parti API | Paylaşımlı veri, giriş yapılan uygulama |
| `WEB-S` | Backend'i olmayan web uygulaması (SPA, statik site, localStorage) | React+Vite, Vercel'de statik |
| `WEB-API` | Kendi sunucusu/API'si/veritabanı olan web veya servis | Next.js + DB, Express API, serverless fonksiyonlar |
| `OYUN` | Oyun motoru projesi (Unity vb.), tek veya çok oyunculu | Unity mobil oyun |
| `ARAÇ` | CLI, kütüphane, MCP sunucusu, script, eklenti | npm paketi, MCP server |
| `YZ` | Projede LLM/yapay zekâ özelliği var (ek profil, diğerleriyle birlikte) | Sohbet, özetleme, öneri |
| `MAĞAZA` | App Store / Google Play'e çıkacak uygulama veya oyun (ek profil) | TestFlight'tan yayına giden her iOS uygulaması |
| `GELİR` | Uygulama içi satın alma, abonelik, paywall veya reklam geliri var (ek profil) | Premium abonelik, tek seferlik kilit açma, AdMob |
| `Hepsi` | Profil fark etmeksizin geçerli | |

> Profil birleşimi: Etiketlerden **herhangi biri** projeye uyuyorsa madde uygulanır. `MAĞAZA` ve `GELİR` ek profillerdir; ana profilin (YEREL/BULUT/OYUN) yanına eklenir. Kişisel kullanım için yapılan, mağazaya çıkmayacak uygulamalarda T, Y, Z kategorileri `➖` olur.
>
> **Android notu:** Projede Android hedefi varsa (Flutter, React Native, Kotlin, Unity Android) "(Android)" ile işaretli kontroller ve **AN** (Platform: Android) kategorisi de uygulanır; mağazaya çıkıyorsa T (Apple) yerine ya da onunla birlikte **GP** (Google Play incelemesi) uygulanır. Android hedefi yoksa AN ve GP `➖` olur. Aynı şekilde O ve T kategorileri yalnız iOS ve macOS hedefinde uygulanır.

---

## 2. Önem seviyesi, zamanlama ve aşama

**Önem**
- 🔴 **Kritik:** Veri kaybı, güvenlik açığı, mağaza reddi veya yasal sorun yaratır. `Yayında` aşamasında bunlar yayın engelidir.
- 🟠 **Yüksek:** Kullanıcıyı doğrudan etkiler veya sorun çıktığında körsün. Yayından önce çözülmeli.
- 🟡 **Orta:** Kaliteyi ve bakım kolaylığını artırır. Yol haritasına alınmalı.
- 🟢 **Düşük:** İyi olur. Ölçek veya ekip büyüyünce.

**Zamanlama**
- 🏁 **Baştan:** Sonradan eklemek pahalıdır (veri modeli, kimlik, migration stratejisi, UTC, yerelleştirme altyapısı). Prototipte bile kararı verilmeli.
- 🚀 **Yayından önce.**
- 📈 **Büyüyünce:** Kullanıcı/yük arttığında.

**Aşamaya göre yorum**
- `Prototip`: Sadece 🔴 + 🏁 maddeleri zorunlu, gerisi not edilir.
- `Beta`: 🔴 ve 🟠 + 🚀 maddeleri zorunlu.
- `Yayında`: 🔴 ve 🟠 tamamı zorunlu; 🟡 planlanmış olmalı.

Ajan bir maddenin varsayılan önemini proje bağlamına göre **bir kademe** yükseltebilir veya düşürebilir; gerekçeyi raporda yazar.

---

## 3. Kontrol maddeleri

Biçim: `ID · Başlık · önem · zamanlama · profiller`, ardından **Ne/Neden**, **Kontrol**, **Geçer ölçütü**.

---

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

---

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

#### B-05 · Debug kodunun prod'a sızmaması · 🟠 · 🚀 · Hepsi
- **Ne/Neden:** Test menüleri, sahte veri, `print`/`console.log` ile hassas veri, devre dışı güvenlik kontrolleri yayına çıkmamalı.
- **Kontrol:** `grep -rnE '#if DEBUG|isDebug|TODO|FIXME|HACK|console\.log|print\('`; debug-only kodun `#if DEBUG` veya `import.meta.env.DEV` ile korunması.
- **Geçer:** Release derlemesinde debug davranışı yok.

---

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

#### C-04 · Docker / konteyner · 🟢 · 📈 · WEB-API
- **Ne/Neden:** Sunucuyu her ortamda aynı şekilde çalıştırmak. Serverless/Vercel kullanılıyorsa genelde gerekmez.
- **Kontrol:** `Dockerfile`, `docker-compose.yml`; imaj küçük mü (multi-stage), root olarak mı çalışıyor, sırlar imaja gömülü mü.
- **Geçer:** Sunucu varsa konteyner tanımı var, root değil, sır içermiyor. Serverless ise `➖`.

#### C-05 · Kubernetes / orkestrasyon · 🟢 · 📈 · WEB-API
- **Ne/Neden:** Çok sayıda servis ve yüksek trafik için. Kişisel ve küçük projelerde **neredeyse her zaman gereksiz**; önermek abartıdır.
- **Kontrol:** Sadece birden fazla servis + yatay ölçek ihtiyacı varsa değerlendir.
- **Geçer:** Gerekmiyorsa `➖` ve gerekçe ("tek servis, serverless").

#### C-06 · Sürümleme ve CHANGELOG · 🟡 · 🚀 · Hepsi
- **Ne/Neden:** Hangi sürümde ne değişti, hangi sürüme geri dönülecek, bilinmeli.
- **Kontrol:** Semver (`MAJOR.MINOR.PATCH`), iOS'ta `CFBundleShortVersionString` + artan build numarası, git tag, `CHANGELOG.md`.
- **Geçer:** Her yayın etiketli ve değişiklikleri yazılı.

#### C-07 · Rollback (geri alma) · 🟠 · 🚀 · WEB-S WEB-API BULUT
- **Ne/Neden:** Bozuk sürüm çıktığında dakikalar içinde önceki sürüme dönebilmek.
- **Kontrol:** Vercel "instant rollback", önceki deploy'u yeniden yayınlama, Firebase rules sürüm geçmişi; veritabanı migration'ının geri alınabilirliği (bkz. H-03). Mobilde gerçek rollback yoktur → kill switch / feature flag (M-03).
- **Geçer:** Geri dönüş yolu biliniyor ve en az bir kez denenmiş.

---

### D. Test ve kod kalitesi

#### D-01 · Birim testleri · 🟠 · 🚀 · Hepsi
- **Ne/Neden:** İş mantığı (hesaplamalar, tarih işlemleri, dönüştürücüler, kurallar) testlenmeli; en çok hata buradan çıkar.
- **Kontrol:** Test hedefi var mı (`*Tests/`, `*.test.ts`, Unity Test Runner); testler geçiyor mu (çalıştır); kritik mantık (ödeme, döngü hesabı, namaz vakti, puanlama vb.) kapsanmış mı.
- **Geçer:** Kritik iş mantığının testi var ve yeşil.

#### D-02 · Entegrasyon testleri · 🟡 · 🚀 · BULUT WEB-API
- **Ne/Neden:** Bileşenler birlikte doğru çalışıyor mu (API + DB, uygulama + Firebase emülatörü, güvenlik kuralları).
- **Kontrol:** Emülatörle çalışan testler, Firestore rules testleri (`@firebase/rules-unit-testing`), API uç nokta testleri.
- **Geçer:** Kritik akışlar (giriş, veri yazma, yetkisiz erişimin reddi) testli.

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

#### D-08 · Yük / stres testi · 🟢 · 📈 · WEB-API
- **Ne/Neden:** Beklenen trafiğin 2-3 katında ne olur?
- **Kontrol:** k6, autocannon, Artillery.
- **Geçer:** Hedef yükte gecikme ve hata oranı kabul edilebilir.

#### D-09 · Kod incelemesi · 🟢 · 📈 · Hepsi
- **Ne/Neden:** Tek kişilik projede bile büyük değişiklikten önce `/code-review` veya ikinci bir göz.
- **Geçer:** Kritik değişiklikler incelemeden geçiyor.

---

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

---

### F. API ve uygulama güvenliği

#### F-01 · Sır taraması (git geçmişi dahil) · 🔴 · 🏁 · Hepsi
- **Ne/Neden:** Silinen anahtar git geçmişinde yaşamaya devam eder.
- **Kontrol:** `gitleaks detect` veya `git log -p | grep -nE 'AKIA[0-9A-Z]{16}|sk_(live|test)_|sk-ant-|sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{35}|-----BEGIN (RSA |EC )?PRIVATE KEY|ghp_[A-Za-z0-9]{36}|xox[bp]-'`. Bulunanları **maskele**.
- **Düzeltme sırası (sır bulunursa):** 1) Anahtarı sağlayıcıda **iptal et ve yenisini üret (rotate)**. 2) Yeni anahtarı `.env` / secret manager'a (Vercel env, GitHub Secrets, Google Secret Manager, 1Password, iOS'ta sunucu tarafı) koy. 3) Koddan kaldır. 4) Gerekirse geçmişi `git filter-repo` / BFG ile temizle (**yıkıcı**, kullanıcı onayı şart; uzak repo zorla push gerektirir). Sadece 3. adım yetmez.
- **Geçer:** Geçmişte ve çalışma ağacında gizli anahtar yok; varsa iptal edilip yenilenmiş. Veritabanı kimlik bilgileri (DB credentials, connection string) kodda değil.

#### F-02 · Girdi doğrulama · 🔴 · 🏁 · BULUT WEB-API WEB-S
- **Ne/Neden:** Kullanıcıdan gelen her veri (form, URL parametresi, API gövdesi, dosya) şema ile doğrulanmalı: tip, uzunluk, aralık, biçim.
- **Kontrol:** Zod/Valibot/Joi kullanımı, Firestore rules'ta alan doğrulaması (`request.resource.data.keys().hasOnly([...])`, tip ve boyut kontrolleri); **beklenmeyen alanlar ve tipler reddediliyor mu** (sayı yerine string, dizi yerine nesne, fazladan `isAdmin` alanı — mass assignment); `null`, boş string, çok uzun string, negatif sayı, emoji/Unicode, büyük JSON gövdesi denenmiş mi.
- **Geçer:** Tüm girdiler **sunucuda** şema ile doğrulanıyor, bilinmeyen alanlar atılıyor veya reddediliyor; istemci doğrulaması sadece kullanıcı deneyimi içindir.

#### F-03 · Enjeksiyon (SQL / NoSQL / komut) · 🔴 · 🏁 · WEB-API ARAÇ
- **Kontrol:** String birleştirerek sorgu (`"SELECT ... " + x`, template literal ile SQL), `exec`/`spawn` ile kullanıcı girdisi, `eval`, `new Function`.
- **Geçer:** Parametreli sorgu/ORM; kabuk komutlarına girdi kaçışlı veya argüman dizisiyle veriliyor.

#### F-04 · XSS · 🔴 · 🏁 · WEB-S WEB-API
- **Kontrol:** `dangerouslySetInnerHTML`, `innerHTML`, `v-html`, markdown'ın temizlenmeden render edilmesi; kullanıcı içeriği (yorum, isim) render ediliyor mu; `href`'e kullanıcı URL'si (`javascript:` şeması); çıktı bağlama göre encode ediliyor mu (HTML, attribute, URL, JS); e-posta şablonlarında ve PDF/rapor üretiminde kullanıcı verisi.
- **Geçer:** Kullanıcı içeriği bağlama uygun encode ediliyor; HTML/Markdown kabul eden alanlar **ayrıca** DOMPurify/sanitize-html ile izin listesi üzerinden temizleniyor.

#### F-05 · CORS ve CSRF · 🟠 · 🚀 · WEB-API
- **Kontrol:** `Access-Control-Allow-Origin: *` + kimlik bilgisi; çerez tabanlı oturumda CSRF token veya `SameSite`.
- **Geçer:** CORS sadece **kendi domain'lerine** kilitli (joker yok, `Origin` başlığını olduğu gibi geri yansıtma yok); durum değiştiren istekler CSRF'e karşı korumalı; GET istekleri durum değiştirmiyor.

#### F-06 · Rate limiting · 🟠 · 🚀 · BULUT WEB-API YZ
- **Ne/Neden:** Giriş, kayıt, şifre sıfırlama, e-posta/SMS gönderen ve ücretli API çağıran uçlar kötüye kullanılabilir (fatura patlaması).
- **Kontrol:** Middleware (Upstash ratelimit, express-rate-limit), Vercel Firewall kuralları, Firebase App Check, Cloud Functions için kota. Genel (hesaptan bağımsız) giriş kilidi varsa: IP değiştiren biri herkesi kilitleyebilir mi, kilidi açan yönetim işlemi ve kilitlenince bildirim var mı (Bizim Site F10).
- **Geçer:** Hassas ve pahalı uçlar IP/kullanıcı başına sınırlı.

#### F-07 · API güvenliği genel · 🟠 · 🚀 · WEB-API BULUT
- **Kontrol:** Hata yanıtlarında stack trace/iç bilgi sızıyor mu; gereksiz alanlar dönüyor mu (şifre hash, e-posta listesi); toplu veri çekme sınırı; HTTP metotları doğru mu; API sürümleme.
- **Geçer:** API sadece gerekeni döndürüyor, hata mesajları genel.

#### F-08 · Güvenlik başlıkları ve CSP · 🟡 · 🚀 · WEB-S WEB-API
- **Kontrol:** (`vercel.json` → `headers`, `next.config` headers, securityheaders.com ile dış tarama)
  - `Strict-Transport-Security: max-age=31536000; includeSubDomains` (HSTS); HTTP → HTTPS yönlendirmesi (P-01).
  - `Content-Security-Policy`: en azından `default-src 'self'`, script kaynakları izin listesinde, `unsafe-inline`/`unsafe-eval` mümkünse yok; önce `Content-Security-Policy-Report-Only` ile dene.
  - `X-Content-Type-Options: nosniff`.
  - `Referrer-Policy: strict-origin-when-cross-origin`.
  - `Permissions-Policy`: kullanılmayan kamera/mikrofon/konum kapalı (`camera=(), microphone=(), geolocation=()`).
  - Clickjacking koruması: CSP `frame-ancestors 'none'` (veya `'self'`) + eski tarayıcılar için `X-Frame-Options: DENY`.
- **Geçer:** Tüm başlıklar ayarlı; securityheaders.com en az A.

- **Ders (Bizim Site F10):** CSP'de joker alt alan adı (`https://*.supabase.co`) kullanma, proje adresini yaz. Başlık testi yalnız tam `*` değerine bakıyorsa jokeri kaçırır; test kaynak listesindeki her `*` karakterini yakalamalı.

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

#### F-10 · SSRF ve dış URL çekme · 🟡 · 🚀 · WEB-API YZ
- **Kontrol:** Kullanıcının verdiği URL'yi sunucu çekiyorsa iç ağ adresleri (`169.254.*`, `localhost`, `10.*`) engelli mi.
- **Geçer:** Dış istekler izin listesiyle sınırlı.

#### F-11 · Bağımlılık güvenliği · 🟠 · 🚀 · Hepsi
- **Kontrol:** `npm audit --omit=dev` (veya `pnpm audit`, `pip-audit`, `bundle audit`), GitHub Dependabot alerts, bilinen CVE'ler (osv.dev, `osv-scanner`), **kullanılmayan paketler** (`npx depcheck`, `knip`), terk edilmiş/az bilinen paketler, `postinstall` script'leri, typosquatting, lockfile kullanımı (A-03), düzenli güncelleme (R-04).
- **Geçer:** Yüksek/kritik açık yok; kullanılmayan paket yok; bağımlılık sayısı makul.

#### F-12 · BaaS güvenlik kuralları (Firebase/Supabase) · 🔴 · 🏁 · BULUT
- **Ne/Neden:** Firestore/Storage/RTDB kuralları veritabanının tek kapısıdır. `allow read, write: if true;` veya `if request.auth != null;` tek başına **açık kapıdır** (her giriş yapan herkesin verisini okur).
- **Kontrol:** `firestore.rules`, `storage.rules`, `database.rules.json`; test modu süresi; koleksiyon bazlı sahiplik; alan doğrulama; liste sorgularının sınırlanması; Supabase'de RLS her tabloda açık mı.
- **Geçer:** Varsayılan red; her koleksiyon için sahiplik + şema doğrulaması; kurallar test edilmiş (D-02).

#### F-13 · Şifreleme (aktarımda ve depoda) · 🟠 · 🏁 · Hepsi
- **Kontrol:** Tüm ağ trafiği HTTPS/WSS (iOS ATS istisnası `NSAllowsArbitraryLoads` var mı); hassas yerel veri için iOS Data Protection (`.completeFileProtection`), Keychain; sağlık/regl/finans gibi hassas veride ekstra şifreleme ihtiyacı.
- **Geçer:** Düz HTTP yok; hassas veri korumalı sınıfta veya şifreli.

#### F-14 · Firewall / ağ erişimi · 🟡 · 📈 · WEB-API
- **Kontrol:** Veritabanı internete açık mı (IP izin listesi), yönetim panelleri herkese açık mı, Vercel Firewall/WAF, açık portlar.
- **Geçer:** DB ve iç servisler doğrudan internete açık değil.

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

#### F-19 · İstek boyutu ve kaynak sınırları · 🟠 · 🚀 · WEB-API
- **Kontrol:** İstek gövdesi boyut sınırı (`express.json({ limit: '100kb' })`, Next.js `bodySizeLimit`), dizi eleman sayısı, sorgu derinliği (GraphQL), regex ile DoS (ReDoS), sayfa boyutu üst sınırı (`?limit=1000000`). Satır ve adet sınırı tetikleyiciyle konduysa yalnız `insert`te değil `update`te de çalışıyor mu (alan değiştirerek sınır aşılabiliyor mu); kullanıcı başına kayıt adedi sınırı var mı (Bizim Site F10).
- **Geçer:** Tek bir istek sunucuyu yoracak kadar büyük olamıyor.

#### F-20 · Hassas uç noktaların korunması · 🟠 · 🚀 · WEB-API BULUT
- **Ne/Neden:** Admin panelleri, debug uçları, seed/test endpoint'leri, `/api/internal/*`, Swagger/GraphQL introspection, `.git/`, `.env`, kaynak harita (source map) dosyaları üretimde "gizli URL" diye korumasız bırakılır. Gizlilik güvenlik değildir.
- **Kontrol:** Tüm route listesini çıkar ve her birinde kimlik + yetki kontrolü var mı bak (**API authentication** her uçta); `curl https://site/.env`, `/.git/config`, `/api/debug`; üretimde source map herkese açık mı; admin uçları için ek koruma (IP izin listesi, 2FA, ayrı alt alan).
- **Geçer:** Kimliksiz erişilebilen her uç bilinçli olarak açık; debug/test uçları üretimde yok.

---

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

#### G-05 · Veri dışa aktarma ve taşınabilirlik · 🟡 · 🚀 · YEREL BULUT WEB-API
- **Ne/Neden:** Kullanıcı verisini alabilmeli (KVKK hakkı; ayrıca çevrimdışı uygulamada cihaz değişimi için tek kurtuluş).
- **Geçer:** Dışa aktarma (JSON/CSV) veya iCloud yedeği ile veri taşınabiliyor.

#### G-06 · Onay ve çerezler · 🟡 · 🚀 · WEB-S WEB-API
- **Kontrol:** Analitik/izleme çerezleri onaysız yükleniyor mu.
- **Geçer:** Zorunlu olmayan izleme onaya bağlı veya gizlilik dostu (çerezsiz) analitik.

#### G-07 · Lisanslar ve kullanım şartları · 🟠 · 🚀 · Hepsi
- **Kontrol:** Açık kaynak bağımlılık lisansları (GPL'in kapalı uygulamaya etkisi), font lisansları, Unity Asset Store/Sketchfab/Poly Haven model lisansları (CC-BY ise atıf), veri kaynakları (TMDB atıf zorunluluğu, kamu verisi kullanım şartları), görsel/ikon lisansları, yapay zekâ ile üretilmiş içerik.
- **Geçer:** Her dış varlığın lisansı biliniyor; atıf gerekenler "Hakkında/Teşekkürler" ekranında.

#### G-08 · Yaş sınırı ve içerik · 🟡 · 🚀 · BULUT WEB-API OYUN
- **Kontrol:** Kullanıcı üretimli içerik varsa App Store Guideline 1.2 (raporlama, engelleme, filtre); yaş derecelendirmesi doğru mu.
- **Geçer:** Kullanıcı içeriği için şikâyet/engelleme mekanizması var.

---

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

#### H-12 · Veri bütünlüğü doğrulaması · 🟡 · 🚀 · Hepsi (veri tutan)
- **Kontrol:** Bozuk/eksik veri okununca uygulama çöküyor mu (decode hatası → `try?` ile sessiz kayıp mı, kullanıcıya bilgi mi); localStorage'ın elle bozulması; JSON şema doğrulaması.
- **Geçer:** Bozuk veri uygulamayı çökertmiyor ve sessizce silinmiyor.

#### H-13 · Sharding / bölümleme · 🟢 · 📈 · WEB-API
- **Ne/Neden:** Tek veritabanı yetmeyecek kadar büyük ölçek için. Küçük projelerde **gereksiz**.
- **Geçer:** Gerekmiyorsa `➖`. Firestore'da "hot document" (saniyede 1+ yazma alan tek doküman) varsa dağıtık sayaç kullanılıyor.

---

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

#### I-04 · CDN · 🟡 · 🚀 · WEB-S WEB-API
- **Kontrol:** Statik varlıklar CDN'den mi (Vercel/Cloudflare otomatik), cache başlıkları, hash'li dosya adları.
- **Geçer:** Statik içerik CDN'de, uzun süreli önbellekli, hash'li.

#### I-05 · Yerel depolama sınırları · 🟡 · 🏁 · WEB-S YEREL
- **Ne/Neden:** localStorage ~5 MB ile sınırlıdır, senkron çalışır ve tarayıcı tarafından silinebilir (Safari ITP 7 gün kuralı). Büyük veya kritik veri için IndexedDB, mümkünse sunucu. iOS'ta `Caches/` dizini sistem tarafından silinebilir.
- **Kontrol:** localStorage'a yazılan veri boyutu, `QuotaExceededError` yakalanıyor mu, kalıcı veri doğru dizinde mi (`Application Support`, `Documents`).
- **Geçer:** Kritik veri silinebilir bir yerde değil; kota hatası ele alınmış.

---

### J. Performans ve ölçek

#### J-01 · Performans bütçesi · 🟡 · 🚀 · Hepsi
- **Ne/Neden:** "Hızlı" ölçülebilir olmalı: açılış süresi, ilk etkileşim, API p95 gecikmesi, FPS.
- **Geçer:** Hedef sayılar yazılı ve ölçülüyor.

#### J-02 · Önbellek (cache) · 🟡 · 📈 · BULUT WEB-S WEB-API
- **Kontrol:** Tekrarlanan pahalı istekler önbellekleniyor mu (HTTP cache, `URLCache`, React Query/SWR, Redis, Next.js cache, görsel cache); üçüncü parti API kotaları (TMDB) önbellek ile korunuyor mu.
- **Geçer:** Sık ve pahalı veri önbellekli.

#### J-03 · Önbellek geçersiz kılma (cache invalidation) · 🟠 · 📈 · BULUT WEB-S WEB-API
- **Ne/Neden:** Bayat veri göstermek, önbelleğin en sık hatasıdır.
- **Kontrol:** Her önbellek için TTL veya olay tabanlı temizleme; yazma sonrası ilgili cache temizleniyor mu; deploy sonrası eski JS paketi ile yeni API uyumsuzluğu; service worker eski sürümde takılıyor mu.
- **Geçer:** Her önbelleğin ne zaman geçersiz olduğu tanımlı.

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

#### J-08 · Web performansı · 🟡 · 🚀 · WEB-S WEB-API
- **Kontrol:** Core Web Vitals (LCP < 2.5 sn, INP < 200 ms, CLS < 0.1), bundle boyutu (`vite build` raporu, rollup-plugin-visualizer), kod bölme (`lazy()`), font yükleme (`font-display: swap`), gereksiz büyük bağımlılık (moment, lodash tamamı).
- **Geçer:** Lighthouse mobil performans ≥ 80; ilk JS paketi makul (< ~200 KB gzip).

#### J-09 · Oyun performansı · 🟠 · 🚀 · OYUN
- **Kontrol:** Hedef cihazda FPS (30/60), draw call, batching, LOD, occlusion culling, GC allocation/frame, shader varyant sayısı, Profiler.
- **Geçer:** En zayıf hedef cihazda hedef FPS sabit.

#### J-10 · Load balancer / proxy / yatay ölçek · 🟢 · 📈 · WEB-API
- **Ne/Neden:** Birden fazla sunucu örneğine trafik dağıtmak. Serverless/Vercel bunu otomatik yapar; kendi sunucunda gerekir.
- **Kontrol:** Sunucu durumsuz mu (oturum bellekte değil, paylaşılan store'da); reverse proxy (nginx/Caddy) ayarları, gerçek IP başlığı, timeout değerleri.
- **Geçer:** Gerekmiyorsa `➖`; gerekiyorsa sunucular durumsuz ve dengeleniyor.

#### J-11 · Soğuk başlangıç ve serverless sınırları · 🟡 · 🚀 · WEB-API
- **Kontrol:** Fonksiyon süre sınırı, bellek, cold start, bağlantı havuzu (serverless'ta DB bağlantı patlaması → pooler kullan).
- **Geçer:** Uzun işler fonksiyon süresini aşmıyor; DB bağlantıları havuzlu.

---

### K. Asenkron işler, kuyruklar ve gerçek zamanlı iletişim

#### K-01 · Timeout · 🟠 · 🏁 · Hepsi (ağ kullanan)
- **Ne/Neden:** Timeout'suz istek sonsuza kadar bekler ve UI'yi/kaynakları kilitler.
- **Kontrol:** `URLSession` `timeoutIntervalForRequest`, `fetch` + `AbortController`, DB sorgu timeout'u, harici API çağrıları.
- **Geçer:** Her dış çağrının makul bir timeout'u var.

#### K-02 · Retry ve üstel geri çekilme · 🟠 · 🚀 · BULUT WEB-API OYUN
- **Kontrol:** Geçici hatalarda (ağ, 429, 5xx) yeniden deneme var mı; exponential backoff + jitter; deneme üst sınırı; 4xx hatalar yeniden denenmiyor mu; tekrar denenen işlem idempotent mi (H-09).
- **Geçer:** Geçici hatalar sınırlı ve geri çekilmeli şekilde yeniden deneniyor.

#### K-03 · Circuit breaker ve kısmi çalışma (graceful degradation) · 🟡 · 📈 · BULUT WEB-API
- **Ne/Neden:** Bir dış servis düştüğünde tüm uygulama çökmemeli; o bölüm "şu an kullanılamıyor" demeli, gerisi çalışmalı.
- **Geçer:** Dış servis hatası izole ediliyor; kullanıcı anlamlı mesaj görüyor.

#### K-04 · Arka plan işleri (background jobs) · 🟡 · 🚀 · WEB-API BULUT YEREL
- **Ne/Neden:** E-posta, bildirim, rapor, görsel işleme gibi uzun işler istek içinde yapılmamalı.
- **Kontrol:** Sunucu: Vercel Cron/Queues, Cloud Functions tetikleyicileri, BullMQ. iOS: `BGTaskScheduler`, `BGAppRefreshTask`, background modes'un gerçekten gerekip gerekmediği.
- **Geçer:** Uzun işler arka planda; iOS arka plan modları sadece gerekenler.

#### K-05 · Kuyruk / mesaj kuyruğu · 🟢 · 📈 · WEB-API
- **Ne/Neden:** Servisleri ayırmak, yük patlamalarını yumuşatmak, işleri kaybetmemek.
- **Kontrol:** Kuyruk varsa: dead letter queue (başarısız mesajlar nereye gidiyor), en az bir kez teslim → idempotent tüketici, sıra garantisi gerekiyor mu.
- **Geçer:** Gerekmiyorsa `➖`; varsa DLQ ve idempotent tüketici.

#### K-06 · Zamanlanmış işler (cron) · 🟡 · 🚀 · WEB-API BULUT
- **Kontrol:** Cron çakışması (önceki iş bitmeden yenisi başlıyor mu), saat dilimi, başarısız olunca haber veriliyor mu, aynı iş iki kez çalışırsa sorun olur mu.
- **Geçer:** Cron işleri izleniyor ve tekrar güvenli.

#### K-07 · WebSocket / gerçek zamanlı · 🟠 · 🚀 · BULUT WEB-API OYUN
- **Kontrol:** Kopunca otomatik yeniden bağlanma + backoff; yeniden bağlanınca kaçırılan olayların alınması; kimlik doğrulama (bağlantı açılırken token); heartbeat/ping; mesaj boyutu ve hız sınırı; dinleyicilerin ekran kapanınca kapatılması (Firestore listener dahil).
- **Geçer:** Bağlantı kopması ve geri gelmesi veri kaybı olmadan ele alınıyor.

#### K-08 · Bildirimler (push / yerel) · 🟡 · 🚀 · YEREL BULUT OYUN
- **Kontrol:** İzin doğru anda isteniyor; APNs anahtarı/sertifika süresi; token yenilemesi; yerel bildirimlerde 64 adet sınırı (iOS) ve saat dilimi değişimi; bildirime tıklayınca doğru ekrana gitme.
- **Geçer:** Bildirimler güvenilir, doğru zamanda ve doğru hedefe.

---

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

#### L-04 · Monitoring (metrik izleme) · 🟡 · 📈 · WEB-API BULUT
- **Kontrol:** İstek sayısı, hata oranı, gecikme (p50/p95/p99), kaynak kullanımı; Vercel Analytics/Observability, Firebase Performance, Grafana.
- **Geçer:** Temel "altın sinyaller" (trafik, hata, gecikme, doygunluk) görünüyor.

#### L-05 · Alarm (alerting) · 🟠 · 🚀 · WEB-API BULUT
- **Ne/Neden:** Sorunu kullanıcıdan önce sen öğrenmelisin.
- **Kontrol:** Hata oranı artışı, servis çökmesi, bütçe aşımı (R-01), sertifika bitişi için bildirim (e-posta/push/Slack); alarm yorgunluğu (çok gürültü) var mı.
- **Geçer:** Kritik durumlar için az ama anlamlı alarm kurulu.

#### L-06 · Health check ve uptime · 🟡 · 🚀 · WEB-API WEB-S
- **Kontrol:** `/health` veya `/api/health` ucu (DB bağlantısını da kontrol eden); harici uptime izleyici (UptimeRobot, Better Stack).
- **Geçer:** Site/API çökünce dışarıdan fark ediliyor.

#### L-07 · Availability / SLO · 🟢 · 📈 · WEB-API
- **Ne/Neden:** Hedef erişilebilirlik (%99, %99.9) ve hata bütçesi. Kişisel projede çoğu zaman `➖`.
- **Geçer:** Gerekiyorsa SLO tanımlı ve ölçülüyor.

#### L-08 · Dağıtık izleme (tracing / observability) · 🟢 · 📈 · WEB-API
- **Ne/Neden:** Bir isteğin birden fazla servis içindeki yolculuğunu görmek (OpenTelemetry).
- **Geçer:** Çok servisli sistemlerde istek kimliği uçtan uca taşınıyor; tek servisse `➖`.

#### L-09 · Ürün analitiği · 🟢 · 📈 · BULUT WEB-S WEB-API OYUN
- **Kontrol:** Hangi özellik kullanılıyor; gizlilik dostu mu (TelemetryDeck, Plausible, PostHog); kişisel veri göndermeden; onay (G-06).
- **Geçer:** Karar vermeye yetecek kadar, gizliliği bozmayacak kadar az veri.

#### L-10 · Güvenlik olaylarının loglanması · 🟡 · 🚀 · WEB-API BULUT
- **Ne/Neden:** Bir saldırı veya hesap ele geçirme olduğunda ne olduğunu sonradan anlayabilmek.
- **Kontrol:** Loglananlar: başarısız/başarılı giriş, şifre sıfırlama, rol değişikliği, yetkisiz erişim denemesi (403), rate limit tetiklenmesi, webhook imza hatası, hesap silme. Her kayıtta zaman, kullanıcı kimliği, IP (gerekiyorsa kısaltılmış), işlem; **sır içermez** (L-02). Kısa sürede çok sayıda başarısız giriş gibi örüntüler için alarm (L-05). Yönetim işlemleri (kod ve şifre değiştirme, tüm cihazlardan çıkış) kalıcı kaydediliyor mu; deneme ve kilit tablolarının saklama süresi belgeyle aynı mı, temizliği gerçekten çalışıyor mu (Bizim Site F10).
- **Geçer:** Güvenlik olayları ayrı ve aranabilir şekilde kayıtlı.

---

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

#### M-04 · Graceful shutdown · 🟢 · 📈 · WEB-API ARAÇ
- **Kontrol:** `SIGTERM` gelince yeni istek almayı bırakıp mevcutları bitirme; DB bağlantılarını kapatma; MCP/CLI süreçlerinde temiz çıkış.
- **Geçer:** Kapanırken yarım iş/bozuk veri kalmıyor.

#### M-05 · Bağımlı servis listesi ve tek hata noktası · 🟡 · 🚀 · BULUT WEB-API
- **Ne/Neden:** Hangi dış servisler (Firebase, TMDB, harita, ödeme, LLM) düşerse ne olur? Ücretsiz katman sınırına takılınca ne olur?
- **Geçer:** Dış bağımlılık listesi ve her birinin düşme davranışı yazılı.

#### M-06 · Uygulama içi veri koruması (yerel) · 🟠 · 🏁 · YEREL
- **Ne/Neden:** Sunucusuz uygulamada veri tek kopyadır; uygulama silinirse veya cihaz değişirse gider.
- **Kontrol:** iCloud yedeğe dahil mi, CloudKit senkron seçeneği, dışa/içe aktarma (G-05), migration hatasında veriyi silmek yerine korumaya alma (H-03).
- **Geçer:** Kullanıcının veriyi kaybetmeden cihaz değiştirmesinin en az bir yolu var.

---

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

#### N-05 · Karanlık mod ve tema · 🟡 · 🚀 · YEREL BULUT WEB-S WEB-API
- **Kontrol:** Sabit renkler (`Color.white`, `#fff`) yerine semantik renkler/asset catalog/CSS değişkenleri; her iki modda kontrast.
- **Geçer:** İki modda da okunaklı ve tutarlı.

#### N-06 · Duyarlı (responsive) düzen ve cihaz çeşitliliği · 🟡 · 🚀 · Hepsi (UI olan)
- **Kontrol:** Web: 320 px genişlikte yatay kaydırma yok, dokunmatik hedefler. iOS: en küçük iPhone (SE), en büyük, iPad (destekleniyorsa), yatay mod, Dynamic Island/çentik, güvenli alanlar. Oyun: farklı en-boy oranları, çentik.
- **Geçer:** Desteklenen en küçük ve en büyük ekranda düzen bozulmuyor.

#### N-07 · Deep link ve URL'ler · 🟢 · 📈 · BULUT WEB-S WEB-API
- **Kontrol:** Universal Links/URL scheme; web'de her ekranın paylaşılabilir URL'si, yenileyince (F5) 404 olmaması (SPA rewrite kuralı); geçersiz linkte düzgün davranış.
- **Geçer:** Paylaşılan bağlantılar doğru ekrana gidiyor.

#### N-08 · Onboarding ve ilk kullanım · 🟡 · 🚀 · YEREL BULUT WEB-S WEB-API OYUN
- **Geçer:** Yeni kullanıcı açıklamaya ihtiyaç duymadan ilk değerli işi yapabiliyor; izinler bağlamında isteniyor.

#### N-09 · Geri alınabilirlik ve onay · 🟡 · 🚀 · YEREL BULUT WEB-S WEB-API
- **Kontrol:** Yıkıcı işlemlerde onay veya "geri al"; form verisinin yanlışlıkla kaybolması (sayfadan çıkınca uyarı, taslak saklama).
- **Geçer:** Kullanıcı tek dokunuşla geri dönülmez veri kaybı yaşamıyor.

#### N-10 · Haptik, ses ve hareket · 🟢 · 📈 · YEREL BULUT OYUN
- **Kontrol:** Reduce Motion'a saygı, sessiz modda ses çalmama, haptiklerin aşırı kullanılmaması.
- **Geçer:** Sistem tercihlerine uyuluyor.

---

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

---

### AN. Platform: Android

> Yalnız Android hedefi olan projelerde (Kotlin, Flutter, React Native, Unity Android). iOS karşılıkları O kategorisindedir. Sürüme bağlı şartlar (hedef API düzeyi, izin türleri) her yıl değişir; ajan şüphede developer.android.com üzerinden güncel belgeyi doğrular. 2026-11-10'da eklendi.

#### AN-01 · İmzalama anahtarı ve Play App Signing · 🔴 · 🏁 · YEREL BULUT OYUN
- **Ne/Neden:** Yükleme anahtarı kaybolursa ya da sızarsa güncelleme yayınlanamaz ya da başkası senin adına yayınlar.
- **Kontrol:** Keystore dosyası ve parolaları depoda değil (`git ls-files | grep -iE 'jks|keystore'`), `gradle.properties` içinde düz parola yok; keystore ve parolanın şifreli bir yedeği var; Play App Signing açık; CI imzalama sırları sır deposunda.
- **Geçer:** Anahtar depo dışında, yedekli; Play App Signing etkin.

#### AN-02 · SDK düzeyleri (target, min, compile) · 🟠 · 🚀 · YEREL BULUT OYUN
- **Ne/Neden:** Google Play her yıl en düşük hedef API düzeyini yükseltir; eski hedefle güncelleme reddedilir. Düşük `minSdk` test yükünü, yüksek `minSdk` kullanıcı kaybını getirir.
- **Kontrol:** `targetSdk` Play'in güncel şartını karşılıyor (Play Console ve developer.android.com'dan doğrula), `compileSdk` güncel, `minSdk` bilinçli seçilmiş ve o sürümde gerçekten denenmiş. Hedef yükseltmede davranış değişiklikleri listesi okunmuş.
- **Geçer:** Hedef düzey güncel şartı karşılıyor; en düşük desteklenen sürümde uygulama açılıp ana akış çalışıyor.

#### AN-03 · İzinler ve çalışma zamanı istekleri · 🟠 · 🏁 · YEREL BULUT OYUN
- **Ne/Neden:** Gereksiz izin hem güveni düşürür hem Play incelemesinde beyan gerektirir.
- **Kontrol:** `AndroidManifest.xml` içinde yalnız kullanılan izinler var (birleştirilmiş manifestte SDK'ların eklediği izinler dahil: `./gradlew :app:processReleaseMainManifest` çıktısı); tehlikeli izinler bağlam içinde, kullanılacağı anda isteniyor; bildirim izni (Android 13+) açılışta değil anlamlı anda isteniyor; arka plan konumu ayrı ve gerekçeli; izin reddedildiğinde ve "bir daha sorma" seçildiğinde uygulama çalışmaya devam ediyor.
- **Geçer:** Kullanılmayan izin yok; her izin reddedildiğinde uygulama çökmeden anlamlı bir durum gösteriyor.

#### AN-04 · Dışa açık bileşenler, intent ve bağlantılar · 🔴 · 🚀 · YEREL BULUT OYUN
- **Ne/Neden:** Dışa açık activity, service, receiver ya da provider başka uygulamalardan gelen girdiyle çalışır; doğrulanmayan intent veri sızıntısına ve yetki aşımına yol açar.
- **Kontrol:** Her bileşende `android:exported` bilinçli (intent filter'ı olmayanlarda `false`); dışa açık bileşenler gelen intent verisini ve URI'yi doğruluyor; `PendingIntent` değiştirilemez bayrakla oluşturuluyor; `ContentProvider` izinle korunuyor ve `grantUriPermissions` dar; App Links alan adı doğrulamalı (`assetlinks.json`), özel şema bağlantıları kimlik ya da ödeme adımı tetiklemiyor; `WebView` kullanılıyorsa JavaScript arayüzü ve dosya erişimi kapalı ya da güvenilir içerikle sınırlı.
- **Geçer:** Gereksiz dışa açık bileşen yok; dış girdi doğrulanmadan gezinme, dosya ya da hesap işlemi yapılmıyor.

#### AN-05 · Güvenli saklama ve yedekleme · 🔴 · 🏁 · YEREL BULUT OYUN
- **Ne/Neden:** Düz `SharedPreferences` ve dış depolama root'lu cihazda, yedekte ve cihaz aktarımında okunabilir.
- **Kontrol:** Belirteç ve sırlar Android Keystore destekli şifreli saklamada; hassas veri dış depolamada değil; `allowBackup` ve veri çıkarma kuralları (`dataExtractionRules`, `fullBackupContent`) hassas dosyaları yedek ve cihaz aktarımı dışında tutuyor; `Log` çağrılarında sır ve kişisel veri yok, sürüm derlemesinde ayrıntılı log kapalı; ekran görüntüsü alınmaması gereken ekranlarda `FLAG_SECURE`.
- **Geçer:** Sırlar şifreli saklamada; yedekten geri yüklenen cihazda başka birinin oturumu açılmıyor; logcat'te sır yok.

#### AN-06 · Ağ güvenliği yapılandırması · 🟠 · 🚀 · BULUT OYUN
- **Ne/Neden:** Düz HTTP ve gevşek sertifika ayarı araya girmeye açıktır; geliştirme istisnaları sürüm derlemesine sızabilir.
- **Kontrol:** Düz metin trafiği kapalı (`usesCleartextTraffic="false"` ya da ağ güvenlik yapılandırması); kullanıcı sertifikalarına güven yalnız debug yapılandırmasında; özel `TrustManager` ya da `HostnameVerifier` ile doğrulama kapatılmamış (`grep -rn 'TrustManager\|HostnameVerifier\|ALLOW_ALL'`); yerel geliştirme adresleri sürüm derlemesinde yok.
- **Geçer:** Sürüm derlemesi yalnız HTTPS konuşuyor; sertifika doğrulaması atlanmıyor.

#### AN-07 · Kod küçültme ve çökme eşlemesi · 🟠 · 🚀 · YEREL BULUT OYUN
- **Ne/Neden:** R8 açıkken eksik keep kuralı yalnız sürüm derlemesinde çöker; eşleme dosyası olmadan çökme kayıtları okunamaz.
- **Kontrol:** Sürüm derlemesinde `isMinifyEnabled` ve kaynak küçültme açık; yansıma, serileştirme ve yerel kod kullanan sınıflar için keep kuralları var; **sürüm derlemesi** gerçek cihazda baştan sona denenmiş (yalnız debug değil); `mapping.txt` ve yerel semboller çökme aracına ve Play Console'a yükleniyor.
- **Geçer:** Sürüm derlemesi ana akışları çökmeden geçiyor; çökme kayıtlarında okunabilir yığın izi var.

#### AN-08 · Arka plan işleri ve pil · 🟡 · 🚀 · YEREL BULUT OYUN
- **Ne/Neden:** Android arka plan çalışmasını Doze, uygulama bekleme kovaları ve üretici kısıtlarıyla sınırlar; yanlış kurulan iş hiç çalışmaz ya da pili tüketir.
- **Kontrol:** Ertelenebilir işler `WorkManager` ile; ön plan servisi yalnız kullanıcıya görünür iş için, türü manifestte beyanlı (Android 14+); tam zamanlı alarm izni gerçekten gerekiyorsa isteniyor; iş Doze'da ve pil tasarrufunda denenmiş (`adb shell dumpsys deviceidle force-idle`); uyandırma kilidi serbest bırakılıyor.
- **Geçer:** Arka plan işi kısıtlı durumda da sonunda çalışıyor; gereksiz ön plan servisi ve kalıcı bildirim yok.

#### AN-09 · Cihaz çeşitliliği ve sistem davranışı · 🟠 · 🚀 · YEREL BULUT OYUN
- **Ne/Neden:** Android'de ekran boyutu, yoğunluk, üretici arayüzü ve bellek çok değişkendir; tek cihazda çalışan uygulama başka cihazda bozulur.
- **Kontrol:** Küçük ve büyük ekran, tablet ya da katlanabilir, yatay konum; kenardan kenara çizim ve sistem çubuğu boşlukları (yeni hedef düzeylerde zorunlu); karanlık tema; en büyük yazı ölçeği; geri hareketi ve geri tuşu her ekranda; "etkinlikleri saklama" geliştirici ayarıyla süreç ölümü sonrası durumun geri gelmesi; düşük bellekli cihaz ya da emülatör profili; en az bir Samsung ve bir saf Android cihaz ya da emülatör.
- **Geçer:** Bu durumların hiçbirinde kırpılan içerik, kaybolan durum ya da çökme yok.

#### AN-10 · Yayın paketi · 🟠 · 🚀 · YEREL BULUT OYUN
- **Ne/Neden:** Yanlış yapılandırılmış paket ya reddedilir ya da test ayarlarını kullanıcıya taşır.
- **Kontrol:** Yayın biçimi App Bundle (AAB); yerel kütüphane varsa 64 bit dahil; `versionCode` her yüklemede artıyor; sürüm derlemesinde `debuggable` kapalı, test uçları, sahte veri ve geliştirici menüsü yok; uygulama kimliği kalıcı (yayından sonra değişmez); paket boyutu ölçülmüş.
- **Geçer:** Paket Play Console ön denetiminden uyarısız geçiyor; sürüm derlemesinde test kalıntısı yok.

#### AN-11 · Android vitals (çökme ve ANR) · 🟡 · 📈 · YEREL BULUT OYUN
- **Ne/Neden:** Play, çökme ve yanıt vermeme oranı eşiğin üstündeki uygulamaların görünürlüğünü düşürür.
- **Kontrol:** Play Console Android vitals: kullanıcının fark ettiği çökme oranı ve ANR oranı kötü davranış eşiğinin altında (güncel eşiği Play Console'dan doğrula); ana iş parçacığında disk ve ağ işi yok (`StrictMode` debug'da açık); soğuk açılış süresi izleniyor.
- **Geçer:** Çökme ve ANR oranları eşiğin altında ve izleniyor.

---

### P. Platform: Web

#### P-01 · HTTPS ve alan adı · 🔴 · 🚀 · WEB-S WEB-API
- **Geçer:** Tüm trafik HTTPS, HTTP→HTTPS yönlendirmesi var; `www` ve kök alan tutarlı.

#### P-02 · SEO ve paylaşım meta verileri · 🟡 · 🚀 · WEB-S WEB-API (herkese açık sayfalar)
- **Kontrol:** `<title>`, `meta description`, Open Graph/Twitter kartı görselleri, `robots.txt`, `sitemap.xml`, `lang="tr"`, canonical; SPA'da içeriğin arama motoruna görünürlüğü (SSR/SSG gerekiyor mu); özel/giriş arkası sayfalar `noindex`.
- **Geçer:** Herkese açık sayfalar düzgün önizleniyor; özel sayfalar indekslenmiyor.

#### P-03 · Favicon, manifest ve PWA · 🟢 · 📈 · WEB-S WEB-API
- **Kontrol:** Favicon, `apple-touch-icon`, `manifest.webmanifest`; service worker varsa güncelleme stratejisi (eski sürümde takılma, bkz. J-03).
- **Geçer:** Ana ekrana eklenince düzgün görünüyor; SW yeni sürümü alıyor.

#### P-04 · 404 ve hata sayfaları · 🟡 · 🚀 · WEB-S WEB-API
- **Geçer:** Bilinmeyen URL'de markalı 404; sunucu hatasında kullanıcı dostu sayfa; SPA yenileme 404 vermiyor.

#### P-05 · Tarayıcı desteği · 🟡 · 🚀 · WEB-S WEB-API
- **Kontrol:** Safari (iOS) özellikle: `100vh` sorunu (`dvh` kullan), tarih input'u, localStorage gizli modda, özel API'ler. Desteklenen tarayıcı listesi (`browserslist`).
- **Geçer:** Güncel Safari, Chrome ve Firefox'ta ana akış çalışıyor.

---

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

---

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

#### R-04 · Bağımlılık güncelleme · 🟡 · 📈 · Hepsi
- **Kontrol:** Dependabot/Renovate; `npm outdated`; büyük sürüm geride kalma; Xcode/Unity/Node LTS sürüm yaşam sonu.
- **Geçer:** Güncellemeler düzenli ve otomatik öneriliyor.

#### R-05 · Runbook ve operasyon notları · 🟡 · 🚀 · BULUT WEB-API
- **Ne/Neden:** "Site çöktü / DB silindi / anahtar sızdı / fatura patladı" anında adım adım ne yapılacağı. Stres anında düşünmek yerine okumak.
- **Geçer:** En olası 3-5 olay için kısa runbook var (Obsidian proje notunda olabilir).

#### R-06 · Altyapı kod olarak (IaC) ve yapılandırma kaydı · 🟢 · 📈 · BULUT WEB-API
- **Kontrol:** Firebase rules/indexes/functions repoda mı (konsoldan elle düzenleme yok); `vercel.json`, Terraform; DNS kayıtlarının bir kopyası.
- **Geçer:** Altyapı yapılandırması repodan yeniden kurulabilir.

#### R-07 · Teknik borç kaydı · 🟢 · 📈 · Hepsi
- **Kontrol:** `TODO/FIXME/HACK` sayısı ve yaşı; bilinen geçici çözümler belgeli mi.
- **Geçer:** Bilinçli borç kayıtlı (`Yapılacaklar.md`), kod içi TODO'lar kontrol altında.

---

### S. Yapay zekâ / LLM özellikleri

#### S-01 · Anahtar istemcide değil · 🔴 · 🏁 · YZ
- **Geçer:** LLM API anahtarı sadece sunucuda/proxy'de (bkz. B-02).

#### S-02 · Maliyet ve kota sınırı · 🔴 · 🚀 · YZ
- **Kontrol:** Kullanıcı başına istek/token sınırı (F-06), `max_tokens`, sağlayıcıda harcama sınırı (R-01), önbellek (prompt caching, aynı soruya aynı yanıt).
- **Geçer:** Tek kullanıcı faturayı patlatamaz.

#### S-03 · Prompt injection ve çıktı güvenliği · 🟠 · 🚀 · YZ
- **Kontrol:** Kullanıcı/dış içerik sistem talimatlarını ezebiliyor mu; modelin araç çağrıları yetkiyle sınırlı mı; model çıktısı HTML olarak render ediliyorsa XSS (F-04); model çıktısıyla DB/komut çalıştırma.
- **Geçer:** Model çıktısına güvenilmiyor; araç yetkileri asgari.

#### S-04 · Hata, zaman aşımı ve yedek davranış · 🟡 · 🚀 · YZ
- **Kontrol:** Akış (streaming) kesilmesi, 429/529 aşırı yük, timeout (K-01), retry (K-02), model kullanılamazsa uygulamanın geri kalanı çalışıyor mu (K-03); model kimliği yapılandırmada mı (kodda gömülü değil).
- **Geçer:** LLM hatası kullanıcı deneyimini kırmıyor.

#### S-05 · Veri gizliliği · 🟠 · 🚀 · YZ
- **Kontrol:** LLM'e gönderilen kişisel/hassas veri; kullanıcıya bildiriliyor mu (G-01); loglarda prompt saklanması (L-02).
- **Geçer:** Gereksiz kişisel veri modele gitmiyor; kullanıcı bilgilendirilmiş.

---

### T. Apple incelemesine göndermeden önce (App Review ön kontrolü)

> Profil: `MAĞAZA` (iOS/macOS). Parantez içindeki numaralar App Store Review Guidelines bölümleridir; ajan şüphede güncel metni developer.apple.com/app-store/review/guidelines adresinden doğrular. Bu kategorinin tamamı **"Yayın hazırlığı"** fazının çıkış kapısıdır (Bölüm 8).

#### T-01 · Hesap silme · 🔴 · 🚀 · MAĞAZA (hesap oluşturulabiliyorsa)
- **Ne/Neden:** Hesap oluşturulabiliyorsa uygulama **içinden** hesap silme başlatılabilmeli (5.1.1(v)). Sadece "bize e-posta atın" yetmez; sadece devre dışı bırakmak yetmez. Sign in with Apple kullanılıyorsa token iptali (REST API ile revoke) de yapılmalı.
- **Kontrol:** Ayarlar'da 2-3 dokunuşla bulunuyor mu; onay adımı var mı; tüm veri siliniyor mu (E-05); aktif abonelik varsa kullanıcıya iptalin App Store'dan yapılması gerektiği söyleniyor mu.
- **Geçer:** Kolay bulunan, gerçekten silen, abonelik uyarılı akış.

#### T-02 · Kullanım koşulları ve gizlilik bağlantıları · 🔴 · 🚀 · MAĞAZA GELİR
- **Ne/Neden:** Abonelik/ödeme ekranında **Terms of Use (EULA)** ve **Privacy Policy** bağlantıları erişilebilir olmalı (3.1.2). App Store Connect'te de Privacy Policy URL'si ve (özel EULA kullanılıyorsa) EULA alanı ya da açıklamada standart Apple EULA bağlantısı bulunmalı.
- **Geçer:** Paywall'da ve ayarlarda iki bağlantı tıklanabilir ve çalışıyor (404 değil).

#### T-03 · Satın almaları geri yükle (Restore Purchases) · 🔴 · 🚀 · GELİR
- **Ne/Neden:** Geri yüklenebilir satın almalar (abonelik, kalıcı kilit açma) için kullanıcı önceki satın alımlarını **geri yükleyebilmeli** (3.1.1). Yeni cihaz/yeniden kurulumda ödediği şeyi kaybetmemeli.
- **Kontrol:** Paywall'da ve ayarlarda "Satın Almaları Geri Yükle" var mı; StoreKit 2'de `AppStore.sync()` / `Transaction.currentEntitlements`; RevenueCat `restorePurchases()`; sonuç kullanıcıya bildiriliyor mu ("Geri yüklenecek satın alım bulunamadı" dahil).
- **Geçer:** Temiz kurulumda geri yükleme ile premium geri geliyor.

#### T-04 · Paywall şeffaflığı · 🔴 · 🚀 · GELİR
- **Ne/Neden:** Ne satın alındığı, **fiyat, süre ve yenileme koşulları** açıkça görünmeli (3.1.2). En sık ret nedenlerindendir. Ayrıntı: V kategorisi.
- **Geçer:** V-01 … V-05 geçiyor.

#### T-05 · Bozuk veya eksik arayüz · 🔴 · 🚀 · MAĞAZA
- **Ne/Neden:** Lorem ipsum, "TODO", "Coming soon", çalışmayan buton, boş ekran, placeholder görsel, test verisi, kırık bağlantı olmamalı (2.1, 2.3.3).
- **Kontrol:** `grep -rniE 'lorem|ipsum|placeholder|todo|coming soon|yakında|test123|dummy'` (UI metinleri ve asset adları); her ekrana gidip her butona bas (W kategorisi).
- **Geçer:** Hiçbir ekranda yarım iş yok; yapılmamış özellik gizli değil, tamamen kaldırılmış.

#### T-06 · İnceleme için test hesabı · 🔴 · 🚀 · MAĞAZA (giriş gerekiyorsa)
- **Ne/Neden:** Giriş gerekiyorsa App Review ekibinin uygulamaya erişebileceği **çalışan** demo hesabı veya erişim bilgisi verilmeli (2.1). Eşleşme (çift/aile uygulaması), davet kodu, fiziksel cihaz, belirli konum gerektiren akışlarda nasıl test edileceği "App Review Information → Notes" bölümünde açıklanmalı; gerekirse demo video.
- **Kontrol:** Hesap gönderim gününde çalışıyor mu, 2FA/e-posta doğrulaması incelemeyi kilitlemiyor mu, demo hesabın premium erişimi var mı, sunucu inceleme süresince açık mı.
- **Geçer:** Hesap ve notlar App Store Connect'te; ekip yardım almadan tüm özelliklere ulaşabilir.

#### T-07 · İnceleme sonrası davranış değiştirme yok · 🔴 · 🚀 · MAĞAZA
- **Ne/Neden:** İnceleme sırasında kapalı bir özelliği sonradan uzaktan açıp uygulamanın **doğasını** değiştirmek (gizli/uyuyan özellik, 2.3.1) hesabın kapatılmasına kadar gidebilir. Feature flag (B-04) meşru kullanım içindir: kademeli açılış, hata durumunda kapatma.
- **Kontrol:** Remote Config/flag'lerle incelemede görünmeyen yeni işlev (ödeme yolu, içerik türü, kumar, harici bağlantı) açılabiliyor mu; incelemede gösterilmeyen özellik "Notes"ta belirtilmiş mi.
- **Geçer:** İncelenen sürüm, kullanıcının alacağı sürümle aynı işlevselliği gösteriyor.

#### T-08 · Web sarmalayıcı (wrapper) değil · 🔴 · 🏁 · MAĞAZA
- **Ne/Neden:** Sadece bir web sitesini `WKWebView` ile açan uygulama reddedilir (4.2 minimum işlevsellik). Yerel deneyim, cihaz özellikleri, çevrimdışı kullanım, bildirim, widget gibi gerçek uygulama değeri sunulmalı.
- **Geçer:** Uygulama web sitesinin sunamayacağı bir değer sunuyor.

#### T-09 · İzin isteklerinde gerekçe · 🔴 · 🚀 · MAĞAZA
- **Ne/Neden:** Kamera, konum, fotoğraf, mikrofon, kişiler, sağlık, bildirim izni istenmeden önce **neden gerektiği** açıkça anlatılmalı (5.1.1). `Info.plist` açıklaması somut olmalı ("Kıble yönünü bulmak için konumunuzu kullanırız"). "İzin ver" yerine başka bir yere yönlendiren veya izni reddedince uygulamayı kilitleyen tasarımlar reddedilir. Ayrıntı: G-03, U-03.
- **Geçer:** Her izin, ihtiyaç anında, önceden kısa bir açıklama ekranıyla ve somut gerekçeyle isteniyor; ret durumunda uygulama çalışıyor.

#### T-10 · Takip ve ATT · 🔴 · 🚀 · MAĞAZA (takip yapılıyorsa)
- **Ne/Neden:** Kullanıcı verisini başka şirketlerin uygulama/web sitelerindeki verilerle birleştiriyorsan veya reklam amaçlı paylaşıyorsan (IDFA, Meta/Google reklam SDK'ları, bazı MMP'ler) **App Tracking Transparency** izni zorunludur (5.1.2). İzin vermeyene özellik kısıtlanamaz, izin karşılığı ödül verilemez.
- **Kontrol:** Kullanılan SDK'lar takip yapıyor mu; `NSUserTrackingUsageDescription` ve `requestTrackingAuthorization` doğru zamanda mı; ATT reddedilince SDK'lar takip yapmıyor mu; `PrivacyInfo.xcprivacy` → `NSPrivacyTracking` ve tracking domain'leri.
- **Geçer:** Takip yoksa ATT yok ve beyan "takip yok"; varsa izin alınıyor ve redde uyuluyor.

#### T-11 · Gizlilik beyanı gerçek davranışla uyumlu · 🔴 · 🚀 · MAĞAZA
- **Ne/Neden:** App Store Connect "App Privacy" beyanı, uygulamanın ve **tüm SDK'ların** gerçekte topladığı verilerle örtüşmeli (5.1.1, 5.1.2). Crashlytics, analytics, reklam, ödeme SDK'ları da veri toplar.
- **Kontrol:** SDK listesi → her birinin privacy manifest'i → toplanan veri türleri; "kullanıcıya bağlı mı / takip için mi" işaretleri; G-02 ile birlikte.
- **Geçer:** Beyan, SDK manifestleri ve gizlilik politikası (G-01) birbiriyle tutarlı.

#### T-12 · Dijital içerik satışı ve IAP · 🔴 · 🏁 · GELİR
- **Ne/Neden:** Uygulama içinde kullanılan dijital ürün/hizmet (premium özellik, abonelik, içerik, sanal para) Apple In-App Purchase ile satılmalı (3.1.1). Fiziksel ürün/hizmetler (kargo, yemek, taksi) IAP dışında satılabilir. Harici ödeme bağlantıları bölgeye ve güncel kurallara bağlıdır (ABD, AB DMA, bazı ülkelerde farklı entitlement'lar); ajan güncel kuralı doğrulamadan harici ödeme önermez.
- **Geçer:** Dijital içerik IAP ile; harici ödeme varsa güncel bölge kuralına uygun.

#### T-13 · Çocuk kategorisi · 🔴 · 🏁 · MAĞAZA (Kids kategorisi veya çocuklara yönelik)
- **Ne/Neden:** Kids Category'de üçüncü taraf reklam ve analitik büyük ölçüde yasaktır; dış bağlantı, satın alma ve izin istekleri ebeveyn kapısı (parental gate) arkasında olmalı (1.3, 5.1.4). COPPA/KVKK çocuk verisi kuralları.
- **Geçer:** Çocuk kategorisi seçilmediyse `➖`; seçildiyse reklam/analitik SDK yok ve ebeveyn kapısı var.

#### T-14 · Kullanıcı üretimli içerik (UGC) · 🔴 · 🚀 · MAĞAZA (UGC varsa)
- **Ne/Neden:** Kullanıcı içerik oluşturabiliyorsa (yorum, mesaj, profil, fotoğraf, anonim değerlendirme): uygunsuz içeriği **filtreleme**, **raporlama**, kullanıcı **engelleme** ve zamanında **moderasyon** mekanizmaları ile yayıncı iletişim bilgisi zorunludur (1.2). G-08 ile birlikte.
- **Kontrol:** Her içerik öğesinde "Bildir"; kullanıcıyı engelle (engellenen içerik anında gizlenir); rapor kuyruğu ve yanıt süresi; küfür/spam filtresi; kullanım şartlarında içerik kuralları.
- **Geçer:** Dört mekanizma da çalışıyor ve incelemede gösterilebilir.

#### T-15 · Telif hakkı ve marka · 🔴 · 🚀 · MAĞAZA
- **Ne/Neden:** Ekran görüntüsü, video, müzik, karakter, logo, font, film afişi, takım/şirket adı gibi içeriklerin kullanım hakkı olmalı (5.2). Başka markanın adını uygulama adında/ikonunda kullanmak reddedilir. API ile gelen içerik (TMDB afişleri) için sağlayıcının şartları ve atıf (G-07).
- **Geçer:** Tüm üçüncü taraf içerik lisanslı veya kullanım şartlarına uygun; mağaza görsellerinde başkasının markası yok.

#### T-16 · Sağlık iddiaları · 🔴 · 🚀 · MAĞAZA (sağlık/fitness/regl/uyku/diyet)
- **Ne/Neden:** Teşhis, tedavi, kalp ritmi, uyku, diyet, doğurganlık, gebelikten korunma gibi iddialar dayanak ve açıklama gerektirir; yanlış ölçüm iddiası kullanıcıya zarar verebilir (1.4.1). Tıbbi cihaz sayılabilecek iddialarda düzenleyici onay istenebilir.
- **Kontrol:** Mağaza metni ve uygulama içi metinlerde "teşhis eder", "%99 doğru", "doğum kontrolü yöntemi" gibi ifadeler; "Bu uygulama tıbbi tavsiye değildir, doktorunuza danışın" uyarısı; tahminlerin tahmin olduğu açık mı.
- **Geçer:** İddialar ölçülü; tıbbi uyarı görünür; doğruluk iddiası varsa kaynaklı.

#### T-17 · Ekran görüntüsü doğruluğu · 🟠 · 🚀 · MAĞAZA
- **Ne/Neden:** Ekran görüntüleri ve önizleme videosu uygulamada **gerçekten bulunan** özellikleri göstermeli; yanıltıcı görsel, olmayan özellik, başka platformun arayüzü kullanılamaz (2.3.3, 2.3.4). Pazarlama başlığı eklenebilir (Y-14) ama arayüz gerçek olmalı.
- **Geçer:** Her görseldeki her özellik, inceleme sürümünde bulunabiliyor.

#### T-18 · Gerçek cihaz testi · 🔴 · 🚀 · MAĞAZA
- **Ne/Neden:** Simülatör gerçek cihaz değildir: bellek, performans, kamera, konum, pusula, bildirim, satın alma ve ağ farklı davranır. Apple incelemeyi gerçek cihazlarda (genellikle güncel iPhone ve iPad) yapar.
- **Kontrol:** Desteklenen en eski ve en yeni cihazda, iPad'de (iPhone uygulaması iPad'de de çalışır, "iPhone only" bile olsa uyumluluk modunda incelenebilir) **crash, donma, düzen ve performans**; en düşük desteklenen iOS sürümü; TestFlight dağıtımı (O-08) ve W kategorisi.
- **Geçer:** En az iki gerçek cihazda W kategorisi geçti; iPad'de düzen kırılmıyor.

#### T-19 · Ürün kalitesi ve tamamlanmışlık · 🔴 · 🚀 · MAĞAZA
- **Ne/Neden:** Uygulama tamamlanmış, kullanılabilir ve yayınlanabilir kalitede olmalı (2.1, 4.0 Tasarım). Beta/demo/deneme sürümü olarak gönderilemez; "beta" kelimesi adda/açıklamada olmamalı. Çok basit veya şablondan üretilmiş uygulamalar (4.2, 4.3 spam) reddedilir.
- **Geçer:** U ve W kategorileri tamam; uygulamanın açık ve tek bir ana değeri var (Z-01).

#### T-20 · Ret (rejection) sonrası süreç · 🟠 · 🚀 · MAĞAZA
- **Ne/Neden:** Ret gerekçesini körlemesine yeni build göndererek çözmeye çalışmak süreyi uzatır.
- **Adımlar:** 1) Resolution Center mesajını ve atıf yapılan guideline numarasını oku. 2) Sorunun kaynağını bul ve gerçekten düzelt. 3) Sadece metadata sorunuysa build göndermeden metadata'yı düzelt. 4) Yanlış anlaşılma varsa Resolution Center'dan net, kibar, ekran görüntülü yanıt ver; hâlâ katılmıyorsan App Review Board'a itiraz (appeal) et. 5) Gelecekte tekrarlanmaması için ret nedenini bu dosyadaki ilgili maddenin **Kontrol** satırına ve projenin `Önemli bilgiler` bölümüne ekle.
- **Geçer:** Ret nedeni kayıtlı ve kök nedeni çözülmüş.

#### T-21 · Diğer sık ret nedenleri · 🟠 · 🚀 · MAĞAZA
- **Kontrol:**
  - Üçüncü taraf girişi (Google/Facebook) varsa Sign in with Apple veya eşdeğer gizlilik odaklı seçenek (4.8).
  - Uygulama adı, alt başlık ve anahtar kelimelerde rakip markası, fiyat, "en iyi", "#1" gibi kanıtlanamaz iddia veya anahtar kelime doldurma yok (2.3.7).
  - Destek URL'si çalışıyor ve iletişim bilgisi var.
  - Uygulama ilk açılışta zorla kayıt istemiyor; hesap gerektirmeyen özellikler hesapsız kullanılabiliyor (5.1.1).
  - Push bildirimleri pazarlama için kullanılıyorsa açık onay ve kapatma seçeneği (4.5.4).
  - Arka plan modları (konum, ses) gerçekten kullanılıyor (2.5.4).
  - Export compliance (şifreleme beyanı) `ITSAppUsesNonExemptEncryption` ile doğru.
  - Yaş derecelendirmesi anketi gerçek içerikle uyumlu.
- **Geçer:** Liste temiz.

---

### GP. Google Play incelemesine göndermeden önce

> Profil: `MAĞAZA` (Android). Apple karşılığı T kategorisindedir. Google Play politikaları sık güncellenir; ajan şüphede güncel metni Play Console politika merkezinden (support.google.com/googleplay/android-developer) doğrular ve tarihini `Kontrol.md`'ye yazar. Bu kategorinin tamamı **"Yayın hazırlığı"** fazının kapısıdır. 2026-11-10'da eklendi.

#### GP-01 · Veri güvenliği formu · 🔴 · 🚀 · MAĞAZA
- **Ne/Neden:** Form uygulamanın ve içindeki SDK'ların gerçek davranışıyla uyuşmazsa uygulama kaldırılabilir.
- **Kontrol:** Play Console veri güvenliği formundaki her veri türü, amaç ve paylaşım beyanı kodla ve SDK'ların topladıklarıyla karşılaştırılmış (analitik, çökme, reklam, kimlik SDK'ları dahil); aktarımda şifreleme ve silme talebi yanıtları doğru; form her yeni SDK ya da veri türünde güncelleniyor.
- **Geçer:** Form, kodda ve SDK belgelerinde görülen her veri toplamayı karşılıyor.

#### GP-02 · Gizlilik politikası · 🔴 · 🚀 · MAĞAZA
- **Ne/Neden:** Kişisel ya da hassas veri işleyen her uygulamada zorunludur; eksikliği ret nedenidir.
- **Kontrol:** Gizlilik politikası bağlantısı mağaza kaydında ve uygulama içinde; herkese açık, giriş istemeyen, PDF olmayan bir sayfa; uygulamanın adını, toplanan verileri, saklama ve silme yolunu ve iletişim bilgisini içeriyor.
- **Geçer:** Bağlantı çalışıyor ve içerik uygulamanın gerçek davranışını anlatıyor.

#### GP-03 · Hesap silme · 🔴 · 🚀 · MAĞAZA (hesap oluşturulan uygulama)
- **Ne/Neden:** Hesap oluşturmaya izin veren uygulama, hesabı ve ilişkili veriyi silme yolunu hem uygulama içinde hem web üzerinden sunmak zorundadır.
- **Kontrol:** Uygulama içinde bulunabilir hesap silme akışı var; uygulamayı kaldırmış kullanıcı için web üzerinden silme talebi bağlantısı var ve veri güvenliği formuna yazılmış; silme gerçekten veriyi siliyor (yalnız devre dışı bırakmıyor), yasal saklama varsa belirtiliyor.
- **Geçer:** Hesap ve verisi uygulama içinden ve web bağlantısından silinebiliyor.

#### GP-04 · Hedef API düzeyi şartı · 🔴 · 🚀 · MAĞAZA
- **Ne/Neden:** Yeni uygulama ve güncellemeler Play'in belirlediği en düşük hedef API düzeyini karşılamak zorundadır (AN-02).
- **Kontrol:** Gönderim tarihinde geçerli şart Play Console'dan doğrulanmış; `targetSdk` bunu karşılıyor; bir sonraki yükseltme tarihi `Yapılacaklar.md`'de.
- **Geçer:** Paket hedef düzey uyarısı olmadan kabul ediliyor.

#### GP-05 · Ödemeler: Play Faturalandırma · 🔴 · 🚀 · MAĞAZA GELİR
- **Ne/Neden:** Uygulama içi dijital içerik ve abonelik Play Faturalandırma dışında satılamaz; fiziksel ürün ve gerçek dünya hizmetleri ise Play Faturalandırma kullanamaz.
- **Kontrol:** Satılan her şey sınıflandırılmış (dijital içerik mi, fiziksel ürün ya da hizmet mi); dijital satışlarda yalnız Play Faturalandırma var, başka ödeme yoluna yönlendirme yok (bölgesel istisna programlarına kayıt yoksa); satın alma sunucuda doğrulanıyor ve onaylanıyor (onaylanmayan satın alma iade edilir); satın alımları geri yükleme çalışıyor.
- **Geçer:** Ödeme yöntemi satılan şeyin türüne uygun; satın alma doğrulanıp onaylanıyor.

#### GP-06 · Abonelik şeffaflığı · 🔴 · 🚀 · MAĞAZA GELİR
- **Ne/Neden:** Yanıltıcı abonelik ekranı ret ve kaldırma nedenidir.
- **Kontrol:** Satın alma ekranında fiyat, faturalama dönemi, deneme süresi ve bitince ne olacağı açık; iptal yolu uygulama içinde anlatılıyor ya da Play abonelik sayfasına bağlanıyor; ücretsiz kullanım sınırı ve abonelikle açılanlar net; kapatma düğmesi görünür.
- **Geçer:** Kullanıcı ödemeden önce ne kadar, ne sıklıkla ödeyeceğini ve nasıl iptal edeceğini görüyor.

#### GP-07 · Hassas izin ve API beyanları · 🔴 · 🚀 · MAĞAZA
- **Ne/Neden:** Bazı izinler yalnız çekirdek işlev için ve beyan formuyla kabul edilir; gerekçesiz kullanım rettir.
- **Kontrol:** Şunlardan biri kullanılıyorsa Play Console beyanı doldurulmuş ve çekirdek işlev gerekçesi var: SMS ve arama kaydı, arka plan konumu, tüm dosyalara erişim, fotoğraf ve video izinleri (seçici yerine geniş izin), erişilebilirlik servisi, tam ekran bildirim, tam zamanlı alarm, yüklü uygulamaları sorgulama, ön plan servisi türleri, VPN servisi. Kullanılmayanlar manifestten çıkarılmış (AN-03).
- **Geçer:** Beyan gerektiren her izin beyanlı ve gerekçeli; gerekmeyen izin yok.

#### GP-08 · İçerik derecelendirme, hedef kitle ve çocuklar · 🟠 · 🚀 · MAĞAZA
- **Ne/Neden:** Yanlış yaş beyanı ve derecelendirme kaldırma nedenidir; çocuklara yönelik uygulamalar Aile politikasına tabidir.
- **Kontrol:** İçerik derecelendirme anketi dürüstçe doldurulmuş; hedef kitle ve içerik bölümü gerçek kitleyi yansıtıyor; hedef kitlede çocuk varsa Aile politikası (reklam SDK'ları, veri toplama, içerik) karşılanıyor; çocuklara yönelik değilse mağaza kaydı çocuklara hitap etmiyor.
- **Geçer:** Derecelendirme ve hedef kitle beyanı uygulamanın içeriğiyle tutarlı.

#### GP-09 · Kullanıcı tarafından üretilen içerik · 🔴 · 🚀 · MAĞAZA (yorum, mesaj, profil, paylaşım olan uygulama)
- **Ne/Neden:** Denetimsiz kullanıcı içeriği kaldırma nedenidir.
- **Kontrol:** Kullanım şartları kabul ettiriliyor ve sakıncalı içeriği tanımlıyor; içerik ve kullanıcı bildirme, kullanıcı engelleme uygulama içinde; bildirimler makul sürede ele alınıyor ve kaydı tutuluyor; moderasyon yolu (insan ya da otomatik) var.
- **Geçer:** Bildir ve engelle çalışıyor; bildirimin ele alındığı gösterilebiliyor.

#### GP-10 · Reklamlar ve reklam kimliği · 🟠 · 🚀 · MAĞAZA GELİR
- **Ne/Neden:** Reklam kimliği kullanımı beyan edilmek zorundadır; yanıltıcı ve rahatsız edici reklam yerleşimi rettir.
- **Kontrol:** Reklam kimliği beyanı Play Console'da doğru; `AD_ID` izni yalnız gerekiyorsa manifestte; reklam SDK'ları Play'in izin verdiği sürümlerde; reklamlar içerikten ayırt edilebiliyor, sistem arayüzünü taklit etmiyor, beklenmedik anda tam ekran açılmıyor; rıza gereken bölgelerde rıza akışı var.
- **Geçer:** Reklam beyanı doğru; reklamlar politika dışı yerleşim içermiyor.

#### GP-11 · Mağaza kaydının doğruluğu · 🟠 · 🚀 · MAĞAZA
- **Ne/Neden:** Yanıltıcı ad, simge, açıklama ve görseller ret ve kaldırma nedenidir.
- **Kontrol:** Ad, simge ve açıklamada başka marka ya da uygulama taklidi, anahtar kelime doldurma, fiyat ve sıralama iddiası ("1 numara", "ücretsiz") yok; ekran görüntüleri gerçek uygulamadan; açıklanan her özellik uygulamada var; iletişim e-postası çalışıyor.
- **Geçer:** Mağaza kaydı uygulamanın gerçek halini anlatıyor.

#### GP-12 · Test kanalları ve aşamalı yayın · 🟠 · 🚀 · MAĞAZA
- **Ne/Neden:** Yeni kişisel geliştirici hesaplarında üretime çıkmadan önce kapalı test şartı vardır; plansız kalınırsa yayın haftalarca gecikir.
- **Kontrol:** Hesap türü için geçerli kapalı test şartı (test kullanıcısı sayısı ve süresi) Play Console'dan doğrulanmış ve takvime konmuş; dahili test → kapalı test → üretim sırası izleniyor; üretim yayını aşamalı dağıtımla başlıyor ve durdurma ölçütü belli; yayın öncesi raporu (pre-launch report) incelenmiş.
- **Geçer:** Test şartı karşılanmış; ilk üretim yayını aşamalı ve izleniyor.

#### GP-13 · İnceleme için uygulama erişimi · 🔴 · 🚀 · MAĞAZA (giriş gerektiren uygulama)
- **Ne/Neden:** İnceleyen kişi giriş yapamazsa uygulama reddedilir.
- **Kontrol:** Play Console uygulama erişimi bölümünde çalışan bir test hesabı ve gereken talimatlar var (iki adımlı doğrulama, konum ya da cihaz şartı varsa nasıl aşılacağı); test hesabı gönderimden hemen önce denenmiş ve süresi dolmuyor.
- **Geçer:** İnceleyen kişi verilen bilgiyle uygulamanın tamamına ulaşabiliyor.

#### GP-14 · Geliştirici hesabı ve iletişim bilgileri · 🟡 · 🚀 · MAĞAZA
- **Ne/Neden:** Doğrulanmamış hesap ve eksik iletişim bilgisi yayını durdurur; bilgiler mağazada herkese görünür.
- **Kontrol:** Geliştirici hesabı kimlik doğrulaması tamam; mağazada görünecek ad, e-posta ve (şartsa) adres ve telefon bilinçli seçilmiş (kişisel adresin görünmesi kabul edilebilir mi); hesap iki adımlı doğrulamayla korunuyor; hesaba erişimi olanlar gözden geçirilmiş.
- **Geçer:** Hesap doğrulanmış, korunuyor; herkese açık bilgiler bilinçli.

---

### U. Yayınlamadan önce düzeltilecek ürün sorunları (ilk deneyim)

> Profil: `MAĞAZA` (ve kullanıcıya açılan her `WEB-S`/`WEB-API`/`OYUN`). Bu sorunlar inceleme reddi değil ama **ilk gün kullanıcı kaybı** demektir. "Yayın hazırlığı" fazında, mümkünse daha önce "İlk deneyim" fazında çözülür.

#### U-01 · Açılış 2 saniyeden uzun · 🟠 · 🚀 · MAĞAZA OYUN
- **Düzeltme:** Splash/startup süresini ölç (J-07, Xcode MCP `profile_launch`); ağır işleri (SDK başlatma, veri taşıma, ağ, büyük görsel) ilk kareden **sonraya** ertele; ilk ekranı önbellekten göster. Splash ekranını yapay olarak uzatma.
- **Geçer:** Soğuk açılışta ilk kullanılabilir ekran < 2 sn (orta seviye cihazda).

#### U-02 · Değer göstermeden kayıt istemek · 🟠 · 🏁 · MAĞAZA BULUT WEB-API
- **Düzeltme:** Önce uygulamanın faydasını yaşat; kaydı mümkün olduğunca geç ve **gerekçeli** iste ("Verilerini kaybetmemek için hesap oluştur"). Anonim/misafir mod, sonradan hesaba bağlama (Firebase anonymous auth → link).
- **Geçer:** Kullanıcı kayıt olmadan uygulamanın ana değerini görebiliyor.

#### U-03 · Açılışta toplu izin isteği · 🟠 · 🚀 · MAĞAZA
- **Düzeltme:** İzinleri tek seferde isteme. Her izni **ihtiyaç oluştuğu anda**, bağlam içinde iste (bildirim → ilk hatırlatıcı kurulurken; konum → harita/pusula ilk açılınca). Sistem penceresinden önce kısa açıklama ekranı göster (sistem penceresi bir kez reddedilince tekrar gösterilemez; Ayarlar'a yönlendirme gerekir).
- **Geçer:** Açılışta en fazla bir izin (o da zorunluysa) isteniyor.

#### U-04 · Boş ana ekran · 🟠 · 🚀 · MAĞAZA WEB-S WEB-API
- **Düzeltme:** İlk oturumda kullanıcıya yapılacak **net bir aksiyon** göster ("İlk tarifini ekle", "Döngünün başladığı günü seç"); örnek veri veya şablon sun; boş durum tasarımı (N-03).
- **Geçer:** İlk açılışta kullanıcı ne yapacağını 3 saniyede anlıyor.

#### U-05 · Uzun onboarding · 🟡 · 🚀 · MAĞAZA
- **Düzeltme:** 8 ekranlık tanıtım yerine onboarding'i kısalt (genelde 3 ekran veya daha az); en güçlü kanıtı/faydayı ilk birkaç saniyeye taşı; "Atla" seçeneği; kişiselleştirme soruları sadece sonucu gerçekten değiştiriyorsa.
- **Geçer:** Onboarding tamamlama oranı ölçülüyor; atlanabilir.

#### U-06 · İlk değer anına (time-to-value) ulaşmak çok uzun · 🟠 · 🚀 · MAĞAZA WEB-S WEB-API OYUN
- **Düzeltme:** Kullanıcıyı "aha anı"na (ilk film önerisi, ilk kıble yönü, ilk oyun turu) mümkün olduğunca hızlı götür; o ana kadarki adım sayısını say ve azalt. Oyunda ilk 30 saniyede oynanış.
- **Geçer:** İlk değer anı tanımlı, adım sayısı ve süresi ölçülmüş.

#### U-07 · Paywall ilk karede açılıyor · 🟠 · 🚀 · GELİR
- **Düzeltme:** Önce ürünün değerini göster, paywall'u **bağlamlı** bir noktada aç (premium özelliğe dokunulduğunda, değer yaşandıktan sonra). Onboarding sonu paywall'u kabul edilen bir kalıptır ama kapatılabilir olmalı (U-08). Ayrıntı: V.
- **Geçer:** Paywall'un açılma noktaları listelenmiş ve her biri bağlamlı.

#### U-08 · Paywall kapatma tuşu görünmüyor · 🔴 · 🚀 · GELİR
- **Düzeltme:** Belirgin ve kolay erişilebilir kapat/geri dön kontrolü (V-04). Gecikmeli beliren, soluk gri, çok küçük "X" hem kullanıcı kaybettirir hem ret riskidir.
- **Geçer:** Kapat butonu anında görünür, ≥ 44pt dokunma alanı, yeterli kontrast.

#### U-09 · Paywall / satın alma çöküyor · 🔴 · 🚀 · GELİR
- **Düzeltme:** Tüm satın alma akışını gerçek cihazda test et (V-10): ürünler yüklenmezse, ağ yoksa, kullanıcı iptal ederse, ödeme beklemede (Ask to Buy) kalırsa, zaten aboneyse.
- **Geçer:** Satın alma akışının tüm dalları gerçek cihazda denenmiş.

#### U-10 · İnternet gidince beyaz ekran · 🔴 · 🚀 · MAĞAZA BULUT WEB-S WEB-API
- **Düzeltme:** Çevrimdışı ve hata durumu tasarla; kullanıcıya bağlantının koptuğunu açıkça bildir; önbellekteki veriyi göster; bağlantı gelince otomatik yenile (N-04, W-01, W-10).
- **Geçer:** Uçak modunda hiçbir ekran boş/sonsuz yükleme göstermiyor.

#### U-11 · Hata mesajı yok veya anlamsız · 🟠 · 🚀 · Hepsi (UI olan)
- **Düzeltme:** Hatanın ne olduğunu ve kullanıcının **ne yapabileceğini** yaz ("Bağlantı kurulamadı. İnternetini kontrol edip tekrar dene." + Tekrar Dene butonu). "Bir sorun oluştu" tek başına yetmez; hata kodu gerekiyorsa küçük ikincil metin olarak (N-03, W-11).
- **Geçer:** Her hata mesajı bir sonraki adımı söylüyor.

#### U-12 · Klavye giriş alanını örtüyor · 🟠 · 🚀 · MAĞAZA WEB-S WEB-API
- **Düzeltme:** Klavye kaçınma (keyboard avoidance) ve kaydırma davranışını düzelt: SwiftUI'da `ScrollView` + `.scrollDismissesKeyboard`, `safeAreaInset`, `@FocusState` ile sonraki alana geçiş; web'de `visualViewport`, `dvh`; gönder butonu klavyenin altında kalmamalı; klavye kapatılabilir olmalı.
- **Geçer:** Her giriş alanı ve gönder butonu klavye açıkken görünür (W-05).

#### U-13 · Dokunma hedefleri küçük · 🟠 · 🚀 · MAĞAZA WEB-S WEB-API OYUN
- **Düzeltme:** Dokunma alanları en az 44×44 pt (Apple) / 48×48 dp (Android); butonlar arası boşluk; küçük ikonlarda `contentShape` veya padding ile alan büyütme (N-01).
- **Geçer:** En küçük cihazda yanlış dokunma olmadan tüm kontroller kullanılabiliyor.

#### U-14 · Geri tuşu / geri hareketi çalışmıyor · 🟠 · 🚀 · MAĞAZA WEB-S WEB-API
- **Düzeltme:** iOS'ta kenardan kaydırarak geri dönme (özel navigasyon bunu bozabilir), modal'larda aşağı kaydırarak kapatma; web'de tarayıcı geri tuşu (SPA geçmişi); **(Android)** donanım/hareket geri davranışı her ekranda test, predictive back, kökte uygulamanın yanlışlıkla kapanmaması (W-07).
- **Geçer:** Her ekrandan beklenen yere geri dönülüyor.

#### U-15 · Karanlık mod bozuk · 🟠 · 🚀 · MAĞAZA WEB-S WEB-API
- **Düzeltme:** Tüm ekranları karanlık modda **tek tek** kontrol et (N-05, W-03): sabit beyaz arka plan, siyah metin, görünmez ikon, kontrastı düşük kenarlıklar, beyaz arka planlı görseller/logolar.
- **Geçer:** Karanlık modda beyaz patlama veya okunamaz alan yok.

#### U-16 · İlk gün gereksiz bildirim · 🟡 · 🚀 · MAĞAZA
- **Düzeltme:** Bildirim iznini değer yaratacağı noktaya taşı (U-03); "Bizi unutma!" türü ilk gün bildirimlerini kaldır; her bildirimin kullanıcıya somut faydası olmalı; sıklık sınırı ve ayarlardan kategori bazlı kapatma (K-08).
- **Geçer:** Her bildirim türünün gerekçesi ve sıklığı tanımlı.

#### U-17 · Hesap silme yok veya bulunmuyor · 🔴 · 🚀 · MAĞAZA BULUT
- **Düzeltme:** T-01, E-05.

#### U-18 · Uygulama boyutu 200 MB üstü · 🟡 · 🚀 · MAĞAZA OYUN
- **Düzeltme:** Büyük asset, video, görsel ve paket bağımlılıklarını analiz et (App Thinning Size Report, Unity Build Report); gereksizleri kaldır, görselleri sıkıştır (I-03), isteğe bağlı içeriği sonradan indir (On-Demand Resources / Background Assets / Addressables). Hücresel ağda 200 MB üstü indirmede kullanıcıya ek onay sorulur ve indirme vazgeçme oranı artar (O-05, Q-05).
- **Geçer:** İndirme boyutu bilinçli; büyük içerik isteğe bağlı.

#### U-19 · Tek dil · 🟡 · 🏁 · MAĞAZA
- **Düzeltme:** Öncelikli hedef pazarlar için lokalizasyon planı oluştur (N-02 altyapısı baştan; çeviri sonra). Sadece Türkçe ise en azından İngilizce ekle; mağaza sayfası lokalizasyonu ayrı iştir (Y-09, Y-10).
- **Geçer:** Hedef pazar listesi ve her dil için durum belli.

---

### V. Paywall, satın alma ve gelir

> Profil: `GELİR`. Paywall hem App Review'un (T-02 … T-04, T-12) hem dönüşümün en kritik ekranıdır.

#### V-01 · Premium'un ne açtığı belli · 🔴 · 🚀 · GELİR
- **Sorun:** "Premium'a Geç" yazıyor ama ne açıldığı belli değil.
- **Yapılması gereken:** Premium'un açtığı özellikleri **madde madde**, kullanıcı faydası diliyle göster (3-6 madde; "Sınırsız tarif kaydı", "Reklamsız"). İsteğe bağlı ücretsiz/premium karşılaştırma tablosu.
- **Geçer:** Kullanıcı neye para verdiğini paywall'dan çıkmadan anlıyor.

#### V-02 · Fiyat paywall üzerinde doğrudan görünüyor · 🔴 · 🚀 · GELİR
- **Sorun:** Fiyatı görmek için butona basmak gerekiyor.
- **Yapılması gereken:** Fiyatı paywall üzerinde **doğrudan** göster; StoreKit'ten gelen yerelleştirilmiş fiyatı kullan (`product.displayPrice`), sabit "₺49,99" yazma. Faturalanan tutar en belirgin fiyat olmalı; "aylık eşdeğeri ₺X" gibi hesaplanmış fiyat ondan daha göze çarpıcı olmamalı.
- **Geçer:** Gerçek faturalanacak tutar ve dönem net görünüyor.

#### V-03 · Otomatik yenileme ve koşullar belirtilmiş · 🔴 · 🚀 · GELİR
- **Yapılması gereken:** "Otomatik yenilenir" bilgisini, dönemi, deneme süresi sonunda ne kadar ücret alınacağını ve **nasıl iptal edileceğini** (Ayarlar → Apple ID → Abonelikler) göster; Terms ve Privacy bağlantıları (T-02). Deneme varsa "7 gün ücretsiz, sonra yıllık ₺X" net olmalı.
- **Geçer:** Satın almadan önce yenileme, ücret ve iptal bilgisi görünür.

#### V-04 · Görünür ve erişilebilir kapat butonu · 🔴 · 🚀 · GELİR
- **Sorun:** Kapatma butonu küçük, gri veya ulaşılması zor.
- **Yapılması gereken:** Görünür ve kolay erişilebilir bir **X / Kapat** kontrolü; ≥ 44pt; yeterli kontrast; gecikmeli belirmemeli; VoiceOver etiketi "Kapat". Kaydırarak kapatma da çalışmalı.
- **Geçer:** Kullanıcı paywall'da sıkışmıyor (W-15).

#### V-05 · Satın almaları geri yükle · 🔴 · 🚀 · GELİR
- **Yapılması gereken:** Paywall'da "Satın Almaları Geri Yükle" seçeneği (T-03).
- **Geçer:** Görünür ve çalışıyor.

#### V-06 · Birden fazla plan ve yıllık planın öne çıkması · 🟡 · 🚀 · GELİR
- **Sorun:** Tek fiyat/tek plan var veya yıllık plan gizli.
- **Yapılması gereken:** Uygunsa aylık + yıllık gibi birden fazla planı **karşılaştırılabilir** şekilde sun; yıllık planı uygun fiyat avantajıyla öne çıkar ("%40 tasarruf" — hesap doğru olmalı); gerekirse ömür boyu (lifetime) seçeneği. Plan sayısını 2-3 ile sınırla (seçim felci).
- **Geçer:** Planlar yan yana, tasarruf hesabı doğru, önerilen plan işaretli.

#### V-07 · Ücretsiz deneme veya sınırlı ücretsiz kullanım · 🟡 · 🚀 · GELİR
- **Yapılması gereken:** Mümkünse 3-7 günlük ücretsiz deneme (introductory offer) veya sınırlı ücretsiz kullanım (freemium: X kayıt ücretsiz). Deneme uygunluğu StoreKit'ten kontrol edilmeli (`isEligibleForIntroOffer`); daha önce deneme kullanmış kişiye "ücretsiz dene" yazılmamalı.
- **Geçer:** Deneme varsa uygunluk kontrolü doğru; yoksa ücretsiz katman değerli.

#### V-08 · Paywall yerleşimi ve zorlayıcı geçişler · 🟡 · 🚀 · GELİR
- **Yapılması gereken:** Paywall'un **nereden açıldığını** (kaynak: onboarding, premium özellik, ayarlar, limit aşımı) ve **kapatılma oranını** ölç; zorlayıcı/gizli geçişlerden (kullanıcı başka bir şeye dokunurken paywall'a yönlendirme, kandırıcı buton) kaçın. Değer gösterilmeden paywall yok (U-07).
- **Geçer:** Her paywall gösterimi kaynak etiketiyle loglanıyor.

#### V-09 · Bölgesel fiyatlandırma · 🟡 · 🚀 · GELİR
- **Yapılması gereken:** App Store'un ülke bazlı fiyat eşitlemesini bilinçli kullan; düşük alım gücü olan pazarlarda (Türkiye dahil) fiyatı yerel olarak ayarla; kur değişimlerinde Apple'ın otomatik güncellemelerini takip et.
- **Geçer:** Hedef ülkelerde fiyatlar bilinçli seçilmiş.

#### V-10 · Satın alma akışının test edilmesi · 🔴 · 🚀 · GELİR
- **Yapılması gereken:** Gerçek cihazlarda satın alma, geri yükleme, iptal, deneme ve fiyat gösterimini test et. Araçlar: Xcode StoreKit Configuration dosyası (yerel), sandbox test hesabı (abonelik süreleri hızlandırılmıştır), TestFlight. Senaryolar: başarılı alım, kullanıcı iptali, ağ hatası, ödeme beklemede (Ask to Buy / SCA), zaten abone, yükseltme/düşürme (aylık → yıllık), deneme bitişi, yenileme başarısız (billing retry, grace period), iade (refund → erişim kalkmalı), başka cihazda geri yükleme, Family Sharing (açıksa), ürünler yüklenemezse paywall'un davranışı.
- **Geçer:** Tüm senaryolar denenmiş; ürün yüklenemezse paywall çökmüyor, anlamlı mesaj veriyor.

#### V-11 · Yetki (entitlement) yönetimi ve doğrulama · 🔴 · 🏁 · GELİR
- **Kontrol:** Premium durumu tek kaynaktan mı (StoreKit 2 `Transaction.currentEntitlements` veya RevenueCat `CustomerInfo`); `Transaction.updates` dinleyicisi uygulama açılışında başlatılıyor mu (aksi halde uygulama dışı yenileme/iade kaçırılır); işlemler `finish()` ediliyor mu; premium durumu `UserDefaults`'ta düz `isPremium = true` olarak mı tutuluyor (kolayca değiştirilebilir); sunucu tarafı içerik varsa doğrulama sunucuda (App Store Server API / RevenueCat webhook, F-18); çevrimdışıyken premium kullanıcı kilitlenmiyor mu.
- **Geçer:** Premium durumu doğrulanmış kaynaktan; yenileme/iade/iptal otomatik yansıyor.

#### V-12 · Ödeme hunisi ve başarısız işlemlerin izlenmesi · 🟠 · 🚀 · GELİR
- **Sorun:** Ödeme ekranı bozuk ve haberin yok.
- **Yapılması gereken:** RevenueCat / App Store Connect / kendi analitiğinle satın alma hunisini izle: paywall gösterimi → plan seçimi → satın alma başlatma → başarılı / iptal / hata. Başarısız işlem oranı için alarm (L-05). App Store Server Notifications veya RevenueCat webhook ile yenileme, iptal, iade, billing issue olaylarını al.
- **Geçer:** Huninin her adımı görülüyor; hata artışı aynı gün fark ediliyor.

#### V-13 · Abonelik yaşam döngüsü ve elde tutma · 🟢 · 📈 · GELİR
- **Kontrol:** Billing grace period açık mı (App Store Connect); iptal eden kullanıcıya win-back teklifi / promosyon kodu; abonelik yönetimi bağlantısı (`showManageSubscriptions`); yükseltme/düşürme grupları doğru yapılandırılmış mı (subscription group, seviye sırası).
- **Geçer:** Ödeme sorunu yaşayan kullanıcı hemen erişimini kaybetmiyor; iptal nedenleri biliniyor.

#### V-14 · Reklam geliri (varsa) · 🟡 · 🚀 · GELİR
- **Kontrol:** Reklam SDK'sı ATT ve gizlilik beyanıyla uyumlu (T-10, T-11); reklam sıklık sınırı; tam ekran reklam kritik akışı (ödeme, kayıt) bölmüyor; yanlışlıkla tıklamaya neden olan yerleşim yok; çocuk kitlesinde uygun ayarlar; eCPM ve reklam gelirinin kullanıcı deneyimi kaybına değip değmediği (Z-03).
- **Geçer:** Reklam deneyimi bozmuyor ve kurallara uygun.

---

### W. Yayınlamadan önce uygulamayı 20 kez kır (manuel kırma testi)

> Profil: `MAĞAZA` ve kullanıcıya açılan her UI. Her yayından önce **gerçek cihazda** yapılır; sonuç `Kontrol.md`'ye tarih ve cihazla yazılır. Mümkün olanlar otomatik teste (D-03) dönüştürülür. Web için karşılıkları parantez içinde.

| # | Test | Başarılı olması gereken | İlgili |
|---|---|---|---|
| W-01 | ✈️ **Uçak modunu aç**, uygulamayı kullan | Sonsuz yükleme yok; çevrimdışı durumu anlaşılır şekilde gösteriliyor | N-04, U-10 |
| W-02 | 📱 Uygulamayı **tamamen kapat** → telefonu kilitle → aç | Açılış hızlı ve stabil; durum (açık ekran, taslak) makul şekilde korunuyor | J-07, U-01 |
| W-03 | 🌙 **Karanlık mod** | Hiçbir ekranda beyaz patlama veya okunamaz alan yok | N-05, U-15 |
| W-04 | 🔤 **En büyük yazı boyutu** (Erişilebilirlik → Daha Büyük Metin) | Metinler taşmıyor, kesilmiyor, üst üste binmiyor; butonlar erişilebilir | N-01 |
| W-05 | ⌨️ **Her giriş alanına dokun** | Klavye önemli alanları ve gönder butonunu kapatmıyor; klavye kapatılabiliyor | U-12 |
| W-06 | 🆕 **İlk kez açıyormuş gibi** başlat (temiz kurulum) | Kullanıcı ne yapacağını hemen anlıyor | U-04, U-05 |
| W-07 | ↩️ **Geri hareketini/tuşunu her yerde dene** ((Android) geri tuşu; web tarayıcı geri) | Yanlışlıkla uygulama kapanmıyor; beklenen ekrana dönülüyor | U-14 |
| W-08 | 🔄 **Ekranı yatay çevir** (iPad'de Split View / Stage Manager) | Ya düzgün destekleniyor ya da dikey mod kilitli; düzen kırılmıyor | N-06 |
| W-09 | 🗑️ **Bir veriyi sil** | Onay veya geri alma mekanizması var | N-09 |
| W-10 | 🌐 **İnterneti kes → veri kaydet** | Başarısız kayıt başarılı gibi gösterilmiyor; kuyruğa alındıysa bu belirtiliyor | H-09, N-04 |
| W-11 | ⚠️ **Hata oluştur** (yanlış giriş, sunucu hatası, geçersiz veri) | "Bir sorun oluştu" yerine kullanıcıya ne yapacağı söyleniyor | U-11 |
| W-12 | 🔐 **İzin ekranlarını kontrol et** (izinleri reddet, sonra Ayarlar'dan aç) | İzin istenmeden önce nedeni açıklanıyor; ret sonrası uygulama çalışıyor | T-09, U-03 |
| W-13 | 🚪 **Hesap silmeyi dene** | Hesap silme yolu açıkça bulunuyor ve çalışıyor | T-01 |
| W-14 | 💳 **Ödeme ekranını aç** | Fiyat + süre + otomatik yenileme + koşullar açık | V-01 … V-03 |
| W-15 | ❌ **Paywall'dan çıkış yolunu bul** | Kullanıcı paywall'da sıkışmıyor | V-04 |
| W-16 | 🔋 **Şarjdan çıkar → 10 dakika kullan** | Anormal ısınma ve pil tüketimi yok (Ayarlar → Pil'de uygulamanın payı makul) | J-06 |
| W-17 | 💾 **Depolama kullanımına bak** (Ayarlar → Genel → iPhone Saklama Alanı) | Önbellek ve geçici dosyalar kontrol altında, zamanla şişmiyor | I-05 |
| W-18 | 🌍 **Telefon dilini değiştir** (ve bölgeyi: tarih/para biçimi) | Desteklenen dillerde arayüz düzgün yerelleştirilmiş; desteklenmeyende düzgün varsayılana düşüyor | N-02 |
| W-19 | 👤 **Uygulamayı hiç bilmeyen birine ver** | Hiç açıklama yapmadan ana işi tamamlayabiliyor (sessizce izle, not al) | U-06 |
| W-20 | 🧹 **Sil → yeniden yükle** | Temiz kurulumda sorunsuz başlıyor; satın alma geri yüklenebiliyor; iCloud/hesap verisi geri geliyor | T-03, M-06 |

**Ek kırma testleri:**

| # | Test | Başarılı olması gereken | İlgili |
|---|---|---|---|
| W-21 | 🐢 **Yavaş ağ** (Network Link Conditioner "3G"/"Very Bad Network"; DevTools "Slow 3G") | Yükleme göstergeleri var, zaman aşımı makul, çift gönderim yok | K-01 |
| W-22 | 👆👆 **Butonlara hızlı hızlı çift dokun** (kaydet, satın al, gönder) | İki kayıt / iki istek oluşmuyor | H-09 |
| W-23 | ⏰ **Saat dilimini ve tarihi değiştir**, gece yarısını geç | Gün hesapları, hatırlatıcılar, seriler (streak) bozulmuyor | H-02 |
| W-24 | 📞 **Kullanım sırasında arama gelsin / arka plana al / bildirimden dön** | Durum korunuyor, ses/oyun duruyor, veri kaybolmuyor | Q-04 |
| W-25 | 🔁 **Eski sürümü kur → veri gir → yeni sürüme güncelle** | Veri eksiksiz geliyor (migration) | H-03 |
| W-26 | 🧮 **Uç değerler gir** (çok uzun metin, emoji, boş, 0, negatif, Türkçe karakter İ/ı/ş/ğ) | Düzen ve kayıt bozulmuyor | F-02, N-02 |
| W-27 | 📵 **Bellek baskısı** (çok sayıda uygulama aç, sonra dön) | Uygulama yeniden başlasa bile kullanıcı kaldığı yeri kaybetmiyor | J-05 |
| W-28 | ♿ **VoiceOver'ı aç** ve ana akışı tamamla | Tüm kontrollerin anlamlı etiketi var | N-01 |
| W-29 | 📏 **En küçük ve en büyük cihaz** (iPhone SE, Pro Max, iPad) | Düzen kırılmıyor, kesilme yok | N-06 |
| W-30 | 🔒 **Düşük Güç Modu ve Hareketi Azalt** açık | Animasyonlar sadeleşiyor, uygulama çalışmaya devam ediyor | N-10 |

---

### X. Saldırgan gibi test (kendi uygulamanda güvenlik testi)

> Profil: `BULUT`, `WEB-API` (ve sunucusu olan `OYUN`). **Yalnızca yetkili olduğun kendi uygulamanda**, tercihen staging ortamında (B-03) ve test hesaplarıyla yapılır. Üretim verisine zarar verecek, başkasının hesabına dokunacak veya hizmeti düşürecek test yapılmaz. Ajan her testi önce kullanıcıya listeler, onay alır, sonuçları `Kontrol.md`'ye yazar. Bulunan açıklar 🔴 olarak ilgili maddeye bağlanır. Araçlar: tarayıcı DevTools, `curl`, Burp Suite Community / OWASP ZAP (yerel proxy), Firebase Rules Playground / emülatör.

#### X-01 · SQL / NoSQL enjeksiyon testi · 🔴 · 🚀 · WEB-API
- **Nasıl:** Arama, filtre, sıralama, ID parametrelerine `'`, `' OR '1'='1`, `"; --`, NoSQL için `{"$ne": null}` / `{"$gt": ""}` gönder; hata mesajı veya fazladan veri dönüyor mu.
- **Geçer:** Tüm girdiler parametreli sorguyla işleniyor (F-03); hata detay sızdırmıyor.

#### X-02 · XSS testi · 🔴 · 🚀 · WEB-S WEB-API
- **Nasıl:** İsim, yorum, başlık, URL alanlarına `<script>alert(1)</script>`, `<img src=x onerror=alert(1)>`, `javascript:alert(1)`, markdown içinde HTML; içerik başka kullanıcıya ve admin paneline nasıl görünüyor.
- **Geçer:** Hiçbir yerde çalışmıyor (F-04).

#### X-03 · CSRF testi · 🟠 · 🚀 · WEB-API
- **Nasıl:** Başka bir origin'den (yerel HTML dosyası) giriş yapmış kullanıcının çereziyle durum değiştiren istek (form POST, `fetch` with credentials) gönder.
- **Geçer:** İstek reddediliyor (F-05).

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

#### X-09 · Webhook imza atlatma testi · 🔴 · 🚀 · WEB-API GELİR
- **Nasıl:** Webhook ucuna imzasız, yanlış imzalı, eski zaman damgalı ve daha önce işlenmiş bir olayı tekrar gönder ("ödeme başarılı" sahte olayı).
- **Geçer:** Hepsi reddediliyor veya etkisiz (F-18).

#### X-10 · CORS yanlış yapılandırma testi · 🟠 · 🚀 · WEB-API
- **Nasıl:** `curl -H "Origin: https://evil.example" -I https://api/...` → yanıtta `Access-Control-Allow-Origin` yansıtılıyor mu, `Allow-Credentials: true` ile birlikte mi.
- **Geçer:** Sadece kendi domain'leri izinli (F-05).

#### X-11 · Oturum ele geçirme kontrolleri · 🟠 · 🚀 · WEB-API BULUT
- **Nasıl:** Çerez bayraklarını DevTools'ta kontrol et (`HttpOnly`, `Secure`, `SameSite`); çıkış yaptıktan sonra eski token/çerezle istek; şifre değiştikten sonra diğer cihazdaki oturum; girişten önce ve sonra oturum kimliği değişiyor mu.
- **Geçer:** E-03 maddeleri doğrulanmış.

#### X-12 · JWT / oturum manipülasyonu testi · 🔴 · 🚀 · WEB-API
- **Nasıl:** JWT payload'ını değiştir (`sub`, `role`), `alg: none` dene, imzayı kaldır, süresi dolmuş token kullan, başka ortamın (staging) token'ını prod'da dene.
- **Geçer:** Hepsi reddediliyor.

#### X-13 · Hassas uç nokta keşfi · 🟠 · 🚀 · WEB-API WEB-S
- **Nasıl:** JS paketlerinde ve source map'lerde API yollarını ara (`grep -o '"/api/[^"]*"' dist/assets/*.js`); `/admin`, `/api/debug`, `/.env`, `/.git/config`, `/swagger`, `/graphql` (introspection), `/api/seed`, `robots.txt`'deki gizli yollar; yorumlarda kalan URL'ler.
- **Geçer:** Kimliksiz ulaşılabilen her uç bilinçli olarak açık (F-20).

#### X-14 · Hata mesajlarından bilgi sızması testi · 🟠 · 🚀 · WEB-API BULUT
- **Nasıl:** Bozuk JSON, yanlış tip, olmayan ID, çok büyük gövde gönder; yanıtta stack trace, SQL sorgusu, dosya yolu, framework sürümü, iç IP var mı; `X-Powered-By` başlığı.
- **Geçer:** Hatalar genel mesaj + istek kimliği döndürüyor; detay sadece sunucu logunda (F-07).

#### X-15 · İstemci tarafı güven testi · 🟠 · 🚀 · BULUT OYUN GELİR
- **Nasıl:** İstemci kodunda değiştirilebilecek değerleri değiştir: premium bayrağı (`UserDefaults`/localStorage `isPremium`), skor, fiyat, indirim, stok; proxy ile isteği düzenle. Firebase'de istemcinin yazabildiği alanları kurallar dışında dene.
- **Geçer:** Sunucu/kurallar değiştirilmiş değeri kabul etmiyor (V-11, F-17, Q-02).

---

### Y. ASO (App Store Optimizasyonu) ve mağaza sayfası

> Profil: `MAĞAZA`. Karakter sınırları App Store Connect'e göredir: **Ad 30**, **Alt başlık 30**, **Anahtar kelimeler 100**, **Promosyon metni 170** (inceleme gerektirmeden güncellenebilir), **Açıklama 4000**. Ajan sınırları ve kuralları şüphede güncel Apple belgesinden doğrular. Arama sıralamasında App Store **ad + alt başlık + anahtar kelimeler** alanlarını kullanır; açıklama arama için değil **dönüşüm** içindir.

#### Y-01 · Anahtar kelime alanını tam kullan · 🟠 · 🚀 · MAĞAZA
- **Hata:** 100 karakterin yarısı boş.
- **Düzeltme:** Keywords alanındaki karakter sınırını mümkün olduğunca verimli kullan (90-100 karakter); tek kelimeler virgülle; uzun kalıplar yerine birleşebilen tek kelimeler (Apple kelimeleri kendi içinde birleştirir: "namaz,vakti" hem "namaz vakti"ni hem ayrı aramaları kapsar).
- **Geçer:** Alan ≥ 90 karakter dolu ve her kelime bilinçli.

#### Y-02 · Virgülden sonra boşluk yok · 🟡 · 🚀 · MAĞAZA
- **Düzeltme:** Keywords alanında gereksiz boşluk kullanma (`kıble,namaz,ezan`); her boşluk bir karakter kaybıdır.
- **Geçer:** Alanda boşluk yok.

#### Y-03 · Aynı kelime birden fazla yerde değil · 🟠 · 🚀 · MAĞAZA
- **Hata:** Aynı kelime ad, alt başlık ve anahtar kelimelerde 3 kez geçiyor.
- **Düzeltme:** Gereksiz tekrarları kaldır; ad/alt başlıkta geçen kelimeyi keywords alanına tekrar yazma; boşalan yere farklı arama niyetlerine yönelik kelimeler koy.
- **Geçer:** Üç alan arasında tekrar yok.

#### Y-04 · Başlık sadece marka değil · 🟠 · 🚀 · MAĞAZA
- **Düzeltme:** Uygulama adında **Marka + ana anahtar kelime** kullan ("Döngü: Regl Takvimi"); 30 karakteri doldur ama doğal oku; ad alanı en güçlü sıralama sinyalidir.
- **Geçer:** Adda en az bir yüksek hacimli, alakalı kelime var.

#### Y-05 · Alt başlık dolu · 🟠 · 🚀 · MAĞAZA
- **Düzeltme:** Alt başlığı ana değer önerisi ve güçlü anahtar kelimelerle doldur ("Ezan vakti ve kıble pusulası"); slogan değil, aranabilir fayda.
- **Geçer:** Alt başlık 30 karaktere yakın ve anahtar kelime içeriyor.

#### Y-06 · Tekil ve çoğul birlikte yazılmamış · 🟡 · 🚀 · MAĞAZA
- **Düzeltme:** Apple İngilizcede tekil/çoğulu büyük ölçüde eşleştirir; ikisini birden yazmak karakter israfıdır. Türkçe eklerde (tarif/tarifler, film/filmler) eşleşme her zaman garanti değildir; arama hacmi yüksek olan biçimi seç, gerekirse test et.
- **Geçer:** Gereksiz tekil/çoğul tekrarı yok.

#### Y-07 · Kategori adı anahtar kelimelerde değil · 🟡 · 🚀 · MAĞAZA
- **Düzeltme:** Kategori adı ("sağlık", "oyun", "yemek") zaten metadata'dan gelir; keyword alanını başka terimlere ayır. "app", "uygulama", "free", "ücretsiz" gibi kelimeler de genelde boşa harcanır.
- **Geçer:** Kategori adı ve genel dolgu kelimeleri yok.

#### Y-08 · Rakip marka adları kullanılmıyor · 🟠 · 🚀 · MAĞAZA
- **Düzeltme:** Rakip marka isimlerini keyword alanına doldurma; hem ret ve kaldırma riski (2.3.7, 5.2) hem de dönüşümü düşük trafik. Gerçek kullanıcı aramalarına (problem, özellik, kullanım durumu) odaklan.
- **Geçer:** Hiçbir alanda başka markanın adı yok.

#### Y-09 · Birden fazla mağaza lokalizasyonu · 🟡 · 🚀 · MAĞAZA
- **Düzeltme:** Öncelikli ülkeler için ayrı App Store lokalizasyonları oluştur (ad, alt başlık, anahtar kelimeler, ekran görüntüleri, açıklama). Her lokalizasyonun kendi 100 karakterlik anahtar kelime alanı vardır; bazı ülke mağazaları birden fazla lokalizasyonu indeksler (ek anahtar kelime alanı fırsatı — güncel listeyi doğrula).
- **Geçer:** Hedef pazarların her birinde yerel mağaza sayfası var.

#### Y-10 · Çeviri değil, yerel anahtar kelime araştırması · 🟡 · 🚀 · MAĞAZA
- **Hata:** Çeviri var ama lokalizasyon yok.
- **Düzeltme:** Kelimeleri doğrudan çevirmek yerine **o ülkedeki kullanıcıların gerçekten aradığı terimleri** araştır (App Store arama önerileri, rakiplerin yerel adları, ASO araçları). Ekran görüntüsü metinleri de yerelleştirilmeli.
- **Geçer:** Her lokalizasyonun anahtar kelimeleri yerel araştırmaya dayanıyor.

#### Y-11 · Anahtar kelime araştırması yapılmış · 🟠 · 🚀 · MAĞAZA
- **Düzeltme:** Arama hacmi (popularity/search volume), rekabet (competition/difficulty) ve alaka (relevance) üzerinden puanlanmış anahtar kelime listesi oluştur (Apple Ads arama popülerliği, App Store arama önerileri, AppFigures/Sensor Tower/AppTweak/Astro vb.). Yeni uygulamada önce düşük rekabetli, yüksek alakalı kelimeler.
- **Geçer:** Puanlı anahtar kelime tablosu proje notunda; seçimler gerekçeli.

#### Y-12 · İkon küçük boyutta okunuyor · 🟠 · 🚀 · MAĞAZA
- **Düzeltme:** İkonu küçük boyutta (arama sonucu, bildirim, Ayarlar ~29-60 pt) test et; detayı azalt; güçlü siluet/sembol; ikonda metin yok veya minimum; açık/koyu/renkli (tinted) ikon varyantları (iOS 18+); rakiplerin yanında ayırt edilebilir.
- **Geçer:** İkon en küçük boyutta tanınabilir ve tüm varyantları var.

#### Y-13 · En güçlü görsel ilk sırada · 🟠 · 🚀 · MAĞAZA
- **Hata:** En güçlü görsel 4. sırada.
- **Düzeltme:** En güçlü değer önermesini **ilk ekran görüntüsüne** taşı; arama sonuçlarında ilk 2-3 görsel (dikeyde) görünür ve çoğu kullanıcı sadece bunları görür. İlk görsel "Uygulama ne yapıyor + kullanıcı ne kazanıyor?" sorusunu cevaplamalı.
- **Geçer:** İlk görsel tek başına uygulamayı anlatıyor.

#### Y-14 · Ekran görüntülerinde başlık metni · 🟠 · 🚀 · MAĞAZA
- **Düzeltme:** Her ekran görüntüsünün neyi gösterdiğini kısa bir **başlık** (headline, 3-6 kelime, fayda odaklı) ile anlat; büyük, okunur font; arayüz gerçek kalmalı (T-17). Ekran görüntüsü metinleri (OCR) aramada etkili olabilir; anahtar kelimeleri doğal şekilde kullan.
- **Geçer:** Her görselde okunabilir fayda başlığı var.

#### Y-15 · App Preview videosu · 🟡 · 🚀 · MAĞAZA
- **Düzeltme:** İlk saniyelerde uygulamanın ana değerini gösteren kısa App Preview ekle (15-30 sn; gerçek uygulama içi görüntü; sessiz izlemeye uygun; ilk karesi poster olarak güçlü). Oyunlarda özellikle etkilidir.
- **Geçer:** En az bir önizleme videosu var ve ilk 3 saniyesi değeri gösteriyor.

#### Y-16 · Açıklamanın ilk satırları güçlü · 🟡 · 🚀 · MAĞAZA
- **Düzeltme:** Açıklamanın ilk 1-3 satırı "daha fazla"ya basmadan görünür; uygulamanın ne yaptığını ve kullanıcıya faydasını açıkla. Sonra özellik listesi, sosyal kanıt, abonelik bilgisi ve Terms/Privacy bağlantıları.
- **Geçer:** İlk satır tek başına uygulamayı satıyor.

#### Y-17 · Uygulama içinden değerlendirme isteme · 🟠 · 🚀 · MAĞAZA
- **Düzeltme:** Kullanıcı olumlu bir başarı/sonuç yaşadıktan **sonra** uygun zamanda StoreKit review prompt göster (SwiftUI `@Environment(\.requestReview)`); sistem yılda en fazla 3 kez gösterir, gösterileceği garanti değildir. İlk açılışta, hata sonrası veya paywall'da isteme; önce "Beğendin mi?" diye sorup memnun olmayanı destek formuna yönlendirmek (review gating) yerine doğrudan sistem istemini kullan. Ayarlarda "Değerlendir" bağlantısı (`action=write-review`).
- **Geçer:** İstem başarı anına bağlı ve sıklığı sınırlı.

#### Y-18 · Yorumlara cevap · 🟡 · 📈 · MAĞAZA
- **Düzeltme:** Özellikle olumsuz yorumlara profesyonel, kısa ve çözüm odaklı cevap ver; düzeltilen hatayı "X sürümünde düzeltildi" diye bildir (kullanıcı yorumunu güncelleyebilir); yorumlardaki tekrar eden sorunları Yapılacaklar'a ekle.
- **Geçer:** Olumsuz yorumların çoğu yanıtlı; tekrar eden şikâyetler görev olarak kayıtlı.

#### Y-19 · Ürün sayfası güncel · 🟡 · 📈 · MAĞAZA
- **Düzeltme:** Yeni özellikleri, ekran görüntülerini, açıklamayı ve sürüm notlarını düzenli güncelle; promosyon metnini (inceleme gerektirmez) kampanya/mevsim için kullan; In-App Events ile görünürlük; sürüm notları "Hata düzeltmeleri" yerine somut değişiklikler.
- **Geçer:** Ekran görüntüleri güncel sürümle eşleşiyor; son 2-3 aydır sayfa gözden geçirilmiş.

#### Y-20 · Trafik kaynağı ve anahtar kelime performansı takibi · 🟡 · 📈 · MAĞAZA
- **Hata:** Hangi anahtar kelimeden geldiğini bilmiyorsun.
- **Düzeltme:** App Store Connect → App Analytics'te kaynak (App Store Arama, Göz Atma, Web referansı, Uygulama referansı) performansını, ürün sayfası görüntüleme → indirme dönüşümünü, Apple Ads anahtar kelime raporlarını ve attribution verilerini (Z-04) takip et; anahtar kelime değişikliğinin etkisini sürüm bazında not al.
- **Geçer:** Aylık ASO raporu (en iyi kaynaklar, dönüşüm oranı, değişikliklerin etkisi) proje notunda.

#### Y-21 · Ürün sayfası testleri ve özel sayfalar · 🟢 · 📈 · MAĞAZA
- **Düzeltme:** Product Page Optimization ile ikon/ekran görüntüsü/önizleme A/B testi; reklam kampanyaları ve farklı kitleler için Custom Product Pages.
- **Geçer:** En az bir A/B testi yapılmış ve sonucu kayıtlı.

---

### Z. Büyüme, konumlandırma ve metrikler

> Profil: `MAĞAZA` (büyüme hedefi olan). Kişisel/arkadaş grubu uygulamalarında `➖`.

#### Z-01 · Tek ana problem ve tek persona · 🟠 · 🏁 · MAĞAZA
- **Sorun:** Uygulama 5 farklı iş yapıyor; hedef kitle "herkes".
- **Düzeltme:** Tek bir ana probleme odaklan; diğer özellikleri ikincil yap. Tek bir ana persona belirle ve şu cümleyi tamamla: **"Bu uygulama özellikle ____ için."** Bu cümle mağaza adı, alt başlık, ilk ekran görüntüsü ve onboarding'in ortak kaynağıdır.
- **Geçer:** Cümle proje ana notunda yazılı ve mağaza metinleriyle tutarlı.

#### Z-02 · İlk ekran görüntüsü ve mesaj · 🟠 · 🚀 · MAĞAZA
- **Sorun:** İlk ekran görüntüsü uygulamanın ne işe yaradığını anlatmıyor.
- **Düzeltme:** Y-13, Y-14.

#### Z-03 · Değerlendirme ve sosyal kanıt · 🟡 · 🚀 · MAĞAZA
- **Sorun:** Hiç değerlendirme yok; kimse ilk olmak istemiyor.
- **Düzeltme:** İlk kullanıcıları TestFlight/beta ile edin (yakın çevre, topluluklar, Reddit/Discord, ilgili forumlar); yorum istemeyi doğru kullanım anına bağla (Y-17); beta kullanıcılarının geri bildirimlerini ve sosyal kanıtı (izinle alıntı, kullanıcı sayısı) mağaza sayfasında ve web sitesinde görünür kıl. Sahte yorum satın alma/yazdırma **yasaktır** ve hesap kapatma nedenidir.
- **Geçer:** Yayın gününde bekleyen bir beta kitlesi var.

#### Z-04 · Ölçüm altyapısı (attribution) · 🟡 · 📈 · MAĞAZA GELİR
- **Kontrol:** Kurulumların hangi kaynaktan geldiği: App Store Connect App Analytics (ücretsiz, gizlilik dostu), Apple Ads attribution (AdServices), SKAdNetwork / AdAttributionKit (ATT'siz reklam ölçümü), gerekirse MMP (AppsFlyer, Adjust, Branch, Singular — ATT ve gizlilik beyanını etkiler, T-10/T-11). Analitik olay şeması: kurulum → onboarding tamam → ilk değer anı → paywall gösterimi → deneme → ödeme → D1/D7/D30 dönüş.
- **Geçer:** Olay şeması yazılı; huninin her adımı ölçülüyor.

#### Z-05 · Rakip analizi · 🟡 · 🏁 · MAĞAZA
- **Sorun:** Rakibi hiç indirmedin.
- **Düzeltme:** 5-10 rakibi indir; onboarding, fiyat, paywall, ASO (ad, alt başlık, ekran görüntüleri) ve özelliklerini karşılaştır; olumsuz yorumlarından fırsat çıkar ("Rakip X'te kullanıcılar en çok neden şikâyet ediyor?"). Tabloyu proje notuna kaydet.
- **Geçer:** Rakip karşılaştırma tablosu ve farklılaşma noktası yazılı.

#### Z-06 · Düzenli güncelleme ritmi · 🟡 · 📈 · MAĞAZA
- **Sorun:** Aylardır güncelleme yok.
- **Düzeltme:** Düzenli bir yayın ritmi (release cadence) belirle (örn. 2-4 haftada bir); yeni özellik + hata düzeltme + performans iyileştirmelerini yayınla; sürüm notları somut. Uzun süre güncellenmeyen uygulamalar hem algıda hem bazen mağaza görünürlüğünde geriler.
- **Geçer:** Ritim belli; son yayın tarihi ritmin içinde.

#### Z-07 · Dil ve pazar genişlemesi · 🟡 · 📈 · MAĞAZA
- **Sorun:** Sadece Türkçe.
- **Düzeltme:** Öncelikle İngilizce lokalizasyon (uygulama + mağaza sayfası) ekle; ardından hedef pazarlara göre genişlet (U-19, Y-09, Y-10). Fiyatlandırmayı pazara göre ayarla (V-09).
- **Geçer:** Hedef pazar sırası ve her biri için lokalizasyon durumu belli.

#### Z-08 · Paywall ve fiyat deneyleri · 🟢 · 📈 · GELİR
- **Kontrol:** Paywall tasarımı, fiyat, deneme süresi, plan sırası için A/B test (RevenueCat Experiments, Superwall, kendi flag'leri B-04); testte tek değişken; yeterli örneklem olmadan karar verme.
- **Geçer:** Deney sonuçları kayıtlı.

#### Z-09 · Metrik sözlüğü ve hedefler · 🟡 · 📈 · MAĞAZA GELİR
- **Ne/Neden:** Reklam ve kullanıcı edinme (UA) kararları bu metriklerle verilir. Ajan proje için takip edilecek **5-8 metrik** seçer, hedef değer koyar ve proje notuna yazar; hepsini birden takip etmek gerekmez. Sektör ortalamaları kategoriye, ülkeye ve döneme göre çok değişir; aşağıdaki "kaba referans" değerleri sadece başlangıç fikri içindir.

**Reklam maliyeti metrikleri**

| Metrik | Açılım | Basit anlamı | Formül | Not |
|---|---|---|---|---|
| CPM | Cost Per Mille | 1.000 reklam gösteriminin maliyeti | harcama ÷ gösterim × 1000 | Kitle ve platform rekabetini gösterir |
| CPC | Cost Per Click | 1 tıklamanın maliyeti | harcama ÷ tıklama | |
| CTR | Click-Through Rate | Reklamı görenlerin yüzde kaçı tıkladı | tıklama ÷ gösterim | Düşükse kreatif/mesaj sorunu |
| CPT | Cost Per Tap | Apple Ads'te 1 dokunmanın maliyeti | harcama ÷ dokunma | Apple Ads'in CPC karşılığı |
| TTR | Tap-Through Rate | Apple Ads'te gösterimlerin yüzde kaçı dokunmaya döndü | dokunma ÷ gösterim | Düşükse anahtar kelime alakasız veya ilk görseller zayıf (Y-13) |
| CR | Conversion Rate | Dokunanların/tıklayanların yüzde kaçı indirdi veya kayıt oldu | dönüşüm ÷ tıklama | Düşükse ürün sayfası sorunu (Y kategorisi) |
| CPI | Cost Per Install | 1 uygulama indirmesinin maliyeti | harcama ÷ kurulum | |
| CPR | Cost Per Registration / Result | 1 kayıt veya belirlenen aksiyonun maliyeti | harcama ÷ kayıt (veya sonuç) | |
| CPA | Cost Per Acquisition / Action | 1 satın alma veya hedef aksiyonun maliyeti | harcama ÷ hedef aksiyon | Hangi aksiyonun "A" olduğu yazılmalı |
| CAC | Customer Acquisition Cost | 1 **ödeyen** müşteriyi kazanmanın toplam maliyeti | toplam pazarlama+satış maliyeti ÷ yeni ödeyen müşteri | CPA'dan geniş: reklam dışı maliyetler de dahil |

**Gelir ve değer metrikleri**

| Metrik | Açılım | Basit anlamı | Formül | Not |
|---|---|---|---|---|
| ARPU | Average Revenue Per User | Kullanıcı başına ortalama gelir | gelir ÷ aktif kullanıcı (dönem) | Ödeyenler için ARPPU ayrı hesaplanır |
| LTV | Lifetime Value | Bir kullanıcının yaşam döngüsü boyunca getirdiği toplam değer | kaba: ARPU × ortalama ömür; abonelikte ≈ aylık ARPPU ÷ aylık churn | Apple/Google komisyonu (%15/%30) **sonrası** net gelirle hesapla |
| ROAS | Return On Ad Spend | Reklama harcanan 1 TL'nin kaç TL gelir getirdiği | reklam kaynaklı gelir ÷ reklam harcaması | Zaman penceresi belirt (D7 ROAS, D30 ROAS) |
| Payback Period | Geri dönüş süresi | Harcanan paranın kaç günde geri kazanıldığı | kohortun kümülatif net geliri CAC'ı geçtiği gün | Nakit akışı için kritik |
| LTV:CAC | Oran | Birim ekonomi sağlıklı mı | LTV ÷ CAC | Kaba referans: ≥ 3 sağlıklı, < 1 her kullanıcıda zarar |
| Ad Revenue eCPM | Effective CPM | Reklam gösterimlerinden 1.000 gösterim başına elde edilen gelir | reklam geliri ÷ gösterim × 1000 | Reklamla para kazanan uygulamalar için (V-14) |

**Elde tutma (retention) metrikleri**

| Metrik | Basit anlamı | Not |
|---|---|---|
| D1 | Kurulumdan 1 gün sonra geri gelen kullanıcı oranı | Onboarding ve ilk değer anının (U-06) göstergesi |
| D7 | 7 gün sonra geri gelen oran | Alışkanlık oluşuyor mu |
| D30 | 30 gün sonra geri gelen oran | Ürün-pazar uyumunun göstergesi |
| Churn | Dönem içinde aboneliği/kullanımı bırakanların oranı | Aboneliklerde aylık churn LTV'yi belirler |

> Kaba referans (mobil, kategoriye göre çok değişir): D1 %25-40, D7 %10-20, D30 %5-10. Kendi kohort eğrin düzleşiyorsa (belli bir oranda sabitleniyorsa) ürün tutuyordur; sıfıra iniyorsa reklam harcaması kayıptır.

**Reklam platformu ve gizlilik kavramları**

| Kavram | Basit anlamı | Pratik not |
|---|---|---|
| Learning Phase | Meta'nın (ve benzer platformların) reklam setini optimize etmek için yeterli dönüşüm verisi topladığı dönem | Bu dönemde sık değişiklik yapma; Meta için kabaca haftada ~50 optimizasyon olayı hedeflenir (güncel değeri doğrula); düşük bütçede daha üst huni olayına (kurulum) optimize et |
| ATT | App Tracking Transparency: iOS'ta kullanıcının takip izni | İzin oranı düşüktür; ölçüm SKAdNetwork/AdAttributionKit'e dayanır (T-10) |
| Attribution | Kullanıcının hangi reklam/kampanyadan geldiğini ölçme | Z-04 |
| MMP | Mobile Measurement Partner: reklam kaynaklarını ve dönüşümleri ölçen üçüncü taraf platform (AppsFlyer, Adjust, Branch, Singular) | Birden fazla reklam ağında harcama yoksa genelde gereksiz; App Analytics + Apple Ads yeterli olabilir |
| SKAdNetwork / AdAttributionKit | Apple'ın kullanıcıyı tanımlamadan reklam dönüşümü ölçme sistemi | Conversion value şemasını erken kurgula |

- **Karar kuralları (ajanın önerilerinde kullanacağı):**
  - Ücretli reklama başlamadan önce: D1/D7 retention ölçülmüş, paywall/ürün sayfası dönüşümü makul ve LTV kabaca tahmin edilmiş olmalı. Tutmayan ürüne reklam harcamak para yakmaktır.
  - CTR/TTR düşük → kreatif veya anahtar kelime sorunu. CR düşük → ürün sayfası sorunu (Y). Kurulum var ama D1 düşük → onboarding sorunu (U). Retention iyi ama gelir düşük → paywall/fiyat sorunu (V).
  - Hedef: CPI < LTV ve kabul edilebilir payback süresi; ROAS hedefini LTV penceresine göre koy.
- **Geçer:** Projede seçilen metrikler, hedefleri ve ölçüm kaynağı proje notunda; aylık güncelleniyor.

---

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

---

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

---

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

---

## 7. Bu dosyanın bakımı

- Yeni bir madde eklemek için ilgili kategoriye bir sonraki ID ile ekle; mevcut ID'leri **değiştirme** (projelerdeki raporlar bu ID'lere bağlı).
- Bir maddeyi kaldırmak yerine başına `(kullanımdan kalktı)` yaz.
- Önemli değişiklikte frontmatter'daki `sürüm` ve `güncellendi` alanlarını artır. Projelerdeki kural dosyaları kaynak sürümünü yazdığı için hangilerinin eskidiği görülür.
- Bir projede öğrenilen genel ders (örn. "Firestore listener'ı kaldırmamak faturayı 10 katına çıkardı") ilgili maddenin **Kontrol** satırına eklenmelidir. Böylece tüm projeler faydalanır.

---

## 8. Fazlara yayma: maddeler proje planına nasıl dağıtılır

Amaç: Kontrol maddeleri yayından bir gün önce topluca değil, **ait oldukları fazda** ele alınsın. Ajan, uygulanır maddeleri (Bölüm 0, adım 4) projenin `Plan.md` fazlarına "kontrol kapısı" olarak dağıtır; faz başında okur, faz sırasında uygular, faz sonunda kontrol eder.

### 8.1 Standart faz tipleri ve varsayılan maddeleri

Projenin kendi fazları bu tiplerle birebir aynı olmak zorunda değildir. Ajan her standart tipin maddelerini, projede **içerik olarak en uygun** faza yerleştirir.

| Faz tipi | Ne zaman | Varsayılan maddeler (sadece uygulanır olanlar) |
|---|---|---|
| **F0 · Temel / kurulum** | İlk faz veya mevcut projede "şimdi" | Tüm 🏁 maddeler: A-01…A-03, B-01, B-02, B-05, D-05, D-06, E-01, E-02, E-06, F-01, F-02, F-12 (iskelet), F-13, G-04, H-01, H-02, H-03 (strateji), I-05, K-01, L-02, M-02, M-06, N-01 (temel), N-02 (altyapı), O-03, O-04, AN-01, AN-03, AN-05, Q-01, Q-02, S-01, T-08, T-12, T-13, U-02, U-19, V-11, Z-01, Z-05 |
| **Özellik fazları** | Her özellik/modül fazı | **Özellik Bitti Tanımı** (8.2) + özelliğe özgü maddeler (8.3) |
| **İlk deneyim / onboarding** | Ana akış çalıştıktan sonra | U-01 … U-06, U-12 … U-16, N-03, N-04, N-08, Z-01 (mesaj) |
| **Gelir / paywall** | Ödeme eklenirken | V-01 … V-14, T-02 … T-04, T-12, U-07 … U-09, F-18, X-09, X-15 |
| **Sertleştirme** | Beta'dan önce | Kalan F maddeleri, X-01 … X-15, E-03, E-04, H-04, H-05, H-08, H-09, J-04 … J-09, K-02, K-03, L-01, L-03 … L-06, L-10, D-01 … D-03, D-07, C-01, B-03, R-01, R-03, R-08, AN-04, AN-06 … AN-09 |
| **Yayın hazırlığı** | Mağaza/üretim gönderiminden önce | T-01 … T-21 (Apple), GP-01 … GP-14 (Android), AN-02, AN-10, W-01 … W-30, G-01 … G-03, G-07, G-08, O-01, O-02, O-05 … O-08, P-01 … P-05, C-06, C-07, A-04, M-01, R-02, R-05, U-17 … U-19 |
| **Mağaza ve lansman** | Yayın haftası | Y-01 … Y-17, Z-02 … Z-04, Z-09 (hedefler) |
| **İşletim / büyüme** | Yayın sonrası, sürekli | Y-18 … Y-21, Z-06 … Z-09, R-04, R-06, R-07, L-07 … L-09, D-08, H-06, H-07, J-10, J-11, M-03 … M-05 AN-11 ve diğer 📈 maddeler |

### 8.2 Özellik Bitti Tanımı (her özellik fazında geçerli)

Bir özellik fazı ancak şunlar sağlanınca "bitti" sayılır (uygulanmayanlar atlanır):

- [ ] İş mantığının birim testi var ve yeşil (D-01).
- [ ] Yeni/değişen veri modeli varsa migration eklendi ve eski veriyle denendi (H-03); tarih/saat UTC (H-02).
- [ ] Yeni koleksiyon/uç nokta varsa sunucu tarafı yetki + şema doğrulaması + kurallar testi (E-02, F-02, F-12, D-02).
- [ ] Ekranlarda boş / yükleniyor / hata / çevrimdışı durumları (N-03, N-04, U-10, U-11).
- [ ] Erişilebilirlik etiketleri, Dynamic Type, dokunma alanları (N-01, U-13).
- [ ] Kullanıcıya görünen metinler yerelleştirme dosyasında; Türkçe İ/ı doğru (N-02).
- [ ] Karanlık modda kontrol edildi (N-05).
- [ ] Ağ çağrılarında timeout ve hata yönetimi (K-01, K-02).
- [ ] Loglarda sır/kişisel veri yok (L-02).
- [ ] Yeni izin varsa `Info.plist` gerekçesi + bağlamlı istek + `PrivacyInfo.xcprivacy` (G-02, G-03, T-09).
- [ ] Lint ve derleyici uyarısı yok (D-05, D-06).

### 8.3 Özelliğe göre eklenen maddeler

Özellik fazı şunlardan birini içeriyorsa ilgili maddeler o fazın kapısına eklenir:

| Özellik içeriyor | Eklenecek maddeler |
|---|---|
| Giriş / hesap | E-01 … E-05, T-01, T-06, U-02, X-05, X-11 |
| Paylaşım / eşleşme / davet | E-06, H-08, H-10, X-04 |
| Ödeme / abonelik / reklam | V kategorisi, T-02 … T-04, T-10, T-12, F-18 |
| Dosya / fotoğraf yükleme | F-09, I-01 … I-03, X-08 |
| Kullanıcı içeriği (yorum, mesaj, profil) | T-14, G-08, F-04, X-02 |
| Bildirim | K-08, U-03, U-16, T-21 (pazarlama bildirimi) |
| Gerçek zamanlı / senkron | K-07, H-08, H-10, J-05 |
| Arka plan işi / cron / kuyruk | K-04 … K-06, M-04 |
| Webhook / dış entegrasyon | F-18, F-19, K-01 … K-03, M-05, X-09 |
| Konum / kamera / sağlık verisi | G-03, G-04, F-13, T-09, T-16, J-06 |
| Yapay zekâ | S-01 … S-05, F-06, R-01, R-08 |
| Widget / uzantı / Live Activity | O-06 |
| Çok oyunculu | Q-02, Q-03, X-15 |
| Yeni dil / pazar | N-02, U-19, Y-09, Y-10, V-09, Z-07 |

### 8.4 Plan.md'ye yazma biçimi

Ajan `Plan.md` içindeki her fazın altına bir satır ekler. Faz adlarını ve sırasını değiştirmez:

```markdown
## Faz 3: Firebase senkronu
- (fazın mevcut içeriği)
- **Kontrol kapısı:** E-02 E-06 F-12 H-08 H-09 H-10 K-07 X-04 + Özellik Bitti Tanımı
```

`Plan.md`'nin en üstüne (hedefin altına) tek seferlik bir blok eklenir:

```markdown
> **Üretim kontrolü:** Profil `BULUT + MAĞAZA + GELİR` · Aşama `Prototip`
> Kaynak: ~/Desktop/hafıza/hafıza/Kurallar/Üretim Kontrolü.md (v1.1) · Rapor: [[Projeler/<Ad>/Kontrol|Kontrol]]
> Her özellik fazında Özellik Bitti Tanımı (§8.2) geçerlidir.
```

### 8.5 Yayma kuralları

1. **Tek sahip:** Her madde ID'si tek bir fazda "tamamlanır" (sahip faz). Sonraki fazlarda yeniden kontrol edilebilir ama tekrar yazılmaz. İstisna: Özellik Bitti Tanımı her özellik fazında geçerlidir.
2. **Erken olan kazanır:** 🏁 maddeler mümkün olan en erken faza konur. Proje zaten ilerlemişse ve 🏁 madde eksikse, **bir sonraki** faza 🔴 öncelikle eklenir.
3. **Eksik fazlar:** Proje yayına gidecekse ve planda "Sertleştirme", "Yayın hazırlığı", "Mağaza ve lansman" karşılığı yoksa, ajan bunları plan sonuna ekler ve kullanıcıya tek cümleyle bildirir. Proje kişisel kullanım içinse sadece gerekenler eklenir.
4. **Orantılılık:** Küçük, kişisel `YEREL` bir uygulamada kapılar kısa kalır (birkaç madde). Her fazı onlarca maddeyle doldurma; uygulanmayan maddeler `Kontrol.md`'de `➖` olarak kalır.
5. **Görevleştirme:** Faz başladığında, kapıdaki maddelerden iş gerektirenler `Yapılacaklar.md` "Şimdi" bölümüne `- [ ] [Üretim H-03] SwiftData şemasını VersionedSchema'ya taşı` biçiminde eklenir. Sadece kontrol gerektirenler faz sonunda kontrol edilir.

### 8.6 Faz döngüsü (ajan her fazda bunu uygular)

1. **Faz başında:** `Plan.md`'deki kontrol kapısı ID'lerinin tam metnini bu dosyadan oku (sadece o maddeleri). İş gerektirenleri `Yapılacaklar.md`'ye ekle.
2. **Faz sırasında:** Kod yazarken bu maddelerin "Kontrol" ve "Geçer" ölçütlerini tasarım kuralı olarak uygula. Kapı dışındaki bir maddeyle ilgili risk görürsen not et, kapsamı büyütme.
3. **Faz sonunda:** Her kapı maddesini kontrol et, kanıtla `Kontrol.md` tablosunu güncelle.
   - 🔴 madde ❌/⚠️ ise faz **bitti sayılmaz**. Ancak kullanıcı açıkça erteleme onayı verirse `Kontrol.md`'ye `Ertelendi → Faz N: <neden>` yazılır ve madde o faza taşınır.
   - 🟠/🟡 eksikler sonraki uygun faza taşınır ve not edilir.
4. **Aşama değişince** (Prototip → Beta → Yayında): Bölüm 2'ye göre zorunlu maddeler değişir; kapılar yeniden değerlendirilir.
5. **Yayın kapısı:** "Yayın hazırlığı" fazının sonunda T ve W kategorilerinin tamamı ve tüm 🔴 maddeler ✅ veya `➖` olmalıdır. Aksi halde ajan "yayına hazır" demez.
