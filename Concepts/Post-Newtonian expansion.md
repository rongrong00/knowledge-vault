---
title: Post-Newtonian expansion
type: concept
tags: [physics/gravity, astro/dynamics]
status: growing
created: 2026-07-29
updated: 2026-09-02
---
# Post-Newtonian expansion

Up: [[MOC - CGF 2026]] · Related: [[Johansson — KETJU]], [[Dynamical friction]]

---

A systematic approximation to general relativity valid when gravity is weak and motions are slow. **Not full GR** — an expansion in $v/c$, not a solution of the Einstein field equations.

Expansion parameter:

$$\epsilon \sim \frac{v^2}{c^2} \sim \frac{GM}{rc^2} \sim \frac{R_s}{r}$$

(the forms are equivalent for a bound orbit by the virial theorem, $v^2 \sim GM/r$)

Order $n$PN means order $\epsilon^n$, i.e. $c^{-2n}$:

$$\mathbf{a} = \mathbf{a}_{\rm N} + c^{-2}\mathbf{a}_{\rm 1PN} + c^{-4}\mathbf{a}_{\rm 2PN} + c^{-5}\mathbf{a}_{\rm 2.5PN} + c^{-6}\mathbf{a}_{\rm 3PN} + c^{-7}\mathbf{a}_{\rm 3.5PN}$$

## What each order does

**1PN, 2PN, 3PN — conservative.** Pericentre precession, modified orbit shape, energy conserved. 1PN gives the Mercury calculation:

$$\Delta\varpi = \frac{6\pi GM}{ac^2(1-e^2)} \ \text{per orbit}$$

**2.5PN — the first dissipative term.** Gravitational radiation reaction: the orbit loses energy and angular momentum, shrinks, and circularizes. **Without it there is no inspiral.** Reproduces the quadrupole formula:

$$\left\langle\frac{dE}{dt}\right\rangle = -\frac{32}{5}\frac{G^4m_1^2m_2^2(m_1+m_2)}{c^5a^5(1-e^2)^{7/2}}\left(1+\frac{73}{24}e^2+\frac{37}{96}e^4\right)$$

> The $(1-e^2)^{-7/2}$ factor is why eccentricity matters so much — an $e=0.9$ binary radiates **hundreds of times faster** than a circular one at the same $a$. This is exactly why KETJU's eccentricity distributions are a headline result and why PTA predictions depend on them.

**3.5PN** — next dissipative correction.

**Spin terms** — spin–orbit at 1.5PN, spin–spin at 2PN.

## Where it fails

As $r \to$ few $R_s$, $\epsilon \to 1$ and the series stops converging. No PN order captures the last few orbits, the plunge, the merger, or the ringdown.

There's also **no horizon** in the formalism: the black holes are point masses with corrections, so nothing prevents them passing through each other if you integrate too far.

## Division of labour with numerical relativity

| | Covers | Cost |
|---|---|---|
| **PN** | long wide-separation inspiral, $10^6$ orbits | cheap — ordinary ODE integrators on Newtonian-looking equations |
| **NR** | last tens of orbits, plunge, merger, ringdown | enormous — Einstein equations on a grid |

For PTA and LISA predictions this works because what you want from a galaxy-scale simulation is the **rate**, the **mass ratio**, and the **eccentricity at entry** into the GW-driven regime. All set well before the strong-field phase. The waveform then comes from NR-calibrated templates or effective-one-body models.

> Remnant properties — final spin, recoil kick — are strong-field quantities, so they come from NR fitting formulae, not from a PN code. Worth knowing if a talk quotes recoil velocities.
