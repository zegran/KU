# Tez → IJPVP Makale Üretim Planı (v1)

> **2026-05-26 not:** Bu stratejik plan (K1–K4 sabit kararları) hâlâ geçerli. Ancak WP numerasyonu artık `Docs/plan/2026-05-26-execution-plan-IJPVP-v2.md`'ye göre okunmalıdır (Methods-first writing order). Bu dosyadaki WP1–WP7 referansları execution plan v2 ile aşağıdaki şekilde eşleşir:
> - WP1 (mapping) = WP1 ✓ aynı
> - WP2 (citations) = WP2 ✓ aynı
> - WP3 (figures/tables) → **WP3a + WP3b (figures) + WP4 (tables/equations)**
> - WP4 (section drafting plan) → WP1 içinde IMRaD spine olarak entegre edildi
> - WP5 (drafting) → **WP5a–WP5g** (Methods → Results → Discussion → Conclusion → Introduction → Abstract+Title → Highlights)
> - WP6 (citation verify) → **WP6a (coherence) + WP6b (citation) + WP6c (anti-AI) + WP6d (iThenticate)**
> - WP7 (self-review + LaTeX + submission) → **WP7a–WP7e + WP8 (submission)**

**Tarih:** 2026-05-26
**Hedef dergi:** International Journal of Pressure Vessels and Piping (Elsevier, Q1) — **SABİT**
**Kaynak:** `Docs/KUnal_tez_org_tr.md` (TR yüksek lisans tezi, 1960 satır) + `Docs/media/media/` (18 şekil)
**Durum:** Planlama tamamlandı; WP0 gate'leri çözüldü; WP1 başlatmaya hazır
**Yazar kararları:** K1=IJPVP sabit · K2 validation profili yazardan alındı · K3 IJPVP-bağlamlı pitch · K4 log'a alındı (WP5'te tekrar açılır)

---

## 0. Sabit Kararlar

### K1 — Hedef Dergi: IJPVP (kapalı karar)
- Tek hedef; IJMS, IJF, EFA değerlendirmeden çıkarıldı
- Tüm metodoloji, terminoloji, bölüm sırası, şekil sayısı, kelime tahsisi IJPVP normlarına göre kurgulanır
- Tier-2 safety net şu an aktif değil; ret hâlinde yeniden değerlendirme

### IJPVP profil parametreleri (planın temeli)
| Parametre | IJPVP normu |
|---|---|
| Uzunluk | 12–20 sayfa, ~6–10k kelime |
| Şekil sayısı | 5–10 main, varsa supplementary |
| Tablo sayısı | 2–5 |
| Referans sayısı | 30–60 |
| Kabul kıstası | Validated numerical model + standards-based methodology + practical engineering value |
| Closed-form gereği | Yok — parametrik FEA + ASME/API + Markl/Miner yeterli |
| Tipik bölüm sırası | Intro → Background → Theory → Numerical Model → Methodology → Results → Discussion → Conclusions |
| Tipik tema | Pipeline integrity, fitness-for-service, FEA + standards |

---

## 1. Validation Audit Sonucu (K2)

Yazarın doğrudan bildirimleri esas alınarak her validation öğesi değerlendirilmiştir.

| # | Öğe | Yazar bildirimi | IJPVP değerlendirmesi | Risk | Eylem |
|---|---|---|---|---|---|
| V1 | Mesh independence | ~30.000 element, eleman başına 24 DOF; toplam ~190k DOF; ek mesh seviyesi gerekmediği değerlendirilmiş | Yüksek DOF tek başına h-convergence kanıtı sayılmaz; hakem genelde explicit convergence tablosu ister | **Orta** | (a) Tezdeki DOF + element kalite metriklerini methodology'de raporla; (b) literatürdeki benzer ripple/dent FEA mesh sıklığına atıf; (c) ideal: 2 alternatif mesh seviyesi koşusu + küçük tablo (gate değil) |
| V2 | Element seçim gerekçesi | Tezde belirtilmiş, makaleye çıkarılacak | İyi | **Düşük** | Tezden ilgili paragrafı al, EN'de yeniden yaz, methodology'de 1 paragraf |
| V3 | Analitik benchmark (ripple-siz baseline) | Yazar bu öğenin ne kastettiğini sordu | **Açıklama:** Kusursuz silindir borunun iç basınç altında hoop stress'i σ_θ = pD/2t (thin-shell) veya Lame ile bilinir; FEA'nın ripple-siz baseline koşusu bu analitik değerle eşleşmeli (≤%2 hata). Bu, BC + element + material setup'ının sanity check'idir | Orta (eksikse) | (a) Tezde ripple-siz baseline koşu varsa raporla; (b) yoksa ~30 dk'lık 1 ek FEA koşusu + Lame karşılaştırma; methodology'de 2-3 cümle |
| V4 | Literatür dataset karşılaştırması | IPC 2002-27124 FEA + deneysel verileri tezde karşılaştırılmış, makaleye hazır | **Güçlü** — IJPVP için ideal external validation | **Çok düşük** | Doğrudan taşı; validation alt-bölümünün omurgası |
| V5 | Fatigue methodology validation | Displacement-controlled S-N eğrileri force-controlled fatigue ömrüne kalibre edilmiş | İyi — Markl methodology'nin standart adımı; explicit yazılması kritik | **Düşük** | Methodology'de "S-N curve calibration" alt-bölümü; 1 şekil + 1 paragraf |
| V6 | Boundary conditions | Yarım boru modeli + 3 BC + iç basınç + end cap force; tüm analizlerde kombine uygulanmış | İyi | **Düşük** | 1 şema şekli + 1 paragraf; symmetry BC justification + end cap force türetimi (basıncın eksenel itkisi / annular kesit alanı) cebirsel gösterim |

### Gate sonucu
**WP0a → GEÇTİ.** Kritik blocker yok.
- 4 güçlü: V2, V4, V5, V6
- 1 düşük maliyetli kapatma: V3 (opsiyonel)
- 1 orta risk: V1 (mitigation stratejisi hazır)

### Opsiyonel pre-yazım aksiyonlar (düşük maliyet, gate değil)
1. **V1:** 2 alternatif mesh seviyesi koşusu + h-convergence küçük tablosu — hakem ilk-tur yorumuna karşı defansif
2. **V3:** Eğer tezde ripple-siz baseline yoksa, 1 ek FEA koşusu + analitik Lame karşılaştırma

Her ikisi de yazıma başlamayı durdurmaz; rebuttal'da kapatılabilir riskler.

---

## 2. Anchor Claim (K3 — IJPVP bağlamında)

### Pitch (tek cümle, IJPVP-uyumlu)
> *"This work develops a parametric stress-concentration-to-life framework for ILI-detected ripple defects in API 5L X70 high-strength gas pipelines, coupling FEA-derived SCF with Markl S-N and rainflow–Miner damage accumulation under realistic pressure-cycle spectra, and establishes a critical SCF threshold for fitness-for-service decisions."*

### Pitch'in IJPVP normlarına uyumu
- **Fiil:** "develops + establishes" — ölçülebilir
- **Nesne:** parametrik framework + critical SCF threshold (somut)
- **Standartlar:** Markl S-N, ASTM E1049 rainflow, Miner kuralı — IJPVP'nin günlük dili
- **Uygulama:** fitness-for-service — IJPVP'nin core kullanım alanı
- **Doğrulama:** V4 (IPC 2002-27124) dış kaynağı
- **Closed-form derivation gerekmiyor** — IJPVP toleranslı

### Feasibility ön-kontrolü (TOC seviyesinde pozitif)
Tezde mevcut bölümler pitch'i destekliyor:
- `SCF Değerinin Kritik Eşiğe Etkisi` → eşik çıkarımı var
- `Karma Çevrim Spektrumu` → realistic pressure spectrum analizi
- `Miner Hesabı — Tam MAOP Çevrimi Senaryosu` → operasyonel senaryo bağlanmış
- `Basınç Çevrimi Analizi — ASTM E1049 Rainflow Sayımı` → standart-uyumlu

**WP1 sırasında doğrulanacak:** Eşik tek sayı mı, eğri mi, D/t-bantlı mı? Bu cevap, anchor figure'ün biçimini belirler.

---

## 3. K4 Log (anti-plagiarism — sonraki aşamaya ertelendi)

**Yazar notu:** Tez kayıt aşaması henüz bitmedi; K4 disiplini WP5 başlangıcında tekrar açılır.

**Hatırlatma (WP5'te aktif olacak):**
- YÖK tez indeksi iThenticate tarafından taranır
- TR → EN doğrudan çeviri %30+ benzerlik üretebilir
- Çözüm SOP: skeleton-extraction (EN bullets) → close-source → rewrite → content cross-check
- Cover letter şeffaflık paragrafı: "based in part on the first author's MSc thesis at [University], 2026"
- Self-cite tez referans olarak references.bib'e eklenir
- Şekiller yeniden çizilirse görsel benzerlik 0
- Hedef iThenticate skor: tezden < %15

**Tetik:** WP5 (drafting) başlamadan önce `Docs/plan/WP0d_rewrite_sop.md` olarak somutlaştırılır.

---

## 4. WP Roadmap (revize, IJPVP-spesifik)

### WP0 — Gates (durum)
- [x] **WP0a** (Validation Audit) — GEÇTİ
- [x] **WP0c** (Journal Targeting) — IJPVP sabitlendi
- [~] **WP0b** (Anchor Feasibility) — TOC seviyesinde pozitif; tam doğrulama WP1 ile birleşik
- [ ] **WP0d** (Rewrite SOP) — WP5 başlangıcında

### WP1 — Thesis-to-IJPVP-Paper Mapping
**Çıktı:** `Docs/plan/WP1_thesis_to_paper_map.md`

Eylemler:
1. `KUnal_tez_org_tr.md` baştan sona ayrıntılı okuma (anchor okuma)
2. Her tez bölümü → IJPVP makale section + paragraf + kelime tahsisi tablosu
3. WP0b doğrulama: critical SCF eşiği veriden nasıl çıkıyor (sayı/eğri/band)
4. V3 baseline koşusu gerekliliği netleşir
5. Anchor figure ön tasarımı

İskelet bölüm tahsisi (WP1'de revize edilecek):
| § | Bölüm | Kelime |
|---|---|---|
| 1 | Introduction | ~700 |
| 2 | Background: API 5L X70 + ILI ripple characterization | ~800 |
| 3 | Theoretical Framework: elasticity + SCF basis | ~800 |
| 4 | Numerical Model: FEA setup + V1–V6 validation entegre | ~1200 |
| 5 | Fatigue Methodology: Markl + rainflow + Miner + S-N calibration | ~1000 |
| 6 | Results: parametric SCF + pressure spectra + Miner damage | ~1500 |
| 7 | Discussion: critical SCF threshold + FFS implications + limitations | ~1000 |
| 8 | Conclusions | ~300 |
| | **Toplam** | **~7300** |

### WP2 — Literatür ve Citation Haritası
**Çıktı:** `Docs/plan/WP2_citation_targets.md`

- Tezdeki referansları sınıflandır: EN peer-reviewed (kullanılır) vs TR/standart-doküman (EN alternatif aranır)
- IJPVP-uyumlu kritik referans kümeleri:
  - API 5L X70 mekanik davranışı (örn. Hashemi, Hillenbrand çalışmaları)
  - ILI caliper + ripple/dent karakterizasyonu (örn. Rosenfeld, Macia, Race)
  - SCF analytical/numerical (Pilkey + ripple-spesifik son 10 yıl)
  - Markl + Wais + ASME B31.4/B31.8 background
  - Pipeline pressure cycle fatigue (örn. Kiefner, Rosenfeld)
- IPC 2002-27124 ana validation referansı olarak vurgulu
- Citation verification: WP6'da `citation-verification` SOP'undan geçer

### WP3 — Şekil ve Tablo Stratejisi
**Çıktı:** `Docs/plan/WP3_figures_tables.md`

- Mevcut 18 şekil için karar matrisi (tut / EN-caption / yeniden çiz / birleştir / çıkar)
- Hedef: 6–8 main figure + 2–3 supplementary
- **Mutlak yeniden üretilecekler:**
  - Critical SCF threshold curve (anchor figure)
  - FEA model şeması (geometri + BC + mesh composite panel)
  - Validation karşılaştırma figürü (V4 — IPC 2002-27124)
  - SCF parametrik kontur/yüzey haritası
  - Rainflow histogram + Miner damage breakdown
- Tablo planı: tezdeki 12 tablodan 3–4 main + supplementary
- K4 disiplini gereği: tüm şekiller yeniden çizilince görsel benzerlik 0

### WP4 — Section Drafting Plan
**Çıktı:** `Docs/plan/WP4_section_drafting_plan.md`

Her section için:
- Kaynak tez satır aralıkları (`KUnal_tez_org_tr.md:NN-MM`)
- Tek cümlelik amacı (IJPVP hakemine ne ispatlıyor)
- Argüman zinciri (3–5 bullet)
- Şekil/tablo bağı
- Kelime hedefi
- WP0d (rewrite SOP) entegrasyonu

### WP5 — Drafting (her section ayrı oturum)
- **Her oturum başında:** WP0d SOP kontrol listesi
- Akış: TR oku → EN bullet skeleton → TR kapat → EN prose
- Section sonu: `writing-anti-ai` ile AI-tone temizliği
- Yazar onayı → bir sonraki section

### WP6 — Citation Verification + BibTeX
- Her referans `citation-verification` SOP'undan geçer (DOI, başlık, yıl, sayfa kontrolü)
- BibTeX üretilir (`Docs/paper/references.bib`)
- Atıf-metin tutarlılık check

### WP7 — Self-Review + LaTeX + Submission Package
- `paper-self-review` ile sistematik kontrol
- IJPVP LaTeX template (Elsevier `els-cas-templates` / `cas-sc`)
- Submission package:
  - Cover letter (K4 şeffaflık paragrafı dahil)
  - Highlights (3–5 madde)
  - Graphical abstract
  - Novelty statement
  - CRediT author statement
  - Data availability statement
- iThenticate skor check
- Submit

---

## 5. Risk Tablosu (revize)

| Risk | Şiddet | Mitigation | Karar tetiği |
|---|---|---|---|
| V1 mesh independence eksikliği | Orta | DOF argümanı + literatür kıyaslama; ideal: 1–2 ek koşu | Methodology yazımı / hakem 1. tur |
| V3 baseline analitik benchmark eksikliği | Düşük-orta | 30 dk'lık 1 ek FEA + Lame karşılaştırma | Methodology yazımı |
| iThenticate yüksek skor (K4) | **Yüksek** | WP0d SOP + cover letter şeffaflık + WP3 şekil yeniden çizim + self-cite | WP5 başlangıcı |
| Critical SCF eşiği veriden net çıkmaması | Orta | WP0b ayrıntılı okuma; gerekirse framing "fitness-for-service envelope"e yumuşatılır | WP1 sırasında |
| Tezdeki TR referansların EN karşılığı zayıf | Düşük | WP2 alternatif EN referans havuzu | WP2 |
| IJPVP'den ret | Düşük (scope-fit iyi) | Tier-2: IJF veya EFA; revize maliyeti orta | Submit sonrası |
| 18 şeklin telif/dergi izin durumu | Çok düşük (tez yazarın) | Yeniden çizim zaten planda | WP3 |

---

## 6. Sonraki Somut Adım

**WP1 başlatılır.** İlk eylemler:
1. `KUnal_tez_org_tr.md` baştan sona ayrıntılı okuma
2. Tez bölümleri → IJPVP makale section haritası tablosu üretimi
3. WP0b doğrulama: critical SCF eşiğinin veriden çıkış biçimi (tek sayı / eğri / D/t band)
4. V3 baseline FEA koşusu gerekliliği netleşmesi
5. Çıktı: `Docs/plan/WP1_thesis_to_paper_map.md`

**Yazar onayı bekleniyor:** WP1'i başlatayım mı, yoksa bu plan üzerinde revizyon var mı?

---

## Sürüm
- **v1 — 2026-05-26** — İlk konsolide plan; K1 sabit (IJPVP), K2 yazar verisi entegre, K3 IJPVP pitch, K4 log
