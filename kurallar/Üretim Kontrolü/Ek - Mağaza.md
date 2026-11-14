---
tür: üretilmiş-parça
kaynak: Kurallar/Üretim Kontrolü.md
kaynak-sürüm: 1.3
kaynak-özet: b6bdd028b3e2
---

# Üretim Kontrolü: Ek - Mağaza

> **Elle düzenlenmez.** Bu dosya `Kurallar/Üretim Kontrolü.md` kaynağından `~/.claude/hooks/uretim_bol.py` ile üretilir; değişiklik kaynağa yapılır, parçalar oturum başında kendiliğinden yenilenir.
>
> **Kimler okur:** Mağazaya çıkan her uygulama ve oyun (`MAĞAZA`): yayın öncesi ürün sorunları ve kırma testi. Platform incelemesi ayrı dosyada.
> **Nasıl okunur:** tamamını değil. Önce dizine bak; fazın kontrol kapısındaki kimliklerin metnini aşağıda bul. Profil, önem, aşama ve fazlara yayma kuralları [[Kurallar/Üretim Kontrolü/Yöntem|Yöntem]] notunda.


15 madde. "Ayrıca" sütunu maddenin hangi tür dosyasında da geçtiğini gösterir; onu okuduysan burada atla.


## Dizin

| Kimlik | Madde | Önem | Zaman | Profil | Ayrıca |
|---|---|---|---|---|---|
| U-01 | Açılış 2 saniyeden uzun | 🟠 | 🚀 | MAĞAZA OYUN | Oyun |
| U-02 | Değer göstermeden kayıt istemek | 🟠 | 🏁 | MAĞAZA BULUT WEB-API | Web, Apple, Android |
| U-03 | Açılışta toplu izin isteği | 🟠 | 🚀 | MAĞAZA | — |
| U-04 | Boş ana ekran | 🟠 | 🚀 | MAĞAZA WEB-S WEB-API | Web |
| U-05 | Uzun onboarding | 🟡 | 🚀 | MAĞAZA | — |
| U-06 | İlk değer anına (time-to-value) ulaşmak çok uzun | 🟠 | 🚀 | MAĞAZA WEB-S WEB-API OYUN | Web, Oyun |
| U-10 | İnternet gidince beyaz ekran | 🔴 | 🚀 | MAĞAZA BULUT WEB-S WEB-API | Web, Apple, Android |
| U-12 | Klavye giriş alanını örtüyor | 🟠 | 🚀 | MAĞAZA WEB-S WEB-API | Web |
| U-13 | Dokunma hedefleri küçük | 🟠 | 🚀 | MAĞAZA WEB-S WEB-API OYUN | Web, Oyun |
| U-14 | Geri tuşu / geri hareketi çalışmıyor | 🟠 | 🚀 | MAĞAZA WEB-S WEB-API | Web |
| U-15 | Karanlık mod bozuk | 🟠 | 🚀 | MAĞAZA WEB-S WEB-API | Web |
| U-16 | İlk gün gereksiz bildirim | 🟡 | 🚀 | MAĞAZA | — |
| U-17 | Hesap silme yok veya bulunmuyor | 🔴 | 🚀 | MAĞAZA BULUT | Web, Apple, Android |
| U-18 | Uygulama boyutu 200 MB üstü | 🟡 | 🚀 | MAĞAZA OYUN | Oyun |
| U-19 | Tek dil | 🟡 | 🏁 | MAĞAZA | — |

---

## Maddeler

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

#### U-10 · İnternet gidince beyaz ekran · 🔴 · 🚀 · MAĞAZA BULUT WEB-S WEB-API
- **Düzeltme:** Çevrimdışı ve hata durumu tasarla; kullanıcıya bağlantının koptuğunu açıkça bildir; önbellekteki veriyi göster; bağlantı gelince otomatik yenile (N-04, W-01, W-10).
- **Geçer:** Uçak modunda hiçbir ekran boş/sonsuz yükleme göstermiyor.

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
