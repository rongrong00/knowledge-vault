---
title: Reina-Campos — SCALES
type: literature
authors: Reina-Campos
year: 2026
venue: CGF 2026, Garching
tags: [talk, conference/CGF2026, astro/dynamics, astro/stellar]
status: growing
read: 2026-07-29
---
# Reina-Campos — SCALES: assembly of the massive clusters powering superbubbles

Up: [[MOC - CGF 2026]] · Related: [[Galactic winds]], [[Star clusters and NSCs]], [[Escape fraction]], [[Calibration and tuning]]

---

## What SCALES is

**Star Clusters As Links between galaxy Evolution and Star formation.** Marta Reina-Campos (CITA/McMaster) with Gnedin, Sills, Hui Li. Paper I: numerical method, arXiv:2408.04694, ApJ.

Core idea: **individual star clusters are the units of star formation**, modelled as sink particles that begin as gas-rich dense clumps and grow through gas accretion and hierarchical merging with gravitationally bound neighbours.

Aim: bridge the scales between high-resolution single-star simulations of isolated clouds and dwarfs, and cosmological zoom-ins.

## Why this is the interesting move

Her earlier projects — **E-MOSAICS** and **EMP-Pathfinder** — attached subgrid cluster populations to star particles. Those follow cluster populations over the age of the Universe for many systems, but **the clusters cannot modify their host galaxies**. They were passive tracers.

> SCALES makes them **dynamical agents**, so clustered feedback can act back on the gas.

## Why it matters beyond star clusters

This is the missing ingredient in the wind story. Superbubble-driven outflows depend on supernovae being **correlated in space and time** — many SNe going off inside an already-evacuated hot cavity, so later ones do work on a low-density interior instead of radiating away in dense gas.

Whether that happens depends on the **cluster mass function**, which no cosmological simulation resolves. TNG's decoupled winds and EAGLE's stochastic $\Delta T$ are both workarounds for not having this. → [[Galactic winds]]

It also feeds directly into [[Escape fraction]] — LyC escape requires low-column channels carved by clustered feedback.

> SCALES is trying to **build** this from the cluster side rather than parameterize around it.

The talk title says "assembly of the massive clusters," suggesting content on the accretion-versus-merging channel — how the rare massive clusters that dominate the energy budget actually get built.

## Questions

**Best — the translation question**
> What mass loading do the superbubbles produce, and how does it compare to what the subgrid wind models assume?

The question the rest of the audience wants answered and can't ask as directly, since most work on the parameterized side. If clustered feedback gives $\eta$ in the right range without tuning, that validates the whole enterprise; if not, more interesting still. The natural bridge from her talk to everyone else's.

**Physics of breakout**
> Is the burstiness of the outflow set by the cluster mass function, or by how the clusters are spatially correlated?

Superbubble breakout needs several clusters going off in the same region, not just one massive one. "Assembly" in the title suggests she's thinking about it.

**What's emergent vs prescribed**
> What sets the end of sink accretion?

The cluster mass function is the model's central output, determined by whatever terminates growth. Low risk.

> Does the CMF come out with a Schechter truncation, and does the truncation mass scale with pressure as observations suggest?

Her earlier work used environmentally dependent prescriptions for exactly this; now it should emerge. The calibration-vs-prediction question for her project.

**Technical**
> Do you sample the IMF stochastically at low cluster masses?

Below ~$10^4M_\odot$ the number of massive stars isn't proportional to cluster mass, and energy is dominated by the tail — changes the feedback budget.

> What fraction of star formation ends up in bound clusters, and does it matter whether the rest is dispersed?

Observed cluster formation efficiency is well below unity and environment-dependent, and SNe from a dispersed population do far less work.

**Friendly**
> What changes relative to EMP-Pathfinder now that the clusters can back-react?

The natural before-and-after; she'll enjoy answering it.

**Coffee break only**
> How much does the outflow depend on the sink accretion radius and the softening?

Legitimate but it's a convergence challenge to the model's core numerics.

## Framing note

Her field is star clusters; most of the room is galaxy formation. A question that translates her result into galaxy-formation currency — mass loading, energy coupling, whether the subgrid models are wrong — is **more useful to her** than a question about cluster demographics, which her own community will already be asking.

---

## What actually happened

*(notes from the talk)*
