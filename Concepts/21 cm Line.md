---
title: 21 cm Line
aliases: [HI line, 1420 MHz line, hydrogen line, H I 21cm]
type: concept
tags: [astro/ISM, astro/cosmology, astro/radio, physics/atomic, physics/hyperfine]
status: growing
created: 2026-08-21
updated: 2026-08-21
---

# 21 cm Line

> The hyperfine transition in the ground state of neutral hydrogen — a *nuclear-spin
> readout*, not an electronic transition. The photon reports the relative orientation
> of the proton's and electron's magnetic moments.

## The mechanism

The proton and the electron are both magnetic dipoles. In the 1s state the electron
wavefunction is **nonzero at the origin**, so the dominant coupling is not the usual
dipole–dipole term but the [[Fermi Contact Interaction]]:

$$
H_{\text{hf}} \;=\; \frac{2\mu_0}{3}\, g_p \mu_N\, g_e \mu_B\, |\psi(0)|^2 \;
\mathbf{I}\!\cdot\!\mathbf{S}
$$

The total spin $\mathbf{F}=\mathbf{I}+\mathbf{S}$ takes $F=1$ (moments parallel,
triplet, $g=3$) or $F=0$ (antiparallel, singlet, $g=1$). The splitting is tiny —
about 5.9 µeV — and the $F=1\to0$ decay emits a 21 cm photon.

It is a **magnetic dipole** transition, forbidden in the electric-dipole sense.
That makes it fantastically slow. A given hydrogen atom essentially never does this.
There is simply so much hydrogen that it doesn't matter — see [[Forbidden Transitions]].

## Key numbers

| Quantity | Value | Note |
|---|---|---|
| $\nu_{10}$ | 1 420.405 751 768 MHz | Known to ~mHz; a frequency standard in its own right |
| $\lambda$ | 21.106 cm | Rest wavelength in vacuum |
| $\Delta E$ | 5.874 µeV | $\sim 10^{-6}$ of the Lyman-α energy |
| $T_\star = \Delta E/k_B$ | 0.0682 K | **The crucial number** — see below |
| $A_{10}$ | $2.85\times10^{-15}\ \mathrm{s^{-1}}$ | Einstein A coefficient |
| Mean lifetime | $\sim 1.1\times10^{7}$ yr | ~11 million years per atom |

## Why it is *the* mass tracer

$T_\star = 0.068$ K is absurdly small compared to any real gas temperature. So in
practice $T_\star / T_s \ll 1$ always, and the level populations sit at essentially
their statistical-weight ratio:

$$
\frac{n_1}{n_0} \;=\; 3\,e^{-T_\star/T_s} \;\approx\; 3
$$

Stimulated emission nearly cancels absorption, the temperature dependence largely
drops out, and in the optically thin limit the [[HI Column Density]] falls almost
straight out of the integrated line:

$$
N_{\rm HI}\ [\mathrm{cm^{-2}}] \;=\; 1.823\times10^{18} \int T_b \, dv \;\;
[\mathrm{K\ km\ s^{-1}}]
$$

Nearly model-free column densities. That is rare in astronomy, and it is why HI is
the workhorse for [[Galaxy Rotation Curves]] — extending them far beyond the optical
disk is a pillar of the [[Dark Matter]] case.

> [!warning] Where it breaks
> The clean linearity assumes optically thin gas. In cold, dense [[Cold Neutral Medium]]
> clouds $\tau \gtrsim 1$ and you *underestimate* $N_{\rm HI}$ unless you do
> emission/absorption pairs against background continuum sources. See [[HI Self-Absorption]].

## Excitation: the part the textbooks rush

The [[Spin Temperature]] $T_s$ that sets the populations is **not** set radiatively —
the transition is far too slow. Three processes compete:

1. **Collisions** — H–H, H–e⁻, H–p. Dominant in dense gas; pulls $T_s \to T_K$.
2. **CMB photons** — pull $T_s \to T_{\rm CMB}$.
3. **Lyman-α scattering** — the [[Wouthuysen-Field Effect]]: an atom absorbs a Lyα
   photon, goes to 2p, and decays back into the *other* hyperfine level. This couples
   $T_s$ to the [[Kinetic Temperature]] of the gas via the colour temperature of the
   Lyα field. Wouthuysen 1952, Field 1958.

The Wouthuysen–Field mechanism is why 21 cm is a probe of the **first stars**: you
need a Lyα background before the gas can decouple from the CMB and become visible.

## Cosmology: emission or absorption?

Against the CMB, the differential [[Brightness Temperature]] is

$$
\delta T_b \;\approx\; 27\, x_{\rm HI}\,(1+\delta)\,
\left(1 - \frac{T_{\rm CMB}}{T_s}\right)
\sqrt{\frac{1+z}{10}}\ \ \mathrm{mK}
$$

The sign is the whole story:

- $T_s < T_{\rm CMB}$ → **absorption** (Dark Ages, [[Cosmic Dawn]])
- $T_s > T_{\rm CMB}$ → **emission** (post-heating, [[Epoch of Reionization]])
- $T_s = T_{\rm CMB}$ → invisible

This is the basis of [[21 cm Cosmology]] and [[Intensity Mapping]] — potentially far
more modes than the CMB gives, because you get a *tomographic* map rather than a
single surface.

> [!question] EDGES
> EDGES (2018) reported a flat-bottomed absorption trough at 78 MHz ($z\approx17$)
> with amplitude ~0.5 K — roughly twice the deepest standard-cosmology prediction.
> Explanations ranged from excess radio backgrounds to baryon–[[Dark Matter]]
> scattering. **SARAS 3** (2022) rejected the EDGES profile at 95.3% confidence.
> Status: unresolved, and largely a fight about [[Foreground Removal]] and
> instrumental systematics. #question

## Instruments

[[CHIME]] · [[HERA]] · [[LOFAR]] · [[MWA]] · [[SKA]] · [[Arecibo]] (ALFALFA) ·
[[FAST]] · [[GBT]]

The band 1400–1427 MHz is **protected** by international radio regulation — one of
the few slices of spectrum astronomy actually owns.

## History

- **1944** — [[Hendrik van de Hulst]] predicts it, in occupied Utrecht, as a student exercise.
- **1951** — Detected by **Ewen & Purcell** at Harvard's Lyman Laboratory, with a
  plywood horn antenna out a window. Confirmed within weeks by Muller & Oort (Netherlands)
  and Christiansen & Hindman (Australia); all three published together in *Nature*.
- **1970s** — HI rotation curves (Roberts & Rots, Bosma) make the [[Dark Matter]]
  problem impossible to ignore.
- **2018–** — Cosmic-dawn era experiments; EDGES claim and its contested status.

The [[Pioneer Plaque]] and Voyager records use the 21 cm transition as their unit of
length and time — the assumption being that any technological civilisation knows this
number.

## Connections

- Contrast with [[Lyman-alpha Line]] — same atom, factor $10^6$ in energy, utterly different physics
- [[Hyperfine Structure]] generally; cf. the caesium standard
- [[Zeeman Splitting]] of the 21 cm line measures interstellar [[Magnetic Fields]]
- [[Damped Lyman-alpha Systems]] — the high-$z$ HI reservoirs 21 cm surveys chase
- [[Cold Neutral Medium]] / [[Warm Neutral Medium]] — the two-phase ISM the line resolves

## Open questions

- #question Is the EDGES trough real? What would settle it — a second independent
  global-signal experiment, or only interferometric detection of the fluctuations?
- #question How well can $T_s$ actually be pinned down at $z\sim10$ without assuming
  a heating history?
- #question What sets the CNM/WNM mass fraction, and can 21 cm absorption surveys
  measure it directly at $z>1$?

## Sources

- Ewen & Purcell 1951, *Nature* **168**, 356 — the detection
- Field 1958, Proc. IRE **46**, 240 — Wouthuysen–Field
- Furlanetto, Oh & Briggs 2006, *Phys. Rep.* **433**, 181 — the standard review
- Pritchard & Loeb 2012, *Rep. Prog. Phys.* **75**, 086901 — cosmology review
- Bowman et al. 2018, *Nature* **555**, 67 — EDGES
- Singh et al. 2022, *Nature Astronomy* **6**, 607 — SARAS 3 non-confirmation

---

> [!info] This is the worked example
> Most links above are **unresolved** on purpose — they're dimmed, and clicking one
> creates the note. That's the intended way to grow this vault. See [[README]].
