---
title: Research Exam — Q&A
type: project
tags: [project, exam, astro/galaxies, sim/TNG, sim/lumina]
status: active
started: 2026-09-02
companion: "[[Research Exam]]"
---

# Research Exam — Q&A

Committee-style questions with answers at speaking length. Numbers and formulas are the
verified ones in [[Research Exam]]. **Bold** marks the phrase to land on. Board questions
are marked ✍.

---

## 0 · Openers

**Q. Tell us what you found, in two minutes.**
The standard picture says a disk inherits its halo's angular momentum, so size should
scale with halo spin. Simulations have found that correlation weak, and that's been read
as the picture failing. I looked at central galaxies from $z=0$ to $7$ in Lumina and
TNG100 — same galaxy-formation model, two volumes — and asked *when* the spin matters.
If you measure the halo spin not at the epoch you observe the galaxy but at earlier
snapshots, the correlation with size rises, peaks, and falls. **The peak sits at about
1.3–1.4 times the median stellar age at every anchor from $z=1$ to $5$.** So the disk
remembers a spin the halo had when the disk's material was being acquired. A predictor
built on that — the halo's spin history weighted by the star-formation history and read
15% of a cosmic time early — correlates with size at $\rho\simeq0.5$–$0.6$, roughly twice
the instantaneous value. Two other channels are independent of it: earlier-forming halos
host larger galaxies, and accreted stars build extended envelopes while in-situ central
growth builds compact cores. That last competition inverts the intrinsic mass–size
relation at $z\gtrsim2$ — but in projected, dust-extincted light it flips back to
positive across most of the observed range. **Size is set more by assembly history than by
the halo's present state.**

**Q. What's the one number you'd want us to remember?**
Present-day halo spin **underpredicts the size–spin correlation by 1.5× at $z=0$ and 5.7×
at $z=5$.** Anyone assigning sizes from halo properties — semi-analytic models, empirical
models — is throwing away most of the signal by using the spin at the wrong time.

**Q. Why does this matter beyond your simulation?**
Three reasons. Galaxy sizes are among the most direct observables of assembly, and JWST
now measures them into reionization, so the theory has to say what sets them. Semi-analytic
and empirical models assign disk sizes from halo spin — this says which spin. And the
mass–size inversion at high $z$ is a genuine tension between simulations and JWST that
turns out to be largely a *measurement-definition* effect.

**Q. What is new here versus Jiang+19, Desmond+17, Yang+22?**
They established that instantaneous spin is a weak predictor and that the strength is
model-dependent. Nobody had asked *when* the spin is imprinted. The sweep, the alignment
of the peak with stellar age, and the acquisition-weighted predictor are new. So is
running the same physics model from $z=7$ to $0$ with high-$z$ statistics — 70,000 halos in
the primary bin at $z=3$.

---

## 1 · The simulations

**Q. Why two simulations? Why not just Lumina?**
Lumina stops at $z=3$. TNG100 runs to $z=0$ and uses the same galaxy-formation model, so
the two together give one consistent model over $z=0$–$7$. They overlap at $z=3$, and I
check that galaxy properties agree there before stitching. The price is that Lumina has
radiative transfer and TNG100 doesn't, so the physics isn't perfectly identical — I'm
explicit that the overlap tests **robustness across volume and resolution, not across
physics**.

**Q. What does the RT actually do to the galaxies you care about?**
Honestly, for MW-mass centrals at $z\le7$, little directly. RT matters most for
reionization and the IGM, and for the ionizing background low-mass halos see. Lumina's
main advantage here is **volume with resolution**: 500 cMpc at $3.6\times10^6M_\odot$ per
gas cell. TNG100 is too small for high-$z$ statistics; TNG300 and MillenniumTNG are too
coarse to measure structure.

**Q. Lumina shortens the gas depletion time at $z>4.75$. Doesn't that affect your
high-$z$ star formation?**
It's a numerical choice to avoid the smallest hydrodynamic timesteps, and the model
reverts to the calibrated TNG value at $z\le4.75$. It acts exactly where the mass–size
inversion is strongest, so I hold it in mind. The argument that it's not driving the
result is that the inversion is already present in TNG100 at $z=2$–$3$ with the standard
depletion time, and BlueTides and FLARES see it with entirely different codes.

**Q. What's the actual resolution difference between the two?**
Closer than people assume. Collisionless softening is 1.77 ckpc in Lumina and 1.48 ckpc
in TNG100 at $z>1$ — **only 1.2× coarser** — so 0.44 vs 0.37 pkpc at $z=3$, 0.22 vs 0.19 at
$z=7$. Baryonic mass resolution is 2.6× coarser. That's why the $z=3$ overlap is a fair
comparison.

**Q. Explain the two-phase ISM model in one minute. What is it doing for you?**
Above about $0.1$ hydrogen atoms per cm³, the gas isn't resolved into clouds. Springel &
Hernquist model each cell as cold clouds in pressure balance with a hot phase: clouds grow
by cooling of the hot phase, get evaporated by supernovae, and form stars; a fraction of
those stars die immediately and heat the hot phase. Because heating is tied to star
formation and star formation to the cold fraction, it **self-regulates to a unique
equilibrium at each density**, and you can eliminate the phases to get one pressure per
density — an effective equation of state. It keeps the Jeans length resolved, makes a
multiphase ISM affordable, and reproduces Kennicutt–Schmidt. The cost is a **pressure
floor**: an artificial minimum disk thickness, sitting exactly in the inner region where
the compaction signal lives.

**Q. What do the winds do, physically, and why are they decoupled?**
Wind particles are launched from star-forming cells at a speed set by the local dark-matter
velocity dispersion — $7.4\,\sigma_{\rm DM}$ scaled by $(H_0/H)^{1/3}$, floored at 350 km/s —
with mass loading $\propto v_w^{-2}$ so energy is conserved. They're decoupled from the
hydro so they can leave the dense ISM without dumping their momentum on the first cell,
and recouple below 5% of the SF threshold. For sizes the key effect is that **winds
preferentially remove low-angular-momentum gas**, which raises the specific angular
momentum of what's left and enlarges disks — one of the main reasons the halo-spin–size
mapping is not clean.

**Q. What does the black-hole model do to sizes?**
Two modes. Thermal at high Eddington ratio; kinetic — energy accumulated and released as a
pulse in a random direction — below $\chi=\min[0.002(M_{\rm BH}/10^8)^2,0.1]$. The kinetic
mode is what quenches massive galaxies in TNG. For sizes, **quenching terminates in-situ
central growth and freezes the compact core**, which is the last step in the compaction
sequence.

---

## 2 · Halos and spin

**Q. Define your spin parameter. Why Bullock and not Peebles?**
$\lambda=j_{\rm dm}/(\sqrt2V_{200c}R_{200c})$, with $j_{\rm dm}$ the specific angular momentum
of the dark matter inside $R_{200c}$ and $V_{200c}$ the circular velocity from the total
mass. Peebles' $\lambda=J|E|^{1/2}/GM^{5/2}$ needs the total binding energy, which is
expensive and ill-defined at the edge of a halo; **Bullock's needs only enclosed mass,
radius and angular momentum**. For a truncated isothermal sphere they coincide; for NFW,
$\lambda'\simeq\lambda f_c^{-1/2}$.

**Q. Why dark-matter spin? The disk forms from gas.**
Because the question is **what a halo-based model can know**. Semi-analytic models, HODs,
and empirical models have the dark-matter halo and nothing else. I'm testing the
predictive power of halo spin specifically; a weak correlation constrains that, not
angular momentum in general. Using the gas spin would be answering a different, easier
question.

**Q. Why is the spin distribution lognormal, and why $\sim0.035$?**
Three parts. *Why small:* tidal torque theory — a non-spherical protohalo is torqued by
its neighbours' tidal field only while it grows linearly, $J\propto t$, and the torque
shuts off at turnaround, so the halo never gets near rotational support. Bullock's fit is
$\lambda'_0=0.035$, $\sigma=0.5$ — a factor-1.6 scatter. *Why lognormal:* two steps. In
linear theory each component of $J$ is a sum over many independent tidal modes, so it's
Gaussian, and $|J|$ is Maxwellian — a symmetric bump on a log axis. Then after turnaround
the halo grows by mergers that each change $J$ by a random **fractional** amount —
Vitvitska's random walk — so $\ln J$ is a sum of random increments, and **the central
limit theorem in log space makes it lognormal**. *Why it barely evolves:* $\lambda$ is
dimensionless by construction, $J\propto M^{5/3}$ against $E\propto M^{5/3}$, and the
random walk has no preferred epoch. If pressed: Bett+07 show the lognormal fails in the
tails — the low end is a power law, because a 3D random vector can't have a
super-exponential cutoff at zero. **The near-static distribution in my Figure 1 is a
check that the halo finder and the definition are behaving**, and the small hydro-vs-DM
offset is baryons exchanging angular momentum with the dark matter.

**Q. Your hydro halos have slightly higher spin than DM-only. Why?**
Baryons condense to the centre and can transfer angular momentum outward to the dark
matter, and the halo boundary itself shifts. Bryan+13 find a few-percent effect that
depends on the feedback model. It's small, systematic, and I'm not building anything on it.

**Q. ✍ Derive the disk-size scaling on the board.**
An exponential disk with flat rotation $V_c$ has $J_d=2M_dR_dV_c$, so $j_d=2R_dV_c$. Set
that equal to the halo's specific angular momentum, $j_h=\sqrt2\lambda V_{200}R_{200}$.
Then $R_d=\lambda R_{200}/\sqrt2$ for $V_c=V_{200}$ — MMW eq. 12. Their eq. 28 adds
$(j_d/m_d)f_c^{-1/2}f_R$ for the NFW energy, the rotation-curve shape, disk self-gravity
and contraction. With $\lambda\sim0.035$ that gives $R_d\sim0.025R_{200}$; Kravtsov finds
$R_{1/2}\simeq0.015R_{200}$ empirically. **So the picture gets the scale right; what I'm
testing is whether it gets the scatter right.**

**Q. ✍ Where does $t_{\rm dyn}=0.1H^{-1}$ come from?**
$M_{200}=\frac{4\pi}{3}R_{200}^3\cdot200\rho_{\rm crit}$ with $\rho_{\rm crit}=3H^2/8\pi G$
gives $V_{200}^2=GM/R=100H^2R^2$, so $R_{200}=V_{200}/(10H)$ — MMW eq. 2. Therefore
$t_{\rm dyn}=R_{200}/V_{200}=0.1H^{-1}$ exactly, at every mass and epoch. In Einstein–de
Sitter $t=\frac23H^{-1}$, so **one dynamical time is 0.15 of the age of the universe** —
which is my $\beta$.

---

## 3 · Disks, kinematics, sizes

**Q. How do you decide a galaxy is a disk?**
Kinematically. I compute $\kappa_{\rm rot}$, the fraction of stellar kinetic energy in
ordered rotation about the disk axis, within $0.1R_{200c}$, and call it a disk if
$\kappa_{\rm rot}>0.5$. That's the standard threshold — Sales+12, Du+20 — and I checked
face-on and edge-on maps by eye. **No Sérsic or bulge–disk decomposition**; if you want
that I'd say it's the natural extension.

**Q. How do you find the disk axis? Isn't that circular — you need the axis to define
the disk stars, and the disk stars to define the axis?**
Two passes. First pass: angular momentum of all stars inside $0.1R_{200c}$ gives a
preliminary axis. Along it, each star gets $j_z$ and an energy, and a circularity
$\epsilon=j_z/j_c(E)$ — its angular momentum relative to a circular orbit of the same
energy. Stars with $\epsilon>0.7$ are disk stars; their angular momentum gives the final
axis. It converges because the bulge contributes little net angular momentum either way.

**Q. How do you get $j_c(E)$? That needs the potential.**
I don't solve for the potential separately. I take the catalogued potential of the bound
star particles, bin it radially, take the median in each bin, and fit a spline in
$\log r$. That gives $\Phi(r)$, then $v_c=\sqrt{r\,d\Phi/dr}$, and I invert
$E=\frac12v_c^2+\Phi$ for $r_c(E)$.

**Q. Why the 3D half-mass radius? Nobody observes that.**
Three reasons. It needs no profile fit and no assumed shape, so it's the most robust size
you can extract from a simulation. It matches Genel+18, so I can check the $z=0$ relation
against theirs. And I measured the 2D projected version too — it agrees to about 10%.
**The observable comparison is done separately, with light**, in the second half of the
paper.

**Q. What stellar mass goes with what?**
Within $2R_{1/2}$ for the mass–size relation, to match Genel+18. **Total bound mass for
every assembly-history analysis**, because there I'm using $M_\star$ as a control and it
must not depend on the size I'm predicting.

**Q. Why three different samples?**
The mass–size relation uses every central, because that's what the observed relation
contains. The spin–size analysis uses disks only, because a disk size is only meaningful
for a rotationally supported system. The light-weighted analysis uses star-forming
centrals with **no** morphological cut, because that's what van der Wel and Miller select.

**Q. Where does $3.6\times10^9M_\odot$ come from?**
A thousand star particles in Lumina — about 2,600 in TNG100 — so $\kappa_{\rm rot}$ and
$\epsilon$ are measured from a resolved velocity field.

---

## 4 · Light and dust

**Q. Walk us through going from star particles to an effective radius.**
Each star particle gets a BPASS SED from its age and metallicity — binary models, Chabrier
IMF. I integrate through rest-1500 Å and rest-$V$. Project face-on in the disk frame.
Estimate the background in an annulus at 21–24 pkpc as the median over eight
sub-annuli — so a satellite in the annulus can't bias it — and subtract it from the
cumulative profile. $R_{\rm eff}$ is the radius enclosing half the background-subtracted
light within 20 pkpc. That's the observers' curve-of-growth procedure, circularized.

**Q. Why BPASS and not, say, Bruzual & Charlot?**
Binaries. Mass transfer and stripping produce hot helium stars that **harden the spectrum
and keep the UV alive past 10 Myr**, especially at low metallicity where winds alone
can't strip envelopes. For rest-UV sizes of high-$z$, low-metallicity galaxies that's the
right population model. The Chabrier IMF matches the TNG model's own IMF.

**Q. Now dust — how exactly?**
Vogelsberger+20's resolved model. Dust is traced by metals in star-forming and cold gas.
For each star I integrate the hydrogen column and column-averaged metallicity along its
sightline to the observer, and $\tau_V=\tau_{\rm dust}(z)\,(Z/Z_\odot)(N_H/N_{H,0})$ with
$N_{H,0}=2.1\times10^{21}$. Because each column is per star with only the gas in front of
it, the geometry is explicit, so I use a **pure screen**, $A_V=1.086\tau_V$, rather than
their mixed-slab formula. Calzetti's curve with the Kriek & Conroy bump takes $A_V$ to any
wavelength. Stars under 10 Myr get an extra birth-cloud screen at twice the galaxy mean —
Charlot & Fall's standard ratio. Then I remeasure $R_{\rm eff}$.

**Q. $\tau_{\rm dust}(z)$ is a free parameter. Doesn't that mean you can get any size
result you want?**
It's one number per redshift, and it's **fixed by the UV luminosity function, not by
sizes** — Moutard, Adams, Bouwens, Varadaraj at their respective redshifts. Once the LF
matches, the sizes are a prediction. And the mechanism that flips the slope — dust
concentrated in the compact, metal-rich cores of massive galaxies — doesn't depend on the
normalization; FLARES and BlueTides see the same reversal with different dust treatments.

**Q. Why does light-weighting flatten the relation but not flip it, while dust flips it?**
Young stars sit beyond the old core, so a light-weighted radius is larger than a
mass-weighted one for a centrally concentrated galaxy — that shifts $\rho$ up by 0.2–0.3
but the massive galaxies are still the most compact. Dust lives where the metals are —
the dense cores — so it **dims the centre and pushes the half-light radius outward
preferentially in the most massive galaxies**. That reorders them.

**Q. Why is the rest-$V$ reversal weaker?**
The Calzetti curve rises steeply to the blue: for the same $A_V$, the 1500 Å extinction is
several times larger. Less extinction in $V$, less outward push, so the $V$-band relation
turns negative about two redshift bins earlier than the UV.

**Q. What is the difference between extinction and attenuation, and which do you have?**
Extinction is what a point source behind a screen suffers — absorption plus scattering
out of the beam, $A=1.086\tau$. Attenuation is the net effect on an extended source with
stars and dust mixed — scattering back in and a spread of columns make it greyer and
geometry-dependent. Because I resolve a column per star, **the screen is the honest
description of my geometry**; what I don't have is scattering into the line of sight,
which a full radiative-transfer code like SKIRT would add.

---

## 5 · Statistics

**Q. Why Spearman rather than Pearson?**
Rank-based, so it measures monotonic association without assuming linearity, and it's
robust to outliers and to the lognormal tails in spin and size. I don't have a model for
the functional form, so I don't want to assume one.

**Q. Explain your partial correlation. What does "at fixed $C$" actually mean?**
Rank-transform every variable. Regress the ranked size on the ranked controls — halo mass,
stellar mass, ex-situ fraction. Regress the ranked predictor on the same controls.
Correlate the two residuals. That's the association between size and the predictor
**after removing everything linearly explainable by the controls, in rank space**. I
bootstrap the whole procedure a thousand times for the 68% interval.

**Q. Why those three controls?**
Halo mass because everything scales with it. Stellar mass because it's the obvious
alternative driver and, at high $z$, an anti-correlated one. Ex-situ fraction because
accreted stars build size independently of anything the halo spin knows about. If the
spin-history signal survives all three, it's not a proxy for any of them.

**Q. Could $\Lambda_{\rm eff}$ just be a proxy for stellar age?**
Partly it could carry age information, since it's SFH-weighted. Two things argue against
it being *only* that. The peak-lookback result — the sweep — uses no $\Lambda_{\rm eff}$ at
all and shows the same thing. And $\beta$ is calibrated on the four TNG100 anchors and
applied to Lumina without refitting, where it still wins. A held-out test against an
age-only predictor is the natural next step, and I'd say that if asked.

---

## 6 · Assembly history

**Q. How do you know which stars are ex-situ?**
In TNG100, from the public stellar-assembly catalogs — Rodriguez-Gomez's classification
on the SubLink trees. In Lumina I build merger trees in post-processing from the SUBFIND
catalogs and apply the same rule: **a star is in-situ if, in the first snapshot after it
formed, it belonged to the main progenitor of its current host**; otherwise ex-situ.

**Q. Lumina's ex-situ fractions are lower than TNG100's. Is that physical or a
classification artifact?**
Some of each is possible — coarser mass resolution means fewer resolved small mergers, and
the trees are built differently. What matters for the result is that the *partial
correlation* with size is stronger in Lumina, $+0.70$ at $z=7$, even with lower typical
$f_{\rm ex}$. **A small accreted component at large radius leaves a large size signal.**

**Q. How do you reconstruct the spin history?**
Follow the main-progenitor branch back and, at each earlier snapshot, **recompute the
Bullock spin from the dark-matter particles inside that progenitor's $R_{200c}$** —
particle data, not catalog values. Then the sweep is just the partial correlation of size
with that earlier spin, at fixed $C$, as a function of lookback time.

**Q. What does the sweep look like, and what's the physical reading?**
At every anchor, the correlation rises from its instantaneous value, peaks at nonzero
lookback, and decays. The peak moves from 0.25 Gyr at $z=5$ to 5 Gyr at $z=0$. Divide by
the median stellar age and **the peaks line up at 1.2–1.5**. The reading: stars inherit
angular momentum from gas that arrived *before* they formed, so the disk remembers an
epoch slightly older than its stars; after that the halo spin random-walks away.

**Q. Why does $z=0$ plateau instead of peaking?**
Because by $z=0$ the star-formation histories are old and extended — a MW-mass galaxy
has been forming stars for 10 Gyr. No single past epoch dominates, so the memory curve
smears into a plateau and the gain over instantaneous spin is smaller. That's also where
the unlagged average, $\beta=0$, does best.

**Q. Define $\Lambda_{\rm eff}$ and tell us how you chose $\beta$.**
The halo's spin history weighted by the in-situ star-formation history, but with each
star's formation time shifted earlier by a fraction $\beta$ of cosmic time:
$\Lambda_{\rm eff}=\sum m_i\lambda[(1-\beta)t_i]/\sum m_i$. I scanned $\beta$ from 0 to
0.35 in steps of 0.025 and took the value maximizing the mean partial correlation over
the four TNG100 anchors. The maximum is broad, at 0.15, and I applied it to Lumina
unchanged. **0.15 of a cosmic time is one virial dynamical time** — the timescale for
material to fall in, consistent with the spin being imprinted at halo entry when tidal
torquing ends.

**Q. How much better is it, honestly?**
Partial $\rho$ of $+0.50$ to $+0.60$ at every anchor versus $+0.27$ to $+0.37$ instantaneous;
raw $+0.62$ to $+0.70$. At high $z$ that's several times the instantaneous coefficient. It
also beats the spin at any *single* past snapshot — the weighting matters, not just the lag.

**Q. Formation time also predicts size. Is that the same thing as spin memory?**
No — it's a second channel. At fixed halo mass, stellar mass, and ex-situ fraction,
earlier-forming halos host larger galaxies, and the coefficient grows from zero at $z=0$
to about $+0.5$ in Lumina. It's independent of the spin history in the partial
correlations. And controlling $M_\star$ and $f_{\rm ex}$ is essential: early-forming halos
have more stars and less accreted material, which masks the trend otherwise.

**Q. Jiang+19 said concentration beats spin. What do you find?**
At fixed halo mass alone, more concentrated halos do host smaller galaxies —
$\rho\simeq-0.25$, slope $-0.4$, shallower than their $-0.7$. But once I control halo
mass, stellar mass, and ex-situ fraction, concentration adds nothing — $|\rho|\lesssim0.16$
— and adding it doesn't move the formation-time coefficient. **Concentration is a proxy
for formation time**, which is what Wechsler and Ludlow would predict.

---

## 7 · The mass–size inversion and compaction

**Q. Why does the mass–size relation invert at high redshift?**
Two competing ways to grow. Accretion of stars deposits mass at large radii and grows
size; in-situ star formation in a gas-rich, dissipative galaxy concentrates mass at the
centre and shrinks the half-mass radius. At high $z$ in-situ growth dominates, and the
galaxies that have grown most are the ones that compactified earliest. The most massive
halos at fixed epoch formed earliest, so **at high $z$ the most massive galaxies are the
most compact** — the opposite of today.

**Q. What's the evidence for compaction specifically, rather than just "in-situ growth"?**
The ordering. In the compact-vs-extended tracks, the central density $\Sigma_1$ separates
first — $z\sim8$ in TNG100 — and the half-mass radii separate several hundred Myr later,
near $z\sim6$. Then the compact systems deplete their gas and quench. That sequence —
**central density up, then size down, then gas out** — is the blue-nugget scenario of
Dekel & Burkert and Zolotov. Lumina shows the same ordering at its $z=6$ selection.

**Q. Ten galaxies each. Is that a result?**
It's illustrative, not statistical, and I say so. The statistical results are the partial
correlations on thousands of galaxies; the tracks show what the median history *looks
like* for the extremes. A dedicated analysis of compaction events — identifying the
inflow and the $\Sigma_1$ rise directly — is the proper follow-up.

**Q. The compact galaxies have the same halo spin today but lower spin in the past. What
does that tell you?**
That the present-day spin has forgotten what mattered. The compact systems were
lower-spin halos *when they were forming their stars*; by the selection epoch the random
walk has erased the difference. **That's the same physics as the sweep, seen in individual
histories.**

**Q. Is the inversion a new result?**
No. Marshall+22 see it in BlueTides half-mass radii at $z=7$–$8$; Roper+22, 23 see an
inverted intrinsic size–luminosity relation in FLARES at $z\ge5$. What's new is showing it
in a model calibrated at low $z$, connecting it to assembly channels with partial
correlations, and showing that light and dust undo it.

---

## 8 · Physics background — board questions

**Q. ✍ Why is the recombination time the relevant scale for equilibrium chemistry?**
Equilibrium means ionization and recombination balance faster than conditions change. The
slower of the two sets the chemical timescale; in ionized gas that's recombination:
$t_{\rm rec}=1/(n_e\alpha_B)$, with $\alpha_B\simeq2.6\times10^{-13}$ cm³/s at $10^4$ K, so
$t_{\rm rec}\approx10^5$ yr$\,(n_e/{\rm cm^{-3}})^{-1}$. In the ISM that's instant. In the IGM
at $z\sim6$, $n_e\sim10^{-4}$, so **$t_{\rm rec}\sim$ Gyr — the age of the universe**. That's
why Lumina integrates the rate equations instead of assuming balance
→ [[Non-equilibrium Thermochemistry]].

**Q. What does a reduced speed of light do, and why is it allowed?**
Explicit RT has to satisfy $\Delta t<\Delta x/\tilde c$, which at the true $c$ is a
thousand times shorter than the hydro step. Setting $\tilde c=0.2c$ relaxes it fivefold.
It's allowed as long as nothing physical needs to move at $c$ — ionization fronts in
dense gas move far slower. Thesan tested 0.1, 0.2, 0.3 and found 0.2 converged; 0.1
delays reionization.

**Q. What does the subcycling do, and why 64 in one regime and 256 in the other?**
Three clocks: hydro at $\Delta x/(v+c_s)$, radiation at $\Delta x/\tilde c$, chemistry at
the ionization and recombination times. Even with $\tilde c=0.2c$ the radiation step is
hundreds of times shorter than the hydro step. So within one hydro step the gas is frozen
and the radiation plus chemistry are advanced $N$ sub-steps — operator splitting. $N$ is a
**cap on how far radiation and gas may drift apart** within a step. During hydrogen
reionization I-fronts heat cells by $10^4$ K inside a single hydro step, so the coupling
matters and the cap is 64. After $z=4.75$ the background is established and evolves
slowly, so 256 is safe and lets the hydro take its natural long steps.

**Q. Why is it called "cooling"?**
Because it removes thermal energy from the gas and radiates it away. A collision turns an
electron's kinetic energy into excitation or ionization of an atom; the atom emits a
photon; in optically thin gas the photon escapes. Thermal energy became light that left —
the temperature drops. The cooling function $\Lambda(T)$ is that radiated power per
volume divided by $n^2$, and its shape is just which atoms have transitions matching
$kT$ at each temperature. The reverse — a photon depositing its excess energy as electron
kinetic energy — is photoheating, and the net is $\Lambda_{\rm cool}-\Gamma_{\rm heat}$.
**It's only cooling if the photons escape.**

**Q. Primordial versus metal-line cooling — what's the difference, and how do your two
simulations handle them?**
Primordial is H and He: Lyα and He II collisional excitation give the peaks at
$2\times10^4$ and $10^5$ K; then collisional ionization, recombination, bremsstrahlung
above $10^6$ K, Compton at high $z$. It has a **hard floor at $10^4$ K** — nothing to
excite below that without H$_2$ or metals — and a dip near $10^{5.5}$–$10^6$ K.
Metal-line is C, N, O, Ne, Mg, Si, S, Fe: many low-lying transitions, so solar-metallicity
gas cools **10–100× faster in the $10^5$–$10^7$ K dip**, and fine-structure lines like
[C II] and [O I] remove the floor. TNG100 takes both from CLOUDY tables in ionization
equilibrium under a uniform UVB, with metals scaled by total $Z$ — and the UVB
*suppresses* cooling by ionizing away the coolants. Lumina replaces **only the primordial
part** with the non-equilibrium network under the local field; metals stay tabulated
because only total $Z$ is tracked. The split is where it is because H+He is six
ionization states and is what reionization acts on; metals are hundreds of coupled ions.
→ [[Non-equilibrium Thermochemistry]]

**Q. Why six frequency bins? Why not one?**
The cross section falls steeply above each edge — roughly $\nu^{-3}$ — so a hard photon
and a soft photon do very different things: the soft one is absorbed at the first neutral
atom, the hard one travels far and deposits more energy per ionization. A grey scheme
gets both the ionization *rate* and the *heating* wrong and can't follow the spectrum
hardening as it propagates. The bins sit at the H I, He I, He II edges — 13.6, 24.6,
54.4 eV — plus three X-ray bands for the long-mean-free-path photons from X-ray binaries
and AGN that pre-heat the neutral IGM.

**Q. What's M1, and what does it get wrong?**
A moment method: evolve radiation energy and flux, and close the hierarchy by building the
pressure tensor from the local flux — isotropic when the flux is small, fully beamed when
it's large. It's local, so the cost doesn't scale with the number of sources — that's what
makes a 500 cMpc reionization box possible. The failure: **two beams can't cross**. Head-on
they cancel and squeeze sideways; oblique ones merge into one averaged source.

**Q. ✍ Estimate $R_{200}$ and $R_{1/2}$ for a MW-mass halo at $z=3$.**
$R_{200}\propto(M/\rho_{\rm crit})^{1/3}$ and $$\rho_{\rm crit}\propto H^2\simeq
\Omega_m(1+z)^3H_0^2\approx19H_0^2$$
at $z=3$, so $R_{200}$ is $19^{1/3}\approx2.7$ times
smaller than at $z=0$: roughly $200/2.7\approx75$ pkpc. Kravtsov's 0.015 gives
$R_{1/2}\approx1.1$ kpc. **Against a softening of 0.44 pkpc that's about $2.5\epsilon$** —
resolved, but not by a wide margin, which is why I keep the 1000-particle floor.

**Q. ✍ What sets the timescale of the spin peak — why ~1 Gyr at $z=3$?**
Median stellar age of a MW-mass galaxy at $z=3$ is of order 0.5–1 Gyr; the peak sits at
1.3–1.4 times that. It's the time since the disk's gas was acquired. It scales with the
age of the universe because star-formation histories do.

**Q. What is the angular-momentum catastrophe and how was it solved?**
Early SPH simulations made disks ten times too small: gas cooled early into dense clumps
that then spiralled in by dynamical friction during mergers, handing their angular
momentum to the halo. The fix was strong early feedback — Governato, Brook — which stops
the early overcooling and **ejects low-angular-momentum gas from the centre**, so what's
left to make the disk has higher $j$ than the halo average. That's why feedback is a main
reason spin and size decouple.

**Q. What's the difference between in-situ growth and compaction?**
In-situ growth is any star formation in the main progenitor. Compaction is a *specific
episode* — an intense gas inflow, from disk instability, minor mergers, or counter-rotating
streams, that drives gas to the centre faster than it can be consumed and builds a dense
core in a fraction of a Gyr, followed by inside-out quenching. The signature is
$\Sigma_1$ rising before size falls.

---

## 9 · Numerics and resolution

**Q. What limits your smallest measurable size?**
Force softening first: 0.44 pkpc at $z=3$ in Lumina, 0.22 at $z=7$; structure inside a
few softening lengths isn't trustworthy. Then particle number for the inner profile —
hence the 1000-particle floor. Then two-body heating from dark-matter particles, which
inflates small galaxies over time. And then the EOS pressure floor, which isn't a
resolution limit at all but acts like one on disk thickness.

**Q. Would two-body heating create your inversion?**
No — it works against it. Spurious heating **puffs galaxies up**, most strongly in dense,
poorly sampled centres at high $z$, so it would make the most compact galaxies *less*
compact. If anything the intrinsic inversion is slightly underestimated.

**Q. Are your sizes converged?**
Not in the strict sense — nobody's are. TNG50, 100, and 300 give different sizes at fixed
mass. What I have is Lumina and TNG100 tracing the same relations at $z=3$ across a
factor of 2.6 in mass resolution and 1.2 in force resolution. And because the subgrid
model is calibrated at a given resolution, running finer isn't automatically more correct.

**Q. What is a Voronoi mesh buying you over SPH or a fixed grid?**
The mesh moves with the flow, so advection errors are small and the scheme is
Galilean-invariant like SPH, but it's a proper finite-volume Godunov solver with sharp
shocks and contact discontinuities like a grid code. Cells refine toward a target mass, so
resolution follows the gas.

**Q. How is the potential computed?**
TreePM — a short-range octree and a long-range particle mesh. For the circularity I don't
touch it; I use the potential values already stored per particle, binned and splined.

---

## 10 · Observations and context

**Q. Where does the observed size–mass relation stand at high $z$?**
Positive out to $z\sim8$ for star-forming galaxies — van der Wel's $R\propto M^{0.22}$ at
$z\lesssim3$, continued by Ward, Allen, Morishita, Miller with JWST. But not uniformly:
Chen+26 see flattening above $10^{10}M_\odot$ toward $z\sim5$, and there are tentative
negative slopes for bright $z=5$ rest-UV and $8<z<9$ rest-optical samples. **My extincted
relation declining to flat at $z\sim6$ sits inside that spread.**

**Q. How well do you match Miller+26?**
In the rest-optical, my dust-extincted medians lie within their 0.2 dex scatter at every
mass from $z=1$ to $4$. I'm slightly high at $z=1$–$2$, then cross below at the massive end
where my median flattens and theirs keeps rising; the deficit reaches 0.3 dex by $z=5$–$6$
above $10^{10.5}M_\odot$. Two caveats: my circularized curve-of-growth radii differ from
their Sérsic radii at the 0.1 dex level, and I'm comparing extincted profiles, not mock
images.

**Q. What's the tension that survives?**
Rest-UV sizes at $z=6$–$7$. My median at $M_{\rm UV}=-20$ is about twice the Shibuya+15
relation, growing toward fainter magnitudes. Shen+24 found the same sign in Thesan with a
larger amplitude. So the model makes faint high-$z$ galaxies too extended in the UV even
after dust.

**Q. JWST finds cold rotating disks at $z>7$ — REBELS-25 — and giant ones like the Big
Wheel. Does that surprise your model?**
Roughly half of $M_\star>10^9$ galaxies at $z=3$–$6$ are disky in JWST imaging, far above
pre-JWST expectations, and my kinematic classification finds disks throughout. Individual
giants like a 9.6 kpc spiral at $z=3.25$ are rare objects that a 500 cMpc box can host;
whether the model makes enough of them is a good follow-up.

**Q. How would you make this comparison truly like-for-like?**
Forward-model: full dust radiative transfer into mock JWST images with the right PSF,
depth, and pixel scale, then run the same GALFIT Sérsic fits the observers run. That
removes the curve-of-growth-vs-Sérsic offset and adds scattering.

---

## 11 · Interpretation, alternatives, falsification

**Q. Is this causal?**
No, and I say so. It's a statistical memory: the disk size retains information about the
halo's past spin beyond what the present state contains. I don't identify the mechanism
that imprints it — halo entry and the end of tidal torquing is the natural candidate,
and the one-dynamical-time lag points that way, but that's an interpretation.

**Q. Would this hold in another galaxy-formation model?**
I expect the *memory* to, because the mechanism is gravitational and it's measured
through dark-matter spin, which every model has. The *amplitude* may well differ — Yang+22
show spin–size strength varies between models, and feedback is what decouples them. A
cross-model test is the obvious next step.

**Q. What would falsify it?**
A cross-model test in which the sweep shows no peak. A held-out test in which an age-only
predictor matches $\Lambda_{\rm eff}$. Or a like-for-like mock-image comparison in which
the light-weighted relation stays inverted.

**Q. What's the practical recommendation for semi-analytic models?**
Don't assign disk size from the spin at the output redshift. **Use the acquisition-weighted
spin history** — integrate $\lambda$ along the tree, weight by star formation, read it one
dynamical time early. It's cheap; SAMs already have the trees.

**Q. If you could rerun one thing, what would it be?**
A resolution ladder at fixed physics inside Lumina's volume — the same halos at two or
three resolutions — so the convergence statement about high-$z$ sizes is direct rather
than inferred from the TNG100 overlap.

## 12 · What's next

- Cross-model test of spin memory (EAGLE/COLIBRE-type physics, or FIRE zooms).
- Held-out and null tests for $\Lambda_{\rm eff}$ with an age-only control.
- Forward-modelled mock JWST images with SKIRT, Sérsic-fit like the data.
- A direct census of compaction events — inflow episodes and the $\Sigma_1$ rise — rather
  than outcome-selected tracks.
- Resolved SN feedback: what removing the EOS floor does to inner sizes
  → [[Pillepich — disks in the first billion years]].
