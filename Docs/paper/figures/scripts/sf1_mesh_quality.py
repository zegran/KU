"""SF1 - Mesh quality / aspect-ratio detail (image12, Sekil 3.4)."""
import os, matplotlib.pyplot as plt
from fig_data import apply_style, W1

apply_style()
HERE = os.path.dirname(__file__)
MEDIA = os.path.join(HERE, "..", "..", "..", "media", "media")
OUT = os.path.join(HERE, "..")

fig, ax = plt.subplots(figsize=(W1*1.5, 7.0/2.54))
ax.imshow(plt.imread(os.path.join(MEDIA, "image12.png")))
ax.axis("off")
ax.set_title("Mesh quality: structured quad, aspect ratio $\\leq$ 3", fontsize=8, loc="left")
fig.tight_layout()
for ext in ("pdf", "png"):
    fig.savefig(os.path.join(OUT, f"sf1_mesh_quality.{ext}"))
print("saved sf1_mesh_quality")
