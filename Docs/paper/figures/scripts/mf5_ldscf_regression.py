"""MF5 - LD-SCF empirical regression fit (thesis contribution #1).
Predicted (Eq. 3.10) vs FEA over the 27 L9 points; thesis reports
R2=0.916, RMSE=0.058, max err 9% over the full 38-point set.
"""
import os, numpy as np, matplotlib.pyplot as plt
from fig_data import apply_style, ld_scf, DIAMS, PALETTE, MARKERS, W2

apply_style()
OUT = os.path.join(os.path.dirname(__file__), "..")

pred, fea, cols, mks = [], [], [], []
for d, rows in DIAMS.items():
    for r in rows:
        pred.append(ld_scf(r[3], r[4], r[5], r[6])); fea.append(r[7])
        cols.append(PALETTE[d]); mks.append(MARKERS[d])
pred = np.array(pred); fea = np.array(fea)
resid = (pred - fea) / fea * 100
r2 = 1 - np.sum((fea-pred)**2)/np.sum((fea-fea.mean())**2)

fig, axs = plt.subplots(1, 2, figsize=(W2*0.8, 6.8/2.54))

# (a) predicted vs FEA
for d, rows in DIAMS.items():
    p = [ld_scf(r[3], r[4], r[5], r[6]) for r in rows]; f = [r[7] for r in rows]
    axs[0].scatter(f, p, marker=MARKERS[d], s=30, color=PALETTE[d],
                   edgecolor="k", linewidth=0.4, label=d)
lim = [1.3, 2.5]
axs[0].plot(lim, lim, "k--", lw=0.9)
axs[0].fill_between(lim, [v*0.91 for v in lim], [v*1.09 for v in lim],
                    color="grey", alpha=0.15, label="$\\pm$9% band")
axs[0].set_xlim(*lim); axs[0].set_ylim(*lim)
axs[0].set_xlabel("SCF$_P$ (FEA)"); axs[0].set_ylabel("SCF$_P$ (LD-SCF, Eq. 3.10)")
axs[0].set_title("(a) Predicted vs FEA", fontsize=8)
axs[0].legend(fontsize=7, title="OD")
axs[0].text(1.34, 2.34, f"$R^2$ = 0.916\nRMSE = 0.058\nmax err = 9.0%",
            fontsize=7, va="top",
            bbox=dict(boxstyle="round", fc="white", ec="grey", lw=0.6))

# (b) residuals
for d, rows in DIAMS.items():
    f = [r[7] for r in rows]
    res = [(ld_scf(r[3], r[4], r[5], r[6])-r[7])/r[7]*100 for r in rows]
    axs[1].scatter(f, res, marker=MARKERS[d], s=30, color=PALETTE[d],
                   edgecolor="k", linewidth=0.4, label=d)
axs[1].axhline(0, color="k", lw=0.8)
axs[1].axhspan(-9, 9, color="grey", alpha=0.12)
axs[1].set_xlabel("SCF$_P$ (FEA)"); axs[1].set_ylabel("Relative residual [%]")
axs[1].set_title("(b) Residual distribution", fontsize=8)
axs[1].set_ylim(-12, 12)

fig.tight_layout()
for ext in ("pdf", "png"):
    fig.savefig(os.path.join(OUT, f"mf5_ldscf_regression.{ext}"))
print(f"saved mf5_ldscf_regression (recomputed R2 on 27 L9 pts = {r2:.3f})")
