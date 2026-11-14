---
tür: üretilmiş-parça
kaynak: Kurallar/Üretim Kontrolü.md
kaynak-sürüm: 1.3
kaynak-özet: b6bdd028b3e2
---

# Üretim Kontrolü: Ek - Yapay Zekâ

> **Elle düzenlenmez.** Bu dosya `Kurallar/Üretim Kontrolü.md` kaynağından `~/.claude/hooks/uretim_bol.py` ile üretilir; değişiklik kaynağa yapılır, parçalar oturum başında kendiliğinden yenilenir.
>
> **Kimler okur:** LLM ya da yapay zekâ özelliği olan projeler (`YZ`).
> **Nasıl okunur:** tamamını değil. Önce dizine bak; fazın kontrol kapısındaki kimliklerin metnini aşağıda bul. Profil, önem, aşama ve fazlara yayma kuralları [[Kurallar/Üretim Kontrolü/Yöntem|Yöntem]] notunda.


14 madde. "Ayrıca" sütunu maddenin hangi tür dosyasında da geçtiğini gösterir; onu okuduysan burada atla.


## Dizin

| Kimlik | Madde | Önem | Zaman | Profil | Ayrıca |
|---|---|---|---|---|---|
| B-01 | Ortam değişkenleri ve yapılandırma ayrımı | 🔴 | 🏁 | BULUT WEB-S WEB-API OYUN ARAÇ YZ | Web, Apple, Android, Oyun, Araç |
| B-02 | İstemciye giden sırlar | 🔴 | 🏁 | BULUT WEB-S YZ | Web, Apple, Android |
| F-06 | Rate limiting | 🟠 | 🚀 | BULUT WEB-API YZ | Web, Apple, Android |
| F-10 | SSRF ve dış URL çekme | 🟡 | 🚀 | WEB-API YZ | Web |
| G-01 | Gizlilik politikası | 🔴 | 🚀 | BULUT WEB-API OYUN YZ (mağazaya çıkan her uygulama) | Web, Apple, Android, Oyun |
| M-03 | Kill switch | 🟡 | 🚀 | BULUT WEB-API OYUN YZ | Web, Apple, Android, Oyun |
| R-01 | Maliyet ve bütçe alarmı | 🔴 | 🚀 | BULUT WEB-API YZ | Web, Apple, Android |
| R-08 | SaaS harcama takibi ve otomasyonu | 🟠 | 🚀 | BULUT WEB-API YZ GELİR | Web, Apple, Android |
| S-01 | Anahtar istemcide değil | 🔴 | 🏁 | YZ | — |
| S-02 | Maliyet ve kota sınırı | 🔴 | 🚀 | YZ | — |
| S-03 | Prompt injection ve çıktı güvenliği | 🟠 | 🚀 | YZ | — |
| S-04 | Hata, zaman aşımı ve yedek davranış | 🟡 | 🚀 | YZ | — |
| S-05 | Veri gizliliği | 🟠 | 🚀 | YZ | — |
| X-07 | Brute force ve rate limit testi | 🟠 | 🚀 | BULUT WEB-API YZ | Web, Apple, Android |

---

## Maddeler

### B. Ortam ve yapılandırma

#### B-01 · Ortam değişkenleri ve yapılandırma ayrımı · 🔴 · 🏁 · BULUT WEB-S WEB-API OYUN ARAÇ YZ
- **Ne/Neden:** Ayar ve sırlar koddan ayrı olmalı; dev/staging/prod farklı değerlerle çalışabilmeli.
- **Kontrol:** `.env.example` var mı; kodda sabit URL/anahtar (`grep -rnE 'https?://[^"]*(api|prod)|sk_live|AIza|apiKey\s*[:=]'`); Xcode'da `.xcconfig` veya build configuration kullanımı; Vite'ta sadece `VITE_` önekli değişkenlerin istemciye gittiğinin farkında olunması.
- **Geçer:** Tüm ayarlar tek yerden okunuyor; `.env.example` güncel; prod sırrı istemci paketine girmiyor.

#### B-02 · İstemciye giden sırlar · 🔴 · 🏁 · BULUT WEB-S YZ
- **Ne/Neden:** Mobil uygulamaya veya web paketine konan her şey **herkese açıktır**. Ücretli API anahtarları (OpenAI, Anthropic, TMDB yazma anahtarı, Stripe secret) istemcide olmamalı.
- **Kontrol:** `dist/` veya build çıktısında anahtar araması; Swift kaynaklarında string anahtar; `Info.plist` içinde gizli değer.
- **Geçer:** İstemcide sadece herkese açık olması tasarlanmış anahtarlar var (Firebase web config, TMDB okuma anahtarı gibi) ve bunlar kurallar/kota ile korunuyor; ücretli anahtarlar bir sunucu veya proxy arkasında.

### F. API ve uygulama güvenliği

#### F-06 · Rate limiting · 🟠 · 🚀 · BULUT WEB-API YZ
- **Ne/Neden:** Giriş, kayıt, şifre sıfırlama, e-posta/SMS gönderen ve ücretli API çağıran uçlar kötüye kullanılabilir (fatura patlaması).
- **Kontrol:** Middleware (Upstash ratelimit, express-rate-limit), Vercel Firewall kuralları, Firebase App Check, Cloud Functions için kota. Genel (hesaptan bağımsız) giriş kilidi varsa: IP değiştiren biri herkesi kilitleyebilir mi, kilidi açan yönetim işlemi ve kilitlenince bildirim var mı (Bizim Site F10).
- **Geçer:** Hassas ve pahalı uçlar IP/kullanıcı başına sınırlı.

#### F-10 · SSRF ve dış URL çekme · 🟡 · 🚀 · WEB-API YZ
- **Kontrol:** Kullanıcının verdiği URL'yi sunucu çekiyorsa iç ağ adresleri (`169.254.*`, `localhost`, `10.*`) engelli mi.
- **Geçer:** Dış istekler izin listesiyle sınırlı.

### G. Gizlilik ve yasal uyum

#### G-01 · Gizlilik politikası · 🔴 · 🚀 · BULUT WEB-API OYUN YZ (mağazaya çıkan her uygulama)
- **Ne/Neden:** App Store ve Google Play zorunlu kılar; KVKK aydınlatma metni gerekir.
- **Kontrol:** Erişilebilir URL; uygulama içinden bağlantı; toplanan verilerle tutarlılık.
- **Geçer:** Güncel politika var ve gerçek davranışla örtüşüyor.

### M. Dayanıklılık ve felaket kurtarma

#### M-03 · Kill switch · 🟡 · 🚀 · BULUT WEB-API OYUN YZ
- **Ne/Neden:** Sorunlu veya pahalı bir özelliği deploy etmeden anında kapatmak (B-04 ile ilişkili).
- **Geçer:** Riskli özellikler uzaktan kapatılabiliyor.

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

### X. Saldırgan gibi test (kendi uygulamanda güvenlik testi)

> Profil: `BULUT`, `WEB-API` (ve sunucusu olan `OYUN`). **Yalnızca yetkili olduğun kendi uygulamanda**, tercihen staging ortamında (B-03) ve test hesaplarıyla yapılır. Üretim verisine zarar verecek, başkasının hesabına dokunacak veya hizmeti düşürecek test yapılmaz. Ajan her testi önce kullanıcıya listeler, onay alır, sonuçları `Kontrol.md`'ye yazar. Bulunan açıklar 🔴 olarak ilgili maddeye bağlanır. Araçlar: tarayıcı DevTools, `curl`, Burp Suite Community / OWASP ZAP (yerel proxy), Firebase Rules Playground / emülatör.

#### X-07 · Brute force ve rate limit testi · 🟠 · 🚀 · BULUT WEB-API YZ
- **Nasıl:** Staging'de giriş, şifre sıfırlama, davet kodu doğrulama, e-posta/SMS gönderen ve LLM çağıran uçlara kısa sürede çok istek (makul sayıda; hizmet dışı bırakma amaçlı değil).
- **Geçer:** Sınır devreye giriyor (429), hesap/IP bazlı yavaşlatma var, olay loglanıyor (F-06, L-10).
