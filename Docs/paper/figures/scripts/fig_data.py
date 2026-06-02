"""Shared data + style for IJPVP paper figures (WP3b).

All numerical values transcribed verbatim from the thesis
(Docs/KUnal_tez_org_tr.md). No fabricated data.
"""
from __future__ import annotations
import numpy as np
import matplotlib as mpl

# ---------------------------------------------------------------- constants
C_PRIME = 1126.0      # MPa, load-controlled Markl coefficient (IPC2002-27124), thesis L1063
SIGMA_HOOP = 349.2    # MPa, nominal hoop stress at MAOP, thesis L855
S_AMP_MAOP = SIGMA_HOOP / 2.0   # 174.6 MPa, amplitude at full MAOP, thesis L1058/L1104
MAOP = 9.55           # MPa, thesis L855
DT_RATIO = 73.1       # constant D/t, thesis L855

# ---------------------------------------------------------------- L9 x 3 data (27 pts)
# columns: exp, theta(deg), d(mm), d_over_D, d_over_t, L_over_d, a_over_C, SCF_FEA
L9_56 = [  # Tablo 3.6 (56" OD=1422.4 mm)
    ("D1", 90, 18, 0.0127, 0.925, 10,   0.25, 1.42),
    ("D2", 90, 24, 0.0169, 1.234, 10,   0.25, 1.70),
    ("D3", 90, 30, 0.0211, 1.542, 12,   0.25, 1.78),
    ("D4", 135, 24, 0.0169, 1.234, 7.5,  0.375, 1.74),
    ("D5", 135, 30, 0.0211, 1.542, 8,    0.375, 1.91),
    ("D6", 135, 18, 0.0127, 0.925, 20,   0.375, 1.45),
    ("D7", 180, 30, 0.0211, 1.542, 6,    0.500, 1.95),
    ("D8", 180, 18, 0.0127, 0.925, 13.3, 0.500, 1.51),
    ("D9", 180, 24, 0.0169, 1.234, 15,   0.500, 1.63),
]
L9_48 = [  # Tablo 3.7 (48" OD=1219.2 mm)
    ("D1", 90, 18, 0.0148, 1.080, 10,   0.25, 1.60),
    ("D2", 90, 24, 0.0197, 1.440, 10,   0.25, 1.77),
    ("D3", 90, 30, 0.0246, 1.800, 12,   0.25, 1.86),
    ("D4", 135, 24, 0.0197, 1.440, 7.5,  0.375, 1.87),
    ("D5", 135, 30, 0.0246, 1.800, 8,    0.375, 2.00),
    ("D6", 135, 18, 0.0148, 1.080, 20,   0.375, 1.50),
    ("D7", 180, 30, 0.0246, 1.800, 6,    0.500, 2.14),
    ("D8", 180, 18, 0.0148, 1.080, 13.3, 0.500, 1.61),
    ("D9", 180, 24, 0.0197, 1.440, 15,   0.500, 1.67),
]
L9_36 = [  # Tablo 3.8 (36" OD=914.4 mm)
    ("D1", 90, 18, 0.0197, 1.440, 10,   0.25, 1.72),
    ("D2", 90, 24, 0.0262, 1.920, 10,   0.25, 1.85),
    ("D3", 90, 30, 0.0328, 2.400, 12,   0.25, 1.89),
    ("D4", 135, 24, 0.0262, 1.920, 7.5,  0.375, 2.06),
    ("D5", 135, 30, 0.0328, 2.400, 8,    0.375, 2.10),
    ("D6", 135, 18, 0.0197, 1.440, 20,   0.375, 1.52),
    ("D7", 180, 30, 0.0328, 2.400, 6,    0.500, 2.37),
    ("D8", 180, 18, 0.0197, 1.440, 13.3, 0.500, 1.80),
    ("D9", 180, 24, 0.0262, 1.920, 15,   0.500, 1.72),
]
DIAMS = {"36\"": L9_36, "48\"": L9_48, "56\"": L9_56}

# ---------------------------------------------------------------- formulas
def ld_scf(dD, dt, Ld, aC):
    """Thesis LD-SCF regression, Eq. 3.10 (R2=0.916)."""
    return 142.1 * dD**0.938 * dt**-0.676 * Ld**-0.167 * aC**0.065

def ipc_scf(DtR, dD, dt, Ld, aC):
    """Rosenfeld et al. IPC2002 formula, Eq. 3.8."""
    return 0.122 * DtR**0.815 * dD**1.06 * dt**0.783 * Ld**0.014 * aC**-2.87

def life_years(scf, n_cycles, c_prime=C_PRIME, s_amp=S_AMP_MAOP):
    """Estimated fatigue life (yr) = N_f / n,  N_f = (C'/(SCF*S_amp))^5."""
    Nf = (c_prime / (scf * s_amp))**5
    return Nf / n_cycles

def scf_crit(n_cycles, T_design, c_prime=C_PRIME, s_amp=S_AMP_MAOP):
    """Closed-form critical SCF: C'/(S_amp*(n*T)^0.2)."""
    return c_prime / (s_amp * (n_cycles * T_design)**0.2)

# ---------------------------------------------------------------- mixed spectrum (Tablo 3.12)
MIXED_SPECTRUM = [  # (label, dP/MAOP %, n_i/yr, damage %)
    ("Full MAOP",  100, 2,   17.4),
    ("High (80%)",  80, 24,  68.6),
    ("Mid (50%)",   50, 52,  14.2),
    ("Small (5%)",   5, 200,  0.0),
]

# ---------------------------------------------------------------- style
GREY = "#3a3a3a"
PALETTE = {"36\"": "#1b3a6b", "48\"": "#b8860b", "56\"": "#7a1f2b"}  # cb-safe, distinct
MARKERS = {"36\"": "o", "48\"": "s", "56\"": "^"}
LINES = {"36\"": "-", "48\"": "--", "56\"": ":"}

def apply_style():
    mpl.rcParams.update({
        "figure.dpi": 120,
        "savefig.dpi": 600,
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Arial"],
        "font.size": 8.5,
        "axes.titlesize": 9,
        "axes.labelsize": 9,
        "legend.fontsize": 7.5,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "axes.linewidth": 0.8,
        "lines.linewidth": 1.4,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "grid.linewidth": 0.5,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "pdf.fonttype": 42,  # editable text in PDF
    })

CM = 1 / 2.54
W1 = 9.0 * CM    # single column ~90 mm
W2 = 19.0 * CM   # double column ~190 mm
