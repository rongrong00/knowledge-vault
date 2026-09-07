---
title: Calibration and tuning
type: concept
tags: [sim/methods, method/calibration]
status: growing
created: 2026-07-29
updated: 2026-09-02
---
# Calibration and tuning

Up: [[MOC - CGF 2026]] · Related: [[Simulation landscape]], [[Predictive power]], [[Galactic winds]], [[Resolution comparison]]

---

**One-line answer:** they tune the free parameters of stellar and AGN feedback, against a small handful of $z=0$ observables, because the physics setting those parameters happens two to four orders of magnitude below the resolution limit.

## Why it's unavoidable

Two numbers make the case:

- A supernova remnant transitions from energy-conserving to momentum-conserving expansion at a cooling radius of ~10 pc, containing $\sim10^3M_\odot$. Your gas cell is $10^6M_\odot$ with ~kpc softening. Dump $10^{51}$ erg thermally and it reaches $\sim10^5$ K at high density, where $t_{\rm cool} <$ timestep. The energy vanishes before doing work. **Overcooling — purely numerical.**
- The Bondi radius of a $10^8M_\odot$ BH in hot gas is ~10 pc; the accretion disc setting radiative efficiency is sub-pc. Nothing about the actual accretion is resolved.

> The subgrid model isn't representing microphysics faithfully. It's a **device for injecting the right amount of momentum and energy at the resolved scale**, and the parameters exist to make that amount come out right.

## The knobs

**Stellar feedback** — usually three or four numbers:
- Energy budget per unit stellar mass formed, as a fraction of available SN energy ($f_{\rm SN}$ in FLAMINGO, $f_{\rm th}$ in EAGLE). Often given density and metallicity dependence so it rises where numerical losses are worst.
- Wind velocity, or in stochastic-thermal schemes the heating increment ($\Delta v_{\rm SN}$, or EAGLE's $\Delta T = 10^{7.5}$ K). **That $\Delta T$ is a numerical choice with no physical referent** — chosen so the heated particle's cooling time exceeds its sound-crossing time.
- Mass loading $\eta$, or TNG's scaling $\eta\propto\sigma^{-2}$ with a velocity floor and metallicity-dependent energy reduction.
- Whether winds are hydrodynamically decoupled and when they recouple — which in TNG-style models effectively decides how much CGM material the wind interacts with. → [[Galactic winds]]

**AGN feedback:**
- Seed mass and seeding halo threshold
- Accretion boost factor or Bondi exponent $\beta_{\rm BH}$, since resolved density and sound speed aren't the Bondi-radius values
- Radiative and coupling efficiencies for the quasar mode
- Low-accretion mode: transition Eddington ratio, kinetic efficiency, burst energy threshold (TNG); or $\Delta T_{\rm AGN}$ (EAGLE/FLAMINGO); or jet velocity

**Star formation:** density threshold, efficiency per free-fall time, EOS stiffness. **Matters less** — self-regulation means the SFR is set by how fast feedback removes gas, not how fast gas turns into stars.

## What they calibrate against

Overwhelmingly the **$z=0$ galaxy stellar mass function**. Stellar feedback sets the faint-end slope; AGN sets the bright-end cutoff. Beyond that, the choice reveals what the project is for:

| Project | Targets |
|---|---|
| EAGLE | SMF + $z=0$ galaxy sizes |
| FLAMINGO | low-$z$ SMF + cluster gas fractions |
| BAHAMAS | same, by hand |
| COLIBRE | $z\approx0$ SMF, sizes, BH masses in massive galaxies |
| TNG | SMF, cosmic SFRD, SHMR, group/cluster $f_{\rm gas}$, BH masses, sizes — looser |

EAGLE added sizes because the SMF alone left a degeneracy: models matching the mass function produced galaxies far too compact. Fixing that drove the switch from a Bondi boost factor to viscosity-limited accretion.

FLAMINGO targets $f_{\rm gas}$ because it exists to predict baryonic effects on the matter power spectrum, and that's what controls it.

COLIBRE's cold gas (HI, molecular) is a **prediction**, not a target — the stronger claim, and probably the right design choice given the ISM model.

> **Notably absent from every target list:** anything at high redshift, anything about the CGM, kinematics, clustering, or morphology. Those are the predictions. → [[Predictive power]]

## How it's actually done

**Old way:** by hand. Run a 25 Mpc box, look at the SMF, adjust, repeat, for months. EAGLE was calibrated this way and explicit about it.

**Current standard: emulation.** FLAMINGO introduced it — Gaussian process emulators trained on Latin hypercubes of 32 smaller-volume simulations, modelling how the SMF and cluster gas fractions vary with the subgrid parameters; then MCMC over the emulator finds the values best reproducing the target data, accounting for observational errors. Four parameters. Fiducial: $f_{\rm SN}\approx0.24$, $\Delta v_{\rm SN}\approx560$ km/s, $\Delta T_{\rm AGN}\approx10^{7.95}$ K, $\beta_{\rm BH}\approx0.51$.

COLIBRE does the same for a model with a resolved cold phase (Chaikin et al. 2025).

> **The emulator buys something conceptually important beyond objectivity.** Because it maps parameters to observables, you can *invert* it: ask for a model reproducing cluster gas fractions shifted $-8\sigma$ from the data while still matching the SMF, and it hands you the parameters. FLAMINGO ships a suite of these.
>
> The result: **model variations get defined by the data they were calibrated to rather than by parameter values** — a far more meaningful axis, since no single parameter maps to a single observable.

## The convergence problem

Subgrid parameters are resolution-dependent by construction, because the numerical losses they compensate for depend on resolution. Two options:

**Weak convergence** (EAGLE, FLAMINGO): recalibrate at each resolution. FLAMINGO calibrates separately for each of its three resolutions; EAGLE has Ref-L100N1504 and Recal-L025N0752 with different parameters. Sensible galaxies everywhere, but **the higher-resolution run is not a converged version of the lower one — it's a different model.**

**Strong convergence** (TNG across TNG50/100/300): keep parameters fixed. TNG50 galaxies are systematically different (higher SFRs at low mass, different sizes) rather than simply better resolved.

> **Relevant to disk size work:** any TNG-resolution-level difference is partly this, not physics. → [[Pillepich — disks in the first billion years]]

## What it costs you

**A calibrated observable carries no evidential weight.** If TNG reproduces the $z=0$ SMF, that tells you the calibration worked, nothing about ΛCDM. The genuine tests are the untargeted quantities — and the field is reasonably disciplined about this in principle and sloppy in practice, especially in press coverage.

**Degeneracy is the deeper issue.** Stellar and AGN feedback trade off continuously; many parameter combinations fit the SMF equally well while predicting very different CGM properties, gas fractions, and metal distributions. Precisely why FLAMINGO ships variations rather than a single model, and why CAMELS exists.

> **The recurring conference question:** once recalibrated, is there an observable that distinguishes model A from model B, or are they degenerate at the level of the calibration data? Applies to [[Huško — hybrid AGN in COLIBRE]], [[Trinca — multi-regime accretion disc]], and most "we added physics X" talks.

## The dissenting approach

FIRE declines to calibrate feedback at all. Energy, momentum and mass return come from STARBURST99 given each star particle's age and metallicity; there is no wind mass loading parameter. The claim is that at ~100 $M_\odot$ resolution the Sedov phase is marginally resolved, so no compensation is needed.

> **Caveat worth being clear-eyed about.** Not tuning feedback ≠ having no free parameters. Star formation efficiency in self-gravitating gas, the resolution itself, and (in CR runs) the diffusion coefficient calibrated against $\gamma$-ray luminosities all function as tuned quantities. The difference is real but narrower than the framing suggests — and it costs you ever having a statistical population.
