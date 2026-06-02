# Paper Figure Manifest (WP3b)

> Üretim: matplotlib 3.10.8 + numpy 1.26.4. Çıktı: PDF (vektör) + PNG (600 dpi).
> Scriptler: `scripts/`. Veri: `scripts/fig_data.py` (tüm sayılar tezden birebir).
> Taslak caption'lar EN (WP5 drafting'te rafine edilir). "Fig. N." numaraları LaTeX'te (WP7d) atanır.

## Ana Figürler (7)

| Dosya | Section | Taslak caption (EN, WP5'te rafine) |
|---|---|---|
| `mf1_model_setup` | Methods | Half-symmetric S4R shell model of a field-bend ripple in an API 5L X70 pipe: (a) geometry, mesh and global axes; (b) internal pressure, end-cap force and boundary conditions via RP-1; (c) structured quad mesh detail at the ripple. |
| `mf2_ripple_geometry` | Methods | Ripple geometry parameterisation: (a) longitudinal raised-cosine crest–trough profile (depth d, half-wavelength L/2); (b) circumferential extent θ (a/C). Constant D/t = 73.1, X70, P = 9.55 MPa. |
| `mf3_validation` | Methods | Model validation against IPC2002-27124 (Rosenfeld et al., 2002): (a) S11 hoop-stress contour at the ripple; (b) peak-stress benchmark (end-cap 0.013%, nominal hoop 220.8 MPa analytic, SCF 3.14 vs 3.55). |
| `mf4_parametric_scf` | Results | Parametric SCF_P over Taguchi L9 × three diameters: (a) FEA SCF_P per case; (b) FEA vs IPC2002 (Eq. 3.8); (c) IPC2002 deviation vs circumferential extent a/C. |
| `mf5_ldscf_regression` | Results | LD-SCF empirical regression (Eq. 3.10): (a) predicted vs FEA with ±9% band (R²=0.916, RMSE=0.058); (b) relative residual distribution. |
| `mf6_mixed_spectrum` | Results | Mixed-spectrum annual fatigue-damage distribution for 56″ D7 (SCF_P=1.95): the 80%-MAOP band contributes 68.6% of damage; T_est ≈ 34 yr. |
| `mf7_anchor_scf_threshold` ⭐ | Discussion | **Critical SCF threshold master curve.** Estimated fatigue life vs SCF_P for n = 4/8/12/24 MAOP-equivalent cycles/yr; intersection with the 100-yr design life gives SCF_crit ≈ 1.57 (n=12). FEA configurations overlaid. |

## Supplementary Figürler (3)

| Dosya | Taslak caption |
|---|---|
| `sf1_mesh_quality` | Structured quad mesh quality; aspect ratio ≤ 3 throughout. |
| `sf2_caliper_to_fea` | Schematic geometry-ILI radius map and extraction of representative FEA ripple parameters (L, d, θ/aC). |
| `sf3_stress_contours` | Full stress-component contour set at the ripple: (a) Von Mises, (b) S11 circumferential, (c) S22 axial. |
| `scripts/scf_regression.py` | (WP7) tez EK-1 Python OLS regresyon kodu + README — supplementary. |

## Üretim Notları
- **MF7 anchor closed-form Tablo 3.11 ile birebir doğrulandı** (161/118/76/33/12 yıl; SCF_crit=1.56).
- **MF1/MF3:** mevcut tez PNG'leri (image8/11/13/16) + vektör overlay (yazar kararı; Elsevier ≥500 dpi için "best available").
- **SF2:** telif-güvenli sentetik radius-map (caliper görseli kullanılmadı).
- **QA bulgusu:** MF4'ün IPC sapması formülden hesaplı; tez satır 955 prose'u a/C grup işaretlerini ters yazmış → WP5/WP6a'da figüre göre düzeltilecek (bkz. `logs/2026-06-02-09`).

## Yeniden üretim
```
cd Docs/paper/figures/scripts
python mf7_anchor_scf_threshold.py   # vb. her figür bağımsız
```
