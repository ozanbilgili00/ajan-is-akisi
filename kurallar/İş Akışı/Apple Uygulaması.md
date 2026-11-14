---
tür: iş-akışı
sürüm: 1.0
güncellendi: 2026-11-10
---

# İş Akışı: Apple Uygulaması

**Kapsam:** iOS ve macOS uygulamaları (`YEREL`, `BULUT`, `MAĞAZA`, `GELİR`). **Tipik sınıf:** GS1; Firebase ya da Supabase kullanan uygulama GS2 ve arka ucu için [[Kurallar/İş Akışı/Web ve Sunucu|Web ve Sunucu]] notu da geçerli.
Önce: [[Kurallar/İş Akışı/İş Akışı|Seçim Notu]] · [[Kurallar/İş Akışı/Güvenlik Hattı|Güvenlik Hattı]] · [[Kurallar/Ajan İş Akışı|Ajan İş Akışı]]

## 1. Hat (faz ya da özellik başına)

1. **Tarif:** Opus ekranı, durumları (boş, yükleniyor, hata, çevrimdışı) ve kabul ölçütlerini yazar.
2. **Mantık önce:** veri modeli, hesaplama ve servis katmanı arayüzden ayrı yazılır ve birim testiyle gelir. Veri modeli değişiyorsa migration planı aynı işte.
3. **Uygulama:** çok dosyalı ya da tasarım kararı isteyen paket `uygulayici`; mevcut kalıbın benzeri ekran, yerelleştirme, erişilebilirlik `uygulayici-haiku`. Arayüz cilasını Opus, Ozan'la hızlı turda yapar.
4. **Doğrulama** (`mekanik`, `mcp__xcode__*` ile): derleme → testler → simülatörde ekran görüntüsü (açık ve karanlık, büyük yazı). Uyarı sayısı raporlanır.
5. **Ekranlar:** Ozan'a gösterilecek görüntüler `~/Desktop/<Proje> Ekranları/` altına kopyalanır.
6. **Güvenlik:** tetikleyici varsa Güvenlik Hattı Bölüm 3. Bu türde sık görülenler aşağıda.
7. **Yayın yolu** (`MAĞAZA`): Sertleştirme → Yayın hazırlığı (Üretim Kontrolü T ve W) → Mağaza. Arşivleme, TestFlight ve gönderim Ozan'ın onayıyla.

## 2. Bu türe özgü güvenlik noktaları

- **Saklama:** belirteç ve sır Anahtar Zinciri'nde; `UserDefaults` ve düz dosyada değil. Sağlık ve konum verisi cihazda kalır, loglanmaz, yedeğe ve analitiğe girmez.
- **İzinler:** her izin bağlam içinde istenir, `Info.plist` gerekçesi ve `PrivacyInfo.xcprivacy` günceldir. Kullanılmayan yetki (entitlement) kaldırılır.
- **Dış girdi:** derin bağlantı, URL şeması, paylaşım uzantısı, pano, kanca ve soket girdisi güvenilmezdir; ayrıştırılıp doğrulanmadan dosya yolu, komut ya da gezinme hedefi olmaz.
- **Alt süreç** (macOS): komut dizi olarak verilir, kabuk dizgisi kurulmaz; yol ve argüman dış girdiden geliyorsa izin listesiyle sınırlanır. Yalnız uygulamanın kendi başlattığı süreç sonlandırılır.
- **Sandbox kapalı ya da ayrıcalıklı yardımcı varsa** iş GS1'den aşağı sayılmaz ve denetçi tek tur zorunludur.
- **Satın alma:** hak sahipliği sunucu ya da StoreKit doğrulamasıyla belirlenir; istemcideki bayrağa güvenilmez. Paywall işi GS2 gibi yürür.
- **Ağ:** yalnız HTTPS; ATS istisnası eklenmez. Üçüncü taraf SDK eklemek yeni bağımlılık kuralına tabidir.

## 3. Ortak kaynaklar

- Tek derleme, tek simülatör, tek `DerivedData`. Paralel ajanlar derleme için sıraya girer.
- **Odak çalma yok:** pencere öne getirme, `open_in_xcode`, açık uygulamayı kapatma yalnız Ozan isterse. Ajan yalnız kendi başlattığı süreci sonlandırır.
- `.xcodeproj` ve dizgi kataloğu (`.xcstrings`) çakışmaya açıktır: aynı anda tek ajan dokunur; kataloğa yalnız sona, Xcode biçiminde eklenir.
- Gerçek cihaz gerektiren iş (kamera, sensör, bildirim) ajana verilmez; Ozan'ın deneme listesine yazılır.

## 4. Bitti tanımı (genel tanıma ek)

- Derleme uyarısız, testler yeşil.
- Ekran görüntüleri açık ve karanlık modda, büyük yazıda kırpılma yok.
- Kullanıcıya görünen metin yerelleştirme dosyasında; Türkçe İ/ı doğru.
- VoiceOver etiketleri var.
- Yeni izin, veri türü ya da SDK varsa gizlilik bildirimi güncel.
- Elle denenmesi gerekenler "Ozan deneyecek" listesinde.

## 5. Tuzaklar

- `@MainActor` dışından arayüz durumuna dokunan kapanış çökme yapar; eşzamanlılık uyarıları hata sayılır. (Kıble)
- Düz `xcodebuild` çıktısı bağlamı doldurur; Xcode MCP kullan. (Ajan İş Akışı Bölüm 12)
- Kart ve fotoğrafa dekoratif döndürme ekleme; büyük boşluk ve küçük yazı bırakma. (Ozan'ın tasarım tercihi)
- Kullanıcının kancaları alt oturumlarda da çalışır; süreç süren uygulamalarda gürültü ve token maliyeti hesaba katılır. (Ajan Merkezi)
