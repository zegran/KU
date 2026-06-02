# Tez → IJPVP Makale Uygulama (Execution) Planı — v2

> **Revision Rationale (v1 → v2):**
> v1, WP'leri topik gruplandırmasıyla (planlama → draft → review) sıralamıştı; profesyonel makale yazım sırasını yansıtmıyordu. v2'de Methods önce yazılır (en faktüel, momentum sağlar), Introduction sondan ikinci (hikaye ancak içerik bittikten sonra netleşir), Abstract + Title en son (gerçek içeriği yansıtmak için). Figürler **metinden önce** kilitlenir (figür-driven narrative). Quality assurance (WP6) tek paket halinde drafting'ten ayrıldı. Submission package (WP7) modüler alt-paketlere bölündü. v1 yedeği: `Docs/plan/archive/2026-05-26-execution-plan-IJPVP-v1.md`.

**Tarih:** 2026-05-26
**Referans plan:** `Docs/plan/2026-05-26-paper-plan-IJPVP-v1.md`
**IJPVP otoriter referans:** `Docs/refs/IJPVP_official_sources.md` v2 (FROZEN)
**Sorumluluk matrisi:** `Docs/plan/2026-05-26-responsibility-matrix.md`
**Skill mapping:** `Docs/plan/WP_skill_mapping.md`

**Kısıt:**
- Yazar onayı olmadan hiçbir WP başlatılmaz veya atlanmaz
- Original article: **6.000 kelime max**
- Her WP başında ilgili skill `Skill()` ile aktive edilir (mapping dosyasına göre)
- Her WP tamamlandığında `logs/` altına satır eklenir

---

## Güncel Durum (2026-06-02 itibarıyla)

| WP | Durum | Çıktı |
|---|---|---|
| WP0a–d | ✅ | gate'ler + WP0d SOP (K4 yazar-üstlenimli) |
| WP1 | ✅ | `WP1_thesis_to_paper_map.md` (Section A 5-fold, closed-form SCF_crit) |
| WP2 | ✅ | `WP2_citation_pool.md` (~54 ref, dergi 2→15) |
| WP3a | ✅ | `WP3a_figure_strategy.md` (7 main + 3 supp) |
| WP3b | ✅ | `Docs/paper/figures/` 10 figür + manifest (anchor MF7 doğrulandı) |
| WP4 | ✅ | `tables/*.tex` (4 main + 3 supp) + `equations.tex` (E1–E10) |
| WP5a | ✅ | `sections/04_methods.md` (~1700 kelime) |
| WP5b | ✅ | `sections/05_results.md` (~1300 kelime, IPC a/C işaret düzeltmesi) |
| WP5c | ✅ | `sections/06_discussion.md` (~1050 kelime, anchor closed-form) |
| WP5d | ✅ | `sections/07_conclusion.md` (~230 kelime) |
| WP5e | ✅ | `sections/01_introduction.md` (~950 kelime) |
| WP5f | ✅ | `sections/00_abstract_title.md` (Title 15w, Abstract 196w, 6 keyword) |
| WP5g | ✅ | `submission/Highlights.md` (5 bullet ≤85 char) |
| **WP6a** | ⏳ **sıradaki** | Coherence pass (QA bayraklarını çözer) |
| WP6b–WP8 | ⏳ | bekliyor |

**İlerleme: 16/26 WP.** Tam manuscript taslağı (~5230/6000 kelime) + figür+tablo+denklem+abstract+highlights. Kalite fazı (WP6) sıradaki.
**Açık QA (WP6a):** 36" ortalama 1.89 vs tez-metni 1.96; a/C sapma işaretleri (L955) Results'ta formülden düzeltildi (teyit); notasyon D/D_f/D_M; sürüm tutarsızlıkları; çapraz referans; provisional citation [n].

---

## Sıralı Akış (v2)

```
WP1 → WP2 ──┐
            ├─→ WP3a → WP3b ──┐
WP4 ────────┘                  ├─→ WP5a → WP5b → WP5c → WP5d → WP5e → WP5f → WP5g
                               │       (Methods → Results → Discussion → Conclusion → Intro → Abstract+Title → Highlights)
                               │
                               └─→ WP6a → WP6b → WP6c → WP6d
                                          (Coherence → Citation → Anti-AI → iThenticate)
                                          ↓
                               WP7a, WP7b, WP7c, WP7d, WP7e
                                          ↓
                                        WP8 Submission
```

---

## WP1 — Thesis-to-Paper Mapping + IMRaD Spine

- **Tetikleyici:** `WP1 başlat`
- **Skill:** `superpowers:writing-plans` (primary) + `doc-coauthoring` (support)
- **Çıktı:** `Docs/plan/WP1_thesis_to_paper_map.md`
- **İçerik:**
  - Tezi baştan sona ayrıntılı okuma
  - IMRaD spine: her tez bölümü → IJPVP section + paragraf + **6.000 kelime hedefi içinde** tahsis
  - Anchor figure (kritik SCF eşik eğrisi) için veri ihtiyacı
  - V1 mesh + V3 baseline ek koşu kararları
  - Section-başı kelime tahsisi: §1≈600, §2≈700, §3≈700, §4≈1.000, §5≈850, §6≈1.200, §7≈750, §8≈200
- **Checkpoint:** Yazar haritayı + kelime tahsisini + anchor figure veri planını onaylar
- **Süre:** 2–3 oturum
- **Log:** `WP1 — superpowers:writing-plans — completed YYYY-MM-DD HH:MM`

---

## WP2 — Citation Pool (40–60 EN kaynak)

- **Tetikleyici:** `WP2 başlat`
- **Skill:** `citation-verification` (primary) + `daily-paper-generator` (support)
- **Çıktı:** `Docs/plan/WP2_citation_pool.md`
- **İçerik:**
  - Tezdeki 33 referans: EN peer-reviewed / TR / standart-doküman / web kategorize
  - IJPVP-uyumlu eksik kümeler önerisi (API 5L X70, ILI ripple/dent, SCF analytical, Markl/Wais, pipeline fatigue)
  - IPC 2002-27124, Rosenfeld, Macia, Race, Kiefner anchor referansları
  - Elsevier numbered style ([n]) formatına hazırlık
- **Checkpoint:** Yazar referans havuzu kapsamını onaylar
- **Süre:** 2–3 oturum
- **Log:** `WP2 — citation-verification — completed ...`
- **🟡 Yazar girdisi:** erişilemeyen referansların doğrulanması

---

## WP3a — Figür Stratejisi (Karar Aşaması)

- **Tetikleyici:** `WP3a başlat`
- **Skill:** `publication-chart-skill` (primary) + `matplotlib-visualization` (support)
- **Çıktı:** `Docs/plan/WP3a_figure_strategy.md`
- **İçerik:**
  - 18 tez şekli karar matrisi (tut / EN-caption / yeniden çiz / birleştir / çıkar)
  - Hedef envanter: 6–8 main + 2–3 supplementary
  - Her main figür: amaç, veri kaynağı, eksen etiketleri, legend, stil
  - **Anchor figure (F8): critical SCF threshold eğrisi** parametrik veri ihtiyacı
- **Checkpoint:** Yazar figür envanteri + anchor figure veri girdilerini onaylar
- **Süre:** 1–2 oturum

---

## WP3b — Figür Üretimi

- **Tetikleyici:** `WP3b başlat` (WP3a onayı sonrası)
- **Skill:** `publication-chart-skill` + `matplotlib-visualization`
- **Çıktı:** `Docs/paper/figures/figN_*.svg` veya `.pdf` (vektör; PNG yedek)
- **İçerik:**
  - F1 FEA model şeması composite panel
  - F2 Ripple geometri parametre tanımı
  - F3 IPC2002-27124 validation karşılaştırması (V4)
  - F4 Mesh independence (V1, opsiyonel)
  - F5 SCF parametrik kontur/yüzey haritası
  - F6 Markl S-N + kalibrasyon (V5)
  - F7 Rainflow histogram + Miner damage breakdown
  - **F8 Critical SCF threshold curve (anchor)**
- **Checkpoint:** Yazar her figürün görsel kalitesini onaylar
- **Süre:** 3–5 oturum
- **🟡 Yazar girdisi:** Anchor F8 parametrik veri seti

---

## WP4 — Tablolar + Denklem Türetimleri

- **Tetikleyici:** `WP4 başlat` (WP3a ile paralel ya da sonra)
- **Skill:** `publication-chart-skill` (tablolar) + `ml-paper-writing` (notasyon disiplini)
- **Çıktı:**
  - `Docs/plan/WP4_tables_equations.md`
  - `Docs/paper/figures/equations/` (LaTeX kaynaklı türetimler)
- **İçerik:**
  - 12 tez tablosundan 3–4 main + supplementary
  - T1 Material properties (API 5L X70)
  - T2 FEA model özet
  - T3 SCF parametrik vakalar
  - T4 Miner damage senaryoları
  - 6 denklem (E1 thin-shell, E2 SCF, E3 end-cap, E4 Markl, E5 Miner, E6 S-N calibration)
- **Checkpoint:** Yazar tablo + denklem son hâlini onaylar
- **Süre:** 1–2 oturum

---

## WP5a — Methods (En Önce)

- **Tetikleyici:** `WP5a başlat` (WP1+WP2+WP3a+WP4 onayları sonrası)
- **Skill:** `ml-paper-writing` (primary) + `doc-coauthoring` (support)
- **Çıktı:** `Docs/paper/sections/04_methods.md` (~1.000 kelime — §4 + §5 birleşik)
- **İçerik:** Numerical model setup, BC, mesh, element, validation alt-bölümü (V1–V6); fatigue methodology (Markl + rainflow + Miner + S-N calibration)
- **Mantık:** Methods en faktüel bölüm; momentum sağlar; F1/F2/F3/F4/F6 figürleri ve T2 tablosu bu bölümde
- **WP0d SOP:** her oturum başında çalıştırılır (TR oku → bullet skeleton → close source → EN prose)
- **Checkpoint:** Yazar onaylar
- **Süre:** 2 oturum

---

## WP5b — Results

- **Tetikleyici:** `WP5b başlat`
- **Skill:** `ml-paper-writing` + `results-analysis`
- **Çıktı:** `Docs/paper/sections/05_results.md` (~1.200 kelime — §6)
- **İçerik:** Parametric SCF (Taguchi L9 × 3), LD-SCF regression, IPC formula comparison, pressure spectrum analysis, Miner damage senaryoları, **critical SCF threshold** (T3, T4 + F5, F7, F8)
- **Checkpoint:** Yazar onaylar
- **Süre:** 2 oturum

---

## WP5c — Discussion

- **Tetikleyici:** `WP5c başlat`
- **Skill:** `ml-paper-writing` + `doc-coauthoring`
- **Çıktı:** `Docs/paper/sections/06_discussion.md` (~750 kelime — §7)
- **İçerik:** Critical SCF threshold yorumu, FFS implications, IPC2002 sapma analizi, D/t=73.1 sınırı, mixed spectrum bulgusu, limitations
- **Checkpoint:** Yazar onaylar
- **Süre:** 1–2 oturum

---

## WP5d — Conclusion

- **Tetikleyici:** `WP5d başlat`
- **Skill:** `ml-paper-writing`
- **Çıktı:** `Docs/paper/sections/07_conclusion.md` (~200 kelime — §8)
- **İçerik:** 3–4 madde net özet + future work
- **Checkpoint:** Yazar onaylar
- **Süre:** 1 oturum

---

## WP5e — Introduction (Sondan İkinci)

- **Tetikleyici:** `WP5e başlat`
- **Skill:** `ml-paper-writing` + `research-ideation`
- **Çıktı:** `Docs/paper/sections/01_introduction.md` (~600 kelime — §1)
- **İçerik:** Motivation → API 5L X70 + field bending + ripple → IPC2002 boşluğu → bu çalışmanın katkısı
- **Mantık:** Methods + Results + Conclusion bittikten sonra hikaye net olur; Introduction artık keşif değil, içeriği konumlandırma görevi yapar
- **Checkpoint:** Yazar onaylar
- **Süre:** 1–2 oturum

---

## WP5f — Abstract + Title (Son)

- **Tetikleyici:** `WP5f başlat`
- **Skill:** `ml-paper-writing` + `doc-coauthoring`
- **Çıktı:** `Docs/paper/sections/00_abstract_title.md`
- **İçerik:** Title (≤15 kelime), abstract (yapılandırılmamış, 150–250 kelime — ⚠ kesin limit IJPVP_official_sources v2'de henüz açık), keywords (1–7, and/of bağlaçsız)
- **Checkpoint:** Yazar onaylar
- **Süre:** 1 oturum

---

## WP5g — Highlights

- **Tetikleyici:** `WP5g başlat`
- **Skill:** `ml-paper-writing`
- **Çıktı:** `Docs/paper/submission/Highlights.md`
- **İçerik:** 3–5 bullet, her biri ≤85 karakter, novel sonuç + yeni yöntem yakalayan
- **Checkpoint:** Yazar onaylar
- **Süre:** 1 oturum

---

## WP6a — Coherence Pass

- **Tetikleyici:** `WP6a başlat`
- **Skill:** `paper-self-review`
- **Çıktı:** `Docs/plan/WP6a_coherence_report.md`
- **İçerik:** Bölümler arası tutarlılık (notation, terminology, figure/table referansları, denklem numaraları), argüman zinciri kontrolü, gereksiz tekrar tespiti
- **Checkpoint:** Yazar revize listesini onaylar
- **Süre:** 1–2 oturum

---

## WP6b — Citation Verification

- **Tetikleyici:** `WP6b başlat`
- **Skill:** `citation-verification`
- **Çıktı:** `Docs/paper/references.bib` + `Docs/plan/WP6b_citation_verification_report.md`
- **İçerik:** Her referans DOI + başlık + yıl + dergi + erişim doğrulaması; Elsevier numbered style formatı; metin-liste tutarlılık
- **Checkpoint:** Yazar onaylar
- **Süre:** 2 oturum

---

## WP6c — Anti-AI / Language Polish

- **Tetikleyici:** `WP6c başlat`
- **Skill:** `writing-anti-ai`
- **Çıktı:** Her section dosyasının revize hâli + `Docs/plan/WP6c_polish_report.md`
- **İçerik:** AI-tone temizliği, inflated/promotional language çıkarılır, doğal akademik ton, EN-US tutarlılık
- **Checkpoint:** Yazar onaylar
- **Süre:** 1–2 oturum

---

## WP6d — iThenticate Check (🔴 Yazar Tarafı)

- **Tetikleyici:** Yazar bunu manuel yapar (CLI yapamaz)
- **Skill:** — (sistem dışı)
- **Çıktı:** iThenticate raporu PDF (yazar yükler)
- **İçerik:** Hedef <%15 tezden örtüşme; >%15 ise WP6c'ye geri dönüş
- **Checkpoint:** Yazar raporu paylaşır + karar
- **Süre:** 1–3 gün takvim

---

## WP7a — Cover Letter + Novelty Statement

- **Tetikleyici:** `WP7a başlat`
- **Skill:** `doc-coauthoring` + `ml-paper-writing`
- **Çıktı:** `Docs/paper/submission/cover_letter.md` + `novelty_statement.md`
- **İçerik:** Editöre net katkı + scope-fit + K4 şeffaflık paragrafı (thesis-derived disclosure)
- **Checkpoint:** Yazar onaylar
- **Süre:** 1 oturum

---

## WP7b — Graphical Abstract

- **Tetikleyici:** `WP7b başlat`
- **Skill:** `publication-chart-skill`
- **Çıktı:** `Docs/paper/submission/graphical_abstract.svg`
- **İçerik:** F8 (anchor) basitleştirilmiş + akış oku; tek panel
- **Checkpoint:** Yazar onaylar
- **Süre:** 1 oturum

---

## WP7c — CRediT + Declarations + Data Availability (🟡 Yazar Girdisi)

- **Tetikleyici:** `WP7c başlat`
- **Skill:** `doc-coauthoring`
- **Çıktı:** `Docs/paper/submission/credit_statement.md` + `declarations.md` + `data_availability.md`
- **İçerik:** Yazar rolleri, funding, conflict, ethical, FEA model + dataset paylaşım kararı
- **Checkpoint:** Yazar tüm declaration alanlarını doldurur
- **Süre:** 1 oturum + yazar bilgi sağlama

---

## WP7d — LaTeX Migration (elsarticle)

- **Tetikleyici:** `WP7d başlat`
- **Skill:** `latex-conference-template-organizer`
- **Çıktı:** `Docs/paper/main.tex` + tüm section'lar `\input{}` ile bağlı
- **İçerik:** Elsevier `cas-sc` veya `els-cas-templates` (CAS — Complete Article Submission) iskelet; tüm markdown → LaTeX; figür referansları; bibTeX bağlantısı
- **Checkpoint:** PDF derlemesi başarılı + yazar görsel kontrol
- **Süre:** 1–2 oturum

---

## WP7e — Final Self-Review

- **Tetikleyici:** `WP7e başlat`
- **Skill:** `paper-self-review`
- **Çıktı:** `Docs/plan/WP7e_final_review_report.md`
- **İçerik:** Submission-ready kontrol listesi; tüm IJPVP frontmatter zorunlulukları; figure/table caption tutarlılığı; reference completeness; word count ≤ 6.000
- **Checkpoint:** Yazar onaylar — submit'e hazır
- **Süre:** 1 oturum

---

## WP8 — Submission (🔴 Yazar Tarafı)

- **Tetikleyici:** Yazar Editorial Manager'a yükler
- **URL:** https://www.editorialmanager.com/IPVP
- **Skill:** — (sistem dışı)
- **Çıktı:** Submission ID + acknowledgment
- **Süre:** 1–2 saat yazar zamanı + sistem işleme

---

## Toplam Tahmini Süre (revize)

| Aşama | CLI oturum | CLI saat | Yazar/dış bekleme |
|---|---|---|---|
| WP1 | 2–3 | 3–6 | 1–2 gün |
| WP2 | 2–3 | 3–5 | 1–3 gün |
| WP3a + WP3b | 4–7 | 5–10 | 1–3 gün |
| WP4 | 1–2 | 2–4 | 1 gün |
| WP5a (Methods) | 2 | 3–5 | 1–2 gün |
| WP5b (Results) | 2 | 3–5 | 1–2 gün |
| WP5c (Discussion) | 1–2 | 2–4 | 1–2 gün |
| WP5d (Conclusion) | 1 | 1–2 | 1 gün |
| WP5e (Introduction) | 1–2 | 2–4 | 1–2 gün |
| WP5f (Abstract+Title) | 1 | 1–2 | 1 gün |
| WP5g (Highlights) | 1 | 1 | 1 gün |
| WP6a–c | 4–6 | 5–9 | 2–4 gün |
| WP6d (iThenticate) | — | — | 1–3 gün yazar |
| WP7a–e | 5–7 | 7–12 | 2–5 gün |
| WP8 | — | — | yazar |
| **Toplam** | **27–43 oturum** | **~38–69 CLI saat** | **6–10 hafta takvim** |

---

## Sürüm
- **v2 — 2026-05-26** — Profesyonel yazım sırasına göre yeniden yapılandırılmış WP akışı; v1 yedek arşivde
