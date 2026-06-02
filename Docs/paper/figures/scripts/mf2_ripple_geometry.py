"""MF2 - Ripple geometry parameter definition (autonomous schematic)."""
import os, numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Wedge, Circle
from fig_data import apply_style, W2, GREY, DT_RATIO, MAOP

apply_style()
OUT = os.path.join(os.path.dirname(__file__), "..")
fig, (axL, axR) = plt.subplots(1, 2, figsize=(W2, 6.6/2.54),
                               gridspec_kw={"width_ratios": [2.1, 1]})

# ---------- (a) longitudinal ripple profile ----------
z = np.linspace(-300, 300, 600)
L = 240.0
d = 60.0  # exaggerated for clarity
env = np.exp(-(z/110.0)**2)               # localized envelope
w = d/2 * np.sin(2*np.pi*z/L) * env       # single trough-crest half-wave
axL.plot(z, w, color="#1b3a6b", lw=2.0)
axL.axhline(0, color=GREY, lw=0.8, ls="--")
axL.text(300, 4, "nominal wall", ha="right", fontsize=7, color=GREY)

# crest-to-trough depth d
zc = z[np.argmax(w)]; zt = z[np.argmin(w)]
axL.annotate("", xy=(zc, w.max()), xytext=(zc, w.min()),
             arrowprops=dict(arrowstyle="<->", color="#7a1f2b", lw=1.3))
axL.text(zc+16, 14, "$d$ (crest$-$trough)", color="#7a1f2b", fontsize=8, va="center")

# wavelength L
axL.annotate("", xy=(zt, -d/2-10), xytext=(zc, -d/2-10),
             arrowprops=dict(arrowstyle="<->", color=GREY, lw=1.1))
axL.text((zc+zt)/2, -d/2-16, "$L/2$", ha="center", va="top", fontsize=8, color=GREY)

axL.set_xlabel("Axial position, $z$ (mm)")
axL.set_ylabel("Radial deviation (mm)")
axL.set_title("(a) Longitudinal ripple profile (raised-cosine)", fontsize=8)
axL.set_ylim(-d, d)

# ---------- (b) cross-section circumferential extent ----------
axR.set_aspect("equal"); axR.axis("off")
R = 1.0
axR.add_patch(Circle((0, 0), R, fill=False, ec=GREY, lw=1.6))
# ripple arc over angle theta (centered at top)
theta = 180.0
w_arc = Wedge((0, 0), R, 90-theta/2, 90+theta/2, width=0.10,
              fc="#7a1f2b", ec="k", lw=0.4)
axR.add_patch(w_arc)
axR.annotate("", xy=(R*np.cos(np.radians(90+theta/2)), R*np.sin(np.radians(90+theta/2))),
             xytext=(R*np.cos(np.radians(90-theta/2)), R*np.sin(np.radians(90-theta/2))),
             arrowprops=dict(arrowstyle="<->", color="#7a1f2b", lw=1.2,
                             connectionstyle="arc3,rad=0.3"))
axR.text(0, 1.28, r"$\theta$  (a/C)", ha="center", fontsize=8, color="#7a1f2b")
axR.plot([0, 0], [0, R], color=GREY, lw=0.8, ls=":")
axR.text(0.06, 0.5, "$R$", fontsize=8, color=GREY)
axR.set_title("(b) Circumferential extent", fontsize=8)
axR.set_xlim(-1.4, 1.4); axR.set_ylim(-1.3, 1.5)

# parameter box
txt = (f"$D/t$ = {DT_RATIO:.1f} (constant)\nAPI 5L X70\n"
       f"$P$ = {MAOP} MPa (MAOP)\n$a/C$ = 0.25 / 0.375 / 0.50\n"
       r"$\theta$ = 90$\degree$ / 135$\degree$ / 180$\degree$")
axR.text(-1.35, -1.25, txt, fontsize=6.8, va="top",
         bbox=dict(boxstyle="round", fc="white", ec="grey", lw=0.6))

fig.tight_layout()
for ext in ("pdf", "png"):
    fig.savefig(os.path.join(OUT, f"mf2_ripple_geometry.{ext}"))
print("saved mf2_ripple_geometry")
