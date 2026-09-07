---
title: Equilibrium spin
type: concept
tags: [astro/BH, astro/accretion]
status: growing
created: 2026-07-29
updated: 2026-09-02
---
# Equilibrium spin vs Eddington ratio

Up: [[MOC - CGF 2026]] · Related: [[Accretion disc states]], [[Super-Eddington accretion]], [[Trinca — multi-regime accretion disc]], [[Huško — hybrid AGN in COLIBRE]]

---

**Ricarte, Narayan & Curd (2023)**, ApJL, arXiv:2307.04621. 38 3D GRRMHD simulations with KORAL, magnetically arrested discs, spins $-0.9$ to $+0.97$, $0.4 \lesssim f_{\rm Edd} \lesssim 40$. Both authors at CfA / Black Hole Initiative.

## The result

| $f_{\rm Edd}$ | Regime | $a_{*,\rm eq}$ |
|---|---|---|
| $< 0.03$ | hot / MAD ADAF | $\approx 0$ (limiting 0.035) |
| 0.03–0.3 | thin disc | $\approx 1$ |
| $\approx 1$ | near-Eddington MAD | $\approx 0.8$ |
| $\gg 1$ | super-Eddington MAD | $\approx 0$ |

> **Non-monotonic — not a contradiction.** 0.8 is the value *at* Eddington (the first noticeable departure from the classical thin-disc answer of ~1); $\approx 0$ is the asymptote well above Eddington.

## Why the shape

Two competing torques: disc gas spins the hole **up**, the Blandford–Znajek jet extracts spin energy and spins it **down**.

Jet strength depends on the magnetic flux the hole can hold. Their key new result: **saturated flux depends on Eddington ratio as well as spin**, driven by $H/R$ rising with $f_{\rm Edd}$. So radiative discs below $f\approx0.3$ behave like standard thin discs, while those well above Eddington closely resemble non-radiative hot flows.

- Thin disc can't confine much flux → no jet to fight spin-up → $a \to 1$
- Both thick regimes (hot and super-Eddington) hold saturated MAD flux → powerful jets → spin ground down

Same double-sided structure as radiative efficiency in [[Accretion disc states]], same underlying reason: geometrically thick at both ends.

## Timescale caveat

Reaching equilibrium requires accreting a significant fraction of your own mass, on a timescale $t_{\rm Sal}/f_{\rm Edd}$. In the hot regime that exceeds a Hubble time, so those BHs never actually reach $a \approx 0$ — noticeable evolution occurs but not equilibrium.

> Only holes accreting near or above Eddington equilibrate in less than a Hubble time. **The low-spin prediction is reachable only on the super-Eddington side** — exactly the regime a high-$z$ BH growth talk cares about.

## Science consequence

Their Fig. 5: two tracks both accreting $10^9\,M_\odot$, one at $f_{\rm Edd}=20$ and one at $f_{\rm Edd}=1$, differ by a **factor of 7** in total feedback energy. The super-Eddington case reaches a lower equilibrium spin and therefore drives less efficient jets.

So a BH could grow more efficiently in a super-Eddington state before jet feedback cuts off its fuel supply.

> Self-consistency question with teeth for any model invoking super-Eddington growth: if your model spins holes *up* during those episodes, strong jets choke the inflow. If it spins them *down*, growth is easier — but then you must explain observed high spins.

## Caveats to hold in reserve

- Assumes the **MAD state**, observationally supported only for low-Eddington sources like M87* and Sgr A*
- The suite covers only ~1.6 decades above Eddington while the framing is about $f_{\rm Edd}\to\infty$; the example tracks integrate a seed starting at $f_{\rm Edd} = 15{,}000$
- **No direct probe of spin exists in the super-Eddington regime** — the ISCO feature reflection spectroscopy needs washes out in thick discs. Currently unfalsifiable where it matters most. That's a legitimate defence for a speaker.
