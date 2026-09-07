---
title: TNG-Cluster vs IllustrisTNG
type: concept
tags: [sim/TNG]
status: growing
created: 2026-07-29
updated: 2026-09-02
---
# TNG-Cluster vs IllustrisTNG

Up: [[MOC - CGF 2026]] · Reference card: [[TNG-Cluster]] · Related: [[Simulation landscape]], [[Resolution comparison]], [[Calibration and tuning]]

---

**Same physics, same resolution — different geometry and selection.** TNG-Cluster is not a new model, it's a sampling strategy.

| | IllustrisTNG | TNG-Cluster |
|---|---|---|
| Geometry | uniform periodic boxes | 352 zoom regions |
| Parent volume | the box itself | 1 Gpc (36× TNG300) |
| Sample | volume-limited, unbiased | flat in halo mass |
| Resolution | TNG50/100/300 | TNG300-1 level |
| Physics | IllustrisTNG model | **identical** |

TNG300 at ~300 Mpc contains only a handful of genuinely massive clusters — nowhere near enough for cluster science. TNG-Cluster buys statistics at the high-mass end without changing the physics.

## The selection

Targets picked on $z=0$ halo mass **alone**, making the sample unbiased in all other properties. The 352 halos are chosen randomly in 0.1 dex mass bins so as to:
- include **every** halo in the parent volume above $10^{15}M_\odot$ (all 92)
- compensate for the drop-off in TNG300 statistics from $10^{14.3}$ upward

producing a **flat distribution in halo mass**.

> **Flat in halo mass means deliberately NOT volume-representative.** Any volume-averaged quantity — a mass function, cluster counts, an SZ or X-ray number density — needs reweighting by the halo mass function. Main thing to get right when using it.

## Practical gotchas

The 352 zooms were stitched back into a virtual box (**L680n8192TNG**) at full fiducial resolution, but the data layout differs from a normal TNG box:

- Each zoom halo's particles live in **dedicated chunk files**, and loading all of them mixes low-resolution background particles from every zoom. Select the right file IDs per halo.
- `GroupPrimaryZoomTarget` flags primary targets at each snapshot, but **those are not the main progenitors of the $z=0$ clusters** — you can't treat a snapshot slice as a merger tree.

## Bonus content, with a caveat

Beyond the 352 targets: **241 additional group-mass** and **9110 additional Milky Way-mass** halos at uncontaminated resolution.

> Tempting as extra statistics, but they all sit in **cluster environments** — environmentally biased relative to a field sample from TNG300.

## Why it exists

Cluster science: ICM thermodynamics, cool-core vs non-cool-core, sloshing and merger shocks, radio relics, X-ray cavities, magnetic amplification, BCG and SMBH assembly, jellyfish galaxies, and mock observables for XRISM and future X-ray missions. All need a hundreds-strong sample of massive clusters no affordable uniform hydro box provides.

## One consequence worth keeping in mind

Because the physics is fixed, TNG-Cluster tests whether the TNG model **extrapolates to a mass regime it wasn't calibrated in** — a genuine out-of-sample test, and a point in the project's favour. → [[Predictive power]]

> But it also means the known TNG issues at the massive end — the kinetic-mode AGN feedback in particular — are inherited wholesale. **More clusters of the same model, not a better model of clusters.**
