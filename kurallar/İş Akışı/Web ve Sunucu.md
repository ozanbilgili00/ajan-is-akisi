---
tür: iş-akışı
sürüm: 1.1
güncellendi: 2026-11-15
---

# İş Akışı: Web ve Sunucu

**Kapsam:** `WEB-API`, `WEB-S`, `BULUT` arka ucu. Supabase, Firebase, kendi sunucusu (VPS, Docker), Vercel. **Tipik sınıf:** GS2-GS3; yalnız tarayıcıda çalışan `WEB-S` GS1.
Önce: [[Kurallar/İş Akışı/İş Akışı|Seçim Notu]] · [[Kurallar/İş Akışı/Güvenlik Hattı|Güvenlik Hattı]] · [[Kurallar/Ajan İş Akışı|Ajan İş Akışı]]

## 1. Hat (iş paketi başına)

1. **Tarif:** Opus kabul ölçütlerini ve dokunulacak dosyaları yazar. Tetikleyici varsa tehdit notu.
2. **Dal:** her iş paketi ayrı dal ve worktree. Ana çalışma kopyasında ajan çalışmaz.
3. **Şema önce:** veri modeli ya da erişim kuralı değişiyorsa migration ve kural testi uygulamadan önce yazılır, yerel veritabanında denenir.
4. **Uygulama:** sunucu ve güvenlik kodu `uygulayici`; saf arayüz, metin, stil `uygulayici-haiku`; kendi içinde kapalı büyük arayüz paketi Gemini'ye gidebilir.
5. **Doğrulama zinciri** (`mekanik`): tip denetimi → lint → birim testleri → erişim kuralı testleri → derleme. Komutlar `&&` ile bağlanır; biri düşerse zincir durur.
6. **Bağımsız test ve denetim:** Güvenlik Hattı Bölüm 3 tablosuna göre.
7. **PR:** CI yeşil + denetim temiz → birleştirme (Güvenlik Hattı "otomatik birleştirme").
8. **Canlı:** migration, dağıtım, ortam değişkeni Ozan'ın onayıyla, yalnız yönetici eliyle. Sonra salt okunur doğrulama (`curl -I` ile başlıklar, sağlık ucu, hata günlüğü).

## 2. Her pakette geçerli tasarım kuralları

- Yetki sunucuda ve veritabanı kuralında denetlenir; istemcideki kontrol yalnız görünümdür. Varsayılan reddet.
- Her yeni tablo ya da koleksiyon erişim kuralıyla ve kural testiyle birlikte gelir; kuralsız tablo birleşmez.
- Girdi sınırda şemayla doğrulanır (uzunluk, tür, adet sınırı); sorgular parametreli.
- Servis anahtarı ve yönetici yetkisi yalnız sunucuda; istemci paketinde sır aranır (derleme çıktısında tarama).
- Hata yanıtı iç ayrıntı sızdırmaz; logda kişisel veri ve belirteç yok.
- Hız sınırı: giriş, kod gönderme, içerik oluşturma ve pahalı uçlarda.
- Güvenlik başlıkları ve CSP testle sabitlenir; joker kaynak (`*`, `*.supabase.co`) kullanılmaz, proje adresi yazılır.
- Kullanıcı içeriği başka kullanıcıya ve yönetim paneline gösterilirken kaçışlanır.

## 3. Ortak kaynaklar

- **Yerel veritabanı tektir.** Sıfırlayan komut (`db:reset` gibi) koşan ajan başka ajanla aynı anda çalışmaz; iş tanımında "veritabanını sıfırlar" diye belirtilir ve işi bitince deneme verisini geri yükler.
- Yerel sunucu portları ve tarayıcı otomasyonu sırayla kullanılır.
- Canlı proje kimlikleri iş tanımına yazılmaz; ajan yalnız yerel adresleri bilir.

## 4. Bitti tanımı (genel tanıma ek)

- Tip, lint, test ve kural testleri yeşil; derleme uyarısız.
- Yeni uç ya da tablo için: yetkisiz kullanıcı, başka kullanıcının kaydı ve hatalı girdi testleri var.
- Derleme çıktısında ve depoda sır taraması temiz.
- Bağımlılık taraması temiz ya da bulgular kayıtlı.
- Canlıya çıktıysa: "canlıda doğrulanacak" listesi işlendi.

## 5. Tuzaklar

- İş tanımında tek başına "Birleştirme." yazma; "Birleştirme YAPMA" yaz. (Kampüs Karnesi)
- Doğrulama zincirinde `;` kullanılırsa lint düşse bile commit'e geçilir; `&&` kullan. (POS)
- Ana çalışma kopyasında ESLint, ajan worktree'lerinin durduğu `.claude/` klasörünü yok saymalı. (POS)
- Paylaşılan yerel veritabanını sıfırlayan test, deneme ortamının verisini siler; test sonrası başlatma betiği çalıştırılır. (Kampüs Karnesi)
- CSP testinin yalnız tam `*` değerine bakması joker alt alan adını kaçırır. (Bizim Site F10)
- Satır ve adet sınırı yalnız `insert` tetikleyicisinde olursa `update` ile aşılır. (Bizim Site F10)
- Genel giriş kilidi, IP değiştiren biri tarafından herkesi kilitlemek için kullanılabilir; kilidi açan yönetim işlemi ve bildirim gerekir. (Bizim Site F10)
- Ajanın verdiği mevzuat ve tarih bilgisi kaynağından doğrulanır. (POS, KVKK uyum tarihi yanlış gelmişti)

## 6. Güvenlik skilleri

Kural ve onay için [[Kurallar/İş Akışı/Güvenlik Hattı|Güvenlik Hattı]] Bölüm 8a. Skill dosyası denetçinin ya da test ajanının iş tanımına yol olarak verilir.

- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/api-security|api-security]] · yeni API ucu ya da yetki kuralı eklenince.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/api-abuse|api-abuse]] · hız sınırı ve kötüye kullanım denetiminde.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/business-logic|business-logic]] · adım atlama, tekrar, fiyat ve miktar akışında.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/idor|idor]] · kimlik alıp sahiplik denetimi yapan her uçta.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/parameter-pollution|parameter-pollution]] · aynı parametrenin birden çok kez gönderilebildiği uçta.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/xss|xss]] · kullanıcı içeriğini gösteren her yerde.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/sqli|sqli]] · sorgu kuran her yerde.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/ssti|ssti]] · şablon motoru kullanılan her yerde.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/rce|rce]] · dış girdiyle komut ya da kod çalıştıran her yerde.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/ssrf|ssrf]] · sunucunun dış adres çağırdığı her yerde.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/file-upload|file-upload]] · dosya ve fotoğraf yükleme akışında.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/oauth|oauth]] · giriş ve geri dönüş adreslerinde.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/open-redirect|open-redirect]] · giriş ve geri dönüş adreslerinde.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/jwt|jwt]] · belirteç üretme ve doğrulama işinde.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/race-condition|race-condition]] · sayaç, oy, stok ve tek kullanımlık hakta.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/toctou|toctou]] · sayaç, oy, stok ve tek kullanımlık hakta.
- [[Kaynaklar/Güvenlik Skilleri/3 Kripto ve TLS/crypto-attacks|crypto-attacks]] · şifreleme, imza ve rastgelelik işinde.
- [[Kaynaklar/Güvenlik Skilleri/3 Kripto ve TLS/tls-attacks|tls-attacks]] · HTTPS bağlantısı ve sertifika ayarında.
- [[Kaynaklar/Güvenlik Skilleri/4 Tedarik zinciri ve CI/supply-chain|supply-chain]] · yeni bağımlılık eklenince.
- [[Kaynaklar/Güvenlik Skilleri/4 Tedarik zinciri ve CI/dependency-confusion|dependency-confusion]] · yeni bağımlılık eklenince.
- [[Kaynaklar/Güvenlik Skilleri/4 Tedarik zinciri ve CI/cicd-pipeline|cicd-pipeline]] · CI dosyası değişince.
- [[Kaynaklar/Güvenlik Skilleri/4 Tedarik zinciri ve CI/cicd-secrets|cicd-secrets]] · CI dosyası değişince.
- [[Kaynaklar/Güvenlik Skilleri/5 Yapay zekâ/ai-security|ai-security]] · YZ özelliği varsa.
- [[Kaynaklar/Güvenlik Skilleri/7 Bulut ve konteyner/cloud|cloud]] · kendi bulut hesabı varsa.
- [[Kaynaklar/Güvenlik Skilleri/7 Bulut ve konteyner/container-escape|container-escape]] · Docker ya da VPS varsa.
- [[Kaynaklar/Güvenlik Skilleri/7 Bulut ve konteyner/k8s-attacks|k8s-attacks]] · Docker ya da VPS varsa.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/graphql|graphql]] · yalnız GraphQL kullanılıyorsa; yoksa ➖.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/request-smuggling|request-smuggling]] · yalnız o teknoloji varsa; yoksa ➖.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/waf-bypass|waf-bypass]] · yalnız WAF kullanılıyorsa; yoksa ➖.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/xxe|xxe]] · yalnız XML işleniyorsa; yoksa ➖.
- [[Kaynaklar/Güvenlik Skilleri/1 Web ve API/deserialization|deserialization]] · yalnız serileştirilmiş veri alınıyorsa; yoksa ➖.
- [[Kaynaklar/Güvenlik Skilleri/6 Genel liste ve rapor/vuln-classes|vuln-classes]] · yayın öncesi tam denetimde.
- [[Kaynaklar/Güvenlik Skilleri/6 Genel liste ve rapor/fast-checking|fast-checking]] · yayın öncesi tam denetimde.
- [[Kaynaklar/Güvenlik Skilleri/6 Genel liste ve rapor/reporting|reporting]] · bulgu kaydı yazılırken.
