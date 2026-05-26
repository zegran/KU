# Log System

İki katmanlı log sistemi:

## 1. `.claude/logs/` — Otomatik oturum logları

Her Claude Code oturumu için otomatik üretilir. Dosya adı: `session-YYYYMMDD-<id>.md`.
Dokunmayın; sistem yönetir.

## 2. `logs/` — Manuel milestone logları

Anlamlı her olayda yeni log dosyası eklenir. Format:

```
logs/YYYY-MM-DD-NN-<short-slug>.md
```

- `YYYY-MM-DD` — tarih
- `NN` — günün kaçıncı log'u (01, 02, ...)
- `<short-slug>` — kebab-case kısa özet

### Ne zaman log yazılır?

- WP tamamlama (WP1 done, WP2 done, ...)
- Karar değişikliği (örn. anchor framing yumuşatıldı)
- Scope shift (yeni section eklendi/çıkarıldı)
- Ek FEA koşusu yapıldı (FEA-1 / FEA-2)
- Author/advisor onay turu sonucu
- Git milestone (initial push, WP merge, vb.)
- Submission, rebuttal, decision

### Log dosyası şablonu

Her log dosyası şu yapıda olur:

```markdown
# <Başlık>

**Tarih:** YYYY-MM-DD
**Tür:** [milestone | decision | scope-shift | external | submission]
**WP bağı:** WP<N> veya —
**Yazar:** <isim>

## Ne oldu
<1-3 paragraf>

## Karar / Sonuç
<madde işaretli>

## Etki
- Hangi dosyalar değişti
- Hangi planlar güncellendi
- Sonraki adımı nasıl etkiler

## Referanslar
- Plan dosyası: `Docs/plan/...`
- Commit: `<sha>`
- Dış dosya: <yol>
```

### Kurallar

- Her log immutable — yazıldıktan sonra düzeltilmez (yanlışsa yeni log + çapraz referans)
- Her log git commit ile birlikte gider (`log: <slug>`)
- Aylık özet: ay sonunda `logs/YYYY-MM-summary.md` üretilebilir
