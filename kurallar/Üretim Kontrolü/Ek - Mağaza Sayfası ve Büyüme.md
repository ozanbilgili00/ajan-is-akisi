---
tür: üretilmiş-parça
kaynak: Kurallar/Üretim Kontrolü.md
kaynak-sürüm: 1.3
kaynak-özet: b6bdd028b3e2
---

# Üretim Kontrolü: Ek - Mağaza Sayfası ve Büyüme

> **Elle düzenlenmez.** Bu dosya `Kurallar/Üretim Kontrolü.md` kaynağından `~/.claude/hooks/uretim_bol.py` ile üretilir; değişiklik kaynağa yapılır, parçalar oturum başında kendiliğinden yenilenir.
>
> **Kimler okur:** Yayın haftası ve sonrası: ASO, mağaza sayfası, büyüme ve metrikler (Y ve Z kategorileri).
> **Nasıl okunur:** tamamını değil. Önce dizine bak; fazın kontrol kapısındaki kimliklerin metnini aşağıda bul. Profil, önem, aşama ve fazlara yayma kuralları [[Kurallar/Üretim Kontrolü/Yöntem|Yöntem]] notunda.


30 madde. "Ayrıca" sütunu maddenin hangi tür dosyasında da geçtiğini gösterir; onu okuduysan burada atla.


## Dizin

| Kimlik | Madde | Önem | Zaman | Profil | Ayrıca |
|---|---|---|---|---|---|
| Y-01 | Anahtar kelime alanını tam kullan | 🟠 | 🚀 | MAĞAZA | — |
| Y-02 | Virgülden sonra boşluk yok | 🟡 | 🚀 | MAĞAZA | — |
| Y-03 | Aynı kelime birden fazla yerde değil | 🟠 | 🚀 | MAĞAZA | — |
| Y-04 | Başlık sadece marka değil | 🟠 | 🚀 | MAĞAZA | — |
| Y-05 | Alt başlık dolu | 🟠 | 🚀 | MAĞAZA | — |
| Y-06 | Tekil ve çoğul birlikte yazılmamış | 🟡 | 🚀 | MAĞAZA | — |
| Y-07 | Kategori adı anahtar kelimelerde değil | 🟡 | 🚀 | MAĞAZA | — |
| Y-08 | Rakip marka adları kullanılmıyor | 🟠 | 🚀 | MAĞAZA | — |
| Y-09 | Birden fazla mağaza lokalizasyonu | 🟡 | 🚀 | MAĞAZA | — |
| Y-10 | Çeviri değil, yerel anahtar kelime araştırması | 🟡 | 🚀 | MAĞAZA | — |
| Y-11 | Anahtar kelime araştırması yapılmış | 🟠 | 🚀 | MAĞAZA | — |
| Y-12 | İkon küçük boyutta okunuyor | 🟠 | 🚀 | MAĞAZA | — |
| Y-13 | En güçlü görsel ilk sırada | 🟠 | 🚀 | MAĞAZA | — |
| Y-14 | Ekran görüntülerinde başlık metni | 🟠 | 🚀 | MAĞAZA | — |
| Y-15 | App Preview videosu | 🟡 | 🚀 | MAĞAZA | — |
| Y-16 | Açıklamanın ilk satırları güçlü | 🟡 | 🚀 | MAĞAZA | — |
| Y-17 | Uygulama içinden değerlendirme isteme | 🟠 | 🚀 | MAĞAZA | — |
| Y-18 | Yorumlara cevap | 🟡 | 📈 | MAĞAZA | — |
| Y-19 | Ürün sayfası güncel | 🟡 | 📈 | MAĞAZA | — |
| Y-20 | Trafik kaynağı ve anahtar kelime performansı takibi | 🟡 | 📈 | MAĞAZA | — |
| Y-21 | Ürün sayfası testleri ve özel sayfalar | 🟢 | 📈 | MAĞAZA | — |
| Z-01 | Tek ana problem ve tek persona | 🟠 | 🏁 | MAĞAZA | — |
| Z-02 | İlk ekran görüntüsü ve mesaj | 🟠 | 🚀 | MAĞAZA | — |
| Z-03 | Değerlendirme ve sosyal kanıt | 🟡 | 🚀 | MAĞAZA | — |
| Z-04 | Ölçüm altyapısı (attribution) | 🟡 | 📈 | MAĞAZA GELİR | — |
| Z-05 | Rakip analizi | 🟡 | 🏁 | MAĞAZA | — |
| Z-06 | Düzenli güncelleme ritmi | 🟡 | 📈 | MAĞAZA | — |
| Z-07 | Dil ve pazar genişlemesi | 🟡 | 📈 | MAĞAZA | — |
| Z-08 | Paywall ve fiyat deneyleri | 🟢 | 📈 | GELİR | — |
| Z-09 | Metrik sözlüğü ve hedefler | 🟡 | 📈 | MAĞAZA GELİR | — |

---

## Maddeler

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
