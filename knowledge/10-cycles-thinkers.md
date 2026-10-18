# 10 — Cycles Thinkers: Overview and Synthesis Map

This section collects the **non-Vedic** thinkers behind the project: people who argued that human affairs, bodies and markets follow rhythms, and that some of those rhythms are tied to the sky. The Vedic side is in [02-vedic-jyotish.md](02-vedic-jyotish.md) and [03-reading-parasharas-light.md](03-reading-parasharas-light.md). Astrological mechanics are in [01-how-astrology-works.md](01-how-astrology-works.md). Ephemeris and software (Swiss Ephemeris) are in [04-software.md](04-software.md).

| File | Subject |
|---|---|
| [11-edward-dewey-cycles.md](11-edward-dewey-cycles.md) | Edward R. Dewey and the Foundation for the Study of Cycles: method, famous cycles, how to run a Dewey-style analysis |
| [12-chizhevsky.md](12-chizhevsky.md) | Alexander Chizhevsky: the sunspot cycle and "mass excitability", heliobiology, air ions |
| [13-paracelsus.md](13-paracelsus.md) | Paracelsus: microcosm and macrocosm, the "star in man", medical astrology |
| [14-osho.md](14-osho.md) | Osho's talks on astrology: three layers, cosmic oneness, freedom through awareness |
| [15-other-cycle-astrology-thinkers.md](15-other-cycle-astrology-thinkers.md) | Short entries: Ptolemy to Tarnas, Kondratiev to Gann, Schwabe/Hale to Halberg |

---

## 1. The one idea they share

Every figure here holds some version of one claim:

> **Events are not uniformly random in time. They come in rhythms, and at least some rhythms are shared across unrelated systems, which suggests a common, possibly cosmic, driver.**

They differ on three questions:

1. **What is the driver?** Planets as signs or causes (classical astrology, Paracelsus, Osho). The Sun's magnetic activity (Chizhevsky, heliobiology). An unknown "environmental force" (Dewey). Purely internal dynamics such as credit, demographics or predator–prey loops (most economists and ecologists).
2. **Is it causal, symbolic or synchronistic?** Ptolemy and Chizhevsky assume physical causation. Paracelsus and Osho mix physical with sympathetic "resonance". Jung and Tarnas talk of correspondence or synchronicity without a mechanism.
3. **Does knowing the cycle change anything?** Fatalists say no. Paracelsus ("the wise man rules the stars"), Osho (awareness frees you from the mechanical layer) and Dewey (forecasting allows preparation) all say knowing a cycle gives you some room to act.

## 2. Synthesis map

```
                         THE SKY
        ┌──────────────────┼────────────────────────┐
   Planets (symbolic/      Sun (physical:           Moon (tides,
   harmonic)               sunspots, flux,          lunations,
   │                       geomagnetism)            18.6-yr nodes)
   │                        │                        │
   Ptolemy → Abu Ma'shar    Schwabe 1843 (~11y)      McWhirter (nodes &
   (Jupiter–Saturn 20y)     Hale (22y magnetic)      business)
   → Kepler (aspects as     │                        Frank Brown (lunar
   harmonics)               Chizhevsky 1924 ──────┐  rhythms in organisms)
   → Paracelsus (star in    (mass excitability)   │  Osho (Moon & body)
     man, medicine)         │                     │
   → Gann / McWhirter /     Halberg (chrono-      │
     Merriman (markets)     biology, "chronomics")│
   → Barbault (cyclic       Ertel (re-analysis)   │
     index), Rudhyar,       Landscheidt / Jose ───┤  (solar motion tied
     Tarnas (outer-planet   (solar inertial       │   back to the planets)
     cycles & history)      motion)               │
   → Osho (inner/essential) │                     │
        │                   │                     │
        └────────┬──────────┴─────────────────────┘
                 ▼
     EMPIRICAL CYCLE HUNTING (no assumed cause)
     Dewey & FSC 1941: periodogram, Bartels test, synchrony
     Kitchin (~3.3y) · Juglar (7–11y) · Kuznets (15–25y) · Kondratiev (~50–60y)
     Lynx/hare ~9.6y · Strauss–Howe generational saeculum (~80–90y)
     Ray Tomes (harmonics of 2 and 3)
                 ▼
     THIS PROJECT'S ENGINE
     ephemeris (Swiss Eph) → planetary/solar time series
     cycles.py → periodogram + Bartels test + phase alignment
     → compare empirical cycles to planetary periods, honestly
```

## 3. How each strand connects to astrology

| Thinker | Link to astrology | Kind of claim |
|---|---|---|
| **Ptolemy** | Wrote the founding rationale: a physical "influence" from the heavens, strongest for Sun and Moon | Causal and naturalistic |
| **Abu Ma'shar** | Jupiter–Saturn conjunctions (~19.86 y) used to time dynasties and religions | Mundane astrology, historical cycles |
| **Paracelsus** | "Star in man": an inner firmament that mirrors the outer one; astrology as a branch of medicine | Microcosm/macrocosm, sympathy |
| **Kepler** | Reformed astrology into a theory of **harmonic aspects**; rejected most of the traditional detail | Geometric resonance |
| **Chizhevsky** | Not an astrologer, and he insisted on physics. But "the Sun's 11-year cycle shapes history" is mundane astrology rebuilt on solar physics | Physical (solar activity) |
| **Dewey** | Not an astrologer. Hunted cycles statistically, then noted that some periods sit near planetary ones and that unrelated series share phases | Empirical; cause left open |
| **Gann, McWhirter, Merriman** | Planetary cycles applied to markets | Financial astrology |
| **Barbault, Tarnas** | Outer-planet cycles (Jupiter–Pluto) correlated with historical waves | Mundane and archetypal |
| **Jung** | Synchronicity, meaning correspondence without cause; the 1952 astrological marriage experiment | Acausal |
| **Gauquelin** | The one statistical astrology result that survived for decades (the "Mars effect"), though still disputed | Empirical |
| **Osho** | Astrology as "the science of cosmic oneness". Splits it into essential, changeable and trivial layers. Meditation as the way out of the mechanical part | Spiritual/psychological |

## 4. What this means for the project's engine

The [cycles.py](11-edward-dewey-cycles.md#7-practical-recipe-a-dewey-style-cycle-analysis) workflow combines the strands:

1. **Get the sky as time series.** Use the Swiss Ephemeris to sample planetary longitudes, synodic angles (e.g. Jupiter–Saturn separation), Barbault's cyclic index and lunar-node position. Add solar data (sunspot number, from SILSO) and geomagnetic data (aa/Kp/Ap).
2. **Get the earthly series.** Prices, conflict counts, admissions and so on.
3. **Find cycles empirically** with Dewey's toolkit: detrend, periodogram, Bartels test.
4. **Only then** compare the periods you found with planetary and solar periods, and test whether the phases agree. Run it **out of sample**.
5. **Report honestly.** Use multiple-comparison corrections and surrogate data (shuffled, red-noise or phase-randomized), and state that a correlation does not establish a mechanism.

### Common planetary and solar periods for matching

| Period | Source |
|---|---|
| 27.3 d / 29.53 d | Sidereal / synodic month |
| ~27 d | Solar rotation (Carrington period 27.2753 d) |
| 0.4 y (Mercury), 1.6 y (Venus synodic 583.9 d), 2.135 y (Mars synodic 779.9 d) | Inner-planet synodic periods |
| 8.85 y / 18.61 y | Lunar apsidal / nodal cycles (18.6 = McWhirter's node cycle) |
| 11.86 y | Jupiter sidereal |
| ~11 y (9–14) / ~22 y | Schwabe sunspot / Hale magnetic cycle |
| 19.86 y | Jupiter–Saturn synodic ("great conjunction") |
| 29.46 y | Saturn sidereal |
| ~35.9 y / ~45.4 y | Saturn–Uranus / Saturn–Neptune synodic |
| ~60 y | Three Jupiter–Saturn conjunctions; near the Kondratiev range |
| 84.0 y / 164.8 y / 248 y | Uranus / Neptune / Pluto sidereal |
| ~127 y (mean) / ~171 y / ~492 y | Uranus–Pluto / Uranus–Neptune / Neptune–Pluto synodic periods |
| ~178.7 y | Solar inertial motion (Jose 1965) |
| ~88 y / ~210 y | Gleissberg / de Vries (Suess) solar cycles |

*(Values are rounded. Synodic periods of the slow planets vary from one cycle to the next because the orbits are eccentric. Uranus–Pluto ranges from about 110 to 145 years.)*

## 5. Scientific status, briefly

- **Solid:** cycles that are clearly physical, such as tides, seasons, the Schwabe/Hale solar cycles, circadian rhythms, lunar effects on many marine organisms, and predator–prey oscillations like lynx and hare.
- **Plausible but contested:** solar and geomagnetic effects on human health (some cardiovascular and mental-health associations are reported, but effects are small and inconsistent). Economic long waves (real in some data, disputed as true periodicities).
- **Weak or unsupported:** planetary cycles as predictors of individual lives or markets. Controlled tests of astrological prediction, such as Carlson 1985 in *Nature* and the large Dean and colleagues reviews, have not supported it. The Gauquelin Mars effect is still disputed.
- **Methodological trap:** cycle-hunting with periodograms reliably *finds* peaks in noise, especially in short, autocorrelated ("red-noise") series. Dewey knew this and used the Bartels test. Even so, scanning many periods across many series produces false positives unless you correct for it. See [11 §6](11-edward-dewey-cycles.md#6-scientific-status-and-pitfalls).

Treat the material as a **hypothesis library**. The engine's job is to test these ideas, not to assume they are true.
