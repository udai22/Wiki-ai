# Astrology Software: The Landscape and a Recommendation

> Part of the knowledge base. The background on how charts are computed is in [01-how-astrology-works.md §3](01-how-astrology-works.md#3-how-a-chart-is-computed-ephemeris--time--place). The guide to the Parashara's Light screen is [03-reading-parasharas-light.md](03-reading-parasharas-light.md).
>
> **Caveat on prices.** Prices and editions change often and resellers quote inconsistent figures. The numbers below are indicative, checked in late 2026 where possible. Confirm on the vendor's own site before buying.

---

## 1. The backbone: Swiss Ephemeris

Almost every serious astrology program, free or commercial, Vedic or Western, takes its planetary positions from the same engine.

- **Who.** The Swiss Ephemeris was written by Dieter Koch and Alois Treindl at **Astrodienst AG** (Zollikon/Zürich, the company behind astro.com) and first released in 1997.
- **What it is.**
  - A C library that compresses NASA/JPL's numerical planetary integrations (DE431; DE440/441 are supported from version 2.10) into compact data files.
  - It covers roughly 13,000 BCE to 17,000 CE, at sub-milliarcsecond agreement with JPL for modern dates.
  - It also contains the Moshier analytic fallback (about 1″) for use without data files.
- **What it provides.** Planets, the nodes (mean and true), asteroids, fixed stars, house systems (about 20, including Placidus, Koch, whole sign and Sripati), **more than 40 ayanamsas** (Lahiri, Raman, KP, Fagan-Bradley, True Chitra …), eclipses, risings and settings, and ΔT.
- **Licensing** (dual):
  1. **GNU AGPL.** Free to use, but if you distribute the software, or run it as a public network service, your whole project must be released under the AGPL or a compatible license.
  2. **Swiss Ephemeris Professional License**, for closed-source or commercial use. A one-time fee to Astrodienst; the current contract lists about **CHF 700** for unlimited projects. Verify this on astro.com/swisseph.
- **Why it matters.** When two good programs disagree about a chart, the cause is almost never the ephemeris. It is a **setting**: ayanamsa, true or mean node, time zone or DST, house system, or dasha year length. Precision has effectively been solved; what differs between programs is **interpretive features and user experience**.

> **This repository's own engine** (`astro/`) uses **pyswisseph** (the Python binding to the Swiss Ephemeris) for all positions, with Lahiri ayanamsa and BPHS tables layered on top. It reproduces the reference chart's Parashara's Light positions to the arc-minute. Because pyswisseph is AGPL, any public deployment of this code must follow AGPL terms, unless a professional license is bought.

---

## 2. Vedic (Jyotish) desktop programs

| Program | Developer | Platform | Price (indicative) | Strengths | Weaknesses |
|---|---|---|---|---|---|
| **Parashara's Light 9.0** | GeoVision Software (USA) / Parashara Software (India) | Windows; separate Mac edition | Paid. Personal, Commercial and Professional editions, roughly US$100–400 / ₹5k–35k by edition and reseller. | Polished and beginner-friendly. Strong classical text references (built-in interpretations), many languages, reports, North/South Indian charts, Ashtakavarga and kaksha, Shadbala, yogas, KP module. | Paid upgrades. Less configurable for advanced Jaimini and Kalachakra research than JHora or Kala. Windows-centric. |
| **Jagannatha Hora (JHora)** | P. V. R. Narasimha Rao | Windows (runs under Wine/CrossOver on Mac/Linux) | **Free** | The most technically complete free Vedic program: dozens of dashas (Vimshottari, Kalachakra, Narayana, Chara, Shoola, Sudarshana …), all vargas including custom ones, every special lagna, arudhas, Tajika, muhurta and panchanga search. Swiss Ephemeris inside. | Dense, dated UI with a steep learning curve. No official support. No longer actively developed (last major version 8.0). |
| **Kala** | Ernst Wilhelm (Vedic Software) | Windows | Paid (a few hundred US$) | Strong rigorous classical calculation; excellent Shadbala and Vimshopaka, muhurta, beautiful charts; reflects the author's teaching. | Windows only; smaller user community. |
| **Shri Jyoti Star** (v9/v10) | Vedic Software | Windows (v10 available via the Microsoft Store, with a free base and paid modules) | Free base to roughly US$100+ for Pro/Jaimini modules | Modular; Parashari, Jaimini, Tajika, KP and Western; Swiss Ephemeris; good research tools (chart databases, search). | Mixed UI; feature set depends on which modules you buy. |
| **Junior Jyotish / LeoStar** | Futurepoint (New Delhi, founded 1985 by Arun Bansal; LeoStar is its flagship) | Windows; Android apps | Paid (₹, various tiers) | India-market standard for professional printouts: Hindi and regional languages, Lal Kitab, KP, varshaphal, matching. | Interface and English documentation aimed at the Indian commercial market; less suited to research. |
| **Maitreya** (8/9) | Martin Pettau | Windows, macOS, Linux | **Free, open source (GPL)** | Cross-platform; both Vedic and Western; Swiss Ephemeris; Ashtakavarga, dashas, vargas, transits. | Smaller feature set than JHora; sporadic development. |

## 3. Western and Hellenistic programs

| Program | Developer | Platform | Price | Strengths |
|---|---|---|---|---|
| **Solar Fire Gold (v9)** | Esoteric Technologies (Australia); sold through Astrolabe | Windows; the same team's **Astro Gold** covers Mac and iOS | Paid, about US$360 new | The Western professional standard: progressions, directions, returns, harmonics, midpoints, astro-mapping, huge reports, Swiss Ephemeris. A sidereal/Vedic mode exists but is basic. |
| **Sirius** / **Kepler** | Cosmic Patterns (David Cochrane) | Windows | Paid (Kepler is cheaper; Sirius is the flagship) | Very broad: research and statistics modules, harmonic and vibrational astrology, a Vedic module, animated charts. Kepler adds an extensive interpretive and teaching layer. |
| **Janus** (v5/v6) | Astrology House (New Zealand) | Windows (Mac via an emulator) | Paid | Strongest commercial tool for **horary and traditional/Hellenistic** work: Lilly-style horary, dignity tables, profections, firdaria, primary directions; also a Vedic module. |
| **Morinus** | Robert Nagy (open source) | Windows, macOS, Linux (Python) | **Free (GPL)** | Traditional and Morinian astrology, primary directions (very precise), profections, firdaria, Arabic parts. Swiss Ephemeris. |
| **Astrolog** | Walter Pullen | All platforms | **Free** | Long-lived, fast, scriptable; Western and sidereal; many chart types and astro-graph maps. |

## 4. Web services

| Service | Operator | Price | Notes |
|---|---|---|---|
| **Astro.com** | Astrodienst (home of the Swiss Ephemeris) | Free charts; paid reports | The reference source for free chart drawing, with the **Astro-Databank** of famous births rated by data quality (Rodden ratings) and an atlas with historical time-zone data, which is the most common source of errors elsewhere. Supports sidereal/Lahiri via extended chart selection. |
| **Astro-Seek** | Czech free service | Free | Fast; huge range of calculators (sidereal, Vedic charts, returns, transits, synastry, ephemeris tables). A good second check. |
| Others | e.g. Drik Panchang, AstroSage, Prokerala | Free (with ads) | Indian services that are good for panchanga, muhurta and quick Vedic checks. Interpretive text quality varies. |

---

## 5. Open-source libraries (for building your own tools)

| Library | Language | License | What it gives you | Notes |
|---|---|---|---|---|
| **pyswisseph** | Python (C binding) | AGPL (Swiss Ephemeris dual license applies) | Full Swiss Ephemeris API: `calc_ut`, `houses_ex`, `set_sid_mode`, eclipses, risings | **This repo's engine is built on it.** The best foundation for Vedic work in Python. |
| **Skyfield** | Python | MIT | High-precision astronomy from JPL kernels (DE421/DE440), with time scales handled correctly | It is a pure *astronomy* library with no houses, ayanamsas or astrological tables. Useful as an **independent cross-check** of positions, or for permissively licensed code. |
| **Kerykeion** | Python | AGPL | Western natal, synastry and transit data; SVG chart drawing; sidereal modes | Built on pyswisseph. Good for chart images and JSON output. |
| **flatlib** | Python | MIT | Traditional/Hellenistic astrology: dignities, almutens, Arabic parts, primary directions, profections | Built on pyswisseph. Small and readable, but maintained only lightly. |
| **VedAstro** | C# core with Python package and web API | Python package MIT (check the other repositories individually) | Vedic charts, dashas, yogas, an online API, ML-friendly datasets | Non-profit open-source project with an active community. |
| **PyJHora** | Python | check the repository's LICENSE | Python implementation of most features in PVR Narasimha Rao's book *Vedic Astrology: An Integrated Approach* and the JHora feature set: many dashas, vargas, special lagnas, Ashtakavarga, yogas, Tajika | The closest open-source equivalent to JHora. Useful for checking our engine's dasha and Jaimini outputs. |
| Others | — | — | Swiss Ephemeris ports for JavaScript (`swisseph` on npm, WASM builds) and Rust; **jyotishyamitra** and **vedicastro** (built on flatlib) on PyPI | Quality varies. Always validate against a reference chart. |

---

## 6. Comparison at a glance

| Need | Best choice | Runner-up |
|---|---|---|
| Learning Vedic astrology, readable screens and texts | **Parashara's Light** | Shri Jyoti Star |
| Maximum Vedic technique depth, free | **Jagannatha Hora** | PyJHora (code) / Maitreya |
| Rigorous classical calculation and muhurta | **Kala** | JHora |
| KP system | KP-specific Indian software (e.g. KP modules in LeoStar or PL) | JHora (KP settings) |
| Western professional work | **Solar Fire** | Sirius / Kepler |
| Horary and Hellenistic | **Janus** | Morinus (free) |
| Mac or Linux user | Maitreya, Morinus, Astro Gold | JHora under Wine |
| Quick free check of any chart | **Astro.com** | Astro-Seek |
| Building software / research | **pyswisseph** | Skyfield (cross-check), PyJHora (Vedic logic reference) |

**On accuracy.** Every option above that uses the Swiss Ephemeris (all of them except Skyfield, which uses JPL directly) gives effectively identical positions, to within arc-seconds. Accuracy differences come from:
1. **Atlas and time-zone data**, especially pre-1970 India (IST was standardised in 1947; Bombay Time was used locally before 1955) and wartime DST.
2. **Default settings**: ayanamsa, node, house system and dasha year.
3. **Algorithm choices** for derived values: arudha exceptions, karaka scheme, Shadbala sub-components, Gulika's definition.

---

## 7. Recommendation

**For this project and this user:**

1. **Keep Parashara's Light 9.0 as the day-to-day reading tool.** It is accurate (Swiss Ephemeris-class), and its screens map cleanly onto the classical texts. [03-reading-parasharas-light.md](03-reading-parasharas-light.md) already decodes its panels for the reference chart.
2. **Install Jagannatha Hora (free) as the second opinion.** Use it for advanced dashas (Kalachakra, Narayana, Chara), custom vargas, and to confirm PL settings when numbers disagree. On Mac or Linux, run it under Wine or CrossOver.
3. **Use Astro.com as the atlas and time-zone authority** whenever a birth time or place is uncertain.
4. **Build research and automation on this repo's pyswisseph engine.**
   - Verify it continually against PL and JHora using the reference chart: positions, padas, the dasha start of ~1 Oct 2021, SAV total 337 with Scorpio = 38, and so on.
   - Use Skyfield as an independent astronomy cross-check.
   - Use PyJHora as a reference implementation for Vedic algorithms.
   - Respect the **AGPL**: if the engine is ever offered as a public web service, publish its source under the AGPL or buy the Swiss Ephemeris professional license.
5. Add **Solar Fire or Janus** only if Western or Hellenistic work becomes a goal; neither is needed for Jyotish.

**Bottom line.** There is no "most accurate" astrology program, because precision is a solved problem shared by all of them through the Swiss Ephemeris. Choose by **tradition and technique coverage**: PL for guided Parashari reading, JHora for depth, and pyswisseph for building.
