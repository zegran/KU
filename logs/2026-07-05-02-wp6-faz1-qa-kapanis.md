# WP6 Faz 1 — QA Kapanışı + Veri Teyidi (Sayısal Zemin)

**Tarih:** 2026-07-05
**Tür:** milestone / wp6-faz1
**Skill:** `paper-self-review` (WP6a sorumlu skill, WP_skill_mapping uyarınca aktive edildi)
**Yazar:** Korcan Ünal

## QA bayrakları — kapanış durumu

| # | Karar | Uygulama |
|---|---|---|
| QA-1 | **1.89 kesin** (yazar kararı + tez v2 kendisi düzeltmiş + hesap: 9 vakanın ortalaması 1.8922) | `main_tables.tex` T3 dipnotundaki "thesis states 1.96" parenteti silindi |
| QA-2 | **OTONOM KARAR: formül-türevli işaretler esas.** Gerekçe: (i) Eq.5'ten hesaplanan sapmalar makale yazımıyla birebir örtüşüyor (a/C=0.25: −30.6…−84.0%; a/C=0.50: +47.9…+437.4%; a/C=0.375: −42.8…+124.7% geçiş); (ii) tezin işaret ataması kendi Δ%=(SEA−IPC)/IPC tanımıyla çelişiyor — bu tanımda −%100'ün altı matematiksel olarak imkânsız, tez −477% yazıyor; (iii) tezin kendi kapanış cümlesi ("geniş ripple'ları hafife almaktadır") makale yönüyle aynı. Tez v2'de paragraf değişmemiş; düzeltme makale tarafında kalıyor | `05_results.md` §3.2 mevcut yazım DOĞRULANDI — değişiklik gerekmez. MF4b/c figürleri de aynı formülden üretildiği için tutarlı |
| QA-3 | **D_m** (tez v2'nin kendi notasyonu). Paper konvansiyonu: D = dış çap, D_f = eğilme rijitliği (paper-tarafı ayrıştırma; tez v2 rijitlikte hâlâ D kullanıyor), D_m = Miner hasarı | `equations.tex` (E9 + konvansiyon yorumu), `04_methods.md` §2.5, `06_discussion.md` §4.1, `main_tables.tex` T4 (D_m,100yr; D_m<1/D_m>1; D_m,yr) |
| QA-4 | **Abaqus/Standard 2020** (tez v2 tablo+metin teyitli — paper zaten doğru) ve **ASME V&V 10-2019** (tez v2 metin satır 646 + kaynakça [16] tutarlı) | Abaqus: değişiklik yok. V&V künyesi Faz 3'te ref listesine işlenecek |
| QA-5 | **Yeniden numaralandırma kararı:** ilk-atıf sırası = numara sırası. Yeni harita: Table 1 = parametrik geometri (ilk atıf §2.2), Table 2 = FE model (§2.3), Table 3 = doğrulama (§2.4), Table 4 = eşik/spektrum (değişmez). Fig/Eq numaraları zaten ilk-atıf sıralı | Uygulama Faz 2'de (section edit'leriyle birlikte, tek geçişte) |

## P2 — çap trendi veri teyidi

- Ortalamalar: 36″ **1.8922**, 48″ **1.7800**, 56″ **1.6767** → tablo değerleri (1.89/1.78/1.68) doğru.
- Trend **9/9 konfigürasyonda monoton** (her L9 vakasında SCF₃₆ > SCF₄₈ > SCF₅₆) — istisnasız.
- 36″/56″ oranı 1.1286 → Discussion'daki "%13" iddiası doğru (12.9%).
- Tez v2 de trendi açıkça yazıyor ("Çap azaldıkça GYF sistematik olarak artmaktadır").
- **Karar:** Trend Discussion'da veri-temelli bulgu olarak KALIR; Abstract'tan çıkarılır (R3, Faz 2'de).

## Tez v2 kaynaklı sayısal güncellemeler (B1–B3, Faz 0 etki analizinden)

1. **Mesh convergence** (`04_methods.md` §2.3): "progressively refining" ifadesi somut üç-seviyeli çalışmayla değiştirildi (20/15/10 mm → VM 640.3/672.8/718.6 MPa; en ince ağ benimsendi). "Stable value" iddiası kaldırıldı (veri monotonik artış gösteriyor — hakem-güvenli yazım).
2. **Benchmark** (`04_methods.md` §2.4 + `main_tables.tex` T2): Circ +1.01% → **+4.9%**; VM −11.5% → **−8.3%** (694.1 → 718.6 MPa); Axial −11.5% → **−6.3%** (714.4 → 755.9 MPa); SCF 3.14 → **3.25** (3.143 → 3.254); Rosenfeld Fig.16 bandı (3.0–3.5, D/t≈128) tutarlılık cümlesi eklendi.
3. **Discussion §4.4:** "~11.5% Von Mises farkı" → "~8%".

## Tez-içi tespit (paper'a taşınmadı)
- Tez v2 satır 1107: tek tam MAOP birim hasarı "2,54×10⁻³" yazıyor; doğrusu 1/396 = 2.525×10⁻³ → paper 2.53e-3 (S2) / 2.5×10⁻³ (prose) değerlerini koruyor.
- Tez v2 satır 802 kapanış paragrafı hâlâ "%4–12 / %11,5" diyor (eski kalıntı); güncel tablosu %4.9–8.3. Paper tablo değerlerini kullanıyor.

## Değişen dosyalar
`Docs/paper/sections/04_methods.md` · `Docs/paper/sections/06_discussion.md` · `Docs/paper/tables/main_tables.tex` · `Docs/paper/figures/equations/equations.tex`

## Sonraki adım
Faz 2 — Yapısal/çerçeve düzeltmeleri (M2–M5, R1–R8, P1/P3/P4) + tablo yeniden numaralandırma.
