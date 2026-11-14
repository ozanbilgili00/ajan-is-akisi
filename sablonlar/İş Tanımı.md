# İş tanımı şablonu

> Her ajan çağrısının ve her Gemini işinin istemi bu başlıkları taşır. Ajan önceki konuşmayı görmez. Kaynak: [[Kurallar/Ajan İş Akışı|Ajan İş Akışı]] Bölüm 7, [[Kurallar/İş Akışı/Güvenlik Hattı|Güvenlik Hattı]] Bölüm 7.

**Amaç:** ne yapılacak ve neden, 2-3 cümle.

**Önce oku:** proje kökü · `CLAUDE.md` · `.claude/rules/uretim.md` · ilgili kaynak dosyalar ve notlar (yol olarak).

**Kapsam:** dokunulacak dosya ve klasörler · dokunulmayacaklar.

**Kabul ölçütleri:**
1. 
2. 

**Doğrulama:** komutlar `&&` ile zincirli ve beklenen sonuç.

**Çalışma yeri:** klasör ya da worktree · dal adı · commit izni (var / yok).

**Rapor dosyası:** tam yol.

**Kısıtlar:** Push YAPMA. Birleştirme YAPMA. PR açma. Pencere öne getirme yok, yalnız kendi başlattığın süreci sonlandır. (projeye özel: ortak kaynak, katalog biçimi, veritabanını sıfırlıyorsa belirt)

**Güvenlik** (tetikleyiciye dokunan ya da GS2-GS3 projedeki işte):
- Sınıf: GS…
- Tehdit notu: (metin ya da yol)
- Dokunulmayacak güvenlik dosyaları: 
- Ortam: yerel / emülatör / staging adı
- Sır okuma ve yazdırma yok · canlıya erişim yok · yeni bağımlılık yok (gerekiyorsa raporda öner) · güvenlik kontrolü işi engelliyorsa kapatma, dur ve raporla.

---
`test-yazari` için uygulama kodu yerine tarif, kabul ölçütleri ve arayüz imzaları verilir.
`guvenlik-denetcisi` için diff ya da dal, tehdit notu ve ilgili Üretim Kontrolü maddeleri verilir; uygulayıcının raporu verilmez.
