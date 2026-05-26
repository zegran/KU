# IJPVP — Resmi Referans Dosyası (Single Source of Truth)

> **🔒 FROZEN — v2, 2026-05-26 (yazar destekli ek kaynak verisi) — yazar onayı olmadan değiştirilmez.**
>
> Bu dosya tamamlandıktan sonra CLI bir daha IJPVP için web araması yapmaz; her IJPVP sorusunda yalnızca bu dosya `view` edilir. Eksik veya çelişkili kayıtlar ⚠ ile işaretlenmiştir ve yazar tarafından manuel doğrulanmalıdır.
>
> **v1 → v2 delta:** quartile kesinleşti (Q1/Q1), scope genişledi, article type listesi + tam makale kelime limiti eklendi, keywords kuralı düzeltildi, highlights kuralı netleşti, Editorial Manager URL doğrulandı. v1 yedeği: `Docs/refs/archive/IJPVP_official_sources_v1.md`.

---

## 1. Bibliyografik Bilgi

| Alan | Değer | Kaynak |
|---|---|---|
| Tam ad | International Journal of Pressure Vessels and Piping | [1][2][3] |
| Print ISSN | 0308-0161 | [2][3] |
| Electronic ISSN | 1879-3541 | [3] |
| Yayıncı | Elsevier (Elsevier Sci Ltd) | [1][2][3] |
| Yayın sıklığı | Aylık (monthly) | [2][3][13] |
| Yayın başlangıç yılı | 1972 | [3] |
| Yıllık makale hacmi | ⚠ Çelişki: 241 [2][13] vs 212 [3] — kaynak yöntemleri farklı (yayın yılı vs takvim yılı olabilir) | [2][3][13] |
| Dil | İngilizce | [3] |
| Indexing | SCIE, Scopus | [2][13] |
| Resmi journal sayfası | https://www.journals.elsevier.com/international-journal-of-pressure-vessels-and-piping | [17] |

---

## 2. Quartile ve Metrikler

### Quartile (v2'de KESİNLEŞTİ → **Q1 / Q1**)

LetPub doğrudan WoS JCR verisini [13] esas aldı.

| Sıralama | Kategori | Sıra | Quartile | Kaynak |
|---|---|---|---|---|
| **JIF** (Journal Impact Factor) | Engineering, Mechanical | 44 / 182 | **Q1** | [13] |
| **JIF** | Engineering, Multidisciplinary | 36 / 179 | **Q1** | [13] |
| **JCI** (Journal Citation Indicator) | Engineering, Mechanical | 38 / 184 | **Q1** | [13] |
| **JCI** | Engineering, Multidisciplinary | 40 / 179 | **Q1** | [13] |

> **Karar:** IJPVP, JCR'a göre **her iki kategoride de Q1** dergidir.

> ⚠ **OOIR [4] Q2 kaydı eski/yanlış sınıflama olarak işaretlenmiştir.** LetPub'ın WoS JCR doğrudan yansıması [13] esas alınmıştır. Manuel JCR teyidi opsiyonel.

### Diğer metrikler

| Metrik | Değer | Yıl | Kaynak |
|---|---|---|---|
| Impact Factor (Web of Science) | 3.500 | 2024 | [4][13] |
| H4-Index (2022–2026) | 27 | 2026 | [4] |
| Ortalama atıf | 7.135 | 4-yıl penceresi | [4] |
| Medyan atıf | 4 | 4-yıl penceresi | [4] |
| TQCC | 9 | 4-yıl penceresi | [4] |
| 4-yıl yayın hacmi | 926 makale | 2022–2026 | [4] |
| Self-citation oranı | %11.40 | 2024–2025 | [2] |
| Gold OA oranı | %5.88 | — | [2] |

### CiteScore çelişkisi (⚠ KORUNAN)
| Kaynak | CiteScore | Yıl |
|---|---|---|
| LetPub [2] | 6 | belirsiz |
| Researcher.life [3] | 3.7 | belirsiz |

> ⚠ CiteScore tutarsız — Scopus CiteScore sayfasından manuel doğrulanmalı.

---

## 3. Scope ve İstisnalar (v2'de GENİŞLE)

### Tematik kapsam (paraphrase, LetPub güncel verisi [13])

Dergi aşağıdaki konuları kapsar:

- Basınçlı kap mühendisliği (genel)
- Yapısal bütünlük değerlendirmesi
- Tasarım yöntemleri
- Kod ve standartlar
- Üretim ve kaynak (additive manufacturing dahil)
- Malzeme davranışı
- Denetim
- Bakım, ömür uzatımı ve yaşlanma yönetimi
- Ömür yönetimi
- **Makine öğrenmesi uygulamaları** (basınçlı ekipman alanında)

**Sektörel kapsam:** enerji, petrokimya, proses endüstrisi, ulaşım, havacılık [13].

**Editör vurgusu (paraphrase):** Dergi, ekonomi, güvenilirlik veya kullanım ömründe büyük iyileştirmeye yol açan **pratik uygulama** odaklı çalışmalara öncelik verir [13].

### Tezin kapsam-uyumu (revize)
Tezde işlenen konular kapsamla **çok yönlü ve doğrudan** örtüşür:
- API 5L X70 doğalgaz boru hatları (basınçlı ekipman, yapısal bütünlük)
- Ripple/wrinkle defektleri (geometrik kusur kaynaklı SCF) — dergi tekrarlı konusu
- Markl + rainflow + Miner yorulma (basınç çevrimi altında ömür yönetimi)
- ASME B31.8 + CSA Z662 + API 5L (kod/standart tabanlı metodoloji)
- **Fitness-for-service framing** ⇒ editör vurgusu olan "pratik uygulama, kullanım ömrü iyileştirme" hedefiyle birebir aynı yörüngede

**Dergideki son yayınlardan konu komşusu örnekler:**
- 2025: kompozit yama onarımı + deneysel doğrulama (Vol. 215) [5]
- yerel cidar incelmesi olan borularda FEA tabanlı SCF [6]
- değişken cidar kalınlığındaki butt kaynaklarda SCF analizi [7]
- boru hatlarında wrinkle bends gerilme analizi [8]

### İstisnalar / sınırlamalar
- **Fluid dynamics:** Salt akışkan dinamiği çalışmaları kapsam dışı. Akışkan dinamiği yalnızca **fluid-structure interaction (akışkan-yapı etkileşimi)** içeren çalışmalarda kabul edilir [14].

> ⚠ Resmi scope statement (verbatim) ScienceDirect 403 nedeniyle çekilemedi. Yukarıdaki paraphrase LetPub güncel verisi [13] ve search snippet [14] üzerinden derlenmiştir. Tam verbatim için yazar dergi ana sayfasını [17] ziyaret edebilir.

---

## 4. Article Type Listesi ve Kelime Limitleri (v2'de KISMİ ÇÖZÜLDÜ)

### Kabul edilen makale türleri [14]
1. Original articles (tam araştırma makalesi)
2. Short communications
3. Review articles
4. Book reviews
5. Technical notes
6. Letters to the Editors
7. Technical news items
8. Review reports

### Kelime limitleri

| Article type | Limit | Kaynak |
|---|---|---|
| **Original article (tam makale)** | **maksimum 6.000 kelime / yaklaşık 12 basılı sayfa** | [14] |
| Short communication | ⚠ kaynakta tam sayı bulunamadı | — |
| Review article | ⚠ kaynakta tam sayı bulunamadı | — |
| Technical note | ⚠ kaynakta tam sayı bulunamadı | — |
| Diğer türler (book review, letter, news, review report) | ⚠ kaynakta tam sayı bulunamadı | — |

### Tezin hedef tipi
**Original article (6.000 kelime / ~12 sayfa).** Önceki execution planında §1–§8 toplam tahsisi **~7.300 kelime** idi → **6.000'e düşürmek gerek**. WP1'de bölüm-başı kelime tahsisleri buna göre revize edilecek.

---

## 5. Manuscript Yapısı

### Tipik yapı (komşu yayınlardan + Elsevier mech-eng normundan)
1. Title
2. Author list + affiliations
3. Abstract (yapılandırılmamış)
4. Keywords
5. Introduction
6. Background / Literature / Theory
7. Methodology / Numerical model
8. Results
9. Discussion
10. Conclusions
11. Declarations
12. References
13. (Opsiyonel) Appendices / Supplementary

> ⚠ **Abstract kelime limiti** kesin sayı ve yapılandırılmış/yapılandırılmamış durumu resmi sayfadan teyit edilmemiştir. Elsevier mech-eng normunda 150–250 kelime yapılandırılmamış olağandır.

### Bölüm beklentileri
- Introduction: motivasyon + literatür açığı + amaç
- Methodology: reproducible detay (mesh, BC, malzeme, yazılım versiyonu, varsayımlar)
- Results: rakamsal, tablo + figür destekli
- Discussion: sınırlamalar zorunlu
- Conclusions: kısa, madde madde

---

## 6. Şekil ve Tablo Politikası

> Elsevier'in genel artwork standardı uygulanır.

| Öğe | Norm |
|---|---|
| Renkli şekil | Online'da ücretsiz |
| Çözünürlük | Line art ≥1000 dpi, halftone ≥300 dpi, combo ≥500 dpi |
| Format | TIFF / EPS / PDF tercih; PNG/JPG kabul |
| Caption stili | Şekil altında, "Fig. N. ..." başlangıçlı |
| Tablo caption | Tablo üstünde, "Table N. ..." |
| Genişlik | Tek sütun ~90 mm; çift sütun ~190 mm |

> ⚠ IJPVP-özel artwork kuralı varsa Elsevier Artwork Quality Specifications sayfasından doğrulanmalı.

---

## 7. Referans Stili: Elsevier Numbered (Style 1)

Elsevier Standard Reference Styles dokümanından paraphrase edilmiştir [9].

### Metin-içi atıf
- Köşeli parantez içinde sayı ile: `[3]`, `[6]`, `[3, 6]`
- Yazar adı kullanılabilir: `Barnaby ve Jones [8]`
- Sıralama: metinde göründüğü sıraya göre

### Referans liste formatı (örnek tipler)

**Dergi makalesi (peer-reviewed):**
Yazarlar, başlık, dergi adı, cilt (sayı) (yıl) sayfalar.

**Konferans bildirisi:**
Yazarlar, başlık, in: editörler (Eds.), tam konferans adı, yer, tarihler, dergi/yayıncı, yıl, sayfalar.

**Kitap:**
Yazarlar, başlık, baskı bilgisi, yayıncı, yer, yıl (gerekli ise bölüm).

**Kitap bölümü:**
Yazarlar, bölüm başlığı, in: editör (Ed.), kitap başlığı, yayıncı, yer, yıl, sayfalar.

**DOI'li makale:**
Standart format + ekinde `doi:10.xxxx/yyyy`.

**Web referansı:**
Kurum, başlık, <URL>, yıl (accessed dd.mm.yy).

### Genel kurallar
- "in press" yalnızca kabul edilmiş makaleler için
- Yayımlanmamış sonuçlar ve kişisel iletişim listeye konulmaz
- Web referansları için URL + erişim tarihi zorunlu
- Atıfta tutarlılık: metin ↔ liste eşleşmeli

> Yerel kopya: `Docs/refs/pdfs/elsevier_references_style_guide.pdf` [9]

---

## 8. Frontmatter Zorunlulukları (v2'de KESİNLEŞTİ)

| Öğe | Durum | Norm |
|---|---|---|
| Title | Zorunlu | Kısa, spesifik |
| Author list + affiliations | Zorunlu | ORCID önerilir |
| **Highlights** | **Zorunlu** | 3–5 madde · her biri ≤85 karakter (boşluk dahil) · ayrı editable dosya · dosya adında "Highlights" geçmeli · novel sonuç + yeni yöntem yakalamalı [15] |
| Abstract | Zorunlu | Yapılandırılmamış (Elsevier mech-eng normu); ⚠ kesin kelime sayısı manuel doğrulama |
| **Keywords** | Zorunlu | **1–7 adet** · İngilizce · "and", "of" gibi bağlaçlı çok kelimeli ifadelerden kaçınılmalı · sadece yerleşik kısaltmalar kullanılabilir [14] |
| Graphical abstract | Önerilen (zorunlu değil) | Tek panel görsel |
| CRediT author statement | Zorunlu | Yazar rolleri açıkça belirtilir |
| Declarations | Zorunlu | Funding · Conflict of Interest · Data Availability · Ethical approval (uygunsa) |
| Acknowledgements | Opsiyonel | Funding ayrı bölümde |

> **Önemli düzelti:** v1'de keywords "5–7" yazılmıştı; doğrusu **1–7**. v1'de highlights için "≤85 karakter" genel Elsevier normu olarak gösterilmişti; v2'de IJPVP-spesifik koşul olarak [15] kaynağıyla teyitli.

---

## 9. Submission Süreci (v2'de DOĞRULANDI)

### Submission portalı (yeni eklendi)
- **Editorial Manager:** https://www.editorialmanager.com/IPVP [16]
- **Resmi journal sayfası:** https://www.journals.elsevier.com/international-journal-of-pressure-vessels-and-piping [17]

### Peer review
- Single anonymized review (Elsevier mech-eng standardı)
- ⚠ Ortalama review süresi: LetPub'da "~24 ay" [2] ifadesi olağandışı yüksek — manuel teyit gerek

### Appeal süreci
- Red kararına itiraz mümkün; editöre formal yazı + gerekçe
- ⚠ Spesifik IJPVP appeal politikası kaynaklarda detaylandırılmadı

### Open Access
- Open access seçeneği mevcut [2]
- ⚠ APC ücreti kaynaklarda yok — Elsevier OA pricelist'ten teyit

### Special issue
- Dergi periyodik olarak special issue yayımlar [1]
- ⚠ Aktif çağrı listesi manuel teyit gerek

---

## 10. Kaynak Haritası

| [n] | Açıklama | URL | Erişim |
|---|---|---|---|
| [1] | IJPVP ScienceDirect ana sayfa | https://www.sciencedirect.com/journal/international-journal-of-pressure-vessels-and-piping | ⚠ HTTP 403 |
| [2] | LetPub IJPVP detay (Q1, CiteScore 6, ~241 art/yıl, 24-ay review) | https://www.letpub.com/index.php?journalid=3860&page=journalapp&view=detail | ✅ Çekildi |
| [3] | Researcher.life IJPVP (CiteScore 3.7, 212 art 2025) | https://researcher.life/journal/international-journal-of-pressure-vessels-and-piping/9578 | ✅ Çekildi |
| [4] | OOIR IJPVP (IF 3.500/2024, H4 27) | https://ooir.org/j.php?issn=0308-0161 | ✅ Çekildi |
| [5] | IJPVP 2025 makale (kompozit yama) | https://www.sciencedirect.com/science/article/abs/pii/S0308016125000249 | Künye teyitli |
| [6] | Yerel cidar incelmesi SCF makalesi | https://www.sciencedirect.com/science/article/abs/pii/S0308016104001322 | Künye teyitli |
| [7] | Butt weld değişken cidar SCF makalesi | https://www.sciencedirect.com/science/article/abs/pii/S0308016120300533 | Künye teyitli |
| [8] | Wrinkle bends stress analizi | https://www.sciencedirect.com/science/article/abs/pii/0263823193900197 | Künye teyitli |
| [9] | Elsevier Numbered Reference Style | Lokal: `Docs/refs/pdfs/elsevier_references_style_guide.pdf` | ✅ Local |
| [10] | Elsevier Copyediting Specification v3.6 | Lokal: `Docs/refs/pdfs/elsevier_copy_editing_style.pdf` | ✅ Local |
| [11] | Booksite Elsevier reference styles | (link ölü 404) | ❌ |
| [12] | Elsevier shop IJPVP journal page | https://shop.elsevier.com/journals/international-journal-of-pressure-vessels-and-piping/0308-0161 | ⚠ Çekilmedi |
| **[13]** | **LetPub IJPVP profil (WoS JCR JIF/JCI Q1/Q1, 2026-05-26 tam içerik)** | LetPub journalid 3860 ek-veri çekimi | ✅ Yazar destekli |
| **[14]** | **ScienceDirect Guide for Authors snippet (article types, 6.000 kelime, fluid-solid interaction, keywords 1–7)** | sciencedirect.com Guide for Authors (search excerpt) | ⚠ Sayfa 403, snippet yazar tarafından sağlandı |
| **[15]** | **Elsevier Highlights resmi rehberi (3–5 bullet, ≤85 char, ayrı dosya)** | Elsevier journal-authors highlights guide | ✅ Norm |
| **[16]** | **Editorial Manager IJPVP submission portalı** | https://www.editorialmanager.com/IPVP | ✅ URL doğrulandı |
| **[17]** | **Resmi Elsevier journal sayfası (IJPVP)** | https://www.journals.elsevier.com/international-journal-of-pressure-vessels-and-piping | ✅ URL doğrulandı |

---

## İndirilen Yerel Dosyalar (`Docs/refs/pdfs/`)

| Dosya | Boyut | Durum |
|---|---|---|
| `elsevier_references_style_guide.pdf` | 470 KB | ✅ |
| `elsevier_copy_editing_style.pdf` | 660 KB | ✅ |

---

## ⚠ Korunan Eksik Maddeler (v2 sonu — 9 madde)

v1'de 10 ⚠ vardı; v2'de **6 madde çözüldü, 5 yeni eklenmedi** → **9 ⚠ kaldı.**

| # | Eksik | Çözüm yolu |
|---|---|---|
| 1 | **CiteScore** çelişkisi (3.7 vs 6) | Scopus CiteScore sayfası |
| 2 | **Abstract kelime limiti** kesin sayı + yapılandırılmış/yapılandırılmamış durumu | Guide for Authors |
| 3 | **Article type kelime limitleri** (tam makale dışındakiler — short comm., review, technical note, vb.) | Guide for Authors |
| 4 | **Peer review türü ve süresi** (24 ay olağandışı) | Dergi son makalelerinin received/accepted tarihleri |
| 5 | **OA APC ücreti** | Elsevier OA pricelist |
| 6 | **Aktif special issue çağrıları** | Elsevier IJPVP special issues sayfası |
| 7 | **Highlights/CRediT IJPVP-özel sapması** (varsa) | Guide for Authors |
| 8 | **Yıllık makale sayısı** (212 vs 241) | Dergi/Scopus istatistikleri |
| 9 | **Resmi scope statement verbatim** | ScienceDirect IJPVP ana sayfası |

### v1 → v2 ⚠ Çözüm İzleme

| v1'deki ⚠ | v2'deki durumu |
|---|---|
| CiteScore çelişkisi | ⚠ Hâlâ açık (#1) |
| Engineering Multidisciplinary quartile (Q1 vs Q2) | ✅ Çözüldü — Q1 (LetPub JCR [13]) |
| Article type listesi + kelime limitleri | 🟡 Kısmi çözüldü — liste tam, tam makale 6k kelime; diğer tipler hâlâ ⚠ (#3) |
| Resmi scope statement (verbatim) + istisnalar | 🟡 Kısmi çözüldü — istisna (fluid-solid interaction) eklendi; verbatim hâlâ ⚠ (#9) |
| Abstract kelime limiti | ⚠ Hâlâ açık (#2) |
| Highlights/CRediT IJPVP-spesifik kuralları | 🟡 Kısmi — highlights detayı netleşti [15]; CRediT özel sapma hâlâ ⚠ (#7) |
| Peer review türü ve süresi | ⚠ Hâlâ açık (#4) |
| Submission Editorial Manager URL | ✅ Çözüldü — https://www.editorialmanager.com/IPVP |
| OA APC ücreti | ⚠ Hâlâ açık (#5) |
| Aktif special issue çağrıları | ⚠ Hâlâ açık (#6) |

**Çözülenler:** 4 tam çözüm (Eng. Multi quartile, Editorial Manager URL, scope istisna, highlights detay) + 2 kısmi (article types, highlights).
**Yeni eklenmedi.**
**Net hareket:** 10 → 9 ⚠.

---

## Kullanım Kuralları

1. Bu dosya FROZEN — yazar "v3 olarak güncelle" demeden değiştirilmez
2. IJPVP ile ilgili her CLI işleminde önce bu dosya `view` edilir
3. Yeni web araması yasak — bilgi yoksa ⚠ olarak işaretle veya yazardan iste
4. Çelişki tespit edilirse → bu dosyaya yazma, yazara bildir

---

## Sürüm
- **v1 — 2026-05-26** — İlk derleme; arşivde: `Docs/refs/archive/IJPVP_official_sources_v1.md`
- **v2 — 2026-05-26** — Yazar destekli ek kaynak verisiyle güncelleme; Q1/Q1 kesinleşti, scope genişledi, article types + 6k kelime limiti eklendi, keywords 1–7 düzeltildi, highlights kuralı netleşti, Editorial Manager URL doğrulandı
