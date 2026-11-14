---
tür: üretilmiş-parça
kaynak: Kurallar/Üretim Kontrolü.md
kaynak-sürüm: 1.3
kaynak-özet: b6bdd028b3e2
---

# Üretim Kontrolü: Ek - Gelir

> **Elle düzenlenmez.** Bu dosya `Kurallar/Üretim Kontrolü.md` kaynağından `~/.claude/hooks/uretim_bol.py` ile üretilir; değişiklik kaynağa yapılır, parçalar oturum başında kendiliğinden yenilenir.
>
> **Kimler okur:** Satın alma, abonelik, paywall ya da reklam geliri olan projeler (`GELİR`).
> **Nasıl okunur:** tamamını değil. Önce dizine bak; fazın kontrol kapısındaki kimliklerin metnini aşağıda bul. Profil, önem, aşama ve fazlara yayma kuralları [[Kurallar/Üretim Kontrolü/Yöntem|Yöntem]] notunda.


21 madde. "Ayrıca" sütunu maddenin hangi tür dosyasında da geçtiğini gösterir; onu okuduysan burada atla.


## Dizin

| Kimlik | Madde | Önem | Zaman | Profil | Ayrıca |
|---|---|---|---|---|---|
| F-18 | Webhook güvenliği | 🔴 | 🚀 | WEB-API BULUT GELİR | Web, Apple, Android |
| R-08 | SaaS harcama takibi ve otomasyonu | 🟠 | 🚀 | BULUT WEB-API YZ GELİR | Web, Apple, Android |
| U-07 | Paywall ilk karede açılıyor | 🟠 | 🚀 | GELİR | — |
| U-08 | Paywall kapatma tuşu görünmüyor | 🔴 | 🚀 | GELİR | — |
| U-09 | Paywall / satın alma çöküyor | 🔴 | 🚀 | GELİR | — |
| V-01 | Premium'un ne açtığı belli | 🔴 | 🚀 | GELİR | — |
| V-02 | Fiyat paywall üzerinde doğrudan görünüyor | 🔴 | 🚀 | GELİR | — |
| V-03 | Otomatik yenileme ve koşullar belirtilmiş | 🔴 | 🚀 | GELİR | — |
| V-04 | Görünür ve erişilebilir kapat butonu | 🔴 | 🚀 | GELİR | — |
| V-05 | Satın almaları geri yükle | 🔴 | 🚀 | GELİR | — |
| V-06 | Birden fazla plan ve yıllık planın öne çıkması | 🟡 | 🚀 | GELİR | — |
| V-07 | Ücretsiz deneme veya sınırlı ücretsiz kullanım | 🟡 | 🚀 | GELİR | — |
| V-08 | Paywall yerleşimi ve zorlayıcı geçişler | 🟡 | 🚀 | GELİR | — |
| V-09 | Bölgesel fiyatlandırma | 🟡 | 🚀 | GELİR | — |
| V-10 | Satın alma akışının test edilmesi | 🔴 | 🚀 | GELİR | — |
| V-11 | Yetki (entitlement) yönetimi ve doğrulama | 🔴 | 🏁 | GELİR | — |
| V-12 | Ödeme hunisi ve başarısız işlemlerin izlenmesi | 🟠 | 🚀 | GELİR | — |
| V-13 | Abonelik yaşam döngüsü ve elde tutma | 🟢 | 📈 | GELİR | — |
| V-14 | Reklam geliri (varsa) | 🟡 | 🚀 | GELİR | — |
| X-09 | Webhook imza atlatma testi | 🔴 | 🚀 | WEB-API GELİR | Web |
| X-15 | İstemci tarafı güven testi | 🟠 | 🚀 | BULUT OYUN GELİR | Web, Apple, Android, Oyun |

---

## Maddeler

### F. API ve uygulama güvenliği

#### F-18 · Webhook güvenliği · 🔴 · 🚀 · WEB-API BULUT GELİR
- **Ne/Neden:** Ödeme (Stripe, RevenueCat, App Store Server Notifications), Git, form servisleri webhook gönderir. Doğrulanmayan webhook'a herkes "ödeme başarılı" yazabilir.
- **Kontrol:**
  - **İmza doğrulama:** sağlayıcının imzası (Stripe `Stripe-Signature`, RevenueCat authorization başlığı, App Store JWS imzalı bildirim) **ham gövde** üzerinden doğrulanıyor mu (JSON parse edildikten sonra doğrulama bozulur); karşılaştırma sabit zamanlı mı.
  - **Replay koruması:** zaman damgası toleransı (örn. 5 dk) + olay kimliği (`event.id`) daha önce işlendiyse atlama (idempotency, H-09).
  - Gövde boyutu sınırı; sadece beklenen olay türleri işleniyor.
  - Webhook yanıtı hızlı (2xx döndürüp ağır işi kuyruğa/arka plana atma, K-04); başarısız olursa sağlayıcının tekrar denemesine dayanıklı.
- **Geçer:** İmzasız veya eski/tekrarlanan webhook reddediliyor (X-09 ile test edilmiş).

### R. Operasyon, maliyet ve bakım

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

### U. Yayınlamadan önce düzeltilecek ürün sorunları (ilk deneyim)

> Profil: `MAĞAZA` (ve kullanıcıya açılan her `WEB-S`/`WEB-API`/`OYUN`). Bu sorunlar inceleme reddi değil ama **ilk gün kullanıcı kaybı** demektir. "Yayın hazırlığı" fazında, mümkünse daha önce "İlk deneyim" fazında çözülür.

#### U-07 · Paywall ilk karede açılıyor · 🟠 · 🚀 · GELİR
- **Düzeltme:** Önce ürünün değerini göster, paywall'u **bağlamlı** bir noktada aç (premium özelliğe dokunulduğunda, değer yaşandıktan sonra). Onboarding sonu paywall'u kabul edilen bir kalıptır ama kapatılabilir olmalı (U-08). Ayrıntı: V.
- **Geçer:** Paywall'un açılma noktaları listelenmiş ve her biri bağlamlı.

#### U-08 · Paywall kapatma tuşu görünmüyor · 🔴 · 🚀 · GELİR
- **Düzeltme:** Belirgin ve kolay erişilebilir kapat/geri dön kontrolü (V-04). Gecikmeli beliren, soluk gri, çok küçük "X" hem kullanıcı kaybettirir hem ret riskidir.
- **Geçer:** Kapat butonu anında görünür, ≥ 44pt dokunma alanı, yeterli kontrast.

#### U-09 · Paywall / satın alma çöküyor · 🔴 · 🚀 · GELİR
- **Düzeltme:** Tüm satın alma akışını gerçek cihazda test et (V-10): ürünler yüklenmezse, ağ yoksa, kullanıcı iptal ederse, ödeme beklemede (Ask to Buy) kalırsa, zaten aboneyse.
- **Geçer:** Satın alma akışının tüm dalları gerçek cihazda denenmiş.

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

### X. Saldırgan gibi test (kendi uygulamanda güvenlik testi)

> Profil: `BULUT`, `WEB-API` (ve sunucusu olan `OYUN`). **Yalnızca yetkili olduğun kendi uygulamanda**, tercihen staging ortamında (B-03) ve test hesaplarıyla yapılır. Üretim verisine zarar verecek, başkasının hesabına dokunacak veya hizmeti düşürecek test yapılmaz. Ajan her testi önce kullanıcıya listeler, onay alır, sonuçları `Kontrol.md`'ye yazar. Bulunan açıklar 🔴 olarak ilgili maddeye bağlanır. Araçlar: tarayıcı DevTools, `curl`, Burp Suite Community / OWASP ZAP (yerel proxy), Firebase Rules Playground / emülatör.

#### X-09 · Webhook imza atlatma testi · 🔴 · 🚀 · WEB-API GELİR
- **Nasıl:** Webhook ucuna imzasız, yanlış imzalı, eski zaman damgalı ve daha önce işlenmiş bir olayı tekrar gönder ("ödeme başarılı" sahte olayı).
- **Geçer:** Hepsi reddediliyor veya etkisiz (F-18).

#### X-15 · İstemci tarafı güven testi · 🟠 · 🚀 · BULUT OYUN GELİR
- **Nasıl:** İstemci kodunda değiştirilebilecek değerleri değiştir: premium bayrağı (`UserDefaults`/localStorage `isPremium`), skor, fiyat, indirim, stok; proxy ile isteği düzenle. Firebase'de istemcinin yazabildiği alanları kurallar dışında dene.
- **Geçer:** Sunucu/kurallar değiştirilmiş değeri kabul etmiyor (V-11, F-17, Q-02).
