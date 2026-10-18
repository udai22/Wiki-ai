# Reading Parashara's Light: A Field Guide to the Screen

> **Purpose.** This guide explains what every panel and column on the Parashara's Light 9.0 (PL) main screen means, using the reference chart as a worked example.
>
> **Reference chart.** 22 Jun 1999, 21:35 IST (16:05 UT), Mumbai (19°05′ N, 72°53′ E), Lahiri ayanamsa, true node.
>
> **How to read the interpretations.** Notes are *descriptive and traditional*: they say what the classical texts associate with a placement, not what will happen. See the scientific note in [01-how-astrology-works.md §6](01-how-astrology-works.md#6-a-note-on-scientific-status). Technique background is in [02-vedic-jyotish.md](02-vedic-jyotish.md).
>
> **How the values were checked.** The derived values below (padas, dignities, avasthas, D3/D9, arudhas, Ashtakavarga, dashas) were recomputed independently with pyswisseph using BPHS rules, and they agree with the screen data provided. If a number on *your* screen differs, the usual cause is a PL setting: node type, 7- or 8-karaka scheme, arudha exception rule, or year length for dashas. See §12.

---

## 0. The chart at a glance

Houses are whole-sign from the Capricorn Lagna, which is the default in PL's Rashi chart.

| House | Sign | Occupants | House lord → placed in |
|---|---|---|---|
| 1 | Capricorn | **Lagna 11°29′**, Ketu | Saturn → 4th |
| 2 | Aquarius | — | Saturn → 4th |
| 3 | Pisces | — | Jupiter → 4th |
| 4 | Aries | Jupiter, Saturn | Mars → 10th |
| 5 | Taurus | — | Venus → 7th |
| 6 | Gemini | Sun | Mercury → 7th |
| 7 | Cancer | Mercury, Venus, Rahu | Moon → 9th |
| 8 | Leo | — | Sun → 6th |
| 9 | Virgo | Moon | Mercury → 7th |
| 10 | Libra | Mars | Venus → 7th |
| 11 | Scorpio | — | Mars → 10th |
| 12 | Sagittarius | (Gulika/Mandi, see §9) | Jupiter → 4th |

PL draws this as a North Indian diamond, with houses fixed and sign numbers written inside, or as a South Indian square, with signs fixed. You switch between them in the chart style options. In the North Indian style the number "10" in the top diamond means Capricorn rises.

**Parashari aspects in this chart:**
- Saturn (4th) aspects the 6th (Sun), the 10th (Mars) and the 1st (Lagna).
- Jupiter (4th) aspects the 8th, the 10th (Mars) and the 12th.
- Mars (10th) aspects the 1st, the 4th (Jupiter and Saturn) and the 5th.
- All planets aspect the 7th from themselves. This makes Mars and Saturn–Jupiter a mutual 4–10 axis, and the Moon (9th) and Mercury–Venus–Rahu (7th) do not aspect each other.

---

## 1. Planet table: longitude, nakshatra, pada and sound

| Body | Sign & degree | Nakshatra (lord) | Pada | Sound | D9 sign |
|---|---|---|---|---|---|
| Lagna | Cp 11°29′ | Shravana (Moon) | 1 | **Khi** | Aries |
| Sun | Ge 6°57′ | Ardra (Rahu) | 1 | **Ku ("Koo")** | Sagittarius |
| Moon | Vi 28°32′ | Chitra (Mars) | 2 | Po | **Virgo (vargottama)** |
| Mars | Li 2°41′ | Chitra (Mars) | 3 | Ra | **Libra (vargottama)** |
| Mercury | Cn 1°28′ | Punarvasu (Jupiter) | 4 | Hi | **Cancer (vargottama)** |
| Jupiter | Ar 5°12′ | Ashwini (Ketu) | 2 | Che | Taurus |
| Venus | Cn 21°49′ | Ashlesha (Mercury) | 2 | Du | Capricorn |
| Saturn | Ar 19°34′ | Bharani (Venus) | 2 | Lu | Virgo |
| Rahu | Cn 20°05′ | Ashlesha (Mercury) | 2 | Du | Capricorn |
| Ketu | Cp 20°05′ | Shravana (Moon) | 4 | Kho | Cancer |

**How to read the columns**

- **Degree.** The degree is measured *within the sign*, 0°–29°59′.
- **Nakshatra and pada.** The nakshatra is the 13°20′ lunar mansion and the pada is its 3°20′ quarter.
  - *Example:* the Sun at Gemini 6°57′ has just entered Ardra (which begins at 6°40′) and is in its 1st pada (6°40′–10°00′).
- **Sound (*akshara*).** Each of the 108 padas has a traditional syllable used for name-giving (*namakarana*). PL lists it for every body. The syllables shown, "Khi, Koo…", are simply the Lagna and the Sun in table order.
  - By custom the **Moon's pada syllable (Po)** is the one recommended for a first name.
  - Spellings vary across texts: Shravana is "Khi/Ju", and "Ku" may be printed "Koo".
- **Nakshatra lord.** The nakshatra's Vimshottari lord. Some practitioners read a planet "through" the lord of the nakshatra it occupies.
  - *Example:* the Sun in Ardra is coloured by Rahu.
  - If your PL view shows a *sub-lord* column, that is the KP-style subdivision.
- **Vargottama.** The Moon, Mars and Mercury fall in the same sign in D1 and D9. Tradition reads this as added steadiness and strength for those planets. PL's Navamsha chart (D9) panel shows it directly.
- **Rahu/Ketu 20°05′.** This is the *true* node. The *mean* node would be Cancer/Capricorn 21°24′. PL lets you choose the node type in its preferences.
- **Retrograde and combustion.** None of the planets is retrograde at this birth. Mercury is about 24½° from the Sun, so it is not combust. PL would mark these with "R" and "C".

---

## 2. Dignity column: "Frnd", "Grt.Fr", "Neutr", "Debil."

PL prints each planet's **compound (panchadha) relationship** to the lord of the sign it occupies (see [02 §1](02-vedic-jyotish.md#1-grahas-planets)). The special statuses take precedence: Exalted, Moolatrikona, Own sign, Debilitated.

| Planet | Sign lord | Natural view | Temporary (by position) | **Compound = screen label** |
|---|---|---|---|---|
| Sun | Mercury | neutral | Mercury 2nd from Sun → friend | **Frnd** |
| Moon | Mercury | friend | Mercury 11th from Moon → friend | **Grt.Fr** |
| Mars | Venus | neutral | Venus 10th from Mars → friend | **Frnd** |
| Mercury | Moon | enemy | Moon 3rd from Mercury → friend | **Neutr** |
| Jupiter | Mars | friend | Mars 7th from Jupiter → enemy | **Neutr** |
| Venus | Moon | enemy | Moon 3rd from Venus → friend | **Neutr** |
| Saturn | Mars | — | — | **Debil.** |

**What "Debil." means for Saturn.** Saturn's debilitation sign is Aries, and its deepest point (*parama nicha*) is **Aries 20°**. Saturn sits at 19°34′, within half a degree of that point, which is as deep as debilitation gets. Classical texts associate a debilitated planet with weakness in its natural significations (for Saturn: discipline, endurance, longevity, service, elders).

Saturn is also this chart's **Lagna lord** (Capricorn) and 2nd lord. Tradition does not stop at "debilitated = bad", however. It checks for **neecha-bhanga** (cancellation of debilitation). Two classical conditions (*Phaladeepika* ch. 7) are met here:
1. Mars, lord of the debilitation sign Aries, is in a kendra (the 10th) from the Lagna.
2. Venus, lord of Saturn's exaltation sign Libra, is in a kendra (the 7th) from the Lagna.

Many authors read neecha-bhanga as a planet that struggles early and then rises. Saturn is also joined by Jupiter and aspected by Mars, so it has to be weighed in context.

---

## 3. Chara karakas: AK, AmK, MK …

PL ranks planets by **degree within their sign**, Jaimini-style:

| Rank | Planet (deg in sign) | Karaka | Traditional meaning |
|---|---|---|---|
| 1 | Moon 28°32′ | **AK**, Atmakaraka | "king" of the chart; the soul's central desire or lesson |
| 2 | Venus 21°49′ | **AmK**, Amatyakaraka | "minister": career, the means of achieving |
| 3 | Saturn 19°34′ | **BK**, Bhratrikaraka | siblings, co-workers, (in some schools) the guru |
| 4 | Sun 6°57′ | **MK**, Matrikaraka | mother, home, education |
| 5 | Jupiter 5°12′ | **PK / PiK** (see note) | children, creativity (Putra) |
| 6 | Mars 2°41′ | **GK**, Gnatikaraka | rivals, obstacles, disease |
| 7 | Mercury 1°28′ | **DK**, Darakaraka | spouse, partners |

**Note on "PiK".** In the **7-karaka scheme**, the one these rankings follow, the 5th karaka is the **Putrakaraka**. Some PL versions abbreviate it in a way that looks like "PiK". In the **8-karaka scheme**, which includes Rahu (counted as 30° − 20°05′ = 9°55′), Rahu would rank 4th. That would give MK Rahu, *Pitrikaraka* (PiK) Sun and PK Jupiter. Your screen's "Sun MK" shows it is set to 7 karakas.

**For this chart, according to tradition:**
- **AK Moon.** The Moon is in the 9th house (dharma, teachers, fortune), vargottama in Virgo, so the **Karakamsha is Virgo**, the AK's navamsha sign. Jaimini texts read the Moon as AK as a soul oriented to feeling, care and the public.
- **AmK Venus.** Venus is also this chart's **yogakaraka**: for Capricorn it owns the 5th (trikona) and the 10th (kendra). As AmK in the 7th, it points tradition towards partnerships, the arts, or client-facing work for career themes.
- **DK Mercury** in the 7th (the house of spouse) with Venus is a repeated "relationship" signature, which tradition counts as emphasis.

---

## 4. Vimshottari dasha panel: what "Ju 1 Oct 2021" means

Each line in the dasha panel is **planet + start date**. "Ju 1 Oct 2021" means the **Jupiter mahadasha begins on about 1 October 2021**. It lasts 16 years, until about October 2037, when the Saturn mahadasha (19 years) begins.

**How PL got there:**
1. The Moon (Virgo 28°32′) is in Chitra, which is ruled by Mars. The Moon has traversed 5°12′ of the nakshatra's 13°20′, which is 39%.
2. That leaves 61% of Mars's 7 years as the balance at birth: about 4 years 3 months, so the Mars dasha ends about late September 2003.
3. Rahu's 18 years follow, from 2003 to 2021, then Jupiter from 2021 to 2037.
4. Why PL says **1 Oct**, not 27 Sep: PL measures the Moon's progress through Chitra by **time** (the fraction of the ~24 hours the Moon spends in the nakshatra, 38.9%) rather than by **arc** (39.0%). It also uses a **365.2422-day year**. This project's engine reproduces PL's dates to within ~10 minutes with these settings (`astro/dasha.py`, `method="time"`). The textbook arc method gives 27 Sep 2021.

**Drilling down.** Clicking a mahadasha opens its **antardashas** (bhuktis):

| Antardasha in Jupiter MD | Starts (approx.) |
|---|---|
| Ju–Ju | Sep/Oct 2021 |
| Ju–Sa | Nov 2023 |
| **Ju–Me** (running as of Oct 2026) | **late May / Jun 2026** |
| Ju–Ke | Sep 2028 |
| Ju–Ve | Aug 2029 |
| Ju–Su | Apr 2032 |
| Ju–Mo | Jan 2033 |
| Ju–Ma | May 2034 |
| Ju–Ra | May 2035 |

**Traditional reading of the period lords.** The texts judge a dasha by what its lord owns, occupies, aspects and signifies.

- **Jupiter:**
  - owns the 3rd (effort, communication) and the 12th (expenses, foreign lands, retreat)
  - sits in the 4th (home, mother, education) with debilitated Saturn
  - aspects the 8th, the 10th (career) and the 12th
  - is the natural karaka of teachers, learning and children
- **Mercury** (the current antardasha):
  - owns the 6th and the 9th
  - sits in the 7th with Venus and Rahu, in vargottama
- *Sarvartha Chintamani* and BPHS give planet-by-planet antardasha results that astrologers then adjust for these placements.

---

## 5. D3 Drekkana panel

**The rule.** Each sign is split into three 10° parts. The 1st part maps to the same sign, the 2nd to the 5th sign from it, and the 3rd to the 9th sign from it (BPHS ch. 6).

**Use.** It is used for siblings, courage and initiative (the 3rd-house theme). Classically it is also used for illness and the nature of death through "drekkana faces".

| Body | D1 | Part | **D3 sign** |
|---|---|---|---|
| Lagna | Cp 11°29′ | 2nd (10–20°) | Taurus |
| Sun | Ge 6°57′ | 1st | Gemini |
| Moon | Vi 28°32′ | 3rd | Taurus |
| Mars | Li 2°41′ | 1st | Libra |
| Mercury | Cn 1°28′ | 1st | Cancer |
| Jupiter | Ar 5°12′ | 1st | Aries |
| Venus | Cn 21°49′ | 3rd | Pisces (exalted in D3) |
| Saturn | Ar 19°34′ | 2nd | Leo |
| Rahu / Ketu | Cn/Cp 20°05′ | 3rd | Pisces / Virgo |

The D3 Lagna is Taurus, and the Moon falls in the D3 Lagna sign. Read any varga as its own chart (Lagna, houses, lords) for its single topic, not as a replacement for the D1.

---

## 6. Samudaya (Sarva) Ashtakavarga panel

**What the numbers are.** "Samudaya" means "aggregate". The panel is the **Sarvashtakavarga (SAV)**: for each sign, the total benefic points (*bindus*) contributed by all 7 planets' individual tables. The total is **always 337**, so the average is about **28 per sign**.

| House | Sign | SAV | Reading by the usual rule of thumb |
|---|---|---|---|
| 1 | Capricorn | 27 | about average |
| 2 | Aquarius | 32 | strong |
| 3 | Pisces | 29 | above average |
| 4 | Aries | 31 | strong |
| 5 | Taurus | 26 | slightly weak |
| 6 | Gemini | 27 | about average |
| 7 | Cancer | 28 | average |
| 8 | Leo | 24 | weak (low 8th points are traditionally fine) |
| 9 | Virgo | 24 | weak |
| 10 | Libra | 25 | slightly weak |
| **11** | **Scorpio** | **38** | **very strong**, the highest in the chart |
| 12 | Sagittarius | 26 | slightly weak |
| | **Total** | **337** | ✔ checksum |

**Traditional uses**
1. **House strength.** Signs with more than 28 bindus are said to deliver their house matters more easily. Here the 11th (gains, networks, elder siblings) stands out at 38. The 2nd (wealth, speech) and the 4th (home) are also strong.
2. **Income versus expense.** The 11th (38) exceeds the 12th (26). The popular rule reads this as income outpacing expenditure.
3. **Transit quality.** Slow planets transiting high-SAV signs are said to give better results. When Saturn transits Scorpio (38), tradition expects less hardship than usual for Saturn, and when it transits Leo or Virgo (24), more.

The panel's per-planet tables (**Bhinnashtakavarga**, BAV) show how each planet's points are distributed. Their totals are fixed: Sun 48, Moon 49, Mars 39, Mercury 54, Jupiter 56, Venus 52, Saturn 39. For this chart, for example, **Saturn's BAV is 5 in Pisces** and **Jupiter's BAV is 6 in Cancer**. These numbers drive the kaksha analysis below.

---

## 7. Gochara kakshas panel

**What a kaksha is.** Each sign is divided into **8 kakshas of 3°45′**. Their lords always come in the same order: **Saturn, Jupiter, Mars, Sun, Venus, Mercury, Moon, Lagna** (0°–3°45′ is Saturn's, 3°45′–7°30′ Jupiter's, …, 26°15′–30° the Lagna's).

**The traditional rule.** A transiting planet gives favourable results while it passes through a kaksha whose lord gave it a bindu in that sign (according to the planet's own BAV). It gives weaker results through a kaksha whose lord did not.

**Worked example, 18 Oct 2026** (sidereal positions computed for that date):

| Transit | Position | Kaksha lord | Bindu in that planet's BAV? | Reading by rule |
|---|---|---|---|---|
| Saturn (R) | Pisces 16°00′ (3rd from Lagna, 7th from Moon) | Venus (15°00′–18°45′) | **No.** Saturn's Pisces bindus come from Sun, Mars, Mercury, Jupiter and Lagna. | weaker stretch, though Saturn's sign total (5) is good |
| Jupiter | Cancer 28°12′ (exalted; 7th from Lagna) | Lagna (26°15′–30°) | **Yes** | supportive stretch |
| Mars | Cancer 17°10′ | Venus | **No** | weaker |
| Sun | Libra 0°38′ | Saturn | Yes | supportive |
| Mercury | Libra 24°40′ | Moon | Yes | supportive |
| Venus (R) | Libra 9°58′ | Mars | **No** | weaker |

PL's Gochara/kaksha panel shows exactly this: each transiting planet, its current kaksha lord, and whether a bindu is present (often as 1/0 or a highlight). The kaksha changes every few days for fast planets and every few months for Saturn.

---

## 8. Arudha Lagna and Bhava Arudhas (2P … 12P)

**The rule** (Jaimini Sutras 1.3; BPHS ch. 29):
1. Count from the house to its lord.
2. Count the same number again from the lord.
3. If the result lands in the house itself or the 7th from it, take the 10th from there instead.

| Pada | House sign | Lord & position | Raw result | **Arudha (with exception)** |
|---|---|---|---|---|
| **AL** (1P) | Capricorn | Saturn in Aries (4 signs on) | Cancer = 7th from house → exception | **Aries** (raw: Cancer) |
| 2P | Aquarius | Saturn in Aries | Gemini | Gemini |
| 3P | Pisces | Jupiter in Aries | Taurus | Taurus |
| 4P | Aries | Mars in Libra | Aries = same sign → exception | Capricorn |
| 5P | Taurus | Venus in Cancer | Virgo | Virgo |
| 6P | Gemini | Mercury in Cancer | Leo | Leo |
| 7P (**A7**, Darapada) | Cancer | Moon in Virgo | Scorpio | Scorpio |
| 8P | Leo | Sun in Gemini | Aries | Aries |
| 9P | Virgo | Mercury in Cancer | Taurus | Taurus |
| 10P | Libra | Venus in Cancer | Aries = 7th → exception | Capricorn |
| 11P | Scorpio | Mars in Libra (Ketu co-lord) | Virgo | Virgo |
| 12P (**UL**, Upapada) | Sagittarius | Jupiter in Aries | Leo | Leo |

**Meaning in tradition.** The arudha is the *image* or *manifestation* of a house: how it appears to the world.
- **AL** shows the public persona and status.
- **A7** shows business partners and the image of relationships.
- **UL** shows marriage.
- **A10** shows visible career standing.

**Example.** If your PL is set to apply the exception, AL Aries holds Jupiter and Saturn. Jaimini authors read the 11th from AL (Aquarius) for gains and the 12th from AL (Pisces) for losses or expenses.

Your screen shows **AL in Aries** with 4P and 10P in Capricorn, so PL is applying the exception (the engine matches all 12 arudhas exactly). With the raw count and no exception, AL would be Cancer and 4P Aries.

For Scorpio and Aquarius, with the dual lords (Mars/Ketu, Saturn/Rahu), PL uses the stronger lord according to a rule set in preferences.

---

## 9. Gulika / Mandi

**What they are.** Gulika and Mandi are *upagrahas* (shadow points) associated with Saturn.

**How they are computed.**
- Daytime (sunrise to sunset) and night-time are each divided into **8 parts**, ruled in a fixed weekday sequence.
- By night the sequence begins with the lord of the 5th weekday from the birth weekday.
- Authorities differ on how to compute them. PL (verified by this repo's engine, `astro/special.py`) takes **Gulika = the Lagna at the *end* of Saturn's part** and **Mandi = Phaladeepika's rule** (a fixed number of ghatis after sunset by weekday, scaled to the night's length). It uses Hindu sunset (disc centre, no refraction).

**Reference chart.**
- The birth was on a **Tuesday night**. Hindu sunset in Mumbai was 19:14:54 IST, and birth was at 21:35.
- On Tuesday night the *first* part (19:14:54–20:36:21) belongs to Saturn.
- **Gulika = Sagittarius 26°18′** (the Lagna at 20:36:21) and **Mandi = Sagittarius 17°02′**. Both match PL to the arcminute, and both fall in the **12th house**.

**Meaning in tradition** (*Phaladeepika* ch. 25; BPHS ch. 3): Gulika is a malefic sensitive point. Its house is said to be afflicted, and its sign lord and transits over it are watched. Some also use it in birth-time rectification.

---

## 10. Shadbala ratios (1.51, 1.36 …)

**What the ratio is.** The ratio is **actual Shadbala ÷ required minimum** (BPHS ch. 27).
- The minimums in rupas are: Sun 6.5, Moon 6, Mars 5, Mercury 7, Jupiter 6.5, Venus 5.5, Saturn 5.
- **Above 1.00:** the planet has enough strength to deliver its significations. A ratio of 1.51 means 151% of its quota.
- **Below 1.00:** the planet is deficient.

**Ranking.** PL ranks the planets by this ratio. Its Shadbala screen also shows the six components (Sthana, Dig, Kala, Cheshta, Naisargika, Drik) in virupas.

**What to expect for this chart.**
- Saturn, being deeply debilitated, gets almost no *uccha bala*.
- Night birth boosts the Moon, Mars and Saturn in *nathonnata bala*.
- Jupiter in the 4th has only about half its dig bala: its directional strength peaks in the 1st and is zero in the 7th.
- Mars in the 10th has *full* dig bala.
- Read the actual numbers from the screen; they depend on many sub-factors.

**How it is used.** A strong ratio is said to let a planet give its results fully during its dasha. A weak one, even a well-placed planet, is said to "promise but not deliver".

---

## 11. Baladi avasthas: Infant / Youth / Old / Dead

**The rule.** These are age states by degree. In **odd** signs the order is: 0–6° infant (*Bala*), 6–12° adolescent (*Kumara*), 12–18° youth (*Yuva*), 18–24° old (*Vriddha*), 24–30° dead (*Mrita*). In **even** signs the order is reversed.

| Planet | Sign (odd/even) | Degree | Avastha | Traditional share of results |
|---|---|---|---|---|
| Sun | Gemini (odd) | 6°57′ | Kumara (adolescent; may be labelled "Youth" in PL) | about half |
| Moon | Virgo (even) | 28°32′ | Bala (infant) | about quarter |
| Mars | Libra (odd) | 2°41′ | Bala (infant) | about quarter |
| Mercury | Cancer (even) | 1°28′ | **Mrita (dead)** | minimal |
| Jupiter | Aries (odd) | 5°12′ | Bala (infant) | about quarter |
| Venus | Cancer (even) | 21°49′ | Kumara (adolescent / "Youth") | about half |
| Saturn | Aries (odd) | 19°34′ | Vriddha (old) | very little |

**How tradition weighs it.** Avasthas modify, but do not override, dignity and strength. Mercury "dead" by Baladi, for example, is also vargottama and has a neutral compound relationship. Astrologers weigh all of these together; no single column decides.

---

## 12. Settings that change what you see

| Setting | Options | Effect on this chart |
|---|---|---|
| Ayanamsa | Lahiri (default), Raman, KP, … | Raman would move every planet about 1°27′ forward. The Lagna would still be Capricorn, but padas, vargas and dasha dates would change. |
| Node | True / Mean | Rahu at 20°05′ vs 21°24′. This changes Rahu's pada, kaksha and karaka degree. |
| Chara karakas | 7 / 8 | 8 brings in Rahu as MK and makes the Sun PiK |
| Arudha exception | on / off | AL Aries vs Cancer; 4P and 10P change |
| Dasha year | 365.25 / 360 / sidereal | shifts dasha dates by days to weeks |
| House system | whole sign / Sripati (bhava chalit) | Bhava chalit can move a planet near a cusp into the neighbouring house |
| Chart style | North / South / East Indian | display only |

---

## 13. A suggested reading order for any PL chart

1. **Rashi (D1) + Lagna.** Identify the house lords and where they sit.
2. **Dignity + avastha + Shadbala.** Ask who is strong and who is weak.
3. **Navamsha (D9).** Look for confirmation and vargottama, then check the topic-specific vargas (D3, D10 …).
4. **Yogas.** PL has a yogas report.
5. **Karakas + arudhas.** This is the Jaimini layer: AK, Karakamsha, AL, UL.
6. **Dasha.** Find the running MD/AD lords and what they rule.
7. **Gochara + Ashtakavarga + kakshas.** These give the timing triggers.

This is the traditional "promise → timing → trigger" sequence described in [01 §4](01-how-astrology-works.md#4-the-logic-of-prediction-promise--timing--trigger).
