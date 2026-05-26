# IJPVP — Resmi Referans Dosyası (Single Source of Truth)

> **🔒 FROZEN — son güncelleme: 2026-05-26 — yazar onayı olmadan değiştirilmez.**
>
> Bu dosya tamamlandıktan sonra CLI bir daha IJPVP için web araması yapmaz; her IJPVP sorusunda yalnızca bu dosya `view` edilir. Eksik veya çelişkili kayıtlar ⚠ ile işaretlenmiştir ve yazar tarafından manuel doğrulanmalıdır.

---

## 1. Bibliyografik Bilgi

| Alan | Değer | Kaynak |
|---|---|---|
| Tam ad | International Journal of Pressure Vessels and Piping | [1][2][3] |
| Print ISSN | 0308-0161 | [2][3] |
| Electronic ISSN | 1879-3541 | [3] |
| Yayıncı | Elsevier (Elsevier Sci Ltd) | [1][2][3] |
| Yayın sıklığı | Aylık (monthly) | [2][3] |
| Yayın başlangıç yılı | 1972 | [3] |
| Yıllık makale hacmi | 2025'te ~212–241 arası (kaynaklara göre değişiyor) | [2][3] |
| Dil | İngilizce (multi-language tag ile birlikte) | [3] |
| Indexing | SCIE, Scopus | [2] |

---

## 2. Quartile ve Metrikler

| Metrik | Değer | Yıl | Kaynak |
|---|---|---|---|
| Impact Factor (Web of Science) | **3.500** | 2024 | [4] |
| H4-Index (2022–2026) | 27 | 2026 | [4] |
| Ortalama atıf | 7.135 | 4-yıl penceresi | [4] |
| Medyan atıf | 4 | 4-yıl penceresi | [4] |
| TQCC | 9 | 4-yıl penceresi | [4] |
| 4-yıl yayın hacmi | 926 makale | 2022–2026 | [4] |
| Self-citation oranı | %11.40 | 2024–2025 | [2] |
| Gold OA oranı | %5.88 | — | [2] |

### Quartile (kategori-bazlı)

| Kategori | Sıra | Quartile | Kaynak |
|---|---|---|---|
| Engineering, Mechanical | 29 / 125 | **Q1** | [4] |
| Engineering, Multidisciplinary | 25 / 74 | **Q2** | [4] |

> ⚠ **Çelişki:** LetPub [2] her iki kategoride de Q1 raporluyor; OOIR [4] (JCR temelli) Engineering Multidisciplinary için Q2 veriyor. **OOIR esas alınmıştır** çünkü doğrudan JCR sıralamasını yansıtıyor. Yazar isterse Clarivate JCR'den manuel doğrulayabilir.

### CiteScore çelişkisi

| Kaynak | CiteScore | Not |
|---|---|---|
| LetPub [2] | 6 | Yıl belirtilmemiş |
| Researcher.life [3] | 3.7 | Yıl belirtilmemiş |

> ⚠ **CiteScore kaynaklarda tutarsız.** Resmi Scopus CiteScore sayfasından manuel doğrulanması önerilir.

---

## 3. Scope ve İstisnalar

### Tematik kapsam (paraphrase)
Dergi, basınç altında çalışan ekipmanın yapısal bütünlüğü, tasarım yöntemleri, üretim, malzeme davranışı, denetim, bakım ve servis ömrünün uzatılması konularını işler. Sektörel kapsam enerji, petrokimya ve havacılık alanlarını içerir [2].

Yayın motiflerinin yoğunlaştığı alanlar: yapısal mühendislik, sonlu elemanlar yöntemi, basınçlı kap analizi, kompozit malzeme uygulamaları, kaynaklı bağlantılar [1].

### Bu tezin kapsam-uyumu
Tezde işlenen konular kapsamla **doğrudan örtüşür:**
- API 5L X70 doğalgaz boru hatları (basınç altında yapısal bütünlük)
- Ripple/wrinkle defektleri (geometrik kusur kaynaklı SCF — derginin tekrarlı yayın konusu)
- Markl + rainflow + Miner yorulma (basınç çevrimi altında ömür tahmini)
- ASME B31.8 + CSA Z662 + API 5L standartlarına dayalı metodoloji (fitness-for-service)

**Dergideki son yayınlar konu komşusu örnekleri (referans):**
- 2025 makale: kompozit yama onarımı + deneysel doğrulama (Vol. 215) [5]
- Geçmiş: yerel cidar incelmesi olan borularda FEA tabanlı SCF [6]
- Geçmiş: değişken cidar kalınlığındaki butt kaynaklarda SCF analizi [7]
- Geçmiş: boru hatlarında wrinkle bends gerilme analizi [8]

> ⚠ **Resmi scope statement (verbatim) ScienceDirect üzerinden erişilemedi (HTTP 403).** Yukarıdaki paraphrase ikincil kaynaklara dayanmaktadır. Yazar dergi sayfasından manuel teyit edebilir [1].

### İstisna / sınırlama
> ⚠ Resmi scope sayfasından (örn. fluid dynamics çalışmalarının fluid-solid interaction içerme zorunluluğu gibi) açık istisna ifadeleri **bu kaynaklardan teyit edilemedi**. Manuel doğrulama önerilir.

---

## 4. Article Type Listesi ve Kelime Limitleri

| Article type | Kelime limiti | Not |
|---|---|---|
| Research article (tam makale) | ⚠ kaynakta net bulunamadı — tipik Elsevier mech-eng normu **6.000–10.000 kelime** | Yazar dergi sayfasından manuel doğrulamalı |
| Review article | ⚠ kaynakta bulunamadı | — |
| Short communication / technical note | ⚠ kaynakta bulunamadı | — |
| Editorial / commentary | ⚠ kaynakta bulunamadı | — |

> ⚠ **Article type ve kelime limitleri ScienceDirect Guide for Authors sayfasında olmalı ama HTTP 403 nedeniyle çekilemedi.** Yazar dergi sayfasını manuel inceleyip bu satırları kesinleştirmeli.

---

## 5. Manuscript Yapısı

### Tipik yapı (komşu yayınlardan + Elsevier mech-eng normundan)
1. Title
2. Author list + affiliations
3. Abstract (yapılandırılmamış, ~150–250 kelime — tipik Elsevier normu)
4. Keywords (5–7)
5. Introduction
6. Background / Literature / Theory
7. Methodology / Numerical model
8. Results
9. Discussion
10. Conclusions
11. Declarations
12. References
13. (Opsiyonel) Appendices / Supplementary

> ⚠ **Abstract kelime limiti** resmi Guide for Authors sayfasından doğrudan teyit edilemedi. Elsevier mech-eng dergilerinde 150–250 kelime norm.

### Bölüm beklentileri
- Introduction: motivasyon + literatür açığı + amaç
- Methodology: reproducible detayda (mesh, BC, malzeme, yazılım versiyonu, varsayımlar)
- Results: rakamsal, tablo + figür destekli
- Discussion: sınırlamalar zorunlu — derginin önemsediği alanlardan biri
- Conclusions: kısa, madde madde tercih edilir

---

## 6. Şekil ve Tablo Politikası

> ⚠ **Detaylı şekil/tablo policy** Elsevier Artwork Guide sayfasındadır; bu turda doğrudan çekilemedi. Aşağıdaki maddeler Elsevier'in standart yayın normudur ve IJPVP için de geçerlidir.

| Öğe | Norm |
|---|---|
| Renkli şekil | Online'da ücretsiz; basılı sürümde değişebilir |
| Çözünürlük | Line art ≥1000 dpi, halftone ≥300 dpi, combo ≥500 dpi (Elsevier standardı) |
| Format | TIFF / EPS / PDF tercih (vektör); PNG/JPG kabul |
| Caption stili | Şekil altında, "Fig. N. ..." başlangıçlı, kısa cümle + açıklama |
| Tablo caption | Tablo üstünde, "Table N. ..." |
| Genişlik | Tek sütun ~90 mm; çift sütun ~190 mm |

> ⚠ Yazar Elsevier "Artwork Quality Specifications" sayfasından manuel doğrulamalı.

---

## 7. Referans Stili: Elsevier Numbered (Style 1)

Elsevier Standard Reference Styles dokümanından paraphrase edilmiştir [9].

### Metin-içi atıf
- Köşeli parantez içinde sayı ile gösterilir: `[3]`, `[6]`, `[3, 6]`
- Yazar adı kullanılabilir: `Barnaby ve Jones [8]`
- Atıf sırası metinde göründüğü sıraya göre numaralandırılır

### Referans liste örnekleri (her tür için bir örnek)

**Dergi makalesi (peer-reviewed):**
```
[1] A. Paivio, B. Jansen, L.J. Becker, Comparisons through the mind's eye, Cognition 37 (2) (1975) 635–647.
```

**Konferans bildirisi (proceedings):**
```
[4] N. Yasuda, S. Takagi, A. Toriumi, Spectral shape analysis of infrared absorption, in: T. Hattori, K. Wada, A. Hiraki (Eds.), Proc. 2nd Int. Symp. Control of Semiconductor Interfaces, ISCSI-2, Karuizawa, Japan, October 28–November 1, 1997, Appl. Surf. Sci. 117–118 (1997) 216–220.
```

**Kitap (tek yazar / editörlü):**
```
[9] W. Strunk Jr., E.B. White, The Elements of Style, third ed., MacMillan, New York, 1979 (Chapter 4).
```

**Kitap bölümü:**
```
[13] T.E. Chaddock, Gastric emptying of a nutritionally balanced liquid diet, in: E.E. Daniel (Ed.), Proc. 4th Int. Symp. Gastrointestinal Motility, ISGM4, 4–8 September 1973, Seattle, WA, Mitchell Press, Vancouver, 1974, pp. 83–92.
```

**Rapor / teknik doküman:**
```
[10] College Bound Seniors, College Board Publications, Princeton, NJ, 1979.
```

**Web referansı:**
```
[20] Cancer Research UK, Cancer statistics reports for the UK,
<http://www.cancerresearchuk.org/aboutcancer/statistics/cancerstatsreport/>, 2003 (accessed 13.03.03).
```

**DOI'li makale:**
```
[8] J.C. VanDecar et al., Aseismic continuation of the Lesser Antilles slab, J. Geophys. Res. 108 (2003) 2043, doi:10.1029/2001JB000884.
```

### Genel kurallar
- Yayın evresi: "in press" yalnızca kabul edilmiş makaleler için
- Yayımlanmamış sonuçlar ve kişisel iletişim referans listesine **konulmaz**, metin içinde belirtilir
- Web referansları için URL + erişim tarihi zorunlu
- Atıfta tutarlılık: metinde her atıf listede olmalı; listede yer alan her kayıt metinde atıfta olmalı

---

## 8. Frontmatter Zorunlulukları

| Öğe | Durum | Norm |
|---|---|---|
| Title | Zorunlu | Kısa, spesifik; tipik ≤15 kelime |
| Author list + affiliations | Zorunlu | ORCID önerilir |
| Highlights | **Zorunlu** (Elsevier standart) | 3–5 madde, her biri ≤85 karakter (boşluk dahil) |
| Abstract | Zorunlu | Yapılandırılmamış (Elsevier mech-eng normu) |
| Keywords | Zorunlu | 5–7 anahtar kelime |
| Graphical abstract | **Önerilen** (zorunlu değil) | Tek panel görsel, kısa ve okunabilir |
| CRediT author statement | **Zorunlu** (Elsevier standart) | Yazar rolleri açıkça belirtilir |
| Declarations | Zorunlu | Funding · Conflict of Interest · Data Availability · Ethical approval (uygunsa) |
| Acknowledgements | Opsiyonel | Funding ayrı bölümde |

> ⚠ Highlights kelime/karakter sınırı, graphical abstract ölçüleri ve CRediT şablonu Elsevier'in standart normudur ama IJPVP'nin özel kuralı varsa manuel doğrulanmalı.

---

## 9. Submission Süreci

### Peer review
- Single anonymized review (Elsevier mech-eng standardı; IJPVP için manuel doğrulanmalı ⚠)
- Ortalama review süresi: ⚠ Tek bir kaynak [2] "~24 ay" demiş ama bu **olağandışı yüksek**; tipik Elsevier mech-eng dergisi 8–16 haftadır. **Manuel teyit gerekli.**

### Submission portalı
- Editorial Manager (Elsevier standart)
- IJPVP submission URL: ⚠ doğrudan teyit edilmedi (ScienceDirect 403). Editorial Manager link'i Guide for Authors sayfasında verilir

### Appeal süreci
- Red kararına itiraz mümkün; editöre formal yazı + gerekçe
- ⚠ Spesifik IJPVP politika maddesi bu kaynaklardan teyit edilemedi

### Open Access
- Open access seçeneği mevcut [2]
- APC: bu kaynaklarda belirtilmemiş ⚠ — manuel teyit (Elsevier IJPVP OA APC sayfası)

### Special issue
- Dergi periyodik olarak special issue yayımlar; çağrılar Elsevier'in IJPVP special issues sayfasında listelenir [1]
- Şu an aktif çağrı kontrolü gerek ⚠

---

## 10. Kaynak Haritası

| [n] | Açıklama | URL | Erişim |
|---|---|---|---|
| [1] | IJPVP ScienceDirect ana sayfa | https://www.sciencedirect.com/journal/international-journal-of-pressure-vessels-and-piping | ⚠ HTTP 403 — manuel ziyaret |
| [2] | LetPub IJPVP detay sayfası (Q1, CiteScore 6, ~241 art/yıl, 24-ay review) | https://www.letpub.com/index.php?journalid=3860&page=journalapp&view=detail | ✅ Çekildi |
| [3] | Researcher.life IJPVP sayfası (Q2 mech eng, CiteScore 3.7, 212 art 2025) | https://researcher.life/journal/international-journal-of-pressure-vessels-and-piping/9578 | ✅ Çekildi |
| [4] | OOIR IJPVP metrik sayfası (IF 3.500/2024, H4-index 27, Q1 mech / Q2 multi) | https://ooir.org/j.php?issn=0308-0161 | ✅ Çekildi |
| [5] | IJPVP 2025 örnek makale (kompozit yama) | https://www.sciencedirect.com/science/article/abs/pii/S0308016125000249 | Başlık/künye teyitli |
| [6] | IJPVP yerel cidar incelmesi SCF makalesi | https://www.sciencedirect.com/science/article/abs/pii/S0308016104001322 | Başlık/künye teyitli |
| [7] | IJPVP değişken cidar kalınlığı butt weld SCF makalesi | https://www.sciencedirect.com/science/article/abs/pii/S0308016120300533 | Başlık/künye teyitli |
| [8] | IJPVP wrinkle bends stress analizi makalesi | https://www.sciencedirect.com/science/article/abs/pii/0263823193900197 | Başlık/künye teyitli (eski) |
| [9] | Elsevier Standard Reference Styles — Numbered Style (Style 1) | İndirildi: `Docs/refs/pdfs/elsevier_references_style_guide.pdf` (459 KB, %200 OK) | ✅ Local |
| [10] | Elsevier Copyediting Specification for Authors v3.6 (30 Oct 2020) | İndirildi: `Docs/refs/pdfs/elsevier_copy_editing_style.pdf` (644 KB, %200 OK) | ✅ Local |
| [11] | Booksite Elsevier reference styles PDF | https://booksite.elsevier.com/9780081019375/content/Elsevier%20Standard%20Reference%20Styles.pdf | ❌ HTTP 404 — link ölü |
| [12] | Elsevier shop IJPVP journal page (subscription info) | https://shop.elsevier.com/journals/international-journal-of-pressure-vessels-and-piping/0308-0161 | ⚠ Çekilmedi (subscription odaklı, scope info yok) |

---

## İndirilen Yerel Dosyalar (`Docs/refs/pdfs/`)

| Dosya | Boyut | Durum |
|---|---|---|
| `elsevier_references_style_guide.pdf` | 470 KB | ✅ Tam |
| `elsevier_copy_editing_style.pdf` | 660 KB | ✅ Tam |
| `elsevier_standard_reference_styles.pdf` | — | ❌ Silindi (404 HTML idi) |

---

## ⚠ İşaretli Eksik Maddeler (Yazar Manuel Doğrulama Listesi)

1. **CiteScore çelişkisi** (3.7 vs 6) — Scopus CiteScore sayfasından teyit
2. **Engineering Multidisciplinary quartile** (Q1 vs Q2) — JCR'den teyit
3. **Article type listesi + kelime limitleri** — Guide for Authors sayfasından
4. **Resmi scope statement (verbatim) + istisnalar** — IJPVP ana sayfasından
5. **Abstract kelime limiti (kesin sayı)** — Guide for Authors
6. **Highlights/CRediT'in IJPVP-spesifik özel kuralları** — varsa Guide for Authors
7. **Peer review türü ve ortalama süresi** — Elsevier IJPVP sayfası ya da editör yorumları
8. **Submission Editorial Manager URL** — Guide for Authors
9. **OA APC ücreti** — Elsevier OA pricelist
10. **Aktif special issue çağrıları** — Elsevier IJPVP special issues sayfası

Bu 10 öğenin tamamı **yazar tarafından dergi sayfası açılıp doğrudan doğrulanmalı** ve bu dosyaya yazar onayıyla eklenmelidir. CLI bunları yeniden web'den aramayacak.

---

## Kullanım Kuralları

1. **Bu dosya FROZEN.** Yazar açıkça "v2 olarak güncelle" diyene kadar değiştirilmez.
2. **IJPVP ile ilgili her CLI işleminde** önce bu dosya `view` edilir.
3. **Yeni web araması yasak** — bilgi burada yoksa ⚠ olarak işaretle veya yazardan iste.
4. **Çelişki tespit edersen** (örn. başka bir kaynaktan farklı bir IF gelirse) → bu dosyaya **yazma**, yazara bildir.

---

## Sürüm
- **v1 — 2026-05-26** — İlk derleme; 4 birincil + 4 örnek-yayın kaynağı + 2 PDF local; 10 ⚠ eksik madde yazar listesi
