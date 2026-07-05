<!--
WP5b Results draft. Drafted under WP0d rewrite SOP (paraphrase).
Citation numbers [n] FINAL (WP6b). Fig.4=MF4, Fig.5=MF5, Fig.6=MF6.
Tables (WP6a renumbering): Table 1 = parametric, Table 4 = threshold/spectrum, S1-S3 supplementary.
IPC deviation signs follow the IPC2002 formula directly (corrects thesis L955 prose;
see logs/2026-06-02-09). Anchor critical-threshold curve (Fig.7/MF7) is in Discussion.
-->

# 3. Results

## 3.1 Parametric stress concentration and the diameter effect

Across the full parametric family the pressure-based stress concentration factor ranged from 1.42 to 2.37 (Fig. 4a, Table 1). Two trends stand out. First, the circumferential extent $\theta$ was the dominant driver: cases with $\theta = 90^\circ$ stayed between 1.42 and 1.89, whereas widening the ripple to $\theta = 180^\circ$ raised $\mathrm{SCF}_P$ to 1.51–2.37. The maximum throughout was the D7 configuration ($\theta = 180^\circ$, largest $d/D$, smallest $L/d$), and the minima were the shallow narrow cases (D1, D6). Depth $d/D$ acted as the second-order driver, with the wavelength ratio $L/d$ weaker still.

Second, $\mathrm{SCF}_P$ depended systematically on diameter even though the diameter-to-thickness ratio was held constant at 73.1. The diameter-averaged factor fell from 1.89 at 36 in to 1.78 at 48 in and 1.68 at 56 in—a smaller pipe consistently produced a higher concentration for the same normalised ripple, in every one of the nine array configurations. Because $D/t$ was held constant, this residual dependence cannot be captured by any correlation that enters geometry only through the diameter-to-thickness ratio: at the scales now common in transmission service, absolute diameter acts as an independent variable.

## 3.2 Benchmark against the existing acceptance correlation

Comparing every analysis against the acceptance correlation of Rosenfeld et al. [4] (Eq. 5) reveals a systematic, extent-dependent departure rather than random scatter (Fig. 4b,c). The sign and magnitude of the departure track the circumferential extent directly. For narrow ripples ($a/C = 0.25$) the correlation over-predicts the FEA result by 31–84%, the over-prediction growing as the diameter decreases. For wide ripples ($a/C = 0.50$) the correlation instead under-predicts, and severely so, by 48% up to more than 400%, with the intermediate $a/C = 0.375$ cases spanning the transition.

The cause lies in the $(a/C)^{-2.87}$ term of the correlation. A large negative exponent forces the predicted SCF to fall steeply as the ripple widens, so that the multiplier drops from about 53 at $a/C = 0.25$ to about 7 at $a/C = 0.50$. The finite element results show the opposite physical tendency: a wider ripple engages more of the circumference and is more severe, not less. The empirical fit of Section 3.4 confirms this, returning an $a/C$ exponent of only $+0.065$—weakly positive—against the correlation's $-2.87$. A circumferential-extent dependence fitted at smaller diameters therefore does not carry over to the large-diameter, high-strength regime examined here.

## 3.3 Wavelength sensitivity

Because $\theta$ and $L/d$ are partially confounded in the L9 array, the wavelength effect was isolated by controlled sweeps at fixed $\theta$ and $d/D$ (Table S1). The response was both stronger than the reference correlation implies and diameter-dependent. For the 36 in pipe, increasing $L/d$ from 6 to 12 lowered $\mathrm{SCF}_P$ by 13.8% (2.17 to 1.87), roughly nine times the change implied by the correlation's wavelength exponent. The 48 in pipe showed a similar but milder reduction of 8.6%. The 56 in pipe, at $\theta = 90^\circ$ and low $d/t$, reversed the trend with a slight 2.3% rise. This interaction between wavelength and scale is a further indication that a single fixed-exponent correlation cannot represent the full geometry space.

## 3.4 Empirical large-diameter SCF correlation

The 38 finite element points were fitted with ordinary least squares in log space (Eq. 6b), which linearises the assumed power-law form and admits a closed-form solution [26]. The result is the correlation of Eq. 6,
$$\mathrm{SCF}_P = 142.1\,(d/D)^{0.938}\,(d/t)^{-0.676}\,(L/d)^{-0.167}\,(a/C)^{0.065},$$
valid for $D/t = 73.1$ and API 5L X70. The fit is accurate over the whole parametric domain: the coefficient of determination is $R^2 = 0.916$, the root-mean-square error is 0.058 SCF units—about 3% of the mean—and no point departs from the prediction by more than 9% (Fig. 5). The residuals are symmetric about the line of perfect agreement, with no systematic bias.

The exponents make the parameter hierarchy explicit. Depth carries the largest positive exponent ($+0.938$), the wall-thickness ratio moderates it ($-0.676$), and the wavelength term is weak ($-0.167$). The circumferential exponent is only $+0.065$, small but positive, and is the quantitative form of the extent-dependent departure discussed in Section 3.2. Within its stated envelope the correlation provides a self-contained acceptance basis for large-diameter pipe; its extension to other $D/t$ ratios requires further analyses and is noted as future work.

## 3.5 Pressure-cycle fatigue damage

Translating the elastic SCF into life through the Markl–Miner framework (Section 2.5) exposes the fifth-power sensitivity of damage to stress amplitude (Table S3). Lowering a cycle from 100% to 50% of MAOP multiplies its allowable count by $2^5 = 32$, and a single full-pressure cycle can produce as much damage as millions of small ones. For a single full-MAOP cycle the worst-case D7 configuration gave allowable counts of 396, 249 and 149 at 56, 48 and 36 in respectively (Table S2); at 56 in this corresponds to a unit damage of $2.5\times10^{-3}$, so only about four full cycles per year would exhaust a 100-year design life.

Realistic operation, however, mixes amplitudes. A representative transmission spectrum—two full-MAOP, 24 high (80%), 52 moderate (50%) and 200 small (5%) cycles per year—applied to the 56 in D7 case ($\mathrm{SCF}_P = 1.95$) gives an annual damage of $2.90\times10^{-2}$ and an estimated life of about 34 years (Table 4, Fig. 6). The damage is not dominated by the largest cycles. The 80%-MAOP band alone contributes 68.6% of the annual total, against 17.4% from the two full-MAOP cycles and 14.2% from the moderate band; the 200 small cycles contribute essentially nothing. The most damaging group is therefore neither the largest in amplitude nor the most numerous, but the moderately large cycles that recur often—a finding that ties ripple severity to the operating pressure spectrum, not to the SCF alone. The threshold this implies for fitness-for-service decisions is developed in Section 4.

<!--
DRAFT NOTES (WP6a):
- ~1550 words target; this draft ~720 content-words (~1100 readable) — slightly under, can expand 3.4/3.5 if needed.
- 36" mean 1.89 used (tabulated-consistent); thesis text says 1.96 — resolve in WP6a.
- IPC deviation signs/values computed from Eq.5 directly (a/C=0.25: -31..-84%; a/C=0.50: +48..+437%) — CORRECTS thesis L955.
- Anchor critical SCF threshold curve (Fig.7/MF7) deliberately deferred to Discussion (Section 4).
- Citations FINAL (WP6b): [4] Rosenfeld, [26] Montgomery (OLS).
-->
