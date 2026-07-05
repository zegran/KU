<!--
WP5c Discussion draft. Drafted under WP0d rewrite SOP (paraphrase).
Citation numbers [n] PROVISIONAL (WP6b). Fig.7 = MF7 anchor master curve.
Eq.10 = closed-form SCF_crit. This section is the paper's climax (anchor claim).
-->

# 4. Discussion

## 4.1 A critical SCF threshold for fitness-for-service

The practical value of coupling the parametric SCF to the Markl–Miner chain is that it produces a single, operationally meaningful decision quantity: the stress concentration above which a ripple cannot meet the design life. Setting the cumulative damage to its limit, $D_m = nT/N_f = 1$, and substituting the load-controlled endurance relation (Eqs. 7–8) gives a closed form for this critical factor,
$$\mathrm{SCF}_{\text{crit}} = \frac{C'}{S_a\,(nT)^{0.2}} \quad\text{(Eq. 10)},$$
where $n$ is the number of full-MAOP-equivalent cycles per year and $T$ the design life. For a representative duty of $n = 12$ cycles/yr over $T = 100$ years, Eq. 10 returns $\mathrm{SCF}_{\text{crit}} \approx 1.57$. This is consistent with the discrete sensitivity analysis, in which configurations below $\mathrm{SCF}_P = 1.51$ remain safe while those at or above 1.65 fail the design life.

Figure 7 generalises the single threshold into a master curve. Plotting estimated life against $\mathrm{SCF}_P$ for a family of cycle counts ($n = 4$ to 24/yr), with the design-life line superimposed, turns Eq. 10 into a direct read-off: for any operating intensity, the intersection gives the admissible SCF, and the parametric cases fall on the curve at their computed factors. An operator with an ILI-measured ripple can therefore estimate $\mathrm{SCF}_P$ from the correlation of Eq. 6, locate the pipe on Figure 7 for its own duty cycle, and obtain an immediate accept / analyse / repair decision. This is the quantitative basis that codes such as CSA Z662 and ASME B31.8 permit but do not themselves supply [1,2], and it advances the field practice from "remove any ripple" toward "assess each ripple," in line with the rigorous-analysis route of API 579 [29].

## 4.2 Applicability of the existing correlation at large diameter

The benchmarking of Section 3 shows that the IPC2002 correlation of Rosenfeld et al., although appropriate for the pipe sizes up to 36 in on which it was calibrated, should not be extrapolated to the large-diameter, high-strength line pipe studied here—precisely the comparison the constant $D/t = 73.1$ design was constructed to allow. Two departures appear. First, because the correlation enters geometry only through $D/t$, it cannot represent the residual diameter dependence observed at fixed $D/t$, where the mean SCF rose by 13% from the 56 in to the 36 in pipe. Second, its $(a/C)^{-2.87}$ term runs against the computed trend: it lowers the predicted SCF as the ripple widens, whereas the finite element results—and the weakly positive fitted exponent of $+0.065$—show that a wider ripple is more severe. The consequence is a systematic, sign-changing departure, from over-prediction by up to 84% for narrow ripples to under-prediction exceeding 400% for wide ones. The under-prediction is the direction that matters for integrity, since it would classify a genuinely severe wide ripple as benign. The proposed correlation removes both departures within its stated envelope.

## 4.3 Severity depends on the pressure spectrum, not the SCF alone

A second outcome of the integrated assessment is that the stress concentration is an incomplete index of fatigue severity. For the mixed spectrum considered, the moderately large 80%-MAOP cycles contributed 68.6% of the annual damage—more than the full-MAOP cycles and the moderate band combined—because they pair a substantial amplitude with a high recurrence, while the fifth-power law suppresses the many small cycles to a negligible share. A pipe with a moderate SCF under a high-amplitude duty can therefore be closer to its limit than one with a high SCF under a benign duty. Severity assessment should accordingly combine the elastic SCF with the rainflow-reduced operating spectrum, as done here, rather than rely on the SCF in isolation; this is consistent with spectrum-based pipeline fatigue practice [E1] and with the broader move toward operationally grounded fitness-for-service evaluation of geometric anomalies [F4].

## 4.4 Validity envelope and limitations

Several boundaries delimit the present results. The empirical correlation (Eq. 6) was derived at a single diameter-to-thickness ratio, $D/t = 73.1$, and for API 5L X70 at MAOP 9.55 MPa; it must not be applied outside this envelope. The ratio was fixed deliberately, as the controlled constant that isolates the diameter effect and keeps the results comparable with smaller-diameter acceptance analyses; repeating the parametric family across a range of $D/t$ values, so that a single generalised regression covers the full geometry space, is the clearest line of future work. The analyses are linear-elastic, which the post-solution yield check justifies for the mild ripples considered, but which would not hold for deeper wrinkles entering the plastic range. The ripple was idealised as a single trough–crest raised-cosine profile; field ripples are often multi-crest, and the ~8% difference in Von Mises stress against the five-crest benchmark of Rosenfeld et al. reflects this and the associated solver and symmetry differences [4]. The fatigue estimates rest on a representative transmission spectrum and a total-life Markl S–N basis; site-specific SCADA pressure records and a separate crack-initiation treatment would refine absolute lives. None of these bounds undermines the threshold framework itself, which is parametric and can be re-derived through Eqs. 6 and 10 for any revised envelope or duty cycle. The assessment chain demonstrated here—inspection-derived geometry, parametric shell finite element analysis, and a spectrum-based Markl–Miner evaluation closed by an explicit threshold—is, moreover, not specific to ripples, and can serve as a template for the fitness-for-service assessment of other geometric surface anomalies in line pipe.

<!--
DRAFT NOTES (WP6a):
- ~1050 words target; this draft ~870 content-words (~1050 readable) — on target.
- Anchor (Fig.7) + closed-form SCF_crit (Eq.10) are the climax; ties Results 3.1/3.2/3.5 together.
- Limitations section explicit (IJPVP requires; pre-empts reviewer on D/t, Von Mises, spectrum).
- Citations provisional: [E1] Kiefner spectrum, [F4] dent-SCF IJPVP, [1][2][4][29] from pool.
- 36" "13%" wording uses tabulated means (1.89/1.68); consistent with WP4/WP5b.
-->
