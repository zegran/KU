# Stress concentration and fatigue life of mild field-bend ripples in large-diameter API 5L X70 pipelines

Korcan Ünal^a^

^a^ [Affiliation, City, Country — to be completed by the author] · ORCID: [⚠ author] · e-mail: [⚠ author]

# Highlights

- Parametric FEA gives ripple SCF of 1.42-2.37 in large-diameter API 5L X70 pipe
- New closed-form SCF correlation (R2=0.916) for large-diameter pipe at D/t=73.1
- SCF rises as diameter falls at constant D/t, so absolute size must be assessed
- Fatigue is spectrum-driven: 80%-MAOP cycles govern most of the annual damage
- Closed-form critical SCF of 1.56 enables fitness-for-service ripple decisions

# Abstract

Mild ripples formed during cold field bending perturb the local stress field of high-strength gas transmission pipelines, and quantitative acceptance guidance at the large diameters now common in transmission service is limited. This work extends ripple acceptance analysis to large-diameter line pipe: a parametric stress-concentration-to-life framework is developed for mild ripples in API 5L X70 and used to establish an explicit acceptance threshold. Elastic shell finite element analyses spanning 36, 48 and 56 in pipe at a fixed diameter-to-thickness ratio of 73.1, arranged as a Taguchi array with supporting wavelength sweeps, map the dependence of the ripple stress concentration factor on depth, wavelength and circumferential extent. The elastic factors are then carried into a load-controlled Markl–rainflow–Miner fatigue assessment under a representative operating pressure spectrum. The stress concentration factor ranged from 1.42 to 2.37 across the parametric domain, and a closed-form empirical correlation reproduces the finite element data with $R^2 = 0.916$. Fatigue damage proved spectrum-governed: the 80%-of-MAOP cycle band alone accounted for more than half of the annual total. The framework yields a closed-form critical stress concentration factor of about 1.56 for a 100-year design life, presented as a master curve for direct fitness-for-service decisions on in-line-inspection-reported ripples.

**Keywords:** API 5L X70; Mild ripple; Stress concentration factor; Finite element analysis; Markl–Miner fatigue; Fitness-for-service


# 1. Introduction

Long-distance gas transmission pipelines rarely follow a straight route. Terrain, geotechnical conditions and existing infrastructure force changes of direction, and these are commonly achieved by field bending: straight joints are plastically curved on site with a cold bending machine instead of installing factory elbows, which reduces the number of girth welds and is economical at large diameter [1,2]. During bending the pipe wall is stretched on the extrados and compressed on the intrados, and in thin-walled, high $D/t$ pipe the intrados compression can produce shallow, periodic crest–trough distortions of the wall [2,3]. These low-amplitude features, termed mild ripples, are distinguished in CSA Z662 from severe buckles: they do not constitute an imminent collapse mechanism, but they do perturb the local stress field [1,4].

The material context sharpens the question. Modern transmission increasingly uses high-strength low-alloy grades such as API 5L X70, whose combination of high yield strength and adequate ductility permits thinner walls and higher operating pressures [5,6]. The same thinner walls, however, make the local stress elevation produced by a geometric imperfection more consequential, because the elastic stress concentration that governs crack initiation scales with the severity of the local curvature change [7]. Pipeline design codes recognise this tension only partially. ASME B31.8 and CSA Z662 define ripple and wrinkle geometries and impose dimensional limits, but they do not quantify the stress concentration or fatigue penalty that a given ripple carries [1,8]. In practice the codes leave the operator two options: remove every reported feature by cut-out or repair with sleeve, or demonstrate acceptability through a rigorous engineering analysis [8,9]. Because the first route is conservative and costly, a defensible quantitative basis for the second is of direct practical value.

Such a basis must begin with reliable field characterisation. In-line inspection with a geometry (caliper) tool measures the internal radius along and around the pipe and returns a radius map in which ripple regions appear as repeating axial bands of inward and outward deviation [10,11]. These maps yield the parameters a numerical model needs—the axial wavelength, the crest-to-trough depth and the circumferential extent of the feature—and so connect the inspection record directly to a finite element representation. Finite element analysis is the established tool for converting that geometry into stress: it resolves the membrane and bending response in the ripple region, and code-referenced acceptance criteria for ripples have themselves been built on experimentally calibrated finite element results [4,12].

A widely used engineering correlation for ripple acceptance was developed by Rosenfeld et al. [4], who combined full-scale cyclic-pressure tests with elastic finite element analysis to express the ripple stress concentration factor as a power-law function of the normalised geometry and to relate it to fatigue life through the Markl S–N framework. The correlation was calibrated on pipe sizes up to 36 in, whereas contemporary transmission routinely uses 42, 48 and 56 in pipe, in which the distribution of bending stiffness and the local stability behaviour differ [13]. Extending ripple acceptance analysis to these diameters is therefore of direct practical interest, and it raises questions regarding the applicability of geometry terms fitted at smaller scale. A second gap is methodological: ripple severity is usually reported as a single stress concentration factor, yet fatigue damage accumulates under a spectrum of operating pressure cycles, and the two have rarely been assessed together for ripples in large-diameter pipe.

This work addresses both gaps. A parametric stress-concentration-to-life framework is developed for mild ripples in large-diameter API 5L X70 pipelines and used to establish an explicit acceptance threshold, intended as a quantitative reference for fitness-for-service evaluations of ripple-type geometric anomalies. A family of 38 elastic shell finite element analyses, organised as a Taguchi array with supporting wavelength sweeps, spans three diameters (36, 48 and 56 in) at a fixed $D/t = 73.1$; the ratio is held constant so that the large-diameter results remain directly comparable with acceptance analyses at smaller diameters. The family maps the dependence of the ripple stress concentration factor on ripple depth, wavelength and circumferential extent, and the elastic factors are then carried into a load-controlled Markl–rainflow–Miner fatigue assessment under a realistic pressure spectrum. The contributions are:

- a closed-form empirical correlation for the ripple stress concentration factor of large-diameter X70 pipe ($D/t = 73.1$), fitted to the finite element data with $R^2 = 0.916$ and a maximum error of 9%;
- a systematic benchmark against the existing acceptance correlation across the studied envelope, quantifying the diameter and circumferential-extent effects that geometry terms fitted at smaller diameters do not carry over to large-diameter pipe;
- an integrated fatigue assessment showing that damage is governed by the operating pressure spectrum as much as by the stress concentration factor, with moderately large cycles dominating;
- a closed-form critical stress concentration factor and an accompanying master curve that translate the framework into a direct fitness-for-service accept / analyse / repair decision for in-line-inspection-detected ripples.

The remainder of the paper is organised as follows. Section 2 presents the theoretical basis, the parametric design, the finite element model and its validation, and the fatigue methodology. Section 3 reports the parametric stress concentration results, the empirical correlation and the fatigue damage analysis. Section 4 develops the critical-threshold framework, examines the limitations of the existing correlation, and states the boundaries of the present results. Section 5 concludes.

# 2. Materials and methods

## 2.1 Theoretical framework

Under internal pressure, a defect-free thin-walled pipe carries load almost entirely through membrane action. Classical thin-shell theory gives the nominal hoop and longitudinal stresses as $\sigma_h = PR/t$ and $\sigma_L = PR/2t$ (Eq. 1), with no through-thickness bending [14]. A field-bend ripple breaks this idealisation. The periodic crest–trough geometry imposes a local change of wall curvature, so the wall must carry bending in addition to membrane stress. The bending stiffness scales with the flexural rigidity $D_f = Et^3/12(1-\nu^2)$ (Eq. 2), and the peak stress concentrates at the crest and trough, where the curvature gradient is steepest.

The severity of this elevation is measured by the pressure-based stress concentration factor, $\mathrm{SCF}_P = \sigma_{\max,\text{local}}/\sigma_{h,\text{nominal}}$ (Eq. 3): the ratio of the peak local stress to the nominal membrane hoop stress of the equivalent defect-free pipe [15]. Because this elastic factor is the input to the fatigue assessment of Section 2.5, every analysis is kept within the linear-elastic range. The assumption is checked after each solution by confirming that the peak stress stays below the specified minimum yield strength of API 5L X70.

A direct consequence of the membrane–bending coupling is that depth alone does not describe ripple severity. At a fixed normalised depth, increasing the pipe diameter lowers the global curvature while the local ripple curvature is unchanged, so the relative curvature change—and hence the SCF—depends jointly on diameter, wall thickness, wavelength and circumferential extent. This diameter dependence is the central reason a parametric study is required, and it is examined directly in Section 3.

## 2.2 Geometry and parametric design

Three line-pipe diameters typical of large-diameter gas transmission were studied: 36, 48 and 56 in (914.4, 1219.2 and 1422.4 mm). To separate the effect of diameter from that of wall slenderness, the thickness of each pipe was sized with the Barlow relation at a design factor of 0.72 [8]. This holds the diameter-to-thickness ratio constant at $D/t = 73.1$ and fixes the nominal hoop stress at $\sigma_h = 349.2$ MPa for a maximum allowable operating pressure (MAOP) of 9.55 MPa across all three sizes (Table 1). Diameter therefore varies while the membrane stress state is held identical, so any change in SCF can be attributed to scale rather than to a change in nominal stress. Holding $D/t$ constant serves a second purpose: it keeps the large-diameter results directly comparable with acceptance analyses calibrated at smaller diameters, where $D/t$ is the governing geometric group.

Table 1. Parametric pipe geometries (constant $D/t = 73.1$, $\sigma_h = 349.2$ MPa, $P = 9.55$ MPa) and resulting $\mathrm{SCF}_P$ summary over the Taguchi L9 array.

| OD | $D$ (mm) | $t$ (mm) | $D/t$ | $\mathrm{SCF}_P$ range | Mean* |
|----|---------|----------|-------|------------------------|-------|
| 36″ | 914.4 | 12.50 | 73.1 | 1.52–2.37 | 1.89 |
| 48″ | 1219.2 | 16.67 | 73.1 | 1.50–2.14 | 1.78 |
| 56″ | 1422.4 | 19.45 | 73.1 | 1.42–1.95 | 1.68 |

*Mean of the nine tabulated L9 cases. Overall $\mathrm{SCF}_P$ range 1.42–2.37; smaller diameter gives higher SCF.

The ripple was represented as a localised raised-cosine crest–trough perturbation of the otherwise cylindrical wall (Fig. 1). Three geometric variables were each set at three levels in a Taguchi L9 orthogonal array [16]: the circumferential extent $\theta$ (90°, 135°, 180°, equivalent to $a/C = 0.25$, 0.375 and 0.50), the normalised depth $d/D$, and the wavelength-to-depth ratio $L/d$. The same array was applied to each diameter with depths scaled to keep $d/D$ fixed, giving 27 finite element analyses. Because $\theta$ and $L/d$ are partially confounded within the L9 design, an additional set of controlled wavelength sweeps—holding $\theta$ and $d/D$ fixed while varying $L/d$—added 11 analyses, for 38 data points in total. The full array is given in Table S1.

![Fig. 1. Ripple geometry parameterisation: (a) longitudinal raised-cosine crest–trough profile (depth *d*, half-wavelength *L*/2); (b) circumferential extent θ (*a/C*). Constant *D/t* = 73.1, API 5L X70, *P* = 9.55 MPa.](C:/Users/zduna/Desktop/Korc/Docs/paper/figures/mf2_ripple_geometry.png){width=15cm}

## 2.3 Finite element model

The pipe wall was modelled with four-node reduced-integration shell elements (S4R) in Abaqus/Standard 2020 [19] (Table 2). For thin-walled pressure geometries with $t/R \ll 1$, shell elements capture the membrane and bending response on the mid-surface without the through-thickness element stacking that solid elements require. The reduced integration of the S4R formulation also avoids the transverse shear locking of fully integrated elements at low computational cost [17,18]. Each node carries six degrees of freedom, the thickness is assigned as a section property, and the material is isotropic linear elastic with $E = 203$ GPa and $\nu = 0.3$.

Table 2. Numerical model and material parameters (representative validation model).

| Parameter | Value |
|-----------|-------|
| Solver | Abaqus/Standard 2020 |
| Element type | S4R (4-node reduced-integration shell) |
| DOF per node | 6 |
| Element shape / scheme | quadrilateral / structured |
| Elements | 31,968 |
| Total DOF | ≈194,388 |
| Model symmetry | half-symmetric (180°) |
| Model length | 5,000 mm |
| Aspect-ratio criterion | ≤ 3 |
| Material model | isotropic linear elastic (API 5L X70) |
| Young's modulus, $E$ | 203,000 MPa |
| Poisson's ratio, $\nu$ | 0.3 |

Symmetry about the $Y$–$Z$ plane was exploited by modelling one half of the pipe (Fig. 2), which halves the cost of the parametric family. On the symmetry plane the out-of-plane translation and the in-plane rotations were restrained. Rigid-body motion was removed with the minimum kinematic constraints applied at a reference node, so that the ripple stress field is not artificially stiffened. A structured quadrilateral mesh was used throughout, with edge seeding concentrating elements at the crest and trough where the gradient is highest, and element aspect ratios were kept below three [17]. The validation model contained 31,968 elements and about 194,000 degrees of freedom. Mesh adequacy was assessed with a three-level convergence study in which the ripple-region element size was reduced from 20 mm to 15 mm and 10 mm; the peak von Mises stress rose from 640.3 MPa to 672.8 MPa and 718.6 MPa as the steep gradient at the crest was resolved, and the finest mesh—which also gave the closest agreement with the reference benchmark of Section 2.4—was adopted for the full parametric family [4].

![Fig. 2. Half-symmetric S4R shell model of a field-bend ripple in an API 5L X70 pipe: (a) geometry, mesh and global axes; (b) internal pressure, end-cap force and boundary conditions via RP-1; (c) structured quadrilateral mesh detail at the ripple.](C:/Users/zduna/Desktop/Korc/Docs/paper/figures/mf1_model_setup.png){width=15cm}

Loading reproduced the closed-end pressurised condition. A uniform pressure was applied to the inner surface, and the axial thrust acting on the (unmodelled) end caps was represented by an equivalent edge force, $F_{\text{cap}} = P\,\pi R_i^2$ (Eq. 4), distributed along the end section and scaled to the half-model. This transmits the correct axial membrane stress without a rigid cap that would distort the local response near the ripple.

## 2.4 Verification and validation

Model fidelity was established at three levels following the ASME V&V 10 methodology [20,21]. First, the end-cap force from the edge-load definition matched the analytical pressure thrust to within 0.013% (Table 3). Second, in the defect-free body of the pipe the computed hoop stress reproduced the thin-shell value $\sigma_h = PD/2t = 220.8$ MPa, confirming the boundary conditions and material setup.

Table 3. Verification and validation against the full-scale benchmark of Rosenfeld et al. [4], matched case $d/D = 0.037$, $a/C = 0.5$. Reference stresses converted from ksi.

| Quantity | Reference | This work | Difference |
|----------|-----------|-----------|------------|
| End-cap force (N) | 1,128,697 | 1,128,840 | 0.013% |
| Nominal hoop stress (MPa) | 220.8 (analytic) | ≈220.8 (FEA) | — |
| von Mises peak (MPa) | 784.0 | 718.6 | −8.3% |
| $S_{11}$ circumferential (MPa) | 759.9 | 796.8 | +4.9% |
| $S_{22}$ axial (MPa) | 806.8 | 755.9 | −6.3% |
| $\mathrm{SCF}_P$ (von Mises basis) | 3.549 | 3.254 | −8.3% |

Third, the model was benchmarked against the full-scale test and finite element study of Rosenfeld et al. [4], using the matched case $d/D = 0.037$, $a/C = 0.5$ on a 36 in pipe at 3.45 MPa (Table 3, Fig. 3). The circumferential stress, which is the component that drives pressure-cycle fatigue, agreed to within $+4.9\%$. The von Mises and axial stresses differed by $-8.3\%$ and $-6.3\%$, and the corresponding SCF was 3.25 against the reference 3.55; both values lie within the $\mathrm{SCF}_P \approx 3.0$–$3.5$ band the reference reports for this depth at $D/t \approx 128$. The residual differences are consistent with documented methodological differences between the two studies: the reference digitised a five-crest ripple from API test specimens whereas a single trough–crest raised-cosine profile was used here; the reference applied quarter rather than half symmetry; and it used the FACTS rather than the Abaqus solver. The reference itself reports an ~8% sensitivity of SCF to crest count, which accounts for much of the gap. The agreement is within the range usually accepted for shell benchmarks of this class and supports use of the model in the parametric study.

![Fig. 3. Model validation against the full-scale benchmark of Rosenfeld et al. [4]: (a) S11 hoop-stress contour at the ripple; (b) peak-stress benchmark (end-cap force 0.013%; nominal hoop 220.8 MPa analytic; SCF 3.25 vs 3.55).](C:/Users/zduna/Desktop/Korc/Docs/paper/figures/mf3_validation.png){width=15cm}

## 2.5 Fatigue assessment methodology

The fatigue assessment couples the elastic SCF to a load-controlled S–N framework. Internal-pressure cycling is a load-controlled demand, for which the Markl endurance relation gives the allowable cycle count as $N_f = (C'/(\mathrm{SCF}_P\,S_a))^5$ (Eq. 5), where $S_a$ is the local stress amplitude and $C'$ a material–loading coefficient [22]. The Markl stress-intensification factor is structurally equivalent to a stress concentration factor [4], so the $\mathrm{SCF}_P$ from the parametric model (Section 3) is used directly in its place. The load-controlled coefficient $C' = 1126$ MPa was adopted rather than Markl's original displacement-controlled value, following the calibration of Rosenfeld et al. against internally pressurised vessel-nozzle tests, because pressure cycling is load- rather than displacement-controlled [4,23].

The stress amplitude of each cycle follows from the pressure range through the nominal hoop stress, $S_{a,i} = \Delta\sigma_{h,i}/2 = \tfrac{1}{2}\sigma_h(\Delta P_i/\mathrm{MAOP})$ (Eq. 6). An operating pressure history is reduced to discrete cycle bins by rainflow counting in accordance with ASTM E1049 [24], and the cumulative damage is summed linearly with the Palmgren–Miner rule, $D_m = \sum_i n_i/N_i$, with failure at $D_m = 1$ and the estimated life taken as the reciprocal of the annual damage, $t_{\text{est}} = 1/D_{m,\text{yr}}$ (Eq. 7) [25]. Because $N_f$ scales with the fifth power of stress amplitude, damage is dominated by the largest pressure cycles. This strong amplitude sensitivity, and its consequences for a realistic operating spectrum, are quantified in Section 3.

# 3. Results

## 3.1 Parametric stress concentration and the diameter effect

Across the full parametric family the pressure-based stress concentration factor ranged from 1.42 to 2.37 (Fig. 4a, Table 1). Two trends stand out. First, the circumferential extent $\theta$ was the dominant driver: cases with $\theta = 90^\circ$ stayed between 1.42 and 1.89, whereas widening the ripple to $\theta = 180^\circ$ raised $\mathrm{SCF}_P$ to 1.51–2.37. The maximum throughout was the D7 configuration ($\theta = 180^\circ$, largest $d/D$, smallest $L/d$), and the minima were the shallow narrow cases (D1, D6). Depth $d/D$ acted as the second-order driver, with the wavelength ratio $L/d$ weaker still.

![Fig. 4. Parametric SCF~P~ over the Taguchi L9 array at three diameters: (a) FEA SCF~P~ per case; (b) FEA vs the reference correlation (Eq. 8); (c) deviation from Eq. 8 vs circumferential extent *a/C*.](C:/Users/zduna/Desktop/Korc/Docs/paper/figures/mf4_parametric_scf.png){width=15cm}

Second, $\mathrm{SCF}_P$ depended systematically on diameter even though the diameter-to-thickness ratio was held constant at 73.1. The diameter-averaged factor fell from 1.89 at 36 in to 1.78 at 48 in and 1.68 at 56 in—a smaller pipe consistently produced a higher concentration for the same normalised ripple, in every one of the nine array configurations. Because $D/t$ was held constant, this residual dependence cannot be captured by any correlation that enters geometry only through the diameter-to-thickness ratio: at the scales now common in transmission service, absolute diameter acts as an independent variable.

## 3.2 Benchmark against the existing acceptance correlation

Comparing every analysis against the acceptance correlation of Rosenfeld et al. [4] (Eq. 8) reveals a systematic, extent-dependent departure rather than random scatter (Fig. 4b,c). The sign and magnitude of the departure track the circumferential extent directly. For narrow ripples ($a/C = 0.25$) the correlation over-predicts the FEA result by 31–84%, the over-prediction growing as the diameter decreases. For wide ripples ($a/C = 0.50$) the correlation instead under-predicts, and severely so, by 48% up to more than 400%, with the intermediate $a/C = 0.375$ cases spanning the transition.

The cause lies in the $(a/C)^{-2.87}$ term of the correlation. A large negative exponent forces the predicted SCF to fall steeply as the ripple widens, so that the multiplier drops from about 53 at $a/C = 0.25$ to about 7 at $a/C = 0.50$. The finite element results show the opposite physical tendency: a wider ripple engages more of the circumference and is more severe, not less. The empirical fit of Section 3.4 confirms this, returning an $a/C$ exponent of only $+0.065$—weakly positive—against the correlation's $-2.87$. A circumferential-extent dependence fitted at smaller diameters therefore does not carry over to the large-diameter, high-strength regime examined here.

## 3.3 Wavelength sensitivity

Because $\theta$ and $L/d$ are partially confounded in the L9 array, the wavelength effect was isolated by controlled sweeps at fixed $\theta$ and $d/D$ (Table S1). The response was both stronger than the reference correlation implies and diameter-dependent. For the 36 in pipe, increasing $L/d$ from 6 to 12 lowered $\mathrm{SCF}_P$ by 13.8% (2.17 to 1.87), roughly nine times the change implied by the correlation's wavelength exponent. The 48 in pipe showed a similar but milder reduction of 8.6%. The 56 in pipe, at $\theta = 90^\circ$ and low $d/t$, reversed the trend with a slight 2.3% rise. This interaction between wavelength and scale is a further indication that a single fixed-exponent correlation cannot represent the full geometry space.

## 3.4 Empirical large-diameter SCF correlation

The 38 finite element points were fitted with ordinary least squares in log space (Eq. 9b), which linearises the assumed power-law form and admits a closed-form solution [26]. The result is the correlation of Eq. 9,
$$\mathrm{SCF}_P = 142.1\,(d/D)^{0.938}\,(d/t)^{-0.676}\,(L/d)^{-0.167}\,(a/C)^{0.065},$$
valid for $D/t = 73.1$ and API 5L X70. The fit is accurate over the whole parametric domain: the coefficient of determination is $R^2 = 0.916$, the root-mean-square error is 0.058 SCF units—about 3% of the mean—and no point departs from the prediction by more than 9% (Fig. 5). The residuals are symmetric about the line of perfect agreement, with no systematic bias.

![Fig. 5. Empirical SCF correlation (Eq. 9): (a) predicted vs FEA with ±9% band (R² = 0.916, RMSE = 0.058); (b) relative residual distribution.](C:/Users/zduna/Desktop/Korc/Docs/paper/figures/mf5_ldscf_regression.png){width=15cm}

The exponents make the parameter hierarchy explicit. Depth carries the largest positive exponent ($+0.938$), the wall-thickness ratio moderates it ($-0.676$), and the wavelength term is weak ($-0.167$). The circumferential exponent is only $+0.065$, small but positive, and is the quantitative form of the extent-dependent departure discussed in Section 3.2. Within its stated envelope the correlation provides a self-contained acceptance basis for large-diameter pipe; its extension to other $D/t$ ratios requires further analyses and is noted as future work.

## 3.5 Pressure-cycle fatigue damage

Translating the elastic SCF into life through the Markl–Miner framework (Section 2.5) exposes the fifth-power sensitivity of damage to stress amplitude (Table S2). Lowering a cycle from 100% to 50% of MAOP multiplies its allowable count by $2^5 = 32$, and a single full-pressure cycle can produce as much damage as millions of small ones. For a single full-MAOP cycle the worst-case D7 configuration gave allowable counts of 396, 249 and 149 at 56, 48 and 36 in respectively (Table S3); at 56 in this corresponds to a unit damage of $2.5\times10^{-3}$, so only about four full cycles per year would exhaust a 100-year design life.

Realistic operation, however, mixes amplitudes. A representative transmission spectrum—two full-MAOP, 24 high (80%), 52 moderate (50%) and 200 small (5%) cycles per year—applied to the 56 in D7 case ($\mathrm{SCF}_P = 1.95$) gives an annual damage of $2.90\times10^{-2}$ and an estimated life of about 34 years (Table 4, Fig. 6). The damage is not dominated by the largest cycles. The 80%-MAOP band alone contributes 68.6% of the annual total, against 17.4% from the two full-MAOP cycles and 14.2% from the moderate band; the 200 small cycles contribute essentially nothing. The most damaging group is therefore neither the largest in amplitude nor the most numerous, but the moderately large cycles that recur often—a finding that ties ripple severity to the operating pressure spectrum, not to the SCF alone. The threshold this implies for fitness-for-service decisions is developed in Section 4.

Table 4. $\mathrm{SCF}_P$ sensitivity of fatigue life ($n = 12$ full MAOP cycles/yr, $\sigma_h = 349.2$ MPa, 100-yr design life). Critical threshold at $\mathrm{SCF}_P \approx 1.56$.

| $\mathrm{SCF}_P$ | $N_f$ | $D_{m,100\,\mathrm{yr}}$ | $t_{\mathrm{est}}$ (yr) | Status |
|------|------|------|------|--------|
| 1.42 | 1932 | 0.62 | 161 | $D_m < 1$ (safe) |
| 1.51 | 1422 | 0.84 | 118 | $D_m < 1$ (attention) |
| 1.65 | 912 | 1.32 | 76 | $D_m > 1$ |
| 1.95 | 396 | 3.03 | 33 | $D_m > 1$ |
| 2.14 | 249 | 4.83 | 21 | $D_m > 1$ |
| 2.37 | 149 | 8.04 | 12 | $D_m > 1$ |

Mixed spectrum (56″ D7, $\mathrm{SCF}_P = 1.95$): $D_{m,\mathrm{yr}} = 2.90 \times 10^{-2}$, $t_{\mathrm{est}} \approx 34$ yr; the 80%-MAOP band contributes 68.6% of annual damage.

![Fig. 6. Mixed-spectrum annual fatigue-damage distribution for the 56″ D7 case (SCF~P~ = 1.95): the 80%-MAOP band contributes 68.6% of the damage; t~est~ ≈ 34 yr.](C:/Users/zduna/Desktop/Korc/Docs/paper/figures/mf6_mixed_spectrum.png){width=15cm}

# 4. Discussion

## 4.1 A critical SCF threshold for fitness-for-service

The practical value of coupling the parametric SCF to the Markl–Miner chain is that it produces a single, operationally meaningful decision quantity: the stress concentration above which a ripple cannot meet the design life. Setting the cumulative damage to its limit, $D_m = nT/N_f = 1$, and substituting the load-controlled endurance relation (Eqs. 5–6) gives a closed form for this critical factor,
$$\mathrm{SCF}_{\text{crit}} = \frac{C'}{S_a\,(nT)^{0.2}} \quad\text{(Eq. 10)},$$
where $n$ is the number of full-MAOP-equivalent cycles per year and $T$ the design life. For a representative duty of $n = 12$ cycles/yr over $T = 100$ years, Eq. 10 returns $\mathrm{SCF}_{\text{crit}} \approx 1.56$. This is consistent with the discrete sensitivity analysis, in which configurations at or below $\mathrm{SCF}_P = 1.51$ meet the design life while those at or above 1.65 fail it.

Figure 7 generalises the single threshold into a master curve. Plotting estimated life against $\mathrm{SCF}_P$ for a family of cycle counts ($n = 4$ to 24/yr), with the design-life line superimposed, turns Eq. 10 into a direct read-off: for any operating intensity, the intersection gives the admissible SCF, and the parametric cases fall on the curve at their computed factors. An operator with an ILI-measured ripple can therefore estimate $\mathrm{SCF}_P$ from the correlation of Eq. 9, locate the pipe on Fig. 7 for its own duty cycle, and obtain an immediate accept / analyse / repair decision. This is the quantitative basis that codes such as CSA Z662 and ASME B31.8 permit but do not themselves supply [1,8], and it advances the field practice from "remove any ripple" toward "assess each ripple," in line with the rigorous-analysis route of API 579 [27].

![Fig. 7. Critical SCF threshold master curve: estimated fatigue life vs SCF~P~ for n = 4/8/12/24 full-MAOP-equivalent cycles per year; the intersection with the 100-yr design-life line gives SCF~crit~ ≈ 1.56 at n = 12 (Eq. 10). Parametric FEA configurations overlaid.](C:/Users/zduna/Desktop/Korc/Docs/paper/figures/mf7_anchor_scf_threshold.png){width=15cm}

## 4.2 Applicability of the existing correlation at large diameter

The benchmarking of Section 3 shows that the IPC2002 correlation of Rosenfeld et al. [4], although appropriate for the pipe sizes up to 36 in on which it was calibrated, should not be extrapolated to the large-diameter, high-strength line pipe studied here—precisely the comparison the constant $D/t = 73.1$ design was constructed to allow. Two departures appear. First, because the correlation enters geometry only through $D/t$, it cannot represent the residual diameter dependence observed at fixed $D/t$, where the mean SCF rose by 13% from the 56 in to the 36 in pipe. Second, its $(a/C)^{-2.87}$ term runs against the computed trend: it lowers the predicted SCF as the ripple widens, whereas the finite element results—and the weakly positive fitted exponent of $+0.065$—show that a wider ripple is more severe. The consequence is a systematic, sign-changing departure, from over-prediction by up to 84% for narrow ripples to under-prediction exceeding 400% for wide ones. The under-prediction is the direction that matters for integrity, since it would classify a genuinely severe wide ripple as benign. The proposed correlation removes both departures within its stated envelope.

## 4.3 Severity depends on the pressure spectrum, not the SCF alone

A second outcome of the integrated assessment is that the stress concentration is an incomplete index of fatigue severity. For the mixed spectrum considered, the moderately large 80%-MAOP cycles contributed 68.6% of the annual damage—more than the full-MAOP cycles and the moderate band combined—because they pair a substantial amplitude with a high recurrence, while the fifth-power law suppresses the many small cycles to a negligible share. A pipe with a moderate SCF under a high-amplitude duty can therefore be closer to its limit than one with a high SCF under a benign duty. Severity assessment should accordingly combine the elastic SCF with the rainflow-reduced operating spectrum, as done here, rather than rely on the SCF in isolation; this is consistent with spectrum-based pipeline fatigue practice [28] and with the broader move toward operationally grounded fitness-for-service evaluation of geometric anomalies [29].

## 4.4 Validity envelope and limitations

Several boundaries delimit the present results. The empirical correlation (Eq. 9) was derived at a single diameter-to-thickness ratio, $D/t = 73.1$, and for API 5L X70 at MAOP 9.55 MPa; it must not be applied outside this envelope. The ratio was fixed deliberately, as the controlled constant that isolates the diameter effect and keeps the results comparable with smaller-diameter acceptance analyses; repeating the parametric family across a range of $D/t$ values, so that a single generalised regression covers the full geometry space, is the clearest line of future work. The analyses are linear-elastic, which the post-solution yield check justifies for the mild ripples considered, but which would not hold for deeper wrinkles entering the plastic range. The ripple was idealised as a single trough–crest raised-cosine profile; field ripples are often multi-crest, and the ~8% difference in von Mises stress against the five-crest benchmark of Rosenfeld et al. reflects this and the associated solver and symmetry differences [4]. The fatigue estimates rest on a representative transmission spectrum and a total-life Markl S–N basis [30]; site-specific SCADA pressure records and a separate crack-initiation treatment would refine absolute lives. None of these bounds undermines the threshold framework itself, which is parametric and can be re-derived through Eqs. 9 and 10 for any revised envelope or duty cycle. The assessment chain demonstrated here—inspection-derived geometry, parametric shell finite element analysis, and a spectrum-based Markl–Miner evaluation closed by an explicit threshold—is not specific to ripples; it offers a template for the fitness-for-service assessment of other geometric surface anomalies in line pipe.

# 5. Conclusions

This study coupled a parametric finite element analysis of mild field-bend ripples in large-diameter API 5L X70 gas pipelines to a load-controlled Markl–Miner fatigue assessment, with the aim of providing a quantitative reference for fitness-for-service evaluation of ripple-type anomalies. Four conclusions follow.

1. Across 38 analyses at a constant diameter-to-thickness ratio of 73.1, the pressure-based stress concentration factor ranged from 1.42 to 2.37 and rose systematically as diameter decreased—a dependence that no correlation entering geometry only through $D/t$ can represent.

2. A closed-form empirical correlation (Eq. 9; $R^2 = 0.916$, maximum error 9%) reproduces the finite element factors within the studied envelope and carries a physically consistent circumferential-extent dependence, in contrast with forms calibrated at smaller diameters.

3. Combining the elastic SCF with rainflow-reduced pressure cycling shows that fatigue damage is governed by the operating spectrum as much as by the SCF: for a representative duty, the 80%-MAOP band alone produced more than half of the annual damage.

4. The assessment yields a closed-form critical stress concentration factor (Eq. 10), $\mathrm{SCF}_{\text{crit}} \approx 1.56$ for a 100-year life at twelve full-MAOP cycles per year, presented as a master curve that supports direct fitness-for-service decisions for in-line-inspection-detected ripples.

Future work should repeat the parametric family across a range of $D/t$ ratios, so that a single generalised regression covers the full geometry space, and replace the representative spectrum with site-specific SCADA records to sharpen absolute life estimates. The assessment methodology itself extends naturally to other geometric surface anomalies in line pipe.

# Declarations

**CRediT authorship contribution statement.** Korcan Ünal: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing – original draft, Writing – review & editing, Visualization.

**Funding.** [⚠ Author to confirm — e.g. "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors."]

**Declaration of competing interest.** [⚠ Author to confirm — e.g. "The author declares that he has no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper."]

**Data availability.** [⚠ Author to confirm — e.g. "The finite element results and the data supporting the fitted correlation are available from the author on reasonable request."]

**Acknowledgements.** [⚠ Optional — author to complete or delete.]


# References

[1] CSA Group, CSA Z662-2023: Oil and Gas Pipeline Systems, CSA Group, Mississauga, ON, Canada, 2023.

[2] P. Bilston, N.W. Murray, The role of cold field bending in pipeline construction, Pipeline Research Council International (PRCI), 1993.

[3] D.W. Murray, Local buckling, strain localization, wrinkling and postbuckling response of line pipe, Eng. Struct. (1997). https://doi.org/10.1016/S0141-0296(96)00096-X.

[4] M.J. Rosenfeld, J.D. Hart, N. Zulfiqar, R.W. Gailing, Development of acceptance criteria for mild ripples in pipeline field bends, in: Proceedings of the 4th International Pipeline Conference (IPC 2002), Calgary, AB, Canada, 2002.

[5] American Petroleum Institute, API Specification 5L: Specification for Line Pipe, API, Washington, DC, USA. ⚠ edition/year

[6] J.I. Omale, E.G. Ohaeri, A.A. Tiamiyu, M. Eskandari, K.M. Mostafijur, J.A. Szpunar, Microstructure, texture evolution and mechanical properties of X70 pipeline steel after different thermomechanical treatments, Mater. Sci. Eng. A (2017). https://doi.org/10.1016/j.msea.2017.07.086.

[7] J. Schijve, Fatigue of Structures and Materials, 2nd ed., Springer, Dordrecht, Netherlands, 2009.

[8] ASME, ASME B31.8-2025: Gas Transmission and Distribution Piping Systems, American Society of Mechanical Engineers, New York, NY, USA, 2025.

[9] T. Johnson, C. Mokry, C. Apps, N. Parsibenehkohal, M. Henderson, Literature review of repair technologies for wrinkled pipelines, in: Proceedings of the 14th International Pipeline Conference (IPC 2022), Calgary, AB, Canada, 2022. https://doi.org/10.1115/IPC2022-86760.

[10] Q. Ma, G. Tian, Y. Zeng, R. Li, H. Song, Z. Wang, B. Gao, K. Zeng, Pipeline in-line inspection method, instrumentation and data management, Sensors 21 (2021) 3862. https://doi.org/10.3390/s21113862.

[11] C. Holliday, D. Wynne, A. Clyne, A. Wilde, Do you have wrinkles? A strain- and stress-based approach for the assessment of wrinkles reported by in-line inspection, in: Proceedings of the 12th International Pipeline Conference (IPC 2018), Calgary, AB, Canada, 2018. https://doi.org/10.1115/IPC2018-78488.

[12] C. Alexander, S. Kulkarni, Evaluating the effects of wrinkle bends on pipeline integrity, in: Proceedings of the 7th International Pipeline Conference (IPC 2008), Calgary, AB, Canada, 2008.

[13] B. Liu, X.J. Liu, H. Zhang, Compressive strain capacity of pipelines for strain-based design, in: Proceedings of the 7th International Pipeline Conference (IPC 2008), Calgary, AB, Canada, 2008. https://doi.org/10.1115/IPC2008-64030.

[14] S.P. Timoshenko, S. Woinowsky-Krieger, Theory of Plates and Shells, 2nd ed., McGraw-Hill, New York, NY, USA, 1959.

[15] W.D. Pilkey, D.F. Pilkey, Peterson's Stress Concentration Factors, 3rd ed., John Wiley & Sons, Hoboken, NJ, USA, 2008.

[16] P.J. Ross, Taguchi Techniques for Quality Engineering: Loss Function, Orthogonal Experiments, Parameter and Tolerance Design, McGraw-Hill, New York, NY, USA, 1988.

[17] R.D. Cook, D.S. Malkus, M.E. Plesha, R.J. Witt, Concepts and Applications of Finite Element Analysis, 4th ed., Wiley, Hoboken, NJ, USA, 2002.

[18] A. Laulusa, O.A. Bauchau, J.-Y. Choi, V.B.C. Tan, L. Li, Evaluation of some shear deformable shell elements, Int. J. Solids Struct. 43 (2006) 5033–5054. https://doi.org/10.1016/j.ijsolstr.2005.08.006.

[19] Dassault Systèmes, Abaqus Analysis User's Guide, Dassault Systèmes Simulia Corp., Providence, RI, USA, 2024.

[20] ASME, Guide for Verification and Validation in Computational Solid Mechanics, ASME V&V 10-2019, American Society of Mechanical Engineers, New York, NY, USA, 2019.

[21] W.L. Oberkampf, C.J. Roy, Verification and Validation in Scientific Computing, Cambridge University Press, Cambridge, UK, 2010.

[22] A.R.C. Markl, Fatigue tests of piping components, Trans. ASME 74 (1952) 287–299.

[23] E.C. Rodabaugh, A review of area replacement rules for pipe connections in pressure vessels and piping, WRC Bulletin 335, Welding Research Council, New York, NY, USA, 1988.

[24] ASTM International, ASTM E1049-85(2017): Standard Practices for Cycle Counting in Fatigue Analysis, ASTM International, West Conshohocken, PA, USA, 2017.

[25] M.A. Miner, Cumulative damage in fatigue, J. Appl. Mech. 12 (1945) A159–A164.

[26] D.C. Montgomery, E.A. Peck, G.G. Vining, Introduction to Linear Regression Analysis, 5th ed., Wiley, Hoboken, NJ, USA, 2012.

[27] American Petroleum Institute, API 579-1/ASME FFS-1: Fitness-for-Service, API, Washington, DC, USA, 2016.

[28] M.J. Rosenfeld, J.F. Kiefner, Basics of Metal Fatigue in Natural Gas Pipeline Systems — A Primer for Gas Pipeline Operators, Kiefner & Associates, Worthington, OH, USA (available in US DOT docket PHMSA-2011-0023). ⚠ report no./year

[29] B. Pinheiro, C. Guedes Soares, I. Pasqualino, Generalized expressions for stress concentration factors of pipeline plain dents under cyclic internal pressure, Int. J. Press. Vessels Pip. (2019). https://doi.org/10.1016/j.ijpvp.2019.01.015.

[30] M. Xie, S. Xing, J. Zhao, Ö. Karakaş, Y. Li, X. Pei, Low-cycle fatigue design of welded offshore pipe components: A modern view on ASME B31 code, Int. J. Fatigue (2022) 106982. https://doi.org/10.1016/j.ijfatigue.2022.106982.

# Supplementary material

Table S1. Full Taguchi L9 array and FEA $\mathrm{SCF}_P$ for the three diameters ($D/t = 73.1$, API 5L X70).

| OD | Case | $\theta$ (°) | $d$ (mm) | $d/D$ | $d/t$ | $L/d$ | $a/C$ | $\mathrm{SCF}_P$ |
|----|------|------|------|------|------|------|------|------|
| 36″ | D1 | 90 | 18 | 0.0197 | 1.440 | 10 | 0.250 | 1.72 |
|  | D2 | 90 | 24 | 0.0262 | 1.920 | 10 | 0.250 | 1.85 |
|  | D3 | 90 | 30 | 0.0328 | 2.400 | 12 | 0.250 | 1.89 |
|  | D4 | 135 | 24 | 0.0262 | 1.920 | 7.5 | 0.375 | 2.06 |
|  | D5 | 135 | 30 | 0.0328 | 2.400 | 8 | 0.375 | 2.10 |
|  | D6 | 135 | 18 | 0.0197 | 1.440 | 20 | 0.375 | 1.52 |
|  | D7 | 180 | 30 | 0.0328 | 2.400 | 6 | 0.500 | 2.37 |
|  | D8 | 180 | 18 | 0.0197 | 1.440 | 13.3 | 0.500 | 1.80 |
|  | D9 | 180 | 24 | 0.0262 | 1.920 | 15 | 0.500 | 1.72 |
| 48″ | D1 | 90 | 18 | 0.0148 | 1.080 | 10 | 0.250 | 1.60 |
|  | D2 | 90 | 24 | 0.0197 | 1.440 | 10 | 0.250 | 1.77 |
|  | D3 | 90 | 30 | 0.0246 | 1.800 | 12 | 0.250 | 1.86 |
|  | D4 | 135 | 24 | 0.0197 | 1.440 | 7.5 | 0.375 | 1.87 |
|  | D5 | 135 | 30 | 0.0246 | 1.800 | 8 | 0.375 | 2.00 |
|  | D6 | 135 | 18 | 0.0148 | 1.080 | 20 | 0.375 | 1.50 |
|  | D7 | 180 | 30 | 0.0246 | 1.800 | 6 | 0.500 | 2.14 |
|  | D8 | 180 | 18 | 0.0148 | 1.080 | 13.3 | 0.500 | 1.61 |
|  | D9 | 180 | 24 | 0.0197 | 1.440 | 15 | 0.500 | 1.67 |
| 56″ | D1 | 90 | 18 | 0.0127 | 0.925 | 10 | 0.250 | 1.42 |
|  | D2 | 90 | 24 | 0.0169 | 1.234 | 10 | 0.250 | 1.70 |
|  | D3 | 90 | 30 | 0.0211 | 1.542 | 12 | 0.250 | 1.78 |
|  | D4 | 135 | 24 | 0.0169 | 1.234 | 7.5 | 0.375 | 1.74 |
|  | D5 | 135 | 30 | 0.0211 | 1.542 | 8 | 0.375 | 1.91 |
|  | D6 | 135 | 18 | 0.0127 | 0.925 | 20 | 0.375 | 1.45 |
|  | D7 | 180 | 30 | 0.0211 | 1.542 | 6 | 0.500 | 1.95 |
|  | D8 | 180 | 18 | 0.0127 | 0.925 | 13.3 | 0.500 | 1.51 |
|  | D9 | 180 | 24 | 0.0169 | 1.234 | 15 | 0.500 | 1.63 |

Table S2. Relative single-cycle damage vs $\Delta P/\mathrm{MAOP}$ ($\mathrm{SCF}_P = 1.95$, $\sigma_h = 349.2$ MPa).

| $\Delta P/\mathrm{MAOP}$ | $S_a$ (MPa) | $N_i$ | Cycles equal to one full-MAOP cycle |
|------|------|------|------|
| 100% | 174.6 | 396 | 1 |
| 80% | 139.7 | 1.21×10³ | 3 |
| 50% | 87.3 | 1.27×10⁴ | 32 |
| 20% | 34.9 | 1.23×10⁶ | 3,134 |
| 10% | 17.5 | 3.91×10⁷ | 98,862 |
| 5% | 8.7 | 1.27×10⁹ | 3,255,554 |

Table S3. Single full-MAOP cycle: $N_f$ and unit damage (D7 configuration, $C' = 1126$ MPa, $S_a = 174.6$ MPa).

| OD | $\mathrm{SCF}_P$ (D7) | $N_f$ | $d_i$ ($n = 1$) | $t_{\mathrm{est}}$ (yr) |
|----|------|------|------|------|
| 56″ | 1.95 | 396 | 2.53×10⁻³ | 396 |
| 48″ | 2.14 | 249 | 4.02×10⁻³ | 249 |
| 36″ | 2.37 | 149 | 6.70×10⁻³ | 149 |

![Fig. S1. Structured quadrilateral mesh quality; element aspect ratio ≤ 3 throughout.](C:/Users/zduna/Desktop/Korc/Docs/paper/figures/sf1_mesh_quality.png){width=12cm}

![Fig. S2. Schematic geometry-ILI radius map and extraction of the representative FEA ripple parameters (*L*, *d*, θ/*aC*).](C:/Users/zduna/Desktop/Korc/Docs/paper/figures/sf2_caliper_to_fea.png){width=12cm}

![Fig. S3. Full stress-component contour set at the ripple: (a) von Mises, (b) S11 circumferential, (c) S22 axial.](C:/Users/zduna/Desktop/Korc/Docs/paper/figures/sf3_stress_contours.png){width=15cm}
