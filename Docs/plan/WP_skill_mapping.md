# WP — Skill Mapping (v1)

> **Revision Rationale:**
> Bu dosya CLI'ın her WP başlangıcında hangi skill'i `Skill()` aracıyla aktive edeceğini tek tabloda sabitler. Önceki yapıda skill seçimi ad-hoc idi; bu mapping ile her WP için sorumlu + destekleyici skill'ler önceden belirlenir, log disipliniyle eşleşir.

**Tarih:** 2026-05-26
**Bağlı:** `Docs/plan/2026-05-26-execution-plan-IJPVP-v2.md`

---

## Mevcut Makale-Yazımı Skill Havuzu

CLI ortamında mevcut ve bu projede kullanılabilir skill'ler:

| Skill | Kullanım amacı |
|---|---|
| `superpowers:writing-plans` | Yapısal plan üretimi, WP haritalama |
| `superpowers:brainstorming` | Açık uçlu fikir tarama (gerekirse WP1 öncesi) |
| `doc-coauthoring` | Uzun-form teknik prose taslakları, iteratif yazım |
| `ml-paper-writing` | Akademik section drafting, IMRaD disiplini |
| `research-ideation` | Motivation/gap framing (Introduction için) |
| `citation-verification` | DOI + başlık + yıl + erişim doğrulama |
| `daily-paper-generator` | Literatür havuzu tarama (WP2 destek) |
| `results-analysis` | İstatistiksel yorum, results section disiplini |
| `results-report` | Sonuç sentezi raporlama |
| `publication-chart-skill` | Yayın kalitesinde figür + tablo |
| `matplotlib-visualization` | Python tabanlı grafik üretimi |
| `paper-self-review` | Sistematik kalite kontrol, coherence pass |
| `writing-anti-ai` | AI-tone temizliği, doğal akademik dil |
| `latex-conference-template-organizer` | Elsevier `cas-sc` template'ine taşıma |
| `review-response` | (Submission sonrası) rebuttal yazımı |
| `post-acceptance` | (Kabul sonrası) sunum/poster/promosyon |

---

## WP → Skill Mapping Tablosu

| WP | Adım | **Sorumlu skill** | **Destekleyici skill(ler)** | Yazar/Sistem aksiyonu | CLI tetikleyici (oturum başı) |
|---|---|---|---|---|---|
| WP1 | Thesis-to-paper map + IMRaD spine | `superpowers:writing-plans` | `doc-coauthoring` | — | `Skill(superpowers:writing-plans)` |
| WP2 | Citation pool (40–60 EN) | `citation-verification` | `daily-paper-generator` | 🟡 ref erişim doğrulama | `Skill(citation-verification)` |
| WP3a | Figür stratejisi (karar) | `publication-chart-skill` | `matplotlib-visualization` | 🟡 görsel onay | `Skill(publication-chart-skill)` |
| WP3b | Figür üretimi | `publication-chart-skill` | `matplotlib-visualization` | 🟡 anchor F8 veri | `Skill(publication-chart-skill)` |
| WP4 | Tablolar + denklem türetimleri | `publication-chart-skill` | `ml-paper-writing` | — | `Skill(publication-chart-skill)` |
| WP5a | Methods | `ml-paper-writing` | `doc-coauthoring` | — | `Skill(ml-paper-writing)` |
| WP5b | Results | `ml-paper-writing` | `results-analysis` | — | `Skill(ml-paper-writing)` |
| WP5c | Discussion | `ml-paper-writing` | `doc-coauthoring` + `results-report` | — | `Skill(ml-paper-writing)` |
| WP5d | Conclusion | `ml-paper-writing` | `doc-coauthoring` | — | `Skill(ml-paper-writing)` |
| WP5e | Introduction (sondan ikinci) | `ml-paper-writing` | `research-ideation` | — | `Skill(ml-paper-writing)` |
| WP5f | Abstract + Title (son) | `ml-paper-writing` | `doc-coauthoring` | — | `Skill(ml-paper-writing)` |
| WP5g | Highlights | `ml-paper-writing` | — | — | `Skill(ml-paper-writing)` |
| WP6a | Coherence pass | `paper-self-review` | — | — | `Skill(paper-self-review)` |
| WP6b | Citation verification | `citation-verification` | — | 🟡 erişim sağlama | `Skill(citation-verification)` |
| WP6c | Anti-AI / language polish | `writing-anti-ai` | — | — | `Skill(writing-anti-ai)` |
| WP6d | iThenticate check | — | — | 🔴 **Yazar yapar** | (CLI dışı) |
| WP7a | Cover letter + novelty | `doc-coauthoring` | `ml-paper-writing` | — | `Skill(doc-coauthoring)` |
| WP7b | Graphical abstract | `publication-chart-skill` | — | 🟡 görsel onay | `Skill(publication-chart-skill)` |
| WP7c | CRediT + declarations + data avail. | `doc-coauthoring` | — | 🟡 yazar bilgi sağlama | `Skill(doc-coauthoring)` |
| WP7d | LaTeX migration | `latex-conference-template-organizer` | — | 🟡 PDF derleme onayı | `Skill(latex-conference-template-organizer)` |
| WP7e | Final self-review | `paper-self-review` | — | — | `Skill(paper-self-review)` |
| WP8 | Submission (Editorial Manager) | — | — | 🔴 **Yazar yapar** | (CLI dışı) |

---

## CLI Otomatik Davranış Kuralı

Yazar `WPx başlat` komutu verdiğinde CLI:

1. İlgili satırdaki **sorumlu skill**'i derhal `Skill()` ile aktive eder
2. Aktive olunca: "Activating: [skill-name] — [reason]" satırı çıktıya basar
3. WP çıktısı tamamlanıp yazar onayı geldiğinde:
   - WP çıktı dosyasını yazar
   - `logs/` altına aşağıdaki formatta satır ekler

### Log formatı (her WP tamamlamasında)

Yeni dosya: `logs/YYYY-MM-DD-NN-wpX-completion.md` veya tek satırlık ekleme: `logs/wp_completion_log.md` (append-only).

**Satır şeması:**
```
WP<n><letter> | <skill-name> | <iso-timestamp> | <output-file-path> | author-approved
```

**Örnek:**
```
WP1   | superpowers:writing-plans   | 2026-05-27T14:32:00+03:00 | Docs/plan/WP1_thesis_to_paper_map.md | author-approved
WP5a  | ml-paper-writing            | 2026-06-02T10:15:00+03:00 | Docs/paper/sections/04_methods.md     | author-approved
WP6c  | writing-anti-ai             | 2026-06-15T16:00:00+03:00 | (multiple section files revised)      | author-approved
```

---

## Skill Aktivasyon Önceliği (çatışma çözümü)

Birden fazla skill geçerli görünürse şu sırayla:

1. **Eğer WP açıkça bu mapping tablosunda varsa** → tablo geçerli
2. **Eğer WP yan dal (örn. ad-hoc rebuttal hazırlığı) ise** → `review-response` veya ilgili skill yazardan onay alarak
3. **İkili görev (örn. drafting + chart)** → primary sorumlu skill seçilir; destekleyici skill `Skill()` ile çağrılmaz ama prompt'unda referans edilir

---

## Bağlı Olduğu Dosyalar

- `Docs/plan/2026-05-26-execution-plan-IJPVP-v2.md` (WP tanımları)
- `Docs/plan/2026-05-26-responsibility-matrix.md` (yazar/CLI sorumluluk sınırı)
- `Docs/refs/IJPVP_official_sources.md` (IJPVP normları)
- `CLAUDE.md` (genel CLI davranış)
- `logs/` (WP tamamlama izleri)

---

## Sürüm
- **v1 — 2026-05-26** — İlk WP-skill mapping; v2 execution planına eşlik eder
