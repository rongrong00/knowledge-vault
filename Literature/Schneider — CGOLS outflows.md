---
title: Schneider — CGOLS outflows
type: literature
authors: Schneider
year: 2026
venue: CGF 2026, Garching
tags: [talk, conference/CGF2026, astro/feedback, sim/codes]
status: growing
read: 2026-07-29
---
# Schneider — CGOLS SFR: how outflow properties depend on star formation rate

Up: [[MOC - CGF 2026]] · Related: [[Galactic winds]], [[Reina-Campos — SCALES]], [[Simulation landscape]]

---

> ⭐ **Highest career relevance.** CGOLS = Cholla Galactic OutfLow Simulation suite, and **Cholla is a fully GPU-native hydrodynamics code** running on Frontier-class machines.

## Two reasons to attend

**1. The physics.** Outflow and mass-loading behaviour at resolution that actually resolves the multiphase structure — the thing cosmological subgrid wind models can only approximate. → [[Galactic winds]]

Specifically relevant: does $\eta$ scale with SFR the way subgrid prescriptions assume?

**2. The engineering.** A working example of exactly the thing I want to do to Gadget-4's gravity solver. **GPU-native versus GPU-ported is a real design question** and she'll have strong opinions.

## Questions

**Physics**
> How does mass loading scale with SFR, and does it match what the subgrid models assume?

Connects to the [[Reina-Campos — SCALES]] question about whether clustered feedback produces $\eta$ in the right range naturally.

> How much of the cool phase is entrained versus formed in situ by cooling in mixing layers?

The cloud-crushing question, at resolution where it can be answered.

**Over coffee — the one to actually pursue**
> What was the experience of building GPU-native from the start, versus porting an existing CPU code? Where does the design differ?

Relevant to the Gadget-4 gravity solver port. Follow-ups worth having ready:
- How much of the win is memory layout vs kernel design?
- Data movement management — what's the strategy for keeping data resident?
- MPI+GPU overlap on Frontier-class machines?
- Profiling workflow (Nsight Systems or ROCm equivalent)?

---

## What actually happened

*(notes from the talk)*
