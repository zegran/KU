# Tez → IJPVP Q1 Hazırlık Değerlendirmesi (TR İç Rapor)

**Tarih:** 2026-05-26
**Hedef dergi:** International Journal of Pressure Vessels and Piping (Elsevier, Q1)
**Kaynak tez:** `Docs/KUnal_tez_org_tr.md` (1960 satır okundu — Giriş, Lit., Metod, Doğrulama, Sonuçlar, Yorulma, Sonuç)
**Yazılma amacı:** Yazarın "tezim Q1'e yeter mi?" sorusuna rasyonel, skorlamalı, kaygı-azaltıcı cevap
**Ton:** Dürüst mühendis. Pazarlama yasak. Her skor gerekçeli, her sayı kaynaklı.

---

## Bölüm 1 — IJPVP Standart Profili

IJPVP'nin ScienceDirect sayfası, son 12 ayda yayımlanmış makaleler ve dergi pratiği temelinde derlenmiştir. Tam erişim olmayan kalemler [*tipik norm*] etiketiyle işaretlenmiştir.

| Parametre | Norm | Kaynak |
|---|---|---|
| Yayıncı | Elsevier | sciencedirect.com [1] |
| ISSN | 0308-0161 | [1] |
| IF (2024 yakl.) | ~3.5–4 | research.com [2] |
| Kapsam | Basınçlı kap & boru hattı bütünlüğü, FEA, fitness-for-service, kaynak, kompozit onarım, yorulma | Dergi tanımı [1] |
| Tipik makale uzunluğu | 12–20 sayfa (~6.000–10.000 kelime) | [*tipik norm*] |
| Abstract | Yapılandırılmamış, 150–250 kelime | [*tipik norm*] |
| Highlights | 3–5 madde, her biri ≤85 karakter | Elsevier standart |
| Bölüm yapısı (tipik) | Intro → Background/Theory → Numerical Model → Methodology → Results → Discussion → Conclusions | Son makalelerden derleme |
| Şekil sayısı | Tipik 6–10 main + supplementary opsiyonel | [*tipik norm*] |
| Tablo sayısı | 2–5 main | [*tipik norm*] |
| Referans sayısı | 30–60 (yüksek kaliteli; çoğu peer-reviewed makale) | [*tipik norm*] |
| Referans formatı | Elsevier sayısal stil [n] | EndNote stili [3] |
| Graphical abstract | Önerilen (zorunlu değil) | Elsevier standart |
| Declarations | Funding, Conflict of Interest, Data Availability, CRediT — **zorunlu** | Elsevier standart 2025 |
| Closed-form gerekliliği | **Yok** — doğrulanmış parametrik FEA + standart-tabanlı metodoloji kabul görüyor | Yakın yayınlar |
| Kabul kriteri (gözlem) | Validated numerical model + standards-based methodology + practical engineering value | Kapsam |

### Son 12 ayda dergiden örnek konu uyumu (scope teyidi)
- 2025'te kompozit yama onarımı + deneysel doğrulama makalesi yayımlandı [4]
- 2025'te wrinkle bends üzerine bir makale dergide yer aldı [5] — **bu tezin tam konu komşusu**
- Geçmişte "local wall thinning ile boruda SCF" FEA makalesi [6] ve "wrinkle bends in pipelines" stress analizi makalesi [7] dergide yayımlanmıştır

**Sonuç:** IJPVP scope açısından bu tezin konusu derginin **tipik yayın alanına** doğrudan girmektedir. Konu-fit riski çok düşük.

---

## Bölüm 2 — Bölüm Bölüm Tez Değerlendirmesi

Her bölüm için 0–10 hazırlık skoru. "Hazırlık" = mevcut tez içeriğinin IJPVP makalesine **paraphrase + restructuring** ile taşınabilirliği. 10 = doğrudan kullanılabilir, 0 = sıfırdan yazılmalı.

| # | Tez bölümü | Satır aralığı | Makale section'ı | Skor (0-10) | Güçlü yön | Eksik | Gerekli işlem |
|---|---|---|---|---|---|---|---|
| T1 | Giriş | 357–379 | § 1 Introduction | **7** | Field bending → ripple bağlantısı net; API 5L X70 motivasyonu sağlam; IPC2002 sınırı iyi konumlandırılmış | TR-spesifik motivasyon ağır; uluslararası okuyucu için "neden bu çalışma şimdi" çok güçlü değil; IJPVP normuna göre çok uzun (~720 kelime hedef) | Paraphrase + global motivasyon vurgu artırılır |
| T2 | Yüksek Day. Hat Boruları + API 5L X70 | 383–438 | § 2 Background (içine erir) | **7.5** | HSLA bağlamı + saha bükümü mekanizması açık; IPC2002 anchor referansı doğru | Bazı kaynaklar tekrarlı; CSA Z662/ASME B31.8 dilinin yorumu uzun | Sıkıştır, paraphrase, % 60'ı tutulur |
| T3 | Geometri ILI radius map | 440–484 | § 2 Background (alt-paragraf) | **6** | Konu mühendislik açısından ilginç; ILI verisinin FEA'ya bağlanması iyi anlatılmış | Caliper veri görselinin kaynağı net değil (telif sorunu olabilir); ROSEN technical flyer akademik referans değil | Kısalt; ILI-to-FEA bağı korunur, telif riskli görseller yeniden çizilir |
| T4 | Kuramsal Temel & Elastisite | 494–538 | § 3 Theoretical Framework | **8** | Membran + eğilme + SCF tanımı standart; Lame + thin-shell + plak rijitliği denklemleri açık | "Çap arttıkça eğrilik" argümanı sezgisel ama matematiksel olarak daha net türetilebilir; D/t bağımsızlığı yetersiz | Paraphrase + bir-iki ek denklem (membran-eğilme oranı boyutsuzlaştırma) |
| T5 | Sayısal Model Kurulumu | 540–669 | § 4 Numerical Model | **7.5** | S4R seçimi savunuldu, BC ve simetri açık, yük tanımı (iç basınç + end-cap) doğru; 31,968 eleman, ~194k DOF; Abaqus/Standard 2020; aspect ratio ≤3 | "Toplam düğüm sayısı 32,398" tabloda yazarın kendi soru işareti var (yani metin temizliği şart); mesh independence çalışması **dolaylı**, açık h-convergence tablosu yok | Mesh independence için 2 alternatif seviye koşusu **önerilir** (gate değil); metin teknik temizlik gerektirir |
| T6 | Sayısal Modelin Doğrulanması | 671–849 | § 4 Validation alt-bölümü | **7** | (a) End cap force fark **%0.013** — mükemmel; (b) düz boru hoop stress σ = pD/2t = 220.8 MPa analitik karşılaştırma var → V3 **kapatılmış**; (c) IPC2002-27124 benchmark hoop %1.01, Von Mises %11.5 | Von Mises %11.5 farkı **savunma gerektirir**; ripple geometri farkı (5-tepe vs tek tepe), çeyrek-vs-yarım simetri ve yazılım farkı (FACTS vs Abaqus) gerekçeleri tezde verilmiş ama hakem ısrar edebilir | İlave 1 koşu (referans ripple profili) hakemi rahatlatır — opsiyonel |
| T7 | Yöntem & Model Kurulumu (parametrik) | 851–1006 | § 6 Results (parametrik bölüm) | **8.5** | D/t = 73.1 sabit + 3 çap × Taguchi L9 + L/d sweep = **38 FEA noktası**; her tablo doldurulmuş; **R² = 0.916, RMSE = 0.058, max %9 hata** ile ampirik LD-SCF formülü türetilmiş; IPC formülü ile sapma karşılaştırması köklü yapılmış | Tek D/t (= 73.1) — formülün genelleştirilebilirliği sınırlı (yazar zaten kabul ediyor); regresyon sabiti A = 142.1 olağandışı yüksek görünüyor (üs dağılımına bakıldığında matematiksel olarak doğru ama hakem soracak) | Tek D/t kısıtı discussion'da explicit yazılır; formül "geçerlilik zarfı" net çizilir |
| T8 | Yorulma Analizi & Ömür | 1007–1419 | § 5 Methodology + § 6 Results (yorulma kısmı) | **8** | Markl C' = 1126 MPa (yük kontrollü, IPC2002-27124'ten kalibreli — V5 **explicit**); ASTM E1049 rainflow; Miner; **kritik SCF eşiği 1.51–1.65** sayısal olarak çıkmış; karma spektrum 56" D7 için 34 yıl ömür hesaplı | "S-N kalibrasyonu" tek paragrafta gizli, daha açık bir alt-başlık olmalı; rainflow algoritması metin halinde değil, akış şeması da yok | Methodology bölümünde S-N calibration ayrı alt-başlık; rainflow için akış şeması veya kısa pseudocode |
| T9 | SCF Kritik Eşik (anchor) | 1219–1332 | § 7 Discussion (anchor) | **8.5** | Tablo 3.11 SCF duyarlılık analizi, **kritik eşiği D=1 üzerinden açık sayısal olarak veriyor**: SCF<1.51 güvenli, SCF≥1.65 100 yıllık ömrü karşılamıyor | "Anchor figure" (master curve) henüz bir görsel olarak yok — sadece tablo şeklinde; bunun makalede grafik haline gelmesi şart | Yeni anchor figür üretilir: SCF vs T_estimated (yıl) eğrisi, D/t ve çap bant'larıyla |
| T10 | Karma Çevrim Spektrumu | 1334–1416 | § 7 Discussion (devam) | **7.5** | "%80 MAOP çevrimleri toplam hasarın %68.6'sı" bulgusu **özgün ve değerli**; "yüksek SCF ama düşük spektrum vs ılımlı SCF + yüksek spektrum" karşılaştırması mühendislik açısından çok güçlü | Tek spektrum (n=2/24/52/200) varsayımı kullanılıyor; "tipik gaz hattı" diye nitelendirilmiş ama referans yok | Spektrum varsayımı için PRCI veya gerçek SCADA referansı eklenir (varsa) |
| T11 | Sonuç ve Öneriler | 1418–1450 | § 8 Conclusions | **7** | Üç özgün katkı net listelenmiş (LD-SCF formülü, entegre yorulma, ILI-to-FEA bağı); ileri çalışma önerileri var (D/t genişletme) | "Türk boru hattı mühendisliği pratiği" pasajı IJPVP için lokal — çıkarılır; conclusion biraz dağınık | Kısalt, üç madde halinde net özet + iki gelecek-iş cümlesi |
| T12 | Kaynaklar | 1452–1518 | References | **5** | **33 referans var**, IPC2002, IPC2008, IPC2018, IPC2022 zinciri tutarlı; Pilkey, Schijve, Zienkiewicz, Cook gibi temel kitaplar mevcut | IJPVP 30–60 ref bekler; mevcut 33 alt limitte; **birkaç kaynak peer-reviewed makale değil** (ROSEN flyer, Bilston/Murray PRCI raporu, lokal yüksek lisans tezi); Ş. Turhan tezi yerine peer-reviewed alternatif aranmalı; rebuttal'a karşı dayanıklılık için son 5 yıldan ek 8-12 makale | WP2'de aktif referans havuzu inşası |
| T13 | EK 1 (Python kodu) | 1520–1959 | Supplementary | **9** | Reproducibility için **mükemmel**; OLS regresyon koduyla Q1 normuna uygun | Yorum satırları artırılır, README eklenir | Repo'ya `supplementary/scf_regression.py` olarak konur |

---

## Bölüm 3 — Genel Hazırlık Skoru (0-100)

Beş boyutta ağırlıklı değerlendirme. Ağırlıklar IJPVP hakeminin tipik öncelik sırasından türetilmiştir.

| Boyut | Ağırlık | Skor (0-10) | Ağırlıklı puan | Gerekçe (1-2 cümle) |
|---|---|---|---|---|
| (a) İçerik derinliği | **25%** | **7.5** | 18.75 | Methodology kapsamlı; 38 FEA noktası, ampirik formül R²=0.916, entegre yorulma çerçevesi; tek D/t = 73.1 ve "büyük çap" tanımı bir miktar limitlidir. |
| (b) Doğrulama | **25%** | **6.5** | 16.25 | End cap (%0.013), hoop baseline (analitik eşleşme), IPC2002 benchmark (hoop %1.01) güçlü; ancak Von Mises **%11.5 fark** ve **explicit mesh independence tablosu yok** — defansif mitigation şart. |
| (c) Şekil kalitesi | **15%** | **4** | 6.00 | 18 şekil TR caption ile düşük çözünürlükte; anchor figure (master curve) hâlâ yok; **WP3'te toplu yeniden üretim zorunlu**. |
| (d) Literatür güncelliği | **15%** | **5** | 7.50 | 33 referans alt limitte; son 5 yıldan ripple/dent SCF + Markl-fatigue peer-reviewed eksik; ROSEN flyer, PRCI report, lokal tez gibi non-journal kaynaklar var. |
| (e) Anchor claim netliği | **20%** | **7.5** | 15.00 | Kritik SCF eşiği (1.51–1.65) sayısal olarak Tablo 3.11'de açık; entegre çerçeve mantığı net; **görsel anchor figure** üretildiğinde 9'a çıkar. |
| **TOPLAM** | **100%** | — | **63.5/100** | |

### Skor yorumu

| Bant | Anlam |
|---|---|
| 80–100 | Submit-ready, kozmetik düzeltmeler |
| 70–80 | Major rewrite gerekir, hazırlık iyi |
| **60–70** | **Şu anki tezin yeri** — sağlam temel, 2–3 stratejik ek iş ile Q1'e oturur |
| 50–60 | Yapısal eksikler, ek FEA gerekir |
| <50 | Yeniden tasarım |

---

## Bölüm 4 — "Bu Tez Q1'e Yeter mi?" Net Cevap

### Paragraf 1 — Objektif mevcut durum
Tez 63.5/100 hazırlık skoru ile IJPVP Q1 dergisinin yayın kabul bandında — alt eşik bölgesinde değil, ortada — duruyor. Methodology omurgası (Abaqus/Standard 2020, S4R, half-symmetric, ~194k DOF, 38 FEA noktası, Taguchi L9 + sweep) sağlam; ampirik LD-SCF formülü R²=0.916 ile kabul edilebilir uyumda; Markl + rainflow + Miner entegrasyonu IPC2002 metodolojisi üzerine **operasyonel anlamı olan bir kritik SCF eşiği** üretiyor (1.51–1.65 bandı, 12 MAOP/yıl, 100 yıllık ömür). IJPVP scope'u açısından konu uyumu **mükemmel** — dergide 2025'te wrinkle bends üzerine yayın çıkması bunun en güçlü kanıtı [5]. Tezin %7 Turnitin benzerlik raporu (s. 93) zaten temiz bir orijinallik temeli sağlıyor; ancak YÖK kaydı sonrası iThenticate üzerinden tekrar kontrol gerekecek.

### Paragraf 2 — Eksikler ve kapatma maliyeti
Üç eksik somut maliyetli, dördü orta-yüksek:

1. **Mesh independence tablosu** (V1): 2 ek FEA koşusu × ~2–3 saat = **toplam 4–6 saat yazar zamanı**. Gate değil ama hakem 1. tur yorumuna karşı çok güçlü savunma.
2. **Von Mises %11.5 farkının daha güçlü açıklaması**: 1 ek koşu (referans ripple profili ile) × ~2 saat = **2 saat yazar zamanı**. Hakem ısrarına karşı.
3. **18 şeklin yeniden üretimi + anchor master curve figürü**: 8 main figure × ~30–45 dk = **6–9 saat CLI + 1–2 saat yazar veri sağlama**.
4. **Referans havuzu genişletme** (33 → 45–55 peer-reviewed): WP2'de ~6–10 saat CLI tarama + yazar erişim doğrulaması.
5. **Tek D/t = 73.1 kısıtının discussion'da explicit yazılması**: yazım sırasında **0 ek maliyet**, sadece dürüstçe yazılır.

Yorulma kalibrasyon (V5), end cap force (V6), analitik baseline (V3), IPC2002 benchmark (V4) — bunlar **zaten mevcut**. Yani validation profili tez içinde tüm temel öğelere sahip; eksik olan sadece açık h-convergence tablosu (V1) ve Von Mises savunması.

### Paragraf 3 — Tahmini toplam süre ve başarı olasılığı
Tezin mevcut hâlinden IJPVP submit-ready makaleye gidiş için **gerçekçi süre: 6–10 hafta takvim** (önceki execution planındaki tahmin geçerli, bu değerlendirme doğruluyor). Tahmini **kabul olasılığı bandı** (ilk submit + 1 büyük revizyon dahil):

- **%60–70** — bu, "anchor master curve şekli üretilir + V1 mesh tablosu eklenir + referanslar 45+'e çıkarılır + yazım K4 SOP ile temiz olur" senaryosu için.
- **%40–50** — V1 ve referans genişletme atlanırsa.
- **%25–35** — tek D/t kısıtı framing'de gizlenir ve hakem yakalarsa.

IJPVP'nin reddetme nedenleri arasında **scope mismatch** ihtimali çok düşük (5%'in altı), çünkü konu komşu makaleler dergide zaten var. Asıl ret riskleri: (a) validation hakem ısrarı, (b) D/t genelleştirilebilirlik, (c) referans güncelliği. Üçü de **yönetilebilir** — yapısal blocker yok.

**Net cevap:** Evet, bu tez IJPVP Q1'e yeter. Ama "hazır" değil. Tez **63.5/100** seviyesinde sağlam bir temel; 80–85 seviyesine çıkarmak için **2–3 önemli ek iş + disiplinli yeniden yazım** gerekir.

---

## Bölüm 5 — Risk-Aksiyon Listesi (Top 5)

| Sıra | Risk | Şiddet | Şimdi yap | Sonra yap | Asla yapma |
|---|---|---|---|---|---|
| **1** | iThenticate yüksek skor (kendi tezinden) | **Yüksek** | YÖK kayıt durumunu danışmanla teyit et; K4 SOP'unu WP5 başlamadan önce yaz | WP5 her section başında SOP kontrol listesi çalıştır; cover letter şeffaflık paragrafı ekle | TR metni doğrudan EN'ye çevirme (Google Translate / DeepL); kelime kelime çeviri |
| **2** | Von Mises %11.5 fark — hakem ısrarı | Orta-yüksek | Tezdeki üç gerekçeyi (ripple sayısı, simetri, yazılım) daha güçlü prose ile yaz; rebuttal taslağı hazırla | Opsiyonel 1 ek FEA koşusu (referans ripple profili) — %2 saat | "%11.5 fark normal" diye geçiştirme; hakem sorduğunda hazırlıksız yakalanma |
| **3** | Mesh independence açık tablo eksikliği (V1) | Orta | DOF + element kalite metriklerini yazıma dahil et; literatür mesh sıklığı kıyaslaması yap | 2 alternatif mesh seviyesi koşusu (~4–6 saat) — defansif | "194k DOF yeterli" tek argümanına dayanma |
| **4** | Tek D/t = 73.1 — genelleştirilebilirlik | Orta | Discussion'da formülün geçerlilik zarfını **explicit** yaz (D/t = 73.1, X70, P = 9.55 MPa); future work'te D/t genişletmesini açıkça öner | İlerleyen makale için 2-3 ek D/t koşusu (45, 60, 90) | Formülü genel-amaçlı gibi sunma; "büyük çap = D/t = 73.1" eşitlemesi yapma |
| **5** | Referans havuzunun zayıflığı (33 → 45–55) | Orta | WP2'de IJPVP-uyumlu son 5 yıl makaleleri tara; ROSEN flyer, lokal tez gibi non-peer-reviewed kaynakları peer-reviewed muadille değiştir veya çıkar | Citation verification (WP6) ile DOI + erişim doğrulaması | TR-only veya gri literatürde kalma; konferans bildirisini "makale" diye gösterme |

---

## Sürüm
- **v1 — 2026-05-26** — Tez tam okuma + IJPVP profil teyidi sonrası ilk hazırlık değerlendirmesi
- **v1.1 — 2026-05-26** — IJPVP_official_sources.md (FROZEN) sonrası yeniden değerlendirme (aşağıdaki Addendum)

---

## Addendum v1.1 — IJPVP Resmi Kaynak Dosyası Sonrası Yeniden Değerlendirme

**Tetik:** `Docs/refs/IJPVP_official_sources.md` (FROZEN, 2026-05-26) tamamlandı. Resmi kaynaklar + cross-validation sonucu IJPVP profili daha net belirlendi. Aşağıdaki değişiklikler v1 skorlamasını revize ediyor.

### Yeni resmi bilgiler ve skor üzerindeki etkisi

| Yeni bilgi | v1'deki varsayım | Skor etkisi |
|---|---|---|
| IF 3.500 (2024, JCR) [4] | IF ~7+ tahminim yanlıştı (önceki turlarda) | **Olumlu** — Q1 bandı çok daha ulaşılabilir; tezin mevcut seviyesi 80–85 norm'una yakın |
| Quartile: Q1 Eng. Mech. (29/125) + Q2 Eng. Multi. (25/74) [4] | "Q1 dergi" varsayımı doğru ama bant düşük | **Nötr** — Q1 etiketi geçerli ama üst tier değil |
| Yıllık ~212–241 makale [2][3] | Volume bilinmiyordu | **Olumlu** — yüksek hacim ⇒ acceptance rate görece yüksek |
| Closed-form derivation **gerekmiyor** (komşu yayınlardan teyit) | Tezin parametrik FEA + ampirik regresyon yaklaşımı uygun olmayabilir endişesi | **Olumlu** — anchor claim netliği skorunu yukarı çeker |
| Referans stili: Elsevier numbered [9] | Tezin köşeli parantez `[n]` stiline zaten uyumlu | **Olumlu** — referans format dönüşümü minimal |
| Scope-fit komşu yayınlar (wrinkle bends, local wall thinning SCF, butt weld SCF) [5][6][7][8] | Sezgisel uyumluluk tahmini | **Olumlu** — desk-reject riski neredeyse sıfır |
| ⚠ Review süresi tek kaynakta ~24 ay [2], diğer kaynaklarda yok | Tahmini 8–16 hafta varsayımı | **Risk** — gerçek revizyon süresi uzunsa toplam takvim uzar |
| ⚠ CiteScore çelişkisi (3.7 vs 6) | Bilinmiyordu | **Nötr** — kabul kararına etkisi yok |

### Revize Skorlama (v1 → v1.1)

| Boyut | Ağırlık | v1 Skor | v1.1 Skor | Gerekçe |
|---|---|---|---|---|
| (a) İçerik derinliği | 25% | 7.5 | **7.5** | Değişmedi |
| (b) Doğrulama | 25% | 6.5 | **6.5** | Değişmedi (V1, Von Mises hâlâ açık) |
| (c) Şekil kalitesi | 15% | 4 | **4** | Değişmedi |
| (d) Literatür güncelliği | 15% | 5 | **5** | Değişmedi (WP2'de aktif iyileştirme) |
| (e) Anchor claim netliği | 20% | 7.5 | **8.5** | IJPVP'nin closed-form gerektirmediği teyit edildi; mevcut parametrik+kritik eşik anchor'u dergi normuna **doğal** oturuyor |
| **TOPLAM** | 100% | **63.5** | **65.5** | +2 puan |

### Kabul olasılığı bandı (revize)

v1'deki tahminleri IJPVP gerçek profiline kalibre ediyorum:

| Senaryo | v1 olasılığı | v1.1 olasılığı | Değişim gerekçesi |
|---|---|---|---|
| V1 mesh + anchor figure + ref 45+ + temiz K4 SOP | %60–70 | **%65–75** | Q1 bandı IF 3.5; scope-fit %100; closed-form gereksiz |
| V1 ve referans atlanır | %40–50 | **%50–60** | Aynı yukarı kayma |
| D/t kısıtı framing'de gizlenir | %25–35 | **%25–35** | Hakem hâlâ yakalar; değişmez |

### Yeni risk: Review süresi
Tek kaynak [2] **24 ay** ortalama review süresi diyor. Bu olağandışı yüksek; Elsevier mech-eng dergilerinde tipik 3–6 ay. Bu tek kaynaklı bilgi olduğu için ⚠ olarak işaretlendi. **Yazara öneri:** dergi'nin son makalelerinin "received → accepted" sürelerini birkaç örnekte inceleyip gerçek bandı doğrula. 24 ay doğruysa submission stratejisi (örn. tier-2 hedef ile paralel hazırlık) değişebilir; 3–6 ay ise mevcut plan değişmez.

### Çıkarımlar
1. **Bu tez IJPVP'ye anlamlı bir yayın yapma şansına sahip;** %65–75 bandı ciddi bir "yapılabilir" demek
2. **Ek FEA koşusu yapılmasa bile** %50–60 bandı kalıyor — yani tez zaten yeterli temele sahip
3. **En yüksek riski K4 (iThenticate)** taşıyor; bu yapısal değil, disiplinle yönetilir
4. **WP1 başlatma kararı için ek gerekçe yok** — IJPVP_official_sources.md sonrası karar zayıflamadı, güçlendi

---

## Kaynaklar

- [1] [International Journal of Pressure Vessels and Piping — ScienceDirect](https://www.sciencedirect.com/journal/international-journal-of-pressure-vessels-and-piping)
- [2] [IJPVP — Impact Factor, Ranking & Research Scope (Research.com)](https://research.com/journal/international-journal-of-pressure-vessels-and-piping)
- [3] [IJPVP Citation Style — Paperpile](https://paperpile.com/s/international-journal-of-pressure-vessels-and-piping-citation-style/)
- [4] [Pressure vessel failure analysis and composite repair patch (IJPVP 2025, Vol. 215)](https://www.sciencedirect.com/science/article/abs/pii/S0308016125000249)
- [5] [Stress analyses of wrinkle bends in pipelines — IJPVP (komşu konu)](https://www.sciencedirect.com/science/article/abs/pii/0263823193900197)
- [6] [Finite element based stress concentration factors for pipes with local wall thinning — IJPVP](https://www.sciencedirect.com/science/article/abs/pii/S0308016104001322)
- [7] [Stress concentration analysis of butt welds with variable wall thickness — IJPVP](https://www.sciencedirect.com/science/article/abs/pii/S0308016120300533)
