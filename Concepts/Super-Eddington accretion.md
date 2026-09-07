---
title: Super-Eddington accretion
type: concept
tags: [astro/BH, astro/accretion]
status: growing
created: 2026-07-29
updated: 2026-09-02
---
# Super-Eddington accretion

Up: [[MOC - CGF 2026]] · Related: [[Eddington limit]], [[Accretion disc states]], [[Equilibrium spin]], [[Trinca — multi-regime accretion disc]]

---

> **Notational warning.** Some authors fix $\eta = 0.1$ in $\dot{M}_{\rm Edd}$, others use the actual spin-dependent value. $\dot{m} = 10$ can mean different physical inflow rates in different talks. Check.

## Escape routes

The [[Eddington limit]] derivation assumes spherical symmetry, steady state, Thomson-only opacity, and freely escaping radiation. Four ways out:

**Geometry.** Disk: inflow equatorial, radiation polar. The two aren't in each other's way. Worth a factor of a few alone.

**Photon trapping** — the important one. At high $\dot{m}$ the disk is so optically thick that diffusion is slower than inflow:

$$t_{\rm diff} > t_{\rm inflow} \implies R_{\rm trap} \sim \dot{m}R_s, \qquad R_s = \frac{2GM}{c^2}$$

Inside $R_{\rm trap}$ photons are advected in and swallowed. This is the slim disc regime. Consequence:

$$L \approx L_{\rm Edd}(1 + \ln\dot{m}), \qquad \eta \propto \dot{m}^{-1}$$

So $\dot{m} = 100$ gives $L$ only a few $\times L_{\rm Edd}$. **The limit on *luminosity* holds approximately; on *accretion rate* it does not.**

**Porosity.** Clumpy flow: photons escape through low-density channels, mass falls through dense ones.

**Magnetic support.** In a MAD, magnetic pressure supports gas against radiation; much of the energy leaves as Poynting flux.

## Two gains, one cost

Helps BH growth twice over:
1. High supply rate.
2. Collapsed $\eta$ means **less feedback energy per unit mass accreted** → far less self-regulation.

Cost: radiation- and magnetically-driven winds strip much of the inflow before the horizon,

$$\dot{M}_\bullet \ll \dot{M}_{\rm supply}$$

This is what the accretion efficiencies in [[Huško — hybrid AGN in COLIBRE]] parameterize. **Super-Eddington *inflow* ≠ super-Eddington *growth*.**

## Why it matters

$10^9\,M_\odot$ holes at $z \approx 7$, ~750 Myr after the Big Bang. From a $100\,M_\odot$ remnant:

$$N = \ln(10^9/10^2) \approx 16\ \text{e-foldings}, \qquad t = N\, t_{\rm Sal} \approx 720\ \mathrm{Myr}$$

Requires continuous Eddington accretion at duty cycle ~1 for essentially all the time available. Not plausible. Three escapes:

- heavy seeds ($10^4$–$10^5 M_\odot$ direct collapse)
- lower $\eta$
- super-Eddington episodes

JWST sharpens it — $z>4$ AGN more abundant and more massive relative to hosts than expected; little red dots make it worse.

## Observational evidence

**Neutron star ULXs** are the cleanest case. M82 X-2 and others show pulsations → accretor is $1.4\,M_\odot$ radiating $10^{39}$–$10^{41}$ erg s$^{-1}$, hundreds of times its own $L_{\rm Edd}$, with no mass ambiguity to hide behind. SS 433 is Galactic. TDEs pass through a super-Eddington phase at peak.

**Missing:** any direct *spin* probe in this regime. Reflection spectroscopy relies on the ISCO feature, which washes out once $H/R \sim 0.5$. So the [[Equilibrium spin]] spin-down prediction is untestable exactly where it does the most work.
