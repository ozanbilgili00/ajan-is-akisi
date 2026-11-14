---
tür: iş-akışı
sürüm: 1.0
güncellendi: 2026-11-10
---

# İş Akışı: Oyun

**Kapsam:** Unity projeleri (`OYUN`), tek ve çok oyunculu. **Tipik sınıf:** tek oyunculu ve çevrimdışı GS0-GS1; çok oyunculu, hesaplı ya da satın almalı GS2. Kendi sunucusu varsa [[Kurallar/İş Akışı/Web ve Sunucu|Web ve Sunucu]] notu da geçerli.
Önce: [[Kurallar/İş Akışı/İş Akışı|Seçim Notu]] · [[Kurallar/İş Akışı/Güvenlik Hattı|Güvenlik Hattı]] · [[Kurallar/Ajan İş Akışı|Ajan İş Akışı]]

## 1. Hat (sistem ya da özellik başına)

1. **Tarif:** Opus sistemi, durum makinesini ve kabul ölçütlerini yazar. Çok oyunculu işte **sahiplik** (hangi nesnenin durumuna kim yazar) tarifin parçasıdır.
2. **Mantık sahneden ayrı:** kurallar, hesaplama ve durum makinesi düz C# sınıflarında; düzenleme modu testiyle gelir.
3. **Uygulama:** betik paketi `uygulayici` ya da (kendi içinde kapalıysa) Gemini; mevcut kalıbın benzeri bileşen `uygulayici-haiku`. Sahne, prefab ve editör işi Unity MCP ile, tek ajan.
4. **Derleme denetimi:** her betik değişikliğinden sonra konsol okunur; derleme hatası varken yeni tür ya da bileşen kullanılmaz.
5. **Doğrulama** (`mekanik`): düzenleme ve oynatma modu testleri → konsolda hata ve uyarı sayısı → hedef cihaz için derleme (faz sonunda).
6. **Oynanış:** his, zorluk ve korku temposu ajanla ölçülmez; Ozan dener. Deneme listesi yazılır.
7. **Performans kapısı** (faz sonunda): kare süresi, bellek, çizim çağrısı hedef cihazda ölçülür.

## 2. Bu türe özgü güvenlik noktaları

- **İstemciye güvenme:** skor, envanter, yakalama ve ilerleme kararı yetkili tarafta doğrulanır. Dağıtık yetkide her nesnenin sahibi bellidir; sahip olmayan istemcinin yazması reddedilir.
- **Oturum:** lobi kodu tahmin edilemez uzunlukta; katılma ve yeniden bağlanma hız sınırına tabi; oyuncu adı ve sohbet girdisi uzunluk ve içerik olarak sınırlanır.
- **Ağ mesajı** güvenilmez girdidir: boyut, aralık ve sıklık denetlenir; hatalı mesaj oturumu çökertmez.
- **Sırlar:** servis anahtarı derlemeye ve depoya girmez; istemcide yalnız herkese açık kimlikler.
- **Kayıt dosyası** kullanıcı tarafından değiştirilebilir: bozuk dosya oyunu çökertmez; satın alınan içerik kayıt dosyasındaki bayrağa göre açılmaz.
- **Üçüncü taraf varlık ve eklenti:** lisansı kontrol edilir; editör betiği içeren paket yeni bağımlılık sayılır ve Opus onaylar.

Çok oyunculu, hesaplı ya da satın almalı işler tetikleyicidir: GS2 kapıları (bağımsız test + denetçi) uygulanır.

## 3. Ortak kaynaklar

- **Tek Unity örneği.** Aynı anda tek ajan kullanır; paralellik yalnız Unity'ye dokunmayan işlerde (düz C# mantığı, belge, araştırma).
- Sahne ve prefab dosyaları birleştirilemez: aynı sahneye iki iş aynı anda dokunmaz; iş tanımında sahne adı yazılır.
- Oynatma modundayken betik düzenlenmez; ajan işi bitince oynatma modundan çıkar ve sahneyi kaydeder.
- Büyük varlık üretimi (model, doku) kotalıdır; sormadan toplu üretim yapılmaz.

## 4. Bitti tanımı (genel tanıma ek)

- Konsolda hata yok; yeni uyarı yok.
- Düzenleme ve oynatma modu testleri yeşil.
- Çok oyunculu işte: iki istemcili senaryo, bağlantı kopması ve sahiplik devri denendi.
- Performans kapısı ölçüldü (faz sonunda) ve hedefin içinde.
- Ozan'ın deneme listesi yazıldı.

## 5. Tuzaklar

- Unity API'leri sürümler arasında değişir ve model bilgisi eskiyebilir; emin olunmayan çağrı belgeyle ya da yansımayla doğrulanır.
- Sahne hiyerarşisi ve bileşen sorguları çok büyük çıktı verir; sayfalı ve özet öncelikli çağrı kullanılır.
- Ağ davranışı tek istemciyle "çalışıyor" görünür; sahiplik hataları ancak ikinci istemciyle çıkar. (Korku Oyunu, Faz 3 otomatik devir testleri)
