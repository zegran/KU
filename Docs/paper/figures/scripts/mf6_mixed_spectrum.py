"""MF6 - Mixed-spectrum fatigue damage distribution (Tablo 3.12).
56" D7 (SCF=1.95): the 80%-MAOP band dominates (68.6% of annual damage).
"""
import os, numpy as np, matplotlib.pyplot as plt
from fig_data import apply_style, MIXED_SPECTRUM, W1

apply_style()
OUT = os.path.join(os.path.dirname(__file__), "..")

labels = [m[0] for m in MIXED_SPECTRUM]
dmg = [m[3] for m in MIXED_SPECTRUM]
ncyc = [m[2] for m in MIXED_SPECTRUM]
y = np.arange(len(labels))[::-1]
colors = ["#b8860b", "#7a1f2b", "#1b3a6b", "#888888"]

fig, ax = plt.subplots(figsize=(W1*1.5, 6.0/2.54))
bars = ax.barh(y, dmg, color=colors, edgecolor="k", linewidth=0.5)
for yi, d, n in zip(y, dmg, ncyc):
    ax.text(d + 1.5, yi, f"{d:.1f}%  (n={n}/yr)", va="center", fontsize=7.5)
ax.set_yticks(y); ax.set_yticklabels(labels)
ax.set_xlabel("Contribution to annual fatigue damage [%]")
ax.set_xlim(0, 82)
ax.set_title("56\" D7 (SCF$_P$=1.95): $D_{yr}$=2.90$\\times$10$^{-2}$, $T_{est}\\approx$34 yr",
             fontsize=7.8)
fig.tight_layout()
for ext in ("pdf", "png"):
    fig.savefig(os.path.join(OUT, f"mf6_mixed_spectrum.{ext}"))
print("saved mf6_mixed_spectrum")
