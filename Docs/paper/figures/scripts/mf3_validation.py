"""MF3 - Validation vs the benchmark of Rosenfeld et al. (2002).
(a) S11 stress contour at ripple (image16, footer cropped)
(b) stress comparison bar (Tablo 3.4) + end-cap/SCF notes.
WP6 Faz 5: values updated to thesis v2 (fine mesh 718.6 MPa; SCF 3.25).
"""
import os, numpy as np, matplotlib.pyplot as plt
from fig_data import apply_style, W2, PALETTE

apply_style()
HERE = os.path.dirname(__file__)
MEDIA = os.path.join(HERE, "..", "..", "..", "media", "media")
OUT = os.path.join(HERE, "..")

fig = plt.figure(figsize=(W2, 7.2/2.54))
gs = fig.add_gridspec(1, 2, width_ratios=[1.5, 1])

# (a) S11 contour, crop bottom footer text
axa = fig.add_subplot(gs[0])
arr = plt.imread(os.path.join(MEDIA, "image16.png"))
h = arr.shape[0]
axa.imshow(arr[: int(0.82 * h)])
axa.axis("off")
axa.set_title("(a) S11 (hoop) contour at ripple, SPOS", fontsize=8, loc="left")

# (b) Tablo 3.4 comparison bars
axb = fig.add_subplot(gs[1])
comp = ["von Mises", "S11 (circ.)", "S22 (long.)"]
ref = [784.0, 759.9, 806.8]      # Rosenfeld et al.
this = [718.6, 796.8, 755.9]     # this work (thesis v2, fine mesh)
dev = [-8.3, 4.9, -6.3]
x = np.arange(len(comp)); w = 0.38
axb.bar(x - w/2, ref, w, color="#888888", edgecolor="k", linewidth=0.4, label="Rosenfeld (2002)")
axb.bar(x + w/2, this, w, color=PALETTE["56\""], edgecolor="k", linewidth=0.4, label="This work")
for xi, dv, yv in zip(x, dev, this):
    axb.text(xi + w/2, yv + 12, f"{dv:+.1f}%", ha="center", fontsize=6.8)
axb.set_xticks(x); axb.set_xticklabels(comp, rotation=20, fontsize=7)
axb.set_ylabel("Peak stress (MPa)")
axb.set_ylim(0, 1020)
axb.set_title("(b) Benchmark vs Rosenfeld et al. (2002)", fontsize=8)
axb.legend(fontsize=6.8, loc="upper center", ncol=2, columnspacing=1.0)
axb.text(-0.4, 70,
         "End-cap force: 0.013%\nNominal hoop: 220.8 MPa (analytic)\nSCF: 3.25 vs 3.55",
         fontsize=6.5, va="bottom",
         bbox=dict(boxstyle="round", fc="white", ec="grey", lw=0.6))

fig.tight_layout()
for ext in ("pdf", "png"):
    fig.savefig(os.path.join(OUT, f"mf3_validation.{ext}"))
print("saved mf3_validation")
