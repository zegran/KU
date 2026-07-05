# WP6 Faz 5 — Tutarlılık Son Turu (Self-Review)

**Tarih:** 2026-07-05/06
**Tür:** milestone / wp6-faz5
**Skill:** `paper-self-review` (uçtan uca okuma + mekanik denetimler)
**Yazar:** Korcan Ünal

## Yakalanan ve düzeltilen tutarsızlıklar

### 1. 🔴 SCF_crit 1.57 → **1.56** (sayısal hata düzeltmesi)
Kesin hesap: SCF_crit = C′/(S_a·(nT)^0.2) = 1126/(174.6·1200^0.2) = **1.5619**. MF7 figürü zaten 1.56 gösteriyordu; metindeki "≈1.57" WP1 dönemi yuvarlama hatasıydı (1.5619 → 1.56'ya yuvarlanır). Düzeltilen 5 konum: Abstract, Discussion §4.1, Conclusion #4, Table 4 caption, Highlights. Metin–figür çelişkisi kapandı.

### 2. Figür numarası takası (ilk-atıf sırası)
Fig. 2 (ripple geometry, §2.2) metinde Fig. 1'den (half model, §2.3) önce anılıyordu → takas: **Fig. 1 = mf2_ripple_geometry, Fig. 2 = mf1_model_setup**. Metin ve manifest güncellendi.

### 3. Denklem yeniden numaralandırması (görünüm sırası)
Eski E5 (IPC) ve E6 (LD-SCF) ilk kez Results'ta görünürken E7–E9 Methods'ta daha önce geçiyordu → yeni sıra: Eq.1–4 (Methods 2.1–2.3), **Eq.5 Markl, Eq.6 S_a, Eq.7 Miner** (Methods 2.5), **Eq.8 IPC** (Results 3.2), **Eq.9 (+9b) LD-SCF** (Results 3.4), Eq.10 SCF_crit (Discussion). `equations.tex` fiziksel olarak yeniden sıralandı; 12 metin-içi atıf güncellendi (Methods 3, Results 3, Discussion 5, Conclusion 1).

### 4. Supplementary tablo takası
Table S3 (dpdamage) S2'den (maopcycle) önce anılıyordu → **S2 = dpdamage, S3 = maopcycle**; `supplementary_tables.tex` blok sırası ve Results §3.5 atıfları düzeltildi.

### 5. MF3 + SF3 figürleri yeniden üretildi
MF3 script'inde v1 benchmark değerleri hardcoded idi (694.1/772.2/714.4; −11.5/+1.01/−11.5; SCF 3.14) → tez v2 değerleriyle güncellendi (718.6/796.8/755.9; −8.3/+4.9/−6.3; SCF 3.25) ve figür yeniden üretildi. Başlık "Benchmark vs IPC2002-27124" → "Benchmark vs Rosenfeld et al. (2002)" (M2 uyumu). SF3 "Von Mises" → "von Mises" ile yeniden üretildi.

### 6. Stil
Discussion cümle içi "Figure 7" → "Fig. 7" (Elsevier konvansiyonu: cümle başında "Figure", içinde "Fig.").

## Temiz çıkan denetimler
- **Sayı/iddia eşleşmesi:** 1.42–2.37, 1.89/1.78/1.68, %13 (12.9), −84/+400%, R²=0.916, RMSE 0.058, max %9, 3.25/3.55, +4.9/−8.3/−6.3, 396/249/149, 2.90×10⁻², ~34 yıl — tüm geçişler tutarlı.
- **Abstract kalitatif ↔ gövde sayısal (P3/R5):** "more than half" (Abstract+Conclusion) ↔ 68.6% (Results 3.5 + Discussion 4.3 + Table 4) ✓.
- **M2 sayımı:** "IPC2002" markası prozda tam 1 geçiş (Discussion 4.2); Rosenfeld adı 6 geçiş (Intro 1, Methods 2 [benchmark + C′], Results 1, Discussion 2) — hedef dağılımda.
- **Atıf-referans eşleşmesi:** 30/30, ilk-atıf sıralı; bayat [E1]/[F4]/[VERIFY]/eski numara kalıntısı yok.
- **Notasyon:** D/D_f/D_m ayrımı metin+tablo+denklem genelinde tutarlı; von Mises normalize.
- **First-mention sıra denetimi (son hal):** Eq.1→2→3, T1, F1, TS1, T2, F2, Eq.4, T3, F3, Eq.5→6→7, F4, Eq.8, Eq.9, F5, TS2, TS3, T4, F6, Eq.10, F7 — **tam sıralı** ✓.

## Değişen dosyalar
`00_abstract_title.md` · `04_methods.md` · `05_results.md` · `06_discussion.md` · `07_conclusion.md` · `submission/Highlights.md` · `tables/main_tables.tex` · `tables/supplementary_tables.tex` · `figures/equations/equations.tex` · `figures/README.md` · `figures/scripts/mf3_validation.py` · `figures/scripts/sf3_stress_contours.py` · `figures/mf3_validation.{pdf,png}` · `figures/sf3_stress_contours.{pdf,png}`

## Sonraki adım
Faz 6 — M6 final docx montajı (`Unal_ripple_SCF_fatigue_IJPVP_R2.docx`).
