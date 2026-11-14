#!/usr/bin/env python3
"""Üretim Kontrolü kaynak dosyasını proje türüne göre parçalara böler.

Kaynak (tek doğru yer):  <vault>/Kurallar/Üretim Kontrolü.md
Üretilen parçalar:       <vault>/Kurallar/Üretim Kontrolü/*.md   (elle düzenlenmez)

  uretim_bol.py            Kaynak değiştiyse parçaları yeniden üretir.
  uretim_bol.py --zorla    Her durumda üretir.
  uretim_bol.py --denetle  Yazmadan kapsama raporu basar.

hafiza.py her oturum başında guncelle() çağırır; parçalar kaynakla hep aynı kalır.
Madde metni kaynaktan harfi harfine kopyalanır; bir madde, etiketine uyan her parçada yer alır.
"""
import hashlib
import os
import re
import sys
import unicodedata

VAULT = os.path.expanduser("~/Desktop/hafıza/hafıza")
KAYNAK = os.path.join(VAULT, "Kurallar", "Üretim Kontrolü.md")
HEDEF = os.path.join(VAULT, "Kurallar", "Üretim Kontrolü")
ETIKETLER = ["Hepsi", "YEREL", "BULUT", "WEB-S", "WEB-API", "OYUN", "ARAÇ", "YZ", "MAĞAZA", "GELİR"]
MAGAZA_KAT = {"T", "GP", "Y", "Z"}  # kendi ek dosyası olan kategoriler

# Tür dosyaları: (dosya, kimler okur, hariç kategoriler, kademeler[(başlık, koşul)])
TURLER = [
    ("Web", "Web sitesi, web uygulaması, PWA ve bunların arka ucu (`WEB-S`, `WEB-API`).", {"O", "AN", "Q"}, [
        ("Her web projesi", lambda e: bool(e & {"WEB-S", "Hepsi"})),
        ("Arka ucu olan web (Firebase, Supabase ya da kendi sunucusu)", lambda e: {"BULUT", "WEB-API"} <= e),
        ("Yalnız kendi sunucusu ya da API'si olan web", lambda e: "WEB-API" in e),
        ("`BULUT` profili de taşıyan web (PWA + hazır arka uç): uygulama odaklı ek maddeler", lambda e: "BULUT" in e),
    ]),
    ("Apple", "iOS ve macOS uygulamaları (`YEREL`, `BULUT`).", {"AN", "P", "Q"}, [
        ("Her uygulama", lambda e: bool(e & {"YEREL", "Hepsi"})),
        ("Buluta ya da dış API'ye bağlı uygulama (`BULUT`)", lambda e: "BULUT" in e),
    ]),
    ("Android", "Android uygulamaları: Kotlin, Flutter, React Native (`YEREL`, `BULUT`).", {"O", "P", "Q"}, [
        ("Her uygulama", lambda e: bool(e & {"YEREL", "Hepsi"})),
        ("Buluta ya da dış API'ye bağlı uygulama (`BULUT`)", lambda e: "BULUT" in e),
    ]),
    ("Oyun", "Unity ve diğer oyun motoru projeleri (`OYUN`). Platform maddeleri burada değil: iOS'a çıkıyorsa "
             "Apple.md içindeki O kategorisi, Android'e çıkıyorsa Android.md içindeki AN kategorisi de okunur.", {"O", "AN", "P"}, [
        ("Her oyun", lambda e: bool(e & {"OYUN", "Hepsi"})),
    ]),
    ("Araç", "CLI, kütüphane, MCP sunucusu, betik, eklenti (`ARAÇ`).", {"AN", "P", "Q"}, [
        ("Her araç", lambda e: bool(e & {"ARAÇ", "Hepsi"})),
    ]),
]
# Ek dosyalar: (dosya, kimler okur, seçici(madde), önsözü de alınacak kategoriler)
EKLER = [
    ("Ek - Mağaza", "Mağazaya çıkan her uygulama ve oyun (`MAĞAZA`): yayın öncesi ürün sorunları ve kırma testi. "
                    "Platform incelemesi ayrı dosyada.", lambda m: "MAĞAZA" in m["e"] and m["kat"] not in MAGAZA_KAT, {"W"}),
    ("Ek - Apple İncelemesi", "App Store'a gönderilecek iOS ve macOS uygulamaları (T kategorisi).", lambda m: m["kat"] == "T", set()),
    ("Ek - Google Play İncelemesi", "Google Play'e gönderilecek Android uygulamaları (GP kategorisi).", lambda m: m["kat"] == "GP", set()),
    ("Ek - Mağaza Sayfası ve Büyüme", "Yayın haftası ve sonrası: ASO, mağaza sayfası, büyüme ve metrikler (Y ve Z kategorileri).",
     lambda m: m["kat"] in {"Y", "Z"}, set()),
    ("Ek - Gelir", "Satın alma, abonelik, paywall ya da reklam geliri olan projeler (`GELİR`).",
     lambda m: "GELİR" in m["e"] and m["kat"] not in MAGAZA_KAT, set()),
    ("Ek - Yapay Zekâ", "LLM ya da yapay zekâ özelliği olan projeler (`YZ`).", lambda m: "YZ" in m["e"], set()),
]
UYARI = ("> **Elle düzenlenmez.** Bu dosya `Kurallar/Üretim Kontrolü.md` kaynağından `~/.claude/hooks/uretim_bol.py` ile üretilir; "
         "değişiklik kaynağa yapılır, parçalar oturum başında kendiliğinden yenilenir.")


def nfc(s):
    return unicodedata.normalize("NFC", s)


def etiket(ham):
    return {x for x in ETIKETLER if re.search(r"(?<![\w-])" + re.escape(x) + r"(?![\w-])", ham)}


def ayristir(metin):
    L = metin.split("\n")
    fm = re.match(r"^---\n(.*?)\n---\n", metin, re.S)
    surum = (re.search(r"^sürüm:\s*(\S+)", fm.group(1), re.M).group(1) if fm else "?")
    bolumler, kat, maddeler, i = {}, {}, [], 0
    b3 = None
    while i < len(L):
        l = L[i]
        m = re.match(r"^## (\d+)\. (.+)", l)
        if m:
            j = i + 1
            while j < len(L) and not re.match(r"^## \d+\. ", L[j]):
                j += 1
            bolumler[m.group(1)] = (l, i, j)
            if m.group(1) == "3":
                b3 = (i, j)
        i += 1
    i, son = b3
    kod = None
    while i < son:
        l = L[i]
        m = re.match(r"^### ([A-Z]{1,2})\. (.+)$", l)
        if m:
            kod = m.group(1)
            j = i + 1
            while j < son and not re.match(r"^#{1,4} ", L[j]) and not re.match(r"^---\s*$", L[j]):
                j += 1
            kat[kod] = {"baslik": m.group(2), "onsoz": "\n".join(L[i + 1:j]).strip("\n")}
            i = j
            continue
        m = re.match(r"^#### ([A-Z]{1,2}-\d+) · (.+)$", l)
        if m:
            j = i + 1
            while j < son and not re.match(r"^#{1,4} ", L[j]) and not re.match(r"^---\s*$", L[j]):
                j += 1
            p = [x.strip() for x in m.group(2).split(" · ")]
            maddeler.append({"id": m.group(1), "kat": kod, "ad": " · ".join(p[:-3]) if len(p) > 3 else p[0],
                             "onem": p[-3] if len(p) >= 4 else "", "zaman": p[-2] if len(p) >= 4 else "",
                             "ham": p[-1], "e": etiket(p[-1]), "metin": "\n".join(L[i:j]).rstrip("\n")})
            i = j
            continue
        i += 1
    return {"surum": surum, "L": L, "bolumler": bolumler, "kat": kat, "maddeler": maddeler}


def bas(ad, kimler, d, ozet):
    return (f"---\ntür: üretilmiş-parça\nkaynak: Kurallar/Üretim Kontrolü.md\nkaynak-sürüm: {d['surum']}\nkaynak-özet: {ozet}\n---\n\n"
            f"# Üretim Kontrolü: {ad}\n\n{UYARI}\n>\n> **Kimler okur:** {kimler}\n"
            "> **Nasıl okunur:** tamamını değil. Önce dizine bak; fazın kontrol kapısındaki kimliklerin metnini aşağıda bul. "
            "Profil, önem, aşama ve fazlara yayma kuralları [[Kurallar/Üretim Kontrolü/Yöntem|Yöntem]] notunda.\n")


def dizin_satiri(m, ayrica=""):
    s = f"| {m['id']} | {m['ad']} | {m['onem']} | {m['zaman']} | {m['ham']} |"
    return s + (f" {ayrica} |" if ayrica is not None else "")


def govde(d, grup, onsoz_ek=()):
    """Kategori başlığı + önsöz + madde metinleri. grup: sıralı madde listesi."""
    out, onceki = [], None
    katlar = list(dict.fromkeys([m["kat"] for m in grup] + list(onsoz_ek)))
    sira = list(d["kat"].keys())
    for k in sorted(katlar, key=sira.index):
        out.append(f"### {k}. {d['kat'][k]['baslik']}\n")
        if d["kat"][k]["onsoz"]:
            out.append(d["kat"][k]["onsoz"] + "\n")
        for m in grup:
            if m["kat"] == k:
                out.append(m["metin"] + "\n")
    return "\n".join(out)


def uret(d, ozet):
    dosyalar, yer = {}, {m["id"]: [] for m in d["maddeler"]}
    tur_uyeleri = {}
    for ad, kimler, haric, kademeler in TURLER:
        kalan = [m for m in d["maddeler"] if m["kat"] not in haric]
        gruplar = []
        for baslik, kosul in kademeler:
            g = [m for m in kalan if kosul(m["e"])]
            kalan = [m for m in kalan if m not in g]
            gruplar.append((baslik, g))
        tur_uyeleri[ad] = {m["id"] for _, g in gruplar for m in g}
        for i in tur_uyeleri[ad]:
            yer[i].append(ad)
        t = [bas(ad, kimler, d, ozet)]
        t.append(f"\n{sum(len(g) for _, g in gruplar)} madde. Her kademenin başlığı kimin için olduğunu söyler; projene uymayan kademeyi atla.\n")
        t.append("\n## Dizin\n")
        for n, (baslik, g) in enumerate(gruplar):
            if not g:
                continue
            t.append(f"\n**Kademe {chr(65 + n)} · {baslik}** ({len(g)} madde)\n\n| Kimlik | Madde | Önem | Zaman | Profil |\n|---|---|---|---|---|")
            t.extend(dizin_satiri(m, None) for m in g)
        for n, (baslik, g) in enumerate(gruplar):
            if g:
                t.append(f"\n---\n\n## Kademe {chr(65 + n)} · {baslik}\n\n" + govde(d, g))
        dosyalar[ad] = "\n".join(t).rstrip("\n") + "\n"
    for ad, kimler, secici, onsoz_ek in EKLER:
        g = [m for m in d["maddeler"] if secici(m)]
        for m in g:
            yer[m["id"]].append(ad)
        t = [bas(ad, kimler, d, ozet)]
        t.append(f"\n{len(g)} madde. \"Ayrıca\" sütunu maddenin hangi tür dosyasında da geçtiğini gösterir; onu okuduysan burada atla.\n")
        t.append("\n## Dizin\n\n| Kimlik | Madde | Önem | Zaman | Profil | Ayrıca |\n|---|---|---|---|---|---|")
        for m in g:
            ayr = ", ".join(a for a in tur_uyeleri if m["id"] in tur_uyeleri[a])
            t.append(dizin_satiri(m, ayr or "—"))
        t.append("\n---\n\n## Maddeler\n\n" + govde(d, g, onsoz_ek))
        dosyalar[ad] = "\n".join(t).rstrip("\n") + "\n"
    # Yöntem ve şablonlar: kaynak bölümleri harfi harfine
    def bolum(nolar):
        return "\n".join("\n".join(d["L"][d["bolumler"][n][1]:d["bolumler"][n][2]]).strip("\n-\n ") + "\n" for n in nolar if n in d["bolumler"])
    kafa = lambda ad, ne: (f"---\ntür: üretilmiş-parça\nkaynak: Kurallar/Üretim Kontrolü.md\nkaynak-sürüm: {d['surum']}\nkaynak-özet: {ozet}\n---\n\n"
                           f"# Üretim Kontrolü: {ad}\n\n{UYARI}\n>\n> {ne}\n\n")
    dosyalar["Yöntem"] = kafa("Yöntem", "Kaynağın 0, 1, 2, 7 ve 8. bölümleri: nasıl uygulanır, profiller, önem ve aşama, bakım, fazlara yayma. "
                              "Bir projede plan kurarken ya da faz kapısı yazarken okunur. \"Bu dosya\" ve \"Bölüm 3\" ifadeleri kaynağı, yani parça dosyalarındaki maddeleri kasteder.") + bolum(["0", "1", "2", "7", "8"])
    dosyalar["Şablonlar ve Komutlar"] = kafa("Şablonlar ve Komutlar", "Kaynağın 4, 5 ve 6. bölümleri: proje kural dosyası şablonu, "
                                             "`Kontrol.md` şablonu ve salt okunur tarama komutları. Yalnız gerektiğinde okunur.") + bolum(["4", "5", "6"])
    # Rehber
    r = [kafa("Rehber", "Hangi proje hangi parçayı okur. Kaynak dosyanın tamamı okunmaz.")]
    r.append("## Parçalar\n\n| Dosya | Kimler okur | Madde | Yaklaşık boyut |\n|---|---|---|---|")
    for ad, kimler, *_ in TURLER + EKLER:
        n = len(re.findall(r"^#### ", dosyalar[ad], re.M))
        r.append(f"| [[Kurallar/Üretim Kontrolü/{ad}\\|{ad}]] | {kimler} | {n} | {len(dosyalar[ad]) // 1000} bin karakter |")
    r.append(f"| [[Kurallar/Üretim Kontrolü/Yöntem\\|Yöntem]] | Plan kuran, faz kapısı yazan yönetici | — | {len(dosyalar['Yöntem']) // 1000} bin karakter |")
    r.append(f"| [[Kurallar/Üretim Kontrolü/Şablonlar ve Komutlar\\|Şablonlar ve Komutlar]] | Proje kural dosyası ya da denetim raporu yazan | — | {len(dosyalar['Şablonlar ve Komutlar']) // 1000} bin karakter |")
    r.append(f"\nKaynak: {len(d['maddeler'])} madde, {len(nfc(open(KAYNAK, encoding='utf-8').read())) // 1000} bin karakter (sürüm {d['surum']}).\n")
    r.append("""## Hangi proje neyi okur

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
""")
    dosyalar["Rehber"] = "\n".join(r)
    return dosyalar, yer


def ozet_al():
    return hashlib.sha1(open(KAYNAK, "rb").read() + open(__file__, "rb").read()).hexdigest()[:12]


def guncelle(zorla=False, yaz=True):
    """Kaynak ya da bu betik değiştiyse parçaları yeniden yazar. (değişti_mi, rapor) döndürür."""
    ozet = ozet_al()
    rehber = os.path.join(HEDEF, "Rehber.md")
    if not zorla and yaz and os.path.isfile(rehber):
        with open(rehber, encoding="utf-8") as f:
            if f"kaynak-özet: {ozet}" in f.read(400):
                return False, "güncel"
    d = ayristir(nfc(open(KAYNAK, encoding="utf-8").read()))
    dosyalar, yer = uret(d, ozet)
    acikta = [i for i, v in yer.items() if not v]
    rapor = [f"kaynak sürüm {d['surum']} · {len(d['maddeler'])} madde · {len(dosyalar)} dosya"]
    for ad, t in dosyalar.items():
        rapor.append(f"  {ad:34}{len(re.findall(r'^#### ', t, re.M)):4} madde {len(t) // 1000:4} bin karakter")
    rapor.append("Hiçbir parçada olmayan madde: " + (", ".join(acikta) if acikta else "yok"))
    if acikta:
        return False, "\n".join(rapor) + "\nHATA: kapsam eksik, dosyalar yazılmadı."
    if yaz:
        os.makedirs(HEDEF, exist_ok=True)
        for eski in os.listdir(HEDEF):
            if eski.endswith(".md") and nfc(eski[:-3]) not in dosyalar:
                os.remove(os.path.join(HEDEF, eski))
        for ad, t in dosyalar.items():
            with open(os.path.join(HEDEF, ad + ".md"), "w", encoding="utf-8") as f:
                f.write(t)
    return True, "\n".join(rapor)


def parcalar(plan):
    """Plan.md metninden projenin okuması gereken parça dosyalarının yollarını çıkarır."""
    plan = nfc(plan)
    ia = re.search(r"\*\*İş akışı:\*\*\s*(.+)", plan)
    ia = ia.group(1) if ia else ""
    bas_ = "\n".join(plan.split("\n")[:20])
    prof = " ".join(l for l in bas_.split("\n") if re.search(r"Üretim kontrolü|\*\*Profil", l))
    e = etiket(prof)
    tur = []
    if "Web ve Sunucu" in ia or e & {"WEB-S", "WEB-API"}:
        tur.append("Web")
    android = bool(re.search(r"Android", ia + prof))
    if "Apple Uygulaması" in ia:
        tur.append("Apple")
    if android:
        tur.append("Android")
    if "Oyun" in ia or "OYUN" in e:
        tur.append("Oyun")
    if "Araç ve MCP" in ia or "ARAÇ" in e:
        tur.append("Araç")
    ek = []
    if "MAĞAZA" in e:
        ek.append("Ek - Mağaza")
        if "Apple" in tur or (not android and "Oyun" in tur):
            ek.append("Ek - Apple İncelemesi")
        if android:
            ek.append("Ek - Google Play İncelemesi")
        ek.append("Ek - Mağaza Sayfası ve Büyüme")
    if "GELİR" in e:
        ek.append("Ek - Gelir")
    if "YZ" in e:
        ek.append("Ek - Yapay Zekâ")
    return [os.path.join(HEDEF, a + ".md") for a in tur], [os.path.join(HEDEF, a + ".md") for a in ek], bool(prof)


if __name__ == "__main__":
    degisti, rapor = guncelle(zorla="--zorla" in sys.argv, yaz="--denetle" not in sys.argv)
    print(rapor)
    sys.exit(1 if "HATA" in rapor else 0)
