# WP3a — Figure Strategy (Karar Aşaması)

> **WP:** WP3a (execution-plan v2) — **karar/strateji**; üretim WP3b'de
> **Skill:** `publication-chart-skill` (primary) + `matplotlib-visualization` (support)
> **Tarih:** 2026-06-02
> **Durum:** ✅ CHECKPOINT ONAYLANDI (2026-06-02) — F8 **n=4/8/12/24** (closed-form), MF1/MF3 **mevcut PNG'lerden**. WP3b başlatılabilir. Son açık-uçlu nokta (SCADA) kapandı.
> **K4 zorunluluk:** Hard rule #5 — **hiçbir tez şekli olduğu gibi kullanılamaz; tümü yeniden üretilir** (görsel benzerlik = 0)

---

## 0. Üretim Ortamı (probe — 2026-06-02)

| Araç | Durum | Karar |
|---|---|---|
| Python | ✅ 3.11.9 | — |
| matplotlib | ✅ 3.10.8 | **Birincil üretim rotası** (WP3b) |
| numpy | ✅ 1.26.4 | Veri + closed-form hesap |
| pubfig | ❌ yok | WP3b başında opsiyonel `uv pip install pubfig`; gerekmezse matplotlib yeterli |

> Mühendislik plotları (line/scatter/bar/contour-overlay) için matplotlib tam kontrol sağlar. pubfig zorunlu değil. Anchor F8 + tüm Results data-plot'ları EK-1 Python kodu (`scf_regression.py`) + matplotlib ile üretilir.

---

## 1. 18 Tez Şekli — Karar Matrisi

Dosyalar: `Docs/media/media/image1-18.png`. image1 = üniversite logosu (şekil değil). 17 içerik görseli, 20 caption.

| Tez şekli | Dosya | İçerik | Telif | **Karar** | Hedef |
|---|---|---|---|---|---|
| Şekil 2.1 | image2 | Tipik ripple temsili katı model | Yazar | **Yeniden çiz** → şematik | MF2 girdi |
| Şekil 2.2 | image3 | Cold-bend mild ripple fotoğraf | ⚠ kaynak belirsiz | **Çıkar** veya yazar fotoğrafı ise yeniden işle | — |
| Şekil 2.3 | image4 | Toprak hareketi wrinkle | 🔴 3. taraf [9] | **Çıkar** (gerekirse metin-içi atıf) | — |
| Şekil 2.4 | image5+6 | Caliper radius map ripple | 🔴 caliper çıktısı | **Yeniden çiz** → kendi şematik ILI→FEA | SF2 |
| Şekil 2.5 | image7 | MFL ILI aracı | 🔴 ROSEN flyer [25] | **Çıkar** (makale için gereksiz) | — |
| Şekil 3.1 | image8 | Ripple Abaqus/CAE görünümü | Yazar | **Yeniden çiz/merge** | MF1 panel |
| Şekil 3.2 | image9+10 | Y–Z simetri düzlemi | Yazar | **Merge** | MF1 panel |
| Şekil 3.3 | image11 | RP + coupling + end-cap kuvveti | Yazar | **Merge** | MF1 panel |
| Şekil 3.4 | image12 | Mesh kalitesi / aspect ratio | Yazar | **Yeniden çiz** | SF1 (opsiyonel) |
| Şekil 3.5 | image13 | FE model genel + mesh | Yazar | **Merge** | MF1 panel |
| Şekil 3.6 | image14 | Düz boru S11 hoop dağılımı | Yazar (Abaqus) | **Yeniden export** hi-res | MF3 panel |
| Şekil 3.7 | image15+16 | Von Mises dağılımı (SPOS) | Yazar (Abaqus) | **Yeniden export** | MF3 panel |
| Şekil 3.8 | (gömülü) | Çevresel S11 (SPOS) | Yazar | **Yeniden export** | MF3 / SF3 |
| Şekil 3.9 | image17 | Eksenel S22 (SPOS) | Yazar | **Yeniden export** | SF3 |
| Şekil 3.10 | image18 | SCF_P: FEA vs IPC çubuk | Yazar (veri) | **Regenerate** (matplotlib) | MF4 |
| Şekil 3.11 | (yok) | FEA vs IPC scatter | Yazar (veri) | **Regenerate** | MF4 panel |
| Şekil 3.12 | (yok) | IPC sapma % | Yazar (veri) | **Regenerate** | MF4 panel |
| Şekil 3.13 | (yok) | L/d sweep (3 geometri) | Yazar (veri) | **Regenerate** | MF5 inset |
| Şekil 3.14 | (yok) | FEA vs LD-SCF tahmin scatter | Yazar (veri) | **Regenerate** | MF5 |
| Şekil 3.15 | (yok) | LD-SCF sapma dağılımı | Yazar (veri) | **Regenerate** | MF5 panel |

### Özet kararlar
- **Çıkar (3):** Şekil 2.2, 2.3, 2.5 (telif/gereksiz)
- **Yeniden çiz şematik (2):** Şekil 2.1, 2.4
- **Merge → composite (4):** Şekil 3.1+3.2+3.3+3.5 → MF1
- **Yeniden export contour (4):** Şekil 3.6+3.7+3.8+3.9 → MF3/SF3
- **Regenerate data-plot (6):** Şekil 3.10-3.15 → MF4+MF5 (matplotlib, veriden)
- **Yeni (2):** MF6 (karma spektrum), MF7 (anchor F8)

---

## 2. Ana Figür Envanteri (7 main)

> Not: WP1 §9.3 kararıyla **mesh-independence figürü (eski F4) iptal** (V1 ek koşu yok). Bu yüzden 8→7 main.

### MF1 — FEA Model & Setup (composite, 4-panel)
- **Amaç (hakeme):** Modelin reproducible olduğunu göster (geometri + simetri + BC + end-cap + mesh).
- **Veri kaynağı:** Şekil 3.1/3.2/3.3/3.5 (Abaqus screenshot yeniden export) + şematik overlay.
- **Paneller:** (a) yarım-boru geometri + global eksenler, (b) Y–Z simetri BC, (c) RP + end-cap kuvveti, (d) structured quad mesh detayı.
- **Stil:** mono/gri-uyumlu çizgi şeması; ok + etiket annotasyon; çift sütun (~190 mm).
- **Tip:** schematic + screenshot composite (matplotlib subplot grid + imported panels).

### MF2 — Ripple Geometry Definition
- **Amaç:** Parametrelerin (d tepe-çukur, L dalga boyu, θ/a-C çevresel yayılım, D/t) net tanımı.
- **Veri:** Şekil 2.1 redraw + raised-cosine zarf fonksiyonu (tez tanımı).
- **Eksenler:** eksenel z (mm) vs radyal sapma (mm); θ kesit insetinde.
- **Stil:** tek sütun (~90 mm); parametre etiketleri ok ile; d/D, a/C formülleri.
- **Tip:** annotated schematic (matplotlib).

### MF3 — Validation vs IPC2002-27124 (composite)
- **Amaç:** Modelin dış doğrulaması (V4) + analitik baseline (V3).
- **Veri:** Şekil 3.6 (düz boru hoop=220.8 MPa) + 3.7 Von Mises contour + Tablo 3.4 (VM/S11/S22 vs Rosenfeld) + Tablo 3.2 (end-cap %0.013).
- **Paneller:** (a) Von Mises contour (yeniden export), (b) bar: bu çalışma vs Rosenfeld (VM -11.5%, S11 +1.01%, S22 -11.5%), (c) SCF karşılaştırma (3.143 vs 3.549).
- **Stil:** çift sütun; bar grup + fark % annotasyon; Von Mises %11.5 farkı caption'da gerekçeli.
- **Tip:** contour + grouped bar (matplotlib).

### MF4 — Parametric SCF: FEA vs IPC (3 diameter)
- **Amaç:** Çap etkisi + IPC2002 formülünün büyük çapta yetersizliği (Results omurgası).
- **Veri:** Tablo 3.6/3.7/3.8 (L9×3, 27 nokta) + Şekil 3.10/3.11/3.12.
- **Paneller:** (a) gruplu bar SCF_P (D1-D9 × 3 çap, FEA vs IPC), (b) FEA vs IPC 45° scatter, (c) sapma % (a/C rejimine göre renk).
- **Eksenler:** SCF_P (1.4-2.4); sapma % (-477…+83).
- **Stil:** çift sütun; a/C grupları renk-kodlu (0.25/0.375/0.50); 45° referans çizgisi.
- **Tip:** grouped bar + scatter (matplotlib).

### MF5 — LD-SCF Regression Fit
- **Amaç:** Ampirik formülün uyumu (R²=0.916, max %9) — tezin 1. katkısı.
- **Veri:** 38 FEA noktası + denklem 3.10 + Şekil 3.13/3.14/3.15.
- **Paneller:** (a) predicted vs FEA 45° scatter (±5% / ±9% bantlar), (b) residual dağılımı, (c) L/d sweep inset (3 geometri).
- **Eksenler:** LD-SCF_pred vs FEA SCF_P; residual.
- **Stil:** tek/çift sütun; R²/RMSE/max-err kutu annotasyon.
- **Tip:** scatter + residual (matplotlib, OLS koddan).

### MF6 — Mixed-Spectrum Damage Distribution
- **Amaç:** Karma spektrum bulgusu — %80 MAOP grubu hasarın %68.6'sı (özgün niş sonuç).
- **Veri:** Tablo 3.12 (56" D7, SCF=1.95).
- **Tip seçimi:** **waterfall veya horizontal stacked bar** (pasta DEĞİL — kesin karşılaştırma gerekli). Hasar % + N_i annotasyon.
- **Eksenler:** çevrim türü (MAOP/%80/%50/%5) vs hasar katkısı %.
- **Stil:** tek sütun; %68.6 vurgu rengi; D_yıl=2.90e-2, ömür 34 yıl caption.
- **Tip:** horizontal bar (matplotlib).

### MF7 — Critical SCF Threshold Master Curve ⭐ ANCHOR
- **Amaç:** Tezin görsel kalbi — kritik SCF eşiğinin FFS karar grafiği.
- **Veri kaynağı:** **Tamamen closed-form (WP1 §5'te doğrulandı, ek FEA/yazar verisi yok):**
  ```
  T_est(SCF, n) = (1/n) · (C'/(SCF·S_amp))^5 ,  C'=1126 MPa, S_amp=174.6 MPa
  SCF_krit(n,T) = C'/(S_amp·(n·T)^0.2)
  ```
- **X ekseni:** SCF_P (1.4 – 3.0)
- **Y ekseni:** Tahmini ömür T_est (yıl, **log ölçek**)
- **Eğri ailesi:** n = 4, 8, 12, 24 tam-MAOP-eşdeğer çevrim/yıl
- **Yatay referans:** T = 100 yıl tasarım ömrü → her eğriyle kesişim = kritik SCF
- **Overlay:** 9 FEA konfigürasyonu (D1-D9, üç çap) n=12 eğrisi üzerinde nokta
- **Annotasyon:** SCF_krit ≈ 1.57 (n=12) dikey işaret; güvenli/kritik bölge gölge
- **Doğrulama kontrol noktaları (Tablo 3.11):** 1.51→1422, 1.65→912, 1.95→396, 2.37→149 çevrim ✓
- **Stil:** çift sütun; renk + çizgi-stili çift kodlama (gri-uyum); D=1 eşik bandı.
- **Tip:** semilog line family + scatter overlay (matplotlib).

---

## 3. Supplementary Figürler (2-3)

| SF | İçerik | Veri | Karar |
|---|---|---|---|
| SF1 | Mesh kalitesi / aspect ratio detayı | Şekil 3.4 | Opsiyonel — Methods desteği |
| SF2 | Caliper radius map → FEA parametre şeması | Şekil 2.4 redraw | ILI→FEA bağı (kendi şematik) |
| SF3 | Tam gerilme contour seti (S11/S22/VM) | Şekil 3.6-3.9 | Reproducibility |
| — | `scf_regression.py` + README | EK-1 | Supplementary kod |

---

## 4. Elsevier Artwork Standartları (IJPVP_official_sources §6)

| Öğe | Norm | Uygulama |
|---|---|---|
| Çözünürlük | combo ≥500 dpi, halftone ≥300, line ≥1000 | matplotlib `dpi=600` export |
| Format | TIFF/EPS/PDF tercih; PNG kabul | **PDF (vektör)** + PNG yedek |
| Caption | Şekil altında "Fig. N. ..." | İngilizce, tek cümle + alt-açıklama |
| Genişlik | tek sütun ~90 mm, çift ~190 mm | figsize buna göre |
| Renk | online ücretsiz | renk + **grayscale-safe** (çizgi-stili çift kodlama) |
| Font | tutarlı | sans-serif, ≥7 pt downscale sonrası |

Çıktı dizini: `Docs/paper/figures/figN_*.pdf` (+ `.png` yedek).

---

## 5. WP3b Üretim Sırası (öneri)

Anchor-öncelikli, momentum sağlayan sıra:
1. **MF7 (anchor F8)** — closed-form, en yüksek değer, hızlı (matplotlib + numpy)
2. **MF4 + MF5** — Results data-plot'ları (38 nokta, EK-1 koddan)
3. **MF6** — karma spektrum (Tablo 3.12)
4. **MF1 + MF2** — model şematikleri (Abaqus export + redraw)
5. **MF3** — validation composite (contour export + bar)
6. **SF1-SF3** — supplementary

---

## 6. Yazar Checkpoint — Kararlar (2026-06-02 onaylandı)

### 6.1 Figür envanteri ✅
- [x] 7 main + 3 supplementary envanteri onaylandı (varsayılan kabul — readiness/WP1 ile uyumlu).
- [x] Çıkarılan 3 figür (2.2/2.3/2.5): **çıkarılacak.** ⚠ 2.2 (cold-bend fotoğraf) telif durumu belirsiz kaldı → güvenli taraf: çıkar (gerekirse WP5'te yazar kendi fotoğrafını sağlarsa eklenir).

### 6.2 Anchor F8 ✅ (son açık-uçlu nokta KAPANDI)
- [x] Master curve tasarımı (n=4/8/12/24 ailesi, T=100 yıl çizgisi) onaylandı.
- [x] **Çevrim varsayımı: n=4/8/12/24 (varsayılan) — closed-form'dan üretilir, ek veri yok.** Varsayım caption'da açık yazılır. SCADA yolu kapatıldı.

### 6.3 Üretim rotası ✅
- [x] **matplotlib birincil rota** (pubfig kurulmayacak — gerekmiyor).
- [x] **MF1/MF3: mevcut tez PNG'lerinden çalış** (temizle + vektörel annotasyon overlay).
  - ⚠ **Çözünürlük riski:** Mevcut PNG'ler Elsevier ≥500 dpi'ye zorlanabilir. **Mitigation:** (1) screenshot panelleri üzerine vektörel etiket/ok/çerçeve overlay (matplotlib) → metin keskin kalır; (2) MF1 geometri/BC/mesh için mümkün olduğunca şematik-ağırlıklı kompozisyon; (3) submission'da "best available" kabul, hakem isterse WP-sonrası hi-res export opsiyonu açık tutulur.

---

## 7. WP3b'ye Devir
- Onaylı envanter → WP3b'de matplotlib script'leri (`Docs/paper/figures/`)
- Her figür: veri → script → PDF + PNG → QA (caption/dpi/grayscale)
- F8 öncelikli; EK-1 kodu temel

---

## Sürüm
- **v1 (taslak) — 2026-06-02** — 20 caption karar matrisi + 7 main/3 supp envanter + F8 closed-form spec + matplotlib rota.
- **v1.1 (onaylı) — 2026-06-02** — Checkpoint kilitlendi: F8 n=4/8/12/24 (closed-form), MF1/MF3 mevcut PNG + vektör overlay, matplotlib rota, 3 figür çıkarıldı. Son SCADA açık-ucu kapandı. WP3a KAPANDI.
