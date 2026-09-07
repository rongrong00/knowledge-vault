---
title: Dynamical friction
type: concept
tags: [astro/dynamics, physics/gravity]
status: growing
created: 2026-07-29
updated: 2026-09-02
---
# Dynamical friction

Up: [[MOC - CGF 2026]] · Related: [[Johansson — KETJU]], [[Star clusters and NSCs]], [[Post-Newtonian expansion]]

---

Drag on a massive object moving through a sea of lighter particles — stars, dark matter, gas. Chandrasekhar (1943). **A collective effect, not collisions**: no particle needs to touch anything.

**Physical picture.** A mass $M$ moving at $\mathbf{v}$ deflects the particles it passes. They're pulled toward its path, and because they take time to respond, the enhanced density builds up *behind* it — a wake. That overdensity pulls backward. The object is decelerated by its own gravitational shadow.

---

## Step 1: a single encounter

Hyperbolic Kepler orbit. Relative speed unchanged, direction rotates by $\theta$:

$$\tan\frac{\theta}{2} = \frac{G(M+m)}{bV^2} \equiv \frac{b_{90}}{b}$$

Half-angle identities give $\sin\theta = 2bb_{90}/(b^2+b_{90}^2)$ and $1-\cos\theta = 2b_{90}^2/(b^2+b_{90}^2)$. Converting via $\Delta\mathbf{v}_M = \frac{m}{M+m}\Delta\mathbf{V}$:

$$\Delta v_{M,\perp} = \frac{m}{M+m}\frac{2bb_{90}V}{b^2+b_{90}^2}, \qquad \Delta v_{M,\parallel} = -\frac{m}{M+m}\frac{2b_{90}^2V}{b^2+b_{90}^2}$$

> **The crucial observation.** The perpendicular kick has random azimuth → averages to zero over many encounters, surviving only in the *mean square* (that's two-body relaxation, a diffusive effect). The parallel component is **always negative regardless of encounter geometry** → accumulates linearly. That systematic piece is dynamical friction.

## Step 2: integrate over impact parameter

Encounter rate in $[b, b+db]$ is $nV\cdot2\pi b\,db$:

$$\frac{dv_\parallel}{dt} = -4\pi n\frac{m}{M+m}b_{90}^2V^2\int_0^{b_{\max}}\frac{b\,db}{b^2+b_{90}^2}$$

$$\int_0^{b_{\max}}\frac{b\,db}{b^2+b_{90}^2} = \frac{1}{2}\ln\left(\frac{b_{\max}^2+b_{90}^2}{b_{90}^2}\right) \simeq \ln\frac{b_{\max}}{b_{90}} \equiv \ln\Lambda$$

> **Origin of the Coulomb logarithm.** The integrand falls as $1/b$, so each *logarithmic interval* in impact parameter contributes equally — a 1 pc encounter and a 100 pc encounter matter the same amount. Diverges logarithmically at large $b$ and must be cut off at the system size. A genuine sensitivity to global structure: the local formula can never be self-contained.
>
> In simulations where DF is applied as a subgrid force, $\ln\Lambda$ ($\sim3$–30) is effectively a **free parameter**, and sinking timescales inherit that uncertainty.

With $b_{90} = G(M+m)/V^2$ and $\rho = nm$:

$$\frac{dv_\parallel}{dt} = -\frac{4\pi G^2\rho(M+m)\ln\Lambda}{V^2}$$

## Step 3: integrate over field star velocities

Drag acts along $\mathbf{V} = \mathbf{v}_M - \mathbf{v}_m$, not along $\mathbf{v}_M$:

$$\frac{d\mathbf{v}_M}{dt} = -4\pi G^2(M+m)m\ln\Lambda\int f(\mathbf{v}_m)\frac{\mathbf{v}_M-\mathbf{v}_m}{|\mathbf{v}_M-\mathbf{v}_m|^3}d^3\mathbf{v}_m$$

> **The elegant step.** That integrand is exactly the Coulomb/Newtonian $1/r^2$ kernel, with *velocity* space playing the role of position space. For isotropic $f$, the **shell theorem** applies verbatim: field stars with $|\mathbf{v}_m| > |\mathbf{v}_M|$ form shells exerting zero net force; slower ones act as if concentrated at the origin.
>
> **Only stars moving slower than $M$ contribute.** The drag depends on the enclosed "mass" in velocity space, not on total density.

$$\frac{d\mathbf{v}_M}{dt} = -16\pi^2 G^2 m(M+m)\ln\Lambda\left[\int_0^{v_M} f(v_m)v_m^2\,dv_m\right]\frac{\mathbf{v}_M}{v_M^3}$$

## Step 4: Maxwellian background

With $X \equiv v_M/(\sqrt2\sigma)$:

$$\int_0^{v_M} f v^2 dv = \frac{n_0}{4\pi}\left[\mathrm{erf}(X)-\frac{2X}{\sqrt{\pi}}e^{-X^2}\right]$$

Taking $M \gg m$:

$$\frac{d\mathbf{v}_M}{dt} = -\frac{4\pi G^2M\rho\ln\Lambda}{v_M^3}\left[\mathrm{erf}(X)-\frac{2X}{\sqrt\pi}e^{-X^2}\right]\mathbf{v}_M$$

## Limits

**Slow ($X\ll1$):** bracket $\to 4X^3/(3\sqrt\pi)$, and $v_M^3$ cancels:

$$\frac{d\mathbf{v}_M}{dt} \propto -\frac{G^2M\rho}{\sigma^3}\mathbf{v}_M$$

Linear drag, like Stokes flow. Friction timescale independent of speed.

**Fast ($X\gg1$):** bracket $\to1$:

$$\left|\frac{d\mathbf{v}_M}{dt}\right| \to \frac{4\pi G^2M\rho\ln\Lambda}{v_M^2}$$

The object outruns its own wake. **Maximum drag near $v_M \sim \sigma$** — objects moving at the background's own dispersion sink most efficiently.

Force: $F \propto M^2\rho/v^2$ — one factor of $M$ from the wake's mass, one from $M$'s coupling to it.

## The wake picture

Equivalent derivation (linear response, Mulder 1983): compute the induced density perturbation $\delta\rho$ and integrate its pull on $M$ directly. Same answer.

Chandrasekhar's version counts momentum transferred in individual encounters; the wake view counts the collective density response. Worth internalizing both, because the wake picture makes clear **when DF fails** — e.g. supersonic motion through gas, where the wake becomes a Mach cone with different scalings (Ostriker 1999 — Eve, not Jerry), or inhomogeneous backgrounds on the scale of $b_{\max}$.

## Assumptions

1. **Infinite homogeneous background** — forces $b_{\max}$ to be chosen by hand
2. **Straight-line unperturbed trajectories** — fails for $b \lesssim b_{90}$
3. **Uncorrelated encounters** — no collective modes, no resonances. Resonant DF can dominate in cored profiles.
4. **Isotropic $f$** — needed for the shell theorem
5. **Background unaffected** — fails once $M$ has depleted or heated its surroundings

> **Point 5 is the important one.** The derivation assumes an inexhaustible supply of slow field stars. A sinking black hole ejects them. Once the reservoir at $|\mathbf{v}_m| < v_M$ empties, the formula stops applying.
>
> **That failure — not any breakdown of the algebra — is why BH binaries stall.** The final parsec problem is the gap between DF (works kpc → pc) and GW emission (works only below ~pc). See [[Johansson — KETJU]].

## Why it matters here

- After a galaxy merger, two BHs start kpc apart. DF against stars and DM brings them to a few pc.
- $F \propto M^2$ means a BH **embedded in an NSC** sinks far more efficiently than a naked one — why [[Partmann — IMBHs in dwarf galaxies]] finds NSCs matter, and why bare IMBHs in dwarfs stall longer than a Hubble time.
