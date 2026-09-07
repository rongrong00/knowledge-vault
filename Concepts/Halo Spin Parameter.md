---
title: Halo Spin Parameter
aliases: [spin parameter, lambda, Bullock spin, Peebles spin, lognormal spin distribution]
type: concept
tags: [astro/dynamics, astro/cosmology, physics/gravity, sim/methods]
status: growing
created: 2026-09-03
updated: 2026-09-03
---

# Halo Spin Parameter

> A dimensionless measure of how much of a halo's support against gravity comes from
> rotation. Typical values are a few percent — halos are pressure-supported, not
> rotating — and the distribution is roughly lognormal with a factor-of-two width,
> almost independent of mass and epoch.

## Definitions

**Peebles (1969):**
$$\lambda=\frac{J\,|E|^{1/2}}{G\,M^{5/2}}$$
the ratio of the halo's angular momentum to what it would need for full rotational
support. Needs the total binding energy $E$, which is expensive and ill-defined at the
halo edge.

**Bullock+01:**
$$\lambda'=\frac{j}{\sqrt2\,V_{\rm vir}R_{\rm vir}}=\frac{J}{\sqrt2\,M V_{\rm vir}R_{\rm vir}}$$
the same idea evaluated at the virial radius, needing only enclosed mass, radius and
angular momentum. For a truncated singular isothermal sphere $\lambda'=\lambda$; for an
NFW halo $\lambda'\simeq\lambda f_c^{-1/2}$ with Mo, Mao & White's energy factor
$f_c\simeq\tfrac23+(c/21.5)^{0.7}$. Fits differ by $\sim10\%$ between conventions — Zjupa &
Springel's Illustris fit is rescaled by 1.1 to Bullock's.

## Where it comes from — tidal torque theory

A non-spherical protohalo is torqued by the tidal field of its neighbours while it is
still growing linearly (Doroshkevich 1970; White 1984 — Peebles 1969 treated a sphere,
for which the first-order torque vanishes):

$$J_i \;\propto\; a^2\dot D\;\epsilon_{ijk}\,T_{jl}\,I_{lk}$$

the antisymmetric product of the tidal tensor $T$ and the protohalo's inertia tensor $I$.
Only the **misaligned** part of the two torques (Lee & Pen 2000). $J$ grows $\propto t$
($\propto a^{3/2}$ in Einstein–de Sitter) until **turnaround**, when the region decouples
from the expansion and torquing shuts off. Because torques act only during linear growth,
the halo ends up far from rotational support: $\lambda\sim0.03$–$0.04$.

## Why it is nearly independent of mass and redshift

$\lambda$ is built to be self-similar. In TTT $J\propto M^{5/3}$ for the Lagrangian mass,
and a virialized halo has $E\propto GM^2/R\propto M^{5/3}$, so
$\lambda\propto M^{5/3}\,M^{5/6}\,M^{-5/2}=M^0$. In Bullock's form, $j\propto M^{2/3}$,
$V\propto M^{1/3}$, $R\propto M^{1/3}$, so $\lambda'\propto M^0$ again. The $\propto t$ growth
of $J$ is likewise scaled out by the growth of $M$ and $R$. Empirically the median drifts
by at most tens of percent over mass and redshift (Bett+07; Macciò+07, 08) — which is
what the near-static spin distribution in [[Research Exam]] Figure 1 checks.

## Why the shape is lognormal

**The empirical fact first.** Barnes & Efstathiou (1987) and Bullock+01 fit a lognormal,
$$P(\lambda')\,d\lambda'=\frac{1}{\lambda'\sqrt{2\pi}\,\sigma}\exp\!\left[-\frac{\ln^2(\lambda'/\lambda'_0)}{2\sigma^2}\right]d\lambda',\qquad \lambda'_0=0.035\pm0.005,\ \sigma=0.5\pm0.3,$$
and it describes the bulk well. A width $\sigma=0.5$ means a factor $e^{0.5}\simeq1.65$
scatter — a 68% range of roughly $0.02$–$0.06$.

**Linear theory gives the core.** Each Cartesian component of $J$ in TTT is a sum over
many independent Fourier modes of the tidal field, so by the central limit theorem each
component is approximately Gaussian with zero mean. The magnitude $|J|$ of a 3D Gaussian
vector is then **Maxwellian** — a $\chi$ distribution with three degrees of freedom:
rising as $J^2$ at small $J$, falling as a Gaussian at large $J$. On a logarithmic axis
that is a nearly symmetric bump, which is why it *looks* lognormal in the core.

**Nonlinear assembly makes it lognormal.** After turnaround the halo grows by mergers and
accretion, and each event changes $J$ by a random *fractional* amount — Vitvitska+02's
random walk. Multiplicative random changes mean $\ln J$ is a **sum** of random increments,
so the central limit theorem now acts in log space and drives the distribution toward
lognormal. The more assembly events a halo has had, the closer to lognormal it gets;
this is also why the shape has no preferred epoch.

**But the tails are not lognormal.** Bett+07 (Millennium) showed the lognormal fails at
both ends and proposed
$$P(\lambda)\propto\left(\frac{\lambda}{\lambda_0}\right)^3\exp\!\left[-\alpha\left(\frac{\lambda}{\lambda_0}\right)^{3/\alpha}\right],\qquad \lambda_0\simeq0.043,\ \alpha\simeq2.5.$$
The power-law rise at small $\lambda$ is the fingerprint of the Maxwellian — a 3D random
vector cannot have a super-exponential cutoff at zero magnitude the way a lognormal does.
So the honest statement is: **lognormal in the core from linear torques plus a merger
random walk; power-law low-end from the vector nature of $J$.**

## What the width comes from

Two sources of scatter: the misalignment angle between $T$ and $I$ in the initial
conditions (Lee & Pen 2000), and the merger random walk afterwards (Vitvitska+02). The
latter is also why the spin **decorrelates over a few Gyr** (Benson+20) and why its
orientation flips, especially in the inner halo (Bett & Frenk 2012, 2016) — the physical
motivation for measuring spin at an earlier epoch in [[Research Exam]].

## Baryonic effects

Full-physics halos sit at slightly higher $\lambda$ than their DM-only counterparts —
a few-percent, feedback-dependent shift (Bryan+13) from baryons condensing and
exchanging angular momentum with the dark matter, and from the halo boundary shifting.
Visible in Lumina vs Lumina-DM at every redshift.

## Connections

- [[Research Exam]] · [[Research Exam — Q&A]]
- [[Dynamical friction]] — the mechanism by which mergers redistribute $J$
- [[Non-equilibrium Thermochemistry]]

## Sources

- Peebles 1969; Doroshkevich 1970; White 1984 — tidal torque theory
- Barnes & Efstathiou 1987; Bullock+01 — lognormal fits
- Lee & Pen 2000 — misalignment; Vitvitska+02 — merger random walk
- Bett+07; Macciò+07, 08 — shape, tails, mass/redshift independence
- Zjupa & Springel 2017 — Illustris; Bryan+13 — baryonic offset
