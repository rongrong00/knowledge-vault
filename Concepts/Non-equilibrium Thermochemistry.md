---
title: Non-equilibrium Thermochemistry
aliases: [equilibrium vs non-equilibrium cooling, non-equilibrium ionization, ionization equilibrium]
type: concept
tags: [astro/IGM, astro/reionization, sim/methods, sim/lumina, physics/atomic]
status: growing
created: 2026-09-02
updated: 2026-09-02
---

# Non-equilibrium Thermochemistry

> Whether the ionization state of gas is *assumed* to instantly reflect its density,
> temperature and a universal radiation field (equilibrium), or *evolved* as a dynamical
> variable driven by the local, time-dependent radiation field (non-equilibrium). The
> difference is largest in low-density gas during and after reionization.

## The quantity being solved for

Gas cooling depends on the **ionization state** — the fractions of H I / H II,
He I / He II / He III, and the free-electron density. Every cooling and heating channel
(recombination, collisional excitation, bremsstrahlung, photoheating, Compton) is a rate
that depends on these abundances. The abundances have to be known before the cooling
rate can be computed.

## The mechanism

**Equilibrium.** Assume ionization and recombination balance instantaneously for each
species:

$$
n_{\rm HI}\,\big(\Gamma_{\rm photo} + n_e\,\Gamma_{\rm coll}\big) \;=\; n_{\rm HII}\,n_e\,\alpha_{\rm rec}(T)
$$

Given $n$, $T$ and a photoionization rate $\Gamma_{\rm photo}$ from a **spatially uniform,
redshift-dependent UV background**, this is algebraic. Solve once, tabulate the net
cooling function $\Lambda(n,T,z)$, look it up during the run. Cheap. This is what
[[TNG-Cluster vs IllustrisTNG|IllustrisTNG]] and TNG100 do (Faucher-Giguère+09 background),
with a **self-shielding correction** (Rahmati+13) that reduces $\Gamma$ in dense gas by a
fitted function of density.

Two hidden assumptions: the radiation field is the same everywhere, and the gas has had
time to reach balance.

**Non-equilibrium.** Integrate the rate equations in time instead of setting them to zero:

$$
\frac{dn_{\rm HI}}{dt} = n_{\rm HII}\,n_e\,\alpha_{\rm rec}(T) - n_{\rm HI}\,\big(\Gamma_{\rm photo} + n_e\,\Gamma_{\rm coll}\big)
$$

and likewise for He I, He II, He III, with $\Gamma_{\rm photo}$ computed from the **local**
radiation field the RT solver carries in that cell. The abundances become extra state
variables advected with the gas. This is what Lumina does, coupled to AREPO-RT and
subcycled 64× (during hydrogen reionization) or 256× ($z<4.75$) per hydrodynamic step,
because these timescales are short.

## Key relations

Equilibrium is valid when the **chemical timescale is short compared to the timescale on
which conditions change**. The chemical timescale is the slower of ionization and
recombination:

$$
t_{\rm rec} \simeq \frac{1}{n_e\,\alpha_{\rm rec}} \approx 10^5\,{\rm yr}\left(\frac{n_e}{1\,{\rm cm^{-3}}}\right)^{-1}\left(\frac{T}{10^4\,{\rm K}}\right)^{0.7}
$$

| Regime | $n_e$ | $t_{\rm rec}$ | Equilibrium? |
|---|---|---|---|
| Dense ISM | $\gtrsim1\,{\rm cm^{-3}}$ | $\lesssim10^5$ yr | yes |
| CGM | $10^{-3}$–$10^{-2}$ | $10^7$–$10^8$ yr | marginal |
| IGM at $z\sim6$ | $10^{-4}$–$10^{-3}$ | $10^8$–$10^9$ yr | **no** — comparable to the Hubble time |

## Why it matters

1. **Reionization is impulsive.** An ionization front sweeps through gas in far less
   than a recombination time; the gas is ionized and heated to $\sim2\times10^4$ K
   essentially instantly, then cools and recombines slowly, *out of* equilibrium for a
   long time. An equilibrium model with a uniform UVB cannot represent a patchy front —
   it turns the whole box's background on with a redshift-dependent amplitude.
2. **Shock-heated or rapidly cooling gas lags.** Recombination cannot keep up, so gas
   stays over-ionized while cooling, which suppresses collisional-excitation cooling near
   $10^4$ K relative to the equilibrium value — factors of a few, in exactly the
   temperature range where gas accretes onto galaxies.
3. **Self-shielding is emergent.** The RT solver attenuates the local field through the
   actual column of neutral gas, so dense clumps shield themselves consistently instead
   of via a correction calibrated on other simulations.
4. **The post-reionization IGM temperature depends on the spectrum** that ionized it
   (harder spectrum → more energy per ionization → hotter gas). A uniform-UVB
   equilibrium model fixes this by assumption; frequency-resolved RT predicts it — which
   is what Lumina's six frequency bins are for.

## Primordial vs metal-line cooling

**Primordial** = H and He only. Channels: collisional excitation of H I Lyα (10.2 eV) and
He II (40.8 eV) — the two peaks near $2\times10^4$ K and $10^5$ K; collisional ionization;
recombination; bremsstrahlung ($\propto T^{1/2}$, dominant above $\sim10^6$ K); inverse
Compton off the CMB ($\propto(1+z)^4$). Peak $\Lambda/n_H^2\sim10^{-22}$ erg cm$^3$ s$^{-1}$.
**Hard floor at $\sim10^4$ K** — nothing to excite below it without H$_2$ or metals — and a
dip near $10^{5.5}$–$10^6$ K between the He II peak and the bremsstrahlung rise.

**Metal-line** = excited lines of C, N, O, Ne, Mg, Si, S, Fe. Many low-lying transitions,
so at $10^5$–$10^7$ K solar-metallicity gas cools **10–100×** faster than primordial (O VI,
C IV, Ne VIII, Fe L-shell fill the dip), and below $10^4$ K fine-structure lines ([C II]
158 μm, [O I] 63 μm) remove the floor. Roughly
$\Lambda\approx\Lambda_{\rm prim}+(Z/Z_\odot)\Lambda_{\rm metal,\odot}$.

**In the simulations.** TNG100: both from CLOUDY tables $\Lambda(n,T,Z,z)$ in ionization
equilibrium under the FG09 background (Wiersma+09 method, solar ratios scaled by total
$Z$, Rahmati+13 self-shielding). The UVB *suppresses* cooling by ionizing away the
coolants — a large effect at low density. Lumina: the **primordial part only** is
replaced by the non-equilibrium network; metal cooling stays tabulated because only
total $Z$ is tracked. *Why that split:* H+He is six ionization states and is what
reionization acts on — affordable and physically sensitive to the local field; metals
are hundreds of coupled ions and are tabulated everywhere.

**Why it matters for galaxies.** $t_{\rm cool}=3kT/(2n\Lambda)$ against $t_{\rm dyn}$ is
the Rees & Ostriker / Silk (1977) argument for galaxy mass scales; which cooling curve you
use shifts that boundary by an order of magnitude at $10^5$–$10^6$ K.

## Caveats and failure modes

- **Cost.** More state variables per cell; a stiff ODE system (ionization and
  recombination rates differ by orders of magnitude); coupling to an RT solver — hence
  the subcycling and the reduced speed of light $\tilde c=0.2c$. It is also why Lumina
  tracks only total metallicity: the memory went to the chemistry and radiation fields.
- **Scope.** Lumina replaces equilibrium **primordial** (H, He) cooling with the
  non-equilibrium network. Metal-line cooling is still handled the standard way, since
  only total $Z$ is tracked.
- **Where it doesn't matter.** In the dense ISM the two agree; differences in galaxy
  *sizes* from this choice alone are expected to be second order relative to the
  galaxy-formation model, which is shared.

## Connections

- [[Research Exam]] — why Lumina and TNG100 differ in cooling
- [[Resolution comparison]] · [[Simulation landscape]]
- [[Epoch of Reionization]] · [[Escape fraction]]
- [[Spin Temperature]] · [[Kinetic Temperature]] — the same equilibrium-vs-not logic for 21 cm

## Sources

- Katz, Weinberg & Hernquist 1996 — the equilibrium primordial cooling standard
- Faucher-Giguère+09 — uniform UV background; Rahmati+13 — self-shielding fit
- Kannan+19 — AREPO-RT; Kannan+22 — Thesan; Zier+26 — Lumina
