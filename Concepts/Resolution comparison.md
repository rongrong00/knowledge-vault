---
title: Resolution comparison
type: concept
tags: [sim/methods, sim/TNG, sim/COLIBRE]
status: growing
created: 2026-07-29
updated: 2026-09-02
---
# Resolution comparison

Up: [[MOC - CGF 2026]] · Related: [[Simulation landscape]], [[Calibration and tuning]], [[Predictive power]], [[Pillepich — disks in the first billion years]]

---

## The numbers

| | baryon mass ($M_\odot$) | box (cMpc) |
|---|---|---|
| COLIBRE m5 | ~$10^5$ | ≤100 |
| COLIBRE m6 | ~$10^6$ | ≤200 |
| COLIBRE m7 | ~$10^7$ | ≤400 |
| TNG50 | $8.5\times10^4$ | 50 |
| TNG100 | $1.4\times10^6$ | ~110 |
| TNG300 | $1.1\times10^7$ | ~300 |
| EAGLE Ref-L100 | $1.8\times10^6$ | 100 |
| FLAMINGO L1_m8 | $10^8$ | 1000 |
| **Lumina** | $3.6\times10^6$ | **500** |

COLIBRE's largest runs use **136 billion particles ($5\times3008^3$)**. The factor 5 rather than 4 is DM supersampling — one gas particle plus four DM particles, so DM and baryon masses come out similar.

> **Why supersample.** To suppress spurious energy transfer from DM to stars — two-body heating that puffs up galaxy sizes. An underappreciated systematic for anyone measuring sizes.

COLIBRE calibration targets: $z\approx0$ SMF, galaxy sizes, and BH masses in massive galaxies. Cold gas is a *prediction*. Reported convergence is good, but in the **weak** sense — recalibrated per resolution, not fixed-parameter. → [[Calibration and tuning]]

The m5 runs are the notable entry: roughly TNG50 resolution in a volume 500× larger. That combination is what makes a resolved multiphase ISM affordable at population-statistics scale.

## Lumina vs COLIBRE — no clean match

| Against | Lumina has |
|---|---|
| m7 (400 cMpc) | 2× the volume, 8× the gas elements, ~3× better mass resolution |
| m5 (100 cMpc) | 125× the volume, 36× worse resolution |

Lumina sits between them and overlaps neither.

> **Practical consequence:** COLIBRE isn't a clean external check at fixed resolution. m7 is coarser than Lumina; m5 is finer but in a box too small for good statistics on rare high-$z$ systems. **m6 is probably the honest comparison**, with a 15× volume difference as the caveat.

## Why m7 reaches $z=0$ but Lumina stops at $z=3$

Three things, and they compound.

**1. Radiative transfer dominates the cost.** Six-bin M1 means 24 extra evolved variables per cell, each needing a Riemann solve, and the RT Courant condition is set by the *reduced* speed of light rather than the gas sound speed. Even at $c_{\rm red}\sim0.01c$ that's still two orders of magnitude above typical gas velocities, so RT subcycling eats the timestep budget. GPU acceleration makes it feasible, not cheap.

**2. $z=3\to0$ is where most of the wall-clock lives.** 11.5 Gyr versus 2.1 Gyr for everything before — 5× more cosmic time, and the expensive kind: deeper potential wells, denser collapsed structures, more black holes, all forcing shorter timesteps. Stopping at $z=3$ typically saves a factor of several, sometimes close to an order of magnitude.

**3. COLIBRE isn't cheap per particle either.** Non-equilibrium H and He, a dust network, and — the expensive one — an explicit multiphase ISM with **no pressure floor**. Removing the floor is exactly what lets gas cool to low temperatures and high densities, driving the Courant timestep down hard. A deliberate trade: pay in dense-gas timesteps for a resolved cold phase.

**And the science case decides it.** Lumina targets hydrogen and helium reionization; He II reionization completes around $z\approx2.7$, so $z=3$ is the natural endpoint, not a truncation. Nothing left to observe, and the RT would keep costing full price.

> Roughly: **Lumina spends its budget on radiation transport and box size; COLIBRE on reaching the present day with expensive local physics.**

## For the TNG–Lumina size comparison

- Same galaxy formation model → differences are RT, resolution, volume. **Not feedback philosophy.**
- Which means agreement between them tests very little → [[Predictive power]]
- TNG's own resolution-level differences (TNG50 vs 100 vs 300) are partly the strong-convergence choice, not physics
- The external check that would matter: a simulation with genuinely different feedback at comparable resolution. COLIBRE m6, or ask [[Pillepich — disks in the first billion years]] about her resolved-SN runs.
