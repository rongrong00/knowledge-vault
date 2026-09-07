---
title: Predictive power
type: concept
tags: [sim/methods]
status: growing
created: 2026-07-29
updated: 2026-09-02
---
# Predictive power

Up: [[MOC - CGF 2026]] · Related: [[Calibration and tuning]], [[Simulation landscape]], [[Galactic winds]]

---

Not one number. It varies by orders of magnitude depending on the observable, and the useful skill is knowing which tier you're standing in.

## Tier 1: gravity alone — genuinely excellent

Halo mass function, large-scale clustering, matter power spectrum on linear and quasi-linear scales: **percent level, converged across independent codes**. Nothing tuned — ΛCDM plus Newtonian gravity plus enough particles.

AbacusSummit and Euclid Flagship exist because this tier is trustworthy enough to build a cosmology survey on. Easy to forget it's part of the same enterprise.

## Tier 2: statistical galaxy properties — good, mixed provenance

Sort what was fit from what wasn't, case by case. Genuine successes:

- **EAGLE and TNG were calibrated only at $z=0$, and the SMF evolution to $z\approx2$ came out roughly right.** A real out-of-sample test that passed.
- **TNG reproduced SDSS clustering split by colour and mass** without those being targets. Non-trivial — requires quenching in the right halos at the right times, not just the right numbers.
- **Auriga and TNG produce realistic disk fractions, rotation curves, Tully-Fisher normalisation** from models tuned to none of those.
- Mass-metallicity relation shape, environmental and satellite quenching, morphology-density relation.

> Honest caveat: many "successes" in the literature are **postdictions** published after the data existed, and the calibration targets (SMF, sizes, gas fractions) constrain more downstream quantities than people acknowledge.

## Tier 3: gas outside galaxies — weak, and everyone knows it

The cleanest quantitative case is the **baryonic suppression of the matter power spectrum**, because it's a single curve every simulation can produce.

| Simulation | Suppression |
|---|---|
| BAHAMAS | ~15%, peaking near $k\sim5$ $h$/Mpc |
| TNG | starts later, ~20% at $k\sim10$ |
| OWLS | >20% |
| SIMBA (CAMELS) | ~30% at $k\sim10$; ~15% already at $k\sim1$ |
| ASTRID (CAMELS) | ~15% at $k\sim10$ |

Meanwhile **Stage-IV surveys need this curve to percent-level accuracy out to $k\approx10$ $h$/Mpc.**

> The inter-simulation spread exceeds the required precision by **more than an order of magnitude**.

Worse, the observations are pulling *outside* the simulated range: joint kSZ, X-ray and lensing analyses find gas expulsion best described by FLAMINGO's **strongest**-feedback variant (~10% suppression at $k=1$), stronger than most state-of-the-art simulations. So the models may be systematically wrong in a known direction.

The CGM story is the same shape — order-unity disagreements in cool gas mass and OVI columns, with no simulation comfortably matching COS-Halos. Root cause: [[Galactic winds]] as implemented are effective transport prescriptions, not outflow models.

## The falsification evidence

The best argument this is science rather than curve-fitting: **a flagship simulation has been killed by data.**

Illustris matched what it was tuned to, then produced badly wrong group and cluster gas fractions and quenched too few massive galaxies. The community didn't patch it — the model was **replaced**. TNG exists because Illustris failed a test it hadn't been fit to.

Recent failures are equally instructive:
- JWST found more UV-bright galaxies at $z>10$ than essentially any simulation predicted
- **Little red dots** are a clean miss — COLIBRE doesn't predict them, since it assumes BH seeds already exist; modelling their formation needs higher resolution and new physics

Nobody claims these were predicted.

## The diagnostic that actually works

Since no single simulation's error bar is meaningful, the operational test is **agreement across independently constructed models**.

If TNG, EAGLE, SIMBA and FIRE — different codes, hydro solvers, feedback philosophies, calibration targets — converge on a result, it's probably a ΛCDM consequence rather than a subgrid artefact. Where they diverge, **the divergence itself is the measurement**: it tells you the observable is feedback-sensitive.

This is the logic behind CAMELS, AGORA, and the CGM/cluster comparison projects, and why FLAMINGO ships twelve variants rather than one answer.

> Reporting a result from a single simulation without checking whether it survives a model change is the most common way to publish something that won't hold up.

**Volume caveat.** FLAMINGO finds the baryonic response converged at the 1% level only for volumes above $\sim200^3$ Mpc$^3$, implying results from Horizon-AGN, SIMBA and CAMELS at $\lesssim100^3$ are likely not converged (TNG300 and MillenniumTNG are). **Some apparent physics disagreements are box-size artefacts.**

## What they're actually good for

The "predictive power" framing undersells these. Their strongest uses:

**Conditional prediction.** "If feedback deposits energy this way, then the CGM looks like this." A falsifiable implication chain even when the antecedent is uncertain — and how the field converts CGM observations into feedback constraints rather than the reverse.

**Forward modelling.** Mock catalogues, selection functions, projection effects, covariance matrices. Here you need a universe that's *plausible*, not *correct*, and simulations are unmatched.

**Mechanism discovery.** Cold-mode accretion, the halo mass threshold in quenching, magnetic amplification timescales — found in simulations, robust to details.

**Marginalisation.** The most sophisticated current use: treat feedback uncertainty as a nuisance parameter, calibrated by cross-correlations with kSZ, X-ray, and FRB dispersion measures. The resummation model maps observed halo baryon fractions to power suppression with **zero free parameters** at $\lesssim1\%$ accuracy — using simulations to bridge observables rather than predict one from theory.

## For my own work

A TNG-vs-Lumina size comparison is favourable in one way — both use the same galaxy formation model, so differences are RT, resolution and volume. But that also means **agreement between them tests very little about the physics**.

> If a claim about high-$z$ sizes is to be believed, the referee question is whether it survives in a simulation with genuinely different feedback. → [[Resolution comparison]]
