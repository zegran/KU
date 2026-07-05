"""WP6 Faz 6 (M6) — IJPVP R2 docx assembly.
Reads section .md files, strips HTML comments, inserts figures (at first-citation
anchors) and tables (markdown pipe tables), appends declarations + references +
supplementary, writes master.md, runs pandoc -> docx.
"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(r"C:\Users\zduna\Desktop\Korc")
SEC = ROOT / "Docs" / "paper" / "sections"
FIG = ROOT / "Docs" / "paper" / "figures"
OUT = ROOT / "Docs" / "paper" / "submission"
SCRATCH = Path(__file__).parent
MASTER = SCRATCH / "master.md"
DOCX = OUT / "Unal_ripple_SCF_fatigue_IJPVP_R2.docx"

STRIP = re.compile(r"<!--.*?-->", re.DOTALL)

def load(name: str) -> str:
    txt = (SEC / name).read_text(encoding="utf-8")
    return STRIP.sub("", txt).strip()

def paras(txt: str):
    return [p for p in txt.split("\n\n") if p.strip()]

def insert_after(plist, anchor, block):
    for i, p in enumerate(plist):
        if anchor in p:
            plist.insert(i + 1, block)
            return plist
    sys.exit(f"ANCHOR NOT FOUND: {anchor[:60]}")

def fig(n, fname, caption, width="15cm"):
    return f"![Fig. {n}. {caption}]({(FIG / fname).as_posix()}){{width={width}}}"

# ---------------- tables (markdown; caption ABOVE per Elsevier) ----------------
T1 = """Table 1. Parametric pipe geometries (constant $D/t = 73.1$, $\\sigma_h = 349.2$ MPa, $P = 9.55$ MPa) and resulting $\\mathrm{SCF}_P$ summary over the Taguchi L9 array.

| OD | $D$ (mm) | $t$ (mm) | $D/t$ | $\\mathrm{SCF}_P$ range | Mean* |
|----|---------|----------|-------|------------------------|-------|
| 36″ | 914.4 | 12.50 | 73.1 | 1.52–2.37 | 1.89 |
| 48″ | 1219.2 | 16.67 | 73.1 | 1.50–2.14 | 1.78 |
| 56″ | 1422.4 | 19.45 | 73.1 | 1.42–1.95 | 1.68 |

*Mean of the nine tabulated L9 cases. Overall $\\mathrm{SCF}_P$ range 1.42–2.37; smaller diameter gives higher SCF."""

T2 = """Table 2. Numerical model and material parameters (representative validation model).

| Parameter | Value |
|-----------|-------|
| Solver | Abaqus/Standard 2020 |
| Element type | S4R (4-node reduced-integration shell) |
| DOF per node | 6 |
| Element shape / scheme | quadrilateral / structured |
| Elements | 31,968 |
| Total DOF | ≈194,388 |
| Model symmetry | half-symmetric (180°) |
| Model length | 5,000 mm |
| Aspect-ratio criterion | ≤ 3 |
| Material model | isotropic linear elastic (API 5L X70) |
| Young's modulus, $E$ | 203,000 MPa |
| Poisson's ratio, $\\nu$ | 0.3 |"""

T3 = """Table 3. Verification and validation against the full-scale benchmark of Rosenfeld et al. [4], matched case $d/D = 0.037$, $a/C = 0.5$. Reference stresses converted from ksi.

| Quantity | Reference | This work | Difference |
|----------|-----------|-----------|------------|
| End-cap force (N) | 1,128,697 | 1,128,840 | 0.013% |
| Nominal hoop stress (MPa) | 220.8 (analytic) | ≈220.8 (FEA) | — |
| von Mises peak (MPa) | 784.0 | 718.6 | −8.3% |
| $S_{11}$ circumferential (MPa) | 759.9 | 796.8 | +4.9% |
| $S_{22}$ axial (MPa) | 806.8 | 755.9 | −6.3% |
| $\\mathrm{SCF}_P$ (von Mises basis) | 3.549 | 3.254 | −8.3% |"""

T4 = """Table 4. $\\mathrm{SCF}_P$ sensitivity of fatigue life ($n = 12$ full MAOP cycles/yr, $\\sigma_h = 349.2$ MPa, 100-yr design life). Critical threshold at $\\mathrm{SCF}_P \\approx 1.56$.

| $\\mathrm{SCF}_P$ | $N_f$ | $D_{m,100\\,\\mathrm{yr}}$ | $t_{\\mathrm{est}}$ (yr) | Status |
|------|------|------|------|--------|
| 1.42 | 1932 | 0.62 | 161 | $D_m < 1$ (safe) |
| 1.51 | 1422 | 0.84 | 118 | $D_m < 1$ (attention) |
| 1.65 | 912 | 1.32 | 76 | $D_m > 1$ |
| 1.95 | 396 | 3.03 | 33 | $D_m > 1$ |
| 2.14 | 249 | 4.83 | 21 | $D_m > 1$ |
| 2.37 | 149 | 8.04 | 12 | $D_m > 1$ |

Mixed spectrum (56″ D7, $\\mathrm{SCF}_P = 1.95$): $D_{m,\\mathrm{yr}} = 2.90 \\times 10^{-2}$, $t_{\\mathrm{est}} \\approx 34$ yr; the 80%-MAOP band contributes 68.6% of annual damage."""

TS1_HEADER = """Table S1. Full Taguchi L9 array and FEA $\\mathrm{SCF}_P$ for the three diameters ($D/t = 73.1$, API 5L X70).

| OD | Case | $\\theta$ (°) | $d$ (mm) | $d/D$ | $d/t$ | $L/d$ | $a/C$ | $\\mathrm{SCF}_P$ |
|----|------|------|------|------|------|------|------|------|"""

L9 = {
    "36″": [("D1",90,18,0.0197,1.440,10,0.250,1.72),("D2",90,24,0.0262,1.920,10,0.250,1.85),
            ("D3",90,30,0.0328,2.400,12,0.250,1.89),("D4",135,24,0.0262,1.920,7.5,0.375,2.06),
            ("D5",135,30,0.0328,2.400,8,0.375,2.10),("D6",135,18,0.0197,1.440,20,0.375,1.52),
            ("D7",180,30,0.0328,2.400,6,0.500,2.37),("D8",180,18,0.0197,1.440,13.3,0.500,1.80),
            ("D9",180,24,0.0262,1.920,15,0.500,1.72)],
    "48″": [("D1",90,18,0.0148,1.080,10,0.250,1.60),("D2",90,24,0.0197,1.440,10,0.250,1.77),
            ("D3",90,30,0.0246,1.800,12,0.250,1.86),("D4",135,24,0.0197,1.440,7.5,0.375,1.87),
            ("D5",135,30,0.0246,1.800,8,0.375,2.00),("D6",135,18,0.0148,1.080,20,0.375,1.50),
            ("D7",180,30,0.0246,1.800,6,0.500,2.14),("D8",180,18,0.0148,1.080,13.3,0.500,1.61),
            ("D9",180,24,0.0197,1.440,15,0.500,1.67)],
    "56″": [("D1",90,18,0.0127,0.925,10,0.250,1.42),("D2",90,24,0.0169,1.234,10,0.250,1.70),
            ("D3",90,30,0.0211,1.542,12,0.250,1.78),("D4",135,24,0.0169,1.234,7.5,0.375,1.74),
            ("D5",135,30,0.0211,1.542,8,0.375,1.91),("D6",135,18,0.0127,0.925,20,0.375,1.45),
            ("D7",180,30,0.0211,1.542,6,0.500,1.95),("D8",180,18,0.0127,0.925,13.3,0.500,1.51),
            ("D9",180,24,0.0169,1.234,15,0.500,1.63)],
}
rows = []
for od, data in L9.items():
    for j, (c,th,d,dD,dt,Ld,aC,s) in enumerate(data):
        rows.append(f"| {od if j==0 else ''} | {c} | {th} | {d} | {dD:.4f} | {dt:.3f} | {Ld} | {aC:.3f} | {s:.2f} |")
TS1 = TS1_HEADER + "\n" + "\n".join(rows)

TS2 = """Table S2. Relative single-cycle damage vs $\\Delta P/\\mathrm{MAOP}$ ($\\mathrm{SCF}_P = 1.95$, $\\sigma_h = 349.2$ MPa).

| $\\Delta P/\\mathrm{MAOP}$ | $S_a$ (MPa) | $N_i$ | Cycles equal to one full-MAOP cycle |
|------|------|------|------|
| 100% | 174.6 | 396 | 1 |
| 80% | 139.7 | 1.21×10³ | 3 |
| 50% | 87.3 | 1.27×10⁴ | 32 |
| 20% | 34.9 | 1.23×10⁶ | 3,134 |
| 10% | 17.5 | 3.91×10⁷ | 98,862 |
| 5% | 8.7 | 1.27×10⁹ | 3,255,554 |"""

TS3 = """Table S3. Single full-MAOP cycle: $N_f$ and unit damage (D7 configuration, $C' = 1126$ MPa, $S_a = 174.6$ MPa).

| OD | $\\mathrm{SCF}_P$ (D7) | $N_f$ | $d_i$ ($n = 1$) | $t_{\\mathrm{est}}$ (yr) |
|----|------|------|------|------|
| 56″ | 1.95 | 396 | 2.53×10⁻³ | 396 |
| 48″ | 2.14 | 249 | 4.02×10⁻³ | 249 |
| 36″ | 2.37 | 149 | 6.70×10⁻³ | 149 |"""

# ---------------- figure captions (final, from manifest) ----------------
CAP = {
 1: ("mf2_ripple_geometry.png", "Ripple geometry parameterisation: (a) longitudinal raised-cosine crest–trough profile (depth *d*, half-wavelength *L*/2); (b) circumferential extent θ (*a/C*). Constant *D/t* = 73.1, API 5L X70, *P* = 9.55 MPa."),
 2: ("mf1_model_setup.png", "Half-symmetric S4R shell model of a field-bend ripple in an API 5L X70 pipe: (a) geometry, mesh and global axes; (b) internal pressure, end-cap force and boundary conditions via RP-1; (c) structured quadrilateral mesh detail at the ripple."),
 3: ("mf3_validation.png", "Model validation against the full-scale benchmark of Rosenfeld et al. [4]: (a) S11 hoop-stress contour at the ripple; (b) peak-stress benchmark (end-cap force 0.013%; nominal hoop 220.8 MPa analytic; SCF 3.25 vs 3.55)."),
 4: ("mf4_parametric_scf.png", "Parametric SCF~P~ over the Taguchi L9 array at three diameters: (a) FEA SCF~P~ per case; (b) FEA vs the reference correlation (Eq. 8); (c) deviation from Eq. 8 vs circumferential extent *a/C*."),
 5: ("mf5_ldscf_regression.png", "Empirical SCF correlation (Eq. 9): (a) predicted vs FEA with ±9% band (R² = 0.916, RMSE = 0.058); (b) relative residual distribution."),
 6: ("mf6_mixed_spectrum.png", "Mixed-spectrum annual fatigue-damage distribution for the 56″ D7 case (SCF~P~ = 1.95): the 80%-MAOP band contributes 68.6% of the damage; t~est~ ≈ 34 yr."),
 7: ("mf7_anchor_scf_threshold.png", "Critical SCF threshold master curve: estimated fatigue life vs SCF~P~ for n = 4/8/12/24 full-MAOP-equivalent cycles per year; the intersection with the 100-yr design-life line gives SCF~crit~ ≈ 1.56 at n = 12 (Eq. 10). Parametric FEA configurations overlaid."),
}
SCAP = {
 "S1": ("sf1_mesh_quality.png", "Structured quadrilateral mesh quality; element aspect ratio ≤ 3 throughout."),
 "S2": ("sf2_caliper_to_fea.png", "Schematic geometry-ILI radius map and extraction of the representative FEA ripple parameters (*L*, *d*, θ/*aC*)."),
 "S3": ("sf3_stress_contours.png", "Full stress-component contour set at the ripple: (a) von Mises, (b) S11 circumferential, (c) S22 axial."),
}

# ---------------- front matter ----------------
abstract_src = load("00_abstract_title.md")
m_title = re.search(r"# Title\s+\*\*(.+?)\*\*", abstract_src, re.DOTALL)
m_abs = re.search(r"# Abstract\s+(.+?)\s+---", abstract_src, re.DOTALL)
m_kw = re.search(r"# Keywords\s+(.+?)$", abstract_src, re.DOTALL | re.MULTILINE)
title = m_title.group(1).strip()
abstract = m_abs.group(1).strip()
keywords = m_kw.group(1).strip().splitlines()[0].strip()

highlights_src = STRIP.sub("", (OUT / "Highlights.md").read_text(encoding="utf-8")).strip()
highlights = re.search(r"# Highlights\s+(.+)$", highlights_src, re.DOTALL).group(1).strip()

refs = load("08_references.md")
refs = re.sub(r"^# References\s*", "", refs).strip()

front = f"""# {title}

Korcan Ünal^a^

^a^ [Affiliation, City, Country — to be completed by the author] · ORCID: [⚠ author] · e-mail: [⚠ author]

# Highlights

{highlights}

# Abstract

{abstract}

**Keywords:** {keywords}
"""

# ---------------- body assembly ----------------
intro = load("01_introduction.md")
methods = load("04_methods.md")
results = load("05_results.md")
discussion = load("06_discussion.md")
conclusion = load("07_conclusion.md")

mp = paras(methods)
insert_after(mp, "Holding $D/t$ constant serves a second purpose", T1)
insert_after(mp, "The full array is given in Table S1.", fig(1, *CAP[1]))
insert_after(mp, "$E = 203$ GPa and $\\nu = 0.3$", T2)
insert_after(mp, "adopted for the full parametric family [4]", fig(2, *CAP[2]))
insert_after(mp, "confirming the boundary conditions and material setup.", T3)
insert_after(mp, "supports use of the model in the parametric study.", fig(3, *CAP[3]))
methods = "\n\n".join(mp)

rp = paras(results)
insert_after(rp, "the minima were the shallow narrow cases (D1, D6).", fig(4, *CAP[4]))
insert_after(rp, "no systematic bias.", fig(5, *CAP[5]))
insert_after(rp, "developed in Section 4.", T4)
insert_after(rp, T4[:40], fig(6, *CAP[6]))
results = "\n\n".join(rp)

dp = paras(discussion)
insert_after(dp, "the rigorous-analysis route of API 579 [27].", fig(7, *CAP[7]))
discussion = "\n\n".join(dp)

declarations = """# Declarations

**CRediT authorship contribution statement.** Korcan Ünal: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing – original draft, Writing – review & editing, Visualization.

**Funding.** [⚠ Author to confirm — e.g. "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors."]

**Declaration of competing interest.** [⚠ Author to confirm — e.g. "The author declares that he has no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper."]

**Data availability.** [⚠ Author to confirm — e.g. "The finite element results and the data supporting the fitted correlation are available from the author on reasonable request."]

**Acknowledgements.** [⚠ Optional — author to complete or delete.]
"""

supp = "\n\n".join([
    "# Supplementary material",
    TS1, TS2, TS3,
    fig("S1", *SCAP["S1"], width="12cm"),
    fig("S2", *SCAP["S2"], width="12cm"),
    fig("S3", *SCAP["S3"], width="15cm"),
])

master = "\n\n".join([front, intro, methods, results, discussion, conclusion,
                      declarations, "# References", refs, supp]) + "\n"
MASTER.write_text(master, encoding="utf-8")

# body word count (sections 1-5 only, math/tags stripped roughly)
body = "\n\n".join([intro, methods, results, discussion, conclusion])
body = re.sub(r"!\[.*?\]\(.*?\)\{.*?\}", "", body, flags=re.DOTALL)
body = re.sub(r"^\|.*\|$", "", body, flags=re.MULTILINE)
body = re.sub(r"\$.*?\$", "EQ", body)
print("Body word count (sections 1-5, incl. embedded captions/tables removed):", len(body.split()))

cmd = ["pandoc", str(MASTER), "-f", "markdown+tex_math_dollars", "-t", "docx",
       "-o", str(DOCX), "--resource-path", str(FIG)]
r = subprocess.run(cmd, capture_output=True, text=True)
print("pandoc rc:", r.returncode)
if r.stderr: print("pandoc stderr:", r.stderr[:2000])
print("wrote:", DOCX)
