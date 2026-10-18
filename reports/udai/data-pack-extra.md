# Data pack: extra computations

Reference chart: 22 Jun 1999, 21:35 IST, Mumbai (18N58, 72E49), Lahiri ayanamsa, true node. The code is in `astro/strength.py` and `astro/special.py`, and the checks are in `tests/test_strength.py`. "PL" means Parashara's Light 9.0.

## Strength and special points

### What matches PL and what doesn't

| Item | PL shows | Engine | Status |
|---|---|---|---|
| Gulika | Sag 26:18 (P.Ashadha) | Sag 26:18:55 | **Match.** Lagna at the *end* of Saturn's 1/8 portion. On a Tuesday night that portion is the 1st (19:14:54 to 20:36:21 IST). |
| Mandi | Sag 17:02 (P.Ashadha) | Sag 17:02:58 | **Match.** Lagna 2 ghatis after sunset on a Tuesday night (the Phaladeepika rule), scaled to the real length of the night. |
| "Be" | Lib 03:59 (Chitra) | Beeja sphuta = Sun + Venus + Jupiter = Lib 03:59:17, Chitra | **Match.** It is not the Bhrigu Bindu, which is Leo 24:18. |
| Shadbala ratios | Su 1.51, Mo 1.36, Ma 1.71, Me 0.94, Ju 1.12, Ve 1.50, Sa 0.99 | 1.528, 1.389, 1.719, **0.937, 1.121, 1.504, 0.987** | Me, Ju, Ve, Sa match to 2 decimals. Ma is +0.01, Su +0.02, Mo +0.03. **The rank order is identical.** |
| House-2 border number "308.67" | 308.67 | Bhava bala of house 2 = 378.27 virupas | **No match** (see below). |

Sunrise and sunset use the Hindu definition: centre of the disc, true horizon, no refraction. That gives sunrise 06:06:15, sunset 19:14:54 and next sunrise 06:06:29 IST. Only this definition reproduces Gulika and Mandi to the arcminute; with upper limb and refraction both points come out about 40′ later.

### Shadbala (virupas)

The required minimums are Sun **6.5**, Moon 6, Mars 5, Mercury 7, Jupiter 6.5, Venus 5.5 and Saturn 5 rupas. PL's Sun ratio of 1.51 is only reproduced with the standard BPHS/Raman minimum of 6.5. With 5 rupas the Sun would need about 143 virupas less than any reading of the rules gives.

| Planet | Uchcha | Saptavargaja | Oja-yugma | Kendradi | Drekkana | **Sthana** | **Dig** | Natonnata | Paksha | Tribhaga | Abda/Masa/Vara/Hora | Ayana | Yuddha | **Kala** | **Chesta** | **Naisargika** | **Drik** | **Total** | Rupas | Ratio | PL | Diff (virupas) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sun | 41.01 | 142.50 | 30 | 15 | 15 | 243.51 | 14.63 | 15.47 | 22.81 | 0 | 60 (hora) | 118.59 | 0 | 216.87 | 59.29 | 60.00 | 1.49 | 595.79 | 9.93 | 1.528 | 1.51 | +6.9 |
| Moon | 11.49 | 142.50 | 30 | 15 | 15 | 213.99 | 8.18 | 44.53 | 74.39 | 0 | 15 (abda) | 40.89 | 0 | 174.81 | 37.19 | 51.43 | 14.58 | 500.17 | 8.34 | 1.389 | 1.36 | +10.6 |
| Mars | 21.56 | 127.50 | 30 | 60 | 15 | 254.06 | 53.20 | 44.53 | 22.81 | 0 | 45 (vara) | 17.20 | 0 | 129.54 | 44.90 | 17.14 | 16.71 | 515.56 | 8.59 | 1.719 | 1.71 | +2.6 |
| Mercury | 35.49 | 60.00 | 0 | 60 | 0 | 155.49 | 3.34 | 60.00 | 37.19 | 0 | 30 (masa) | 56.34 | 0 | 183.53 | 33.72 | 25.71 | −8.18 | 393.62 | 6.56 | 0.937 | 0.94 | −1.2 |
| Jupiter | 30.07 | 63.75 | 15 | 60 | 15 | 183.82 | 32.09 | 15.47 | 37.19 | 60 | 0 | 43.92 | 0 | 156.59 | 22.18 | 34.29 | 8.37 | 437.34 | 7.29 | 1.121 | 1.12 | +0.5 |
| Venus | 21.73 | 97.50 | 30 | 60 | 15 | 224.23 | 30.42 | 15.47 | 37.19 | 60 | 0 | 50.17 | 0 | 162.84 | 40.26 | 42.86 | −4.17 | 496.44 | 8.27 | 1.504 | 1.50 | +1.4 |
| Saturn | 0.14 | 65.62 | 15 | 60 | 15 | 155.77 | 32.70 | 44.53 | 22.81 | 0 | 0 | 10.17 | 0 | 77.50 | 16.44 | 8.57 | 5.00 | 295.97 | 4.93 | 0.987 | 0.99 | −1.0 |

- **Ratio rank** (same as PL): Mars > Sun > Venus > Moon > Jupiter > Saturn > Mercury.
  - **Strongest:** Mars (1.72).
  - **Weakest:** Mercury (0.94).
  - Both Mercury and Saturn fall below their minimums.
- **Rank by absolute rupas:** Sun 9.93 > Mars 8.59 > Moon 8.34 > Venus 8.27 > Jupiter 7.29 > Mercury 6.56 > Saturn 4.93.

**Conventions used.** A brute-force search over about 37,000 combinations of textual variants chose these.

- **Saptavargaja** uses the compound (5-fold) relationship, with temporal friendship from the D1. Moolatrikona (45) counts in the D1 only; exaltation gets no special score in the vargas.
- **Kendradi** uses whole-sign houses. Sripati houses would move Mars to the 9th and Jupiter to the 3rd, and that breaks both.
- **Dig bala** uses the true lagna and MC.
- **Natonnata** is measured from apparent midnight, using the Sun's hour angle.
- **Paksha bala:**
  - Mercury counts as a benefic.
  - The Moon's paksha bala is doubled.
- **Chesta bala:**
  - The Sun's chesta is its (single) ayana bala, and the Moon's is its (single) paksha bala.
  - For the other planets, the seeghra kendra uses the *true heliocentric* (manda-corrected) planet and the mean Sun. Meeus mean elements were worse, for example Mercury 26.8 against the implied 34.9.
- **Ayana bala** uses the declination of the ecliptic point, and is doubled for the Sun.
- **Year and month lords** come from the Kali ahargana (Raman's method): year Moon, month Mercury, weekday Mars. The hora lord is the Sun, counting 1-hour horas from sunrise.
- **Drik bala** is ¼ of (benefic − malefic) sphuta drishti, with Raman's special-aspect additions.
- **Yuddha:** there is no planetary war in this chart.

**One empirical deviation: tribhaga.** BPHS and Raman give the three thirds of the night to the Moon, Venus and Mars, in that order. Birth falls in the first third (19:15–22:52), so by the text the Moon gets 60. But PL's totals for the Moon (about −60) and Venus (about +60) only fit if *Venus* takes it. The engine defaults to Venus to match PL; set `Options(tribhaga_night=("Moon","Venus","Mars"))` to follow the text. That changes the Moon to 1.556 and Venus to 1.322.

**Remaining residuals.**
- Sun +6.9, Moon +10.6 and Mars +2.6 virupas. No single discrete rule removes them.
- A true declination (with latitude) for ayana halves the Moon's residual, but makes Venus, Mars and Saturn worse.
- They most likely come from PL's internal formulas for ayana, chesta and natonnata (Surya Siddhanta-style mean motions or kranti tables), which can't be recovered from seven 2-decimal ratios.

### Ishta and Kashta phala

These are √(uchcha × chesta) and √((60 − uchcha)(60 − chesta)). The Sun's chesta here is its ayana bala, and the Moon's is its paksha bala.

| | Sun | Moon | Mars | Mercury | Jupiter | Venus | Saturn |
|---|---|---|---|---|---|---|---|
| Ishta | **49.31** | 20.67 | 31.12 | 34.59 | 25.83 | 29.58 | 1.53 |
| Kashta | 3.66 | 33.26 | 24.09 | 25.38 | 33.64 | 27.48 | **51.07** |

The Sun is the most auspicious and Saturn the least: Saturn is at its deepest debilitation and moving slowly.

### Upagrahas and sphutas

| Point | Longitude | Rule |
|---|---|---|
| Gulika | Sag 26:18 P.Ashadha | End of Saturn's portion (PL). Start of the portion: Sag 06:51; middle: Sag 16:24. |
| Mandi | Sag 17:02 P.Ashadha | Tuesday night, 2 ghatis after sunset |
| Dhuma | Lib 20:17 Vishakha | Sun + 133°20′ |
| Vyatipata | Vir 09:42 U.Phalguni | 360° − Dhuma |
| Parivesha | Pis 09:42 U.Bhadrapada | Vyatipata + 180° |
| Indrachapa | Ari 20:17 Bharani | 360° − Parivesha |
| Upaketu | Tau 06:57 Krittika | Indrachapa + 16°40′ (= Sun − 30°) |
| **Beeja sphuta ("Be")** | **Lib 03:59 Chitra** | Sun + Venus + Jupiter |
| Kshetra sphuta | Ari 06:26 Ashwini | Moon + Mars + Jupiter |
| Bhrigu Bindu | Leo 24:18 P.Phalguni | Midpoint of Rahu → Moon |

### Special lagnas and Yogi

| Point | Value |
|---|---|
| Hora Lagna | Vir 20:43 Hasta |
| Ghatika Lagna | Leo 27:16 U.Phalguni |
| Bhava Lagna | Cap 28:31 Dhanishta |
| Pranapada | Vir 00:42 U.Phalguni |
| **Indu Lagna** | **Aries**. The 9th lord from the lagna is Mercury (8 kalas) and from the Moon is Venus (12 kalas): 20 mod 12 = 8, and the 8th from the Moon is Aries, holding Jupiter and Saturn. |
| Sri Lagna | Gem 02:03 Mrigashira |
| Varnada Lagna | Gemini |
| Yogi point | Pis 08:49 U.Bhadrapada |
| **Yogi** | **Saturn** |
| Duplicate Yogi | Jupiter |
| Avayogi point | Vir 15:29 Hasta |
| **Avayogi** | **Moon** |

The Hora, Ghatika and Bhava lagnas count from the Sun's longitude at sunrise.

### Vimshopaka bala (out of 20)

Scoring is BPHS: own, exalted or moolatrikona sign 20, great friend 18, friend 15, neutral 10, enemy 7, great enemy 5. Each varga is weighted by its share of the scheme.

| Scheme | Sun | Moon | Mars | Mercury | Jupiter | Venus | Saturn |
|---|---|---|---|---|---|---|---|
| Shadvarga | 16.50 | **18.25** | 15.25 | 10.00 | 10.65 | 15.40 | 9.90 |
| Saptavarga | 16.80 | **18.15** | 15.25 | 10.62 | 10.65 | 14.70 | 9.95 |
| Dashavarga | **17.17** | 16.27 | 14.12 | 13.62 | 9.62 | 16.20 | 9.95 |
| Shodashavarga | **16.50** | 16.07 | 13.95 | 13.57 | 10.35 | 15.90 | 11.52 |

### Bhava bala (Raman: lord's shadbala + bhava dig bala + bhava drishti; equal-house madhyas from the lagna)

| House | Madhya | Lord | Adhipati | Dig | Drishti | Total (virupas) | Rupas |
|---|---|---|---|---|---|---|---|
| 1 | Cap 11:29 | Sa | 295.97 | 30 | 56.98 | 382.94 | 6.38 |
| 2 | Aqu 11:29 | Sa | 295.97 | 50 | 32.30 | 378.27 | 6.30 |
| 3 | Pis 11:29 | Ju | 437.34 | 50 | 32.68 | 520.02 | 8.67 |
| 4 | Ari 11:29 | Ma | 515.56 | 0 | 14.51 | 530.08 | 8.83 |
| 5 | Tau 11:29 | Ve | 496.44 | 10 | 0.16 | 506.60 | 8.44 |
| 6 | Gem 11:29 | Me | 393.62 | 10 | 18.02 | 421.64 | 7.03 |
| 7 | Can 11:29 | Mo | 500.17 | 30 | 20.30 | 550.47 | 9.17 |
| 8 | Leo 11:29 | Su | 595.79 | 40 | 45.34 | 681.13 | 11.35 |
| 9 | Vir 11:29 | Me | 393.62 | 20 | 27.32 | 440.94 | 7.35 |
| 10 | Lib 11:29 | Ve | 496.44 | 30 | 88.20 | 614.63 | 10.24 |
| 11 | Sco 11:29 | Ma | 515.56 | 20 | 56.63 | 592.20 | 9.87 |
| 12 | Sag 11:29 | Ju | 437.34 | 50 | 57.57 | 544.91 | 9.08 |

**Ranking:** 8 > 10 > 11 > 7 > 12 > 4 > 3 > 5 > 9 > 6 > 1 > 2. The two Saturn-ruled houses, the 1st and 2nd, are weakest because Saturn is the weakest planet in absolute rupas.

**The "308.67" in PL's border is not matched.**
- "11Aqu29 32 308.67" breaks down as the equal-house cusp of house 2, its sarvashtakavarga (32, which matches the engine) and an unknown number.
- 308.67 is not a cusp longitude in any of the 23 Swiss Ephemeris house systems.
- As a bhava bala, it would leave only about 12 virupas beyond Saturn's own shadbala of about 296–297. Every textual variant tested gives 298–390.
- The only near hit (309.5) needs the bhava dig bala set to zero and Saturn's special aspect dropped, which is not principled.
- Values for the other 11 houses from the PL screen would settle what this number is.

### Sripati (bhava chalit) houses

Each quadrant between the lagna (Cap 11:29) and MC (Lib 23:04) is trisected to give the bhava madhyas; the sandhis lie halfway between them. These agree with Swiss Ephemeris system 'S' to 1e-6°.

| House | Sandhi (start) | Madhya |
|---|---|---|
| 1 | Sag 28:25 | Cap 11:29 |
| 2 | Cap 28:25 | Aqu 15:21 |
| 3 | Pis 02:17 | Pis 19:12 |
| 4 | Ari 06:08 | Ari 23:04 |
| 5 | Tau 06:08 | Tau 19:12 |
| 6 | Gem 02:17 | Gem 15:21 |
| 7 | Gem 28:25 | Can 11:29 |
| 8 | Can 28:25 | Leo 15:21 |
| 9 | Vir 02:17 | Vir 19:12 |
| 10 | Lib 06:08 | Lib 23:04 |
| 11 | Sco 06:08 | Sco 19:12 |
| 12 | Sag 02:17 | Sag 15:21 |

**Planets that change house under bhava chalit:**
- **Mars** moves from the 10th to the **9th**. At Lib 2:41 it is before the 10th sandhi at Lib 6:08.
- **Jupiter** moves from the 4th to the **3rd**. At Ari 5:12 it is before the 4th sandhi at Ari 6:08, a margin of only 56′.
- Saturn (Ari 19:34) stays in the 4th.
- Mercury (Can 1:28) stays in the 7th, just past the Gem 28:25 sandhi.
- Every other planet keeps its whole-sign house.
