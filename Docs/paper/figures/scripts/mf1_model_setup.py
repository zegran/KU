"""MF1 - FEA model setup composite from existing thesis screenshots
(image8 geometry+mesh, image11 loads/BC/RP, image13 mesh detail) with
clean vector panel labels. Author-approved: work from existing PNGs.
"""
import os, matplotlib.pyplot as plt
from fig_data import apply_style, W2

apply_style()
HERE = os.path.dirname(__file__)
MEDIA = os.path.join(HERE, "..", "..", "..", "media", "media")
OUT = os.path.join(HERE, "..")

panels = [
    ("image8.png",  "(a) Half-symmetric model, mesh & global axes"),
    ("image11.png", "(b) Internal pressure, end-cap force & BC (RP-1)"),
    ("image13.png", "(c) Structured quad mesh detail at ripple"),
]
fig, axs = plt.subplots(3, 1, figsize=(W2*0.62, 18.0/2.54))
for ax, (img, title) in zip(axs, panels):
    arr = plt.imread(os.path.join(MEDIA, img))
    ax.imshow(arr)
    ax.set_title(title, fontsize=8, loc="left")
    ax.axis("off")
fig.tight_layout(h_pad=0.6)
for ext in ("pdf", "png"):
    fig.savefig(os.path.join(OUT, f"mf1_model_setup.{ext}"))
print("saved mf1_model_setup")
