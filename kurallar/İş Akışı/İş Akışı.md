---
tür: ana-kural
sürüm: 1.0
güncellendi: 2026-11-10
---

# İş Akışı: Seçim Notu

Her projede aynı hat işlemez. Bu kategori, işin **proje türüne** ve **güvenlik sınıfına** göre hangi hatla yürüyeceğini tanımlar. Kim hangi modelle çalışır sorusunun cevabı burada değil, [[Kurallar/Ajan İş Akışı|Ajan İş Akışı]] notundadır; bu notlar onun üstüne "bu projede hat nasıl" bilgisini koyar.

**Klasör:** `~/Desktop/hafıza/hafıza/Kurallar/İş Akışı/`

| Not | İçerik |
|---|---|
| [[Kurallar/İş Akışı/Güvenlik Hattı\|Güvenlik Hattı]] | Güvenlik sınıfları (GS0-GS3), tetikleyiciler, zorunlu kapılar, ajan çalışma güvenliği. Her türde geçerli. |
| [[Kurallar/İş Akışı/Web ve Sunucu\|Web ve Sunucu]] | `WEB-API`, `WEB-S`, `BULUT` arka ucu (Supabase, Firebase, VPS) |
| [[Kurallar/İş Akışı/Apple Uygulaması\|Apple Uygulaması]] | iOS ve macOS (`YEREL`, `BULUT`, `MAĞAZA`, `GELİR`) |
| [[Kurallar/İş Akışı/Oyun\|Oyun]] | Unity (`OYUN`), tek ve çok oyunculu |
| [[Kurallar/İş Akışı/Araç ve MCP\|Araç ve MCP]] | CLI, MCP sunucusu, betik, kanca (`ARAÇ`) |
| [[Kurallar/İş Akışı/Araştırma ve Belge\|Araştırma ve Belge]] | Web ve repo araştırması, rapor, plan, başvuru metni |

## 1. Ne zaman okunur

1. **Projede ilk plan, faz ya da ajan işinden önce:** bu not + projenin tür notu. Oturumda bir kez.
2. **İş bir güvenlik tetikleyicisine dokunuyorsa** (Güvenlik Hattı, Bölüm 2): Güvenlik Hattı. GS2 ve GS3 projelerde her oturumda bir kez.
3. Alt ajanlar bu notları okumaz. Gereken kural, iş tanımının "Kısıtlar" ve "Güvenlik" maddelerine taşınır.

## 2. Seçim

1. **Tür:** `Plan.md` başındaki profil bloğundan. Profil yoksa önce Üretim Kontrolü Bölüm 0'a göre belirlenir.
2. **Güvenlik sınıfı:** Güvenlik Hattı Bölüm 1'e göre projenin taban sınıfı.
3. `Plan.md` profil bloğuna tek satır yazılır:
   `> **İş akışı:** Web ve Sunucu · Güvenlik sınıfı GS3`
4. Birden çok türe giren proje (örn. çok oyunculu oyun + sunucu, iOS uygulaması + Firebase) iki notu da kullanır; çelişkide **sıkı olan** geçerlidir.
5. Proje büyüdükçe sınıf yükselir (örn. localStorage'dan sunucuya geçiş). Sınıf yalnız Ozan'ın açık onayıyla düşer.

## 3. İş tipine göre hat

Tür notu fazın genel hattını verir. Tek bir işin hattı tipine göre kısalır ya da uzar.

| İş tipi | Hat |
|---|---|
| **Özellik** | Tarif ve kabul ölçütü → (güvenlik tetikleyicisi varsa tehdit notu) → uygulama → doğrulama → bağımsız test ve denetim (sınıfa göre) → kayıt |
| **Hata düzeltme** | Teşhis (Opus) → hatayı yakalayan test → düzeltme → doğrulama. Güvenlik koduna dokunuyorsa özellik gibi denetlenir. |
| **Denetim bulgusu** | Bulguyu yeniden üret → düzelt → aynı kanıtla kapandığını göster → ikinci tur (sınıfa göre) |
| **Yeniden düzenleme** | Önce mevcut davranışı kilitleyen test → değişiklik → aynı testler yeşil. Davranış değişiyorsa özelliktir. |
| **Araştırma** | Araştırma ve Belge notu |
| **Acil canlı sorun** | Önce durdur (geri al, özelliği kapat) → Ozan'a haber → kök neden → kalıcı düzeltme normal hatla. Acil olması denetimi kaldırmaz; sonraya alır ve kaydeder. |
| **Cila, metin, ince ayar** | Opus tek başına, Ozan'la hızlı tur. Ajan açılmaz. |

## 4. Projelerin ataması

2026-11-10'da her projenin `Plan.md` dosyasına yazıldı; kesin kaynak o satırdır, bu tablo özetidir. Tür ve sınıf Opus'un atamasıdır; Ozan değiştirebilir. Oturum kancası (`hafiza.py`) satırı okuyup oturum başında hangi notların okunacağını söyler; `mcp__hafiza__is_akisi` aynı notları tek çağrıda getirir.

| Proje | İş akışı | Sınıf |
|---|---|---|
| Kampüs Karnesi, BANÜ Genç Oyunlar | Web ve Sunucu | GS3 |
| POS | Web ve Sunucu (+ Android istemci) | GS3 |
| Bizim Site, Köprü DGS | Web ve Sunucu | GS2 |
| Mesai Paneli | Web ve Sunucu | GS1 (sunucuya geçince GS3) |
| CineHub | Web ve Sunucu | GS1 |
| dg9, dg9-v2 | Apple Uygulaması + Web ve Sunucu (Firebase) | GS2 |
| Tarif | Apple Uygulaması | GS1 (paywall işleri GS2 kapılarıyla) |
| Döngü | Apple Uygulaması | GS1 (sağlık verisi) |
| Kıble | Apple Uygulaması | GS1 (konum) |
| Sistem Monitörü, Claude Notch, Ada, AULA Mac, M8 Panel, Drone 3D Galeri, Metro | Apple Uygulaması | GS1 |
| NetLab | Apple Uygulaması | GS0 |
| Ajan Merkezi, Kalkış | Apple Uygulaması + Araç ve MCP | GS1 |
| Korku Oyunu | Oyun | GS2 (çok oyunculu) |
| Gemini MCP, Hafıza MCP, xcode-mcp, OpenRocket MCP | Araç ve MCP | GS1 |
| Status Line | Araç ve MCP | GS0 |
| Lab Ekibi Yarışma ve Projeler | Araştırma ve Belge | GS0 |

## 5. Bakım

- Bir projede öğrenilen ve başka projeye de yarayacak ders, tür notunun "Tuzaklar" bölümüne tarihli ve proje adıyla eklenir. Yalnız o projeyi ilgilendiren kural projenin `.claude/rules/uretim.md` dosyasında kalır.
- Yeni proje türü çıkarsa (örn. gömülü yazılım, veri hattı) aynı başlıklarla yeni not açılır ve yukarıdaki tabloya eklenir.
- Proje kuralı bu notlardan daha sıkı olabilir, daha gevşek olamaz.
- Önemli değişiklikte `sürüm` ve `güncellendi` alanları artırılır.

## 6. Gerekçe

- **2026-11-10 (Ozan):** "iş akışını yapılan projeye göre değiştirmeyi istiyorum, kategori olarak iş akışı yapalım, özellikle güvenlik kısmı sıkı olmalı". Yapı, sınıflar ve sıkılık düzeyi için kararı Opus'a bıraktı ("kararları sana bırakıyorum"). Bu kategorideki sınıf tanımları, eşikler ve proje atamaları Opus'un önerisidir; Ozan değiştirebilir.
