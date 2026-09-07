---
title: Simulation landscape
type: concept
tags: [sim/codes]
status: growing
created: 2026-07-29
updated: 2026-09-02
---
# Simulation landscape

Up: [[MOC - CGF 2026]] · Related: [[Calibration and tuning]], [[Predictive power]], [[Resolution comparison]], [[TNG-Cluster vs IllustrisTNG]]

---

## Codes vs projects

> RAMSES is a **code**; TNG and FIRE are **projects**. The code solves the fluid equations; the project sets volume, resolution, and subgrid physics. Two projects on one code can disagree wildly; two projects on different codes can agree well.

| Code | Method | Who | Used by |
|---|---|---|---|
| GADGET-2/3/4 | SPH + TreePM | Springel | Millennium, EAGLE, Magneticum |
| AREPO | moving Voronoi mesh, FV MHD | Springel/Pakmor | Illustris, TNG, Auriga, THESAN, MTNG, Lumina |
| GIZMO | meshless finite mass/volume | Hopkins | FIRE, SIMBA |
| RAMSES | AMR | Teyssier | Horizon-AGN, NewHorizon, Obelisk, SPHINX |
| SWIFT | task-based, SPHENIX SPH | Schaller/Durham | FLAMINGO, COLIBRE |
| MP-Gadget | rewritten GADGET SPH | Feng/Di Matteo | BlueTides, ASTRID |
| ENZO | AMR | community | Renaissance, AGORA |
| GASOLINE2 / ChaNGa | SPH | Wadsley/Quinn | NIHAO, Romulus |
| Cholla | GPU-native grid | Schneider | CGOLS → [[Schneider — CGOLS outflows]] |

> The SPH vs mesh vs meshless debate was fierce c. 2010–2015 and has largely cooled. Modern SPH fixed the worst surface-tension and mixing pathologies, and the field mostly accepts that **subgrid feedback choices now dominate over hydro solver choices** for galaxy-scale predictions.

## Large-volume flagships

50–500 Mpc, resolution $\sim10^6$–$10^7M_\odot$.

**Illustris → IllustrisTNG → MillenniumTNG → TNG-Cluster.** Illustris (2014) was proof of concept but produced no red galaxies and blew gas out of groups. TNG fixed it with kinetic AGN feedback at low accretion rates plus MHD. TNG50/100/300 trade volume against resolution. MTNG pushed to 500 Mpc for cosmology and clustering. → [[TNG-Cluster vs IllustrisTNG]]

**EAGLE → BAHAMAS → FLAMINGO → COLIBRE.** Virgo/Durham/Leiden. EAGLE (2015) established the calibration philosophy: tune to the $z=0$ SMF and sizes, treat everything else as prediction. FLAMINGO went to 2.8 Gpc for weak lensing and cluster cosmology.

**COLIBRE** is the newest of that line — new code (SWIFT), 4× more DM than baryon particles to suppress spurious energy transfer, up to 20× more particles total, new structure finder. Headline physics: **explicit multiphase ISM with no pressure floor**, non-equilibrium H and He, dust model with three grain species and two grain sizes. Two AGN variants: purely thermal, or thermal + spin-dependent kinetic jets → [[Huško — hybrid AGN in COLIBRE]].

> The cold-ISM-plus-dust combination is the main thing distinguishing COLIBRE from TNG, which uses an effective equation of state instead.

**SIMBA** (GIZMO, Davé). Torque-limited BH accretion rather than Bondi; bipolar AGN jets at prescribed velocities. Usually the outlier in CGM comparison papers, often in interesting ways.

**ASTRID** (MP-Gadget, Di Matteo/Ni/Bird). 250 Mpc/h with $2\times5500^3$; notable for targeting massive BHs, reionization, and massive neutrinos in one box. Good statistics on rare quasars.

**Horizon-AGN** (RAMSES) — early morphology and spin studies. **Magneticum** (GADGET-3) — cluster and SZ work.

## Zoom-ins

**FIRE / FIRE-2 / FIRE-3** (GIZMO, Hopkins). Opposite philosophy from the boxes: very high resolution on individual halos, resolved multiphase ISM, stellar feedback taken directly from stellar evolution with essentially no tuning. Original FIRE had no AGN; FIRE-3 added it. Where most CR-MHD work lives → [[Cosmic rays]].

**Auriga** (AREPO, TNG-like physics). ~30 MW analogues at high resolution with magnetic fields. Natural comparison for MW disk structure and stellar halos.

**NIHAO, Romulus, VINTERGATAN, HESTIA, APOSTLE, NewHorizon, Obelisk** fill out the rest, differing in mass range, code, and whether constrained to the Local Group.

**GRIFFIN** — solar-mass resolution dwarfs, non-equilibrium cooling and chemistry, individual massive stars, HII regions. → [[Partmann — IMBHs in dwarf galaxies]], Lahén.

## Radiation hydrodynamics / reionization

Couple radiative transfer to the hydro rather than assuming a uniform UV background.

**THESAN** (AREPO-RT + TNG physics, 95 Mpc). Established the template: reionization topology, IGM, and galaxy populations self-consistently in one box. THESAN-ZOOM added zooms.

**Lumina** — the scaled-up successor. 500 cMpc with $2\times6000^3$ elements, gas and DM masses $3.6\times10^6$ and $1.9\times10^7M_\odot$, running to $z=3$ to follow galaxies, BHs and the IGM through both H and He reionization. AREPO with the IllustrisTNG galaxy formation model plus a GPU-accelerated M1 solver in six frequency bins. Volume chosen deliberately: enough dynamic range for the faint galaxies driving H reionization, enough volume for the rare bright quasars driving He II reionization. Includes coherent baryon–CDM streaming velocities in the ICs.

> **Since Lumina uses the TNG model, differences vs TNG are radiation transport, resolution, and volume — not feedback model.** Important for interpreting a size comparison. See [[Resolution comparison]].

**SPHINX** (RAMSES-RT), **CoDa**, **CROC**, **Renaissance** — other main reionization efforts, generally smaller volumes at higher resolution.

## N-body only

Millennium, Bolshoi/MultiDark, Uchuu, AbacusSummit, Euclid Flagship. Built for halo statistics, emulators, mock catalogues. AbacusSummit is the current DESI reference set.

## Parameter-space suites

**CAMELS** — thousands of small boxes across varied cosmological *and* astrophysical parameters, using several different subgrid models. Built for machine learning and for marginalising over baryonic uncertainty rather than for any single realistic universe. → [[Predictive power]]

## Note

Nothing here has SIDM. For gravothermal collapse work the relevant simulation landscape is entirely separate and much smaller.
