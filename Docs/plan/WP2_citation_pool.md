# WP2 — Citation Pool + Reference Targets

> **WP:** WP2 (execution-plan v2)
> **Skill:** `citation-verification` (primary) + `daily-paper-generator` (support)
> **Tarih:** 2026-06-02
> **Durum:** ✅ CHECKPOINT ONAYLANDI (2026-06-02) — Havuz ~54 kaynak, B+F kümesi genişletildi (yazar talebi). WP3a/WP4 başlatılabilir. Tam DOI doğrulama WP6b.
> **Hedef:** 33 → **48-53 EN kaynak**, non-peer-reviewed değiştir, Elsevier numbered style
> **Anti-fabrikasyon:** Tüm yeni adaylar WebSearch ile **varlık-doğrulamalı**; tam DOI/metadata doğrulaması **WP6b**'ye ertelendi. Doğrulanamayanlar `[VERIFY]` işaretli.

---

## 0. WP2 Kapsamı (execution-plan v2)

1. Tezdeki 33 referansı kategorize et (EN peer-reviewed / standart / konferans / kitap / TR-thesis / web).
2. IJPVP-uyumlu eksik referans kümeleri (§3).
3. Anchor referansları (IPC2002-27124, Rosenfeld, Markl, Kiefner, dent/ILI).
4. Elsevier numbered style ([n]) hazırlığı.
5. **Yazar girdisi:** erişilemeyen referansların doğrulanması.

> **Not (citation-verification disiplini):** WP2 havuz-planı adımıdır. Hiçbir referans uydurulmadı. Yeni adaylar gerçek WebSearch sonuçlarından alındı; her birinin URL'si ve doğrulama durumu işaretli. Tam künye + DOI doğrulaması WP6b'de `references.bib` üretilirken yapılır.

---

## 1. Mevcut 33 Referans — Kategorizasyon ve Durum

| # | Künye (kısalt) | Tür | Durum | Eylem |
|---|---|---|---|---|
| [1] | CSA Z662-2023 | Standart | ✅ güçlü | Tut |
| [2] | ASME B31.8-2025 | Standart | ✅ güçlü | Tut |
| [3] | Bilston & Murray, Cold Field Bending, PRCI 1993 | Rapor (gri) | 🟡 zayıf | Peer-reviewed alt. ara veya standart-yanı koru |
| [4] | Rosenfeld et al., IPC2002-27124 | Konferans | ✅ anchor | Tut · **[13] ile birleştir** |
| [5] | API 5L | Standart | ✅ güçlü | Tut · **[19] ile birleştir** |
| [6] | IPC2008-64030, Compressive Strain Capacity | Konferans | ✅ | Tut |
| [7] | Alexander & Kulkarni, FEA of Wrinkled Pipelines, IPC | Konferans | 🟡 künye eksik (yıl yok) | Yıl + IPC numarası tamamla |
| [8] | Pilkey, Peterson's SCF, 3rd ed, Wiley 2008 | Kitap | ✅ kanonik | Tut |
| [9] | IPC2018-78488, Wrinkle Strain and Fatigue | Konferans | ✅ | Tut · [14] ile çapraz kontrol |
| [10] | IPC2022-86760, Repair of Wrinkled Pipelines | Konferans | ✅ | Tut · [15] ile çapraz kontrol |
| [11] | Turhan, Fatigue of Welded API 5L X70, MS thesis METU 2020 | Tez (TR-kurum) | 🔴 zayıf | **A1 (Springer JFAP) ile değiştir/destekle** |
| [12] | DNVGL-ST-F101 | Standart | ✅ | Tut |
| [13] | Rosenfeld IPC2002-27124 (tam künye) | Konferans | 🔴 **[4] DUPLİKAT** | [4] ile birleştir |
| [14] | Holliday et al., IPC2018 (Do You Have Wrinkles?) | Konferans | ✅ | [9]'un tam künyesi — tek girdiye indir |
| [15] | Johnson et al., IPC2022 (Repair Tech.) | Konferans | ✅ künye eksik (yıl/sayfa) | [10]'un tam künyesi — tamamla |
| [16] | Montgomery et al., Linear Regression Analysis, Wiley | Kitap | ⚠ **çift kullanım** | Tut — ama satır 389 [16]'yı X70 mikroyapı için atıfla (hata); ayrıştır |
| [17] | Schijve, Fatigue of Structures and Materials, Springer 2009 | Kitap | ✅ kanonik | Tut |
| [18] | Sen & Cheng, IPC2010, FEA of Cold Bend Pipes | Konferans | ✅ | Tut |
| [19] | API 5L | Standart | 🔴 **[5] DUPLİKAT** | [5] ile birleştir |
| [20] | ASME V&V 10-2006 | Standart | ⚠ versiyon | Metin V&V 10-**2019** diyor (satır 675); sürüm tutarsızlığı çöz |
| [21] | Oberkampf & Roy, V&V in Scientific Computing, Cambridge 2010 | Kitap | ✅ | Tut |
| [22] | Rodabaugh, WRC Bulletin 335, 1988 | Bülten | 🟡 yarı-peer | **Tut** — C'=1126 MPa kaynağı (kritik) |
| [23] | ASTM E1049-85(2017) | Standart | ✅ | Tut |
| [24] | Miner, Cumulative Damage in Fatigue, ASME JAM 1945 | **Dergi** | ✅ kanonik | Tut |
| [25] | ROSEN, RoCorr MFL flyer | Web/flyer | 🔴 zayıf | ILI ref ile değiştir (C1/C2) veya web-ref formatına çek |
| [26] | Madier, Practical FEA, Elsevier 2020 | Kitap | ✅ | Tut |
| [27] | Cook et al., Concepts & Applications of FEA, 4th ed, Wiley 2002 | Kitap | ✅ kanonik | Tut |
| [28] | Zienkiewicz et al., FEM, 7th ed, Elsevier 2013 | Kitap | ✅ kanonik | Tut |
| [29] | API 579-1/ASME FFS-1, 2016 | Standart | ✅ FFS anchor | Tut |
| [30] | Laulusa et al., Shear Deformable Shell Elements, IJSS 2006 | **Dergi** | ✅ | Tut (S4R gerekçesi) |
| [31] | Yavuz, Materials selection aircraft skin panels, Procedia SI 2019 | **Dergi** | 🟡 tematik uzak | Boru-ilgili kabuk-element ref ile değiştir öneri |
| [32] | Dassault, Abaqus User's Guide 2024 | Yazılım kılavuzu | ⚠ versiyon | Metin Abaqus **2020** diyor (satır 680); sürüm birleştir |
| [33] | Rahmah, MFL Data Fusion, PPSA Conf. 2024 | Sunum (arşivsiz) | 🟡 zayıf | ILI peer-reviewed ile değiştir/destekle |

### Özet
- **Toplam listelenen:** 33 · **Duplikat çıkınca benzersiz:** ~31
- **Peer-reviewed DERGİ makalesi sadece 3:** [24], [30], [31] → **IJPVP için en büyük zayıflık** (hakem peer-reviewed dergi atfı bekler)
- **Güçlü tutulacak:** standartlar (1,2,5,12,20,23,29), konferanslar (4,6,7,9,10,18), kitaplar (8,16,17,21,26,27,28), dergi (24,30)
- **Değiştir/güçlendir:** [3],[11],[25],[31],[33] (5 zayıf kaynak)

### 🔴 Düzeltilecek atıf hataları (WP6a/WP6b)
1. **Duplikatlar:** [4]≡[13], [5]≡[19] → birleştir, numaralandırmayı kaydır
2. **[16] çift kullanım:** satır 389 X70 mikroyapı tezi için [16] diyor ama liste [16]=Montgomery regresyon kitabı. X70 mikroyapı için ayrı ref gerek (→ A1 veya yeni)
3. **Sürüm tutarsızlığı:** V&V 10-2006 vs 2019 [20]; Abaqus 2020 vs 2024 [32]
4. **Eksik künye:** [7] yıl yok; [15] yıl/sayfa eksik

---

## 2. IJPVP-Uyumlu Yeni Aday Referanslar (WebSearch-doğrulamalı)

> Her aday gerçek arama sonucundan alındı; **varlık WebSearch ile teyitli**, tam DOI/yazar listesi **WP6b**'de doğrulanacak (`[VERIFY]`).

### Küme A — API 5L X70 mekanik/yorulma davranışı (zayıf [11]'i değiştirir)
| ID | Künye | Venue | URL / DOI | Durum |
|---|---|---|---|---|
| A1 | Fatigue Behavior of Welded API 5L X70 Steel Used in Pipelines | J. Failure Analysis and Prevention (Springer), 2020 | doi:10.1007/s11668-020-00959-x | ✅ DOI'li |
| A2 | Drexler et al., Fatigue crack growth rates of API X70 pipeline steel in pressurized hydrogen | Fatigue Fract. Eng. Mater. Struct. (Wiley), 2014 | doi:10.1111/ffe.12133 | ✅ DOI'li |
| A3 | SCC and fatigue crack growth of API 5L X70 welded joint in ethanol environment | **IJPVP** (ISSN 0308-0161) | sciencedirect.com/.../S0308016116303180 | ✅ IJPVP self-relevant |

### Küme B — Ripple/wrinkle field bend (mevcut konferansları destekler)
| ID | Künye | Venue | URL | Durum |
|---|---|---|---|---|
| B1 | Stress analyses of wrinkle bends in pipelines | ⚠ Thin-Walled Structures (0263-8231) — readiness'te IJPVP sanılmıştı | sciencedirect.com/.../0263823193900197 | `[VERIFY]` venue |
| B2 | Evaluating the Effects of Wrinkle Bends on Pipeline Integrity | IPC2008, ASME | asmedigitalcollection.../IPC2008 | ✅ konferans |

### Küme C — Dent / ILI geometrik anomali yorulma (anchor FFS bağlamı)
| ID | Künye | Venue | URL | Durum |
|---|---|---|---|---|
| C1 | API RP-1183, Assessment and Management of Dents | API standart, 2020 | API publication | ✅ standart (çok ilgili) |
| C2 | Integrity Assessment of In-Service Gas Pipeline with Dent Defect at Highway Crossing | Dergi (`[VERIFY]` ad) | sciencedirect.com/.../S2452321624004955 | `[VERIFY]` venue |
| C3 | Failure pressure prediction... dent-corrosion defect, FEM | Ocean Engineering (Elsevier) | sciencedirect.com/.../S0029801822021588 | ✅ dergi |

### Küme D — Markl SIF / yorulma metodolojisi (C' ve Markl temelini güçlendirir)
| ID | Künye | Venue | URL | Durum |
|---|---|---|---|---|
| D1 | Experimental Evaluation of the Markl Fatigue Methods and ASME Piping SIF (Part 1 & 2) | PVP2008, ASME | asmedigitalcollection.../PVP2008 | ✅ konferans |
| D2 | Markl, Fatigue Tests of Piping Components, Trans. ASME, 1952 | **Dergi (kanonik)** | `[VERIFY]` tam künye | ⚠ ekle — tez yalnızca dolaylı atıfla |

### Küme E — Boru hattı basınç-çevrim yorulma / spektrum (karma-spektrum bulgusunu destekler)
| ID | Künye | Venue | URL | Durum |
|---|---|---|---|---|
| E1 | Rosenfeld & Kiefner, Basics of Metal Fatigue in Natural Gas Pipeline Systems | Kiefner/PHMSA raporu | regulations.gov PHMSA-2011-0023 | 🟡 gri (otoriter, spektrum varsayımı kaynağı) |
| E2 | Evaluation of Fatigue in Gas Pipelines | IPC2016, ASME | asmedigitalcollection.../IPC2016 | ✅ konferans |
| E3 | INGAA, Fatigue Considerations for Natural Gas Transmission Pipelines | INGAA endüstri raporu | ingaa.org | 🟡 gri |

### Küme F — SCF analitik/sayısal (IJPVP komşu — desk-reject riskini düşürür)
| ID | Künye | Venue | URL | Durum |
|---|---|---|---|---|
| F1 | Finite element based stress concentration factors for pipes with local wall thinning | **IJPVP** | sciencedirect.com/.../S0308016104001322 | ✅ IJPVP komşu |
| F2 | Stress concentration analysis of butt welds with variable wall thickness | **IJPVP** | sciencedirect.com/.../S0308016120300533 | ✅ IJPVP komşu |
| F3 | SCF and fatigue analysis of lateral nozzle with local wall thinning | Engineering Failure Analysis (Elsevier) | sciencedirect.com/.../S1350630717308300 | ✅ dergi |

**Yeni aday toplamı (ilk tur):** 17 (A:3, B:2, C:3, D:2, E:3, F:3) + Markl orijinal.

### 🔎 Genişletme — B+F kümesi (yazar talebi, 2026-06-02)
Ripple/wrinkle + SCF analitik kümeleri genişletildi. **En kritik bulgu F4** — bu tezin metodolojik ikizi (parametrik FEA → ampirik SCF ifadesi → çevrimsel basınç yorulması), üstelik **IJPVP'de yayımlanmış**. Hakem-tanıdık atıf tabanını ve desk-reject korumasını doğrudan güçlendirir.

| ID | Künye | Venue | URL / DOI | Durum |
|---|---|---|---|---|
| **F4** | **Generalized expressions for SCF of pipeline plain dents under cyclic internal pressure** | **IJPVP** | sciencedirect.com/.../S0308016118303867 | ✅✅ **metodolojik ikiz** |
| F5 | Fatigue life assessment of damaged pipelines under cyclic internal pressure: longitudinal & transverse plain dents | Int. J. Fatigue (Elsevier) | sciencedirect.com/.../S0142112314001650 | ✅ dergi |
| F6 | Fatigue analysis of damaged steel pipelines under cyclic internal pressure | Int. J. Fatigue (Elsevier) | sciencedirect.com/.../S0142112308002144 | ✅ dergi |
| F7 | Empirical SCF modeling via FEA + ANN for fatigue design of tubular KT-joints | Fatigue Fract. Eng. Mater. Struct. (Wiley), 2023 | doi:10.1111/ffe.14122 | ✅ DOI'li (ampirik-SCF analog) |
| B3 | Local buckling failure analysis of high-strength pipelines | Petroleum Science (Springer), 2017 | doi:10.1007/s12182-017-0172-3 | ✅ DOI'li |
| B4 | Local buckling, strain localization, wrinkling and postbuckling response of line pipe | ⚠ Int. J. Solids Struct. (`[VERIFY]`) | sciencedirect.com/.../S014102969600096X | `[VERIFY]` venue |
| B5 | Behavior of wrinkled steel pipelines subjected to cyclic axial loadings | `[VERIFY]` dergi/konf. | researchgate (key word doğrulamalı) | `[VERIFY]` venue |

**Genişletme toplamı:** +7 (B+4, F+4 → B5/B4/B3 wrinkle; F4/F5/F6/F7 SCF). Bunlardan F4 zorunlu-atıf.
**Yeni aday genel toplam:** 17 + 7 = **~24**.

---

## 3. Havuz Boyut Hesabı

| Kategori | Mevcut (benzersiz) | Yeni aday | Toplam |
|---|---|---|---|
| Peer-reviewed dergi | 2 (24,30) | 13 (A1,A2,A3,C3,F1,F2,F3,F4,F5,F6,F7,B3,B4) | **15** |
| Konferans (ASME/IPC/PVP) | 6 | 4 (B2,B5,D1,E2) | **10** |
| Standart | 7 | 1 (C1 API RP-1183) | **8** |
| Kitap | 6 | — | **6** |
| Bülten/rapor (gri) | 1 (22) | 2 (E1,E3) | **3** |
| Kanonik dergi (Markl/Miner) | 1 (24) | 1 (D2) | dahil |
| **TOPLAM (yaklaşık)** | **~31** | **~24** | **~54** |

> Hedef bant **48-55** üst sınırında. **Peer-reviewed dergi 2→15 (×7.5 artış)** — IJPVP zayıflığını köklü kapatır. F4 (IJPVP dent-SCF) metodolojik ikiz olarak en yüksek hakem-değeri taşır.

---

## 4. Elsevier Numbered Style Hazırlığı

- Format: metin-içi `[n]`, listede görünüm sırasına göre (zaten tez `[n]` stilinde — minimal dönüşüm).
- Dergi makalesi: `Yazarlar, başlık, dergi, cilt (sayı) (yıl) sayfalar.`
- Konferans: `Yazarlar, başlık, in: tam konf. adı, yer, tarih, yayıncı, yıl, sayfalar.`
- Web ref: `Kurum, başlık, <URL>, yıl (accessed dd.mm.yy).` → [25] ROSEN, [33] bu formata.
- Kaynak: `Docs/refs/IJPVP_official_sources.md` §7 + `Docs/refs/pdfs/elsevier_references_style_guide.pdf`.

---

## 5. WP6b'ye Devir (tam doğrulama)

WP6b'de `Docs/paper/references.bib` üretilirken her referans için:
1. Google Scholar/DOI ile varlık + künye doğrulama
2. `[VERIFY]` işaretli alanları çöz (B1 venue, C2 venue/ad, D2 Markl tam künye)
3. Duplikat birleştirme + numara yeniden sıralama
4. Atıf hataları düzelt (§1 hataları)
5. Metin ↔ liste tutarlılık

---

## 6. 🟡 Yazar Girdisi Bekleyen

1. **Erişim doğrulaması:** A1/A2 (Springer/Wiley paywall) — yazar kurumsal erişimle PDF teyit edebilir mi?
2. **[11] Turhan tezi:** Tamamen çıkarılsın mı, yoksa A1 yanında self-context olarak kalsın mı?
3. **Spektrum referansı (E1/E3):** Karma çevrim spektrumu varsayımı (n=2/24/52/200) için gri-literatür atfı kabul mü, yoksa yazarda gerçek SCADA verisi var mı (WP1 §9.2 ile bağlantılı)?

---

## 7. Yazar Checkpoint — Onay Bekleyen

- [ ] Havuz kapsamı (48-53, 6 küme) onaylanıyor mu?
- [ ] Zayıf 5 kaynak ([3],[11],[25],[31],[33]) değiştirme/koruma kararları?
- [ ] Yeni 17 aday küme dağılımı yeterli mi, yoksa belirli bir alanda (örn. dent fatigue, X70) daha fazla mı?
- [ ] §6 yazar girdisi maddeleri

---

## 8. Kaynak Aramaları (bu WP'de yapılan WebSearch)

Tüm yeni adaylar şu gerçek aramalardan derlendi (2026-06-02):
- API 5L X70 fatigue crack growth → A1, A2, A3
- wrinkle/ripple field bend IJPVP → B1, B2
- dent ILI fatigue FEM → C1, C2, C3
- Markl SIF fatigue piping → D1, D2
- pipeline pressure cycle fatigue Kiefner → E1, E2, E3
- local wall thinning SCF IJPVP → F1, F2, F3
- **(genişletme)** wrinkle buckling HS pipeline cyclic FEA → B3, B4, B5
- **(genişletme)** SCF empirical formula parametric pipe imperfection → F4 (IJPVP ikiz), F7
- **(genişletme)** dent SCF strain-based fatigue parametric → F5, F6

---

## Sürüm
- **v1 (taslak) — 2026-06-02** — 33 referans kategorizasyon + 17 WebSearch-doğrulamalı yeni aday + 6 küme.
- **v1.1 (onaylı) — 2026-06-02** — Yazar talebiyle B+F kümesi genişletildi (+7 aday, F4 IJPVP metodolojik ikiz dahil). Havuz ~54, peer-reviewed dergi 2→15. WP2 KAPANDI. Tam DOI doğrulama WP6b.
