---
title: Trinca — multi-regime accretion disc
type: literature
authors: Trinca
year: 2026
venue: CGF 2026, Garching
tags: [talk, conference/CGF2026, astro/BH, astro/accretion]
status: growing
read: 2026-07-29
---
# Trinca — multi-regime accretion disc, BH growth and spin

Up: [[MOC - CGF 2026]] · Related: [[Accretion disc states]], [[Super-Eddington accretion]], [[Equilibrium spin]], [[Huško — hybrid AGN in COLIBRE]]

---

## Background

**Alessandro Trinca.** Comes from the **CAT** semi-analytic model (Trinca et al. 2022) and the Rome/Insubria high-redshift line — driving problem is growing seeds fast enough for $z>6$ quasars and now the JWST AGN. Recent coauthor with Zana, Capelo, Lupi and Schneider on super-Eddington accretion in protogalactic cores.

> Emphasis is **early BH growth**, so the slim-disc regime is the point rather than a completeness item — the opposite emphasis from [[Huško — hybrid AGN in COLIBRE]], whose model is really about jets and quenching at the massive end.

## The model: adapted from Kao et al. (2025)

Kao et al. 2025, arXiv:2504.19281 (Kao, Capelo, Cenci, Mayer, Lupi, Sala). Zurich/Insubria lineage: Fiacconi+18 α-disc → Cenci+21 in GIZMO → this.

- **Subgrid disc** with an inner **photon-trapping** region from radiation-hydrodynamics fitting formulae, plus an outer thin α-disc with three regions
- Spin prescription transitioning between **Bardeen–Petterson** and inner **thick-disc precession** depending on accretion rate
- Their idealized circumnuclear-disc runs found that **misaligned inflows onto an initially aligned BH–disc system produce very high Eddington ratios**, because the inflow rapidly strips the disc's angular momentum

## What he reported

1. **Repeated bursts of super-Eddington accretion**
2. **Accretion smoothed by disc-mediated growth** — the subgrid disc acts as a low-pass filter, so single-timestep spikes in resolved inflow get integrated away. Surviving bursts are long compared to the disc drain time, not numerical noise.
3. **Final spin goes up**, because of later prolonged sub-Eddington accretion

> This matches the "Power-Law $\dot M$" track in [[Equilibrium spin]] (Ricarte+23): a seed starts super-Eddington near $a\approx0$, rises to ~0.9 in the thin-disc phase, then declines again in the hot regime, running out of fuel before reaching the equilibrium spin for its final Eddington ratio.
>
> So the result is **consistent** with that picture rather than in tension — but it also means the early spin history gets erased.

## Where the interesting question sits (revised after the result)

**Best — the erasure question**
> Does the final spin retain any memory of the burst history, or does the thin-disc phase erase it? If it's erased, what observable distinguishes your model from one without super-Eddington bursts?

Same shape as the degeneracy question for Huško — what does the added machinery buy?

**The mass, not the spin**
> Even if spin memory is erased, the mass isn't. If bursts spin the hole down, jets are weak during them, growth is unimpeded, and you get a more massive BH at fixed gas supply. Does the burst phase leave its imprint on $M_\bullet$–$M_*$ or the high-$z$ BH mass function?

**Coherence — my pick**
> Prolonged sub-Eddington spin-up requires the angular momentum direction to stay roughly fixed for a Gyr. How coherent is accretion in the thin-disc phase? Why doesn't misalignment interrupt it the way it *triggers* the earlier bursts?

The same mechanism he invoked for the bursts is now implicitly assumed not to operate later. Asking why the physics switches off is fair, specific, and he'll have a real answer.

**The physics gap**
> Kao et al. treat the super-Eddington regime via photon trapping — a radiation-hydrodynamics picture, not a magnetized one. Ricarte-style spin-down requires the MAD state and Blandford–Znajek extraction. Does the model include BZ spin-down in that state, or does the inner disc spin the hole *up* during bursts?

Answer determines the sign of the whole feedback loop: spun-up → strong jets → self-limiting growth; spun-down → easy growth.

**The averaging question**
> Does the subgrid disc vector-average the misalignment? Kao's mechanism triggers bursts through misaligned inflow, but a disc with a long drain time averages the incoming angular momentum, which would give coherent spin-up instead.

Takes his own two ingredients and points out they pull against each other.

**Parameter sensitivity**
> What sets the drain timescale, and how does the burst duty cycle respond to the circularization radius?

In Fiacconi-style models the drain time depends on disc mass and the circularization radius of the inflow — and that radius is a subgrid parameter, not resolved. If bursts are robust to it, real result; if they wash out, less so.

## Caveat on the porting

Kao et al. were **idealized circumnuclear-disc** simulations. At cosmological resolution the angular momentum direction of "inflowing gas" is measured on kpc rather than pc scales, so the misalignment statistics driving everything are set by resolved gas, not by the physics they validated.

## Cross-talk

- Spin-down vs chaotic accretion are **degenerate in outcome** here — if bursts are triggered by misaligned inflow, accreted angular momentum directions are uncorrelated by construction, suppressing spin independently of any magnetic mechanism.
- OpenGadget3 (Sala et al. 2024) finds the coherent→uncorrelated transition near $2\times10^7M_\odot$, with counter-rotating accretion more likely at higher BH mass. Does this model reproduce that scale, and is it converged?

---

## What actually happened

*(notes from the talk)*
