# KU — Thesis → IJPVP Paper Production Pipeline

> Systematic conversion of a Turkish MSc thesis on **ripple defect SCF & fatigue life in API 5L X70 high-strength gas pipelines** into a peer-reviewed English manuscript targeted at the *International Journal of Pressure Vessels and Piping* (Elsevier, Q1).

**Status:** WP6a–WP6c complete (autonomous R2 chain) · final docx assembled · **WP6d (iThenticate, author) next** _(updated 2026-07-06)_
**Target journal:** International Journal of Pressure Vessels and Piping (IJPVP) — locked
**Source:** TR MSc thesis (Korcan Ünal, 2026) — local-only, not tracked

---

## Project Goal

Develop a parametric SCF-to-life framework for ILI-detected ripple defects, coupling FEA-derived stress concentration with Markl S-N and rainflow–Miner damage accumulation under realistic pressure-cycle spectra, and establish a critical SCF threshold for fitness-for-service decisions.

---

## Repository Layout

```
Korc/
├── README.md                           # This file
├── CLAUDE.md                           # Project-level Claude instructions
├── .gitignore
├── .claude/
│   ├── logs/                           # Session logs (auto-generated)
│   └── (settings.json — local-only, gitignored)
├── Docs/
│   ├── KUnal_tez_org_tr.md            # TR thesis (markdown — pandoc converted)
│   ├── media/media/                    # 18 figures extracted from thesis
│   └── plan/                           # Planning artifacts (WP0–WP7)
│       ├── 2026-05-26-paper-plan-IJPVP-v1.md         # Strategic plan (K1–K4 closed)
│       ├── 2026-05-26-execution-plan-IJPVP-v2.md     # Execution plan v2 (active)
│       ├── WP1_thesis_to_paper_map.md                # ✅ done
│       ├── WP2_citation_pool.md                      # ✅ done (~54 refs)
│       ├── WP3a_figure_strategy.md                   # ✅ done
│       ├── WP4_tables_equations.md                   # ✅ done
│       └── WP0d_rewrite_sop.md                       # ✅ done (K4 SOP, author-owned)
├── Docs/paper/                         # (WP5+ — generated content)
│   ├── sections/                       # 04_methods.md ✅ · 05_results.md ✅ · (06_discussion next)
│   ├── figures/                        # ✅ 10 figs (mf1–7, sf1–3) + scripts + manifest
│   ├── figures/equations/              # ✅ equations.tex (E1–E10)
│   ├── tables/                         # ✅ main_tables.tex + supplementary_tables.tex
│   ├── submission/                     # (WP7 — cover letter, highlights, etc.)
│   ├── references.bib                  # (WP6b)
│   └── main.tex                        # (WP7d — IJPVP Elsevier template)
└── logs/                               # Manual milestone logs (see logs/README.md)
```

`_Archive/` (original .docx thesis source) is **gitignored** — copyright protected, local reference only.

---

## Workflow (Work Packages v2)

> v2 reorders WPs in professional writing sequence: Methods first, Introduction second-to-last, Abstract last. Figures locked before text. See `Docs/plan/2026-05-26-execution-plan-IJPVP-v2.md`. v1 archived.

| WP | Purpose | Skill (primary) | Status |
|----|---------|-----------------|--------|
| **WP0a** | Validation Audit (K2 gate) | — | ✅ Passed |
| **WP0b** | Anchor Claim Feasibility (K3) | — | ✅ Resolved in WP1 (closed-form SCF_crit) |
| **WP0c** | Journal Targeting (K1) | — | ✅ IJPVP locked |
| **WP0d** | Anti-Plagiarism Rewrite SOP (K4) | — | ✅ Fixed (author-owned measures) |
| **WP1** | Thesis-to-paper map + IMRaD spine | `superpowers:writing-plans` | ✅ Done (Section A, 5-fold) |
| **WP2** | Citation pool (40–60 EN refs) | `citation-verification` | ✅ Done (~54 refs, 2→15 journals) |
| **WP3a** | Figure strategy (lock before text) | `publication-chart-skill` | ✅ Done (7 main + 3 supp) |
| **WP3b** | Figure production | `publication-chart-skill` | ✅ Done (10 figs, anchor verified) |
| **WP4** | Tables + equation derivations | `publication-chart-skill` | ✅ Done (4 main + 3 supp tables, E1–E10) |
| **WP5a** | **Methods** (first — most factual) | `ml-paper-writing` | ✅ Drafted (~1700 w) |
| **WP5b** | **Results** | `ml-paper-writing` | ✅ Drafted (~1300 w) |
| **WP5c** | **Discussion** | `ml-paper-writing` | ✅ Drafted (~1050 w, anchor) |
| **WP5d** | **Conclusion** | `ml-paper-writing` | ✅ Drafted (~230 w) |
| **WP5e** | **Introduction** (second-to-last) | `ml-paper-writing` | ✅ Drafted (~950 w) |
| **WP5f** | **Abstract + Title** (last) | `ml-paper-writing` | ✅ Drafted (196 w, 15-w title) |
| **WP5g** | **Highlights** | `ml-paper-writing` | ✅ Drafted (5 bullets) |
| **WP6a** | Coherence pass | `paper-self-review` | ✅ Done (QA-1..5, R1-R8, M2-M5, tez v2) |
| **WP6b** | Citation verification | `citation-verification` | ✅ Done (30 refs, DOI-verified) |
| **WP6c** | Anti-AI / language polish | `writing-anti-ai` | ✅ Done (Q1 register pass) |
| **WP6d** | iThenticate check (🔴 author) | — | ⏳ **Next** |
| **WP7a** | Cover letter + novelty | `doc-coauthoring` | ⏳ |
| **WP7b** | Graphical abstract | `publication-chart-skill` | ⏳ |
| **WP7c** | CRediT + declarations + data avail. | `doc-coauthoring` | ⏳ |
| **WP7d** | LaTeX migration (elsarticle) | `latex-conference-template-organizer` | ⏳ |
| **WP7e** | Final self-review | `paper-self-review` | ⏳ |
| **WP8** | Submission (🔴 author) | — | ⏳ |

**Progress: 19 / 26 WPs complete** (WP0a–d, WP1–WP4, WP5a–g, WP6a–c). Manuscript finalized against thesis v2 and assembled as `Docs/paper/submission/Unal_ripple_SCF_fatigue_IJPVP_R2.docx`. Author gate: WP6d (iThenticate) + künye teyitleri, then WP7 (submission package).

Each WP is gate-locked: no WP starts without author authorization; no WP is skipped. See `Docs/plan/WP_skill_mapping.md` for skill activation rules.

**Realistic timeline:** 27–43 CLI sessions · 6–10 calendar weeks.

See `Docs/plan/2026-05-26-execution-plan-IJPVP-v2.md` for the full execution plan.

---

## Critical Decisions (Locked)

- **K1 (Journal):** IJPVP — fixed, no alternatives in scope
- **K2 (Validation):** Author confirmed V1–V6 profile; gate passed; V1 mesh + V3 baseline are defensive mitigations, not blockers
- **K3 (Anchor):** Parametric SCF-to-life framework + critical SCF threshold for FFS
- **K4 (Anti-Plagiarism):** Rewrite SOP active (`WP0d_rewrite_sop.md`); YÖK registration + iThenticate measures **owned by author** (2026-06-02); CLI applies paraphrase-not-translate drafting procedure

---

## Log System

- **`.claude/logs/`** — auto-generated per-session logs (session ID + timestamp)
- **`logs/`** — manual milestone logs (one entry per WP completion, decision change, or scope shift). See `logs/README.md` for format.

---

## Confidentiality & Ethics

- Source thesis (`.docx`) is the author's intellectual property; not redistributed
- All figures will be regenerated for publication (visual similarity to thesis = 0)
- iThenticate target: < 15% overlap with author's own thesis
- Cover letter will include transparent disclosure of thesis-derived material
- Self-citation of thesis included in references

---

## Author

**Korcan Ünal** — MSc thesis author, primary investigator
Repository maintained for paper production workflow.

---

## License

Manuscript content: © Author, all rights reserved (pre-publication).
Tooling and planning artifacts: see future LICENSE file if open-sourced.
