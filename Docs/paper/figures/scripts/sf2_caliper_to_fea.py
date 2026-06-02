"""SF2 - Caliper geometry-ILI radius map -> FEA parameters (own schematic,
no third-party caliper image; copyright-safe synthetic illustration)."""
import os, numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from fig_data import apply_style, W2, GREY

apply_style()
OUT = os.path.join(os.path.dirname(__file__), "..")
fig, (axm, axf) = plt.subplots(1, 2, figsize=(W2, 6.4/2.54),
                               gridspec_kw={"width_ratios": [1.6, 1]})

# synthetic radius-map: axial z vs clock position, ripple bands
z = np.linspace(0, 6, 400)            # m along axis
clock = np.linspace(0, 12, 200)       # o'clock
Z, C = np.meshgrid(z, clock)
# nominal + localized ripple (alternating crest/trough) around 6 o'clock
ripple = 1.2*np.exp(-((Z-3)/0.45)**2) * np.sin(2*np.pi*(Z-3)/0.6) \
         * np.exp(-((C-6)/2.2)**2)
im = axm.pcolormesh(Z, C, ripple, cmap="RdBu_r", shading="auto",
                    vmin=-1.2, vmax=1.2)
axm.set_xlabel("Axial distance (m)"); axm.set_ylabel("Circumferential (o'clock)")
axm.set_yticks([0, 3, 6, 9, 12])
axm.set_title("(a) Geometry-ILI radius map (schematic)", fontsize=8)
cb = fig.colorbar(im, ax=axm, fraction=0.046, pad=0.02)
cb.set_label("Radial deviation (norm.)", fontsize=7)
axm.annotate("ripple band", xy=(3, 6), xytext=(4.3, 9.5), fontsize=7,
             color="k", arrowprops=dict(arrowstyle="->", lw=0.8))

# FEA parameter extraction box
axf.axis("off")
axf.set_title("(b) Extracted FEA parameters", fontsize=8)
items = [r"$L$  wavelength (axial spacing)",
         r"$d$  crest$-$trough depth",
         r"$\theta$ / (a/C)  circumferential extent",
         r"axial location",
         r"$\rightarrow$ representative shell model"]
for i, t in enumerate(items):
    axf.text(0.02, 0.85-0.17*i, t, fontsize=8, va="center")
    if i < 4:
        axf.plot(-0.02, 0.85-0.17*i, ">", color=GREY, ms=5, clip_on=False)
axf.set_xlim(0, 1); axf.set_ylim(0, 1)

fig.tight_layout()
for ext in ("pdf", "png"):
    fig.savefig(os.path.join(OUT, f"sf2_caliper_to_fea.{ext}"))
print("saved sf2_caliper_to_fea")
