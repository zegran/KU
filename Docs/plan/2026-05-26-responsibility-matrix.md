# Sorumluluk Matrisi ve Dosya Bağımlılıkları (v1)

**Tarih:** 2026-05-26
**Amaç:** Proje genelindeki tüm artefakt dosyalarının sahibini, otoritesini, bağımlılığını ve değişiklik kuralını tek tabloda sabitlemek. CLI ve yazar arasındaki sorumluluk sınırlarını netleştirir.

---

## 1. Otorite Sınıflandırması

| Sınıf | Anlam | Değişiklik kuralı |
|---|---|---|
| 🔒 **FROZEN** | Yazar onayı olmadan asla değiştirilmez | Yazar açıkça "v2 olarak güncelle" demeden dokunulmaz |
| 📘 **Authoritative** | Proje boyunca tek kaynak gerçek; karar dayanağı | Sadece yazar onayıyla güncellenir; CLI öneri sunar |
| 📒 **Living** | Aktif gelişen; aşamalar ilerledikçe yeniden yazılır | CLI üretir, yazar her checkpoint'te onaylar |
| 📝 **Log** | Tarihli, immutable; yanlışsa yeni log + çapraz referans | Eklenir, asla düzenlenmez |
| 🔧 **Infrastructure** | Repo işletim katmanı (config, settings, gitignore) | CLI değiştirir; hassas konularda yazara sorulur |

---

## 2. Dosya Envanteri ve Sorumluluk

### 2.1 Kaynak (read-only, eternally untouchable)
| Dosya | Sınıf | Sahip | Bağımlı olduğu | Etkilediği |
|---|---|---|---|---|
| `_Archive/korcan_unal_tez (03052026).docx` | 🔒 FROZEN | Yazar | — | `Docs/KUnal_tez_org_tr.md` (pandoc kaynak) |
| `Docs/KUnal_tez_org_tr.md` | 🔒 FROZEN | CLI (üretildi) | `_Archive/*.docx` | WP1, hazırlık raporu, tüm sonraki section taslakları |
| `Docs/media/media/image{1-18}.png` | 🔒 FROZEN | CLI (extract) | `_Archive/*.docx` | WP3 (yeniden çizim için referans) |

### 2.2 Resmi Referanslar
| Dosya | Sınıf | Sahip | Bağımlı olduğu | Etkilediği |
|---|---|---|---|---|
| `Docs/refs/IJPVP_official_sources.md` | 🔒 FROZEN | CLI (oluşturdu), yazar (doğrulayacak ⚠ maddeler) | Web kaynakları (4 birincil + 2 PDF) | Tüm IJPVP-ilgili kararlar; readiness v1.1; WP1+ |
| `Docs/refs/pdfs/elsevier_references_style_guide.pdf` | 🔒 FROZEN | Elsevier | — | WP6 (citation formatting) |
| `Docs/refs/pdfs/elsevier_copy_editing_style.pdf` | 🔒 FROZEN | Elsevier | — | WP5 (drafting style), WP7 (final pass) |

### 2.3 Planlama
| Dosya | Sınıf | Sahip | Bağımlı olduğu | Etkilediği |
|---|---|---|---|---|
| `Docs/plan/2026-05-26-paper-plan-IJPVP-v1.md` | 📘 Authoritative | Yazar (kararlar), CLI (yazım) | K1–K4 yazar kararları | Tüm WP'ler |
| `Docs/plan/2026-05-26-execution-plan-IJPVP-v1.md` | 📘 Authoritative | Yazar (kararlar), CLI (yazım) | paper-plan-v1, IJPVP_official_sources | WP1–WP7 işletim |
| `Docs/plan/2026-05-26-readiness-assessment-TR.md` | 📘 Authoritative | CLI (yazım), yazar (onay) | tez markdown, IJPVP_official_sources | WP1 başlatma kararı |
| `Docs/plan/2026-05-26-responsibility-matrix.md` | 📘 Authoritative | Bu dosya | — | Tüm değişiklik kararları |
| `Docs/plan/WP{1-7}_*.md` | 📒 Living | CLI üretecek, yazar onaylar | İlgili WP girdileri | Sonraki WP'ler |
| `Docs/plan/WP0d_rewrite_sop.md` | 📘 Authoritative (üretilince) | CLI yazacak, yazar onaylar | K4 kararları + YÖK durumu | WP5 her section başında |

### 2.4 Paper Çıktıları (WP5+)
| Dosya | Sınıf | Sahip | Bağımlı olduğu | Etkilediği |
|---|---|---|---|---|
| `Docs/paper/sections/0{1-8}_*.md` | 📒 Living | CLI üretecek, yazar onaylar | WP4 plan + tez markdown + WP0d SOP | LaTeX migration, submission |
| `Docs/paper/figures/*` | 📒 Living | CLI + yazar (veri/onay) | WP3 plan + tez verisi | Submission |
| `Docs/paper/references.bib` | 📒 Living | CLI üretecek, citation-verification gate | WP2 + WP6 | Submission |
| `Docs/paper/main.tex` | 📒 Living | CLI (WP7) | Tüm sections + figures + bib | Submission |
| `Docs/paper/submission/*` | 📒 Living | CLI + yazar (CRediT, data avail.) | Tüm önceki çıktılar | Submit |

### 2.5 Repo Infrastructure
| Dosya | Sınıf | Sahip | Bağımlı olduğu | Etkilediği |
|---|---|---|---|---|
| `README.md` | 🔧 Infra | CLI maintain | — | GitHub görüntüleme |
| `CLAUDE.md` | 🔧 Infra | CLI maintain | Plan dosyaları | Tüm CLI oturumları |
| `.gitignore` | 🔧 Infra | CLI maintain | — | Git tracking |
| `logs/README.md` | 🔧 Infra | CLI | — | Log disiplini |
| `logs/YYYY-MM-DD-NN-*.md` | 📝 Log (immutable) | CLI yazar | İlgili olay | Tarih çizgisi |
| `.claude/logs/session-*.md` | 📝 Log (auto) | Sistem | — | Oturum izi |

---

## 3. Sorumluluk Akışı (RACI tarzı)

| Aktivite | CLI | Yazar | Danışman | Sistem (Git/iThenticate) |
|---|---|---|---|---|
| Tezi okuma + map | R | A | — | — |
| K1–K4 stratejik karar | C | A,R | C | — |
| IJPVP scope teyidi | R | A | — | — |
| Validation audit | R | A | C (ek FEA için) | — |
| Section drafting (TR→EN) | R | A | — | — |
| Anti-plagiarism SOP uygulama | R | A | — | iThenticate kontrol |
| Şekil yeniden üretim | R | A,C (görsel onay) | — | — |
| Citation verification | R | A | — | — |
| LaTeX migration | R | A | — | — |
| Cover letter | C,R | A | C | — |
| iThenticate çekimi | — | A,R | — | I |
| Submission | — | A,R | A | I (Editorial Manager) |
| Rebuttal | C,R | A | C | I |
| Ek FEA koşusu | — | C | A,R | — |
| Git commit/push | R | A | — | I |

**Lejant:** R=Responsible (yapan), A=Accountable (sorumlu/onaylayan), C=Consulted, I=Informed

---

## 4. Değişiklik Kuralları

### 🔒 FROZEN dosyalar
- Yazar açıkça **"v2 olarak güncelle"** demeden değiştirilmez
- ⚠ işaretli eksik maddeler yazardan toplanır, **yazar onayıyla** dosyaya eklenir
- Yanlış bilgi tespit edilirse: dosyaya **yazma**, yazara bildir + log

### 📘 Authoritative dosyalar
- Yazar onayı şart; CLI sadece **değişiklik önerisi** sunar (diff veya açıklama)
- Versiyon bump (v1 → v2) yapılır; v1 silinmez, history korunur

### 📒 Living dosyalar
- CLI üretir, her checkpoint'te yazar onayı alır
- Onay sonrası "kabul" işaretiyle bir sonraki aşamaya geçilir

### 📝 Log
- Eklenir, asla düzenlenmez
- Yanlışlık tespit edilirse yeni log + eski loga çapraz referans

### 🔧 Infrastructure
- CLI tipik düzeltmeleri yapar; **secret/credential** içeren değişikliklerde yazara sorulur
- Hassas dosyalar (`settings.json`) gitignored — push edilemez

---

## 5. Çatışma Çözümü

| Senaryo | Eylem |
|---|---|
| FROZEN dosyada eksiklik | ⚠ olarak işaretle, yazardan iste, dosyaya yazma |
| İki kaynakta çelişki | Daha otoriter olanı kullan; çelişkiyi belgele; yazara bildir |
| Plan kararı ile uygulama çatışıyor | Plan otoriterdir; uygulama duracak, yazara sor |
| Yazar talimatı CLAUDE.md ile çatışıyor | Yazar talimatı önceliklidir (CLAUDE.md user instruction precedence prensibi) |
| WP atlama isteği | Reddedilir, execution plan gate kuralı gereği yazardan açık onay istenir |

---

## Sürüm
- **v1 — 2026-05-26** — İlk sorumluluk matrisi; IJPVP_official_sources.md FROZEN sonrası
