---
tür: iş-akışı
sürüm: 1.0
güncellendi: 2026-11-10
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
