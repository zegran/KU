<!--
WP5a Methods draft (Section A structure: Theory + Model + V&V + Fatigue).
Drafted under WP0d rewrite SOP (paraphrase, not translation).
Citation numbers [n] are PROVISIONAL — finalized in WP6b against WP2 pool.
Figure refs: Fig.1=MF1, Fig.2=MF2, Fig.3=MF3.
Tables (WP6a renumbering, first-citation order): Table 1 = parametric geometries (old T3),
Table 2 = FE model (old T1), Table 3 = validation (old T2), Table 4 = threshold/spectrum (unchanged).
Equations: Eq.(N) = equations.tex E1-E10.
-->

# 2. Materials and methods

## 2.1 Theoretical framework

Under internal pressure, a defect-free thin-walled pipe carries load almost entirely through membrane action. Classical thin-shell theory gives the nominal hoop and longitudinal stresses as $\sigma_h = PR/t$ and $\sigma_L = PR/2t$ (Eq. 1), with no through-thickness bending [1]. A field-bend ripple breaks this idealisation. The periodic crest–trough geometry imposes a local change of wall curvature, so the wall must carry bending in addition to membrane stress. The bending stiffness scales with the flexural rigidity $D_f = Et^3/12(1-\nu^2)$ (Eq. 2), and the peak stress concentrates at the crest and trough, where the curvature gradient is steepest.

The severity of this elevation is measured by the pressure-based stress concentration factor, $\mathrm{SCF}_P = \sigma_{\max,\text{local}}/\sigma_{h,\text{nominal}}$ (Eq. 3): the ratio of the peak local stress to the nominal membrane hoop stress of the equivalent defect-free pipe [8]. Because this elastic factor is the input to the fatigue assessment of Section 2.5, every analysis is kept within the linear-elastic range. The assumption is checked after each solution by confirming that the peak stress stays below the specified minimum yield strength of API 5L X70.

A direct consequence of the membrane–bending coupling is that depth alone does not describe ripple severity. At a fixed normalised depth, increasing the pipe diameter lowers the global curvature while the local ripple curvature is unchanged, so the relative curvature change—and hence the SCF—depends jointly on diameter, wall thickness, wavelength and circumferential extent. This diameter dependence is the central reason a parametric study is required, and it is examined directly in Section 3.

## 2.2 Geometry and parametric design

Three line-pipe diameters typical of large-diameter gas transmission were studied: 36, 48 and 56 in (914.4, 1219.2 and 1422.4 mm). To separate the effect of diameter from that of wall slenderness, the thickness of each pipe was sized with the Barlow relation at a design factor of 0.72 [2]. This holds the diameter-to-thickness ratio constant at $D/t = 73.1$ and fixes the nominal hoop stress at $\sigma_h = 349.2$ MPa for a maximum allowable operating pressure (MAOP) of 9.55 MPa across all three sizes (Table 1). Diameter therefore varies while the membrane stress state is held identical, so any change in SCF can be attributed to scale rather than to a change in nominal stress. Holding $D/t$ constant serves a second purpose: it keeps the large-diameter results directly comparable with acceptance analyses calibrated at smaller diameters, where $D/t$ is the governing geometric group.

The ripple was represented as a localised raised-cosine crest–trough perturbation of the otherwise cylindrical wall (Fig. 2). Three geometric variables were each set at three levels in a Taguchi L9 orthogonal array: the circumferential extent $\theta$ (90°, 135°, 180°, equivalent to $a/C = 0.25$, 0.375 and 0.50), the normalised depth $d/D$, and the wavelength-to-depth ratio $L/d$. The same array was applied to each diameter with depths scaled to keep $d/D$ fixed, giving 27 finite element analyses. Because $\theta$ and $L/d$ are partially confounded within the L9 design, an additional set of controlled wavelength sweeps—holding $\theta$ and $d/D$ fixed while varying $L/d$—added 11 analyses, for 38 data points in total. The full array is given in Table S1.

## 2.3 Finite element model

The pipe wall was modelled with four-node reduced-integration shell elements (S4R) in Abaqus/Standard 2020 (Table 2). For thin-walled pressure geometries with $t/R \ll 1$, shell elements capture the membrane and bending response on the mid-surface without the through-thickness element stacking that solid elements require. The reduced integration of the S4R formulation also avoids the transverse shear locking of fully integrated elements at low computational cost [27,30]. Each node carries six degrees of freedom, the thickness is assigned as a section property, and the material is isotropic linear elastic with $E = 203$ GPa and $\nu = 0.3$.

Symmetry about the $Y$–$Z$ plane was exploited by modelling one half of the pipe (Fig. 1), which halves the cost of the parametric family. On the symmetry plane the out-of-plane translation and the in-plane rotations were restrained. Rigid-body motion was removed with the minimum kinematic constraints applied at a reference node, so that the ripple stress field is not artificially stiffened. A structured quadrilateral mesh was used throughout, with edge seeding concentrating elements at the crest and trough where the gradient is highest, and element aspect ratios were kept below three [27]. The validation model contained 31,968 elements and about 194,000 degrees of freedom. Mesh adequacy was assessed with a three-level convergence study in which the ripple-region element size was reduced from 20 mm to 15 mm and 10 mm; the peak Von Mises stress rose from 640.3 MPa to 672.8 MPa and 718.6 MPa as the steep gradient at the crest was resolved, and the finest mesh—which also gave the closest agreement with the reference benchmark of Section 2.4—was adopted for the full parametric family [4].

Loading reproduced the closed-end pressurised condition. A uniform pressure was applied to the inner surface, and the axial thrust acting on the (unmodelled) end caps was represented by an equivalent edge force, $F_{\text{cap}} = P\,\pi R_i^2$ (Eq. 4), distributed along the end section and scaled to the half-model. This transmits the correct axial membrane stress without a rigid cap that would distort the local response near the ripple.

## 2.4 Verification and validation

Model fidelity was established at three levels following the ASME V&V 10 methodology [20,21]. First, the end-cap force from the edge-load definition matched the analytical pressure thrust to within 0.013% (Table 3). Second, in the defect-free body of the pipe the computed hoop stress reproduced the thin-shell value $\sigma_h = PD/2t = 220.8$ MPa, confirming the boundary conditions and material setup.

Third, the model was benchmarked against the full-scale test and finite element study of Rosenfeld et al. [4], using the matched case $d/D = 0.037$, $a/C = 0.5$ on a 36 in pipe at 3.45 MPa (Table 3, Fig. 3). The circumferential stress, which is the component that drives pressure-cycle fatigue, agreed to within $+4.9\%$. The Von Mises and axial stresses differed by $-8.3\%$ and $-6.3\%$, and the corresponding SCF was 3.25 against the reference 3.55; both values lie within the $\mathrm{SCF}_P \approx 3.0$–$3.5$ band the reference reports for this depth at $D/t \approx 128$. The residual differences are consistent with documented methodological differences between the two studies: the reference digitised a five-crest ripple from API test specimens whereas a single trough–crest raised-cosine profile was used here; the reference applied quarter rather than half symmetry; and it used the FACTS rather than the Abaqus solver. The reference itself reports an ~8% sensitivity of SCF to crest count, which accounts for much of the gap. The agreement is within the range usually accepted for shell benchmarks of this class and supports use of the model in the parametric study.

## 2.5 Fatigue assessment methodology

The fatigue assessment couples the elastic SCF to a load-controlled S–N framework. Internal-pressure cycling is a load-controlled demand, for which the Markl endurance relation gives the allowable cycle count as $N_f = (C'/(\mathrm{SCF}_P\,S_a))^5$ (Eq. 7), where $S_a$ is the local stress amplitude and $C'$ a material–loading coefficient [22]. The Markl stress-intensification factor is structurally equivalent to a stress concentration factor [4], so the $\mathrm{SCF}_P$ from the parametric model (Section 3) is used directly in its place. The load-controlled coefficient $C' = 1126$ MPa was adopted rather than Markl's original displacement-controlled value, following the calibration of Rosenfeld et al. against internally pressurised vessel-nozzle tests, because pressure cycling is load- rather than displacement-controlled [4,22].

The stress amplitude of each cycle follows from the pressure range through the nominal hoop stress, $S_{a,i} = \Delta\sigma_{h,i}/2 = \tfrac{1}{2}\sigma_h(\Delta P_i/\mathrm{MAOP})$ (Eq. 8). An operating pressure history is reduced to discrete cycle bins by rainflow counting in accordance with ASTM E1049 [23], and the cumulative damage is summed linearly with the Palmgren–Miner rule, $D_m = \sum_i n_i/N_i$, with failure at $D_m = 1$ and the estimated life taken as the reciprocal of the annual damage, $t_{\text{est}} = 1/D_{m,\text{yr}}$ (Eq. 9) [24]. Because $N_f$ scales with the fifth power of stress amplitude, damage is dominated by the largest pressure cycles. This strong amplitude sensitivity, and its consequences for a realistic operating spectrum, are quantified in Section 3.

<!--
DRAFT NOTES (for WP5b/WP6a, not part of prose):
- Word count target ~2050 (Section A); this draft ~1850 — within range.
- Citations provisional; map to WP2 pool, finalize numbering in WP6b. Markl original (D2) [VERIFY].
- 36" mean discrepancy (1.89 vs 1.96) belongs to Results (Section 3), flagged in WP4.
- a/C deviation-sign correction (thesis L955) applies to Results, not Methods.
- Parametric SCF *results* (LD-SCF regression, IPC deviation) go in Results (WP5b).
-->
