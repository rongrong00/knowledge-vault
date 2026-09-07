---
title: Eddington limit
type: concept
tags: [astro/BH, astro/accretion, physics/radiation]
status: growing
created: 2026-07-29
updated: 2026-09-02
---
# Eddington limit

Up: [[MOC - CGF 2026]] · Related: [[Super-Eddington accretion]], [[Accretion disc states]]

---

## Setup

Point source of luminosity $L$, isotropic, surrounded by fully ionized hydrogen. Find $L$ where outward radiation force balances inward gravity.

## Radiation force

Flux at radius $r$:

$$F = \frac{L}{4\pi r^2}$$

Radiation carries momentum at $F/c$ per unit area. Electron Thomson cross-section:

$$\sigma_T = \frac{8\pi}{3}\left(\frac{e^2}{m_e c^2}\right)^2 = 6.65\times10^{-25}\ \mathrm{cm^2}$$

Force on one electron:

$$f_{\rm rad} = \frac{\sigma_T F}{c} = \frac{\sigma_T L}{4\pi r^2 c}$$

Since $\sigma_T \propto m^{-2}$, the proton cross-section is smaller by $(m_p/m_e)^2 \approx 3.4\times10^6$ — protons feel essentially no radiation force.

## The coupling argument

> The step people forget. Radiation pushes electrons out, leaving protons. Any charge separation generates an electrostatic field, and the Coulomb force vastly exceeds both gravity and radiation pressure, so the plasma cannot separate. Electrons drag protons along.

So do force balance on the **electron–proton pair**: cross-section of an electron, mass of a proton.

$$f_{\rm grav} = \frac{GM(m_p+m_e)}{r^2} \simeq \frac{GMm_p}{r^2}$$

## Balance

Both forces $\propto r^{-2}$, so $r$ cancels identically — the result is a statement about luminosity, not about a particular radius. If radiation wins anywhere it wins everywhere.

$$L_{\rm Edd} = \frac{4\pi GMm_pc}{\sigma_T} \approx 1.26\times10^{38}\left(\frac{M}{M_\odot}\right)\ \mathrm{erg\,s^{-1}}$$

## Opacity form

Generalizes to any opacity source:

$$L_{\rm Edd} = \frac{4\pi GMc}{\kappa}, \qquad \kappa_{\rm es} = \frac{\sigma_T}{\mu_e m_p}$$

Pure H: $\kappa_{\rm es} = 0.40$ cm$^2$ g$^{-1}$. Solar: $0.2(1+X) \approx 0.34$.

## Accretion rate and growth

With $L = \eta\dot{M}c^2$:

$$\dot{M}_{\rm Edd} = \frac{L_{\rm Edd}}{\eta c^2} \approx 2.2\times10^{-8}\left(\frac{\eta}{0.1}\right)^{-1}\left(\frac{M}{M_\odot}\right)\ M_\odot\,\mathrm{yr^{-1}}$$

BH gains rest mass at $\dot{M}_\bullet = (1-\eta)\dot{M} \propto M$ → exponential growth, $M(t) = M_0 e^{t/t_{\rm Sal}}$:

$$t_{\rm Sal} = \frac{\eta}{1-\eta}\cdot\frac{\sigma_T c}{4\pi Gm_p} = \frac{\eta}{1-\eta}\times 450\ \mathrm{Myr} \approx 50\ \mathrm{Myr}\ (\eta=0.1)$$

> You'll see 45 Myr quoted too — that drops the $(1-\eta)$ factor. Don't chase the discrepancy.

## Assumptions, and where each fails

1. **Spherical symmetry** — in a disk, gas comes in equatorially, radiation leaves polarly. Breaks the argument entirely.
2. **Steady state** — it's a force balance, not an equation of motion. Gas with inward momentum can fall through.
3. **Fully ionized metal-free H** — with dust, $\kappa$ can be $100\times$ larger, dropping the effective limit correspondingly.
4. **Thomson only** — line opacity vastly exceeds $\sigma_T$ at specific frequencies (hot star winds). Klein–Nishina *raises* the limit at $h\nu \gtrsim m_ec^2$.
5. **Free escape of radiation** — fails at high $\dot{m}$ → [[Super-Eddington accretion]].
6. **Homogeneous medium** — porosity lets photons leak through low-density channels.
7. **Newtonian gravity, no self-gravity**
8. **Isotropic emission** — beaming allows exceeding the isotropic-equivalent limit.
9. **Only radiation opposes gravity** — ignores magnetic pressure, rotation.
10. **Quasi-neutral well-coupled plasma**

> $L_{\rm Edd}$ is a *characteristic scale*, not a boundary. Every real system violates at least one assumption, which is why super-Eddington sources aren't paradoxes.
