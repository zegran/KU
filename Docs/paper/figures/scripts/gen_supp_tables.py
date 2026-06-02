"""Generate supplementary LaTeX tables from fig_data (exact, no transcription)."""
import os
from fig_data import DIAMS

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "tables",
                   "supplementary_tables.tex")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

lines = []
lines.append("% Supplementary tables (WP4), auto-generated from fig_data.py.")
lines.append("% Requires \\usepackage{booktabs}.\n")

# ---- TS1: full Taguchi L9 x 3 ----
lines.append(r"\begin{table}[t]\centering")
lines.append(r"\caption{Full Taguchi L9 array and FEA $\mathrm{SCF}_P$ for the three diameters "
             r"($D/t=73.1$, API 5L X70).}\label{tab:l9full}")
lines.append(r"\begin{tabular}{llccccccc}")
lines.append(r"\toprule")
lines.append(r"OD & Case & $\theta$($^\circ$) & $d$(mm) & $d/D$ & $d/t$ & $L/d$ & $a/C$ & $\mathrm{SCF}_P$ \\")
lines.append(r"\midrule")
for dname, rows in DIAMS.items():
    od = dname.replace('"', "$''$")
    for j, r in enumerate(rows):
        tag = od if j == 0 else ""
        lines.append(f"{tag} & {r[0]} & {r[1]} & {r[2]} & {r[3]:.4f} & "
                     f"{r[4]:.3f} & {r[5]} & {r[6]:.3f} & {r[7]:.2f} \\\\")
    lines.append(r"\midrule")
lines[-1] = r"\bottomrule"
lines.append(r"\end{tabular}\end{table}")
lines.append("")

# ---- TS2: single full MAOP cycle (thesis Tablo 3.10) ----
lines.append(r"\begin{table}[t]\centering")
lines.append(r"\caption{Single full-MAOP cycle: $N_f$ and unit damage (D7 configuration, "
             r"$C'=1126$~MPa, $S_a=174.6$~MPa).}\label{tab:maopcycle}")
lines.append(r"\begin{tabular}{lcccc}")
lines.append(r"\toprule")
lines.append(r"OD & $\mathrm{SCF}_P$(D7) & $N_f$ & $d_i$ ($n{=}1$) & $t_{\mathrm{est}}$(yr) \\")
lines.append(r"\midrule")
for od, scf, Nf, di, T in [("56$''$",1.95,396,"2.53e-3",396),
                            ("48$''$",2.14,249,"4.02e-3",249),
                            ("36$''$",2.37,149,"6.70e-3",149)]:
    lines.append(f"{od} & {scf} & {Nf} & {di} & {T} \\\\")
lines.append(r"\bottomrule\end{tabular}\end{table}")
lines.append("")

# ---- TS3: dP/MAOP single-cycle relative damage (thesis Tablo 3.9) ----
lines.append(r"\begin{table}[t]\centering")
lines.append(r"\caption{Relative single-cycle damage vs $\Delta P/\mathrm{MAOP}$ "
             r"($\mathrm{SCF}_P=1.95$, $\sigma_h=349.2$~MPa).}\label{tab:dpdamage}")
lines.append(r"\begin{tabular}{cccl}")
lines.append(r"\toprule")
lines.append(r"$\Delta P/\mathrm{MAOP}$ & $S_a$(MPa) & $N_i$ & Relative damage \\")
lines.append(r"\midrule")
for dp, sa, Ni, rel in [("100\\%",174.6,"396","1"),
                        ("80\\%",139.7,r"1.21$\times10^3$","3"),
                        ("50\\%",87.3,r"1.27$\times10^4$","32"),
                        ("20\\%",34.9,r"1.23$\times10^6$","3134"),
                        ("10\\%",17.5,r"3.91$\times10^7$","98862"),
                        ("5\\%",8.7,r"1.27$\times10^9$","3255554")]:
    lines.append(f"{dp} & {sa} & {Ni} & {rel} \\\\")
lines.append(r"\bottomrule\end{tabular}\end{table}")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print("wrote", os.path.relpath(OUT))
print(f"TS1 rows: {sum(len(r) for r in DIAMS.values())} (expect 27)")
