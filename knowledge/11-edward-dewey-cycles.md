# 11 — Edward R. Dewey and the Science of Cycles

> "Everything that has been studied has been found to have cycles present." (Dewey's own summary claim; see the caveats in §6)

## 1. Who he was

- **Edward Russell Dewey (1895–1978)**, American economist.
- Around 1930–31 he worked as an economic analyst at the **US Department of Commerce**. Herbert Hoover's administration wanted to know what caused the Great Depression. Dewey said every economist he asked gave a different answer, and he came to suspect that recurring rhythms explained more than the theories did.
- The **Matamek Conference on Biological Cycles** (Canada, 1931) was convened by Copley Amory and gathered ecologists studying wildlife population cycles (lynx, hare, salmon). Its follow-on committee was reorganised as the **Foundation for the Study of Cycles (FSC)**, incorporated **10 January 1941**. Amory was chairman and Dewey director. Dewey led it for about three decades.
- FSC's aim was interdisciplinary: collect every series with apparent periodicity (economics, biology, climate, geology, sociology) and look for shared periods. It published the journal *Cycles* (from 1950) and still operates, now from Albuquerque, New Mexico, and partly as a commercial market-cycles service.

### Key books

| Year | Title | Notes |
|---|---|---|
| 1947 | *Cycles: The Science of Prediction* (with **Edwin F. Dakin**), Henry Holt | Argues the US economy is driven by a few superimposed cycles: ~54-yr, ~18⅓-yr building, ~9-yr and ~41-month. **Milton Friedman** reviewed it harshly: evidence not fully presented, results not reproducible. |
| 1967 | *The Case for Cycles* (FSC) | Short manifesto version. |
| 1970 | *Cycles: Selected Writings* (FSC, Pittsburgh) | Anthology of his *Cycles* articles. The best source for his technical method. |
| 1971 | *Cycles: The Mysterious Forces That Trigger Events* (with **Og Mandino**), Hawthorn | Popular book. Covers the cycle catalogue, cycle synchrony, Chizhevsky's war/sunspot work and speculation on cosmic causes. Later reissued by Harriman House. |

## 2. Dewey's core claims

1. **Ubiquity.** Rhythmic fluctuations show up across almost every kind of time series.
2. **Persistence.** Some cycles continue for many repetitions with stable period and phase, beyond what chance would produce. He backed this with the Bartels test (§3.5).
3. **Common periods.** Unrelated phenomena share the same period, e.g. ~9.6 y in lynx, salmon, insect outbreaks and some economic series.
4. **Synchrony.** Cycles with the same period in unrelated series also tend to **peak at about the same calendar time**. For Dewey this was the strongest clue to an **external, environmental driver**. He did not name the driver dogmatically but speculated about solar, planetary, cosmic-ray and electromagnetic causes.
5. **Harmonic ratios.** Many common periods are related by factors of **2 and 3**. His "cycle table" starts from **17.75 years** and generates related periods by multiplying or dividing by 2 and 3 (e.g. 35.5, 53.25, 71, 106.5…; 8.875, 5.92…).
6. **Forecasting.** If a cycle is real and persistent, extrapolating it gives a probabilistic forecast. It does not give certainty, and cycles can "invert" or disappear (Dewey acknowledged this).

## 3. Dewey's method, step by step

Dewey's workflow pre-dates easy computing. Much of it was done by hand or on early mainframes. Here is a modern restatement.

### 3.1 Data preparation
- Use the longest, most homogeneous series you can get, at a consistent sampling interval (annual, monthly).
- Take **logarithms** of series that grow exponentially, such as prices and production, so the cycles are proportional.

### 3.2 Detrending: moving averages and "ratio-to-trend"
- Compute a **centred moving average** whose length equals the cycle you are trying to remove or isolate. A moving average of length *P* removes a cycle of period *P* (and its harmonics) almost completely.
- **Ratio-to-trend** (Dewey's standard): divide each value by the moving average, i.e. `x_t / MA_t`, to get a percentage deviation series. For log data, subtract instead.
- To isolate a band, Dewey often used **two moving averages**: a long one to remove trend and a shorter one to smooth away shorter cycles. The difference between them is effectively a band-pass filter.
- *Caveat:* moving averages can **create** spurious oscillations (the **Slutsky–Yule effect**, Slutsky 1927). Smoothing random noise produces wave-like series. This is the single biggest hazard of the method.

### 3.3 Spotting candidate periods
- **Visual inspection** and peak-to-peak counting on the detrended series.
- **Periodogram or spectral analysis.** Dewey used Schuster-type periodograms and Buys-Ballot tables. A Buys-Ballot table folds the series at a trial period and averages each phase; a strong cycle gives a large-amplitude average profile. Modern equivalents are the FFT periodogram, the **Lomb–Scargle** periodogram for uneven data, and the Bloomfield/Welch methods.

### 3.4 Fitting the cycle
- For a trial period *P*, fit `y_t ≈ A·cos(2πt/P − φ)` by least squares to get amplitude *A* and phase φ, which fixes the crest dates.
- **Refine** *P* by scanning nearby values to maximise amplitude or explained variance.

### 3.5 Testing significance: the Bartels test
From **Julius Bartels (1899–1964)**, a German geophysicist. See Bartels 1935, *"Random fluctuations, persistence, and quasi-persistence in geophysical and cosmical periodicities"*, *Terrestrial Magnetism and Atmospheric Electricity* 40.

Idea: cut the series into *n* consecutive segments, each one cycle (*P*) long. For each segment compute the harmonic vector (amplitude and phase at period *P*). If the cycle is real and persistent, the vectors point the same way and add up. If it is noise, their phases are random and they tend to cancel.

- Let `v_k` = complex harmonic coefficient for segment *k* (k = 1..n).
- Mean vector `V = (1/n) Σ v_k`; observed amplitude `A = |V|`.
- Expected amplitude if phases were random: `K = sqrt( Σ|v_k|² ) / n` (the "expectancy").
- **Bartels ratio** `r = A / K`. **Probability of chance** `p ≈ exp(−r²)`.
- FSC convention: **p < 0.05** suggests significance, p < 0.01 is strong. Commercial cycle software usually shows "Bartels score" = p or 1 − p. **Check which convention a tool uses.**
- *Caveat:* the formula assumes segments are independent. Red noise (autocorrelated data) makes neighbouring segments similar and **inflates** significance. Testing many trial periods requires a multiple-comparisons correction.

### 3.6 Synchrony and cross-series comparison
- Collect all series showing roughly the same period. Shift them to a common reference and compare crest dates. Dewey published tables of 9.6-yr and 18.2-yr cycles with crests clustering near the same years.
- He read tight crest clustering across physically unrelated systems as evidence of a shared external pacemaker.

## 4. Famous cycles in Dewey's catalogue

| Period | Phenomena (as reported by Dewey/FSC) | Status today |
|---|---|---|
| **~9.6 years** | Canadian lynx pelts (Hudson's Bay Co. records), snowshoe hare, Atlantic salmon abundance, tent caterpillar and chinch bug outbreaks, some disease and economic series; the "9.6-year cycle" flagship | Lynx–hare ~9–10 yr cycle is **robust** (Elton & Nicholson 1942; Bulmer 1974 estimated ~9.63 yr), explained mainly by predator–prey and food-web dynamics (Krebs et al.). A shared extra-ecological cause is **not established**. |
| **~9.2 years** | US stock prices, some industrial series | Weak; not a standard finding in financial econometrics. |
| **~17.75 years** | Base of Dewey's 2×/3× harmonic table; various economic and natural series | Speculative. |
| **~18.2 years / ~18⅓ years** | Real-estate and building activity (Dewey & Dakin); some natural series | US building cycles of ~18–20 yr are documented historically (Kuznets-type swings, Homer Hoyt's Chicago land-value studies). Periodicity is loose. Not the same as the 18.6-yr lunar nodal cycle, though some writers link them. |
| **~54 years** | Wholesale prices, interest rates: the **Kondratiev** wave | Long waves are debated. Few repetitions in the data make strict periodicity untestable. |
| **~41 months (3.4 y)** | Stock prices, business inventories: the **Kitchin** cycle (Kitchin 1923 found ~40 months) | Inventory-cycle-type fluctuations are real; strict periodicity is doubtful. |
| **~3.86 / ~4 years** | Various economic series; the US "presidential cycle" in stocks is often mentioned alongside | A political-calendar effect, not a natural cycle. Weak out of sample. |
| **~5.9 / 8 / 12 / 22 / 100+ years** | Many others in FSC files: rainfall, tree rings, war (Dewey's "war cycles" of ~11.2, 17.7, 22.1, 142 yrs) | Mostly unreplicated. |

### Dewey and Chizhevsky
Dewey popularised Chizhevsky in the West. His 1971 book summarises the four-phase "mass excitability" cycle and reproduces Chizhevsky's war/sunspot chart. Dewey also noted a problem: in Chizhevsky's data the sunspot peak sometimes *precedes* the excitability index by about a year. See [12-chizhevsky.md](12-chizhevsky.md).

## 5. Planetary-period connections

Dewey insisted he was not an astrologer. He did list possible "environmental forces", and he and FSC researchers pointed to near-matches between empirical cycles and astronomical periods:

- **~11.86 yr** (Jupiter's orbit) and **~11 yr** (sunspots), against ~11–12 yr economic and climate cycles.
- **~19.86 yr** (Jupiter–Saturn synodic) and its halves/thirds, against ~9.6–9.9 and ~18–20 yr cycles.
- **~59.6 yr** (three J–S conjunctions), close to the Kondratiev range.
- **~17.75 yr** has no tidy planetary match. Dewey treated it as a numerical base, not a planetary period.

### Successors

**Paul D. Jose (1965)**, *"Sun's motion and sunspots"*, *Astronomical Journal* 70. The Sun orbits the solar system's barycentre, mainly because of Jupiter and Saturn. Jose found a **~178.7-year** periodicity in that solar inertial motion (SIM) and proposed it modulates sunspot cycles.

**Theodor Landscheidt (1927–2004)** extended Jose. He used changes in the Sun's orbital angular momentum ("torque cycles" or "impulses of torque", IOT) to forecast solar-activity extremes, El Niño, and a **Gleissberg-type grand minimum around 2030**. Results were mixed. Some forecasts (e.g. a weak solar cycle 24) were in line with what happened. Others (several ENSO calls) failed. Mainstream solar physics regards planetary–solar coupling as **unproven**: planetary tidal forces on the Sun are tiny, and the barycentric argument is criticised on physical grounds. It is still an active minority research line (e.g. Scafetta, Stefani et al. on Venus–Earth–Jupiter tidal synchronisation of the dynamo).

**Ray Tomes (New Zealand)** developed a **"Harmonics Theory"**. All observed cycles, economic to cosmological, would be harmonics of a single fundamental, with periods related by small-integer ratios (mainly 2 and 3, extending Dewey's table). He compiled FSC-reported periods to show clustering near harmonic values. It is speculative and appears outside the peer-reviewed literature. With enough ratios, clustering near harmonics is easy to produce by chance.

**FSC after Dewey.** Later FSC researchers (e.g. Richard Mogey) and commercial cycle analysts (Hurst, Millard, Bressert) moved the toolkit into trading software: spectral scans plus Bartels scores.

## 6. Scientific status and pitfalls

- **Friedman's critique (1948)** still applies to much cycle work: undocumented data handling, results that cannot be reproduced, and claims that run ahead of the tests.
- **Spurious cycles.** Moving averages create them (Slutsky–Yule). So does red noise, since economic and ecological series are strongly autocorrelated and their spectra rise toward low frequencies. Periodogram peaks against a white-noise null are therefore misleading. Test against an **AR(1)/red-noise null** (as in Torrence & Compo 1998 for wavelets) or phase-randomised surrogates.
- **Look-elsewhere effect.** Scanning hundreds of trial periods in hundreds of series *guarantees* "significant" hits. Correct with Bonferroni or FDR, or better, pre-register the period you will test.
- **Few repetitions.** A 54-yr cycle in 200 years of data repeats fewer than 4 times. No statistic can establish periodicity from that.
- **Quasi-periodicity.** Even real cycles (sunspots, 9–14 yr; lynx) drift in period and amplitude. Strict sine extrapolation fails, and **out-of-sample** testing is the only honest check.
- **Synchrony claims** need a significance test. Phase clustering of a few hand-picked series is weak evidence, and selection of which series to show is a major bias.
- **What holds up:** physically driven cycles (seasonal, tidal, solar, predator–prey) and loose business-cycle regularities. Hard-periodic economic "cycles" that forecast reliably have not survived out-of-sample testing in academic finance and economics.

## 7. Practical recipe: a Dewey-style cycle analysis

The project's engine implements this in **`astro/cycles.py`**: `ratio_to_trend`, `periodogram`, `bartels`, `fit_sine`, `synthesize` and the one-call `dewey_scan`. `bartels()` returns **p**, the probability that the cycle is chance, so lower is better. Periods are given in samples (e.g. years for annual data).

**Step 0 — State the hypothesis first.** Example: "US stock index has a ~19.86-yr cycle phase-locked to Jupiter–Saturn conjunctions." Write down the period and expected phase *before* looking. This is the main defence against false positives.

**Step 1 — Load and clean.**
```python
import numpy as np
y = np.log(series)            # log for growth series
t = np.arange(len(y)) * dt    # dt = sampling interval in years
```

**Step 2 — Detrend.**
- Option A (Dewey): ratio-to-trend with a centred moving average of length > 2× the longest period of interest.
- Option B (modern): subtract a low-order polynomial or LOESS trend, or first-difference.
- Keep a copy of the raw series. Check that the result is not an artifact of the detrending choice by trying two methods.

**Step 3 — Periodogram.**
```python
from astro import cycles
y_detr = cycles.ratio_to_trend(series, window=21)       # Dewey detrend (Step 2, option A)
peaks = cycles.periodogram(y_detr, np.arange(3, 60, 0.1))[:10]   # [(period, amplitude), ...]
# or all-in-one: cycles.dewey_scan(series, periods, trend_window=21, top=10)
```
Plot power against **period** on a log axis.

**Step 4 — Build a noise null.** Fit AR(1) to the detrended series. Generate about 1000 surrogate series and take the 95th/99th percentile of their periodogram at each frequency. Only peaks above this red-noise envelope count as candidates.

**Step 5 — Bartels test on each candidate.**
```python
for P in candidate_periods:
    p = cycles.bartels(y_detr, P)   # p ≈ exp(-r²), probability the cycle is chance
```
Keep cycles with p < 0.05 **after** correcting for the number of periods tested.

**Step 6 — Fit amplitude and phase.** `cycles.fit_sine(y, P)`: least-squares sine fit at the refined period gives crest dates. Check stability by fitting the first half and second half separately: the period and phase should roughly agree.

**Step 7 — Out-of-sample test.** `cycles.synthesize(y_train, periods, horizon=n)` projects forward. Fit on data up to year *T*, forecast *T*…end, and score the forecast against naive baselines (random walk, climatology). A cycle that fails this is descriptive, not predictive.

**Step 8 — Synchrony and astronomy (optional).**
- Compare the period with the astronomical periods table in [10-cycles-thinkers.md](10-cycles-thinkers.md#common-planetary-and-solar-periods-for-matching).
- For planetary hypotheses, build the *actual* ephemeris-derived series (e.g. cos of the Jupiter–Saturn angle, or sunspot number) and test **phase coherence** against the earthly series, using cross-spectral coherence or the phase-locking value with surrogate significance. Do not just match periods: with dozens of planetary periods available, something will always be close.

**Step 9 — Report.** Give the period, amplitude, phase, Bartels p, the red-noise and multiple-test-corrected significance, the number of repetitions in the data, and out-of-sample skill. Treat a cycle with fewer than about 5 repetitions as **anecdotal**.

## Sources and further reading
- Dewey & Dakin, *Cycles: The Science of Prediction* (1947); Dewey & Mandino, *Cycles: The Mysterious Forces That Trigger Events* (1971); Dewey, *Cycles: Selected Writings* (1970).
- Friedman, M., review of Dewey & Dakin, *Journal of the American Statistical Association* (1948).
- Bartels, J. (1935), *Terr. Magn. Atmos. Electr.* 40:1–60.
- Slutsky, E. (1927/1937), "The summation of random causes as the source of cyclic processes", *Econometrica* 5.
- Jose, P. D. (1965), *Astron. J.* 70:193. Landscheidt, T., *Sun–Earth–Man: A Mesh of Cosmic Oscillations* (1989).
- Torrence & Compo (1998), "A practical guide to wavelet analysis", *BAMS* 79.
- Wikipedia: [Edward R. Dewey](https://en.wikipedia.org/wiki/Edward_R._Dewey), [Foundation for the Study of Cycles](https://en.wikipedia.org/wiki/Foundation_for_the_Study_of_Cycles).
