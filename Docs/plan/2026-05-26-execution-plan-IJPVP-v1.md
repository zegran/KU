# Tez → IJPVP Makale Uygulama (Execution) Planı — v1

**Tarih:** 2026-05-26
**Referans plan:** `Docs/plan/2026-05-26-paper-plan-IJPVP-v1.md` (otoriter; K1–K4 kapalı)
**Bu dosyanın amacı:** v1 stratejik planı üzerine **somut, sıralı, onay-gate'li üretim akışı** kurmak.
**Kısıt:** Yazar onayı olmadan hiçbir WP başlatılmaz veya atlanmaz. Süre tahminleri konservatif; her oturum ~1–2 saat varsayılmıştır.

---

## Bölüm 1 — Üretim Envanteri

Makaleyi submit-ready hâle getirmek için üretilecek tüm artefaktlar. Tez kaynak satır aralıkları WP1'de doğrulanacak (şu an TOC-tabanlı tahmin).

### 1A — Section Taslakları (paper body)
| # | Artefakt | Tez kaynak (tahmini) | Hedef kelime | Türü |
|---|---|---|---|---|
| A1 | § 1 Introduction | GİRİŞ + LİT. TARAMASI özet | ~700 | EN prose |
| A2 | § 2 Background (API 5L X70 + ILI ripple) | Yüksek Dayanımlı Hat Boruları + Geometri ILI bölümleri | ~800 | EN prose |
| A3 | § 3 Theoretical Framework (elasticity + SCF) | Kuramsal Temel ve Elastisite Çerçevesi | ~800 | EN prose + denklem |
| A4 | § 4 Numerical Model + Validation (V1–V6 entegre) | Sayısal Modelleme + Temsili Hasar + Doğrulama | ~1200 | EN prose + tablo + şekil |
| A5 | § 5 Fatigue Methodology (Markl + rainflow + Miner + S-N kalibrasyon) | Yorulma Analizi + Markl S-N + Rainflow + Miner alt-bölümleri | ~1000 | EN prose + denklem + şekil |
| A6 | § 6 Results (parametric SCF + spectra + Miner damage) | Yöntem ve Model Kurulumu + Çevrim Büyüklüğü + Karma Spektrum + Miner senaryoları | ~1500 | EN prose + figür + tablo |
| A7 | § 7 Discussion (critical SCF + FFS implications + limitations) | SCF Değerinin Kritik Eşiğe Etkisi + sentez | ~1000 | EN prose + anchor figür |
| A8 | § 8 Conclusions | SONUÇ VE ÖNERİLER | ~300 | EN prose |
| | **Toplam body** | | **~7300** | |

### 1B — Şekiller (hedef 6–8 main + 2–3 supplementary)
| # | Artefakt | Tez kaynak | Üretim biçimi |
|---|---|---|---|
| F1 | FEA model şeması (geometri + BC + mesh composite panel) | ŞEKİLLER DİZİNİ'ndeki model şekilleri | **Yeniden çiz** (vektör, EN annotation) |
| F2 | Ripple geometri parametre tanımı (d, L, d/t, d/L) | Temsili Hasar Modeli | **Yeniden çiz** |
| F3 | Validation karşılaştırma (V4 — IPC 2002-27124) | Doğrulama bölümü | **Yeniden çiz** (overlay plot) |
| F4 | Mesh independence (V1) — opsiyonel | (yoksa ek FEA'dan üretilir) | **Yeni** (V1 mitigation) |
| F5 | SCF parametrik kontur/yüzey haritası | SCF parametrik sonuçlar | **Yeniden çiz** (yüksek DPI) |
| F6 | Markl S-N eğrisi + kalibrasyon (V5) | Markl S-N alt-bölümü | **Yeniden çiz** |
| F7 | Rainflow histogram + Miner damage breakdown | Basınç Çevrimi Analizi + Miner senaryoları | **Yeniden çiz** |
| F8 | **Critical SCF threshold curve (anchor figure)** | SCF Kritik Eşik bölümü | **Yeni — anchor** |
| F9-S1 | Mesh DOF tablosu / element kalite metrikleri (supplementary) | Sayısal model bölümü | Tablo/şekil |
| F10-S2 | Tam MAOP çevrim senaryosu detayları (supplementary) | Miner — Tam MAOP | Şekil |
| F11-S3 | Karma çevrim spektrum tüm vakalar (supplementary) | Karma Çevrim Spektrumu | Şekil |

**Not:** Mevcut 18 tez şekli WP3'te tek tek incelenir; yukarıdaki liste hedef envantere göre yapılandırılmıştır. Tüm main figure'ler yeniden çizilir (K4 görsel benzerlik 0).

### 1C — Tablolar (hedef 3–4 main + supplementary)
| # | Artefakt | Tez kaynak | Tür |
|---|---|---|---|
| T1 | Pipeline + material properties (API 5L X70) | Materyal bölümü | Main |
| T2 | FEA model özet (DOF, element tipi, BC, yük) | Sayısal Modelleme | Main |
| T3 | SCF parametrik vakalar matrisi | SCF sonuçları | Main |
| T4 | Miner damage senaryoları sonuç tablosu | Miner senaryoları | Main |
| T5-S | Tüm tez tablolarından supplementary'ye düşenler | Çeşitli | Supplementary |

### 1D — Denklem Türetimleri
| # | Artefakt | Tez kaynak | İçerik |
|---|---|---|---|
| E1 | Thin-shell hoop/long stress (Lame baseline) | Kuramsal Temel | σ_θ = pD/2t, σ_z |
| E2 | SCF tanımı | Kuramsal Temel | K_t = σ_max / σ_nominal |
| E3 | End cap force türetimi | (yeni, V6 destek) | F_endcap = p·A_internal |
| E4 | Markl S-N denklemi | Markl bölümü | i·S·N^b = C |
| E5 | Rainflow + Miner damage formu | Rainflow + Miner bölümleri | D = Σ n_i / N_i |
| E6 | S-N curve calibration (V5) | Yorulma bölümü | displacement → force conversion |

### 1E — Validation Alt-Bölümü (§ 4 içinde)
| # | Artefakt | Kaynak | Çıktı |
|---|---|---|---|
| V-A | DOF + mesh kalite metrikleri raporu (V1) | Tezdeki sayılar | 1 paragraf + 1 tablo |
| V-B | Element seçim gerekçesi (V2) | Tezde mevcut | 1 paragraf |
| V-C | Lame baseline karşılaştırma (V3) | Tezde varsa raporla; yoksa **ek FEA gerekli** | 2-3 cümle + 1 sayı |
| V-D | IPC 2002-27124 dış doğrulama (V4) | Tezde mevcut | 1 alt-paragraf + 1 şekil (F3) |
| V-E | S-N kalibrasyon (V5) | Tezde mevcut | 1 paragraf + 1 şekil (F6) |
| V-F | BC + symmetry justification (V6) | Tezde mevcut | 1 paragraf + 1 şekil (F1) |

### 1F — Ek FEA Koşuları (CLI üretemez — yazar/danışman alanı)
| # | Artefakt | Tetik | Maliyet (yazar) | Gate |
|---|---|---|---|---|
| FEA-1 | V1 mesh independence — 2 alternatif mesh seviyesi (coarse + fine) | Defansif, opsiyonel | ~2-4 saat CAD/solver | Gate değil |
| FEA-2 | V3 ripple-siz baseline koşu (Lame karşılaştırma için) | Tezde yoksa **önerilen** | ~30-60 dk | Gate değil ama önerilir |

### 1G — Frontmatter / Submission Package
| # | Artefakt | İçerik | Üretim aşaması |
|---|---|---|---|
| FM1 | Title + Author affiliations + Keywords (5–7) | — | WP4 başlangıcı |
| FM2 | Abstract (~250 kelime, IJPVP yapısı) | Problem + Method + Result + Implication | WP5 sonu |
| FM3 | Highlights (3–5 madde, her biri ≤85 karakter) | Anchor claim + 4 destekleyici | WP5 sonu |
| FM4 | Graphical abstract | Anchor figür (F8) basitleştirilmiş + akış oku | WP7 |
| FM5 | Cover letter | Novelty + scope-fit + K4 şeffaflık paragrafı | WP7 |
| FM6 | Novelty statement | 3-4 cümle | WP7 |
| FM7 | CRediT author statement | Yazar rolleri | WP7 (yazar input) |
| FM8 | Data availability statement | FEA model + dataset paylaşım kararı | WP7 (yazar input) |
| FM9 | Funding / conflict of interest | — | WP7 (yazar input) |

### 1H — Referanslar
| # | Artefakt | Kaynak | Hedef |
|---|---|---|---|
| R1 | references.bib | Tez referanslarından + WP2 ek havuzu | 30–60 kayıt |
| R2 | Citation verification raporu | Her kayıt için DOI + başlık + yıl + sayfa | WP6 |
| R3 | Self-cite (tez) BibTeX kaydı | YÖK kayıt sonrası | WP6/WP7 |

---

## Bölüm 2 — Otonomi Sınıflandırması

| 🟢 CLI Otonom | 🟡 CLI Yarı-Otonom (yazar girdisi şart) | 🔴 CLI Yapamaz (yazar/danışman/sistem dışı) |
|---|---|---|
| TR→EN paraphrase-rewrite (WP0d SOP ile) | Anchor framing son onayı (Form 2 vs Form 3 yumuşatma) | Ek FEA koşuları (FEA-1, FEA-2) |
| Section taslakları (A1–A8) ilk versiyon | Atıf doğrulama (kritik referansların gerçek erişimi) | Lamé/thin-shell sayısal hesap (verinin yazardan gelmesi gerek) |
| BibTeX formatlama | Novelty yargısı (alanın hakem perspektifi) | Deneysel veri üretimi |
| Şekil caption ilk taslağı (EN) | Kritik şekil seçimi (hangi 6-8 main kalır) | Danışman onayı |
| Literatür hipotezleri (önerilen ref. listesi) | V5 S-N kalibrasyon vurgusunun şiddeti | iThenticate raporu çekimi |
| Tablo dönüşümü (tez tablosu → IJPVP formatı) | T1 material properties tablosunun gerçek değerleri | Dergiye submission (ID, hesap) |
| Plan/checkpoint dosyaları (WP1–WP7 çıktıları) | T2 FEA tablosunun gerçek DOF/eleman sayıları | YÖK kayıt durumunun beklenmesi (K4 tetik) |
| LaTeX template iskelet hazırlığı | Cover letter şeffaflık paragrafının kişisel detayları | Şekil yeniden çiziminin **görsel kalite onayı** (yazar görsel review) |
| Self-review checklist çalıştırma | CRediT rol dağılımı | Telif/izin sorunlarının çözümü (gerekirse) |
| writing-anti-ai temizliği | Data availability kararı | Co-author iletişimi |
| Paraphrase cross-check | F8 (anchor figure) parametrik veri girdisi | Submission sonrası rebuttal kararları |
| WP0d rewrite SOP somutlaştırma | Highlight maddelerinin son seçimi | Ödeme/APC işlemleri (open access opsiyonu) |

**Not:** 🟡 satırlar yazar tarafından sağlanmadan ilgili WP **bekleme moduna** geçer. CLI proaktif uyarır.

---

## Bölüm 3 — Sıralı Emir Akışı

Her WP için: **(a)** tetikleyici yazar komutu · **(b)** CLI çıktı(lar)ı · **(c)** checkpoint kriteri · **(d)** gerçekçi süre.

**Genel kural:** Her WP sonunda CLI durur, yazar onayı bekler. "Devam" komutu olmadan bir sonraki WP başlamaz.

---

### WP1 — Thesis-to-IJPVP Mapping

- **(a) Tetikleyici komut:** `WP1 başlat`
- **(b) CLI çıktıları:**
  - `Docs/plan/WP1_thesis_to_paper_map.md`
    - Tezin baştan sona ayrıntılı okuma notları
    - Her tez bölümü → makale section + paragraf + kelime tahsisi tablosu (Bölüm 1A güncellenir)
    - Anchor feasibility (WP0b) doğrulaması: critical SCF eşiğinin veriden çıkış biçimi (sayı/eğri/band)
    - V3 baseline koşu gerekliliği netleştirmesi (tezde var mı yok mu)
    - 18 mevcut tez şeklinin tek tek tezdeki rolü ve makale envanterine map'lenmesi
- **(c) Checkpoint kriteri:**
  - Yazar onaylar: bölüm haritası doğru, anchor feasibility kararı kabul edilir, V3 kararı verilir
- **(d) Süre:** **2–3 oturum** (~3–6 saat) — 1960 satırlık tezin ayrıntılı okunması + map üretimi

---

### WP2 — Citation Strategy & Reference Pool

- **(a) Tetikleyici komut:** `WP2 başlat`
- **(b) CLI çıktıları:**
  - `Docs/plan/WP2_citation_targets.md`
    - Tezdeki tüm referansların kategorize tablosu (EN-peer-reviewed / TR / standart-doküman / web)
    - IJPVP-uyumlu konularda eksik referans havuzu önerisi (her biri için arama anahtar kelimeleri ve isim/yıl önerileri — DOI doğrulama WP6'da)
    - IPC 2002-27124 ana validation referansı kaydı
    - Self-cite (tez) için BibTeX şablonu
- **(c) Checkpoint kriteri:**
  - Yazar onaylar: önerilen referans havuzu kapsamlı; eklenecek/çıkarılacak isim listesi netleşir
- **(d) Süre:** **2–3 oturum** (~3–5 saat)
- **🟡 Yazar girdisi gerekli:** Önerilen referansların erişilebilirliği ve uygunluğu

---

### WP3 — Figures & Tables Strategy

- **(a) Tetikleyici komut:** `WP3 başlat`
- **(b) CLI çıktıları:**
  - `Docs/plan/WP3_figures_tables.md`
    - 18 mevcut tez şekli için karar matrisi (tut / EN-caption / yeniden çiz / birleştir / çıkar)
    - Bölüm 1B envanterinin son hâli (F1–F8 main + F9-F11 supplementary)
    - Her yeniden çizilecek şekil için: amaç, veri kaynağı, eksen etiketleri (EN), legend, stil parametreleri
    - Tablo envanteri (12 tez tablosu → 3–4 main + supplementary) son hâli
    - Anchor figure (F8) için parametrik veri ihtiyacı listesi
- **(c) Checkpoint kriteri:**
  - Yazar onaylar: hangi şekiller yeniden çizilecek, hangileri orijinal kalır; tablo seçimi onaylı
- **(d) Süre:** **1–2 oturum** (~2–3 saat)
- **🟡 Yazar girdisi gerekli:** Görsel kalite önceliği, F8 için veri sağlanması (sonra WP5'te)

---

### WP4 — Section-by-Section Drafting Plan

- **(a) Tetikleyici komut:** `WP4 başlat`
- **(b) CLI çıktıları:**
  - `Docs/plan/WP4_section_drafting_plan.md`
    - § 1–§ 8 için: kaynak tez satır aralıkları (kesin), tek cümlelik amacı, argüman zinciri (3–5 bullet), şekil/tablo bağı, kelime hedefi
    - WP0d (rewrite SOP) referansı her section'da
  - `Docs/plan/WP0d_rewrite_sop.md` — anti-plagiarism SOP somut hâli (K4 tetiği aktif olur — yazar tez YÖK kayıt durumunu bildirmeden WP5 başlatılmaz)
- **(c) Checkpoint kriteri:**
  - Yazar onaylar: section bazlı argüman zincirleri ve kelime tahsisi doğru
  - Yazar bildirir: YÖK kayıt durumu (K4 tetik)
- **(d) Süre:** **1–2 oturum** (~2–4 saat)

---

### WP5 — Drafting (her section ayrı oturum)

**Kritik kural:** Her section ayrı CLI oturumunda. Her oturum başında WP0d SOP kontrol listesi çalıştırılır.

- **(a) Tetikleyici komut:** `WP5 başlat: §N` (örn. `WP5 başlat: §1`)
- **(b) CLI çıktıları (her section için):**
  - `Docs/paper/sections/0N_<section_name>.md` — EN prose taslak
  - Section sonu: writing-anti-ai temizlik raporu
  - Section sonu: TR ↔ EN içerik kapsama kontrolü raporu (paraphrase doğrulaması)
- **(c) Checkpoint kriteri (her section için):**
  - Yazar onaylar veya revize istek listesi verir → revize → tekrar onay
  - Onay sonrası bir sonraki section komutu beklenir
- **(d) Süre (her section):**
  - § 1, § 8 (kısa): 1 oturum (~1–2 saat) + revizyon
  - § 2, § 3, § 5 (orta): 1–2 oturum (~2–4 saat)
  - § 4, § 6, § 7 (uzun, anchor ağırlıklı): 2 oturum (~3–5 saat)
- **Toplam WP5:** **10–16 oturum** (~20–32 saat) — yazar onay turları dahil değil
- **🟢🟡🔴 Karma:** Prose CLI; F8 anchor verisi 🟡; FEA-1/FEA-2 gerekirse 🔴

---

### WP6 — Citation Verification + BibTeX

- **(a) Tetikleyici komut:** `WP6 başlat`
- **(b) CLI çıktıları:**
  - `Docs/paper/references.bib` — tüm referanslar BibTeX formatında
  - `Docs/plan/WP6_citation_verification_report.md` — her referans için DOI + başlık + yıl + dergi + erişim durumu
  - Atıf-metin tutarlılık raporu (her [Ref] yerinde mi, kullanılmayan ref var mı)
- **(c) Checkpoint kriteri:**
  - Yazar onaylar: her referans doğrulandı veya yazardan kaynak teyidi geldi
  - Eksik referanslar için yazar erişim sağlar veya alternatif önerilir
- **(d) Süre:** **2–3 oturum** (~3–5 saat) + erişim bekleme süreleri
- **🟡 Yazar girdisi gerekli:** Erişilmeyen referansların doğrulanması

---

### WP7 — Self-Review + LaTeX + Submission Package

- **(a) Tetikleyici komut:** `WP7 başlat`
- **(b) CLI çıktıları:**
  - `Docs/paper/main.tex` — IJPVP Elsevier `els-cas-templates` (cas-sc) iskelet
  - Tüm section'lar markdown'dan LaTeX'e taşınmış
  - `Docs/paper/submission/cover_letter.md` (K4 şeffaflık paragrafı dahil)
  - `Docs/paper/submission/highlights.md`
  - `Docs/paper/submission/novelty_statement.md`
  - `Docs/paper/submission/credit_statement.md` (yazar dolduracak iskelet)
  - `Docs/paper/submission/data_availability.md` (yazar dolduracak iskelet)
  - `Docs/plan/WP7_self_review_report.md` (paper-self-review skill çıktısı)
  - Graphical abstract için F8'den türetilmiş basitleştirilmiş versiyon
- **(c) Checkpoint kriteri:**
  - Yazar onaylar: tüm submission package elemanları doğru
  - iThenticate raporu (yazar çeker) sonucu < %15 tez örtüşmesi
  - Yazar/danışman final review
- **(d) Süre:** **3–4 oturum** (~5–8 saat) + iThenticate + danışman review beklemeleri
- **🔴 CLI yapamaz:** iThenticate çekimi, dergi hesabı/submission, APC ödeme

---

## Toplam Tahmini Süre (gerçekçi)

| Aşama | CLI oturum | CLI saat | Yazar/dış bekleme |
|---|---|---|---|
| WP1 | 2–3 | 3–6 | 1–2 gün onay |
| WP2 | 2–3 | 3–5 | 1–3 gün ref. araştırma |
| WP3 | 1–2 | 2–3 | 1–2 gün onay |
| WP4 | 1–2 | 2–4 | 1–3 gün YÖK kayıt teyidi |
| WP5 | 10–16 | 20–32 | Her section 1–3 gün onay turu |
| WP6 | 2–3 | 3–5 | 3–7 gün ref. erişim |
| WP7 | 3–4 | 5–8 | 3–10 gün iThenticate + danışman |
| **Toplam** | **21–33 oturum** | **~38–63 CLI saat** | **3–6 hafta takvim** |

**Takvim notu:** Tek başına CLI saatleri gerçek takvimi vermez. Yazar onay turları, ek FEA koşuları (varsa), iThenticate ve danışman review beklemeleri eklenince **gerçekçi takvim 6–10 hafta**.

---

## Genel Kısıtlar & Disiplinler

1. **Onay gate'leri zorunlu:** Her WP yazar onayı olmadan bitmemiş sayılır
2. **WP atlanamaz:** WP1 olmadan WP2/WP3 başlamaz; WP4 olmadan WP5 başlamaz; vb.
3. **WP5 section sırası:** Önerilen § 1 → § 2 → § 3 → § 4 → § 5 → § 6 → § 7 → § 8. Ancak § 6 ve § 7 yazılmadan abstract ve highlights final hâline gelmez.
4. **K4 disiplini:** WP5 başlamadan önce WP0d SOP somutlaşmış olmalı; her section oturumu başında SOP kontrol listesi çalışır
5. **K2 mitigation tetiği:** FEA-1 (V1 mesh) ve FEA-2 (V3 baseline) gerek olursa WP1 veya WP4 sonrasında yazara bildirilir; karar yazara aittir; gate değildir
6. **Optimistik tahmin yasak:** Yukarıdaki süreler conservative; her WP'de %20-30 sapma payı vardır
7. **Hata düzeltme bütçesi:** WP5 sonrası 1-2 oturumluk konsolidasyon/uyum revizyonu için pay ayrılmıştır (WP7 içinde)

---

## Sonraki Somut Adım

**Yazar komutu bekleniyor:** `WP1 başlat`

Komut verildiğinde CLI:
1. Tezi ayrıntılı okumaya başlar
2. `Docs/plan/WP1_thesis_to_paper_map.md` üretir
3. WP1 checkpoint'inde durur

---

## Sürüm
- **v1 — 2026-05-26** — İlk execution planı; v1 stratejik plan üzerine kurulu
