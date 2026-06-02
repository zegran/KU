"""MF4 - Parametric SCF: FEA vs IPC2002 across three diameters.
Reproduces thesis Sekil 3.10/3.11/3.12 from the L9 tables.
"""
import os, numpy as np, matplotlib.pyplot as plt
from fig_data import (apply_style, ipc_scf, DT_RATIO, DIAMS, PALETTE, MARKERS, W2)

apply_style()
OUT = os.path.join(os.path.dirname(__file__), "..")
fig, axs = plt.subplots(1, 3, figsize=(W2, 6.4/2.54))

# panel (a): grouped bars of FEA SCF per config
labels = [r[0] for r in DIAMS["56\""]]
x = np.arange(len(labels)); w = 0.26
for i, (d, rows) in enumerate(DIAMS.items()):
    axs[0].bar(x + (i-1)*w, [r[7] for r in rows], w, color=PALETTE[d],
               edgecolor="k", linewidth=0.4, label=d)
axs[0].set_xticks(x); axs[0].set_xticklabels(labels, rotation=45, fontsize=6.5)
axs[0].set_ylabel("SCF$_P$ (FEA)"); axs[0].set_xlabel("Taguchi L9 case")
axs[0].set_title("(a) Parametric FEA SCF$_P$", fontsize=8)
axs[0].legend(fontsize=7, title="OD")
axs[0].set_ylim(0, 2.6)

# panel (b): FEA vs IPC 45-deg scatter, colored by a/C
for d, rows in DIAMS.items():
    fea = [r[7] for r in rows]
    ipc = [ipc_scf(DT_RATIO, r[3], r[4], r[5], r[6]) for r in rows]
    axs[1].scatter(ipc, fea, marker=MARKERS[d], s=28, color=PALETTE[d],
                   edgecolor="k", linewidth=0.4, label=d)
lim = [0.5, 4.5]
axs[1].plot(lim, lim, "k--", lw=0.9, label="45$\\degree$ (FEA=IPC)")
axs[1].set_xlim(*lim); axs[1].set_ylim(1.2, 2.6)
axs[1].set_xlabel("SCF$_P$ (IPC2002, Eq. 3.8)"); axs[1].set_ylabel("SCF$_P$ (FEA)")
axs[1].set_title("(b) FEA vs IPC2002", fontsize=8)
axs[1].legend(fontsize=6.8)

# panel (c): deviation % = (FEA-IPC)/IPC*100
for d, rows in DIAMS.items():
    dev = [(r[7]-ipc_scf(DT_RATIO, r[3], r[4], r[5], r[6])) /
           ipc_scf(DT_RATIO, r[3], r[4], r[5], r[6])*100 for r in rows]
    aC = [r[6] for r in rows]
    axs[2].scatter(aC, dev, marker=MARKERS[d], s=28, color=PALETTE[d],
                   edgecolor="k", linewidth=0.4, label=d)
axs[2].axhline(0, color="k", lw=0.8)
axs[2].set_xlabel("Circumferential extent, a/C"); axs[2].set_ylabel("Deviation (FEA$-$IPC)/IPC  [%]")
axs[2].set_title("(c) IPC2002 deviation", fontsize=8)
axs[2].set_xticks([0.25, 0.375, 0.50])

fig.tight_layout()
for ext in ("pdf", "png"):
    fig.savefig(os.path.join(OUT, f"mf4_parametric_scf.{ext}"))
print("saved mf4_parametric_scf")
