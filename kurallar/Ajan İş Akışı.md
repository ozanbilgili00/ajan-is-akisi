---
tür: ana-kural
sürüm: 1.2
güncellendi: 2026-11-12
---

# Ajan İş Akışı: Ana Kural Dosyası

Alt ajanların (Haiku, Sonnet), Gemini'nin ve Opus'un hangi işi ne zaman yapacağını tek yerde tanımlar. Amaç maliyeti düşürmek ve hız kazanmak; hiçbir projede bu düzeni baştan anlatmak gerekmez.

**Mutlak yol:** `~/Desktop/hafıza/hafıza/Kurallar/Ajan İş Akışı.md` · **Ajan tanımları:** `~/.claude/agents/` · **Özet:** `~/.claude/CLAUDE.md` "Ajan iş akışı" bölümü.

**Projeye göre hat:** bu dosya kimin hangi modelle çalışacağını söyler. İşin projeye göre nasıl yürüyeceği (doğrulama zinciri, ortak kaynaklar, bitti tanımı) ve güvenlik kapıları `Kurallar/İş Akışı/` klasöründedir: [[Kurallar/İş Akışı/İş Akışı|Seçim Notu]], [[Kurallar/İş Akışı/Güvenlik Hattı|Güvenlik Hattı]] ve tür notları. Çelişkide sıkı olan geçerlidir.

**Ne zaman okunur:** Yönetici (ana oturum) ilk ajanı açmadan ya da Gemini'ye ilk işi vermeden önce bir kez okur. Alt ajanlar bu dosyayı okumaz; kendi tanımlarına uyar.

**İçindekiler:** 1 Roller · 2 Ajan açma kararı · 3 Kim ne yapar · 4 Opus ne zaman kod yazar · 5 Gemini · 6 Test ajanı ve güvenlik denetçisi · 7 İş tanımı şablonu · 8 Hat · 9 Paralellik · 10 Aksilikler · 11 Kayıt · 12 Araçlar · 13 Projeye özel kurallar · 14 Gerekçe ve ölçümler

---

## 1. Roller

| Ajan | Model · efor | Ne için | Yapamaz |
|---|---|---|---|
| Yönetici (ana oturum) | Opus | Plan, iş tanımı, denetim, son karar, gerektiğinde kod | — |
| `mekanik` | Haiku · medium | Derleme, test, ölçüm, tarama, ekran görüntüsü, vault ve belge güncellemesi | Kaynak kodu değiştirmek |
| `uygulayici-haiku` | Haiku · high | Tarifi net, sınırı belli kod; test genişletme; arayüz metni ve stil | Tasarım kararı, güvenlik açısından kritik kod |
| `uygulayici` | Sonnet · medium | Çok dosyalı ya da tasarım kararı isteyen paket; güvenlik açısından kritik kod | — |
| `test-yazari` | Sonnet · medium | Tariften bağımsız test (uygulama kodunu okumadan) | Uygulama kodunu değiştirmek |
| `guvenlik-denetcisi` | Sonnet · high | Temiz bağlamda bağımsız güvenlik denetimi | Kod değiştirmek |
| Gemini (`mcp__gemini__*`) | Gemini 4 Hidrojen · kod `high`, okuma ve özet `low`-`medium` | Sonnet'in yapacağı büyük ve tarifi net kod paketi, büyük okuma ve özet; şartlar uyuyorsa (Bölüm 5) | Denetim, güvenlik kodu, tasarım kararı isteyen paket |

- Hiçbir alt ajan başka ajan açamaz, Gemini'yi çağıramaz. `mekanik` dışındakiler hafıza araçlarını kullanamaz.
- Canlıya erişen araçlar (Supabase, Firebase, Vercel MCP) tüm alt ajanlara kapalıdır (`disallowedTools`); yalnız yönetici kullanır (Güvenlik Hattı Bölüm 6).
- Efor tavanı: Sonnet en çok `medium`, yalnız denetimde `high`. Haiku en çok `high`. Tanımdaki değer çağrıda yükseltilmez.
- Yerleşik türler (`general-purpose`, `Explore`, `Plan`) kullanılırsa `model` ve `effort` her çağrıda açıkça verilir. Web ve fizibilite araştırması: `general-purpose`, Sonnet, `medium`. Kod tabanı keşfi: `Explore`, Haiku, `medium`.

## 2. Ajan açma kararı

Varsayılan: Opus tek başına çalışır. Ajan, aşağıdaki dört şartın hepsi sağlanıyorsa sormadan açılır.

1. **Ayrılabilir:** işin sınırı ve kabul ölçütü birkaç cümleyle yazılabiliyor.
2. **Yeterince büyük:** işi anlatmak, işi yapmaktan belirgin şekilde kısa.
3. **Doğrulanabilir:** sonuç test, derleme, ölçüm ya da diff okumasıyla kontrol edilebiliyor.
4. **Kaynak çakışmıyor:** aynı dosyalar, tek Unity, tek simülatör ya da tek derleme klasörü başka işle paylaşılmıyor (paylaşılıyorsa sırayla).

"Yeterince büyük" için kılavuz eşikler (herhangi biri yeter):
- 3 ya da daha çok dosya değişecek, ya da yaklaşık 150 satırdan fazla yeni kod.
- 10 ya da daha çok dosya okumayı gerektiren tarama ve araştırma.
- 2 dakikadan uzun süren ya da tekrar tekrar koşacak derleme, test ve ölçüm turu.
- Birbirinden bağımsız 2 ya da daha çok parça.

Ajan açılmaz:
- 1-2 dosyalık, yaklaşık 50 satırın altındaki değişiklik.
- Nedeni bilinmeyen hatanın teşhisi (teşhisi Opus yapar; uzun yeniden üretme ve ölçüm adımları `mekanik`e gidebilir).
- Ozan'la hızlı gidip gelen ince ayar turları (arayüz cilası, metin, tasarım konuşması).
- Plan, mimari karar, iş tanımı yazımı, denetim kararı.

Ajanlı düzende yürüyen bir işte kapı ölçümleri (derleme, test, performans, ekran görüntüsü) her zaman `mekanik`e verilir; Opus yalnız sonucu okur. Tek seferlik, 1 dakikanın altında ve çıktısı kısa bir komutu Opus kendisi koşar.

## 3. Kim ne yapar

Bir işi vermeden önce şu sırayla sorulur: **Haiku yapabilir mi → Gemini'ye uygun mu → Sonnet.**

**Haiku'ya (`uygulayici-haiku`):** tarifi net ve sınırı belli kod (bileşen, yardımcı işlev, mevcut kalıbın benzeri), test yazma ve genişletme, arayüz metni ve stil, erişilebilirlik düzeltmeleri, mekanik denetim düzeltmeleri, yalnız istemcide çalışan özellikler, belge.

**Sonnet'te kalır (`uygulayici`):** kimlik, oturum, şifreleme, yetki kodu; veritabanı rolleri, erişim kuralları ve migration tasarımı; CSP ve önbellek gibi hatası sessiz kalan mimari kararlar; çok dosyalı ve tasarım kararı isteyen paketler.

Haiku'nun yazdığı kod aynı denetimden geçer. Bulgu sayısı ve token harcaması Sonnet paketleriyle karşılaştırılır; Haiku'nun payı buna göre genişletilir ya da daraltılır.

## 4. Opus ne zaman kod yazar

- **Küçük düzeltme:** ajana anlatmak değişikliğin kendisinden uzun sürecekse.
- **Denetim sonrası:** ajan işinden çıkan küçük eksikleri (birkaç satır, tek dosya) kendisi kapatır. Büyük ya da çok dosyalı bulgu aynı ajana `SendMessage` ile geri gider; bağlamı korunur.
- **Devralma:** ajan aynı işte iki kez başarısız olduysa, ya da limit dolduysa ve Haiku ile Gemini uygun değilse.
- **Kesişen tasarım:** birçok parçayı birden etkileyen, parçalanınca tutarsızlaşacak işler.
- **Gerekli gördüğünde:** yukarıdakiler kılavuzdur; Opus daha ucuz ya da daha güvenli olacağını görürse kendisi yazar ve nedenini ara raporda bir cümleyle söyler.

## 5. Gemini

Amaç Claude kotasını korumak. Gemini, Sonnet uygulayıcının yerine şu şartların hepsi varsa kullanılır:

- İş büyük ve kendi içinde kapalı bir kod paketi.
- Dokunulacak dosyaların listesi açıkça verilebiliyor (kopyada `.git` yok; `git diff`, `git log` istenmez).
- Uygulamayı çalıştırmak, ağa çıkmak ya da cihaz kullanmak gerekmiyor.
- Kimlik, yetki, şifreleme, ödeme kodu değil.
- Acil değil (taban yaklaşık 40 saniye, büyük iş 7-19 dakika).
- `gemini_status` kotanın müsait olduğunu gösteriyor.

Akış: `gemini_status` → `gemini_task` (kod) ya da `gemini_ask` (okuma, özet) → `gemini_result` → yamayı Opus okur → `gemini_apply` → derleme ve test → kötüyse geri al.

Kurallar:
- Aynı anda tek iş. Kota birlikte tükenir, işler yarıda kalır.
- **Model: Gemini 4 Hidrojen.** Kademe seçilir, model kimliği yazılmaz:
  - Kod paketi (`gemini_task`): `tier: derin` (`gemini-4-hydrogen-high`).
  - Depo okuma, özet, rapor taslağı (`gemini_ask`): `tier: dengeli` (`medium`); kısa ve tek konulu okuma `tier: hizli` (`low`).
  - `xhigh` kullanılmaz: `high`a göre yaklaşık iki kat çıktı token'ı, küçük kazanç. Yalnız Ozan isterse.
- **Hidrojen'in sınırı:** bağımsız ölçümde Sonnet 5.5'in biraz altında; terminal ve uzun ajan işlerinde Sonnet önde. Bu yüzden tasarım kararı isteyen ya da uygulamayı çalıştırarak ilerleyen paket Gemini'ye gitmez, `uygulayici`de kalır.
- **Yükseltme:** Hidrojen aynı pakette iki kez başarısız olursa iş `uygulayici`ye (Sonnet) geçer. Claude kotası doluysa ve paket bekleyemiyorsa `model: claude-sonnet-5-5-medium` ile Gemini üzerinden bir kez denenir; üstüne çıkılmaz.
- Denetim ve inceleme Gemini'ye verilmez (eski modellerde `high` efor kotayı çok hızlı bitirdi, bulguların yaklaşık 6'da 1'i yanlıştı; Hidrojen'le yeniden ölçülmedi).
- Hidrojen'in Pro hesaptaki kotası bilinmiyor. İlk işlerde `gemini_status` kullanım özeti `Projeler/Gemini MCP` günlüğüne yazılır; kota hatası gelirse tarih ve iş sayısı not edilir.
- Küçük soru ve deneme çağrısı yapılmaz.
- Kota doluysa sormadan Claude ajanına dönülür, ara raporda belirtilir.
- Gemini'nin her iddiası koda bakılarak doğrulanır.

## 6. Test ajanı ve güvenlik denetçisi

Kararı işin neye dokunduğu ve projenin güvenlik sınıfı verir. **Kesin tablo Güvenlik Hattı Bölüm 3'tedir** (GS0-GS3); aşağıdaki tablo sınıfı henüz yazılmamış projede en az uygulanacak düzeydir.

| İş neye dokunuyor | `test-yazari` | `guvenlik-denetcisi` |
|---|---|---|
| Kimlik, oturum, şifreleme, yetki, ödeme, veritabanı erişim kuralları, sır yönetimi | Evet | Evet, iki tur |
| Ağdan ya da kullanıcıdan gelen girdiyi işleyen sunucu kodu, dosya yükleme, kullanıcı girdisiyle alt süreç, derin bağlantı | İşe göre | Evet, tek tur |
| Hatası sessiz kalan mantık (hesaplama, veri hattı, ayrıştırıcı, eşitleme) | Evet | Hayır |
| Arayüz, yerel kişisel araç, oyun içi mantık, belge | Hayır | Hayır |

- `test-yazari` açılmayan işte testi uygulayan ajan kendisi yazar.
- İki tur: ilk denetim, bulgular kapatıldıktan sonra temiz bağlamda ikinci denetim.
- Kriptografi ve kimlik çekirdeğinde denetçi çağrıda `model: opus` ile çalıştırılabilir.
- Kritik ya da yüksek bulgu açıkken iş bitmiş sayılmaz, birleştirilmez. GS3 projede orta bulgu da engeldir.
- İkinci tur yeni bir denetçi örneğiyle yapılır; düzeltmeyi yazan ajan kendi işini denetlemez.
- Yayına gidecek projede Sertleştirme fazında bir kez tam denetim yapılır (Üretim Kontrolü, X kategorisi: yalnız kendi uygulamasında, staging'de, Ozan'ın onayıyla).
- `YEREL`, `OYUN`, `ARAÇ` profilli ve ağa açık parçası olmayan projede bu iki ajan hiç açılmayabilir.

## 7. İş tanımı şablonu

Her ajan çağrısının ve her Gemini işinin istemi şu başlıkları taşır (kopyalanabilir hali: `Şablonlar/İş Tanımı.md`). Ajan önceki konuşmayı görmez; tanım tek başına yeterli olmalıdır.

- **Amaç:** ne yapılacak ve neden, 2-3 cümle.
- **Önce oku:** proje kökü; `CLAUDE.md`, `.claude/rules/uretim.md`; ilgili kaynak dosyalar ve vault notları (yol olarak). Üretim Kontrolü maddesi gerekiyorsa kaynak dosya değil, projenin parça dosyası (`Kurallar/Üretim Kontrolü/<Tür>.md`) ve okunacak kimlikler verilir.
- **Kapsam:** dokunulacak dosya ve klasörler; dokunulmayacaklar.
- **Kabul ölçütleri:** numaralı, kontrol edilebilir maddeler.
- **Doğrulama:** çalıştırılacak komut ve beklenen sonuç.
- **Çalışma yeri:** klasör ya da worktree, dal adı; commit izni var mı.
- **Rapor dosyası:** tam yol (Bölüm 11).
- **Kısıtlar:** projeye özel yasaklar (odak çalma, katalog biçimi, tek Unity gibi). Yasak açık yazılır: "Birleştirme YAPMA", "push YAPMA".
- **Güvenlik** (tetikleyiciye dokunan ya da GS2-GS3 projedeki işte): Güvenlik Hattı Bölüm 7'deki madde.

Doğrulama komutları `&&` ile zincirlenir. İsteme sır, canlı proje kimliği, bot engeli ya da erişim duvarı atlatma talimatı yazılmaz.

`test-yazari` için uygulama kodu yerine tarif, kabul ölçütleri ve arayüz imzaları verilir. `guvenlik-denetcisi` için diff ya da dal, projenin güvenlik notu ve ilgili Üretim Kontrolü maddeleri verilir; uygulayıcının raporu verilmez.

## 8. Hat

1. Opus iş tanımını yazar ve ajanı açar; Ozan'a tek satır haber verir.
2. Ajan çalışır, raporunu artımlı yazar.
3. Opus raporu iddia sayar: diff'i okur, doğrulamayı kendisi ya da `mekanik` ile yeniden koşturur.
4. Gerekiyorsa `test-yazari` ve `guvenlik-denetcisi` (Bölüm 6).
5. Bulgular kapatılır (Bölüm 4 ve 10).
6. Kayıt (Bölüm 11) ve Ozan'a 3-6 satırlık ara rapor.

**Bitti tanımı:** kabul ölçütleri sağlandı · doğrulama yeşil · açık kritik ya da yüksek bulgu yok · fazın kontrol kapısı kanıtlandı · vault güncel.

Commit, push ve PR kuralları projeye göredir (`uretim.md`). Proje kuralı yoksa push için Ozan'a sorulur. PR akışı olan projede CI yeşil ve denetim bulguları kapalıysa Opus PR'ı sormadan birleştirir. Birleşince canlıda migration ya da dağıtım tetikleyen PR Ozan'ın onayını bekler.

## 9. Paralellik

- Paralel ajan yalnız dosyaları kesişmeyen işlerde, ayrı worktree ve dalda açılır. Aynı dosyalara dokunan işler sıralıdır.
- Aynı anda en çok 3 ajan, bunların en çok 2'si Sonnet. Gemini ayrıca en çok 1 iş.
- Ortak kaynaklar sırayla kullanılır: tek Unity örneği, tek simülatör, tek Xcode derleme klasörü, cihaz, ana çalışma kopyası.
- Aynı projede ikinci bir Claude oturumu varsa iş bölümü `ListAgents` ve `SendMessage` ile yapılır, ana nota yazılır.

## 10. Aksilikler

- **Doğrulama düştü:** bulgular aynı ajana `SendMessage` ile gider (bir tur).
- **Haiku ikinci kez düştü:** iş `uygulayici`ye yükseltilir (önceki rapor ve bulgularla); kalan küçükse Opus kapatır.
- **Sonnet ikinci kez düştü:** Opus devralır.
- **Kullanım limiti (429):** acil değilse limit açılınca aynı ajan `SendMessage` ile sürdürülür. Beklenemiyorsa sıra: Haiku (uygunsa) → Gemini (uygunsa) → Opus.
- **Gemini kotası dolu:** Claude ajanına dönülür, raporda belirtilir.
- **Ajan kapsam dışına çıktı ya da iş tanımı yanlıştı:** değişiklik alınmaz; tanım düzeltilip yeniden verilir.
- **Ajan rapor dosyası yazmayı reddetti:** rapor son mesajdan alınır, yönetici `Günlük.md`'ye özetler.
- **Sır sızdı ya da ajan güvenlik kontrolünü atlattı** (testi kapatma, `--no-verify`, kuralı gevşetme): iş durur, değişiklik alınmaz, Ozan'a ilk satırda haber verilir (Güvenlik Hattı Bölüm 6).
- **Bağlam yaklaşık %40'ı geçti (Ozan'ın ekranındaki değer):** yeni ajan açılmaz, çalışanlar durdurulur, yarım iş kaydedilir, vault'a "DEVAM" notu (dal, commit, ajan kimlikleri) yazılır ve Ozan'a compact için haber verilir.

## 11. Kayıt

- **Ham rapor:** ajan kendi raporunu `Projeler/<Ad>/Ajan Raporları/<YYYY-AA-GG> <kısa ad>.md` dosyasına artımlı yazar (faz bazlı projede `Faz N.md`). Proje vault'ta yoksa oturumun scratchpad klasörüne.
- **Özet:** Opus her ajan işini `Günlük.md`'ye yazar: ne istendi · kim (model, efor) · sonuç · denetim kararı. `Ajanlar.md` tutan projelerde (Kampüs Karnesi) o dosya da sürdürülür; yeni projede ayrı dosya açılmaz.
- **Ölçüm:** biten her alt ajan otomatik kaydedilir (`~/.claude/hooks/olcum.py`, `SubagentStop` kancası → `~/.claude/state/ajan-olcum.jsonl`: ajan türü, model, süre, tur, araç çağrısı, token). `python3 ~/.claude/hooks/olcum.py ozet 30` ajan türüne göre ortalamayı verir. Bulgu sayısı ve denetim kararı otomatik ölçülemez; onları Opus günlük özetine yazar. Haiku'nun payı (Bölüm 3) ve efor tavanları bu özetle gözden geçirilir.
- Ajanlar ana notu, `Yapılacaklar.md`'yi ve `Günlük.md`'yi güncellemez; bunu Opus yapar ya da açıkça `mekanik`e verir.

## 12. Araçlar

- **Xcode MCP (`mcp__xcode__*`):** iOS ve macOS'ta derleme, test, simülatör, ekran görüntüsü ve profil işleri düz `xcodebuild` yerine bununla yapılır (çıktı kısa ve yapılı). Aynı anda tek derleme ve tek simülatör. `open_in_xcode` ve pencereyi öne getiren işlemler yalnız Ozan isterse.
- **Unity MCP:** tek Unity örneği; ajanlar sırayla kullanır.
- **Gemini MCP:** yalnız yönetici çağırır (Bölüm 5).
- **Hafıza MCP (`mcp__hafiza__*`):** yönetici kullanır; `mekanik` yalnız iş tanımı isterse. `is_akisi` projenin tür notunu ve (GS2-GS3 ise) Güvenlik Hattı'nı tek çağrıda getirir; `denetle` iş akışı satırı eksik projeleri işaretler.
- **Güvenlik kancası (`~/.claude/hooks/guvenlik.py`):** sır okumayı, kanca atlatmayı ve alt ajanın canlıya ya da dışarıya yazmasını engeller; yöneticinin canlı yazmalarını Ozan'a sordurur (Güvenlik Hattı, "Zorlama").

## 13. Projeye özel kurallar

Projenin türü ve güvenlik sınıfı `Plan.md` profil bloğundaki `**İş akışı:**` satırında yazar; hat o türün notuna göre yürür (`Kurallar/İş Akışı/`). Satır yoksa ilk plan ya da faz işinde Seçim Notu Bölüm 2'ye göre eklenir.

Projeye özel ajan kısıtları (yasak klasörler, katalog biçimi, commit düzeni, zorunlu ölçüm betiği) proje kökündeki `.claude/rules/uretim.md` dosyasına "Ajanlar" başlığıyla yazılır ve iş tanımının "Kısıtlar" maddesine taşınır. Proje kuralı bu dosyadan daha sıkıysa proje kuralı geçerlidir; daha gevşek olamaz.

## 14. Gerekçe ve ölçümler

Bu kurallar Ozan'ın talimatlarından ve ölçümlerden derlendi. Değiştirirken gerekçeye bak.

- **2026-10-06 (Sistem Monitörü, Kampüs Karnesi):** "gerekli yerlerde işleri sonnet5.5 med eforta yaptır sen denetle ... birbirinizle iletişim halinde olun hafızaya her işi kaydedin". Aynı gün: "arada bana rapor ver hiç rapor vermiyorsun" ve "context 40ı geçince compact için işlemlere ara ver".
- **2026-10-07:** CI yeşil ve denetimler temizse PR'ı Opus birleştirir ("Evet, hep sen birleştir").
- **2026-10-08/09:** "sub agent olarak haiku 5.5'i de kullanabilirsin gerekli yerlerde".
- **2026-10-10:** Sonnet limite takılınca Opus ölçümleri kendi yapmaya başladı; Ozan "neden ajanları kullanmıyorsun" dedi. Mekanik kapı işleri ajanda kalır. Aynı gün: Token Optimizer hook'unun bağlam yüzdesi yanıltıcı (hook %43, ekran %9); Ozan'ın ekranı esas.
- **2026-10-12:** "denetimde highda kullanabilirsin ama geri kalanlarda sonnet med i geçmesin maliyet çok yükseliyo haiku high seviyeye çıkabilir". Efor belirtilmeden açılan ajan başına 300-850 bin token gidiyordu. Aynı gün: "haikunu yapabileceğini düşündüğün kod işlerini vermeni istiyorum".
- **2026-10-12 (bu dosya):** Ozan'ın kararları: Opus kod yazabilir ve ajanın yapamadığı işi devralır; ajanlar her projede değil, şartlar elverişliyse; Gemini maliyet için, gerektiğinde Sonnet gibi; test ajanı ve güvenlik denetçisi projenin kapsamına göre. Bölüm 2'deki eşikler, Bölüm 3'teki Sonnet listesi ve Bölüm 9'daki "en çok 3 ajan" Opus'un önerisidir; Ozan değiştirebilir.
- **2026-11-10:** Ozan: "iş akışını yapılan projeye göre değiştirmeyi istiyorum, kategori olarak iş akışı yapalım, özellikle güvenlik kısmı sıkı olmalı"; kararları Opus'a bıraktı. `Kurallar/İş Akışı/` kategorisi açıldı (seçim notu, güvenlik hattı, beş tür notu). Bu dosyaya eklenenler: canlı MCP araçlarının alt ajanlara kapatılması, GS3'te orta bulgu engeli, iş tanımına Güvenlik maddesi, Kampüs Karnesi ve POS dersleri (açık yasak dili, `&&` zinciri, rapor reddi). Aynı gün ikinci tur ("hepsini yap"): güvenlik kancası, ölçüm kancası, oturum kancasında iş akışı bloğu, Hafıza MCP `is_akisi` aracı, 29 projenin `Plan.md` satırı, şablonlar (`Şablonlar/İş Tanımı.md`, `Şablonlar/Güvenlik.md`), Üretim Kontrolü v1.2 (Bizim Site F10 dersleri). Yedek: `~/.claude/yedek/2026-11-10/`.
- **2026-11-12:** Ozan: "geminide hidrojen modelini de mcpye ekle ve ajan kullanımı kuralını ona göre kullan". Gemini 4 Hidrojen aynı gün çıktı; Google'ın günlük kodlama ve ajan işi modeli, 1M bağlam, efor `low/medium/high/xhigh` (varsayılan `high`). Artificial Analysis endeksi: `low` 27, `medium` 41, `high` 51, `xhigh` 54; görev başı maliyet `high` 1,87 $, `xhigh` 3,16 $ (Sonnet 5.5'in yaklaşık üçte biri). Terminal-Bench 4.0 bağımsız ölçüm: Hidrojen %54, Sonnet 5.5 %64. Rakamlar çıkış günü haberlerinden, bağımsız doğrulaması sınırlı. Kendi denememiz: `low` ve `medium` başsız modda depo kopyasından dosyayı doğru okudu (48 sn, ~27 bin token). Kademe seçimi ve "kodda `high`, `xhigh` yok" kuralı Opus'un önerisidir; Ozan değiştirebilir. Kod yazma kalitesi Hidrojen'le henüz ölçülmedi; aşağıdaki ölçümler eski modellere aittir.
- **Gemini ölçümleri (Hidrojen öncesi):** kod yazma güvenilir (20/20 gizli test; 21 dosyalık paket ilk çalıştırmada 0 tip, lint ve test hatası). İncelemede yaklaşık 6 bulgudan 1'i kendinden emin yanlış. Yeni hesapta kota 3 işte doldu (1 kod işi `medium`, 2 inceleme `high`; tek inceleme 534 saniyede 295 bin token), yaklaşık 5 saatte sıfırlanıyor. Ayrıntı: `Projeler/Gemini MCP`.
- **Kampüs Karnesi deneyimi:** tariften test yazan ayrı ajan ve temiz bağlamlı denetçi, uygulayıcının kaçırdığı orta düzey bulguları yakaladı; limit yüzünden yarıda kalan ajan `SendMessage` ile aynı bağlamla sürdürüldü.
