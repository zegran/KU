# Author Review R1 — WP6 Girdisi

**Kaynak:** `Unal_ripple_SCF_fatigue_IJPVP_draft (1).docx` içindeki 9 yazar yorumu (Korcan ÜNAL, 04.06.2026 × 8 + 03.07.2026 × 1)
**Kapsam:** Abstract (6 yorum) + Introduction (3 yorum)
**Statü:** WP6a coherence pass'e kullanıcı-review girdisi. Uygulama WP6a içinde, yazar onayıyla.

---

## A. Madde listesi (senior-to-senior)

### R1 — Abstract: IPC2002 vurgusunu kaldır, çerçeveyi pozitife çevir [yorum 0, 4]
- **Anchor:** "IPC2002" (Abstract'ta 2 geçiş).
- **İstek:** Abstract, IPC2002'ye ve "small-diameter'a kalibre edildi" göreceli kıyasına yaslanmasın. Çalışma, *kabul kriterleri dahilinde daha geniş çaplı analizlerin yapılması* olarak konumlansın.
- **Aksiyon:** Abstract'taki her iki IPC2002 referansını sil; ilk cümleyi "extends ripple acceptance analysis to large-diameter pipe within existing acceptance criteria" ekseninde yeniden kur. Rakip-correlation eleştirisi Abstract'tan çıkar, Results/Discussion'da kalır.

### R2 — Abstract: "Thirty-eight" analiz sayısı vurgusu kalksın [yorum 1]
- **Anchor:** "Thirty-eight elastic shell finite element analyses…"
- **Aksiyon:** Sayı verme; "Elastic shell finite element analyses were conducted…" yeterli. Taguchi + sweep detayı kalabilir. Sayı Methods'ta zaten belgeli.

### R3 — Abstract: çap trendi iddiasını kaldır [yorum 2]
- **Anchor:** "and rose as diameter decreased"
- **İstek:** "Bu şekilde olmayabilir" — trend iddiası Abstract'tan çıksın; yalnız aralık kalsın.
- **Aksiyon:** "The stress concentration factor ranged from 1.42 to 2.37." Nokta. Trend tartışması Discussion'a kalır (bkz. D2 karar maddesi).

### R4 — Abstract: ">400% under-prediction" cümlesi kalksın [yorum 3]
- **Anchor:** "a trend the D/t-only IPC2002 form omits while also under-predicting wide ripples by more than 400%"
- **Aksiyon:** Cümleyi tamamen sil. R1 ile birlikte Abstract IPC2002-temizliğinin parçası. Kantitatif kıyas Results §3 ve Discussion'da korunur.

### R5 — Abstract: 68.6% → kalitatif ifade [yorum 5]
- **Anchor:** "…80%-of-MAOP cycle band contributing 68.6% of the annual total."
- **Gerekçe:** Değer *varsayılan* çevrim sayısına dayanıyor; Abstract'ta nokta hassasiyeti savunulamaz.
- **Aksiyon:** "the 80%-of-MAOP cycle band was found to govern more than half of the annual fatigue damage" tarzı ifade. 68.6% Results/Tablo 4'te kalır; orada spektrum varsayımı zaten açık.

### R6 — Introduction: "hydraulic" silinsin [yorum 6]
- **Anchor:** Intro ¶1: "hydraulic bending machine"
- **Aksiyon:** "cold bending machine" — hidrolik vurgusu tamamen çıkar. `01_introduction.md` satır 9.

### R7 — Introduction: "sleeve" → "repair with sleeve" [yorum 7]
- **Anchor:** Intro ¶3: "remove every reported feature by cut-out or sleeve"
- **Aksiyon:** "…by cut-out or repair with sleeve". `01_introduction.md` satır 11.

### R8 — Introduction: Rosenfeld paragrafı akademik registera yeniden yazılsın [yorum 8, 03.07]
- **Anchor:** `01_introduction.md` satır 15 paragrafı (IPC2002-27124 / Rosenfeld).
- **İstek:** Yazar örnek metin verdi (yorum içinde). Ton: nötr, korelasyonu "engineering correlation" olarak takdim; "open question / safety consequences" dramatizasyonu yerine "raising questions regarding applicability". İkinci boşluk (SCF + spektrum birlikte değerlendirilmemiş) korunuyor.
- **Aksiyon:** Yazar örneğini *iskelet* olarak al (birebir kopyalama değil — rewrite SOP geçerli), paragrafı yeniden yaz, WP6c anti-AI pass'ten geçir. "IPC2002-27124" rapor numarası vurgusu düşer; atıf [4] kalır.

---

## B. Kesişen temalar

1. **IPC2002 de-emphasis (R1, R4, R8):** Strateji "rakibi yenmek" değil "kapsamı genişletmek" olarak yeniden konumlanıyor. Abstract + Intro yumuşar; kantitatif benchmark Results/Discussion'da teknik bulgu olarak kalır.
2. **Abstract'ta kesinlik → kalitatiflik (R2, R3, R5):** Varsayıma dayalı veya tek-DoE'lik sayılar Abstract'tan çekiliyor; gövde metin hassasiyeti koruyor.

## C. Propagasyon kontrolleri (WP6a'ya ek bayrak)

Yorumlar Abstract/Intro'ya yazıldı ama aynı iddialar başka yerlerde de var — tutarlılık için karar gerekli:

| # | İddia | Diğer geçişler | Öneri |
|---|-------|----------------|-------|
| P1 | ">400% under-prediction" | `01_introduction.md:20` (contributions bullet), `05_results.md:19`, `06_discussion.md:19`, `07_conclusion.md:13` | Results/Discussion'da KALSIN (veriye dayalı). Intro contributions bullet ve Conclusion #2'de ton R8 ile hizalansın — **yazar kararı** |
| P2 | "SCF rose as diameter decreased" | `06_discussion.md:19` ("mean SCF rose by 13% from 56 in to 36 in") | Yorum 2 "olmayabilir" diyor → veri teyidi gerekli. Mevcut QA-1 bayrağıyla (36" ort. SCF 1.96 vs 1.89) birleştir |
| P3 | "68.6%" | `05_results.md:39`, `06_discussion.md:23`, `07_conclusion.md:15` | Results'ta kalsın; Conclusion #3'te ">50%" kalitatif forma çekilmesi değerlendirilsin — **yazar kararı** |
| P4 | Highlights | WP5g çıktısı sections/ altında ayrı dosya olarak görünmüyor | Bulunup R1–R5 ile hizalanacak; yoksa WP6a'da yeniden üretilecek |

## D. WP6 eşlemesi

- **WP6a (coherence pass):** R1–R7 + P1–P4 → mevcut 6 QA bayrağına ek olarak işlenir. P2, QA-1 ile doğrudan bağlantılı.
- **WP6c (anti-AI pass):** R8 yeniden yazımı ve R1/R5'in yeni cümleleri buradan da geçer.
- **Uygulama sırası önerisi:** önce P2 veri teyidi (QA-1), sonra Abstract yeniden yazımı (R1–R5 tek geçişte), sonra Intro (R6–R8).

## E. Yazar onayı bekleyen kararlar

1. P1: Intro contributions bullet'ında "400%" kalsın mı, yumuşasın mı?
2. P2: Çap trendi veri teyidi sonrası Discussion'da kalacak mı?
3. P3: Conclusion #3'te 68.6% kalitatife çekilsin mi?
4. Highlights dosyasının mevcut konumu / yeniden üretim onayı.

---
*Bu doküman docx yorumlarının yapılandırılmış dökümüdür; manuscript'e hiçbir edit uygulanmamıştır.*
