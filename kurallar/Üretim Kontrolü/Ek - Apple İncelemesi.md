---
tür: üretilmiş-parça
kaynak: Kurallar/Üretim Kontrolü.md
kaynak-sürüm: 1.3
kaynak-özet: b6bdd028b3e2
---

# Üretim Kontrolü: Ek - Apple İncelemesi

> **Elle düzenlenmez.** Bu dosya `Kurallar/Üretim Kontrolü.md` kaynağından `~/.claude/hooks/uretim_bol.py` ile üretilir; değişiklik kaynağa yapılır, parçalar oturum başında kendiliğinden yenilenir.
>
> **Kimler okur:** App Store'a gönderilecek iOS ve macOS uygulamaları (T kategorisi).
> **Nasıl okunur:** tamamını değil. Önce dizine bak; fazın kontrol kapısındaki kimliklerin metnini aşağıda bul. Profil, önem, aşama ve fazlara yayma kuralları [[Kurallar/Üretim Kontrolü/Yöntem|Yöntem]] notunda.


21 madde. "Ayrıca" sütunu maddenin hangi tür dosyasında da geçtiğini gösterir; onu okuduysan burada atla.


## Dizin

| Kimlik | Madde | Önem | Zaman | Profil | Ayrıca |
|---|---|---|---|---|---|
| T-01 | Hesap silme | 🔴 | 🚀 | MAĞAZA (hesap oluşturulabiliyorsa) | — |
| T-02 | Kullanım koşulları ve gizlilik bağlantıları | 🔴 | 🚀 | MAĞAZA GELİR | — |
| T-03 | Satın almaları geri yükle (Restore Purchases) | 🔴 | 🚀 | GELİR | — |
| T-04 | Paywall şeffaflığı | 🔴 | 🚀 | GELİR | — |
| T-05 | Bozuk veya eksik arayüz | 🔴 | 🚀 | MAĞAZA | — |
| T-06 | İnceleme için test hesabı | 🔴 | 🚀 | MAĞAZA (giriş gerekiyorsa) | — |
| T-07 | İnceleme sonrası davranış değiştirme yok | 🔴 | 🚀 | MAĞAZA | — |
| T-08 | Web sarmalayıcı (wrapper) değil | 🔴 | 🏁 | MAĞAZA | — |
| T-09 | İzin isteklerinde gerekçe | 🔴 | 🚀 | MAĞAZA | — |
| T-10 | Takip ve ATT | 🔴 | 🚀 | MAĞAZA (takip yapılıyorsa) | — |
| T-11 | Gizlilik beyanı gerçek davranışla uyumlu | 🔴 | 🚀 | MAĞAZA | — |
| T-12 | Dijital içerik satışı ve IAP | 🔴 | 🏁 | GELİR | — |
| T-13 | Çocuk kategorisi | 🔴 | 🏁 | MAĞAZA (Kids kategorisi veya çocuklara yönelik) | — |
| T-14 | Kullanıcı üretimli içerik (UGC) | 🔴 | 🚀 | MAĞAZA (UGC varsa) | — |
| T-15 | Telif hakkı ve marka | 🔴 | 🚀 | MAĞAZA | — |
| T-16 | Sağlık iddiaları | 🔴 | 🚀 | MAĞAZA (sağlık/fitness/regl/uyku/diyet) | — |
| T-17 | Ekran görüntüsü doğruluğu | 🟠 | 🚀 | MAĞAZA | — |
| T-18 | Gerçek cihaz testi | 🔴 | 🚀 | MAĞAZA | — |
| T-19 | Ürün kalitesi ve tamamlanmışlık | 🔴 | 🚀 | MAĞAZA | — |
| T-20 | Ret (rejection) sonrası süreç | 🟠 | 🚀 | MAĞAZA | — |
| T-21 | Diğer sık ret nedenleri | 🟠 | 🚀 | MAĞAZA | — |

---

## Maddeler

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
