---
title: Cosmic rays
type: concept
tags: [astro/ISM, astro/feedback]
status: growing
created: 2026-07-29
updated: 2026-09-02
---
# Cosmic rays

Up: [[MOC - CGF 2026]] · Related: [[Galactic winds]], [[Simulation landscape]]

---

Not rays — individual charged particles. ~90% protons, ~9% helium nuclei, ~1% heavier nuclei and electrons, at relativistic speeds. Name is a historical leftover.

**Discovery.** Physicists c. 1900 saw electroscopes discharge even when shielded, and assumed ground radioactivity. Hess went up in a balloon in 1912 and found ionization *increased* with altitude. Nobel.

## The spectrum

Power law $dN/dE \propto E^{-2.7}$, spanning $\sim10^6$–$10^{20}$ eV. The highest-energy particle ever detected carried roughly the kinetic energy of a well-hit tennis ball, in a single proton.

- **Knee** at $\sim3\times10^{15}$ eV — steepens to $-3.1$. Galactic accelerators running out of steam.
- **Ankle** at $\sim5\times10^{18}$ eV — flattens. Galactic population dying out, extragalactic taking over.

Flux: ~1 particle m$^{-2}$ s$^{-1}$ at GeV; ~1 km$^{-2}$ century$^{-1}$ at the top.

> **Plotting note.** Always plot $E^{2.7}\times$ flux, never raw flux. Over 34 decades a slope change from $-2.7$ to $-3.1$ is a rounding error visually — the line looks perfectly straight. Scaling divides out the dominant trend so the breaks become actual features. The $E^3$ convention tilts it so the knee reads as a peak. Same information, different emphasis.
>
> Real figures also show a low-energy turnover below ~10 GeV from solar wind modulation, a suppression above $\sim5\times10^{19}$ eV (GZK cutoff), and visible scatter between experiments in overlap regions.

## Origin and propagation

Galactic component: **diffusive shock acceleration** at SN remnant blast waves — a particle bounces across the shock front gaining energy each crossing, and the statistics give a power law ($\sim E^{-2}$ at source, steepened to $-2.7$ by energy-dependent escape). Above the ankle: AGN jets, GRBs, radio galaxies, still genuinely disputed.

**You can't trace them back.** Charged, so they spiral around field lines and arrival directions are almost completely randomized. A GeV proton has a gyroradius of order an AU, so it has forgotten where it started. Arrives isotropically.

Consequence: they random-walk rather than streaming out, staying confined for tens of Myr. Known from **secondary-to-primary ratios** — boron isn't made in stars in quantity, so observed boron came from carbon fragmenting on interstellar gas en route. B/C gives grammage $\sim10$ g cm$^{-2}$, far more than a straight-line path.

## Why they matter

Local energy density $\sim1$ eV cm$^{-3}$ — about the same as thermal gas, magnetic field, and starlight. **That rough equipartition is the whole reason they're dynamically interesting.**

They're also the only thing ionizing deep molecular cloud interiors where UV can't penetrate, and that residual ionization couples gas to the magnetic field and drives ion-neutral chemistry.

## Detection

- **Direct**: AMS-02; Voyager 1 sampling the unmodulated spectrum outside the heliosphere
- **Indirect**: air showers (Auger, IceCube)
- **Remote**: synchrotron from CR electrons; $\pi^0$-decay gamma rays from CR protons hitting gas (Fermi-LAT). **This last one calibrates simulation transport models.**

---

## Cosmic rays in simulations

Modeled as a second relativistic fluid, $\gamma_{\rm cr} = 4/3$, energy density $e_{\rm cr}$ advected with the gas, adding $P_{\rm cr} = (\gamma_{\rm cr}-1)e_{\rm cr}$ to the momentum equation. Most production runs are "grey" (one bin, dominated by ~GeV protons); spectrally resolved schemes exist (CREST, Girichidis) but are expensive. Injection typically 5–10% of each SN's energy, plus structure-formation shocks and AGN jets for clusters.

### Transport is where the physics lives

Pure advection freezes CRs into the gas and does almost nothing. The interesting behaviour needs relative motion:

- **Anisotropic diffusion** along field lines, $\kappa_\parallel \sim 10^{28}$–$10^{29}$ cm$^2$ s$^{-1}$, $\kappa_\perp \approx 0$
- **Streaming** down the CR pressure gradient at roughly $v_A$, with excited Alfvén waves damping and heating the thermal gas

The diffusion operator is stiff, so modern codes use two-moment formulations (Jiang & Oh 2018; Thomas & Pfrommer 2019).

### Why this matters dynamically

Thermal SN energy in dense gas radiates away almost instantly — the overcooling problem that forces subgrid wind models. **CR energy doesn't have that escape route**: hadronic and Coulomb losses are slow at low density, so the energy survives and pushes on gas via a smooth, extended pressure gradient.

Reported consequences:
- Winds cooler, denser, slower, more mass-loaded than thermally driven ones, launched from a large volume rather than in hot bubbles → [[Galactic winds]]
- Substantial non-thermal pressure support in the CGM, letting the halo sit at lower density and temperature at fixed total pressure. **The main selling point**, since it helps with the large cool CGM masses COS-Halos sees.
- Modest SFR suppression, strongest around $L^*$. Dwarfs less affected — low column densities let CRs stream out before doing work.
- Thicker gas disks from vertical CR pressure support
- In clusters, CR heating offsetting cooling flows

### The big caveat

Everything scales with $\kappa$, effectively a free parameter. FIRE-2 calibrates against $\gamma$-ray luminosities of nearby galaxies and MW grammage, landing near $3\times10^{29}$ cm$^2$ s$^{-1}$. Too low and CRs are trapped and over-pressurize the disk; too high and they leak out without coupling. Self-confinement vs extrinsic-turbulence theories give genuinely different scalings, so **"CRs matter a lot" and "CRs are a 20% effect" are both defensible**.

> **TNG has no CR module at all.** Any disk-structure comparison against a CR-MHD run compares different feedback philosophies, not just different resolutions.

Starting point for the AREPO side: Pfrommer–Pakmor–Simpson–Springel.
