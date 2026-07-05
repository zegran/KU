# Paper Figure Manifest (WP3b; final numbering WP6 Faz 5)

> Üretim: matplotlib 3.10.8 + numpy 1.26.4. Çıktı: PDF (vektör) + PNG (600 dpi).
> Scriptler: `scripts/`. Veri: `scripts/fig_data.py`.
> **Final "Fig. N" numaraları aşağıda sabitlendi** (ilk-atıf sırası; Fig.1 ↔ MF2 takası WP6 Faz 5).
> MF3 ve SF3, tez v2 değerleriyle 2026-07-05'te yeniden üretildi.

## Ana Figürler (7) — final numaralandırma

| Fig | Dosya | Section | Final caption (EN) |
|---|---|---|---|
| **Fig. 1** | `mf2_ripple_geometry` | Methods 2.2 | Ripple geometry parameterisation: (a) longitudinal raised-cosine crest–trough profile (depth d, half-wavelength L/2); (b) circumferential extent θ (a/C). Constant D/t = 73.1, API 5L X70, P = 9.55 MPa. |
| **Fig. 2** | `mf1_model_setup` | Methods 2.3 | Half-symmetric S4R shell model of a field-bend ripple in an API 5L X70 pipe: (a) geometry, mesh and global axes; (b) internal pressure, end-cap force and boundary conditions via RP-1; (c) structured quad mesh detail at the ripple. |
| **Fig. 3** | `mf3_validation` | Methods 2.4 | Model validation against the full-scale benchmark of Rosenfeld et al. [4]: (a) S11 hoop-stress contour at the ripple; (b) peak-stress benchmark (end-cap 0.013%; nominal hoop 220.8 MPa analytic; SCF 3.25 vs 3.55). |
| **Fig. 4** | `mf4_parametric_scf` | Results 3.1–3.2 | Parametric SCF_P over the Taguchi L9 array at three diameters: (a) FEA SCF_P per case; (b) FEA vs the reference correlation (Eq. 8); (c) deviation from Eq. 8 vs circumferential extent a/C. |
| **Fig. 5** | `mf5_ldscf_regression` | Results 3.4 | Empirical SCF correlation (Eq. 9): (a) predicted vs FEA with ±9% band (R² = 0.916, RMSE = 0.058); (b) relative residual distribution. |
| **Fig. 6** | `mf6_mixed_spectrum` | Results 3.5 | Mixed-spectrum annual fatigue-damage distribution for the 56″ D7 case (SCF_P = 1.95): the 80%-MAOP band contributes 68.6% of the damage; t_est ≈ 34 yr. |
| **Fig. 7** ⭐ | `mf7_anchor_scf_threshold` | Discussion 4.1 | **Critical SCF threshold master curve.** Estimated fatigue life vs SCF_P for n = 4/8/12/24 full-MAOP-equivalent cycles/yr; the intersection with the 100-yr design-life line gives SCF_crit ≈ 1.56 at n = 12 (Eq. 10). Parametric FEA configurations overlaid. |

## Supplementary Figürler (3)

| Fig | Dosya | Final caption |
|---|---|---|
| Fig. S1 | `sf1_mesh_quality` | Structured quadrilateral mesh quality; element aspect ratio ≤ 3 throughout. |
| Fig. S2 | `sf2_caliper_to_fea` | Schematic geometry-ILI radius map and extraction of the representative FEA ripple parameters (L, d, θ/aC). |
| Fig. S3 | `sf3_stress_contours` | Full stress-component contour set at the ripple: (a) von Mises, (b) S11 circumferential, (c) S22 axial. |

`scripts/scf_regression.py` — (WP7) tez EK-1 Python OLS regresyon kodu + README — supplementary.

## Üretim Notları
- **MF7 anchor:** closed-form Tablo 3.11 ile birebir doğrulandı (161/118/76/33/12 yıl); **SCF_crit = 1.5619 → metin genelinde ≈1.56** (WP6 Faz 5'te 1.57 yuvarlama hatası düzeltildi).
- **MF3:** tez v2 benchmark değerleriyle yeniden üretildi (718.6/796.8/755.9 MPa; −8.3/+4.9/−6.3%; SCF 3.25 vs 3.55).
- **MF1/MF3 raster panelleri:** tez PNG'leri (image8/11/13/16) + vektör overlay (yazar kararı; Elsevier ≥500 dpi için "best available").
- **SF2:** telif-güvenli sentetik radius-map (caliper görseli kullanılmadı).
- **QA-2 (kapandı):** MF4 IPC sapması formülden hesaplı; tez satır 955 işaretleri kendi tanımıyla çelişiyor; formül-türevli işaretler esas (bkz. `logs/2026-07-05-02`).

## Yeniden üretim
```
cd Docs/paper/figures/scripts
python mf7_anchor_scf_threshold.py   # vb. her figür bağımsız
```
