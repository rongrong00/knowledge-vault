---
title: Accretion disc states
type: concept
tags: [astro/BH, astro/accretion]
status: growing
created: 2026-07-29
updated: 2026-09-02
---
# Accretion disc states

Up: [[MOC - CGF 2026]] · Related: [[Eddington limit]], [[Super-Eddington accretion]], [[Equilibrium spin]], [[Huško — hybrid AGN in COLIBRE]], [[Trinca — multi-regime accretion disc]]

---

Three regimes of accretion disc theory, sorted by Eddington ratio $\dot{m} = \dot{M}/\dot{M}_{\rm Edd}$. The physics of what happens to the dissipated energy changes qualitatively at both ends.

| | Thick disc | Thin disc | Slim disc |
|---|---|---|---|
| Regime | $\dot{m} \lesssim 0.01$ | $0.01 \lesssim \dot{m} \lesssim 1$ | $\dot{m} \gtrsim 1$ |
| Geometry | $H/R \sim 1$ | $H/R \ll 1$ | $H/R \sim 0.5$ |
| Radiative efficiency | low, drops with $\dot{m}$ | high, 0.06–0.4 | low, saturates |
| Feedback mode | jets (+ winds) | thermal isotropic | jets + thermal |
| Archetype | Sgr A*, M87, BCGs | quasars | high-$z$ growth, ULXs |

## Thin disc

Shakura & Sunyaev (1973). Optically thick, geometrically thin, **radiatively efficient**: $t_{\rm cool} \ll t_{\rm inflow}$, so viscously dissipated energy is radiated locally before it can be carried inward.

Efficiency set by the ISCO and therefore by spin — about 5.7% for Schwarzschild, up to ~42% for maximal. Spectrum is a multi-temperature blackbody, the big blue bump. This is a quasar; in feedback terms it maps to isotropic thermal injection representing radiation and broad-line winds.

## Thick disc (ADAF / RIAF)

Takes over at low accretion rates. Density gets low enough that Coulomb coupling between ions and electrons becomes inefficient. Viscous dissipation heats the *ions*; ions can't transfer energy to electrons fast enough; **electrons are what radiate**. So the heat stays in the flow.

Ion temperatures approach virial, pressure support puffs the disc to $H/R \sim 1$, and energy is *advected* into the hole rather than radiated. Efficiency falls roughly linearly with $\dot{m}$.

Compensation: this thick, hot, magnetically-dominated configuration is excellent at launching jets. Large-scale poloidal flux threads the horizon, Blandford–Znajek extraction gives jet powers that can exceed the accretion luminosity, efficiency scaling roughly as $a^2$. This is radio mode / maintenance mode — every BCG, plus Sgr A* and M87.

## Slim disc

Abramowicz et al. (1988). Super-Eddington end. The flow is *so* optically thick that photons are trapped: diffusion time out of the disc exceeds inflow time, so radiation is dragged into the hole with the gas. Efficiency drops again and luminosity grows only logarithmically with $\dot{m}$ — see [[Super-Eddington accretion]].

Rare and short-lived, but relevant for early BH growth and for little red dots.

## The unifying structure

> Radiative efficiency is **non-monotonic** in $\dot{m}$, peaking in the middle and falling at both ends, via two *different* advection mechanisms: thermal energy advected in the thick disc, trapped radiation advected in the slim disc.

The same double-sided structure appears in [[Equilibrium spin]], and for the same underlying reason — the disc is geometrically thick at both ends.

## Why it matters for simulations

Old two-mode AGN prescriptions (quasar mode / radio mode) had the right qualitative structure but a hand-set threshold and hand-set efficiencies. Grounding transitions in disc theory means the Eddington-ratio boundaries, the efficiencies, and the jet-versus-thermal split all follow from $\dot{m}$ and spin rather than from tuned parameters.

> That's the actual argument for the added complexity — and why the degeneracy question is the good one to ask, since the physical motivation is strong regardless of whether the observables end up distinguishable. See [[Calibration and tuning]].
