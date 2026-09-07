---
title: TNG-Cluster
aliases: [TNG Cluster, TNG-Cluster simulation]
type: concept
tags: [astro/simulations, astro/clusters, astro/ICM, dataset]
status: growing
created: 2026-09-07
updated: 2026-09-07
---

# TNG-Cluster

> A zoom-in extension of [[IllustrisTNG]] built to fix its worst statistical weakness:
> massive galaxy clusters are rare, so even a 300 Mpc box contains almost none.

## What it is

352 individually re-simulated galaxy clusters, selected from a parent volume of
**1 Gpc³** — about **36× larger than [[TNG300]]**. Each is run with the full
[[IllustrisTNG]] galaxy formation model at TNG300-comparable resolution, using
[[AREPO]] moving-mesh [[Magnetohydrodynamics]].

Publicly released **March 2025**.

## Specifications

| Quantity | Value |
|---|---|
| Clusters | 352 |
| Halo mass range | $\sim10^{14}$ – $>10^{15}\ M_\odot$ |
| Above $10^{15}\ M_\odot$ | ~90 (TNG300 gives a couple) |
| Parent volume | 1 Gpc³ |
| Baryonic cell mass | $\sim10^{6}\ M_\odot$ |
| DM particle mass | $\sim6\times10^{6}\ M_\odot$ |
| Softening | 1.5 kpc gas / 2.5 kpc collisionless |

## The design choice that matters

**The physics model is unchanged.** Same AGN feedback, same MHD, same parameters as
TNG50/100/300 — *no recalibration for the cluster regime*.

This is deliberate and it cuts both ways:

- **Good:** it is a clean *mass extension* of the existing suite. A difference between
  TNG-Cluster and TNG300 cannot be blamed on retuned physics, so cross-volume
  comparisons actually mean something.
- **Honest:** any failure of the TNG [[AGN Feedback]] prescription at cluster scales
  shows up undisguised. That is arguably the point — it is a prediction, not a fit.

Contrast with suites that recalibrate per mass regime, where agreement with cluster
observables is partly built in.

## What it is good for

[[Intracluster Medium]] physics: cool cores, sloshing, shocks, turbulence and gas
motions from core to outskirts, and the observables that follow —
[[Sunyaev-Zeldovich Effect]] signals and X-ray scaling relations.

> [!note] Relevance to my work
> Further from [[21 cm Line]] territory than [[TNG50]]. Worth remembering if I ever
> want cluster-scale radio halos, or the CGM/ICM boundary. #question Is there any
> useful HI content in these halos, or is it all far too hot?

## Access

Same machinery as the rest of TNG — web API and the `illustris_python` loaders.
See [[TNG Data Access]].

## Sources

- Nelson et al. 2024, *A&A* **686**, A157 — "Introducing the TNG-Cluster simulation"
  ([arXiv:2311.06338](https://arxiv.org/abs/2311.06338))
- Ayromlou et al. 2024, *A&A* — "An atlas of gas motions in the TNG-Cluster simulation"
- [tng-project.org/cluster](https://www.tng-project.org/cluster/) ·
  [data access](https://www.tng-project.org/data/cluster/)

## Connections

- [[IllustrisTNG]] · [[TNG50]] · [[TNG300]]
- [[Zoom-in Simulations]] — the technique that makes 352 clusters affordable
- [[AGN Feedback]] · [[AREPO]] · [[Magnetohydrodynamics]]
- [[Galaxy Clusters]] · [[Intracluster Medium]] · [[Cool Core Clusters]]
