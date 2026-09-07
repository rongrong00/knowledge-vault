---
title: Johansson — KETJU
type: literature
authors: Johansson
year: 2026
venue: CGF 2026, Garching
tags: [talk, conference/CGF2026, astro/dynamics, sim/codes]
status: growing
read: 2026-07-29
---
# Johansson — KETJU: BH dynamics and GW in compact high-$z$ galaxies

Up: [[MOC - CGF 2026]] · Related: [[Post-Newtonian expansion]], [[Dynamical friction]], [[Star clusters and NSCs]], [[Huško — hybrid AGN in COLIBRE]]

---

## What KETJU is

"Ketju" = Finnish for **chain** (chain regularization). Helsinki: Rantala, Mannerkoski, Johansson.

### The problem it solves

Gravitational softening keeps a collisionless N-body code stable, but **destroys exactly the physics that hardens a BH binary**. Once two BHs are within a softening length, the code can't resolve their mutual orbit or the individual stellar scatterings that extract angular momentum.

So cosmological simulations merge BHs **by fiat** when they come within ~10–100 pc. A bookkeeping rule, not dynamics. That's the numerical face of the final-parsec problem. → [[Dynamical friction]]

### The solution

A small **regularized region** around each black hole, radius **3× the BH softening length**, so all BH–BH and BH–star interactions are **unsoftened**, integrated with the algorithmically regularized **MSTAR** integrator instead of the leapfrog used elsewhere.

Star–star interactions inside the region stay softened, to avoid energy errors as particles cross the boundary.

**Regularization** = a coordinate and time transformation removing the $1/r$ singularity of the two-body problem, so close passages and extreme eccentricities integrate accurately without the timestep collapsing. The standard trick from collisional stellar dynamics, transplanted into a cosmological tree code.

### Not full GR

**Post-Newtonian, through 3.5PN** → [[Post-Newtonian expansion]] — covering the 2.5PN radiation-reaction term. A binary can be followed to roughly **ten Schwarzschild radii**, several orders of magnitude beyond the merger separations used in softened GADGET-based codes. Multiple-BH systems supported, including leading non-linear PN cross terms.

> **Formal inconsistency worth knowing:** the regularized region uses PN dynamics while the surrounding galaxy is Newtonian, and the boundary isn't covariant. Fine in practice — PN corrections are negligible at the boundary by construction — but it's an approximation stitched to another approximation.

## What it's used for

**Core formation.** Binary scouring — the binary ejects stars by three-body slingshot and carves a constant-density core in massive ellipticals. KETJU can produce this rather than assume it.

**GW predictions.** Merger rates, timescales and waveforms for LISA and PTAs, from realistic galaxy-scale initial conditions.

**Binary demographics.** In a cosmological group-scale run of $\sim2\times10^{13}M_\odot$: eleven SMBHs formed binaries plus a hierarchical triplet, all eventually merging after hardening through dynamical friction → stellar scattering → GW emission. Binaries formed at **eccentricities 0.3–0.9, one reaching 0.998**, merging on timescales of tens to several hundred Myr.

> Those eccentricities are the interesting output. PTA signal predictions depend sensitively on them — the $(1-e^2)^{-7/2}$ scaling in the quadrupole formula — and they're precisely what a softened code cannot give you.

## Availability

First version in GADGET-3 (Rantala et al. 2017), used for isolated merger and core-formation work. **GADGET-4 implementation released publicly in 2023.**

## Cross-talk question

BH mergers are one of the three channels changing spin in [[Huško — hybrid AGN in COLIBRE]], alongside accretion and jet spin-down. Whether that channel matters depends on whether mergers actually complete and on what timescale — which every subgrid model answers **by assumption** and KETJU answers **by integration**.

> Are the merger timescales and mass ratios that come out consistent with what the subgrid models assume?

Also connects to [[Star clusters and NSCs]] — whether a BH arrives at a merger naked or embedded in an NSC largely determines whether it sinks or stalls.

---

## What actually happened

*(notes from the talk)*
