---
title: TNG-Cluster
aliases: [TNG Cluster, TNG-Cluster simulation]
type: concept
tags: [sim/TNG, astro/clusters, astro/ICM, dataset]
status: growing
created: 2026-09-07
updated: 2026-09-07
---

# TNG-Cluster

Up: [[MOC - Astrophysics]] · **For the comparison, see [[TNG-Cluster vs IllustrisTNG]]** —
that note covers geometry, selection and why the physics is deliberately unchanged.
This one is the reference card: numbers, provenance, access.

> 352 zoom-in galaxy clusters run with the unmodified [[IllustrisTNG]] model, drawn
> from a 1 Gpc³ parent volume. Publicly released **March 2025**.

## Specifications

| Quantity | Value |
|---|---|
| Clusters | 352 |
| Halo mass range | $\sim10^{14}$ – $>10^{15}\ M_\odot$ |
| Above $10^{15}\ M_\odot$ | **92** — every such halo in the parent volume |
| Parent volume | 1 Gpc³ (36× [[TNG300]]) |
| Baryonic cell mass | $\sim10^{6}\ M_\odot$ |
| DM particle mass | $\sim6\times10^{6}\ M_\odot$ |
| Softening | 1.5 kpc gas / 2.5 kpc collisionless |
| Code | [[AREPO]] moving mesh, ideal [[Magnetohydrodynamics]] |
| Released | March 2025 |

## What it is good for

[[Intracluster Medium]] physics: cool cores, sloshing, shocks, turbulence, and gas
motions from core to outskirts — plus the observables that follow, [[Sunyaev-Zeldovich Effect]]
signal and X-ray scaling relations.

## Access

Same machinery as the rest of TNG — web API and the `illustris_python` loaders.
[tng-project.org/data/cluster](https://www.tng-project.org/data/cluster/)

> [!question] Relevance to my own work
> Much further from [[21 cm Line]] territory than [[TNG50]]. Worth remembering if I
> ever want cluster-scale radio halos or the CGM/ICM boundary. Is there any useful
> HI content in these halos, or is it all far too hot? #question

## Sources

- Nelson et al. 2024, *A&A* **686**, A157 — "Introducing the TNG-Cluster simulation"
  ([arXiv:2311.06338](https://arxiv.org/abs/2311.06338))
- Ayromlou et al. 2024, *A&A* — "An atlas of gas motions in the TNG-Cluster simulation"
- [tng-project.org/cluster](https://www.tng-project.org/cluster/)

## Connections

- [[TNG-Cluster vs IllustrisTNG]] — the comparison, in depth
- [[Simulation landscape]] · [[Resolution comparison]] · [[Calibration and tuning]]
- [[IllustrisTNG]] · [[TNG50]] · [[TNG300]] · [[Zoom-in Simulations]]
