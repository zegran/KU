"""SF3 - Full stress-component contour set at the ripple
(image15 Von Mises, image16 S11 circ., image17 S22 axial)."""
import os, matplotlib.pyplot as plt
from fig_data import apply_style, W2

apply_style()
HERE = os.path.dirname(__file__)
MEDIA = os.path.join(HERE, "..", "..", "..", "media", "media")
OUT = os.path.join(HERE, "..")

panels = [
    ("image15.png", "(a) von Mises"),
    ("image16.png", "(b) S11 (circumferential)"),
    ("image17.png", "(c) S22 (axial)"),
]
fig, axs = plt.subplots(3, 1, figsize=(W2*0.7, 16.0/2.54))
for ax, (img, title) in zip(axs, panels):
    arr = plt.imread(os.path.join(MEDIA, img))
    h = arr.shape[0]
    ax.imshow(arr[: int(0.84 * h)])
    ax.axis("off")
    ax.set_title(title, fontsize=8, loc="left")
fig.tight_layout(h_pad=0.5)
for ext in ("pdf", "png"):
    fig.savefig(os.path.join(OUT, f"sf3_stress_contours.{ext}"))
print("saved sf3_stress_contours")
