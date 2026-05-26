# 🚀 Oturum Devir Dosyası (Session Handover)

> **Son oturum tarihi:** 2026-05-26
> **Sonraki oturumda ilk okunacak dosya:** Bu dosya
> **Sonraki adım:** Yazar `WP1 başlat` komutu vermeden CLI hiçbir yazıma başlamaz

---

## 1. Tek Cümlede Proje Durumu

Korcan Ünal'ın TR yüksek lisans tezini (API 5L X70 doğalgaz boru hatlarında mild ripple SCF + Markl/Miner yorulma analizi) **International Journal of Pressure Vessels and Piping** (Elsevier Q1, IF 3.500) dergisine **6.000 kelimelik original article** olarak hazırlamak üzere planlama tamamlandı; **27–43 oturumluk üretim akışı** Methods-first sırasında WP1–WP8 olarak gate'lenmiş hâlde duruyor; WP1 başlatma yetkisi yazardan bekleniyor.

---

## 2. Sabit Olan Kararlar (Pinned)

| # | Karar | Durum |
|---|---|---|
| **K1** | Hedef dergi: **IJPVP** (Elsevier, Q1/Q1, IF 3.500 — 2024 JCR) | 🔒 SABİT |
| **K2** | Validation Gate **GEÇTİ** — V4 (IPC2002-27124), V5 (S-N kalibrasyon), V6 (BC) güçlü; V1 (mesh) ve V3 (Lame baseline tezde zaten var) defansif | 🔒 SABİT |
| **K3** | Anchor claim: *"Parametric SCF-to-life framework + critical SCF threshold (1.51–1.65) for FFS decisions in API 5L X70 pipelines"* | 🔒 SABİT |
| **K4** | Anti-plagiarism SOP **WP5a başlamadan önce** somutlaşır; YÖK kayıt durumu danışmanla teyit edilmeli | ⏸ Beklemede |
| Article type | **Original article** — max 6.000 kelime / ~12 sayfa | 🔒 SABİT |
| Submission portalı | Editorial Manager: https://www.editorialmanager.com/IPVP | 🔒 SABİT |
| Hazırlık skoru | **66.5 / 100** (v1.2) | Mevcut |
| Kabul olasılığı (full prep) | **%67–77** | Tahmini |

---

## 3. Mevcut Dosya Yapısı (Onaylanmış)

```
Korc/                                                    https://github.com/zegran/KU
├── HANDOVER.md                                          ← BU DOSYA — yeni oturumun ilk durağı
├── README.md                                            Workflow tablosu v2
├── CLAUDE.md                                            Project-level Claude talimatları
├── .gitignore
│
├── _Archive/                                            🔒 GITIGNORED (local-only)
│   └── korcan_unal_tez (03052026).docx                  ← ORİJİNAL TEZ, asla dokunulmaz
│
├── Docs/
│   ├── KUnal_tez_org_tr.md                              🔒 FROZEN — TR tez markdown (1960 satır)
│   │
│   ├── media/media/image1-18.png                        🔒 FROZEN — 18 tez şekli (referans)
│   │
│   ├── refs/                                            🔒 IJPVP otoriter referansları
│   │   ├── IJPVP_official_sources.md                    🔒 v2 FROZEN — IJPVP tek kaynak gerçek
│   │   ├── pdfs/
│   │   │   ├── elsevier_references_style_guide.pdf     (470 KB)
│   │   │   └── elsevier_copy_editing_style.pdf         (660 KB)
│   │   └── archive/
│   │       └── IJPVP_official_sources_v1.md            v1 yedek
│   │
│   ├── plan/                                            📘 Authoritative planlar
│   │   ├── 2026-05-26-paper-plan-IJPVP-v1.md           Stratejik plan (K1–K4)
│   │   ├── 2026-05-26-execution-plan-IJPVP-v2.md       ← AKTİF execution plan
│   │   ├── 2026-05-26-readiness-assessment-TR.md       v1.2 — skor 66.5/100
│   │   ├── 2026-05-26-responsibility-matrix.md         RACI + dosya sahipliği
│   │   ├── WP_skill_mapping.md                         WP → Skill ataması
│   │   └── archive/
│   │       └── 2026-05-26-execution-plan-IJPVP-v1.md   v1 yedek
│   │
│   └── paper/                                           🔜 (WP5+ üretilecek)
│       ├── sections/                                    (boş — WP5a başlayınca dolar)
│       ├── figures/                                     (boş — WP3b başlayınca dolar)
│       ├── submission/                                  (boş — WP7 başlayınca dolar)
│       ├── references.bib                               (boş — WP6b'de oluşturulur)
│       └── main.tex                                     (boş — WP7d'de oluşturulur)
│
├── logs/                                                📝 Manuel milestone logları
│   ├── README.md
│   ├── 2026-05-26-01-project-bootstrap.md
│   ├── 2026-05-26-02-ijpvp-sources-and-reassessment.md
│   ├── 2026-05-26-03-ijpvp-sources-v2.md
│   ├── 2026-05-26-04-wp-structure-v2-skill-mapping.md
│   └── 2026-05-26-05-session-end-handover.md            ← FINAL LOG (bu oturum)
│
└── .claude/
    └── logs/                                            📝 Auto session logs (sistem)
```

---

## 4. WP Akışı (v2 — Aktif)

```
WP1 → WP2 ─────────┐
                   ├─→ WP3a → WP3b ──┐
WP4 ───────────────┘                  ├─→ WP5a → WP5b → WP5c → WP5d → WP5e → WP5f → WP5g
                                      │       (Methods→Results→Discussion→Conclusion→Intro→Abstract+Title→Highlights)
                                      │
                                      └─→ WP6a → WP6b → WP6c → WP6d
                                                 (Coherence → Citation → Anti-AI → 🔴 iThenticate)
                                                 ↓
                                      WP7a → WP7b → WP7c → WP7d → WP7e
                                                 ↓
                                              🔴 WP8 Submission
```

| WP | İçerik | Sorumlu Skill | Sonraki tetik |
|----|---|---|---|
| WP1 | Thesis-to-paper map + IMRaD spine (6.000 kelime tahsisi) | `superpowers:writing-plans` | `WP1 başlat` |
| WP2 | Citation pool (40–60 EN ref) | `citation-verification` | `WP2 başlat` |
| WP3a | Figür stratejisi (karar) | `publication-chart-skill` | `WP3a başlat` |
| WP3b | Figür üretimi (8 main + supp) | `publication-chart-skill` | `WP3b başlat` |
| WP4 | Tablolar + denklem türetimleri | `publication-chart-skill` | `WP4 başlat` |
| **WP5a** | **Methods (önce)** | `ml-paper-writing` | `WP5a başlat` |
| WP5b | Results | `ml-paper-writing` | `WP5b başlat` |
| WP5c | Discussion | `ml-paper-writing` | `WP5c başlat` |
| WP5d | Conclusion | `ml-paper-writing` | `WP5d başlat` |
| WP5e | Introduction (sondan ikinci) | `ml-paper-writing` | `WP5e başlat` |
| WP5f | Abstract + Title (son) | `ml-paper-writing` | `WP5f başlat` |
| WP5g | Highlights | `ml-paper-writing` | `WP5g başlat` |
| WP6a | Coherence pass | `paper-self-review` | `WP6a başlat` |
| WP6b | Citation verification | `citation-verification` | `WP6b başlat` |
| WP6c | Anti-AI polish | `writing-anti-ai` | `WP6c başlat` |
| WP6d | iThenticate (🔴 yazar) | — | yazar manuel |
| WP7a | Cover letter + novelty | `doc-coauthoring` | `WP7a başlat` |
| WP7b | Graphical abstract | `publication-chart-skill` | `WP7b başlat` |
| WP7c | CRediT + declarations + data avail. | `doc-coauthoring` | `WP7c başlat` |
| WP7d | LaTeX migration (cas-sc) | `latex-conference-template-organizer` | `WP7d başlat` |
| WP7e | Final self-review | `paper-self-review` | `WP7e başlat` |
| WP8 | Submission (🔴 yazar) | — | Editorial Manager |

---

## 5. ⚠ Yazar Bekleyen Aksiyonlar (Sonraki Oturum Önce)

### Yüksek öncelik (WP başlatmadan önce)
1. **YÖK tez kayıt durumu** danışmanla teyit (K4 SOP tetikleyicisi)
2. **IJPVP Guide for Authors** sayfasından kesin abstract kelime limiti ve diğer article type limitleri manuel doğrulama

### Orta öncelik (WP1–WP4 sürerken paralel)
3. **Mevcut 9 ⚠ madde** (`IJPVP_official_sources.md` sonunda) — yazar manuel dergi sayfasından doğrulama
4. **V1 mesh independence** için ek 1–2 FEA koşusu kararı (defansif, gate değil)
5. **V3 baseline koşusu** — tezde zaten Lame karşılaştırması var (line 743-749), ek koşu **gereksiz** olabilir; WP1'de teyit

### Düşük öncelik (ileride)
6. Dergi son makalelerinin "received → accepted" tarihlerini inceleyip gerçek peer-review süresini doğrulama (LetPub'daki 24 ay olağandışı)

---

## 6. Sonraki Oturum Açıldığında Yapılacak İş Sırası

CLI ortamı:

```
1. HANDOVER.md (bu dosya) → ilk durak
2. CLAUDE.md → otomatik yüklü
3. Docs/refs/IJPVP_official_sources.md (v2) → IJPVP soruları için
4. Docs/plan/2026-05-26-execution-plan-IJPVP-v2.md → WP akışı
5. Docs/plan/WP_skill_mapping.md → Skill tetikleyicileri
```

Yazar komutu beklenir. İlk komut iki seçenek arasında:

**Seçenek A** — Doğrudan WP1 başlat:
> "WP1 başlat"

CLI otomatik `Skill(superpowers:writing-plans)` aktive edip tez okuma + IMRaD spine üretimine geçer.

**Seçenek B** — Önce ⚠ doğrulamaları yap:
> "Yazar 9 ⚠ maddesi için dergi sayfasından bilgileri topladı, IJPVP_official_sources v3'e taşı"

CLI v2 → v3 güncellemesi yapar, sonra WP1'e geçilir.

---

## 7. Repo Durumu

| Kalem | Değer |
|---|---|
| GitHub | https://github.com/zegran/KU (public, main branch) |
| Commit sayısı | 4 |
| Son commit | `948d248 plan(wp): restructure to v2 + skill mapping` |
| Tracked dosya sayısı | ~40 |
| Boyut | ~7 MB tracked (5.9 MB media + ~1 MB plan/refs + 1.1 MB PDF) |
| `_Archive/` | gitignored, local-only (17 MB) |

### Push durumu
- ✅ Tüm değişiklikler push edildi
- ✅ Working tree temiz (uncommitted yok)
- ✅ Remote tracking aktif

---

## 8. Hızlı Komut Referansı (Sonraki Oturum)

```
# Repo durumu kontrol
git log --oneline
git status

# Bir WP başlat (örnek)
"WP1 başlat"

# Bir log eklemek için (CLI yapacak)
logs/YYYY-MM-DD-NN-<slug>.md

# IJPVP referans güncelleme (v3'e taşı, yazar onayıyla)
"IJPVP_official_sources v3'e güncelle: [yeni doğrulanan maddeler]"

# Hazırlık raporu yeniden hesaplama
"readiness-assessment v1.3 — [yeni veri] sonrası skor revize"
```

---

## 9. Bilinmeyen / Risk Olarak Kalan Noktalar

| Risk | Etki | Mitigation |
|---|---|---|
| 9 ⚠ IJPVP detayı (abstract limit, article type limits) | Section drafting'de yanlış tahsis | WP1'de teyit gerek |
| 24-ay peer review süresi (tek kaynak) | Takvim 6–10 hafta'dan çok daha uzun olabilir | Dergi son makalelerinin tarihleri kontrol |
| iThenticate skor (K4) | WP5 sonu yüksek çıkarsa WP6c'ye geri dönüş | Anti-plagiarism SOP disiplini |
| Anchor F8 (critical SCF curve) parametrik veri girdisi | WP3b'de yazar veri sağlamazsa darboğaz | Yazar tez Tablo 3.11'den türetebilir |
| D/t = 73.1 tek değer kısıtı | Hakem genelleştirme isteyebilir | Discussion'da explicit yazılır; future work eklenir |

---

## 10. Kapanış Notu

Bu oturumda **5 commit, 40+ dosya, ~25k satır** üretildi. Tüm plan otoriter dosyalar v1/v2 versiyonlanmış. Hiçbir aşama atlanmadı; gate disiplini aktif.

**Hiçbir kazanım kaybedilmedi.** Repo GitHub'da, plan dosyaları FROZEN, log zinciri tam. Sonraki oturumun başlangıcı için yeterli bağlam burada.

**Sonraki adım yazar elinde:** YÖK kayıt teyidi sonrası `WP1 başlat`.

---

## Sürüm
- **v1 — 2026-05-26** — İlk oturum sonu devir dosyası
