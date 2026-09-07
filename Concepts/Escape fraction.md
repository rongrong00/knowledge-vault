---
title: Escape fraction
type: concept
tags: [astro/ISM, astro/reionization]
status: growing
created: 2026-07-29
updated: 2026-09-02
---
# Escape fraction

Up: [[MOC - CGF 2026]] · Related: [[Galactic winds]], [[Reina-Campos — SCALES]], [[Simulation landscape]], [[Resolution comparison]]

---

The fraction of ionizing photons produced by a galaxy's stars that actually escape into the IGM instead of being absorbed inside the galaxy. **The single largest uncertainty in reionization modelling.**

$$f_{\rm esc} = \frac{\dot{N}_{\rm ion,\,escaped}}{\dot{N}_{\rm ion,\,produced}}$$

for $h\nu > 13.6$ eV, $\lambda < 912$ Å (Lyman continuum → "LyC escape fraction"). Typically a few percent to a few tens of percent, varying enormously between galaxies and over time within one galaxy.

## Absolute vs relative — don't confuse them

The *relative* escape fraction is measured against the UV continuum at 1500 Å:

$$f_{\rm esc}^{\rm rel} = f_{\rm esc}^{\rm abs}\times 10^{0.4A_{1500}}$$

Observers often quote the relative version because it doesn't require knowing dust attenuation, **but it isn't the physically meaningful quantity.** Check which a paper means.

## Why it dominates reionization

$$\dot{n}_{\rm ion} = f_{\rm esc}\,\xi_{\rm ion}\,\rho_{\rm SFR}$$

with $\xi_{\rm ion}$ the ionizing photon production efficiency per unit UV luminosity ($\sim10^{25.2}$–$10^{25.6}$ Hz erg$^{-1}$). Reionization requires

$$\dot{n}_{\rm ion} > \frac{n_{\rm H}}{t_{\rm rec}}, \qquad t_{\rm rec} = \left[C\,\alpha_B\,n_{\rm H}(1+z)^3\right]^{-1}$$

with $C = \langle n^2\rangle/\langle n\rangle^2$ the clumping factor.

> $f_{\rm esc}$ enters **linearly and multiplicatively** — a pure efficiency factor in front of everything else. Since $\xi_{\rm ion}$ and $\rho_{\rm SFR}$ are now reasonably constrained by JWST, $f_{\rm esc}$ absorbs most of the remaining ignorance. Usual quoted requirement: $f_{\rm esc}\sim0.1$–0.2 population-averaged.

## Why it's hard — physics

Photoionization cross-section at the Lyman edge is $\sigma_0 = 6.3\times10^{-18}$ cm$^2$, so $\tau=1$ at $N_{\rm HI} = 1.6\times10^{17}$ cm$^{-2}$ — **a tiny column by ISM standards**.

So escape isn't about average conditions at all; it's about whether feedback has carved low-column sightlines. This makes $f_{\rm esc}$ intensely anisotropic and time-variable, spiking a few Myr after a starburst once SNe and radiation pressure have cleared channels, then collapsing again.

> Which is why it couples directly to **clustered feedback and superbubble breakout** — see [[Reina-Campos — SCALES]] and [[Galactic winds]].

## Why it's hard — observations

**You cannot measure it during reionization.** The IGM is opaque to LyC above $z\gtrsim4$, so direct detections are confined to $z\sim0.3$ (HST/COS, LzLCS) and $z\sim3$.

Everything at $z>6$ relies on indirect diagnostics calibrated at low $z$: Ly$\alpha$ profile peak separation, O32, UV slope $\beta$, Mg II, Ly$\alpha$ escape fraction. Whether those calibrations hold at $z=8$ is open.

Foreground contamination is brutal — a chance low-$z$ interloper leaking flux into the LyC band mimics a detection, and several early claimed detections were exactly this.

## For simulations

Central quantity for Lumina and THESAN, and where the resolution problem bites hardest. At $10^6$–$10^7 M_\odot$ gas resolution you **cannot resolve the sub-pc channels through which photons actually escape**, so the emergent escape fraction is partly a property of the ISM model rather than of the physics.

RHD at least computes it self-consistently instead of imposing it, which is the main advantage over post-processing — but "self-consistently at insufficient resolution" is not "correctly."

**The related debate:** which galaxies dominate the budget? Faint dwarfs have shallow potentials and bursty feedback → higher $f_{\rm esc}$, but individually low luminosity. Bright galaxies produce more photons but trap them. The answer determines the required faint-end slope of the UV luminosity function — **which is why box size and dynamic range are the design drivers for Lumina**. See [[Resolution comparison]].

> **Terminology.** The same phrase is used for the **Ly$\alpha$ escape fraction**, a different quantity governed by resonant scattering and dust rather than photoelectric absorption. If someone quotes $f_{\rm esc}$ near unity, they probably mean Ly$\alpha$.
