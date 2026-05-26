# WP Yapısı v2 + Skill Mapping

**Tarih:** 2026-05-26
**Tür:** scope-shift (yapısal)
**WP bağı:** WP0
**Yazar:** Korcan Ünal

## Ne oldu

1. Execution plan v1 → v2 yeniden yazıldı (profesyonel yazım sırası)
2. v1 arşivlendi: `Docs/plan/archive/2026-05-26-execution-plan-IJPVP-v1.md`
3. Yeni WP yapısı: WP1, WP2, WP3a/b, WP4, WP5a-g, WP6a-d, WP7a-e, WP8
4. `Docs/plan/WP_skill_mapping.md` oluşturuldu — her WP için sorumlu + destekleyici skill ataması + log formatı
5. `README.md` workflow tablosu yeni numerasyonla yenilendi
6. `CLAUDE.md` v2 execution plan + skill mapping pointer'larıyla güncellendi
7. `paper-plan-v1.md` başına v2 numerasyon eşleme notu eklendi

## Karar / Sonuç

### Yeni WP sırası (gerekçe)
- **WP5a (Methods) en önce:** En faktüel; momentum sağlar
- **WP5b → WP5c → WP5d:** Results → Discussion → Conclusion
- **WP5e (Introduction) sondan ikinci:** Hikaye ancak içerik bittikten sonra net
- **WP5f (Abstract+Title) son:** Gerçek içeriği yansıtır
- **WP5g (Highlights) Abstract sonrası**
- **WP3a/b (figürler) metinden ÖNCE:** Figure-driven narrative
- **WP4 (tablolar/denklemler) WP3a ile paralel**
- **WP6a/b/c (quality assurance):** Coherence → Citation → Polish, sırayla
- **WP6d (iThenticate):** Yazar tarafı, gate
- **WP7a–e:** Submission package modüler
- **WP8:** Submission, yazar tarafı

### Skill ataması (özet)
- Drafting WP'leri: `ml-paper-writing` primary
- Figürler: `publication-chart-skill`
- Citation: `citation-verification`
- Polish: `writing-anti-ai`
- Review: `paper-self-review`
- LaTeX: `latex-conference-template-organizer`

### Süre revize
- 27–43 CLI oturum (v1: 21–33) — daha granüler bölünme
- 6–10 hafta takvim (değişmedi)

## Etki

### Değişen dosyalar
- `Docs/plan/2026-05-26-execution-plan-IJPVP-v2.md` (yeni)
- `Docs/plan/archive/2026-05-26-execution-plan-IJPVP-v1.md` (arşiv)
- `Docs/plan/WP_skill_mapping.md` (yeni)
- `Docs/plan/2026-05-26-paper-plan-IJPVP-v1.md` (v2 eşleme notu eklendi)
- `README.md` (workflow tablosu)
- `CLAUDE.md` (authoritative references güncellendi)

### Sonraki adımı nasıl etkiler
- Yazar `WP1 başlat` komutu verdiğinde CLI otomatik `Skill(superpowers:writing-plans)` ile başlar
- Her WP tamamlamada `logs/wp_completion_log.md` formatında satır eklenecek
- IMRaD spine WP1'de oluşturulacak (önceki ayrı WP4 değil)

## Referanslar

- Execution v2: `Docs/plan/2026-05-26-execution-plan-IJPVP-v2.md`
- Execution v1 (arşiv): `Docs/plan/archive/2026-05-26-execution-plan-IJPVP-v1.md`
- Skill mapping: `Docs/plan/WP_skill_mapping.md`
- Önceki log: `logs/2026-05-26-03-ijpvp-sources-v2.md`
