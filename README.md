# KU — Thesis → IJPVP Paper Production Pipeline

> Systematic conversion of a Turkish MSc thesis on **ripple defect SCF & fatigue life in API 5L X70 high-strength gas pipelines** into a peer-reviewed English manuscript targeted at the *International Journal of Pressure Vessels and Piping* (Elsevier, Q1).

**Status:** Planning complete · WP1 awaiting author authorization
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
│       ├── 2026-05-26-execution-plan-IJPVP-v1.md     # Execution plan (envanter + WP akışı)
│       ├── WP1_thesis_to_paper_map.md                # (pending)
│       ├── WP2_citation_targets.md                   # (pending)
│       ├── WP3_figures_tables.md                     # (pending)
│       ├── WP4_section_drafting_plan.md              # (pending)
│       └── WP0d_rewrite_sop.md                       # (pending — K4 SOP)
├── Docs/paper/                         # (WP5+ — generated content)
│   ├── sections/                       # 01_introduction.md … 08_conclusions.md
│   ├── figures/                        # Regenerated publication-quality figures
│   ├── submission/                     # Cover letter, highlights, etc.
│   ├── references.bib                  # (WP6)
│   └── main.tex                        # (WP7 — IJPVP Elsevier template)
└── logs/                               # Manual milestone logs (see logs/README.md)
```

`_Archive/` (original .docx thesis source) is **gitignored** — copyright protected, local reference only.

---

## Workflow (Work Packages)

| WP | Purpose | Status |
|----|---------|--------|
| **WP0a** | Validation Audit (K2 gate) | ✅ Passed |
| **WP0b** | Anchor Claim Feasibility (K3) | 🟡 TOC-level positive; full check in WP1 |
| **WP0c** | Journal Targeting (K1) | ✅ IJPVP locked |
| **WP0d** | Anti-Plagiarism Rewrite SOP (K4) | ⏸ Triggered at WP5 start |
| **WP1** | Thesis-to-paper section mapping | ⏳ Awaiting `WP1 başlat` |
| **WP2** | Citation strategy & reference pool | ⏳ |
| **WP3** | Figures & tables strategy | ⏳ |
| **WP4** | Section-by-section drafting plan | ⏳ |
| **WP5** | Drafting (8 sections, one per session) | ⏳ |
| **WP6** | Citation verification + BibTeX | ⏳ |
| **WP7** | Self-review + LaTeX + submission package | ⏳ |

Each WP is gate-locked: no WP starts without author authorization; no WP is skipped.

**Realistic timeline:** 21–33 CLI sessions · 6–10 calendar weeks (incl. author review turns, optional FEA runs, iThenticate, advisor review).

See `Docs/plan/2026-05-26-execution-plan-IJPVP-v1.md` for the full execution plan.

---

## Critical Decisions (Locked)

- **K1 (Journal):** IJPVP — fixed, no alternatives in scope
- **K2 (Validation):** Author confirmed V1–V6 profile; gate passed; V1 mesh + V3 baseline are defensive mitigations, not blockers
- **K3 (Anchor):** Parametric SCF-to-life framework + critical SCF threshold for FFS
- **K4 (Anti-Plagiarism):** SOP deferred to WP5; YÖK thesis registration status must be confirmed before drafting begins

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
