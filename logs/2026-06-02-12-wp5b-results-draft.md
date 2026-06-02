# WP5b Tamamlandı — Results Section Draft

**Tarih:** 2026-06-02
**Tür:** milestone
**WP bağı:** WP5b
**Yazar:** Korcan Ünal
**Skill:** ml-paper-writing (primary) + results-analysis (support)

## Ne oldu

Results section'ı (§3) rewrite-SOP'la taslaklandı: 3.1 parametrik SCF + çap etkisi, 3.2 IPC2002'den sapma, 3.3 dalga boyu (L/d) duyarlılığı, 3.4 ampirik LD-SCF korelasyonu, 3.5 basınç-çevrim yorulma hasarı. ~1300 okunabilir kelime.

**Kritik düzeltme uygulandı:** IPC sapma değerleri formülden (Eq.5) doğrudan hesaplandı — a/C=0.25 → −31..−84% (IPC fazla tahmin), a/C=0.50 → +48..+437% (IPC ciddi düşük tahmin). Bu, tez satır 955'in ters-işaretli prose'unu **düzeltiyor** (WP3b QA bulgusu). Fiziksel yorum: IPC'nin (a/C)^−2.87 terimi geniş ripple'ı daha az şiddetli gösteriyor; FEA tersini gösteriyor (ampirik a/C üssü +0.065).

## Karar / Sonuç

- **SCF aralığı 1.42–2.37;** çap-ortalamaları 1.89/1.78/1.68 (36/48/56"); θ baskın parametre; D7 worst-case.
- **LD-SCF formülü açık yazıldı** (Eq.6, R²=0.916, RMSE=0.058, max %9); üs hiyerarşisi: d/D +0.938, d/t −0.676, L/d −0.167, a/C +0.065.
- **Yorulma:** 5. kuvvet duyarlılığı; tek MAOP çevrimi N_f=396/249/149; karma spektrum 56" D7 → D_yıl=2.90e-2, ömür ~34 yıl, %80 MAOP grubu hasarın %68.6'sı.
- **Anchor (kritik eşik master curve, Fig.7/MF7) bilinçli olarak Discussion'a (WP5c) ertelendi.**

## ⚠ Drafting notları (WP6a)
- 36" ortalama 1.89 (tablo-tutarlı) kullanıldı; tez metni 1.96 — WP6a'da çözülecek.
- IPC sapma işaretleri/değerleri formülden; tez L955 düzeltildi.
- ~1300 kelime (hedef ~1550); gerekirse 3.5 genişletilebilir.

## Etki

- **Yeni dosya:** `Docs/paper/sections/05_results.md`
- **Bu log:** `logs/2026-06-02-12-wp5b-results-draft.md`
- **Plan etkisi:** Methods + Results tamam. WP5c (Discussion) için anchor F8 + IPC limit argümanı + FFS + limitations zemini hazır.
- **Sonraki adım:** WP5c (Discussion).

## Referanslar

- Results: `Docs/paper/sections/05_results.md`
- Methods: `Docs/paper/sections/04_methods.md`
- IPC sapma QA: `logs/2026-06-02-09-wp3b-figure-production.md`
- Önceki log: `logs/2026-06-02-11-wp5a-methods-draft.md`

---

### WP completion record (WP_skill_mapping formatı)
```
WP5b | ml-paper-writing | 2026-06-02T00:00:00+03:00 | Docs/paper/sections/05_results.md | drafted (author review pending)
```
