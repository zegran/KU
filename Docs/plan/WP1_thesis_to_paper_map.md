# WP1 — Thesis-to-IJPVP-Paper Map + IMRaD Spine

> **WP:** WP1 (execution-plan v2)
> **Skill:** `superpowers:writing-plans` (primary) + `doc-coauthoring` (support)
> **Tarih:** 2026-06-02
> **Kaynak tez:** `Docs/KUnal_tez_org_tr.md` (1960 satır — tamamı okundu)
> **IJPVP normu:** `Docs/refs/IJPVP_official_sources.md` v2 FROZEN
> **Durum:** ✅ CHECKPOINT ONAYLANDI (2026-06-02) — Section yapısı **Seçenek A** + V1 **argüman/literatür** kilitlendi. WP2/WP3a/WP4 başlatılabilir.
> **Kelime hedefi:** Original article, **maksimum 6.000 kelime** (gövde metni)

---

## 0. WP1 Kapsamı (execution-plan v2'den)

Bu dosya beş işi tamamlar:
1. Tezin baştan sona okunması (tamamlandı — bulgular §1).
2. IMRaD omurgası: her tez bölümü → IJPVP section + kelime tahsisi (§3, §4).
3. Anchor figure (kritik SCF eşiği) veri planı (§5).
4. V1 mesh + V3 baseline koşu kararları (§6).
5. WP0b doğrulaması: kritik eşik veriden nasıl çıkıyor (§2).

---

## 1. Tez İçerik Envanteri (tam okuma sonrası — doğrulanmış sayılar)

Aşağıdaki tüm sayılar tez metninden birebir teyit edildi; WP5 drafting'inde bunlar otoriter kabul edilir.

### 1.1 Model ve malzeme
| Parametre | Değer | Tez satırı |
|---|---|---|
| Malzeme | API 5L X70, izotropik doğrusal elastik | 667 |
| E / ν | 203.000 MPa / 0.3 | 667 |
| Eleman | S4R (4-düğüm, reduced-integration kabuk), 6 DOF/düğüm | 490, 550 |
| Eleman sayısı / DOF | 31.968 eleman / ~194.388 DOF | 550 |
| Yazılım | Abaqus/Standard 2020 | 680 |
| Model simetrisi | Yarım-simetrik (180°), Y–Z düzlemi | 548, 686 |
| Boru uzunluğu | 5.000 mm | 687 |
| Aspect ratio kriteri | ≤ 3 | 550, 652 |
| Global mesh | 20 mm + ripple bölgesinde edge seeding | 648-650 |

### 1.2 Parametrik tasarım
| Parametre | Değer | Tez satırı |
|---|---|---|
| Çaplar | 36" (914.4 mm), 48" (1219.2 mm), 56" (1422.4 mm) | 860-862 |
| **D/t sabiti** | **73.1** (tüm çaplarda, Barlow + DF=0.72) | 855 |
| MAOP | 9.55 MPa | 855 |
| σ_hoop (nominal) | 349.2 MPa (tüm çaplarda eşit) | 855 |
| Deney tasarımı | Taguchi L9 × 3 çap = 27 + 11 L/d sweep = **38 FEA noktası** | 874, 971 |
| Parametreler | θ (90/135/180°), d/D, L/d | 868-872 |
| SCF_P aralığı | **1.42 – 2.37** | 924 |
| Ortalama SCF_P | 56":1.68, 48":1.78, 36":1.96 (çap↓ ⇒ SCF↑) | 933 |

### 1.3 LD-SCF ampirik formülü (tezin 1. özgün katkısı)
```
SCF_P = 142.1 · (d/D)^0.938 · (d/t)^−0.676 · (L/d)^−0.167 · (a/C)^0.065
```
(Denklem 3.10, satır 984) — **R²=0.916, RMSE=0.058, max bağıl hata %9.0** (satır 997).
OLS log-lineer regresyon, `numpy.linalg.lstsq` (EK-1 Python kodu, satır 1520+).
**Geçerlilik zarfı:** D/t=73.1, X70, P=9.55 MPa — tek D/t (genelleştirme sınırı, yazar kabul ediyor).

### 1.4 Yorulma zinciri (tezin 2. özgün katkısı)
| Bileşen | Değer | Tez satırı |
|---|---|---|
| Markl S-N | N_f = (C'/(i·S))⁵, i ≡ SCF_P | 1040, 1050 |
| C' (yük kontrollü) | 1126 MPa (163.300 psi, IPC2002-27124 kalibreli — **V5**) | 1063 |
| S_amp @ MAOP | 174.6 MPa (= σ_hoop·ΔP/MAOP /2) | 1058, 1104 |
| Çevrim sayımı | ASTM E1049 rainflow | 1065-1069 |
| Hasar | Miner D=Σ(n_i/N_i), kritik D≥1 | 1138-1144 |
| 5. kuvvet duyarlılığı | ΔP/MAOP %100→%50 ⇒ N_i 32× artar | 1132 |

### 1.5 Karma spektrum bulgusu (tezin değerli niş sonucu)
56" D7 (SCF=1.95), tipik gaz hattı spektrumu (n=2/24/52/200): D_yıl=2.90×10⁻², ömür ≈ **34 yıl**.
**Baskın grup %80 MAOP (n=24): toplam hasarın %68.6'sı** (satır 1410-1414).
Mühendislik mesajı: en yüksek hasar ne en büyük genlikli ne en kalabalık grup → operasyonel spektrum SCF kadar belirleyici.

---

## 2. WP0b Çözümü — Kritik SCF Eşiği Veriden Nasıl Çıkıyor

**Soru (stratejik plan §2):** Eşik tek sayı mı, eğri mi, D/t-bantlı mı?

**Cevap: Tek-değer bandı (1.51–1.65), tek bir operasyonel varsayıma koşullu — ve kapalı forma genelleştirilebilir.**

Tablo 3.11 (satır 1223-1330), n=12 tam MAOP çevrim/yıl + 100 yıl + σ_h=349.2 MPa varsayımı altında:
- SCF_P < 1.51 → D₁₀₀ < 1 (güvenli; dikkat bölgesi 0.5<D<1)
- SCF_P 1.51–1.65 → kritik eşik geçişi
- SCF_P ≥ 1.65 → 100 yıllık ömür karşılanamıyor

### Kapalı form türetimi (WP1'de doğrulandı)
Kritik koşul D_100yr = n·T/N_f = 1, ve N_f = (C'/(SCF·S_amp))⁵ ⇒

```
SCF_krit = C' / [ S_amp · (n·T)^0.2 ]
         = 1126 / [ 174.6 · (12·100)^0.2 ]  ≈  1.57
```

Doğrulama (denklem ↔ Tablo 3.11):
| SCF_P | N_f (denklem) | N_f (tez) | ✓ |
|---|---|---|---|
| 1.51 | 1421 | 1422 | ✓ |
| 1.65 | 912 | 912 | ✓ |
| 1.95 | 396 | 396 | ✓ |
| 2.37 | 149 | 149 | ✓ |

**Çıkarım:** Eşik bandı tek bir n=12 varsayımına aittir. Gerçek anchor (master curve), eşiği **çevrim-sayısı ailesi** olarak gösterir → tek banttan genelleştirilebilir bir karar grafiğine dönüşür. Bu tamamen mevcut denklemlerden hesaplanır (§5).

---

## 3. Tez → Makale Section Haritası (satır-aralığı bazlı)

| Tez bölümü | Tez satırı | → IJPVP section | Hazırlık (readiness) | Ana işlem |
|---|---|---|---|---|
| Giriş | 357-379 | Introduction | 7/10 | Paraphrase, global motivasyon↑, TR-spesifik kısımları çıkar |
| API 5L X70 + HSLA | 383-438 | Introduction (background içine erir) | 7.5/10 | %60'ı tut, sıkıştır |
| Geometri ILI / caliper | 440-484 | Introduction (1 paragraf) | 6/10 | Kısalt; ILI→FEA bağı korunur; ROSEN/caliper görselleri yeniden çiz (telif) |
| Kuramsal Temel + elastisite | 494-538 | Methods §2.1 (SCF basis) | 8/10 | Paraphrase + membran-eğilme denklemleri |
| Sayısal Model Kurulumu | 540-669 | Methods §2.2 (FE model) | 7.5/10 | S4R/BC/end-cap; **metin temizliği** (satır 685 yazar soru işareti) |
| Doğrulama (V&V) | 671-849 | Methods §2.3 (Validation) | 7/10 | End-cap %0.013, hoop 220.8 MPa, IPC2002 benchmark; Von Mises %11.5 savunması güçlendir |
| Parametrik Yöntem + LD-SCF | 851-1006 | Results §1 (parametric) | 8.5/10 | Taguchi L9, IPC sapma, sweep, regresyon — doğrudan taşı |
| Yorulma Metodolojisi | 1007-1158 | Methods §2.4 (fatigue method) | 8/10 | Markl/rainflow/Miner/C' kalibrasyon — **S-N calibration ayrı alt-başlık** |
| Yorulma Sonuçları | 1160-1217 | Results §2 (MAOP-cycle damage) | 8/10 | Tablo 3.9, 3.10 → Results |
| SCF Kritik Eşik (anchor) | 1219-1332 | Discussion (anchor) | 8.5/10 | Tablo 3.11 → **F8 master curve** + closed-form |
| Karma Çevrim Spektrumu | 1334-1416 | Discussion (devam) | 7.5/10 | %68.6 bulgusu; spektrum varsayımına referans ara |
| Sonuç ve Öneriler | 1418-1450 | Conclusions | 7/10 | 3 madde + future work; "Türk pratiği" pasajı çıkar |
| Kaynaklar (33) | 1452-1518 | References | 5/10 | WP2: 33→45-55, non-peer-reviewed değiştir |
| EK-1 Python | 1520-1959 | Supplementary | 9/10 | `supplementary/scf_regression.py` + README |

---

## 4. IMRaD Omurgası + Kelime Tahsisi (6.000 kelime)

### ⚠ Çözülmesi gereken yapısal karar (yazar onayı — §9.1)

Execution-plan v2'nin WP5 alt-adımları yalnızca şu section dosyalarını üretiyor:
`00_abstract_title`, `01_introduction`, `04_methods`, `05_results`, `06_discussion`, `07_conclusion`.
**Dosya numaraları 02 ve 03 atlanmış** — yani §2 Background ve §3 Theory için ayrı WP5 adımı yok. Ayrıca WP5a "04_methods ~1.000 kelime" diyor ama readiness v1.2 §4=1000 + §5=850 = 1850 öngörüyor. İki tutarsızlık var; WP1 bunları çözmek için.

**✅ KARAR (2026-06-02): Seçenek A onaylandı. Seçenek B referans olarak korunuyor.**

#### ✅ ONAYLANDI — Seçenek A: 5-gövde-section (fold yapısı)
Background §1 Introduction'a, Theory §4 Methods'a katlanır. Mevcut WP5 dosya numaralandırmasıyla (00,01,04,05,06,07) **birebir uyumlu** — yeni dosya/WP adımı gerekmez. IJPVP'nin 6.000 kelime sınırı için en gerçekçi yapı (FEA validation makalesinde Methods en uzun section olması normaldir).

| § | Section (dosya) | Kelime | Tez kaynağı |
|---|---|---|---|
| 1 | **Introduction** (`01_introduction.md`) — motivasyon, API 5L X70, field bending→ripple, ILI karakterizasyon, IPC2002 açığı, amaç | **950** | 357-484 (T1+T2+T3 condensed) |
| 2 | **Methods** (`04_methods.md`) — SCF basis + FE model + V&V + fatigue methodology | **2.050** | 494-849 + 1007-1158 |
| 3 | **Results** (`05_results.md`) — parametrik SCF, IPC sapma, L/d sweep, LD-SCF regresyon, MAOP-cycle damage, karma spektrum | **1.550** | 851-1006 + 1160-1416 |
| 4 | **Discussion** (`06_discussion.md`) — kritik SCF eşik (anchor), IPC limit, çap etkisi, %68.6 bulgusu, D/t=73.1 zarfı, FFS, limitations | **1.050** | 1219-1416 cross-cut |
| 5 | **Conclusions** (`07_conclusion.md`) — 3 katkı + future work | **250** | 1418-1450 |
| — | Abstract+Title (`00_abstract_title.md`) | (~200, gövde dışı) | yeni |
| | **Gövde toplam** | **~5.850** | **< 6.000 ✓** |

#### Seçenek B: 8-section (readiness v1.2 yapısı korunur)
§1=600, §2=700, §3=700, §4=1000, §5=850, §6=1200, §7=750, §8=200 = 6.000. Background ve Theory ayrı section kalır → `02_background.md` + `03_theory.md` yeni dosyalar; WP5a penceresinde çizilir. Daha geleneksel ama 6.000 kelimede front-matter ağırlığı yüksek; iki ek drafting adımı gate dışı kalır.

> **CLI önerisi: Seçenek A.** Gerekçe: (1) WP5 dosya numaralandırmasıyla zaten uyumlu, (2) 6.000 kelime sınırına daha rahat oturuyor, (3) IJPVP komşu makaleleri (lokal wall thinning SCF [6], wrinkle bends [8]) lean front-matter + ağır Methods/Results yapısı kullanıyor.

> **WP5a kelime düzeltmesi:** Hangi seçenek seçilirse seçilsin, "Methods ~1.000 kelime" gerçekçi değil. Seçenek A'da Methods ≈ 2.050 (theory+model+V&V+fatigue). Bu, WP5a checkpoint'inde 2 oturum olarak planlanmalı.

---

## 5. Anchor Figure (F8) Veri Planı — DE-RISKED

**Bulgu: F8 tamamen hesaplanabilir; ek FEA veya yazar verisi gerekmez** (HANDOVER risk tablosundaki "F8 darboğazı" iptal).

### F8 tasarımı — "Critical SCF Threshold Master Curve"
- **X ekseni:** SCF_P (1.4 – 3.0)
- **Y ekseni:** Tahmini yorulma ömrü T_est (yıl, log ölçek)
- **Eğri ailesi:** yıllık tam-MAOP-eşdeğer çevrim sayısı n = 4, 8, 12, 24 (her biri bir eğri)
- **Yatay referans:** T = 100 yıl (tasarım ömrü) → her eğriyle kesişim = o n için kritik SCF
- **Overlay:** 9 gerçek FEA konfigürasyonu (D1–D9, üç çap) n=12 eğrisi üzerinde nokta olarak

### Hesap (mevcut denklemlerden — yeni veri yok)
```
T_est(SCF, n) = N_f / n = (1/n) · (C' / (SCF · S_amp))^5
C' = 1126 MPa,  S_amp = 174.6 MPa (@ tam MAOP)
SCF_krit(n, T) = C' / [ S_amp · (n·T)^0.2 ]
```
Doğrulanmış kontrol noktaları (§2 tablosu) bu denklemi onaylıyor.

**İkincil anchor adayı (Discussion):** karma-spektrum hasar dağılımı (Tablo 3.12) → waterfall/pasta: %80 MAOP %68.6, MAOP %17.4, %50 %14.2, %5 ~%0.

> **WP3a/WP3b notu:** F8 üretimi `matplotlib-visualization` + EK-1 Python koduyla tek script. Yazar girdisi yalnızca **çevrim spektrumu varsayımının onayı** (n=4/8/12/24 makul mü, ya da gerçek SCADA verisi var mı).

---

## 6. V1 Mesh + V3 Baseline Koşu Kararları

| Öğe | Karar | Gerekçe |
|---|---|---|
| **V3 (analitik baseline)** | ✅ **Ek koşu GEREKSİZ** | Tez satır 743-749: σ_hoop=pD/2t=220.8 MPa analitik eşleşme zaten var. Methods'ta 2-3 cümle olarak raporlanır. |
| **V1 (mesh independence)** | ✅ **KARAR: argüman + literatür (ek koşu YOK)** | Tez satır 650: yakınsama nitel yapılmış (mesh sıkı→max gerilme kararlı), ama açık h-convergence tablosu yok. **Methods'ta yazılacak:** DOF + aspect ratio≤3 + literatür (5k-20k eleman [4]) + V&V'deki IPC2002 %0.3 SCF uyumu dolaylı kanıt. 2 mesh seviyesi koşusu yapılmayacak; hakem ısrar ederse rebuttal'da kapatılır. WP'yi yavaşlatmaz. |
| **Metin temizliği** | 🔴 **Zorunlu** | Tez satır 685: "32.398 (toplam düğüm sayısı az değil mi?" — yazarın kendi soru işareti makaleye taşınamaz. Satır 1075: "Tablo 7.1" ama caption 3.9 (numara tutarsızlığı). Denklem 3.12 iki kez (satır 1043, 1053). WP5a/WP6a'da düzeltilir. |

---

## 7. Figür / Tablo → Section Bağı (WP3a/WP4 için ön envanter)

### Ana figür adayları (hedef 6-8 main)
| Fig | İçerik | Tez kaynağı | Section | Durum |
|---|---|---|---|---|
| F1 | FEA model şeması (geometri+BC+mesh composite) | Şekil 3.1/3.3/3.5 | Methods | yeniden çiz |
| F2 | Ripple geometri parametre tanımı (d, L, θ, a/C) | Şekil 2.1 + yeni | Methods | yeniden çiz |
| F3 | V&V: IPC2002-27124 karşılaştırma (S11/VM/S22) | Şekil 3.7/3.8/3.9 + Tablo 3.4 | Methods | yeniden çiz |
| F4 | Mesh independence (V1, opsiyonel) | yeni (koşu yapılırsa) | Methods | koşula bağlı |
| F5 | SCF_P parametrik (FEA vs IPC) + sapma | Şekil 3.10/3.11/3.12 | Results | yeniden çiz |
| F6 | LD-SCF regresyon uyumu (45° scatter) + L/d sweep | Şekil 3.13/3.14/3.15 | Results | yeniden çiz |
| F7 | Karma spektrum hasar dağılımı (%68.6) | Tablo 3.12 | Discussion | yeni |
| **F8** | **Critical SCF threshold master curve (ANCHOR)** | Tablo 3.11 + closed-form | Discussion | **yeni — §5** |

### Ana tablo adayları (hedef 3-4 main)
| Tab | İçerik | Tez kaynağı | Section |
|---|---|---|---|
| T1 | FE model + malzeme özeti | Tablo 3.1 + 1.2 metni | Methods |
| T2 | V&V özeti (end-cap %0.013 + IPC2002 benchmark) | Tablo 3.2 + 3.4 | Methods |
| T3 | Parametrik geometri + SCF_P sonuçları (L9×3) | Tablo 3.5-3.8 | Results |
| T4 | Kritik eşik duyarlılığı / karma spektrum | Tablo 3.11 + 3.12 | Discussion |

---

## 8. Anchor Claim Onayı (K3 — feasibility tam doğrulandı)

Stratejik plan pitch'i tezde tam destekleniyor:
- ✅ Parametrik SCF-to-life framework → 38 FEA + LD-SCF + Markl-Miner zinciri mevcut
- ✅ Critical SCF threshold → Tablo 3.11 + closed-form SCF_krit = C'/(S_amp·(n·T)^0.2)
- ✅ Realistic pressure spectrum → ASTM E1049 rainflow + karma spektrum
- ✅ FFS karar bağlamı → API 579/ASME FFS-1 atfı (satır 1450), editör "pratik uygulama" vurgusuyla örtüşür
- ✅ External validation → IPC2002-27124 (V4)

**Anchor claim feasibility: TAM POZİTİF.** WP0b kapandı.

---

## 9. Yazar Checkpoint — Kararlar (2026-06-02 onaylandı)

### 9.1 Section yapısı (KRİTİK) ✅
- [x] **Seçenek A (5-section fold)** onaylandı.
- [x] Methods kelime tahsisi ~2.050 kabul (WP5a = 2 oturum olarak planlanacak).

### 9.2 Anchor figure 🟢 (varsayılan kabul, WP3a'da kesinleşir)
- [x] F8 master curve tasarımı (SCF vs T_est, n=4/8/12/24 ailesi) **varsayılan onay**.
- [ ] Çevrim varsayımı: **n=4/8/12/24 varsayılan kabul edildi.** Yazarda gerçek SCADA/PRCI spektrumu varsa WP3a'da değiştirilir — bloklamaz.

### 9.3 Validation ek koşu ✅
- [x] V1: **ek koşu YOK** — argüman + literatür yeterli (yazar kararı).
- [x] Von Mises %11.5: **ek koşu YOK** (V1 ile tutarlı defansif-hafif çizgi). Mevcut 3 gerekçe (ripple sayısı, simetri, yazılım) güçlü prose ile yazılır + rebuttal taslağı WP6'da hazırlanır.

### 9.4 Kapsam dışı bırakılanlar 🟢 (varsayılan — readiness ile uyumlu, açıkça doğru)
- [x] "Türk boru hattı pratiği" pasajı (satır 1450) makaleden **çıkarılacak**.
- [x] D/t=73.1 tek-değer kısıtı Discussion'da **explicit** yazılacak (genelleştirme iddiası yok).

> Tüm checkpoint kararları kapandı. 9.2'deki SCADA verisi tek açık-uçlu nokta; WP3a'da yazara tekrar sorulacak (bloklamaz).

---

## 10. WP1 Sonrası Akış

```
WP1 (bu dosya) → yazar checkpoint (§9)
   ↓ onay
WP2 (citation pool 40-60) ─┐
                            ├→ WP3a (figür stratejisi, F8 dahil) → WP3b
WP4 (tablo+denklem) ────────┘
   ↓
WP5a Methods (2 oturum) → WP5b Results → ... (Methods-first sıra)
```

WP1 checkpoint onayı gelince:
1. `Docs/plan/WP1_thesis_to_paper_map.md` final'lenir (seçilen section yapısıyla)
2. `logs/` altına WP1 completion satırı eklenir
3. Yazar bir sonraki `WPx başlat` komutunu verir

---

## Sürüm
- **v1 (taslak) — 2026-06-02** — Tez tam okuma + IMRaD spine + anchor F8 de-risk + WP0b closed-form çözümü. Yazar checkpoint bekliyor.
- **v1.1 (onaylı) — 2026-06-02** — Checkpoint kararları kilitlendi: Section **Seçenek A** (5-fold), V1 **ek koşu yok**, Von Mises **ek koşu yok**, F8 master curve + n=4/8/12/24 varsayılan, kapsam dışı pasajlar onaylandı. WP1 KAPANDI.
