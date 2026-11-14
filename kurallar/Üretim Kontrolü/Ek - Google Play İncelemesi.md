---
tür: üretilmiş-parça
kaynak: Kurallar/Üretim Kontrolü.md
kaynak-sürüm: 1.3
kaynak-özet: b6bdd028b3e2
---

# Üretim Kontrolü: Ek - Google Play İncelemesi

> **Elle düzenlenmez.** Bu dosya `Kurallar/Üretim Kontrolü.md` kaynağından `~/.claude/hooks/uretim_bol.py` ile üretilir; değişiklik kaynağa yapılır, parçalar oturum başında kendiliğinden yenilenir.
>
> **Kimler okur:** Google Play'e gönderilecek Android uygulamaları (GP kategorisi).
> **Nasıl okunur:** tamamını değil. Önce dizine bak; fazın kontrol kapısındaki kimliklerin metnini aşağıda bul. Profil, önem, aşama ve fazlara yayma kuralları [[Kurallar/Üretim Kontrolü/Yöntem|Yöntem]] notunda.


14 madde. "Ayrıca" sütunu maddenin hangi tür dosyasında da geçtiğini gösterir; onu okuduysan burada atla.


## Dizin

| Kimlik | Madde | Önem | Zaman | Profil | Ayrıca |
|---|---|---|---|---|---|
| GP-01 | Veri güvenliği formu | 🔴 | 🚀 | MAĞAZA | — |
| GP-02 | Gizlilik politikası | 🔴 | 🚀 | MAĞAZA | — |
| GP-03 | Hesap silme | 🔴 | 🚀 | MAĞAZA (hesap oluşturulan uygulama) | — |
| GP-04 | Hedef API düzeyi şartı | 🔴 | 🚀 | MAĞAZA | — |
| GP-05 | Ödemeler: Play Faturalandırma | 🔴 | 🚀 | MAĞAZA GELİR | — |
| GP-06 | Abonelik şeffaflığı | 🔴 | 🚀 | MAĞAZA GELİR | — |
| GP-07 | Hassas izin ve API beyanları | 🔴 | 🚀 | MAĞAZA | — |
| GP-08 | İçerik derecelendirme, hedef kitle ve çocuklar | 🟠 | 🚀 | MAĞAZA | — |
| GP-09 | Kullanıcı tarafından üretilen içerik | 🔴 | 🚀 | MAĞAZA (yorum, mesaj, profil, paylaşım olan uygulama) | — |
| GP-10 | Reklamlar ve reklam kimliği | 🟠 | 🚀 | MAĞAZA GELİR | — |
| GP-11 | Mağaza kaydının doğruluğu | 🟠 | 🚀 | MAĞAZA | — |
| GP-12 | Test kanalları ve aşamalı yayın | 🟠 | 🚀 | MAĞAZA | — |
| GP-13 | İnceleme için uygulama erişimi | 🔴 | 🚀 | MAĞAZA (giriş gerektiren uygulama) | — |
| GP-14 | Geliştirici hesabı ve iletişim bilgileri | 🟡 | 🚀 | MAĞAZA | — |

---

## Maddeler

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
