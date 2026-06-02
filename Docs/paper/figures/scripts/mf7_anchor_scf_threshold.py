"""MF7 (anchor F8) - Critical SCF threshold master curve.

Fully closed-form from Markl-Miner; verified against thesis Tablo 3.11.
"""
import os, numpy as np, matplotlib.pyplot as plt
from fig_data import (apply_style, life_years, scf_crit, S_AMP_MAOP, C_PRIME,
                      DIAMS, PALETTE, MARKERS, W2, GREY)

apply_style()
OUT = os.path.join(os.path.dirname(__file__), "..")

# --- verification against Tablo 3.11 (n=12, 100 yr) ---
checks = {1.42: 161, 1.51: 118, 1.65: 76, 1.95: 33, 2.37: 12}
print("MF7 verification vs Tablo 3.11 (T_est, yr @ n=12):")
for scf, ref in checks.items():
    t = life_years(scf, 12)
    print(f"  SCF={scf}: model={t:6.1f}  thesis={ref}")
print(f"  SCF_crit(n=12,T=100) = {scf_crit(12,100):.3f} (thesis band 1.51-1.65)")

# --- figure ---
fig, ax = plt.subplots(figsize=(W2, 8.5/2.54))
scf = np.linspace(1.40, 3.00, 400)
ncyc = [4, 8, 12, 24]
styles = ["-", "--", "-.", ":"]
for n, ls in zip(ncyc, styles):
    ax.plot(scf, life_years(scf, n), ls, color=GREY, lw=1.6,
            label=f"n = {n} MAOP-eq. cyc/yr")
    sc = scf_crit(n, 100)
    ax.plot(sc, 100, "o", color="white", mec=GREY, ms=5, zorder=5)

# design-life line
ax.axhline(100, color="#7a1f2b", lw=1.2, ls=(0, (6, 3)))
ax.text(2.92, 112, "100-yr design life", ha="right", va="bottom",
        fontsize=7.5, color="#7a1f2b")

# safe / critical shading using n=12 curve
ax.axhspan(100, 1e5, color="#2e7d32", alpha=0.05)
ax.axhspan(1e0, 100, color="#7a1f2b", alpha=0.05)
ax.text(1.44, 6e3, "SAFE  (T > design)", fontsize=7.5, color="#2e7d32")
ax.text(1.44, 3, "CRITICAL  (T < design)", fontsize=7.5, color="#7a1f2b")

# overlay 27 FEA configs on n=12 curve
for dname, rows in DIAMS.items():
    xs = [r[7] for r in rows]
    ys = [life_years(r[7], 12) for r in rows]
    ax.scatter(xs, ys, marker=MARKERS[dname], s=26, color=PALETTE[dname],
               edgecolor="k", linewidth=0.4, zorder=6, label=f"FEA {dname} (n=12)")

# critical SCF annotation
scrit12 = scf_crit(12, 100)
ax.axvline(scrit12, color="k", lw=0.8, ls=":")
ax.annotate(f"SCF$_{{crit}}\\approx${scrit12:.2f}\n(n=12, 100 yr)",
            xy=(scrit12, 100), xytext=(1.75, 600),
            fontsize=7.5, ha="left",
            arrowprops=dict(arrowstyle="->", lw=0.7))

ax.set_yscale("log")
ax.set_xlim(1.40, 3.00)
ax.set_ylim(2, 2e4)
ax.set_xlabel("Pressure-based stress concentration factor, SCF$_P$")
ax.set_ylabel("Estimated fatigue life, $T_{est}$ (years)")
ax.legend(loc="upper right", ncol=2, framealpha=0.9, fontsize=6.8)
fig.tight_layout()

for ext in ("pdf", "png"):
    fig.savefig(os.path.join(OUT, f"mf7_anchor_scf_threshold.{ext}"))
print("saved mf7_anchor_scf_threshold.pdf / .png")
