---
tür: üretilmiş-parça
kaynak: Kurallar/Üretim Kontrolü.md
kaynak-sürüm: 1.3
kaynak-özet: b6bdd028b3e2
---

# Üretim Kontrolü: Rehber

> **Elle düzenlenmez.** Bu dosya `Kurallar/Üretim Kontrolü.md` kaynağından `~/.claude/hooks/uretim_bol.py` ile üretilir; değişiklik kaynağa yapılır, parçalar oturum başında kendiliğinden yenilenir.
>
> Hangi proje hangi parçayı okur. Kaynak dosyanın tamamı okunmaz.


## Parçalar

| Dosya | Kimler okur | Madde | Yaklaşık boyut |
|---|---|---|---|
| [[Kurallar/Üretim Kontrolü/Web\|Web]] | Web sitesi, web uygulaması, PWA ve bunların arka ucu (`WEB-S`, `WEB-API`). | 159 | 76 bin karakter |
| [[Kurallar/Üretim Kontrolü/Apple\|Apple]] | iOS ve macOS uygulamaları (`YEREL`, `BULUT`). | 129 | 62 bin karakter |
| [[Kurallar/Üretim Kontrolü/Android\|Android]] | Android uygulamaları: Kotlin, Flutter, React Native (`YEREL`, `BULUT`). | 132 | 67 bin karakter |
| [[Kurallar/Üretim Kontrolü/Oyun\|Oyun]] | Unity ve diğer oyun motoru projeleri (`OYUN`). Platform maddeleri burada değil: iOS'a çıkıyorsa Apple.md içindeki O kategorisi, Android'e çıkıyorsa Android.md içindeki AN kategorisi de okunur. | 69 | 32 bin karakter |
| [[Kurallar/Üretim Kontrolü/Araç\|Araç]] | CLI, kütüphane, MCP sunucusu, betik, eklenti (`ARAÇ`). | 39 | 18 bin karakter |
| [[Kurallar/Üretim Kontrolü/Ek - Mağaza\|Ek - Mağaza]] | Mağazaya çıkan her uygulama ve oyun (`MAĞAZA`): yayın öncesi ürün sorunları ve kırma testi. Platform incelemesi ayrı dosyada. | 15 | 12 bin karakter |
| [[Kurallar/Üretim Kontrolü/Ek - Apple İncelemesi\|Ek - Apple İncelemesi]] | App Store'a gönderilecek iOS ve macOS uygulamaları (T kategorisi). | 21 | 14 bin karakter |
| [[Kurallar/Üretim Kontrolü/Ek - Google Play İncelemesi\|Ek - Google Play İncelemesi]] | Google Play'e gönderilecek Android uygulamaları (GP kategorisi). | 14 | 9 bin karakter |
| [[Kurallar/Üretim Kontrolü/Ek - Mağaza Sayfası ve Büyüme\|Ek - Mağaza Sayfası ve Büyüme]] | Yayın haftası ve sonrası: ASO, mağaza sayfası, büyüme ve metrikler (Y ve Z kategorileri). | 30 | 19 bin karakter |
| [[Kurallar/Üretim Kontrolü/Ek - Gelir\|Ek - Gelir]] | Satın alma, abonelik, paywall ya da reklam geliri olan projeler (`GELİR`). | 21 | 13 bin karakter |
| [[Kurallar/Üretim Kontrolü/Ek - Yapay Zekâ\|Ek - Yapay Zekâ]] | LLM ya da yapay zekâ özelliği olan projeler (`YZ`). | 14 | 8 bin karakter |
| [[Kurallar/Üretim Kontrolü/Yöntem\|Yöntem]] | Plan kuran, faz kapısı yazan yönetici | — | 13 bin karakter |
| [[Kurallar/Üretim Kontrolü/Şablonlar ve Komutlar\|Şablonlar ve Komutlar]] | Proje kural dosyası ya da denetim raporu yazan | — | 6 bin karakter |

Kaynak: 278 madde, 147 bin karakter (sürüm 1.3).

## Hangi proje neyi okur

| Proje | Tür dosyası | Ek dosyalar |
|---|---|---|
| Web sitesi, web uygulaması, PWA | Web (kademesine kadar) | `YZ` → Ek - Yapay Zekâ · `GELİR` → Ek - Gelir |
| iOS ya da macOS uygulaması | Apple | `MAĞAZA` → Ek - Mağaza + Ek - Apple İncelemesi, yayın haftasında Ek - Mağaza Sayfası ve Büyüme · `GELİR` → Ek - Gelir · `YZ` → Ek - Yapay Zekâ |
| Android uygulaması | Android | `MAĞAZA` → Ek - Mağaza + Ek - Google Play İncelemesi, yayın haftasında Ek - Mağaza Sayfası ve Büyüme · `GELİR` → Ek - Gelir · `YZ` → Ek - Yapay Zekâ |
| Oyun | Oyun (+ çıktığı platformun O ya da AN kategorisi) | Mağazaya çıkıyorsa platformun mağaza ekleri · çevrimiçi sunucusu varsa Web'in B ve C kademeleri |
| CLI, MCP sunucusu, betik | Araç | `YZ` → Ek - Yapay Zekâ |
| Uygulama + kendi arka ucu | Uygulamanın tür dosyası + Web'in B ve C kademeleri | Profile göre |
| İki platforma çıkan uygulama (Flutter, React Native) | Apple + Android (ortak maddeler aynıdır; ikincisinde yalnız AN ve farklı kademeleri oku) | İki mağaza eki |

## Okuma kuralı

1. Oturum başındaki hafıza bağlamı projenin parçalarını yol olarak verir; onlar dışındaki parça okunmaz.
2. Bir parçanın da tamamı okunmaz: önce **dizin**, sonra fazın `**Kontrol kapısı:**` satırındaki kimliklerin metni.
3. Hafıza MCP yüklüyse `kural_oku` (kimlik, aralık ya da kategori ile) ve `kural_listele` (profil süzgeciyle) aynı işi parça dosyasını açmadan yapar; alt ajanlar MCP kullanamadığı için onlara parça dosyasının yolu ve kimlikler verilir.
4. Plan kurarken ve faz kapısı yazarken [[Kurallar/Üretim Kontrolü/Yöntem|Yöntem]] okunur.
5. Madde eklemek ya da değiştirmek için yalnız kaynak dosya düzenlenir (Yöntem, Bölüm 7).
