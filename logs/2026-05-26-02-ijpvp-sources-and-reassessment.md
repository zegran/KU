# IJPVP Resmi Kaynak Dosyası + Hazırlık Yeniden Değerlendirmesi

**Tarih:** 2026-05-26
**Tür:** milestone + scope-shift
**WP bağı:** WP0 (referans altyapısı)
**Yazar:** Korcan Ünal

## Ne oldu

1. `Docs/refs/IJPVP_official_sources.md` (🔒 FROZEN) oluşturuldu — IJPVP ile ilgili tüm gelecek sorularda tek kaynak.
2. 3 birincil + 4 cross-validation web kaynağı tarandı; 2 Elsevier PDF (~1.1 MB toplam) yerelleştirildi (`Docs/refs/pdfs/`).
3. ScienceDirect IJPVP Guide for Authors sayfası HTTP 403 döndü; 10 ⚠ eksik madde yazar manuel doğrulama listesine alındı.
4. Booksite Elsevier reference styles PDF linki ölü (404) — silindi.
5. Hazırlık raporu v1.1 addendum ile revize edildi: **63.5 → 65.5/100**.
6. Sorumluluk matrisi `Docs/plan/2026-05-26-responsibility-matrix.md` olarak yayımlandı.
7. CLAUDE.md güncellendi: IJPVP web search yasağı + FROZEN file pointer eklendi.

## Karar / Sonuç

- **IJPVP IF 2024 = 3.500 (JCR)** — daha önce varsayılan IF~7 yanlıştı; gerçek bant daha ulaşılabilir
- **Quartile:** Q1 Eng. Mechanical (29/125), Q2 Eng. Multidisciplinary (25/74)
- **Yıllık makale hacmi:** ~212–241 (yüksek hacim ⇒ acceptance rate görece yüksek)
- **Closed-form derivation gerekmiyor** — tezin mevcut parametrik+ampirik yapısı dergi normuna doğal oturuyor
- **Referans stili:** Elsevier numbered (Style 1) — tez zaten [n] kullanıyor
- **Kabul olasılığı revize bandı:** %65–75 (full prep), %50–60 (V1 atlanırsa)
- **⚠ 10 madde yazar doğrulama listesinde** (CiteScore, article type kelime limitleri, scope verbatim, vb.)
- **⚠ Tek kaynaklı 24 ay review süresi bilgisi** — yazar dergi son makalelerinden teyit etmeli

## Etki

### Değişen dosyalar
- `Docs/refs/IJPVP_official_sources.md` (yeni, FROZEN)
- `Docs/refs/pdfs/elsevier_references_style_guide.pdf` (yeni)
- `Docs/refs/pdfs/elsevier_copy_editing_style.pdf` (yeni)
- `Docs/plan/2026-05-26-readiness-assessment-TR.md` (v1.1 addendum eklendi)
- `Docs/plan/2026-05-26-responsibility-matrix.md` (yeni)
- `CLAUDE.md` (IJPVP web search yasağı + FROZEN pointer)
- `.gitignore` (değişiklik yok)
- `README.md` (değişiklik yok — bir sonraki commit'te güncellenecek)

### Sonraki adımı nasıl etkiler
- WP1 başlatma kararı zayıflamadı, **güçlendi**: yazar hâlâ `WP1 başlat` komutuyla yetkilendirebilir
- WP2'de citation hazırlığı artık Elsevier numbered style'a göre yapılır
- Yazar 10 ⚠ maddeyi (özellikle article type kelime limitleri) dergi sayfasından doğrulamadan WP4'e (section drafting plan) geçilemez

## Referanslar

- Plan v1: `Docs/plan/2026-05-26-paper-plan-IJPVP-v1.md`
- Execution v1: `Docs/plan/2026-05-26-execution-plan-IJPVP-v1.md`
- Readiness v1.1: `Docs/plan/2026-05-26-readiness-assessment-TR.md`
- Responsibility matrix: `Docs/plan/2026-05-26-responsibility-matrix.md`
- IJPVP FROZEN: `Docs/refs/IJPVP_official_sources.md`
- Önceki log: `logs/2026-05-26-01-project-bootstrap.md`
