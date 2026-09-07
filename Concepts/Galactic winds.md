---
title: Galactic winds
type: concept
tags: [astro/feedback, astro/ISM]
status: growing
created: 2026-07-29
updated: 2026-09-02
---
# Galactic winds

Up: [[MOC - CGF 2026]] · Related: [[Cosmic rays]], [[Reina-Campos — SCALES]], [[Schneider — CGOLS outflows]], [[Calibration and tuning]], [[Escape fraction]]

---

## Why simulations need them

Without outflows, cosmological simulations turn far too much baryonic mass into stars — several times the observed values across most of the halo mass range. Winds reconcile the halo mass function with the stellar mass function at the low-mass end (AGN handles the high end).

Three other jobs beyond mass removal:

- **Metal transport.** The mass-metallicity relation and CGM/IGM enrichment are set almost entirely by how much enriched gas is ejected and whether it returns.
- **Angular momentum selection.** Gas reaching the centre has low specific angular momentum. Preferentially ejecting it, and letting higher-$j$ material fall back later, is how simulations make extended disks and bulgeless dwarfs instead of compact spheroids. → relevant to [[Pillepich — disks in the first billion years]]
- **Delaying accretion.** The fountain shifts star formation to lower redshift, fixing "too many stars too early."

## The central number

**Mass loading:** $\eta = \dot{M}_{\rm out}/\mathrm{SFR}$ — solar masses leaving per solar mass of stars formed.

Steeply mass-dependent: $\eta \gtrsim 10$ in dwarfs, $\lesssim 1$ at Milky Way mass. This falloff produces the shape of the stellar-to-halo-mass relation.

> **Reading $\eta$ from papers:** it depends strongly on *where* it's measured (disk scale height? $0.25R_{\rm vir}$? $R_{\rm vir}$?) and what velocity cut counts as "outflowing." A factor of several between papers is often definitional rather than physical.

## Implementations

| Scheme | Codes | Mechanism |
|---|---|---|
| Pure thermal | — | Physically honest, numerically useless |
| Stochastic thermal | EAGLE, COLIBRE | Heat few particles a lot, fixed $\Delta T = 10^{7.5}$ K |
| Kinetic + decoupled | Illustris, TNG | Kick cells to prescribed $v$, decouple hydrodynamically |
| Explicit multi-channel | FIRE | SNe, stellar winds, radiation pressure, photoionization from stellar evolution |
| Delayed cooling / momentum | RAMSES-based | Switch off cooling, or inject terminal remnant momentum |

**Pure thermal.** Dump SN energy as heat into neighbouring gas. At cosmological resolution the heated gas is dense and cools before it expands, so you get almost no wind. **Overcooling** — and essentially every scheme below is a workaround for it.

**Stochastic thermal.** Instead of heating many particles a little, heat a few a lot, with probability set by the energy budget. The wind then emerges from resolved pressure gradients rather than being imposed. The $\Delta T = 10^{7.5}$ K is chosen so the cooling time exceeds the sound-crossing time of the resolution element — a **numerical construct with no physical referent**.

**Kinetic wind particles** (Springel & Hernquist 2003). Stochastically kick gas cells to a prescribed velocity and direction, and **temporarily decouple them hydrodynamically** so they fly through the disk without interacting, recoupling once density drops below a threshold or a timer expires.

TNG specifics: velocity scales with local DM velocity dispersion with a redshift-dependent floor; $\eta \propto \sigma^{-2}$ from an energy-driven scaling; 10% of wind energy thermal; available energy reduced at high metallicity to mimic radiative losses.

> **On decoupling.** It is a straightforward admission that the disk isn't resolved well enough to launch a wind through. Real winds escape via low-density chimneys carved by clustered supernovae, which the simulation can't make. The cost: where and how the wind couples to the CGM is set by a threshold parameter rather than by physics, and CGM predictions inherit that.
>
> This is exactly the gap [[Reina-Campos — SCALES]] is attacking.

**Explicit multi-channel (FIRE).** No decoupling, no imposed velocity. Each star particle injects SN energy and momentum, stellar wind mass and momentum, radiation pressure, and photoionization heating according to stellar evolution models, with the terminal momentum of the remnant injected directly when the Sedov phase is unresolved. Winds emerge as an outcome. Requires ~$10^2$–$10^3 M_\odot$ per element, so no large volumes.

## What real winds look like

Strongly **multiphase**. A hot ($\sim10^7$ K) volume-filling phase carries most of the *energy* and moves fast; cool ($\sim10^4$ K) and molecular material carries most of the *mass* and moves slower, apparently entrained by the hot phase. M82 is the textbook case; at high $z$ they appear as blueshifted absorption in down-the-barrel spectra.

Almost no cosmological simulation resolves this. The **cloud-crushing problem** — how cool clumps survive acceleration rather than shredding — is active, attacked in idealized wind-tunnel simulations. Current answer involves radiative cooling in turbulent mixing layers letting clouds *grow* rather than be destroyed.

> A TNG or EAGLE "wind" should be read as an **effective mass-and-metal-transport prescription** that reproduces the right global budgets, not a model of the outflow itself. That distinction is why the CGM predictions are the weak tier — see [[Predictive power]].

## Winds vs AGN outflows

Separate machinery. Stellar winds dominate below $\sim10^{12}M_\odot$; AGN-driven outflows take over above and are what quench massive galaxies. Some codes let them interact (SIMBA's jets propagate into a medium already stirred by stellar winds), but they're parameterized independently.
