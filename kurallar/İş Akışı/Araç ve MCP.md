---
tür: iş-akışı
sürüm: 1.1
güncellendi: 2026-11-15
---

# İş Akışı: Araç ve MCP

**Kapsam:** CLI, MCP sunucusu, betik, kanca, eklenti (`ARAÇ`). **Tipik sınıf:** GS1. Yalnız okuyan ve ekrana yazan araç GS0.
Önce: [[Kurallar/İş Akışı/İş Akışı|Seçim Notu]] · [[Kurallar/İş Akışı/Güvenlik Hattı|Güvenlik Hattı]] · [[Kurallar/Ajan İş Akışı|Ajan İş Akışı]]

Bu araçlar küçük görünür ama çoğu **Ozan'ın makinesinde, onun yetkisiyle komut çalıştırır ve dosya yazar**; girdileri de bir modelden gelir. Bu yüzden hat kısa, güvenlik kısmı sıkıdır.

## 1. Hat

1. **Tarif:** Opus her aracın sözleşmesini yazar: girdi şeması, çıktı biçimi, yan etkisi (okur, yazar, süreç başlatır, ağa çıkar), hata durumları.
2. **Uygulama:** çoğu iş küçüktür, Opus kendisi yazar. Çok araçlı ya da çok dosyalı paket `uygulayici`; şeması net tekil araç `uygulayici-haiku`.
3. **Doğrulama:** tip denetimi → birim testleri → duman testi (sunucuyu başlat, her aracı bir geçerli ve bir hatalı girdiyle çağır).
4. **Gerçek kullanım denemesi:** araç gerçek bir projede, geçici klasörde ya da kopya üzerinde denenir; ilk deneme canlı vault ya da gerçek proje üzerinde yapılmaz.
5. **Güvenlik:** yazan, silen, süreç başlatan ya da ağa çıkan her araç tetikleyicidir → Opus satır satır okur, denetçi tek tur.
6. **Kurulum:** `settings.json`, kanca ve izin listesi değişikliği Ozan'a gösterilerek yapılır; önce yedek alınır.

## 2. Bu türe özgü güvenlik noktaları

- **Girdi modelden gelir, güvenilmezdir.** Her araç girdisi şemayla doğrulanır (tür, uzunluk, izinli değerler).
- **Yol sınırı:** dosya işlemi izinli kök klasörlerle sınırlıdır; yol çözümlenip (`..`, sembolik bağ) kökün içinde kaldığı denetlenir.
- **Alt süreç:** komut ve argümanlar dizi olarak verilir; kabuk dizgisi kurulmaz, `shell: true` kullanılmaz. Çalıştırılabilecek komutlar izin listesindedir. Zaman aşımı ve çıktı boyutu sınırı vardır.
- **Yıkıcı işlem** (silme, üstüne yazma, süreç sonlandırma, geri alınamayan değişiklik) ayrı araçtır, adı ve açıklaması bunu söyler; mümkünse geri alma kaydı tutar. Başka uygulamanın sürecini kapatmak her zaman onaylıdır.
- **Sırlar:** araç çıktısına, loga ve hata mesajına sır yazılmaz; ortam değişkenleri toptan dökülmez. Anahtar gereken araç onu ortamdan okur, parametre olarak almaz.
- **Çıktı da girdidir:** aracın döndürdüğü dış içerik (web sayfası, dosya, başka modelin cevabı) çağıran modele talimat gibi görünebilir; çıktı veri olarak etiketlenir, araç açıklamaları dış içerikten üretilmez.
- **Ağ:** yalnız gereken adresler; kullanıcı girdisiyle adres kuruluyorsa iç ağ ve `file://` engellenir.
- **İzin listesi:** bir sunucuyu `mcp__<sunucu>` olarak toptan izinli yapmak, o sunucunun yazan araçlarını da onaysız kılar; yazan araçları olan sunucu için bu Ozan'ın bilinçli kararıdır.
- **Kanca:** her oturumda ve alt oturumda çalışır; hızlı olmalı, hata verince oturumu kilitlememeli, girdisini (araç adı, yol, komut) güvenilmez saymalı.

## 3. Ortak kaynaklar

- Çalışan MCP sunucusu ve kanca canlıdır: üzerinde çalışılan araç o anda başka oturumlarca kullanılıyor olabilir. Derleme çıktısını değiştiren iş Ozan'a haber verilerek yapılır.
- `~/.claude/` ayarları tüm projeleri etkiler; yalnız yönetici, yedek alarak dokunur.
- Harici kotalar (Gemini, API anahtarları) deneme çağrılarıyla tüketilmez.

## 4. Bitti tanımı (genel tanıma ek)

- Tip ve testler yeşil; duman testi her aracı kapsıyor.
- Her araç için hatalı girdi, kök dışı yol ve zaman aşımı denendi.
- Araç hata verdiğinde çağıranı çökertmiyor, anlaşılır mesaj dönüyor.
- README ya da ana notta: kurulum, araç listesi, yan etkiler, ortam değişkenleri (değerleri değil).

## 5. Tuzaklar

- MCP araçları otomatik kip sınıflandırıcısına takılır; sunucu izin listesine eklenmeden ajan işi yarıda kalır. (MCP izin notu)
- Gemini kotası birkaç işte dolar; inceleme işi `high` eforla kotayı bitirir ve bulguların bir kısmı yanlıştır. Hidrojen öncesi ölçüm; Hidrojen ve Neon'la 10 işte (~670 bin token) kota engeli çıkmadı, üst sınır bilinmiyor. (Gemini MCP)
- Kural ya da faz eşleştiren araç, not biçimine duyarlıdır: `**Kontrol kapısı:**` satırı faz başlığının hemen altında olmalı. (Hafıza MCP)
- Canlı boruda satır okuma bazı API'lerle teslim edilmez; süreç süren araçta akış okuma ayrıca test edilir. (Ajan Merkezi)
- Betikte sabit geçici klasör yolu bırakma; oturuma özel klasör parametreyle verilir. (Ajan Merkezi)

## 6. Güvenlik skilleri

Kural ve onay için [[Kurallar/İş Akışı/Güvenlik Hattı|Güvenlik Hattı]] Bölüm 8a. Skill dosyası denetçinin ya da test ajanının iş tanımına yol olarak verilir.

- [[Kaynaklar/Güvenlik Skilleri/5 Yapay zekâ/ai-security|ai-security]] · araç çıktısındaki dolaylı istem enjeksiyonu ve araç açıklamasında.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/rce|rce]] · alt süreç ve komut enjeksiyonunda.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/toctou|toctou]] · yol denetimi ile kullanım arasındaki sembolik bağda.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/ssrf|ssrf]] · URL çeken araçta.
- [[Kaynaklar/Güvenlik Skilleri/8 Fuzzing/fuzzing|fuzzing]] · girdi ayrıştırıcılarında.
- [[Kaynaklar/Güvenlik Skilleri/8 Fuzzing/fuzzing-course|fuzzing-course]] · girdi ayrıştırıcılarında, ders kaynağı olarak.
- [[Kaynaklar/Güvenlik Skilleri/4 Tedarik zinciri ve CI/supply-chain|supply-chain]] · npm ve pip bağımlılıklarında.
- [[Kaynaklar/Güvenlik Skilleri/4 Tedarik zinciri ve CI/dependency-confusion|dependency-confusion]] · npm ve pip bağımlılıklarında.
- [[Kaynaklar/Güvenlik Skilleri/4 Tedarik zinciri ve CI/cicd-pipeline|cicd-pipeline]] · CI varsa.
- [[Kaynaklar/Güvenlik Skilleri/4 Tedarik zinciri ve CI/cicd-secrets|cicd-secrets]] · CI varsa.
- [[Kaynaklar/Güvenlik Skilleri/6 Genel liste ve rapor/reporting|reporting]] · bulgu yazımında.
