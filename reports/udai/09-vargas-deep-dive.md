# 09 · Divisional charts (vargas): the deep dive

*Udai, 22 Jun 1999, 21:35 IST, Mumbai. Lahiri ayanamsa, true node, BPHS division rules, Parashari (unequal) trimsamsa. Every number below was computed with this repo's `astro/` engine. Scratch scripts are in `/tmp/udai/`.*

This chapter goes past [01-parashari §1.5](01-parashari.md). That section gave the D9 and D10 lagna tables and the Libra cluster in outline. Here every varga is read planet by planet, and every time-sensitive lagna is given with the clock window in which it holds.

**Tags.**
- **[Robust]** holds for any birth time from 20:51 to 22:41 (−43.5 to +66 min) and under small ayanamsa changes.
- **[Moderate]** depends on convention: ayanamsa, true vs mean node, or which list a text uses.
- **[Time-sensitive]** changes within minutes of the recorded time.

**The ground rule.** A planet's varga sign moves with the planet, so the slow planets' signs are fixed in every varga. Only the **varga lagnas** move with the clock. Section 0 lists the few planetary exceptions.

---

## 0. Which planetary varga positions are fragile

Each planet was swept across ±60 minutes and tested against a few arcminutes of ayanamsa error.

| Point | Fragile in | Why | Tag |
|---|---|---|---|
| **Moon** | D20, D40, D60 | The Moon reaches 28°30′ Virgo at **21:30:15**. Before that moment its D20 is Aquarius (Pisces after), its D40 Scorpio (Sagittarius after), and its D60 Taurus (Gemini after). It also leaves its D45 at +15.5 min and its D24 at +25.5 min. | Time-sensitive |
| **Mercury** | D20, D40, D60 | All three change at +34 min, and Mercury sits 1.8′ from its D60 boundary. | Moderate |
| **Sun** | D60 | 2.4′ from the next shashtiamsa. The KP ayanamsa, 5.8′ smaller than Lahiri, would move it. | Moderate |
| **Saturn** | D20, D40, D60 | 4.5′ inside its current part. | Moderate |
| **Rahu/Ketu** | D3, D9, D12, D24, D27, D30, D45, D60 | The true node is 20°05′ Cancer, 5′ past a 20° boundary. The **mean node is 21°24′ Cancer**. With the mean node the D9 is unchanged (still Capricorn), but **Rahu's D10 moves to Libra, joining the cluster**, its D24 becomes Sagittarius and its D60 Capricorn. | Moderate |
| Everything else | — | At least 10′ from any boundary in every varga, and unchanged over ±60 min. | Robust |

---

## 1. D9 Navamsa in depth

BPHS ch. 6 assigns the navamsa to the spouse (*kalatra*). In practice, from Parashara through Sanjay Rath and P.V.R. Narasimha Rao (*Vedic Astrology: An Integrated Approach*), the D9 is also read as **the chart of a planet's inner strength and its fruit**. A planet's navamsa shows what its rasi promise ripens into. Rath's shorthand is that the rasi is the tree and the navamsa is the fruit.

### 1.1 Planet by planet [Robust]

Karakamsa (KK) = Virgo, the navamsa of the Atmakaraka (AK) Moon. Dignities are compound, with temporal relations taken from D1.

| Planet | D9 sign and degree | Dignity in D9 | From KK | Reading |
|---|---|---|---|---|
| Sun | Sagittarius 2°38′ | great friend (Jupiter) | 4th | The 8th lord ripens in a dharma sign. Authority comes through teaching, law or principle more than display. |
| Moon (AK) | **Virgo 16°51′, vargottama** | great friend | KK | The soul planet is the same in body and fruit. The Virgo/Chitra craftsman motif is the deepest layer of the chart. |
| Mars | **Libra 24°14′, vargottama** | friend | 2nd | The 10th-house dig-bala Mars carries its strength into the fruit. It speaks and earns through technical skill (2nd from KK). |
| Mercury (DK) | **Cancer 13°13′, vargottama, pushkara navamsa** | neutral | 11th | The 6th and 9th lord is protected twice, by vargottama and by pushkara (§1.3). |
| Jupiter | Taurus 16°54′ | neutral (Venus's sign) | 9th | Guru and dharma devata, from the 9th of the KK. See §1.4. |
| Venus (AmK) | Capricorn 16°21′ | great friend (Saturn) | 5th | The yogakaraka ripens in Saturn's sign. See §1.4. |
| Saturn | Virgo 26°10′ | great friend (Mercury) | **in the KK** | The debilitated lagna lord is comfortable in D9 and sits with the AK. See §1.4. |
| Rahu | Capricorn 0°47′ | — | 5th | The Venus–Rahu pairing repeats in D9. |
| Ketu | Cancer 0°47′ | — | 11th | With Mercury. |

### 1.2 Vargottama: Moon, Mars, Mercury [Robust]

All three hold the first navamsa of a movable sign (Mars in Libra, Mercury in Cancer) or the last navamsa of a dual sign (Moon in Virgo). Varahamihira (*Brihat Jataka* ch. 1) and *Saravali* treat vargottama as strength comparable to own sign.

- **Moon–Mercury exchange in both D1 and D9.** The Moon is in Mercury's sign and Mercury in the Moon's sign, and since both are vargottama the exchange repeats in D9. Rath and PVR treat a varga repetition of a yoga as confirmation, and an AK–DK exchange in both charts as an especially binding link between self and partner/business ([02-jaimini](02-jaimini.md)).
- **Mars vargottama in the 10th** strengthens the dig-bala reading of [01](01-parashari.md): the visible technical drive is also the inner one.

### 1.3 Pushkara navamsa and pushkara bhaga [Robust for planets, Time-sensitive for lagna]

These are **not in BPHS**. They come from later muhurta and jataka tradition and are used in modern practice by PVR Narasimha Rao and others. Pushkara navamsas are the two benefic-ruled navamsas in each element:

- fire signs: 7th and 9th navamsas
- earth: 3rd and 5th
- air: 6th and 8th
- water: 1st and 3rd

Pushkara bhagas are single "nourishing" degrees. The common list is Ar 21, Ta 14, Ge 18, Cn 8, Le 19, Vi 9, Li 24, Sc 11, Sg 23, Cp 14, Aq 19, Pi 9. Some lists differ by a degree, and authors disagree on whether "21" means 20°–21° or the point 21°00′.

| Point | Navamsa no. | Pushkara navamsa? | Distance from pushkara bhaga |
|---|---|---|---|
| Lagna | 4th of Capricorn (Aries) | **No** at 21:35 | −2°31′ (Cp 14°) |
| Sun | 3rd of Gemini | No | −11° |
| Moon | 9th of Virgo | No | +19.5° |
| Mars | 1st of Libra | No | −21° |
| **Mercury** | **1st of Cancer** | **Yes** (Cancer navamsa) | −6.5° |
| Jupiter | 2nd of Aries | No | −15.8° |
| Venus | 7th of Cancer | No | +13.8° |
| **Saturn** | 6th of Aries | **No, but 26′ short** of the 7th (Libra) pushkara navamsa | **−1°26′** from Ar 21° |
| Rahu / Ketu | 7th | No | — |

- **Mercury is the only pushkara-navamsa planet.** Combined with vargottama, this makes Mercury, the 9th lord (fortune, dharma) and DK, much stronger than its "neutral, dead-avastha" D1 label suggests [Robust].
- **Saturn misses both pushkara markers by less than 1.5°.** This is a near-miss, not a hit. Read neutrally, it adds to the chart's recurring "almost there, earned later" Saturn motif. Do not count it as support [Robust].
- **The lagna is in a pushkara navamsa in both neighbouring windows.**
  - The Pisces navamsa (lagna 6°40′–10° Capricorn, **21:17–21:29:30**) is a pushkara navamsa.
  - So is the Taurus navamsa (13°20′–16°40′, **21:42–21:54**).
  - The lagna reaches the Capricorn pushkara bhaga at 14°00′ at about **21:44:15**.
  - The recorded Aries navamsa is the only one of the three that is not pushkara. This does not argue for any window by itself. It is one more factor to weigh during rectification [Time-sensitive].

### 1.4 The five named placements [Robust]

**Venus in Capricorn D9.**
- The yogakaraka and AmK ripens in the sign of Saturn, its great friend.
- Venus is **5th from the AK**: an AK–AmK trine, which SJC counts as a working career–soul link.
- The D9 dispositor of Venus is Saturn, debilitated in D1. Classically this routes Venus's fruit through Saturn's maturation, so the career engine runs best when it accepts structure, patience and hierarchy.
- In D9, Venus is 15°34′ from Rahu, against 1°44′ in D1. The pair is less fused in the fruit than in the body, so Rahu's colouring is real but no longer eclipsing.

**Saturn in Virgo D9.**
- It is not exalted, so the "debilitated in rasi, exalted in navamsa" neecha-bhanga rule found in later texts does **not** apply.
- What does apply:
  - Saturn is in a great friend's sign.
  - It sits with the AK in the karakamsa.
  - Its navamsa lord, Mercury, is vargottama and pushkara.
- Jaimini's sutra for Saturn in the KK gives *prasiddha-karmājīva*, fame through persistent work (see 02).
- Parashari and Jaimini agree: the D1 weakness of the lagna lord is a seed in good soil.

**Jupiter in Taurus D9.**
- Jupiter is in Venus's sign, a natural enemy, which the compound relation turns neutral. That is a middling dignity for the 3rd and 12th lord.
- What raises Jupiter in D9 is its aspects.
  - At 16°54′ Taurus it casts a **near-exact 5th aspect on the Moon** (16°51′ Virgo, 3′ apart) and a 9th aspect on Venus (16°21′ Capricorn).
  - So Jupiter, the Moon/Saturn and Venus/Rahu form an **earth trine in D9** (Taurus–Virgo–Capricorn).
- Rath uses graha drishti inside D9. Strict Jaimini counts only rashi drishti, but Taurus also aspects Capricorn and Cancer by sign, so Jupiter reaches Venus and Mercury either way [Robust].
- Degree closeness inside a varga is a refinement some modern readers use and others ignore [Moderate].

**Sun in Sagittarius D9.**
- In a great friend's sign, 4th from the KK, and it aspects the KK by rashi drishti (02 uses this for the ishta devata).
- The 8th lord ripens into a principled, teacherly expression. The 8th's research and hidden-knowledge themes ripen in a Jupiter sign.

**Rahu in Capricorn D9.**
- With Venus, in Saturn's sign, 5th from the KK.
- The karakamsa sutras link Rahu in the 5th from swamsa to instruments and machines (*yantra*), and to unorthodox learning.
- This placement holds under both the true and the mean node [Robust].

### 1.5 The D9 dispositor chain [Robust]

- Sun → Jupiter → Venus → Saturn → Mercury ⇄ Moon
- Mars → Venus → … ; Rahu → Saturn → … ; Ketu → Moon

Every chain ends in the **Moon–Mercury mutual reception**. There is no single final dispositor. The D1 chains end in the same loop (Sun → Mercury ⇄ Moon; Mars → Venus → Moon; Jupiter and Saturn → Mars → …).

The same terminal loop in body and fruit is a strong, uncommon signature. The life keeps coming back to Virgo/Cancer themes: mind, analysis, craft, care. Saturn is the second-to-last link in D9, so most of the chart's energy passes through Saturn before it reaches the Mercury–Moon loop.

### 1.6 The three D9 lagna scenarios [Time-sensitive]

| | **Pisces** (21:17 – 21:29:30) | **Aries** (21:29:30 – 21:42, recorded) | **Taurus** (21:42 – 21:54) |
|---|---|---|---|
| Houses occupied | 3 Ju · 5 Me Ke · 7 Mo Sa · 8 Ma · 10 Su · 11 Ve Ra | 2 Ju · 4 Me Ke · 6 Mo Sa · 7 Ma · 9 Su · 10 Ve Ra | 1 Ju · 3 Me Ke · 5 Mo Sa · 6 Ma · 8 Su · 9 Ve Ra |
| Lagna lord | Jupiter in the 3rd | Mars in the 7th, vargottama, aspecting the lagna | Venus in the 9th |
| 7th house / 7th lord | Virgo (Moon AK + Saturn) / Mercury in the 5th | Libra (Mars) / **Venus in the 10th** with Rahu | Scorpio, empty / Mars in the 6th |
| 9th and 10th lords | Mars in the 8th; Jupiter in the 3rd | Jupiter in the 2nd; Saturn in the 6th | Saturn rules both (yogakaraka) and sits in the 5th |
| Sun | 10th, with dig bala | 9th | 8th |
| KK from the D9 lagna | **7th**: the soul's work happens through the partner | **6th**: growth through service, competition, problem-solving | **5th**: mantra, students, creative intelligence |
| D9 Arudha (AL) | Cancer (Mercury, Ketu) | **Capricorn** (Venus, Rahu); this uses the exception rule, since the raw count lands on Aries itself | **Virgo**, i.e. the KK itself (Moon, Saturn) |
| D9 Upapada | Aries | Cancer (Mercury, Ketu) | Capricorn (Venus, Rahu) |
| Pushkara-navamsa lagna | yes | no | yes |
| D9 lagna from D1 lagna | 3rd | 4th | **5th, a trine** |

**Reading notes.**
- **Pisces.** The AK and Saturn in the D9 7th describe a partner who is serious, mature or work-oriented. The relationship becomes a vehicle for the soul's lessons. Rath reads AK in the 7th of D9 as "dharma lived through partnership". The D9 AL in Cancer, 11th from the KK, shows the inner life seen as networks and communities.
- **Aries (recorded).** The D9 7th lord Venus is in the 10th, which joins partnership with career and public role. Mars, the lagna lord, in the 7th gives a direct, energetic partnership style. Because the D9 AL is Capricorn with Venus–Rahu, the inner life is perceived through ambition and Venusian/technical output. The KK in the 6th is the classic sign of a person sharpened by competition.
- **Taurus.** This is the most supportive D9: a benefic lagna, Jupiter rising, and Saturn as yogakaraka in a trine with the AK. The D9 AL falls on the karakamsa, so how the inner self is perceived and what it is coincide. 01 already ranked this window highest. The Arudha and pushkara points add to that.
- **Gemini** begins at 21:54 (+19 min). Jupiter becomes the 7th and 10th lord in the 12th, and the D9 AL falls in Leo. It is listed only to bound the window.

Do not read partner traits from the 7th of D9 without event-based rectification. The only partner indicator robust across all three windows is **Venus in Capricorn with Rahu, 5th from the AK, under Jupiter's aspect**.

---

## 2. D10 Dasamsa

BPHS ch. 6 assigns the dasamsa to *mahat-phala*: great results, status, power. Reading it as the career chart in the modern sense is largely **K.N. Rao's contribution**. He developed and tested it over decades of research at Bharatiya Vidya Bhavan, much of it published in his *Journal of Astrology*. I cite the method, not any single article, because I cannot verify individual article titles here. His book *Planets and Children* is about the D7, not the D10. B.V. Raman leaned on the D9 rather than the D10 for profession, so this is a real difference in emphasis between the masters.

The D10 counting rule is that odd signs count from the sign itself and even signs from the 9th (BPHS). That rule is standard and gives the positions below.

### 2.1 Robust D10 placements and dasamsa deities

BPHS gives ten dasamsa deities: Indra, Agni, Yama, Rakshasa, Varuna, Vayu, Kubera, Ishana, Brahma and Ananta. They run in that order in odd signs and in reverse in even signs. Rath's school reads them as the "ten directions" of a planet's work.

| Planet | D10 sign and degree | Dignity | Deity |
|---|---|---|---|
| **Saturn** (D1 lagna and 2nd lord) | **Libra 15°44′** | **exalted** | Kubera (resources, treasury) |
| **Venus** (D1 5th and 10th lord) | **Libra 8°10′** | **own / moolatrikona** | Yama (rules, discipline, justice) |
| **Mars** (D1 4th and 11th lord) | **Libra 26°56′** | friend | Indra (command) |
| Sun | Leo 9°36′ | own / moolatrikona | Yama |
| Moon (AK) | Aquarius 15°24′ | enemy (Saturn's sign) | Indra |
| Mercury | Pisces 14°42′ | **debilitated**, with Ketu | Ananta |
| Jupiter | Taurus 22°07′ | neutral | Agni |
| Rahu / Ketu | Virgo / Pisces (true node) | — | Rakshasa |

**Mercury's D10 debilitation is cancelled** [Robust]. Jupiter, lord of Pisces, is in Taurus, a kendra (4th) from the D10 Moon in Aquarius. That cancels it whichever D10 lagna is right.

**The D1 10th lord (Venus) is in its own sign in D10, and the D1 lagna lord (Saturn) is exalted there.** In Rao's method the most important check is whether the D1 career lord and lagna lord are well placed in the D10. Here both are, so career is a strong area of the life whatever the D10 lagna [Robust].

### 2.2 The four D10 lagna scenarios [Time-sensitive]

| D10 lagna | Window | Libra cluster in | D10 lagna lord | D10 10th lord | Lagna deity |
|---|---|---|---|---|---|
| **Scorpio** | 21:14:30 – 21:25:45 | 12th | Mars in the 12th | **Sun in the 10th, own sign** | Ishana |
| **Sagittarius** | 21:25:45 – 21:37:00 (recorded) | **11th** | Jupiter in the 6th | Mercury, debilitated, in the 4th with Ketu; Rahu in the 10th | Kubera |
| **Capricorn** | 21:37:00 – 21:48:00 | **10th** | **Saturn, exalted, in the 10th** | **Venus, own sign, in the 10th** | Vayu |
| **Aquarius** | 21:48:00 – 21:59:00 | 9th | Saturn, exalted, in the 9th | Mars in the 9th; Moon in the D10 lagna | Varuna |

How Rao's school would read each:
- **Scorpio.** The 10th lord, the Sun, is strong in its own house, so the career shows through authority, government or a leadership title. The strong Libra group sits in the 12th: foreign, back-office or behind-the-scenes institutional work, research or large organisations.
- **Sagittarius (recorded).** The strengths gather in the 11th: gains, networks, professional circles, income above title. Rahu in the 10th, with the 10th lord debilitated (though cancelled), gives a career that is unconventional, technology- or foreign-tinged, or works through new fields. The lagna lord Jupiter in the 6th (service, competition, upachaya) means it improves with effort and time. The work is advisory, analytical and teacherly.
- **Capricorn.** This is the textbook strong dasamsa. Lagna lord and 10th lord sit together in the 10th, the lagna lord exalted and the 10th lord yogakaraka, and the D10 mirrors the D1 lagna. Expect visible authority in structured fields: engineering, administration, systems, finance, design-engineering. This is the variant worth testing first in rectification (01 and 00 agree).
- **Aquarius.** The cluster sits in the 9th (fortune, mentors, higher learning, policy), with lords of the 4th, 9th, 10th and lagna together. A dharma–karma yoga inside the D10, plus the AK Moon rising, gives a career tied to purpose, teaching, research institutions, or work done in the name of a principle.

### 2.3 The dasha lens (Rao's method) [Robust signs, Time-sensitive houses]

Rao reads a career change in a dasha through the dasha lord's D10 house.

| Dasha | Lord's D10 sign | Sagittarius D10 | Capricorn D10 |
|---|---|---|---|
| Jupiter MD (2021–2037) | Taurus | 6th: jobs, service, competition | 5th: trine, intelligence, mantra |
| Ju/Me (Jun 2026 – Sep 2028) | Pisces, debilitated but cancelled | 4th | 3rd: effort, initiative |
| Ju/Ve (Aug 2029 – Apr 2032) | Libra, own sign | **11th** | **10th** |
| Saturn MD (Oct 2037 –) | Libra, exalted | **11th** | **10th** |

In both live windows, Venus's sub-period and Saturn's mahadasha activate the Libra cluster. That agrees with the timing convergence in 00 §4.

### 2.4 Career-field reading of the Libra cluster [Robust]

Libra is a sign of commerce, contracts, law, balance and design.
- Saturn exalted there: systems, scale, infrastructure, long-horizon process, labour and organisation.
- Venus in its own sign: design, finance, aesthetics, negotiation, media, user experience.
- Mars there: engineering, hardware, technical execution, competition, property.

The classical combinations (Saturn–Mars for machines and engineering, Venus–Saturn for structured design, architecture and finance) point to **technical design, systems engineering, or the business and finance of technical products**. These are classical significations, not a prediction of any particular job title.

---

## 3. The other vargas

BPHS ch. 6 gives the uses quoted in each entry. Planet signs are [Robust] unless §0 flags them. Windows are [Time-sensitive].

### D3 Drekkana: siblings, courage (*bhrātṛ*)
- **Placements:** Su Ge · **Mo Ta (exalted)** · Ma Li · Me Cn · Ju Ar · **Ve Pi (exalted)** + Ra · Sa Le · Ke Vi.
- **Lagna windows:**
  - Capricorn before 21:29:30.
  - **Taurus from 21:29:30 to 22:06.** This is the most stable varga lagna after the D1.
- **Taurus reading:**
  - The exalted Moon is in the D3 lagna, and its lord Venus is exalted in the 11th.
  - The 3rd (Cancer) holds Mercury. Its lord, the Moon, is exalted in the lagna. This is a strong 3rd-house picture: initiative, communication, supportive sibling bonds.
  - Mars, the karaka for siblings, sits in the 6th, which suggests sibling ties combine help with rivalry.
- **Other drekkana schemes:** the Parivritti, Somanatha and Jagannatha drekkanas, used by SJC, give different charts. They are not computed here [Moderate].

### D4 Chaturthamsa: fortune (*bhāgya*) per BPHS; property and home in modern use
- **Placements:** Su Ge · Mo Ge · Ma Li + **Sa Li (exalted)** · Me Cn + Ke · Ju Ar · Ve Cp + Ra.
- The D4 maps sign quarters onto kendras, so the four strong groups lie on the cardinal cross.
- **Lagna windows:**
  - Capricorn before 21:20:15.
  - **Aries from 21:20:15 to 21:48.**
  - Cancer after.
- **Aries reading:**
  - Jupiter, the 9th lord, is in the lagna.
  - Mars, the lagna lord, is in the 7th with exalted Saturn, the 10th lord.
  - Venus is in the 10th.
  - The 4th (Cancer) holds Mercury and Ketu, and its lord the Moon is in the 3rd.
  - Fortune is built through partnership and work, not inherited. Saturn's exaltation here is a second varga in which the D1-debilitated lagna lord is exalted.
- **Where the sources split:** BPHS says "fortune"; most modern authors read residence and property. Both are given here [Moderate].

### D7 Saptamsa: children and grandchildren (*putra-pautra*)
- **Placements:** Su Cn · Mo Vi · Ma Li · Me Cp · **Ju Ta** + Ra · Ve Ge · Sa Le · Ke Sc.
- **Lagna windows:**
  - Leo, 21:07:45 – 21:24:15.
  - **Virgo, 21:24:15 – 21:40:15** (recorded).
  - Libra, 21:40:15 – 21:55:45.
- **Method (K.N. Rao, *Planets and Children*):** read the D7 lagna, the 5th house and its lord, and Jupiter, together with the dashas.
- **Virgo:**
  - The Moon is in the lagna, and the lagna lord Mercury is in the 5th.
  - The 5th lord Saturn is in the 12th.
  - Jupiter, the putrakaraka, is in the 9th (a trikona) with Rahu.
- **Libra:**
  - Mars is in the lagna, and the lagna lord Venus is in the 9th.
  - The 5th lord Saturn is in the 11th.
  - Jupiter is in the 8th.
- **Robust core:** Jupiter is in a Venus sign with Rahu in every window.
- This report makes no forecasts about children. The structure is given for a reader doing event-based work.

### D12 Dwadasamsa: parents
- **Placements:** **Su Le (own) + Mo Le** · Ma Sc (own) + Sa Sc · Me Cn · Ju Ge · **Ve Pi (exalted)** + Ra · Ke Vi.
- **Robust core:** both luminaries, the father and mother karakas, share Leo, with the Sun in its own sign. Read across schools, that means strong, dignified parent figures who are closely linked to each other. Saturn and Mars together in Scorpio, a sign where Saturn is a great enemy, show friction or burden on the lineage side.
- **Lagna windows:**
  - Aries, 21:20:15 – 21:29:30.
  - **Taurus, 21:29:30 – 21:39** (recorded).
  - Gemini, 21:39 – 21:48.
  - Cancer, 21:48 – 21:57.
- **Taurus:** the 4th (mother) is Leo, holding the Sun and Moon. The 9th lord Saturn (father) is in the 7th with Mars.
- **Gemini:** Jupiter is in the lagna, and the Sun and Moon are in the 3rd.
- The D12 is one of the best rectification tools in the chart. 00 §6 suggests checking it against parents' milestones.

### D16 Shodasamsa: vehicles, comforts, happiness (*vāhana-sukha*)
- **Placements:** **Su Pi + Mo Pi + Ve Pi (exalted)** · Ma Ta · Me Ar · Ju Ge · **Sa Aq (moolatrikona)** · Ra and Ke both in Aquarius.
- **The nodes sharing a sign is an artefact of the division**, not a conjunction. Opposite points in signs of the same modality land in the same D16 sign. The same happens in D20, D24, D30, D40 and D45. Practitioners ignore such node "conjunctions".
- **Lagna windows:**
  - Virgo, 21:27:15 – 21:34:15.
  - **Libra, 21:34:15 – 21:41:15.** The recorded time is only 45 seconds inside.
  - Scorpio, 21:41:15 – 21:48.
- **Libra:** the lagna lord Venus is exalted in the 6th with the luminaries, and Saturn is in moolatrikona in the 5th.
- **Robust core:** this is Venus's best varga (exalted, with both lights), and Saturn is again dignified.

### D20 Vimsamsa: worship, spiritual practice (*upāsanā*)
- **Placements:** Su Sg · Mo Pi (Aquarius before 21:30:15) · Ma Ta · Me Ar · **Ju Cn (exalted)** · Ve Ge · Sa Ta · Ra and Ke in Taurus.
- **Lagna windows:**
  - Libra, 21:25:45 – 21:31:30.
  - **Scorpio, 21:31:30 – 21:37** (recorded).
  - Sagittarius, 21:37 – 21:42:30.
  - Capricorn, 21:42:30 – 21:48.
- **Scorpio:** the exalted Jupiter is in the 9th, the house of dharma. The lagna lord Mars is in the 7th with Saturn.
- **Sagittarius:** the Sun is in the lagna, and the lagna lord Jupiter is exalted in the 8th, a house of the occult and of inner transformation.
- **Robust core:** **Jupiter's only exaltation in the 16 vargas is here.** The planet that is weakest in vimshopaka terms (§5) is at its best in the spiritual chart. That matches 02's ishta and dharma devata readings, and the classical view of Jupiter as functionally difficult but spiritually rich for Capricorn.
- **Deities:** Jupiter is in Lakshmi's vimsamsa and Saturn in Shachi's. These are devotional colours only.

### D24 Chaturvimsamsa (Siddhamsa): learning (*vidyā*)
- **Placements:** Su Cp · **Mo Ta (exalted)** · Ma Li · Me Le · **Ju Sg (moolatrikona)** + **Ve Sg** · Sa Sc · nodes in Scorpio.
- **Lagna windows:**
  - Pisces, 21:29:30 – 21:34:15.
  - **Aries, 21:34:15 – 21:39** (recorded).
  - Taurus, 21:39 – 21:43:30.
  - Gemini, 21:43:30 – 21:48.
- **Aries:** Jupiter and Venus are in the 9th (higher learning) and the Sun in the 10th.
- **Pisces:** the lagna lord Jupiter is in the 10th with Venus.
- **Taurus:** the exalted Moon rises.
- **Robust core:** the guru planet is in its own sign with the yogakaraka, and the Moon is exalted. That is a strong learning signature in every window. Rath and PVR read the 4th, 5th and 9th of D24 for school, intelligence and higher study; that convention is modern.

### D30 Trimsamsa (Parashari): evils and misfortunes (*ariṣṭa*)
- **Placements:** Su Aq · Mo Sc (debilitated) · **Ma Ar (own / moolatrikona)** · Me Ta · Ju Aq · Ve Cp · Sa Ge · nodes Cp.
- **Lagna windows:**
  - Virgo, 21:10:30 – 21:37.
  - Pisces, 21:37 – about 22:06.
- **Classical use:** the trimsamsa shows the kinds of difficulty a person meets and how strong their resistance is. Rath and PVR also use it for health and temperament under stress.
- **Robust core:**
  - **Mars is in its own trimsamsa** (Agni's portion): strong resilience and fight.
  - The Moon is debilitated in D30: stress lands in the emotions first.
  - These are tendencies, not events.
- **Note:** Varahamihira's trimsamsa, used for women's charts in BJ, is a different tradition and is not applied here.

---

## 4. D60 Shashtiamsa

**Why it matters.** BPHS ch. 7 gives the D60 the **largest single vimshopaka weight**: 4 of 20 points in the shodashavarga scheme and 5 of 20 in the dashavarga. Ch. 6 says the shashtiamsa should be consulted for all matters. That is the textual basis for calling it Parashara's most important varga. Parashara assigns no single topic to it. Later tradition, including Rath, reads it as the karmic layer from past lives.

**Method (BPHS).**
1. Double the degrees within the sign and take the integer part. Add 1 to get the shashtiamsa number, from 1 to 60. Each part is 30′ of arc.
2. The D60 sign is counted from the planet's own sign.
3. The deity is read from the list of 60 names in order for odd signs, and in **reverse order for even signs**.
4. The names below follow the Santhanam translation's list.

**Where sources disagree.**
- A few names vary between editions, for example *Purishaka* / *Purisha* and *Kalinasha* / *Kalināśa*.
- Some modern authors question the even-sign reversal.
- The benefic or malefic class of each name is broadly agreed.
- All D60 results are [Moderate] at best for a planet within a few arcminutes of a boundary. See §0: the Sun, Mercury and Saturn.

### 4.1 The planets' shashtiamsas

| Point | Rasi position | Part (1–60) | Sign parity | Deity no. | **Deity** | Class | D60 sign | Tag |
|---|---|---|---|---|---|---|---|---|
| Sun | Ge 6°57′33″ | 14 | odd | 14 | **Marutvan** | benefic | Cancer | Moderate (part 15, *Kala*, malefic, is 2.4′ ahead; a KP-type ayanamsa moves it there) |
| Moon | Vi 28°32′23″ | 58 | even | 3 | **Deva** | benefic | Gemini | Time-sensitive (before 21:30:15: part 57, *Kubera*, benefic, Taurus D60, where the Moon is exalted) |
| Mars | Li 2°41′33″ | 6 | odd | 6 | **Kinnara** | benefic | Pisces | Robust |
| Mercury | Cn 1°28′12″ | 3 | even | 58 | **Payodhi** | benefic | **Virgo (exalted)** | Moderate (1.8′ to part 4, *Amrita*, benefic) |
| Jupiter | Ar 5°12′43″ | 11 | odd | 11 | **Maya** | malefic | Aquarius | Robust |
| Venus | Cn 21°49′00″ | 44 | even | 17 | **Amrita** | benefic | Aquarius | Robust |
| Saturn | Ar 19°34′27″ | 40 | odd | 40 | **Vishadagdha** | malefic | Cancer | Moderate (4.5′ from part 39, *Purnachandra*, benefic) |
| Rahu | Cn 20°05′17″ | 41 | even | 20 | **Komala** | benefic | Scorpio | Moderate (node choice; the mean node gives a different part) |
| Ketu | Cp 20°05′17″ | 41 | even | 20 | **Komala** | benefic | Taurus | Moderate |
| Lagna | Cp 11°29′10″ | 23 | even | 38 | **Amrita** | benefic | Scorpio | **Time-sensitive** (see §4.2) |

**Reading [Moderate].**
- **Seven of nine points are in benefic shashtiamsas**, including both luminaries, the yogakaraka Venus (*Amrita*, "nectar") and the 9th lord Mercury, which is also exalted in D60.
- **The two malefic shashtiamsas belong to Jupiter and Saturn**, the D1 Aries pair in the 4th.
  - Jupiter is in *Maya*, illusion.
  - Saturn is in *Vishadagdha*, burnt by poison.
  - Both are also in signs of compound enemies in D60.
- Read in the BPHS frame, the benefic shashtiamsa protects what a planet signifies, and the malefic one makes its results harder won. The karmic difficulty in this chart is therefore concentrated in the Jupiter–Saturn conjunction: home, foundations, teachers, the lagna lord.
- This matches the rasi (debilitated Saturn), the vimshopaka (§5), and the neecha-bhanga "earned late" theme.
- These are interpretive colours, not verdicts. Saturn is only 4.5′ from a benefic part, so a slightly different ayanamsa would soften the picture.

### 4.2 Why the D60 lagna cannot be used [Time-sensitive]

The ascendant moves about 16′ of arc per minute here, so each 30′ shashtiamsa lasts only **about 1 minute 52 seconds**. The sequence is:

| Clock time (IST) | Lagna | Part | D60 sign | Deity | Class |
|---|---|---|---|---|---|
| 21:29:28 – 21:31:20 | 10°00′ – 10°30′ Cp | 21 | Virgo | Vishadagdha | malefic |
| 21:31:20 – 21:33:12 | 10°30′ – 11°00′ | 22 | Libra | Purnachandra | benefic |
| **21:33:12 – 21:35:04** | **11°00′ – 11°30′** | **23** | **Scorpio** | **Amrita** | **benefic** |
| 21:35:04 – 21:36:56 | 11°30′ – 12°00′ | 24 | Sagittarius | Sudha | benefic |
| 21:36:56 – 21:38:46 | 12°00′ – 12°30′ | 25 | Capricorn | Kantaka | malefic |
| 21:38:46 – 21:40:38 | 12°30′ – 13°00′ | 26 | Aquarius | Yama | malefic |

The recorded 21:35:00 is **4 seconds** before the D60 lagna changes. No hospital clock is that precise, so the D60 lagna and its houses are unusable without full rectification. Only the planets' shashtiamsas in §4.1 carry weight.

---

## 5. Vimshopaka-style dignity summary

**Basis.** Dignities across the 16 shodashavarga charts (D1, 2, 3, 4, 7, 9, 10, 12, 16, 20, 24, 27, 30, 40, 45, 60).
- Compound relations use D1 temporal friendship.
- Exaltation, moolatrikona and own sign count as sign-level in the vargas.
- Points follow BPHS ch. 7: own 20, great friend 18, friend 15, neutral 10, enemy 7, great enemy 5. Exaltation scores 20 and debilitation 5.
- The scores are illustrative. Parashara's Light and Jagannatha Hora use slightly different dignity rules, so the decimals will differ, but the ranking should not [Moderate]. The counts are [Robust] except for the §0 caveats.

| Planet | Exalted | Own / MT | Friend or great friend | Neutral | Enemy or great enemy | Debilitated | Vimshopaka (16-varga) | Shodashavarga vaisheshikamsa |
|---|---|---|---|---|---|---|---|---|
| **Sun** | 1 (D27) | 3 (D2, D10, D12) | 8 | 3 | 0 | 1 (D45) | **16.4** | 4: Nagapushpa |
| **Venus** | **4 (D3, D12, D16, D40)** | 1 (D10) | 6 | 5 | **0** | **0** | **15.9** | 5: Kanduka |
| **Moon** | 2 (D3, D24) | 0 | 9 | 0 | 4 (D10, D16, D20, D40) | 1 (D30) | 15.6 | 2: Bhedaka |
| Mars | 0 | 2 (D12, D30) | 9 | 4 | 0 | 1 (D40) | 13.6 | 2: Bhedaka |
| Mercury | 1 (D60) | 1 (D45) | 6 | 7 | 0 | 1 (D10, cancelled) | 13.3 | 2: Bhedaka |
| **Saturn** | **2 (D4, D10)** | 1 (D16) | 6 | 2 | **4 (D2, D12, D24, D60)** | **1 (D1)** | 11.5 | 3: Kusuma |
| **Jupiter** | 1 (D20) | 1 (D24) | 2 | **10** | 2 (D30, D60) | 0 | **10.4** | 2: Bhedaka |

In the dashavarga set (D1, 2, 3, 7, 9, 10, 12, 16, 30, 60) the ranking is Sun 17.2, Venus 16.2, Moon 15.5, Mars 14.1, Mercury 12.9, Saturn 10.0, Jupiter 9.6. That puts Venus at Gopuramsa (4 dignified vargas) and Sun at Uttamamsa (3).

**Who gains and who loses across the vargas.**
- **Saturn gains the most dignity relative to D1.**
  - It is debilitated in D1, but exalted in D4 (fortune and property) and D10 (career), in moolatrikona in D16 (comforts), and a great friend in D9, D20, D27, D30, D40 and D45.
  - It loses in D2 (wealth), D12 (parents), D24 (learning) and D60.
  - Taken across the vargas, Saturn is weak in the body chart and in the inherited and karmic layers, but strong where action is built: career and property. That is neecha-bhanga, varga by varga [Robust].
- **Venus is the chart's most consistently dignified planet.** It is never debilitated and never in an enemy sign, and it is exalted in four vargas. The yogakaraka's promise is confirmed in every layer [Robust].
- **The Sun, only a "friend" in D1 Gemini, rises in the vargas.** It holds own sign or MT in the wealth, career and parents charts and is exalted in D27. As 8th lord it gives quiet, durable strength.
- **The Moon (AK) is split.** It is strong in courage (D3) and learning (D24) and vargottama in D9. It is in enemy signs in career (D10), comfort (D16) and spiritual practice (D20), and debilitated in D30. Its D20 position is time-sensitive (§0).
- **Jupiter is the weakest in vimshopaka terms**: 10 of 16 neutral, with malefic D30 and D60. It still peaks where its nature belongs: exalted in D20, moolatrikona in D24. This fits the BPHS view that Jupiter is functionally malefic for Capricorn (3rd and 12th lord), and it argues against expecting easy material gifts from the 2021–37 Jupiter mahadasha.
- **Mercury** stands out only in the subtle charts: D9 vargottama and pushkara, exalted in D60, own sign in D45.

A commonly cited reading of BPHS ch. 7 treats a vimshopaka of 15 or more as giving full results. On that scale the Sun, Venus and Moon reach it, and Saturn and Jupiter do not. Translations differ on the exact bands, so the scale is [Moderate].

---

## 6. The 64th navamsa and the 22nd drekkana (khara points) [Moderate]

These are traditional sensitive points. Both fall in the **8th sign from the reference point, in the same division**: 210° ahead in both cases.

- The **22nd drekkana** is used in *Brihat Jataka*'s chapter on the end of life.
- The **64th navamsa** is paired with it in later manuals.
- Authors disagree on whether to count from the lagna, the Moon, or both.

Modern practice mostly uses the two points to mark transits worth noting. They are described here as structure only. **No longevity or health inference is drawn.**

| Reference | 22nd drekkana | Its lord | 64th navamsa | Its lord |
|---|---|---|---|---|
| Moon (Vi 28°32′) → Ar 28°32′ | Sagittarius drekkana of Aries | Jupiter | Sagittarius navamsa (4th from the Moon's D9) | Jupiter |
| Lagna (Cp 11°29′) → Le 11°29′ | Sagittarius drekkana of Leo | Jupiter (holds 21:29:30 – 22:06) | Cancer navamsa (4th from the D9 lagna) | Moon (Pisces D9: Gemini/Mercury; Taurus D9: Leo/Sun) |

From the Moon, both khara lords are Jupiter, and that is robust. Jupiter is also the D60-*Maya* planet and the vimshopaka-weakest. It is a planet whose periods call for patience, not one to fear.

---

### Key findings

- **Saturn's dignity is restored in the vargas** [Robust]. Debilitated in D1, it is exalted in D10 and D4, in moolatrikona in D16, sits with the AK in the D9 karakamsa, and is disposited by a vargottama, pushkara Mercury. It stays weak in D2, D12, D24 and D60 (*Vishadagdha*). Its strength is in what is built (career, property), not in what is inherited or easy.
- **Venus is the most consistently dignified planet** [Robust]. It is never debilitated or in an enemy sign across all 16 vargas, exalted in four, in moolatrikona in D10, and in the *Amrita* shashtiamsa. The D1 10th lord and D1 lagna lord are both dignified in D10, which makes career a strong area of life whichever D10 lagna is correct.
- **The D9 confirms the core** [Robust]. The Moon, Mars and Mercury are vargottama. Mercury is the only pushkara-navamsa planet. Every D9 dispositor chain ends in the Moon–Mercury exchange, the same loop as in D1. Jupiter's near-exact aspect binds the Moon/Saturn and Venus/Rahu in an earth trine.
- **Time-sensitive layers to test by rectification.**
  - The D9 lagna: Pisces / **Aries** / Taurus. The Taurus window also puts the lagna in a pushkara navamsa and places the D9 AL on the karakamsa.
  - The D10 lagna: Scorpio / **Sagittarius** / Capricorn / Aquarius. Capricorn, 21:37–21:48, puts exalted Saturn and own-sign Venus in the 10th.
  - The D16 lagna is only 45 seconds into Libra at the recorded time.
  - The D60 lagna changes 4 seconds after 21:35:00 and is unusable.
- **The D60 planets are mostly benefic** [Moderate]. Seven of nine points are in benefic shashtiamsas. The two malefic ones are Jupiter (*Maya*) and Saturn (*Vishadagdha*), the D1 Aries pair, so the karmic difficulty is concentrated in that one conjunction. The Sun's and Saturn's classes depend on a few arcminutes of ayanamsa. The Moon's D60, D20 and D40 change if the birth was before 21:30:15.
