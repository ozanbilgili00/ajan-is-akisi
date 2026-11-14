---
tür: üretilmiş-parça
kaynak: Kurallar/Üretim Kontrolü.md
kaynak-sürüm: 1.3
kaynak-özet: b6bdd028b3e2
---

# Üretim Kontrolü: Yöntem

> **Elle düzenlenmez.** Bu dosya `Kurallar/Üretim Kontrolü.md` kaynağından `~/.claude/hooks/uretim_bol.py` ile üretilir; değişiklik kaynağa yapılır, parçalar oturum başında kendiliğinden yenilenir.
>
> Kaynağın 0, 1, 2, 7 ve 8. bölümleri: nasıl uygulanır, profiller, önem ve aşama, bakım, fazlara yayma. Bir projede plan kurarken ya da faz kapısı yazarken okunur. "Bu dosya" ve "Bölüm 3" ifadeleri kaynağı, yani parça dosyalarındaki maddeleri kasteder.

## 0. Ajan talimatı: bu dosyayı bir projeye nasıl uygularsın

Bir projede "üretim kontrolü kur", "kontrol kurallarını yaz" veya "projeyi denetle" dendiğinde şu sırayı izle:

1. **Projeyi tanı.** Obsidian notunu (`Projeler/<Ad>/<Ad>.md`, `Plan.md`) oku. Sonra repoyu tara: dil ve çatı, paket dosyaları (`package.json`, `Package.swift`, `*.xcodeproj`, `Packages/manifest.json`), backend var mı, veri nerede tutuluyor, kimlik doğrulama var mı, dağıtım nasıl yapılıyor.
2. **Profil seç.** Bölüm 1'deki profillerden bir veya birkaçını seç. Bir proje birden fazla profile girebilir (örn. çevrimiçi co-op oyun = `OYUN` + `WEB-API`).
3. **Aşamayı belirle.** `Prototip`, `Beta` (TestFlight / kapalı test) veya `Yayında`. Önem seviyeleri aşamaya göre yorumlanır (Bölüm 2).
4. **Her maddeyi değerlendir.** Bölüm 3'teki her madde için:
   - Profil etiketi projeye uymuyorsa → `➖ Uygulanmaz` (tek satır gerekçe yaz).
   - Uyuyorsa → maddenin **Kontrol** satırındaki adımları gerçekten uygula, kanıt topla (`dosya:satır`, komut çıktısı) ve durum ver: `✅ Var` · `⚠️ Kısmi` · `❌ Yok` · `❓ Bilinmiyor`.
   - Emin değilsen tahmin etme, `❓` yaz ve neyin doğrulanması gerektiğini belirt.
5. **Fazlara yay.** Uygulanan maddeleri Bölüm 8'e göre `Plan.md` fazlarına "Kontrol kapısı" olarak dağıt. Faz sırasında ve sonunda bu kapılar kullanılır.
6. **Proje kural dosyasını yaz.** Bölüm 4'teki şablonla projenin köküne `.claude/rules/uretim.md` yaz. Claude Code bu klasördeki kuralları otomatik yükler. Proje köküne yazamıyorsan `CLAUDE.md` içine "Üretim kuralları" bölümü olarak ekle. Bu dosya *kalıcı kurallar* içerir ("şunu her zaman yap / asla yapma"), denetim sonucu içermez.
7. **Denetim raporunu yaz.** Bölüm 5'teki şablonla Obsidian'da `Projeler/<Ad>/Kontrol.md` oluştur veya güncelle. ❌ ve ⚠️ maddelerden 🔴/🟠 olanları `Yapılacaklar.md` dosyasına "Sonra" altına `- [ ] [Üretim <ID>] ...` olarak ekle. `Günlük.md` dosyasına kısa kayıt düş.
8. **Kullanıcıya özet ver.** Kritik bulgular, en çok etki edecek ilk 3-5 iş, `➖` sayısı.

### Ajanın uyması gereken sınırlar
- **Denetim salt-okunurdur.** Bulguyu düzeltmek için kod değiştirme, paket kurma veya yapılandırma değiştirme; önce kullanıcıya sor. İstisna: kullanıcı açıkça "düzelt" dediyse.
- **Bulunan sırları asla yazdırma.** Rapora sadece `dosya:satır` ve türünü yaz (`Firebase API key`, `Stripe secret` gibi), değeri `****` ile maskele. Sızan bir sır bulduysan bunu ilk sıraya koy ve anahtarın **iptal edilip yenilenmesi** gerektiğini söyle; sadece silmek yetmez, git geçmişinde kalır.
- **Yıkıcı komut çalıştırma.** Veritabanına yazma, deploy, `git push`, `firebase deploy`, `rm`, geçmişi yeniden yazma yasak.
- **Kodu dış servise gönderme.** Çevrimiçi tarayıcılara/yapay zekâ servislerine kod veya sır yükleme.
- **Abartma.** Kişisel, iki kullanıcılı bir uygulamaya Kubernetes önerme. Her öneri profil ve aşamayla orantılı olmalı. "Uygulanmaz" demek başarısızlık değildir.
- **Kanıt göster.** "Var" diyorsan nerede olduğunu, "Yok" diyorsan nereye baktığını yaz.

## 1. Profiller

| Etiket | Tanım | Tipik örnek |
|---|---|---|
| `YEREL` | Sunucusu olmayan, veriyi cihazda tutan iOS/macOS uygulaması (SwiftData, UserDefaults, dosya) | Çevrimdışı takip uygulaması, pusula, menü çubuğu aracı |
| `BULUT` | Mobil/masaüstü uygulama + BaaS (Firebase, Supabase, CloudKit) veya üçüncü parti API | Paylaşımlı veri, giriş yapılan uygulama |
| `WEB-S` | Backend'i olmayan web uygulaması (SPA, statik site, localStorage) | React+Vite, Vercel'de statik |
| `WEB-API` | Kendi sunucusu/API'si/veritabanı olan web veya servis | Next.js + DB, Express API, serverless fonksiyonlar |
| `OYUN` | Oyun motoru projesi (Unity vb.), tek veya çok oyunculu | Unity mobil oyun |
| `ARAÇ` | CLI, kütüphane, MCP sunucusu, script, eklenti | npm paketi, MCP server |
| `YZ` | Projede LLM/yapay zekâ özelliği var (ek profil, diğerleriyle birlikte) | Sohbet, özetleme, öneri |
| `MAĞAZA` | App Store / Google Play'e çıkacak uygulama veya oyun (ek profil) | TestFlight'tan yayına giden her iOS uygulaması |
| `GELİR` | Uygulama içi satın alma, abonelik, paywall veya reklam geliri var (ek profil) | Premium abonelik, tek seferlik kilit açma, AdMob |
| `Hepsi` | Profil fark etmeksizin geçerli | |

> Profil birleşimi: Etiketlerden **herhangi biri** projeye uyuyorsa madde uygulanır. `MAĞAZA` ve `GELİR` ek profillerdir; ana profilin (YEREL/BULUT/OYUN) yanına eklenir. Kişisel kullanım için yapılan, mağazaya çıkmayacak uygulamalarda T, Y, Z kategorileri `➖` olur.
>
> **Android notu:** Projede Android hedefi varsa (Flutter, React Native, Kotlin, Unity Android) "(Android)" ile işaretli kontroller ve **AN** (Platform: Android) kategorisi de uygulanır; mağazaya çıkıyorsa T (Apple) yerine ya da onunla birlikte **GP** (Google Play incelemesi) uygulanır. Android hedefi yoksa AN ve GP `➖` olur. Aynı şekilde O ve T kategorileri yalnız iOS ve macOS hedefinde uygulanır.

## 2. Önem seviyesi, zamanlama ve aşama

**Önem**
- 🔴 **Kritik:** Veri kaybı, güvenlik açığı, mağaza reddi veya yasal sorun yaratır. `Yayında` aşamasında bunlar yayın engelidir.
- 🟠 **Yüksek:** Kullanıcıyı doğrudan etkiler veya sorun çıktığında körsün. Yayından önce çözülmeli.
- 🟡 **Orta:** Kaliteyi ve bakım kolaylığını artırır. Yol haritasına alınmalı.
- 🟢 **Düşük:** İyi olur. Ölçek veya ekip büyüyünce.

**Zamanlama**
- 🏁 **Baştan:** Sonradan eklemek pahalıdır (veri modeli, kimlik, migration stratejisi, UTC, yerelleştirme altyapısı). Prototipte bile kararı verilmeli.
- 🚀 **Yayından önce.**
- 📈 **Büyüyünce:** Kullanıcı/yük arttığında.

**Aşamaya göre yorum**
- `Prototip`: Sadece 🔴 + 🏁 maddeleri zorunlu, gerisi not edilir.
- `Beta`: 🔴 ve 🟠 + 🚀 maddeleri zorunlu.
- `Yayında`: 🔴 ve 🟠 tamamı zorunlu; 🟡 planlanmış olmalı.

Ajan bir maddenin varsayılan önemini proje bağlamına göre **bir kademe** yükseltebilir veya düşürebilir; gerekçeyi raporda yazar.

## 7. Bu dosyanın bakımı

- Yeni bir madde eklemek için ilgili kategoriye bir sonraki ID ile ekle; mevcut ID'leri **değiştirme** (projelerdeki raporlar bu ID'lere bağlı).
- Bir maddeyi kaldırmak yerine başına `(kullanımdan kalktı)` yaz.
- Önemli değişiklikte frontmatter'daki `sürüm` ve `güncellendi` alanlarını artır. Projelerdeki kural dosyaları kaynak sürümünü yazdığı için hangilerinin eskidiği görülür.
- Bir projede öğrenilen genel ders (örn. "Firestore listener'ı kaldırmamak faturayı 10 katına çıkardı") ilgili maddenin **Kontrol** satırına eklenmelidir. Böylece tüm projeler faydalanır.

## 8. Fazlara yayma: maddeler proje planına nasıl dağıtılır

Amaç: Kontrol maddeleri yayından bir gün önce topluca değil, **ait oldukları fazda** ele alınsın. Ajan, uygulanır maddeleri (Bölüm 0, adım 4) projenin `Plan.md` fazlarına "kontrol kapısı" olarak dağıtır; faz başında okur, faz sırasında uygular, faz sonunda kontrol eder.

### 8.1 Standart faz tipleri ve varsayılan maddeleri

Projenin kendi fazları bu tiplerle birebir aynı olmak zorunda değildir. Ajan her standart tipin maddelerini, projede **içerik olarak en uygun** faza yerleştirir.

| Faz tipi | Ne zaman | Varsayılan maddeler (sadece uygulanır olanlar) |
|---|---|---|
| **F0 · Temel / kurulum** | İlk faz veya mevcut projede "şimdi" | Tüm 🏁 maddeler: A-01…A-03, B-01, B-02, B-05, D-05, D-06, E-01, E-02, E-06, F-01, F-02, F-12 (iskelet), F-13, G-04, H-01, H-02, H-03 (strateji), I-05, K-01, L-02, M-02, M-06, N-01 (temel), N-02 (altyapı), O-03, O-04, AN-01, AN-03, AN-05, Q-01, Q-02, S-01, T-08, T-12, T-13, U-02, U-19, V-11, Z-01, Z-05 |
| **Özellik fazları** | Her özellik/modül fazı | **Özellik Bitti Tanımı** (8.2) + özelliğe özgü maddeler (8.3) |
| **İlk deneyim / onboarding** | Ana akış çalıştıktan sonra | U-01 … U-06, U-12 … U-16, N-03, N-04, N-08, Z-01 (mesaj) |
| **Gelir / paywall** | Ödeme eklenirken | V-01 … V-14, T-02 … T-04, T-12, U-07 … U-09, F-18, X-09, X-15 |
| **Sertleştirme** | Beta'dan önce | Kalan F maddeleri, X-01 … X-15, E-03, E-04, H-04, H-05, H-08, H-09, J-04 … J-09, K-02, K-03, L-01, L-03 … L-06, L-10, D-01 … D-03, D-07, C-01, B-03, R-01, R-03, R-08, AN-04, AN-06 … AN-09 |
| **Yayın hazırlığı** | Mağaza/üretim gönderiminden önce | T-01 … T-21 (Apple), GP-01 … GP-14 (Android), AN-02, AN-10, W-01 … W-30, G-01 … G-03, G-07, G-08, O-01, O-02, O-05 … O-08, P-01 … P-05, C-06, C-07, A-04, M-01, R-02, R-05, U-17 … U-19 |
| **Mağaza ve lansman** | Yayın haftası | Y-01 … Y-17, Z-02 … Z-04, Z-09 (hedefler) |
| **İşletim / büyüme** | Yayın sonrası, sürekli | Y-18 … Y-21, Z-06 … Z-09, R-04, R-06, R-07, L-07 … L-09, D-08, H-06, H-07, J-10, J-11, M-03 … M-05 AN-11 ve diğer 📈 maddeler |

### 8.2 Özellik Bitti Tanımı (her özellik fazında geçerli)

Bir özellik fazı ancak şunlar sağlanınca "bitti" sayılır (uygulanmayanlar atlanır):

- [ ] İş mantığının birim testi var ve yeşil (D-01).
- [ ] Yeni/değişen veri modeli varsa migration eklendi ve eski veriyle denendi (H-03); tarih/saat UTC (H-02).
- [ ] Yeni koleksiyon/uç nokta varsa sunucu tarafı yetki + şema doğrulaması + kurallar testi (E-02, F-02, F-12, D-02).
- [ ] Ekranlarda boş / yükleniyor / hata / çevrimdışı durumları (N-03, N-04, U-10, U-11).
- [ ] Erişilebilirlik etiketleri, Dynamic Type, dokunma alanları (N-01, U-13).
- [ ] Kullanıcıya görünen metinler yerelleştirme dosyasında; Türkçe İ/ı doğru (N-02).
- [ ] Karanlık modda kontrol edildi (N-05).
- [ ] Ağ çağrılarında timeout ve hata yönetimi (K-01, K-02).
- [ ] Loglarda sır/kişisel veri yok (L-02).
- [ ] Yeni izin varsa `Info.plist` gerekçesi + bağlamlı istek + `PrivacyInfo.xcprivacy` (G-02, G-03, T-09).
- [ ] Lint ve derleyici uyarısı yok (D-05, D-06).

### 8.3 Özelliğe göre eklenen maddeler

Özellik fazı şunlardan birini içeriyorsa ilgili maddeler o fazın kapısına eklenir:

| Özellik içeriyor | Eklenecek maddeler |
|---|---|
| Giriş / hesap | E-01 … E-05, T-01, T-06, U-02, X-05, X-11 |
| Paylaşım / eşleşme / davet | E-06, H-08, H-10, X-04 |
| Ödeme / abonelik / reklam | V kategorisi, T-02 … T-04, T-10, T-12, F-18 |
| Dosya / fotoğraf yükleme | F-09, I-01 … I-03, X-08 |
| Kullanıcı içeriği (yorum, mesaj, profil) | T-14, G-08, F-04, X-02 |
| Bildirim | K-08, U-03, U-16, T-21 (pazarlama bildirimi) |
| Gerçek zamanlı / senkron | K-07, H-08, H-10, J-05 |
| Arka plan işi / cron / kuyruk | K-04 … K-06, M-04 |
| Webhook / dış entegrasyon | F-18, F-19, K-01 … K-03, M-05, X-09 |
| Konum / kamera / sağlık verisi | G-03, G-04, F-13, T-09, T-16, J-06 |
| Yapay zekâ | S-01 … S-05, F-06, R-01, R-08 |
| Widget / uzantı / Live Activity | O-06 |
| Çok oyunculu | Q-02, Q-03, X-15 |
| Yeni dil / pazar | N-02, U-19, Y-09, Y-10, V-09, Z-07 |

### 8.4 Plan.md'ye yazma biçimi

Ajan `Plan.md` içindeki her fazın altına bir satır ekler. Faz adlarını ve sırasını değiştirmez:

```markdown
## Faz 3: Firebase senkronu
- (fazın mevcut içeriği)
- **Kontrol kapısı:** E-02 E-06 F-12 H-08 H-09 H-10 K-07 X-04 + Özellik Bitti Tanımı
```

`Plan.md`'nin en üstüne (hedefin altına) tek seferlik bir blok eklenir:

```markdown
> **Üretim kontrolü:** Profil `BULUT + MAĞAZA + GELİR` · Aşama `Prototip`
> Kaynak: ~/Desktop/hafıza/hafıza/Kurallar/Üretim Kontrolü.md (v1.1) · Rapor: [[Projeler/<Ad>/Kontrol|Kontrol]]
> Her özellik fazında Özellik Bitti Tanımı (§8.2) geçerlidir.
```

### 8.5 Yayma kuralları

1. **Tek sahip:** Her madde ID'si tek bir fazda "tamamlanır" (sahip faz). Sonraki fazlarda yeniden kontrol edilebilir ama tekrar yazılmaz. İstisna: Özellik Bitti Tanımı her özellik fazında geçerlidir.
2. **Erken olan kazanır:** 🏁 maddeler mümkün olan en erken faza konur. Proje zaten ilerlemişse ve 🏁 madde eksikse, **bir sonraki** faza 🔴 öncelikle eklenir.
3. **Eksik fazlar:** Proje yayına gidecekse ve planda "Sertleştirme", "Yayın hazırlığı", "Mağaza ve lansman" karşılığı yoksa, ajan bunları plan sonuna ekler ve kullanıcıya tek cümleyle bildirir. Proje kişisel kullanım içinse sadece gerekenler eklenir.
4. **Orantılılık:** Küçük, kişisel `YEREL` bir uygulamada kapılar kısa kalır (birkaç madde). Her fazı onlarca maddeyle doldurma; uygulanmayan maddeler `Kontrol.md`'de `➖` olarak kalır.
5. **Görevleştirme:** Faz başladığında, kapıdaki maddelerden iş gerektirenler `Yapılacaklar.md` "Şimdi" bölümüne `- [ ] [Üretim H-03] SwiftData şemasını VersionedSchema'ya taşı` biçiminde eklenir. Sadece kontrol gerektirenler faz sonunda kontrol edilir.

### 8.6 Faz döngüsü (ajan her fazda bunu uygular)

1. **Faz başında:** `Plan.md`'deki kontrol kapısı ID'lerinin tam metnini bu dosyadan oku (sadece o maddeleri). İş gerektirenleri `Yapılacaklar.md`'ye ekle.
2. **Faz sırasında:** Kod yazarken bu maddelerin "Kontrol" ve "Geçer" ölçütlerini tasarım kuralı olarak uygula. Kapı dışındaki bir maddeyle ilgili risk görürsen not et, kapsamı büyütme.
3. **Faz sonunda:** Her kapı maddesini kontrol et, kanıtla `Kontrol.md` tablosunu güncelle.
   - 🔴 madde ❌/⚠️ ise faz **bitti sayılmaz**. Ancak kullanıcı açıkça erteleme onayı verirse `Kontrol.md`'ye `Ertelendi → Faz N: <neden>` yazılır ve madde o faza taşınır.
   - 🟠/🟡 eksikler sonraki uygun faza taşınır ve not edilir.
4. **Aşama değişince** (Prototip → Beta → Yayında): Bölüm 2'ye göre zorunlu maddeler değişir; kapılar yeniden değerlendirilir.
5. **Yayın kapısı:** "Yayın hazırlığı" fazının sonunda T ve W kategorilerinin tamamı ve tüm 🔴 maddeler ✅ veya `➖` olmalıdır. Aksi halde ajan "yayına hazır" demez.
