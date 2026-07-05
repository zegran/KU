# WP6 Faz 6 — M6 Final Docx Montajı + WP6 Zincir Kapanışı

**Tarih:** 2026-07-06
**Tür:** milestone / wp6-faz6 + session-end
**Yazar:** Korcan Ünal

## Teslimat

**`Docs/paper/submission/Unal_ripple_SCF_fatigue_IJPVP_R2.docx`** (9.87 MB)

İçerik sırası (IJPVP FROZEN kaynak §5/§8'e göre): Title page (yazar/affiliation placeholder'lı) → Highlights (5 bullet) → Abstract (~200 kelime) + Keywords (6) → 1. Introduction → 2. Materials and methods → 3. Results → 4. Discussion → 5. Conclusions → Declarations (CRediT + Funding/CoI/Data placeholder) → References (30) → Supplementary material (Table S1–S3 + Fig. S1–S3).

- Figürler ilk-atıf noktalarına gömülü, "Fig. N." caption altta (Elsevier normu); 7 main + 3 supp, 600 dpi PNG.
- Tablolar gerçek Word tabloları, "Table N." caption üstte; 4 main + 3 supp.
- Denklemler OMML (Word native math) — 170 matematik nesnesi.
- Gövde (1–5. bölümler) ≈ 4.3–4.9k kelime → 6.000 limiti altında ✓.

## Doğrulama
- Zip bütünlüğü OK (`testzip` temiz); 10 embedded media; 7 `<w:tbl>`; tüm yapısal başlıklar + "Fig. 7." / "Table 4." / "1.56" / "Rosenfeld" probe'ları mevcut.
- Montaj yeniden üretilebilir: `Docs/paper/submission/build/build_docx.py` + `master.md` (pandoc 3.9, `-f markdown+tex_math_dollars`).

## Bitiş kriteri durumu (direktif §6)
1. ✅ Güncellenmiş section .md dosyaları (00/01/04/05/06/07 + 08_references + Highlights + tablolar + equations + figür manifesti)
2. ✅ Faz logları (2026-07-05-01…06 + bu dosya) + 7 `wp6:` commit
3. ✅ `Unal_ripple_SCF_fatigue_IJPVP_R2.docx`

**Kapsam dışı bırakılanlar (direktif):** WP6d (iThenticate — yazar), push (Hard Rule 7 — yazar onayı bekliyor).

## Sonraki adım
Yazar: (1) R2.docx'i oku; (2) placeholder/⚠ alanları doldur; (3) WP6d iThenticate; (4) onay sonrası `WP7 başlat`.
