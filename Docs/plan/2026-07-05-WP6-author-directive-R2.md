# WP6 Yazar Direktifi R2 — Otonom Uçtan Uca Düzeltme Emri

**Tarih:** 2026-07-05
**Yazar:** Korcan Ünal
**Statü:** 🟢 YETKİLENDİRİLDİ — Bu direktif, WP6a → WP6b → WP6c zincirinin ve final docx montajının **otonom, uçtan uca** yürütülmesi için yazar onayıdır. Ara checkpoint'lerde durma yok; her fazın sonunda log + commit atılır, zincir kesintisiz ilerler.
**Kapsam dışı:** WP6d (iThenticate — yazar tarafında), push/submit (ayrı yazar onayı gerekir, Hard Rule 7 geçerli).
**Bağlı doküman:** `Docs/paper/reviews/2026-07-05_author_review_R1_WP6_input.md` (R1–R8, P1–P4 — bu direktifin ayrılmaz parçası).

---

## 0. Yeni kaynak: güncellenmiş tez

Yazar tezde minör güncellemeler yaptı: **`_selfReview/korcan_unal_tez_02072026.docx`**

1. Bu dosyayı **read-only kaynak** kabul et (üzerine yazma). `_Archive/` kuralı aynen geçerli.
2. Pandoc ile `Docs/KUnal_tez_org_tr_v2_02072026.md`'ye çevir. Eski `Docs/KUnal_tez_org_tr.md`'yi silme; v2 artık aktif kaynak.
3. v1 ↔ v2 diff çıkar, değişen bölümleri tespit et ve `logs/`'a kaydet. Manuscript'i etkileyen her değişikliği ilgili section'a yansıt.
4. QA-3 ve QA-6 çözümleri (aşağıda) bu v2 metinden parse edilir.

## 1. QA bayrakları — yazar kararları (FINAL)

| # | Bayrak | Yazar kararı |
|---|--------|--------------|
| QA-1 | 36" ortalama SCF: 1.96 vs 1.89 | **1.89 doğru kabul et** (9 vakanın aritmetik ortalaması). Taslakta 1.89 kalır; tez metnindeki 1.96 ile çelişki manuscript'e taşınmaz. |
| QA-2 | a/C sapma işaretleri (tez satır 955 ters) | **Otonom karar.** Makale için en doğru olanı sen belirle: formülden türetilen figür/Results yazımı esas alınsın, tutarlılığı tüm section'larda uygula, kararını logla. |
| QA-3 | D/D_f/D_M notasyonu | **Güncellenmiş tezden (v2) parse et** ve metin genelinde tek tip uygula. |
| QA-4 | V&V 10-2006/2019, Abaqus 2020/2024 sürümleri | **Otonom.** Doğru sürümü önce tez v2'den doğrula; analizde fiilen kullanılan sürümü yaz. Tezde çelişki sürerse analiz dosyalarındaki/metindeki en son tutarlı sürümü seç ve logla. |
| QA-5 | Çapraz referanslar (Fig 1–7, Table 1–4, E1–E10) | **Otonom.** Makale ilmine göre tara, numaralandırmayı düzelt, section'lar arası tutarlılığı garanti et. |
| QA-6 | Citation numaraları (provisional) | **Tez v2 referans listesini esas alarak** WP6b'de kesinleştir. |

## 2. R1 review maddeleri (Abstract + Introduction)

`2026-07-05_author_review_R1_WP6_input.md` içindeki **R1–R8 tamamı uygulanacak**. Propagasyon kararları (oradaki E bölümü) şimdi kapanıyor:

- **P1 (>400% iddiası):** Abstract ve Intro contributions'tan çıkar (R1/R4 gereği). Results/Discussion'da veri-temelli bulgu olarak kalabilir ancak M2 (IPC minimalizasyonu) ile uyumlu, düşük profilde yaz. Conclusion'da IPC kıyası vurgusunu azalt.
- **P2 (çap trendi):** QA-1 kararı (1.89) sonrası trendi veriden yeniden teyit et. Veri desteklemiyorsa Discussion'daki %13 iddiasını da kaldır/yumuşat — otonom karar, logla.
- **P3 (68.6%):** Abstract'ta kalitatif (">50%"), Results/Tablo 4'te sayısal kalır. Conclusion'da kalitatif forma çek.
- **P4 (Highlights):** Bulunamıyorsa WP6a'da yeniden üret; R1–R5 ve M1–M5 ile hizalı olsun.

## 3. MAJOR yazar istekleri (M1–M6) — öncelikli

### M1 — Q1 dil seviyesi: "tez çevirisi" tonundan çık
Makalenin dili tezin diline fazla yakın; şu an translate gibi duruyor. **Tüm section'lara tam kapsamlı dil pass'i** uygulanacak:
- Skill zinciri: `ml-paper-writing` + `writing-anti-ai` + `paper-self-review` (WP_skill_mapping.md kurallarına göre logla).
- Rewrite SOP (WP0d) disiplini geçerli: TR kaynağa bakmadan, iskelet üzerinden yeniden yaz.
- Hedef register: IJPVP Q1 — kısa, iddia-önce cümleler; pasif/nominal tez kalıplarından arındır; paragraf başları topic-sentence ile.
- Yorum 8'deki yazar örnek paragrafı ton kalibrasyonu için referans al (birebir kopyalama yok).

### M2 — IPC2002 referansını minimalize et
IPC2002'ye çok yerde referans verme gereği yok. **Özgün bir çalışma olarak kurgula:**
- IPC2002/Rosenfeld atfı: Introduction'da 1 kez konumlandırma + Results'ta 1 kez benchmark + Discussion'da 1 kez yorum. Bunun dışındaki tüm geçişleri kaldır veya nötr ifadeye çevir.
- Anlatı ekseni: "mevcut korelasyonu çürütmek" değil, "büyük çaplı borular için FEA-türevli özgün korelasyon geliştirmek".

### M3 — D/t = 73.1'in rolünü yeniden çerçevele
D/t oranı bu makalede **yalnızca bir referans yaklaşımı / kontrollü sabittir**. Doğru kurgu:
- IPC korelasyonu ≤36 in borulardan türetilmiş regresyona dayanır; bu çalışma daha büyük çaplı boruların (36/48/56 in) FEA'sından türetilen regresyonu onunla **karşılaştırılabilir kılmak için** D/t'yi sabit tutmuştur.
- Vurgulanan asıl tema: **IPC formülünün büyük çaplarda farklı davranabileceğini göstermek.**
- Future work: D/t aralığı genişletilerek tek bir genelleştirilmiş regresyon formülü elde edilebilir — Conclusion/Discussion'a gelecek çalışma referansı olarak yaz.
- Bu çerçeve Methods (DoE gerekçesi), Discussion ve Conclusion'da tutarlı işlensin.

### M4 — FFS (Fitness-for-Service) amacını akademik olarak vurgula
Makale, soğuk saha bükümlerinde oluşan ripple tipi geometrik bozuklukların FEA + yorulma ömrü ile çalışılmasını tarifler ve **boruların FFS değerlendirmelerine referans olması amacıyla** yapılmıştır. Bu amaç Introduction (motivasyon) ve Conclusion'da (katkı) akademik dille açıkça yer alsın.

### M5 — Metodolojinin genelleştirilebilirliği
Çalışmanın, boru yüzeyinde meydana gelen **diğer geometrik bozukluklar için de aynı metodolojiyle referans alınabileceği** makale diliyle belirtilsin (Discussion sonu veya Conclusion — tek, ölçülü cümle/paragraf; overclaim yapma).

### M6 — Final teslimat: profesyonel .docx
Zincirin sonunda makale **tek bir profesyonel Word dosyası** olarak teslim edilecek:
- Tüm section'lar birleşik, IJPVP formatına uygun (kaynak: `Docs/refs/IJPVP_official_sources.md` — FROZEN, web araması YASAK).
- Figürler (7 main + 3 supplementary) yerleşik, caption'lı, numaralı — hepsi regenerate edilmiş (Hard Rule 5).
- Tablolar (1–4) ve denklemler (E1–E10) kurallara uygun gömülü.
- Kesinleşmiş referans listesi (WP6b çıktısı) dahil.
- Title page, highlights, abstract, keywords, declaration bölümleri eksiksiz.
- Çıktı: `Docs/paper/submission/Unal_ripple_SCF_fatigue_IJPVP_R2.docx`

## 4. Uygulama sırası (fazlar — kesintisiz)

1. **Faz 0 — Kaynak güncelleme:** Tez v2 pandoc çevirisi, diff, etki analizi (§0).
2. **Faz 1 — Veri/QA kapanışı:** QA-1..QA-5 + P2 veri teyidi. Sayısal zemin sabitlenmeden metne dokunma.
3. **Faz 2 — Yapısal/çerçeve düzeltmeleri:** M2, M3, M4, M5 + R1–R8 + P1/P3/P4 (section bazında: Abstract → Intro → Methods → Results → Discussion → Conclusion → Highlights).
4. **Faz 3 — WP6b:** Citation kesinleştirme (tez v2 + WP2 citation pool), bibliography finalize.
5. **Faz 4 — WP6c / M1:** Tam dil pass'i (Q1 register + anti-AI). Faz 2-3'ten sonra yapılır ki yeniden yazılan metin de geçsin.
6. **Faz 5 — Tutarlılık son turu:** QA-5 çapraz referans son kontrolü, sayı/iddia tutarlılığı (Abstract kalitatif ↔ gövde sayısal), self-review skill'i ile uçtan uca okuma.
7. **Faz 6 — M6 montaj:** Final docx üretimi + doğrulama (açılabilirlik, figür çözünürlüğü, numaralandırma).

Her faz sonunda: `logs/` milestone kaydı + Conventional Commit (`wp6:` prefix). Push YOK.

## 5. Kısıtlar (değişmedi)

- `_Archive/` ve `_selfReview/` kaynak dosyaları read-only.
- IJPVP web araması yasak — FROZEN kaynak dosyası kullanılır.
- Doğrudan TR→EN çeviri yasak — rewrite SOP.
- WP6d (iThenticate) ve WP7/WP8 dışarıda; final docx teslimi sonrası yazar review'ı ile devam kararı verilir.

## 6. Bitiş kriteri

Zincir şu üçü teslim edildiğinde tamamlanmış sayılır: (1) güncellenmiş section .md dosyaları, (2) faz logları + commit'ler, (3) `Unal_ripple_SCF_fatigue_IJPVP_R2.docx`. Ardından tek bir kapanış özeti: yapılan otonom kararlar listesi (QA-2, QA-4, P2 dahil) + yazarın gözden geçirmesi gereken noktalar.
