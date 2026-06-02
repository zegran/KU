# WP4 — Tables + Equation Derivations

> **WP:** WP4 (execution-plan v2)
> **Skill:** `publication-chart-skill` (primary, tablolar) + `ml-paper-writing` (support, notasyon)
> **Tarih:** 2026-06-02
> **Durum:** TASLAK — yazar checkpoint onayı bekliyor (§5)
> **Çıktılar:** `Docs/paper/tables/{main,supplementary}_tables.tex` · `Docs/paper/figures/equations/equations.tex`

---

## 0. WP4 Kapsamı (execution-plan v2)
1. 12 tez tablosu → 3-4 main + supplementary konsolidasyon.
2. 6+ denklem türetimi (LaTeX, tutarlı notasyon).
3. Notasyon tutarsızlıklarının düzeltilmesi.

---

## 1. Tablo Konsolidasyonu (12 tez → 4 main + 3 supp)

| Paper tablo | İçerik | Tez kaynağı | Section |
|---|---|---|---|
| **T1** `tab:model` | Sayısal model + malzeme özeti | Tablo 3.1 + L667 (E,ν) | Methods |
| **T2** `tab:validation` | V&V (end-cap + IPC2002 benchmark) | Tablo 3.2 + 3.3 + 3.4 | Methods |
| **T3** `tab:parametric` | Parametrik geometri + SCF özeti | Tablo 3.5 + 3.6/3.7/3.8 özet | Results |
| **T4** `tab:threshold` | Yorulma duyarlılık + kritik eşik + spektrum | Tablo 3.11 + 3.12 | Results/Discussion |
| TS1 `tab:l9full` | Tam Taguchi L9 × 3 (27 satır) | Tablo 3.6/3.7/3.8 | Supplementary |
| TS2 `tab:maopcycle` | Tek MAOP çevrimi N_f | Tablo 3.10 | Supplementary |
| TS3 `tab:dpdamage` | ΔP/MAOP bağıl hasar | Tablo 3.9 | Supplementary |

**12 → 7 (4 main + 3 supp).** Tablo 3.6/3.7/3.8 (3 ayrı L9) tek TS1'de birleşti; 3.2/3.3/3.4 tek T2'de; 3.11/3.12 tek T4'te.

> TS1 (27 satır) `gen_supp_tables.py` ile `fig_data.py`'den **otomatik üretildi** (transkripsiyon hatası riski yok). Satır sayısı doğrulandı: 27.

---

## 2. Denklem Seti (E1–E10, `equations.tex`)

| E | İçerik | Tez denklemi | Not |
|---|---|---|---|
| E1 | Thin-shell σ_h=PR/t, σ_L=PR/2t | 3.1 | — |
| E2 | Flexural rigidity D_f=Et³/12(1−ν²) | 3.3 | **D_f** (D çakışması çözüldü) |
| E3 | SCF_P = σ_max/σ_nom | 3.2/3.7 | — |
| E4 | End-cap F_cap=P·πR_i² | 3.4 | — |
| E5 | IPC2002 referans korelasyon | 3.8 | (a/C)^−2.87 — karşılaştırma |
| E6 | **LD-SCF regresyon (THIS WORK)** | 3.10 | R²=0.916 — **kutulu**, ana katkı |
| E6b | Log-lineer OLS formu | 3.9 | türetme |
| E7 | Markl N_f=(C'/(SCF·S_a))⁵ | 3.11→3.12 | C'=1126 MPa |
| E8 | S_a=Δσ_h/2=½σ_h(ΔP/MAOP) | 3.13 | — |
| E9 | Miner D_M=Σn_i/N_i, t_est=1/D_yr | 3.14-3.16 | **D_M** (damage) |
| E10 | **SCF_crit=C'/(S_a(n·T)^0.2) (THIS WORK)** | — (WP1 türevi) | **kutulu**, Tablo 3.11 genelleştirmesi |

> Execution-plan "6 denklem" diyordu; LD-SCF (E6) ve closed-form eşik (E10) tezin **iki özgün katkısı** olduğundan set 10'a genişletildi. E5 (IPC) karşılaştırma için zorunlu.

---

## 3. 🔴 Notasyon Düzeltmeleri (tez → paper)

| Sorun | Tez | Paper düzeltmesi |
|---|---|---|
| **D üçlü çakışma** | D = çap, D = flexural rigidity (3.3), D = Miner hasar (3.14) | **D**=dış çap · **D_f**=flexural rigidity · **D_M**=Miner hasar |
| Çift denklem 3.12 | Markl N_f hem 3.11→3.12 hem 3.12 olarak iki kez | E7 tek denklem; SCF_P sürümü inline |
| Tablo numarası | Satır 1075 "Tablo 7.1" ama caption 3.9 | TS3 olarak tek numara |
| i ≡ SCF | Markl i (SIF) = SCF_P eşdeğerliği | Metinde 1 cümle ile açık belirtilir |

---

## 4. ⚠ Veri Tutarsızlık Bayrakları (WP5/WP6a'da çözülecek)

1. **36" ortalama SCF:** Tez metni (satır 933) **1.96** diyor; ancak tezin kendi 36" L9 tablosunun (Tablo 3.8) 9 değerinin ortalaması **1.89**. T3'te 1.89 (tablo-tutarlı) kullanıldı + dipnotla flag. WP5'te çözülmeli (1.96 muhtemelen sweep noktalarını içeriyor).
2. **a/C sapma işaretleri** (WP3b'de yakalandı): satır 955 prose'u ters; figür/T-veri doğru. Bkz. `logs/2026-06-02-09`.
3. **Sürüm tutarsızlıkları** (WP2'den): V&V 10-2006/2019, Abaqus 2020/2024 — T1'de Abaqus **2020** (metin tutarlı) kullanıldı.

---

## 5. Yazar Checkpoint — Onay Bekleyen

- [ ] 4 main + 3 supplementary tablo konsolidasyonu onaylanıyor mu?
- [ ] Denklem seti E1–E10 (10 denklem, LD-SCF + SCF_crit kutulu) onaylanıyor mu?
- [ ] Notasyon düzeltmeleri (D_f, D_M ayrımı) onaylanıyor mu?
- [ ] 36" ortalama 1.89 vs 1.96: hangisi otoriter? (T3 dipnotu buna göre güncellenir)

---

## 6. WP5a'ya Devir
- T1/T2 + E1-E4/E7-E8 → Methods
- T3/T4 + E5/E6/E9/E10 → Results
- LaTeX tablolar WP7d'de `main.tex`'e `\input{}` ile bağlanır
- E6 (LD-SCF) + E10 (SCF_crit) = paper'ın iki kutulu özgün denklemi

---

## Sürüm
- **v1 (taslak) — 2026-06-02** — 12→7 tablo konsolidasyon (4 main LaTeX + 3 supp auto-gen) + 10 denklem (notasyon disambig) + 3 tutarsızlık bayrağı. Yazar checkpoint bekliyor.
