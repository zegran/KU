# Project-Level Claude Instructions — KU (Thesis → IJPVP Paper)

This file is auto-loaded by Claude Code when working in this repository. It overrides default behavior for this project only. User global instructions still apply.

---

## Project Identity

- **Goal:** Convert TR MSc thesis → English manuscript for *International Journal of Pressure Vessels and Piping* (Elsevier, Q1)
- **Subject domain:** API 5L X70 pipeline integrity, ripple defect SCF, FEA + Markl/Miner fatigue
- **Author:** Korcan Ünal
- **Status:** Planning phase complete; awaiting `WP1 başlat`

## Authoritative References (read before acting)

1. `Docs/refs/IJPVP_official_sources.md` — 🔒 **FROZEN v2** single source of truth for IJPVP. Every IJPVP-related decision starts here. **No new web searches for IJPVP** — view this file instead. Missing items marked ⚠ are author-doğrulanacak.
2. `Docs/plan/2026-05-26-paper-plan-IJPVP-v1.md` — strategic plan, K1–K4 closed
3. `Docs/plan/2026-05-26-execution-plan-IJPVP-v2.md` — **v2** execution plan (Methods-first writing order, WP1–WP8). v1 archived.
4. `Docs/plan/WP_skill_mapping.md` — per-WP skill activation rules (Skill() trigger + log format)
5. `Docs/plan/2026-05-26-readiness-assessment-TR.md` — current readiness 66.5/100 (v1.2)
6. `Docs/plan/2026-05-26-responsibility-matrix.md` — file ownership + change rules
7. `README.md` — repo overview

When the user issues a `WP<N> başlat` command, follow the execution plan exactly. Do not improvise WP scope.

## Hard Rules

1. **`_Archive/korcan_unal_tez (03052026).docx`** — read-only. Never modify, never delete, never write. Pandoc conversion already done into `Docs/KUnal_tez_org_tr.md`; use the markdown.
2. **No WP skipping or merging.** Gate-locked sequence: WP1 → WP2 → WP3 → WP4 → WP5 → WP6 → WP7. Author authorization required for each.
3. **No optimistic time estimates.** Use the conservative ranges from the execution plan.
4. **K4 (anti-plagiarism) is non-negotiable.** WP5 cannot start until:
   - `Docs/plan/WP0d_rewrite_sop.md` exists and is approved
   - Author confirms YÖK thesis registration status
5. **All paper figures must be regenerated** (no thesis figure reused as-is in publication output). Original 18 figures in `Docs/media/media/` are reference only.
6. **Communication language:** Turkish (user preference). Technical terms and paper content remain English.
7. **Author authorization is required for any push, submission, or external action.**
8. **IJPVP web search is BANNED.** `Docs/refs/IJPVP_official_sources.md` is FROZEN single source of truth. For any IJPVP question, `view` this file. If information is missing, mark ⚠ and ask the author — never re-fetch.

## Drafting Discipline (WP5 onward)

When drafting any section:
1. Read the relevant TR thesis line range
2. Extract an EN bullet-point skeleton (≤10 words per bullet)
3. **Close the TR source** (do not look while drafting prose)
4. Write EN prose from the skeleton + mental model
5. Run `writing-anti-ai` on the draft
6. Cross-check TR ↔ EN for content coverage (not phrasing)
7. Save to `Docs/paper/sections/0N_<name>.md`
8. Wait for author approval before next section

This SOP will be formalized in `Docs/plan/WP0d_rewrite_sop.md` at WP4 end.

## Logging

After every meaningful WP step or decision change:
1. Append milestone log to `logs/` per `logs/README.md` format
2. Update `Docs/plan/` files with status changes
3. Use git commits with Conventional Commits format (`plan:`, `docs:`, `wp1:`, etc.)

## Skill Routing (project-specific)

- Section drafting → `ml-paper-writing` + `doc-coauthoring`
- AI-tone removal → `writing-anti-ai`
- Citation verification → `citation-verification`
- Figure regeneration → `publication-chart-skill` + `matplotlib-visualization`
- Self-review → `paper-self-review`
- LaTeX migration → `latex-conference-template-organizer`
- Rebuttal (post-submission) → `review-response`

## Forbidden

- Direct TR → EN translation (use rewrite SOP)
- Pushing without explicit author authorization
- Editing `_Archive/`
- Modifying authoritative plan files (`*-v1.md`) without explicit author request (version bump to v2 instead)
- Claiming a WP is complete without checkpoint approval
