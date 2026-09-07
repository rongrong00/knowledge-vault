---
title: Research Exam
type: project
tags: [project, exam, astro/galaxies, sim/TNG, sim/lumina]
status: active
started: 2026-09-02
paper: "The Lumina Project: The Assembly-History Origin of Galaxy Disk Sizes across Cosmic Time"
source: "~/Desktop/CosmoSim/The_Lumina_Project__The_Assembly_History_Origin_of_Galaxy_Disk_Sizes_across_Cosmic_Time (2)/main.tex"
draft_date: 2026-09-02
---

# Research Exam — complete technical reference

**Part I** lays out the paper: every choice, every step, every number, in pipeline order.
**Part II** is the background a committee opens with — disk formation, size measurement,
resolution, the galaxy-formation model, radiative transfer, stellar populations and dust.

---

# Part I · The paper

## 1 · The claim, in the draft's own register

> Galaxy size retains information about the halo's assembly history beyond what its
> present-day properties contain — in particular the spin the halo carried when the
> disk's material was acquired.

The draft is hedged on purpose: it *tests whether* the weak spin–size correlation is a
timing mismatch; finds that sizes *can retain* information about past spin; and that an
acquisition-weighted spin history *correlates more strongly* with size than instantaneous
spin. Use that register — "suggests", not "shows".

**The 60-second version.** Mo, Mao & White (1998): a disk inherits its halo's angular
momentum, so $R\propto\lambda R_{\rm vir}$. Simulations keep finding this weak. Sweeping
the epoch at which spin is measured, the size–spin correlation peaks at a *nonzero*
lookback time — $\simeq1.3$–$1.4\times$ the sample's median stellar age at every anchor
from $z=1$ to $5$. Stars inherit angular momentum from gas accreted before they formed,
so the disk remembers a spin the halo no longer has. An SFH-weighted spin history
evaluated 15% of a cosmic time early ($\Lambda_{\rm eff}$) is the strongest halo-based
predictor in both simulations. Earlier-forming halos host larger galaxies through an
independent channel. On the stellar side, accreted stars build extended envelopes while
compaction-driven in-situ growth builds dense cores, inverting the intrinsic mass–size
relation at $z\gtrsim2$ — but in projected, dust-extincted light the relation flips back
to positive over most of the observed range.

## 2 · The simulations

| | Lumina | Lumina-DM | TNG100-1 |
|---|---|---|---|
| Box | 500 cMpc (338.3 $h^{-1}$) | same | 110.7 cMpc (75 $h^{-1}$) |
| $N_{\rm gas}$, $N_{\rm dm}$ | $6000^3$, $6000^3$ | —, $3000^3$ | $1820^3$, $1820^3$ |
| $m_{\rm b}$ | $3.6\times10^6M_\odot$ | — | $1.4\times10^6M_\odot$ |
| $m_{\rm dm}$ | $1.9\times10^7M_\odot$ | $1.8\times10^8M_\odot$ | $7.5\times10^6M_\odot$ |
| $\epsilon_{\rm coll}$ | 1.77 ckpc | 1.77 ckpc | 1.48 ckpc ($z>1$); 0.74 pkpc ($z\le1$) |
| $\epsilon_{\rm gas,min}$ | 0.44 ckpc | — | 0.19 ckpc |
| $z_{\rm init}\to z_{\rm final}$ | 49 → 3 | 49 → 0 | 127 → 0 |
| Code | AREPO + AREPO-RT | GADGET-4 | AREPO |

Both hydro runs use the **same IllustrisTNG galaxy-formation model** (§9). TNG100-1
provides $z\le3$ and overlaps Lumina at $z=3$; it has no RT — optically thin, spatially
uniform, redshift-dependent UV background (Faucher-Giguère+09), cooling in ionization
equilibrium with self-shielding (Rahmati+13, Wiersma+09). Lumina-DM shares Lumina's
initial conditions and random phases.

**Why this pair.** Lumina holds **over 70,000 halos in the primary mass bin at $z=3$ and
still a few hundred at $z=7$**, at a resolution that supports morphology and size
measurements. TNG100 alone is too small a volume for high-$z$ statistics; TNG300 and
MillenniumTNG are too coarse for structural measurements. The two are checked to overlap
in galaxy properties at $z=3$.

**Lumina's departures from fiducial TNG** (full detail §10): non-equilibrium
thermochemistry coupled to on-the-fly RT instead of equilibrium primordial cooling; total
gas metallicity only; a shortened gas depletion time at $z>4.75$ (reverting to the
calibrated TNG value at $z\le4.75$); no magnetic fields.

## 3 · The pipeline, step by step

### 3.1 Halo finding and selection
- Friends-of-friends groups; subhalos with **SUBFIND** (Springel+01, Springel+21).
- **Central** = the subhalo with the largest total bound mass in its FoF group.
- **Galaxy center** = position of the central's most bound particle; all particle
  positions recentered on it.
- $M_{200c}$ = mass inside the sphere whose mean density is $200\rho_{\rm crit}$;
  $R_{200c}$ defined from it and used as the virial radius throughout.
- **Two halo-mass bins**, chosen to balance resolution against statistics:
  $10^{11.8}\le M_{200c}\le10^{12.2}M_\odot$ (MW-mass; well resolved and populated
  $z=0$–$7$) and $10^{12.3}\le M_{200c}\le10^{12.7}M_\odot$ (tests mass dependence).

### 3.2 Halo spin
$$\lambda=\frac{j_{\rm dm}}{\sqrt2\,V_{200c}R_{200c}},\qquad V_{200c}=\sqrt{\frac{GM_{200c}}{R_{200c}}}$$

$j_{\rm dm}$ is the **specific** angular momentum of the dark matter inside $R_{200c}$;
$V_{200c}$ is the circular velocity from the **total** mass. Bullock's form is used
because it needs only enclosed mass, radius and angular momentum; the Peebles definition
$\lambda_P=J|E|^{1/2}/(GM^{5/2})$ needs the total binding energy.

### 3.3 The disk frame and circularity (two passes)
1. Subtract the mass-weighted mean stellar velocity.
2. Preliminary axis: angular momentum of stars inside a spherical aperture of
   $0.1R_{200c}$.
3. For each star, $j_z$ along that axis and $E=\tfrac12v^2+\Phi(r)$, where $\Phi(r)$ is
   built by taking the **median catalogued potential of bound star particles in radial
   bins and fitting a spline in $\log r$** — no separate potential solve.
4. Circularity $\epsilon=j_z/j_c(E)$, with $j_c(E)=r_c(E)\,v_c(r_c(E))$,
   $v_c(r)=\sqrt{r\,\mathrm{d}\Phi/\mathrm{d}r}$, and $r_c(E)$ from inverting
   $E=\tfrac12v_c^2(r_c)+\Phi(r_c)$. $\epsilon=1$ is a circular orbit in the disk plane;
   $\epsilon\simeq0$ has little net rotation about the axis.
5. Disk stars: $\epsilon>0.7$. **Recompute** the angular momentum from those stars only —
   that direction is the final disk normal. Rotate all stellar positions and velocities.

### 3.4 Rotational support and morphology
$$\kappa_{\rm rot,\star}=\frac{\sum_i\frac12m_iv_{\phi,i}^2}{\sum_i\frac12m_iv_i^2}$$
over all stars bound to the central inside $0.1R_{200c}$, velocities in the disk frame
(Sales+12). **Disk-dominated if $\kappa_{\rm rot,\star}>0.5$** (Du+20, Yang+22), confirmed
by visual inspection of face-on and edge-on surface-density maps. No Sérsic or bulge–disk
decomposition — morphology is purely kinematic.

### 3.5 Sizes and stellar masses
- **Primary size:** $R^{\rm 3D}_{1/2,\star}$, the radius enclosing half the subhalo's
  bound stellar mass. The 2D projected half-mass radius in the disk frame agrees to
  $\sim10\%$; 3D is kept for consistency with Genel+18.
- **$M_\star$ for the mass–size relation:** within $2R_{1/2}$, matching Genel+18.
- **$M_\star$ for every assembly-history analysis:** total bound stellar mass, so the
  control variable cannot depend on the size being predicted.

### 3.6 The three samples
| Analysis | Sample |
|---|---|
| Mass–size | every central in the halo-mass selection |
| Spin–size, disk classification, all assembly-history work | centrals with $\kappa_{\rm rot,\star}>0.5$ **and** $M_\star\ge3.6\times10^9M_\odot$ |
| Light-weighted | **star-forming centrals, no morphological cut** — to match observed samples |

- The $3.6\times10^9M_\odot$ floor = **1000 star particles in Lumina** (~2570 in TNG100),
  so the kinematics are resolved.
- **Star-forming:** sSFR no more than 0.5 dex below the SFMS ridge. The ridge is the
  running median of $\log$ sSFR in 0.2-dex $M_\star$ bins, refit iteratively after
  dropping galaxies $>0.5$ dex below it until convergence — so quenched galaxies cannot
  drag the high-mass ridge down (Donnari+19).

### 3.7 Light: from star particles to $R_{\rm eff}$
1. **SED per star particle** from its age and metallicity: **BPASS v2.2.1 with binary
   evolution** (Stanway & Eldridge 2018), **Chabrier (2003) IMF**.
2. **Two rest-frame bands:** 1500 Å (traces recent SF; close to HST/JWST size bands —
   Shibuya+15, Miller+25) and Johnson $V$ (closer to van der Wel+14 optical sizes and the
   rest-optical JWST sizes of Miller+26).
3. **Project face-on** in the disk-aligned frame.
4. **Background:** in a projected annulus at **21–24 pkpc**, take the **median surface
   density over eight concentric sub-annuli** — so a satellite falling in the annulus
   cannot bias it. Subtract this from the cumulative light profile.
5. **Curve of growth:** $R_{\rm eff}$ = projected radius enclosing half the
   background-subtracted light **within a 20 pkpc aperture**, following the observational
   procedure. Circularized (radius of enclosed light, not semi-major axis).

Done for every galaxy in both simulations, intrinsic and dust-extincted.

### 3.8 Dust: from gas columns to extincted $R_{\rm eff}$
Follows the **resolved dust model of Vogelsberger+20 (Model B)**.
1. **Dust is traced by metals** in star-forming gas and cold gas ($T<8000$ K).
2. **Per star $i$**, integrate along the line of sight to the observer: the hydrogen
   column $N_{{\rm H},i}$ and the column-averaged gas metallicity $Z_{{\rm g},i}$.
3. **$V$-band optical depth:**
$$\tau_{V,i}=\tau_{\rm dust}(z)\left(\frac{Z_{{\rm g},i}}{Z_\odot}\right)\left(\frac{N_{{\rm H},i}}{N_{\rm H,0}}\right),\qquad Z_\odot=0.0127,\; N_{\rm H,0}=2.1\times10^{21}\,{\rm cm^{-2}}$$
   with **one free normalization $\tau_{\rm dust}(z)$ per redshift** (Nelson+18,
   Vogelsberger+20).
4. **Screen, not slab.** Because each star's column uses only the gas in front of it, the
   star–dust geometry is explicit, so every resolved column is treated as a **pure
   extinction screen**: $A_{V,i}=1.086\,\tau_{V,i}$. This is a deliberate departure from
   Vogelsberger+20's mixed-slab attenuation, and the justification is the resolved
   geometry.
5. **Wavelength dependence:** Calzetti+00 curve $k(\lambda)$ with the Kriek & Conroy
   (2013) 2175 Å feature: $A_{\lambda,i}=A_{V,i}\,k(\lambda)/R_V$, $R_V=4.05$.
6. **Birth clouds:** stars younger than **10 Myr** get an additional screen for their
   unresolved natal cloud (Charlot & Fall 2000) — optical depth **twice the galaxy mean**,
   with a shallow power-law wavelength dependence (Vogelsberger+20).
7. Remeasure the half-light radii from the extincted luminosities.
8. **Calibrate $\tau_{\rm dust}(z)$** so the simulated dust-extincted rest-1500 Å
   **luminosity function** matches the observed one: Moutard+20 ($z=0$–$2$), Adams+23
   ($z=3$–$5$), Bouwens+21 ($z=6$), Varadaraj+26 ($z=7$). The normalization is fixed by the
   LF, not by sizes — sizes are then a prediction.

### 3.9 Statistics
- **Spearman $\rho$** everywhere: monotonic association, no functional form assumed.
- **68% intervals:** bootstrap the galaxies **1000×**, take the 16th–84th percentiles.
- **Partial Spearman:** rank-transform every variable; regress the ranked target and the
  ranked predictor **separately** on the ranked controls; correlate the two residual
  vectors. The **complete estimator** is bootstrapped 1000×.

### 3.10 Merger trees and the ex-situ fraction
- **$f_{\rm ex}$** = fraction of stellar mass accreted from other galaxies
  (Rodriguez-Gomez+16).
- **TNG100:** the **SubLink** merger trees (Rodriguez-Gomez+15) and the **stellar
  assembly catalogs** of the IllustrisTNG data release (Nelson+19).
- **Lumina:** merger trees **built in post-processing from the SUBFIND catalogs**. Each
  star is classified by whether it **belonged to the main progenitor of its current host
  in the first snapshot after formation** — if yes, in-situ; if not, ex-situ.
- Typical $f_{\rm ex}$ is **lower in Lumina** than in TNG100, yet the size–$f_{\rm ex}$
  partial correlation is *stronger* there: a small accreted component at large radius
  leaves a large size signal.

### 3.11 Spin histories and the sweep
- For every MW-mass central at each anchor (**TNG100: $z=0,1,2,3$; Lumina: $z=3,4,5$** —
  seven anchors), follow the **main-progenitor branch** and **recompute the Bullock spin
  from the dark-matter particles within $R_{200c}$ at each earlier snapshot** — particle
  data, not catalog values.
- **Controls throughout: $C=(\log M_{200c},\log M_\star,f_{\rm ex})$**, all held fixed.
- **The sweep:** $\rho(R,\lambda_{\rm halo}(t_{\rm lb})\,|\,C)$ as a function of lookback
  time $t_{\rm lb}$ before the anchor. Diamonds = instantaneous, stars = peak. The right
  panel rescales the lookback axis by each sample's **median stellar age**.

### 3.12 $\Lambda_{\rm eff}$
$$\Lambda_{\rm eff}(\beta)=\frac{\sum_i m_i\,\lambda[(1-\beta)\,t_i]}{\sum_i m_i}$$
- $m_i$ = **in-situ** stellar mass formed at cosmic time $t_i$; $\lambda(t)$ **linearly
  interpolated in cosmic time** between main-progenitor snapshots.
- $\beta$ = the fraction of cosmic time by which angular-momentum acquisition precedes
  star formation. Evaluated on a **grid $0$–$0.35$ in steps of $0.025$**; the value
  maximizing the **unweighted mean partial correlation over the four TNG100 anchors
  ($z=0$–$3$)** is chosen. The maximum is broad, at **$\beta=0.15$**, and is **applied to
  Lumina without refitting**.
- Compared against instantaneous spin, the spin at the single best past snapshot, and the
  unlagged average ($\beta=0$) on **identical samples** at all seven anchors.

### 3.13 Formation time and concentration
- **$z_{\rm form}$:** epoch at which the main progenitor first reached **half its anchor
  mass** (Wechsler+02). Correlated with residual size at fixed $C$.
- **Concentration (appendix):** fit an **NFW profile** to each MW-mass central's dark
  matter, $c=R_{200c}/r_s$. Tested against $z_{\rm form}$ with $C$ as control, both ways.

### 3.14 Compaction tracks
- **TNG100:** ten compact and ten extended galaxies **selected at $z=3$, matched in halo
  mass**; follow their medians back.
- **Lumina:** the same, selected at $z=6$ (solid) and $z=3$ (dashed), $N=10$ per
  population and anchor.
- Panels: $R_{1/2,\star}$; **$\Sigma_1=M_\star(<1\,{\rm pkpc})/(\pi\,{\rm kpc}^2)$**;
  $M_{200}$; $M_\star$; gas fraction; halo spin. Bands are 16–84th percentiles.

## 4 · Results — every number

**Spin distribution.** Approximately lognormal at every redshift (Bullock+01, Zjupa+16),
peak near $\lambda\sim0.03$–$0.04$, little shape evolution. The $z=0$ overlay is Zjupa &
Springel's Illustris-Dark SO fit, **rescaled to the Bullock convention by a factor 1.1**.
Hydro Lumina halos sit at slightly higher spin than Lumina-DM at fixed $z$ — a few-percent
baryonic effect (Bryan+13).

**Spin–size, instantaneous.** MW-mass disks: $\rho=+0.27$ to $+0.37$, flat in $z$;
reproduces Desmond+17, Jiang+19 and extends to $z=7$. High-mass bin: $-0.14$ at $z=0$,
$\simeq+0.3$ at $z=2$–$5$ — mergers and continued accretion in massive low-$z$ halos
redistribute angular momentum and erase the mapping; colder high-$z$ disks stay closer to
halo spin.

**Mass–size, intrinsic.** $\rho=+0.45$ at $z=0$ (Shen+03; agrees with Genel+18 TNG100),
weakens through $z=1$–$2$, reverses, reaches $-0.66$ at $z=7$. Lumina and TNG100 trace the
same relation at $z=3$. Marshall+22 (BlueTides, $z=7$–$8$) and Roper+22,23 (FLARES, $z\ge5$)
report the same intrinsic inversion.

**Mass–size in light** (star-forming centrals).

| Measure | $z=0$ | trend |
|---|---|---|
| 3D half-mass | $+0.45$ | inverts by $z\simeq1.5$; $-0.66$ at $z=7$ |
| Intrinsic rest-UV | $+0.34$ | $\Delta\rho\simeq+0.2$–$0.3$ above mass-weighted at $z\ge2$, still turns over: $-0.29$ at $z=7$ |
| Dust-extincted rest-UV | $\simeq+0.4$ ($z\le2$) | $+0.1$ at $z=5$, flat at $z=6$, mildly negative at $z=7$ |
| Rest-$V$ | same pattern | turns negative ~2 bins earlier ($z\ge5$) — weaker optical extinction |

Light-weighting flattens because young stars extend beyond the old core; dust reverses
because it sits in the metal-rich compact cores of the most massive galaxies (Vijayan+24)
and moves their half-light radii outward. FLARES and BlueTides show the same dust-driven
reversal (Roper+22, Marshall+22); ASTRID mock-JWST slopes are flat-to-positive at
$z=3$–$6$ (LaChance+25); the wavelength dependence matches FLARES (Punyasheel+25).

Against **Miller+26** (JWST rest-5000 Å, $0.5<z<8$, $\simeq0.2$ dex scatter): medians within
the scatter at $z=1$–$4$ at every mass; slightly high at $z=1$–$2$; cross below at the
massive end where the simulated median flattens; **deficit $\simeq0.3$ dex by $z=5$–$6$ for
$M_\star\gtrsim10^{10.5}M_\odot$**. Caveats: circularized curve-of-growth vs their Sérsic
radii differ at the $\sim0.1$ dex level; extincted profiles are not mock images
(Costantin+23, Ceverino+26). Observations are not uniformly positive either: flattening
above $10^{10}M_\odot$ toward $z\sim5$ (Chen+26), tentative negative slopes for bright
$z=5$ rest-UV (Varadaraj+24) and $8<z<9$ rest-optical (Yang+25).

**Residual rest-UV tension.** At $z=6$ and $7$ the median extincted rest-UV half-light
radius is **$\simeq2\times$ the Shibuya+15 size–luminosity relation at $M_{\rm UV}=-20$**
($M_{\rm UV}$ from the SFR), growing toward fainter magnitudes — same sign as Shen+24 for
Thesan, smaller amplitude.

**Residual drivers at fixed $(M_{200c},\lambda)$.**
- $\rho(R,f_{\rm ex}|M_{200c},\lambda)=+0.45$–$0.55$ over $z=0$–$3$ — stronger than the
  dependence on spin itself. Lumina: $+0.53$ at $z=3$ → $+0.70\pm0.05$ at $z=7$.
  High-$f_{\rm ex}$ galaxies also sit at the upper right of the unconditioned plane because
  $f_{\rm ex}$ correlates with normalized size and, weakly, with spin.
- $\rho(R,M_\star|M_{200c},\lambda)$: $+0.27$ at $z=0$ → $-0.75$ at $z=7$. Same halo mass
  and spin, more stars → larger at low $z$, more compact at high $z$.

**Spin memory.** At every anchor in both sims the sweep rises above its instantaneous
value, peaks, declines. Gain $\Delta\rho\simeq0.09$–$0.34$. Peak lookback $\simeq0.25$ Gyr
at $z=5$ → $\simeq5$ Gyr at $z=0$; both sims agree at $z=3$. Normalized: peaks at
**$1.36$–$1.47$ (Lumina), $\simeq1.2$–$1.3$ (TNG100)** over $z=1$–$5$ — the gray band is
$1.2$–$1.5$. At $z=0$ a broad plateau, smaller gain: once SFHs are old and extended no
single epoch stands out.

**$\Lambda_{\rm eff}$.** Partial $\rho=+0.50$ to $+0.60$ at every anchor; several times the
instantaneous coefficient at high $z$, and above the spin at any single past snapshot. Raw
size–$\Lambda_{\rm eff}$ correlation $+0.62$ to $+0.70$, roughly twice instantaneous.
Unlagged $\beta=0$ wins only where SFHs are extended ($z\le2$, clearest at $z=0$). The lag
$\simeq$ 1–2 virial dynamical times ($t_{\rm dyn}=r_{200}/V_{200}\simeq0.1H^{-1}$ at every
epoch and mass) — an imprint at halo entry, where tidal torquing ends.

> **For modellers:** present-day spin underpredicts the size–spin correlation by
> **1.5× at $z=0$ and 5.7× at $z=5$**.

**Formation time.** At fixed $C$, earlier-forming halos host larger galaxies (agrees with
Somerville+26). $\rho(R,z_{\rm form}|C)$: $\simeq0$ at $z=0$; $+0.21$, $+0.31$, $+0.36$ at
TNG $z=1,2,3$; $+0.44$, $+0.47$, $+0.48$ at Lumina $z=3,4,5$ (up to $+0.54$ by $z=7$).
Controlling $M_\star$ and $f_{\rm ex}$ is essential — early-forming halos have more stars
and less ex-situ material, which masks the trend otherwise. Secondary in the high-mass bin.

**Concentration (appendix).** At fixed $M_{200c}$ alone, $\rho(\log R,\log c|\log M_{200c})
=-0.22$ to $-0.26$ over $z=3$–$5$, slope $\mathrm{d}\log R/\mathrm{d}\log c=-0.38$ to
$-0.44$ (shallower than Jiang+19's $R_e\simeq0.02(c/10)^{-0.7}R_{\rm vir}$, fit over a
wider range). At fixed $C$: $-0.06\le\rho\le+0.16$, unchanged by adding $z_{\rm form}$;
adding $c$ shifts the $z_{\rm form}$ coefficient by $\le0.04$. Concentration encodes
formation history (Wechsler+02, Ludlow+14) and adds nothing beyond it here.

**Compaction.** TNG100: $\Sigma_1$ tracks separate at **$z\sim8$**; half-mass radii stay
similar until **$z\sim6$** — the size difference lags central-density growth by several
hundred Myr. Compact systems then deplete gas and reduce SF; extended ones stay gas-rich.
Lumina ($z=6$ selection): central densities already differ at the earliest resolved
epochs; radii separate near $z\sim7$; compact galaxies reach half their anchor $M_\star$
earlier, have lower gas fractions at selection, **nearly identical current halo spins but
lower spins at earlier epochs**. The $z=3$ selection shows the same ordering.

## 4b · The figures — what is on each, and what to say

For every figure: what is plotted, how to read it, the one line to land on. Panels run
$z=0$ (top left) to $z=7$ (bottom right) unless stated; TNG100 is **blue**, Lumina **pink**;
running median solid, 16–84th percentile dashed or shaded; $N$ and Spearman $\rho$
annotated per panel with 68% bootstrap intervals.

**Fig 1 — Spin distribution** (`spin_distribution_mwmass`). $P(\lambda)$ for all halos
$M_{200c}>10^{11.8}M_\odot$; Lumina, Lumina-DM (orange), TNG100. The $z=0$ panel overlays
Zjupa & Springel's Illustris-Dark lognormal, rescaled ×1.1 to Bullock's convention.
*Say:* "Lognormal, peak 0.03–0.04, essentially no evolution — a check that the halo
finder and definition behave. The hydro runs sit a few percent above DM-only."

**Fig 2 — Spin–size, MW-mass** (`spin_size_M11.8-12.2_noband`). $R^{\rm 3D}_{1/2}/R_{200c}$
vs $\lambda$ for disks ($\kappa_{\rm rot}>0.5$, $M_\star\ge3.6\times10^9$). *Say:* "Positive
at every redshift, as MMW predict, but $\rho=0.27$–$0.37$ and flat in $z$ — the weak
correlation everyone finds, now extended to $z=7$."

**Fig 3 — Spin–size, high-mass** (`spin_size_M12.3-12.7`), $z=0$–$5$. *Say:* "$-0.14$ at
$z=0$, $+0.3$ at $z=2$–$5$: mergers in massive low-$z$ halos erase the mapping."

**Fig 4 — Mass–size, intrinsic** (`mass_size_8panel`). $R^{\rm 3D}_{1/2}$ vs $M_\star$ for
**centrals in halos $M_{200c}\ge10^{11}M_\odot$** — a wider selection than the two analysis
bins. Black squares: Genel+18 at $z\le3$. *Say:* "$+0.45$ at $z=0$, matching Genel;
weakens through $z=1$–$2$, inverts, $-0.66$ by $z=7$. Lumina and TNG100 agree at $z=3$."

**Fig 5 — $\rho(R,M_\star)$ vs $z$** (`rho_size_vs_z`). One panel. Black = 3D half-mass;
red = rest-$V$; blue = rest-UV; dashed intrinsic, solid dust-extincted; star-forming
sample. Shaded band: $z\le8$ where observations report a positive slope. *Say:* "This is
the whole light story in one plot. Mass-weighted inverts by $z\simeq1.5$. Intrinsic light
lifts it 0.2–0.3 but still inverts. Dust-extincted UV stays positive to $z\sim5$."

**Fig 6 — Rest-UV mass–size** (`mass_size_light_uv`). Rest-1500 Å half-light radius vs
$M_\star$, star-forming centrals. Solid + shaded = extincted; dashed = intrinsic; dotted
grey = 3D half-mass for reference; $\rho_{\rm ext}$ and $\rho_{\rm intr}$ annotated. *Say:*
"Watch the dashed line sit above the grey one — that's light-weighting — and the solid
above the dashed — that's dust pushing the massive end out."

**Fig 7 — Rest-$V$ mass–size** (`mass_size_light_v`). Same, Johnson $V$; black line +
grey band = Miller+26 JWST rest-5000 Å relation with its 0.2 dex scatter over $0.5<z<8$,
$M_\star\le10^{11}$; the massive end at $z\ge5$ is their extrapolation. *Say:* "Inside the
scatter at $z=1$–$4$; we flatten at the massive end where they keep rising; 0.3 dex low by
$z=5$–$6$ above $10^{10.5}$."

**Fig 8 — Residual: ex-situ** (`spin_size_exsitu_2x4`). Fig 2's plane coloured by
$f_{\rm ex}$; TNG100 $z\le2$, Lumina $z\ge3$; colour scale spans the central 96% of each
panel's $f_{\rm ex}$; partial $\rho(R,f_{\rm ex}|M_{200c},\lambda)$ annotated. *Say:* "High
$f_{\rm ex}$ collects at the upper right. Partial correlation $+0.45$–$0.55$, stronger than
spin itself, and rising to $+0.70$ in Lumina at $z=7$ even though $f_{\rm ex}$ is lower there."

**Fig 9 — Residual: stellar mass** (`spin_size_mstar_4x2`). Coloured by $M_\star$, $z=0$–$7$.
*Say:* "The partial coefficient flips sign: $+0.27$ at $z=0$, $-0.75$ at $z=7$. Same halo,
same spin, more stars → more compact at high $z$. This is the inversion in residual form."

**Fig 10 — Spin memory** (`spin_memory_sweep_2panel_mock`) — **the central figure.** Left:
partial $\rho(R,\lambda(t_{\rm lb})|C)$ vs lookback time, one curve per anchor; diamonds =
instantaneous, stars = peak; shaded 68% bootstrap. Right: lookback axis divided by each
sample's median stellar age; grey band 1.2–1.5. *Say:* "Every curve rises from the
diamond to a star at nonzero lookback, then decays. The peak moves from 0.25 Gyr at $z=5$
to 5 Gyr at $z=0$. Divide by stellar age and they line up — except $z=0$, which is a
plateau." *Note the filename says `mock`; be ready to say the sweep is real output.*

**Fig 11 — Predictor ladder** (`predictor_ladder`). Partial $\rho$ at fixed $C$ for four
spin predictors at all seven anchors: instantaneous $\lambda$; the best single past
snapshot; unlagged $\Lambda_{\rm eff}(\beta=0)$; lagged $\Lambda_{\rm eff}(\beta=0.15)$.
$\beta$ from TNG100 only. *Say:* "The lagged history wins at every anchor, $+0.50$ to
$+0.60$. Unlagged wins only at $z\le2$ where SFHs are extended. It beats the best single
snapshot, so the weighting matters, not just the lag."

**Fig 12 — $\Lambda_{\rm eff}$–size** (`leff_size`). $R/R_{200c}$ vs $\Lambda_{\rm eff}(0.15)$
for MW-mass disks, $z=0$–$7$. *Say:* "Raw $\rho=+0.62$–$0.70$, about twice Fig 2. Same
galaxies, same sizes — only the spin was read at a different time."

**Fig 13 — Formation time** (`size_vs_zform`). Residual size at fixed $C$ vs $z_{\rm form}$,
one panel per anchor. *Say:* "Earlier-forming halos host larger galaxies once you control
$M_\star$ and $f_{\rm ex}$; zero at $z=0$, $+0.36$ at $z=3$, up to $+0.5$ in Lumina. Without
those controls it's masked, because early formers have more stars and less accretion."

**Fig 14 — Compaction tracks, TNG100** (`compaction_trace_sigma1`). Ten compact (green)
vs ten extended (orange) MW-halo-mass galaxies selected at $z=3$, matched in halo mass;
six panels: $R_{1/2}$, $\Sigma_1$, $M_{200}$, $M_\star$, $f_{\rm gas}$, $\lambda$; 16–84
bands. *Say:* "$\Sigma_1$ separates at $z\sim8$; sizes don't separate until $z\sim6$.
Central density first, size second, gas depletion third — the compaction ordering."

**Fig 15 — Compaction tracks, Lumina** (`lumina_compaction_trace`). Same panels; solid =
$z=6$ selection, dashed = $z=3$. *Say:* "Same ordering where the inversion is strongest.
And look at the spin panel: identical today, lower in the past for the compact ones —
the memory result seen in individual histories."

**Table 1** — the simulation parameters (§2). **Table 2** — concentration vs formation
time partials (appendix): $c$ adds $\le0.16$ at fixed $C$ and moves the $z_{\rm form}$
coefficient by $\le0.04$.

## 5 · Definitions cheat-list

$M_{200c},R_{200c}$ · $\lambda=j_{\rm dm}/(\sqrt2V_{200c}R_{200c})$ · $\epsilon=j_z/j_c(E)$,
disk $>0.7$ · $\kappa_{\rm rot,\star}$ in $0.1R_{200c}$, disk $>0.5$ · $R^{\rm 3D}_{1/2,\star}$ ·
$M_\star(<2R_{1/2})$ vs total bound · $R_{\rm eff}$ = half of background-subtracted light in
20 pkpc · $\tau_V$, $A_V=1.086\tau_V$, $R_V=4.05$ · $f_{\rm ex}$ · $C=(\log M_{200c},\log
M_\star,f_{\rm ex})$ · $\Lambda_{\rm eff}(\beta=0.15)$ · $z_{\rm form}$ = half anchor mass ·
$c=R_{200c}/r_s$ · $\Sigma_1$ · floor $3.6\times10^9M_\odot$ = 1000 particles.

---

# Part II · Background

## 6 · Disk formation — the pictures

### 6.1 Where halo angular momentum comes from
**Tidal torque theory** (Hoyle 1949; Peebles 1969; Doroshkevich 1970; White 1984): a
protohalo acquires angular momentum from the tidal field of neighbouring density
perturbations while it is still growing in the linear/quasi-linear regime. For a
**non-spherical** protohalo the first-order torque is nonzero and $J$ grows $\propto t$
(i.e. $\propto a^{3/2}$ in Einstein–de Sitter) — Doroshkevich (1970), White (1984).
Peebles (1969) treated a spherical Lagrangian region, for which the first-order term
vanishes and growth is only second-order, $J\propto t^{5/3}$; his lasting contribution
is the **freeze-out at turnaround**. The result is a spin parameter that is **small**
(Bullock+01: lognormal with $\lambda'_0=0.035\pm0.005$, $\sigma=0.5\pm0.3$) and nearly
**independent of halo mass and redshift** (Bett+07; Macciò+07, 08) — which is exactly
what the spin-distribution figure checks.

**Why it is small.** In tidal torque theory
$$J_i\;\propto\;a^2\dot D\;\epsilon_{ijk}\,T_{jl}\,I_{lk},$$
the antisymmetric product of the tidal tensor $T$ and the protohalo's inertia tensor $I$
— only their *misaligned* part torques (Lee & Pen 2000). Torques act only while the region
grows linearly and shut off at turnaround, so the halo never approaches rotational
support: a few percent of the angular momentum it would need.

**Why it is independent of mass and redshift.** $\lambda$ is self-similar by construction.
In TTT $J\propto M^{5/3}$ for the Lagrangian mass, and a virialized halo has
$E\propto GM^2/R\propto M^{5/3}$, so $\lambda\propto M^{5/3}M^{5/6}M^{-5/2}=M^0$. In
Bullock's form $j\propto M^{2/3}$, $V\propto M^{1/3}$, $R\propto M^{1/3}$ → $\lambda'\propto
M^0$. The $\propto t$ growth of $J$ is likewise scaled out by the growth of $M$ and $R$.
Empirically the median drifts by at most tens of percent (Bett+07; Macciò+07, 08).

**Why the shape is lognormal — three steps.**

1. *The empirical fact.* Barnes & Efstathiou (1987) and Bullock+01 fit
$$P(\lambda')\,d\lambda'=\frac{1}{\lambda'\sqrt{2\pi}\,\sigma}\exp\!\left[-\frac{\ln^2(\lambda'/\lambda'_0)}{2\sigma^2}\right]d\lambda',\qquad \lambda'_0=0.035\pm0.005,\ \sigma=0.5\pm0.3.$$
   $\sigma=0.5$ is a factor $e^{0.5}\simeq1.65$ — a 68% range of roughly $0.02$–$0.06$.
2. *Linear theory gives the core.* Each Cartesian component of $J$ is a sum over many
   independent Fourier modes of the tidal field, so by the central limit theorem each
   component is Gaussian with zero mean. The magnitude of a 3D Gaussian vector is
   **Maxwellian** — a $\chi$ distribution with three degrees of freedom, rising as $J^2$ at
   small $J$ and falling as a Gaussian at large $J$. On a log axis that is a nearly
   symmetric bump, which is why it *looks* lognormal in the core.
3. *Nonlinear assembly makes it lognormal.* After turnaround the halo grows by mergers
   and accretion, each changing $J$ by a random **fractional** amount — Vitvitska+02's
   random walk. Multiplicative random changes mean $\ln J$ is a **sum** of random
   increments, so the central limit theorem now acts in log space and drives the
   distribution toward lognormal. More assembly events → closer to lognormal, and the
   walk has no preferred epoch — which is also why the shape does not evolve.

**Why not exactly lognormal.** Bett+07 (Millennium) showed the fit fails at both ends and
proposed
$$P(\lambda)\propto\left(\frac{\lambda}{\lambda_0}\right)^3\exp\!\left[-\alpha\left(\frac{\lambda}{\lambda_0}\right)^{3/\alpha}\right],\qquad \lambda_0\simeq0.043,\ \alpha\simeq2.5.$$
The power-law rise at small $\lambda$ is the fingerprint of the Maxwellian — a 3D random
vector cannot have the super-exponential cutoff at zero that a lognormal has. The honest
one-liner: **lognormal in the core from linear torques plus a merger random walk;
power-law low end from the vector nature of $J$.**

**Where the width comes from.** Two sources: the misalignment angle between $T$ and $I$ in
the initial conditions, and the merger random walk afterwards. The latter is also why the
spin **decorrelates over a few Gyr** (Benson+20) and why its orientation flips, especially
in the inner halo (Bett & Frenk 2012, 2016) — the physical motivation for the sweep
(§6.5). The small hydro-vs-DM offset in Figure 1 is baryons condensing and exchanging
angular momentum with the dark matter (Bryan+13). Standalone note → [[Halo Spin Parameter]].

**The two definitions.** Peebles (1969): $\lambda=J|E|^{1/2}/(GM^{5/2})$ — the ratio of the
halo's angular momentum to what it would need for rotational support. Bullock+01:
$\lambda'=j/(\sqrt2V_{200}R_{200})$ — the same idea evaluated at the virial radius
without computing $E$. For a truncated singular isothermal sphere the two coincide; for
an NFW halo $\lambda'\simeq\lambda\,f_c^{-1/2}$ with MMW's energy factor $f_c$.

### 6.2 Fall & Efstathiou (1980) → Mo, Mao & White (1998)
The founding assumption: gas in a halo shares the halo's specific angular momentum, cools,
and **conserves $j$ as it falls in**, settling where rotational support is reached. Fall &
Efstathiou showed this needs a massive dark halo to give disks of the observed size; MMW
turned it into the standard scaling.

*The derivation you should be able to sketch.* An exponential disk of scale length
$R_d$ and flat rotation $V_c$ has $J_d=2M_dR_dV_c$, so $j_d=2R_dV_c$. Set the disk's
specific angular momentum equal to the halo's: with the Bullock definition
$j_h=\sqrt2\lambda V_{200}R_{200}$, so

$$R_d=\frac{\lambda R_{200}}{\sqrt2}\;(\text{for } V_c=V_{200},\ j_d=m_d)$$

MMW's eq. 28 carries the general factors: $R_d=\frac{1}{\sqrt2}\lambda R_{200}\,(j_d/m_d)f_c^{-1/2}f_R$, where $m_d=M_d/M_{200}$, $j_d=J_d/J_{200}$, $f_c\simeq\tfrac23+(c/21.5)^{0.7}$
corrects the NFW halo's energy relative to isothermal, and $f_R$ absorbs the non-flat NFW
rotation curve together with the disk's self-gravity and the halo's adiabatic
contraction. Their eq. 2, $r_{200}=V_c/(10H)$, is where $t_{\rm dyn}=r_{200}/V_{200}
=0.1H^{-1}$ comes from — exactly, not approximately. With $\lambda\sim0.035$,
$R_d\sim0.025R_{200}$ — and Kravtsov (2013) finds empirically that the stellar
**half-mass** radius follows $R_{1/2}\simeq0.015R_{200}$ (power-law slope $0.95\pm0.07$)
over eight decades of $M_\star$ with $\simeq0.2$ dex scatter, so the picture gets the
*scale* right. The paper's normalized size $R_{1/2}/R_{200c}$ against $\lambda$ is
the direct test of the *spin dependence*.

### 6.3 The angular-momentum problem, and what feedback does
Early SPH simulations (Navarro & Benz 1991; Navarro & Steinmetz 1997, 2000) made disks
**far too small**: gas cooled early into dense clumps, which lost their angular momentum
to the halo by dynamical friction during mergers — "overcooling" / the angular-momentum
catastrophe. The cure was **strong early feedback**: it prevents early overcooling, and it
**preferentially ejects low-$j$ gas** from galaxy centres (Governato+07, 10; Brook+11), so
the gas that eventually forms the disk has *higher* specific angular momentum than the
halo average. This is why feedback is one of the main reasons the halo-spin–size mapping
is not clean — and why it varies between models (Yang+22).

### 6.4 Empirical anchors
- **$j_\star$–$M_\star$** (Fall 1983; Romanowsky & Fall 2012; Fall & Romanowsky 2013):
  two parallel tracks with log-slope $\simeq0.6$ ($0.61\pm0.04$ for disks), close to the
  $2/3$ expected for halos, with ellipticals a factor $\sim5$ below spirals at fixed mass.
  Retention fractions $f_j\simeq0.55$–$0.6$ for disks, $\simeq0.1$ for ellipticals.
  Posti+18 find a single unbroken power law over $7\lesssim\log M_\star\lesssim11.5$ but
  with slope $0.55\pm0.02$ — shallower than $2/3$, a mild tension with pure retention.
- **Kravtsov (2013):** $R_{1/2}\propto R_{200}$ over eight decades in mass — size tracks
  the halo's *radius*, spin scatter is secondary.
- **Halo spin is a weak predictor** in simulations: Desmond+17, Jiang+19 (NIHAO/VELA —
  concentration does better), Yang+22 (strength is model-dependent), Sun+26
  (GIZMO/FIRE-3 isolated runs — concentration again), Liang+26 (ML on TNG50 with matched
  DM-only run, no causal driver).

### 6.5 Why halo spin decorrelates — the physical motivation for the sweep
Halo spin is **not conserved**. It is built by a **random walk** of mergers and accretion
(Vitvitska+02), its magnitude **decorrelates over a few Gyr** (Benson+20), and its
**orientation flips**, especially in the inner halo (Bett & Frenk 2012, 2016). A disk that
formed early therefore remembers a spin its halo no longer has. Prior hints: in EAGLE,
morphology tracks the angular-momentum *history* of the inner halo (Zavala+16); altering
the angular momentum of the baryonic Lagrangian region in the initial conditions changes
the final stellar angular momentum and structure accordingly (Cadiou+22). What was
missing was *when* the spin is imprinted — hence the sweep.

### 6.6 Two-phase assembly and inside-out growth
Massive galaxies assemble in **two phases** (Naab+09; Oser+10; van Dokkum+10): an early,
dissipative, **in-situ** phase ($z\gtrsim2$) that builds a compact core, and a later
phase in which **ex-situ** stars accreted through (mostly minor) mergers are deposited at
large radii and build the extended envelope. This explains how early-type galaxies grow
in size by factors of several since $z\sim2$ with only modest mass growth — inside-out.
The paper's positive $f_{\rm ex}$–size partial correlation is this picture measured
directly, in both simulations, at every epoch.

### 6.7 Compaction — "blue nuggets"
Dekel & Burkert (2014); Zolotov+15; Tacchella+16; Lapiner+23. At high $z$, gas-rich
galaxies fed by violent disk instability, minor mergers, or counter-rotating streams drive
gas to the centre — a **wet compaction** event — building a dense, star-forming core
(**blue nugget**). Central gas is then consumed and expelled; star formation quenches
inside-out; the remnant is a compact **red nugget**. The diagnostic is the central stellar
surface density **$\Sigma_1$** (Barro+17; quenching sets in above
$\log\Sigma_1\simeq9.5$ in $M_\odot\,{\rm kpc^{-2}}$), which rises *before* the size drops — precisely
the ordering the compaction tracks look for: $\Sigma_1$ separates at $z\sim8$, sizes at
$z\sim6$. Because the most massive halos at high $z$ formed earliest, they are the most
likely to have already compactified — which is why the intrinsic mass–size relation
inverts.

### 6.8 Halo assembly history
- **Formation time** $z_{\rm form}$ (Wechsler+02): half-mass epoch of the main progenitor.
- **Concentration encodes it**: NFW $\rho\propto[(r/r_s)(1+r/r_s)^2]^{-1}$, $c=R_{200}/r_s$;
  earlier-forming halos are more concentrated: Wechsler+02 fit $M(a)=M_0\,e^{-2a_c(1/a-1)}$
  and find $c_{\rm vir}=4.1/a_c$, i.e. $c\propto(1+z_{\rm form})$; Ludlow+14 show the full
  *shape* of the accretion history maps onto the profile — $c$ is set by the epoch at
  which the main progenitor's mass equalled the mass now inside the scale radius. This is why the
  appendix finds $c$ redundant once $z_{\rm form}$ is controlled.
- **Assembly bias** (Wechsler & Tinker 2018 review): at fixed mass, halo properties and
  clustering depend on formation history — the general statement of which "size
  remembers assembly" is a galaxy-scale instance.

### 6.9 Size evolution with redshift
Half-light radius at fixed UV luminosity shrinks as $(1+z)^{-m}$ with $m\simeq1.0$–$1.3$
from HST (Oesch+10: $1.12\pm0.17$; Shibuya+15: $1.10\pm0.06$ median, $1.20\pm0.04$ at
fixed $L$) — the paper quotes $-1.2$. van der Wel+14: $R_{\rm eff}\propto M_\star^{0.22}$
for late types, $\propto M_\star^{0.75}$ for early types; evolution at fixed mass
$\propto(1+z)^{-0.75}$ (late) versus $(1+z)^{-1.48}$ (early); scatter $0.16$–$0.19$ dex
for late types. JWST extends to $z\sim12$ with effective radii of a few hundred pc (Ono+23,
Miller+25). The observed star-forming size–mass slope stays positive to $z\sim8$
(Morishita+24, Miller+26); simulations (Shen+24, Thesan) tend to make rest-UV sizes too
large by factors of a few.

## 7 · How you measure a galaxy size

**The ladder, most to least model-dependent:**

| Method | Assumes |
|---|---|
| 3D half-mass radius | a centre — nothing else; not observable |
| 2D projected half-mass | a viewing angle; still mass-weighted |
| Curve-of-growth $R_{\rm eff}$ | a centre, an aperture, a background — **what I use for light** |
| Sérsic fit $R_e$ | a parametric profile |
| Petrosian radius | a fixed surface-brightness ratio (SDSS) |
| Isophotal ($D_{25}$) | an absolute SB threshold — cosmologically dimmed |
| Kinematic scale length | a rotation curve and a disk model |

**Sérsic:** $I(R)=I_e\exp\{-b_n[(R/R_e)^{1/n}-1]\}$, $b_n\simeq2n-1/3$; $n=1$ exponential
disk, $n=4$ de Vaucouleurs; for an exponential disk $R_e=1.678R_d$. Most observational
catalogs report Sérsic $R_e$ (GALFIT/imfit), so curve-of-growth radii carry a $\sim0.1$ dex
methodological offset before any physics.

**The choices that move the answer:**
1. **Mass- vs light-weighted** — at high $z$ this is the sign of the size–mass slope.
2. **Band** — rest-UV traces $\lesssim100$ Myr star formation, rest-optical/IR the
   assembled mass; sizes shrink toward the red (colour gradients).
3. **Dust** — concentrated in compact metal-rich cores, so it pushes $R_{\rm eff}$ out.
4. **Aperture and background** — the 20 pkpc aperture and 21–24 pkpc annulus.
5. **Circularized vs semi-major** — circularized is smaller by $\sqrt{b/a}$.
6. **Projection** — face-on in the disk frame is something observers cannot choose.
7. **Observational realism not included** — PSF, surface-brightness limits, pixelization,
   Sérsic-fit systematics: the gap between an extincted profile and a mock image.

## 8 · What resolution does to sizes and components

Four distinct limits:

**(i) Force resolution.** Structure inside a few softening lengths is untrustworthy;
Plummer-equivalent forces are Newtonian only beyond $\sim2.8\epsilon$. Comoving softenings
scale as $\epsilon/(1+z)$:

| | $z=3$ | $z=5$ | $z=7$ |
|---|---|---|---|
| Lumina ($1.77$ ckpc) | 0.44 pkpc | 0.29 pkpc | 0.22 pkpc |
| TNG100 ($1.48$ ckpc at $z>1$) | 0.37 pkpc | 0.25 pkpc | 0.19 pkpc |

TNG100's $1.48$ ckpc is $1\,h^{-1}$ ckpc, frozen to $0.5\,h^{-1}=0.74$ pkpc below $z=1$
(continuous at the switch). Gas softenings are adaptive, $\epsilon_{\rm gas}=2.5\times$
the cell radius, floored at 0.44 (Lumina) and $0.125\,h^{-1}=0.19$ ckpc (TNG100). Lumina is only $\simeq1.2\times$ coarser — the two are
closely matched, which is part of why the $z=3$ overlap is a fair comparison.

**(ii) Mass resolution.** A half-mass radius from $N$ particles carries $\sim R/\sqrt N$
Poisson noise, but the real risk is the *inner* profile — which is what compaction
changes. Hence $\ge1000$ star particles.

**(iii) Spurious collisional heating.** Discreteness drives energy equipartition: massive
DM particles scatter lighter stars, **artificially puffing up** galaxies (Ludlow+19) and
thickening disks (Ludlow+21). The heating rate scales as $\rho_{\rm DM}m_{\rm DM}/\sigma_{\rm DM}$
— set by the DM particle mass and the local halo, largely *insensitive* to the stellar
particle mass — so it bites hardest in dense, poorly-sampled high-$z$ centres. It biases sizes *upward*, i.e. against an inverted
relation, so it does not manufacture the result. COLIBRE supersamples DM $4\times$ for
this reason → [[Resolution comparison]].

**(iv) The pressure floor.** The effective EOS (§9) sets a minimum disk scale height
independent of softening. A disk cannot be thinner than the EOS permits however fine the
grid; runs with resolved SNe that drop it change inner structure directly. The sharpest
form of "your inner sizes are model-set, not resolved."

**On components.** $\kappa_{\rm rot}$ and $\epsilon$ need a well-sampled velocity field;
under-resolved galaxies look artificially dispersion-supported *and* artificially
extended at once.

**The honest framing.** Simulated sizes are **not** converged in general (TNG50/100/300
differ), and because the subgrid model is calibrated at a given resolution, finer is not
automatically more correct. Lumina–TNG100 agreement at $z=3$ buys robustness across
*volume and resolution at fixed physics* — not a test of the physics.

## 9 · The IllustrisTNG model, component by component

**AREPO:** finite-volume Godunov hydrodynamics on a moving unstructured **Voronoi** mesh
whose generating points follow the flow — quasi-Lagrangian, Galilean-invariant, low
advection error, cells refined/derefined toward a target mass. Gravity: TreePM (octree +
particle mesh).

### The two-phase ISM and the effective equation of state
Above the star-formation threshold — **one physical density, quoted three ways**: the
draft writes $n_{\rm H,SF}=0.106\,{\rm cm^{-3}}$, Pillepich+18 write $n_{\rm H}\simeq0.1$,
Vogelsberger+13 write $0.13\,{\rm cm^{-3}}$ (total nucleons); say "about 0.1 hydrogen
atoms per cm³" — gas is **not** resolved into clouds; it follows Springel & Hernquist
(2003): cold clouds ($T_c\simeq10^3$ K; results insensitive for $T_c\ll10^4$ K) in pressure
equilibrium with a hot ambient phase, exchanging mass by **cloud growth** (radiative
cooling of the hot phase) and **cloud evaporation** (thermal conduction inside supernova
bubbles). Stars form from the clouds; a fraction $\beta$ die immediately as supernovae
(instantaneous recycling; $\beta=0.226$ for TNG's Chabrier IMF, $0.106$ for Salpeter —
note that $0.106$ is *this* number, not a density), returning mass and heat to the hot
phase. Since heating is
tied to the SFR, which is tied to the cold fraction, the system **self-regulates** to a
unique equilibrium at each density; eliminating the phase variables leaves one pressure
per density — an **effective EOS**, far stiffer than isothermal.

*For:* keeps the Jeans length resolved (no artificial fragmentation); makes a multiphase
ISM affordable; reproduces Kennicutt–Schmidt by construction.
*Against:* a pressure floor is an artificial vertical scale. TNG softens it to
$0.3\times$SH03 $+\,0.7\times$ isothermal at $10^4$ K, but the floor remains — in exactly
the inner region where the compaction signal lives.

### Star formation
Stochastic from gas on the EOS, $\dot\rho_\star=(1-\beta)\rho_c/t_\star$ with
$t_\star(n)=t_0(n/n_{\rm th})^{-1/2}$ and $t_0=2.2\,h^{-1}$ Gyr $\simeq3.28$ Gyr — the
density dependence gives a Schmidt slope of 1.5 against Kennicutt's observed $1.4\pm0.15$
(matched after vertical integration to the surface-density relation). **Chabrier (2003)**
IMF.

### Stellar feedback — kinetic winds
Wind particles are launched from star-forming cells, **temporarily decoupled** from the
hydrodynamics, and recouple when the density drops below **$0.05\times$ the SF threshold**
or after **$0.025\,t_{\rm H}$** (rarely triggered). Decoupling lets winds escape the dense
ISM without depositing momentum immediately — the least physical part of the model.
$v_w=\max[\kappa_w\sigma_{\rm DM}(H_0/H(z))^{1/3},\,v_{w,\min}]$ with $\kappa_w=7.4$ and
$v_{w,\min}=350$ km/s; mass loading $\eta=(2/v_w^2)\,e_w(1-\tau_w)$ with $e_w$
metallicity-dependent and $\tau_w=0.1$ of the energy injected thermally. Launched
**isotropically** in TNG (bipolar in Illustris). *Why it matters:* winds remove **low-$j$ gas** preferentially,
raising the specific angular momentum of the remainder and enlarging disks (§6.3).

### Black holes
Seeded at $8\times10^5h^{-1}M_\odot$ when a FoF halo exceeds $5\times10^{10}h^{-1}M_\odot$.
Bondi–Hoyle–Lyttleton accretion capped at Eddington, $\dot M=\min(\dot M_{\rm Bondi},
\dot M_{\rm Edd})$, with **no boost factor** ($\alpha=1$; Illustris used 100). **Two
feedback modes** (Weinberger+17): **thermal** at high Eddington ratio; **kinetic** at low
Eddington ratio — energy accumulates to a threshold, then is released as a pulse in a
random direction — the mode that quenches massive galaxies in TNG. Kinetic below
$\chi=\min[0.002(M_{\rm BH}/10^8M_\odot)^2,\,0.1]$, thermal above. Quenching terminates in-situ central
growth and freezes the compact core.

### Enrichment, cooling, magnetic fields
TNG tracks nine elements (H, He, C, N, O, Ne, Mg, Si, Fe) from SNIa, SNII and AGB yields,
plus a separately tagged NS–NS-merger r-process component from which europium is derived
(Naiman+18); **Lumina tracks total $Z$ only**. TNG100 cools in ionization equilibrium under
the Faucher-Giguère+09 UVB using CLOUDY tables built following Wiersma+09, with Rahmati+13
self-shielding. TNG runs ideal MHD (Pakmor & Springel 2013, Powell cleaning) from a uniform
$10^{-14}$ comoving G seed ($1.6\times10^{-10}$ G physical at $z=127$); **Lumina does not
evolve magnetic fields.**

## 10 · What is specific to Lumina

### On-the-fly radiative transfer (AREPO-RT)
Moment-based: radiation energy density and flux on the same Voronoi mesh, closed with
**M1**, which builds the Eddington tensor from the local flux and so gets both limits
right — free-streaming ($P=E$, beamed) and optically thick ($P=E/3$, isotropic). Cost is
**independent of the number of sources**, which is what makes reionization in 500 cMpc
possible. Known failure: fluxes are single-valued per cell, so **head-on beams cannot
cross** — their fluxes cancel and the radiation is squeezed sideways into a spurious
perpendicular source (Rosdahl+13); beams meeting at an angle are **merged into one
averaged source** (Aubert & Teyssier 08). Casting shadows behind opaque clumps is actually
a *strength* of M1 over flux-limited diffusion.

### The six frequency bins
Cross sections fall steeply above threshold — $\sigma\propto\nu^{-3}$ in the Kramers
approximation near the edge, tending to $\nu^{-7/2}$ at high frequency (Verner+96 give
the full fits) — so a grey scheme gets both the ionization and the heating rate wrong and
cannot follow spectral hardening. Bins sit at the ionization edges (H I 13.6, He I 24.6,
He II 54.4 eV):

| Bin | Range | Job |
|---|---|---|
| 1 | 13.6–24.6 eV | H I — drives hydrogen reionization |
| 2 | 24.6–54.4 eV | H I + He I |
| 3 | 54.4 eV → X-ray | adds He II — hardest stellar/AGN photons |
| 4–6 | three X-ray bands | long mean free path: escape to the IGM, pre-heat distant neutral gas, secondary ionizations |

Sources: stellar populations, accreting black holes, high-mass X-ray binaries
(Madau+17, Pacucci+14). Frequency-dependent cross sections from Verner+96.

### Equilibrium vs non-equilibrium thermochemistry → [[Non-equilibrium Thermochemistry]]
Cooling needs the ionization state. **Equilibrium** (TNG100) sets ionization = recombination
per species, algebraically, under a spatially uniform redshift-dependent UVB, and tabulates
$\Lambda(n,T,z)$ once — valid when the chemical timescale is short, i.e. in dense gas.
**Non-equilibrium** (Lumina) integrates $$dn_{\rm HI}/dt=n_{\rm HII}n_e\alpha_{\rm rec}
-n_{\rm HI}(\Gamma_{\rm photo}+n_e\Gamma_{\rm coll})$$ and its He counterparts in time, with
$\Gamma_{\rm photo}$ from the *local* RT field. It matters where
$t_{\rm rec}\simeq1/(n_e\alpha)\approx10^5\,{\rm yr}\,(n_e/{\rm cm^{-3}})^{-1}$ is long — the
IGM/CGM at $z\sim6$, where it approaches the Hubble time: ionization fronts are impulsive,
cooling gas lags over-ionized, self-shielding emerges from the actual column, and the
post-reionization temperature follows the local spectrum. Lumina replaces only the
**primordial** cooling; metal-line cooling stays standard since only total $Z$ is tracked.

### Reduced speed of light, subcycling, thermochemistry
Explicit RT needs $\Delta t\le\Delta x/\tilde c$ — orders of magnitude below the hydro
step at true $c$. **$\tilde c=0.2c$** relaxes it. Gnedin & Abel (2001) state the validity
condition as gas velocities $v\ll\tilde c$; for a hyperbolic M1 scheme the operative
condition is that I-fronts move well below $\tilde c$ (Rosdahl+13; Thesan App. A). Thesan
finds $0.2c$ and $0.3c$ converged and $0.1c$ delays reionization — tested at reduced
resolution, then adopted for the flagship. Radiation and thermochemistry
are **subcycled 64×** during hydrogen reionization and **256×** at $z<4.75$ — the
chemistry timescales are short, and the stiff network (ionization and recombination rates
differing by orders of magnitude) cannot ride the hydro step.

### Initial conditions
$z=49$, CAMB, **separate transfer functions for baryons and CDM** (different linear growth
before the baryon drag epoch; a single one overestimates small-scale baryon power), plus
the **baryon–CDM streaming velocity** (Tseliakhovich & Hirata 2010): rms $\simeq30$ km/s
at recombination against a sound speed of $\simeq6$ km/s (Mach $\sim5$), decaying
$\propto1/a$, coherent over several comoving Mpc (the Silk scale). It suppresses the gas
content of minihalos and raises the minimum cooling mass, delaying the first stars
(Tseliakhovich, Barkana & Hirata 2011).

### Deliberate departures from TNG
Total $Z$ only; no MHD; a **shortened gas depletion time at $z>4.75$** to avoid the
smallest hydrodynamic timesteps, reverting to the calibrated value at $z\le4.75$ —
acting precisely where the mass–size inversion is strongest.

## 11 · Stellar populations and dust — the physics behind §3.7–3.8

**BPASS** (Binary Population and Spectral Synthesis; Eldridge & Stanway). Population
synthesis that follows **binary evolution** — mass transfer and envelope stripping make hot
helium stars (initial masses $\sim10$–$20M_\odot$), which **harden the spectrum and keep
the ionizing/UV output alive to ages $\gtrsim10$ Myr**, most strongly at low metallicity
where winds alone cannot strip envelopes. That persistence, not the peak young-age
budget, is the main binary effect. Versions: v2.1 is Eldridge+17 (PASA 34, e058); v2.2 is
Stanway & Eldridge 2018 (MNRAS 479, 75); **v2.2.1** is the July-2018 bug-fix release of
v2.2 — cite both papers for it.

**Extinction vs attenuation.** *Extinction* is what a point source behind a dust screen
suffers — absorption plus scattering out of the beam, $A_\lambda=1.086\tau_\lambda$.
*Attenuation* is the net effect on an extended source with stars and dust mixed:
scattering back in, and a distribution of columns, make it **greyer** than extinction and
geometry-dependent. Vogelsberger+20 Model B converts the resolved optical depth with the
homogeneous-mixture formula $A_V=-2.5\log[(1-e^{-\tau})/\tau]$ (Calzetti+94) and treats
only the birth clouds as a screen. The paper evaluates a column **per star along its own
sightline** using only the gas in front of it, so the geometry is explicit and a screen
is the right description for the resolved component as well. (Vogelsberger+20's Model A
is empirical IRX–$\beta$; Model C is full SKIRT radiative transfer.)

**Calzetti+00.** Empirical *attenuation* law for local starbursts; the $4.05\pm0.80$ is
their $R'_V$, an *effective total obscuration at $V$*, not a true extinction $R_V$. The
curve has no 2175 Å bump — an absence established observationally in Calzetti+94.
**Kriek & Conroy (2013)** add the bump with amplitude $E_b=0.85-1.9\,\delta$: steeper
curves ($\delta<0$) carry stronger bumps. The $k(\lambda)/R_V$ scaling converts $A_V$ to
any band.

**Charlot & Fall (2000).** Two dust components: **birth clouds** around stars younger than
$t_{\rm BC}=10^7$ yr, and the **diffuse ISM** seen by all stars. Their standard model sets
$\hat\tau_V^{\rm BC}=1.0$, $\hat\tau_V^{\rm ISM}=0.5$ — i.e. **exactly twice** — with the
same $\lambda^{-0.7}$ power law for both components. That is the origin of the "twice the
galaxy mean" birth-cloud screen for stars $<10$ Myr (Vogelsberger+20 eqs. 20–22:
$\tau^{\rm unres}_V=2\langle\tau^{\rm res}_V\rangle$, $A\propto\lambda^{-0.7}$, applied as
a screen).

**Why UV is hit harder than $V$.** $k(\lambda)$ rises steeply to the blue, so for the same
$A_V$ the 1500 Å extinction is several times larger — which is why the dust reversal of the
size–mass slope is strong in rest-UV and weaker (and lost ~2 redshift bins earlier) in
rest-$V$.

**Why $\tau_{\rm dust}(z)$ at all.** The dust-to-metal ratio and the unresolved
sub-cell structure are not predicted by the simulation; a single per-redshift
normalization absorbs both, and fixing it on the UV LF is the standard Vogelsberger+20
procedure.

## 12 · Observational context to have cold

Galaxies at $z\gtrsim3$ are systematically compact (Oesch+10, Ono+23, Miller+25, Allen+25)
and largely irregular (Kartaltepe+23) — yet **roughly half of $M_\star>10^9M_\odot$
galaxies at $z=3$–$6$ are disky** (Ferreira+23, Kartaltepe+23), far above pre-JWST
expectation (Ferreira+22). Dynamically cold disks exist early: REBELS-25, a kinematically
cold gas disk at $z=7.3$ (Rowland+24); the Big Wheel, a spiral with $R_e=9.6$ kpc at
$z=3.25$ (Wang+25). Rotationally dominated, sometimes cold, disks at high $z$: Neeleman+20,
Rizzo+20. The observed size–mass relation stays positive to $z\sim8$ (Morishita+24,
Miller+26), against inverted intrinsic relations in BlueTides and FLARES (Marshall+22,
Roper+22).

## Connections

- [[Research Exam — Q&A]] — committee-style questions with spoken-length answers
- [[Halo Spin Parameter]] — definitions, tidal torque origin, why lognormal
- [[Non-equilibrium Thermochemistry]] — equilibrium vs non-equilibrium cooling
- [[Resolution comparison]] — COLIBRE's DM supersampling, TNG vs Lumina resolution
- [[Pillepich — disks in the first billion years]] — resolved SNe, dropping the EOS floor
- [[Calibration and tuning]] · [[Simulation landscape]] · [[Predictive power]]
- [[TNG-Cluster vs IllustrisTNG]] · [[Galactic winds]] · [[Dynamical friction]]
- [[Eddington limit]] · [[Super-Eddington accretion]] · [[Accretion disc states]]
- [[MOC - CGF 2026]] · [[MOC - Astrophysics]]
