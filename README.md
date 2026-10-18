# Astrology & Cycles Project

A working Vedic astrology engine on the **Swiss Ephemeris**, plus a knowledge base covering how astrology works: Parashara and the Vedic masters, Dewey's cycle science, Chizhevsky's solar history, Paracelsus, Osho, and the wider tradition.

## What's here

| Path | What it is |
|---|---|
| `astro/` | Calculation engine (Python, `pyswisseph`) |
| `knowledge/` | The knowledge base. Start with `01-how-astrology-works.md` (the map). |
| `reports/reference-chart.md` | Full printout for the reference chart (22 Jun 1999, 21:35, Mumbai) |
| `tests/` | Engine checked value-by-value against Parashara's Light 9.0 |

## Engine features

- **Chart**: sidereal positions (Lahiri by default; also Raman, KP, Fagan-Bradley, Yukteshwar, True Chitra, tropical), whole-sign houses, nakshatra and pada, retrograde motion, outer planets
- **Dignity**: exaltation, debilitation, moolatrikona, own sign, and five-fold compound friendship (natural + temporal)
- **Baladi avasthas** (age states) and **Jaimini chara karakas** (AK…DK)
- **Arudha padas**: AL plus all 12 bhava arudhas
- **16 divisional charts** (D1–D60, Parashari rules)
- **Vimshottari dasha** to pratyantardasha, with both the time-based (Parashara's Light) and arc-based (textbook) birth balance
- **Ashtakavarga**: all seven bhinnashtakavargas plus the sarvashtakavarga
- **KP** star, sub and sub-sub lords
- **Gochara (transits)**: house from Moon and Lagna, bindus, kakshas, Sade Sati
- **Cycles** (`astro/cycles.py`):
  - Dewey's method: ratio-to-trend, periodogram, Bartels significance test, synthesis and projection
  - Chizhevsky's four solar-cycle phases
  - Jupiter–Saturn great conjunctions
  - Barbault's cyclic index
  - Reference tables of the Dewey cycles and planetary periods

## Accuracy vs Parashara's Light 9.0 (reference chart)

| Item | Result |
|---|---|
| Planets | within 1″ |
| Ascendant | within 4″ |
| Rahu/Ketu (true node) | within 22″ |
| Dasha dates | within 10 min |
| Sarvashtakavarga, arudhas, D3, KP lords, karakas, avasthas, dignities, transit kakshas | exact |

Two settings explain the remaining small gaps:

- PL uses the **true node**.
- PL computes the dasha birth balance from the **time** the Moon spends in its nakshatra, with a year of **365.2422 days**.

## Quick start

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m astro chart    --date 1999-06-22 --time 21:35 --tz 5.5 --place mumbai
.venv/bin/python -m astro dasha    --depth 3 --year 2026
.venv/bin/python -m astro transits --on "2025-01-05 15:28"
.venv/bin/python -m astro cycles
.venv/bin/python -m pytest -q
```

Use `--lat/--lon` for any place, `--ayanamsa krishnamurti` for KP, and `--node mean` for the mean node.

For full JPL precision, put Astrodienst's `.se1` files in `ephe/`. Without them the engine uses the built-in Moshier ephemeris (~1″ for planets).

## A note on evidence

The engine computes positions exactly. The meaning given to those positions is tradition. Controlled tests have not supported astrology's predictive claims. The knowledge base presents each school on its own terms and notes where the evidence stands.

Licensing: the Swiss Ephemeris is AGPL, or under a paid professional license from Astrodienst.
