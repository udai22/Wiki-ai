# 10 · Audit, contradictions and the skeptic's case

*Udai · 22 Jun 1999, 21:35 IST, Mumbai. Audited 18 Oct 2026. Scope: 00–09, 11, 12, `data-pack.md`, `birth-time-sensitivity.txt` and `GROUND-RULES.md`, as they stood at 06:21 on 18 Oct 2026. `data-pack-extra.md` (06:28) was used only to confirm the sunrise convention.*

This chapter does three jobs. It checks the other chapters' facts against the engine. It asks where they go further than the traditions or the evidence allow. And it writes down the most checkable claims so they can be scored later, as [GROUND-RULES](GROUND-RULES.md) rule 4 requires.

**How the checks were made.** Every number below was recomputed with this repo's `astro/` engine (`chart`, `vargas`, `dasha`, `ashtakavarga`, `kp`, `transits`, `rectify`, `cycles`, `special`) and with `swisseph` directly. Lahiri and true node are used unless marked otherwise. Transit hits and ingresses were found by bisection to under a minute. The scratch scripts are in `/tmp/udai_audit/`.

**A note on dates.** Several "one-day" disagreements between chapters come from mixing **UT dates** (ch. 04, 00, 11) with **IST dates** (ch. 03, 08, 12). This chapter gives IST throughout, and gives UT as well where the two differ. The reports should pick one convention. IST is the obvious choice, since the birth time is in IST.

---

## 0. The verdict in brief

- **The computational core is sound.** The following all reproduce exactly:
  - planet positions, nakshatras and padas;
  - houses, both kinds of aspect, all 12 arudhas and both karaka schemes;
  - every D9 and D10 sign, and the ashtakavarga table;
  - the Vimshottari dates at all three levels, and the Yogini dates;
  - all four Chara dasha variants, the KP cusp table and the varga windows;
  - the Tajika returns and the eclipse and station tables.
- **There are about a dozen real errors.** None of them changes the overall picture. They cluster in four places:
  - the master map's robust window (21:05 should be **20:51**);
  - ch. 05 putting **sidereal** Jupiter dates into the tropical chapter, and a Saturn-ruled window that is true for only one zodiac;
  - two arithmetic slips in ch. 01;
  - ch. 06, 08 and 12, which have a handful of one-day date errors and one probable Tajika table error.
- **The bigger problem is interpretive, not computational.** The neecha-bhanga count double-counts conditions that are not independent. Summaries say "every system agrees" where only some do. Many period descriptions would fit almost any 27- to 33-year-old. §3 and §4 deal with this.

**The two specific questions in the brief:**
- **The Saturn return is neither 27 nor 29 Apr 2029 in both zodiacs.**
  - Sidereal (Lahiri, over 19°34′27″ Aries): **29 Apr 2029, 13:08 UT (18:38 IST)**.
  - Tropical (over 13°25′14″ Taurus): **26 Apr 2029, 05:58 UT (11:28 IST)**.
  - Chapters 00 and 04 are right for the sidereal return. Chapter 05's "27 Apr" is a day late for the tropical one.
- **Ch. 05's "Jupiter crossed natal Venus on 12 Sep 2026" is the sidereal date.** Jupiter reached sidereal Venus (21°49′ Cancer) on 12 Sep 2026, 10:04 UT. It reached tropical Venus (15°40′ Leo) on **10 Sep 2026**. The "opposed the Ascendant on 26 Jul 2026" in the same sentence is also sidereal: it is the opposition to the sidereal lagna at 11°29′ Capricorn. The tropical opposition to 5°20′ Aquarius was on **24 Jul 2026**.

---

## 1. Errata

Severity: **Wrong** means the statement is false as written. **Imprecise** means it is off by a day or two, mislabelled, or stated more strongly than the numbers allow. **OK** means it was checked and confirmed, and is listed only where it was explicitly queried.

### 1.1 `00-master-map.md`

| # | Line, section | Claim | Engine says | Severity | Suggested correction |
|---|---|---|---|---|---|
| 1 | L27, §1 table | Robust layer holds "21:05 – 22:41 (−43 to +66 min)" | Lagna is Capricorn from −43.5 min, which is **20:51:30**, to +66 min (22:41). The time 21:05 corresponds to −30 min | **Wrong** | "20:51 – 22:41". The same error is copied into 06 L11 and 09 L8 |
| 2 | L40–46, §2.1 | "Five or six classical neecha-bhanga conditions", with the 6th given as "Saturn is exalted in the D10" | D10 exaltation is not a classical neecha-bhanga condition. The classical varga condition is exaltation in the **navamsa**, and it fails here: Saturn is in Virgo in D9. Ch. 01's 6th condition is a different one (#9, the navamsa lord Mercury in a kendra) | **Wrong** | Replace the D10 bullet with "Mercury, lord of Saturn's navamsa, is in a kendra (minor rule)". Mention D10 exaltation separately, as varga support |
| 3 | L91, §3 | KP Mars sub "holds only 21:33:30 – 21:36:30" | With the KP ayanamsa: −1.75 to +1.25 min, i.e. **21:33:15 – 21:36:15**. With Lahiri: 21:33:45 – 21:36:30. `birth-time-sensitivity.txt` gives −1.0/+1.5, which is the Lahiri figure on a 30-second grid | Imprecise | Give the KP-ayanamsa window and name the ayanamsa used |
| 4 | L97, §3 | KP "argue[s] against 21:29 – 21:30" | Ch. 03 L259 argues against the **Venus-sub window, −14 to −5.5 min (21:21 – 21:29:30)**, and treats 21:29:30 – 21:33 (Moon sub) as a secondary zone | Imprecise | "They argue against 21:21 – 21:29" |
| 5 | L110 | "Saturn into Aries 2 Jun 2027" | 2 Jun 23:58 UT = **3 Jun 2027, 05:28 IST** | Imprecise | Use 3 Jun (IST), as ch. 03 and ch. 08 do |
| 6 | L111 | Chara for Aug 2029 – Apr 2032 is "Aquarius, then Capricorn sub-periods" | Cancer MD sub-periods: Pisces (to Oct 2029), Aquarius (Oct 2029 – Aug 2030), Capricorn (Aug 2030 – Jun 2031), Sagittarius (Jun 2031 – Apr 2032) | Imprecise | List all four |
| 7 | L111 | "double transits on the 5th, 7th and 11th, Sep 2030 – May 2032" | They are intermittent. The 5th and 7th: 23 Sep 2030 – 16 Feb 2031, 14 Jun – 14 Oct 2031, 5 Mar – 30 May 2032. The 11th: only 23 Sep 2030 – 16 Feb 2031 and 14 Jun – 14 Oct 2031 | Imprecise | Give the three windows, and say the 11th drops out after Oct 2031 |
| 8 | L111 | "Vimshottari, Chara, Yogini and double transits all agree" | Yogini's *mahadasha* for the whole window is **Sankata** ("difficulty", 2027–35). Only two sub-periods (Dhanya and Bhramari, Jul 2029 – Jan 2031) are favourable | Overreach | "Vimshottari and the double transits agree; Yogini agrees only at sub-period level, inside a Sankata mahadasha" |
| 9 | L129, §5 | 7- vs 8-karaka "changes only the labels for parents and children" | Per ch. 02, PK (children) is Jupiter in both schemes. What changes is MK (Sun becomes Rahu), and PiK (the Sun) appears | Imprecise | "…changes only the parent labels (MK and PiK)" |
| 10 | L131, §5 | "Every variant agrees that Libra and Cancer dominate 2013–2045" | SJC with Scorpio→Ketu: Scorpio 2011–21, Libra 2021–30, **Leo 2032–42**, Cancer only from 2042. SJC with Scorpio→Mars: **Leo 2023–33**. Libra appears in every variant, but in the 2030s Leo competes with Cancer | Overreach | "Libra runs in every variant at some point in 2012–31; the 2030s are Cancer or Leo depending on the variant" |
| 11 | L118 | Barbault index "lifetime low in 2021" | Annual means for 1999–2040: 2021 = 508 (lowest), then 2022 = 511 and 2020 = 539 | OK | — |
| 12 | L3 | "checked against Parashara's Light 9.0" | Partly documented. `data-pack-extra.md` (added 06:28) records PL comparisons for Gulika, Mandi, shadbala and sunrise. No PL output is stored for positions, dashas or vargas | Partly unverifiable | Store PL exports for the core tables, or soften to "designed to match PL" |

### 1.2 `01-parashari.md`

| # | Line | Claim | Engine says | Severity | Suggested correction |
|---|---|---|---|---|---|
| 13 | L16 | Arudha Lagna and Upapada tagged [Moderate] | AL and UL depend only on the lagna sign, so they hold from −43.5 to +66 min (`birth-time-sensitivity.txt`). Ch. 00 and ch. 02 call them Robust | Imprecise (tag) | Move them to [Robust] |
| 14 | L102 | Mahapurusha yogas absent "despite **four** planets being in kendras" | **Five** grahas are in kendras: Jupiter and Saturn (4th), Mercury and Venus (7th), Mars (10th). Both nodes are in kendras too | **Wrong** | "five planets (seven bodies, counting the nodes)" |
| 15 | L115 | "11th > 12th … and the more refined **11th > 10th > 1st** both hold" | SAV: 11th = 38, 10th = **25**, 1st = **27**. So 10th < 1st | **Wrong** | "11th > 12th holds; 11th > 10th > 1st fails, because the 10th (25) is below the lagna (27)" |
| 16 | L54, L160 | "Five or six **independent** cancellation conditions" | The conditions rest on only three facts: **Mars in a lagna kendra**, which gives #1 and also #7, since Mars in Libra always aspects Aries; **Venus in a lagna kendra**, which gives #3, and #6 follows automatically because any two planets in lagna-kendras are in mutual kendras; and **the Sun 10th from the Moon**, which gives #5. Rule #9 is a minor fourth | Imprecise (overcount) | "Three independent placements satisfy five or six listed rules" |
| 17 | L85–107, yoga table | Sakata not listed | Phaladeepika's Sakata is **present** (ch. 06 L84): the Moon is 6th from Jupiter and not in a kendra from the lagna, so the yoga's own exception fails | Imprecise (omission) | Add "Sakata: present, mild, mitigated". Master map §2.4 should list it too |
| — | L31–41 | Neecha-bhanga rule-by-rule table | Every placement in it checks out: Mars 10th; Venus 7th; Sun 10th from the Moon; Mars 2nd and Venus 11th from the Moon; Saturn's D9 Virgo; Mercury in the 7th | OK | — |
| — | L89–105 | Yoga presence and absence | Gaja Kesari absent (Jupiter 8th from the Moon). Kemadruma absent. Sunapha, Vesi and Pasa (7 planets in 5 signs) present. Amala, Budha-Aditya, Chandra-Mangala, Harsha, Vimala and all five Mahapurusha yogas absent | OK | — |

### 1.3 `02-jaimini.md`

| # | Line | Claim | Engine says | Severity | Suggested correction |
|---|---|---|---|---|---|
| 18 | L53 | The Moon is "roughly 3.7 hours of clock time from changing" navamsa | 3.7 h is the distance **backwards**. Forwards, the Moon leaves the Virgo navamsa, and Virgo itself, at **+175 min (≈00:30 IST on 23 Jun)** | Imprecise | "about 2.9 h after, or 3.7 h before" |
| 19 | L203–208 | HL Virgo 22°45′ and GL Virgo 2°22′, "so the AK Moon occupies both"; HL in Virgo from −45 to +14 min | This holds only with sunrise at 06:02 (upper limb, with refraction). The engine's `special.special_lagnas` uses Hindu sunrise (disc centre, no refraction: **06:06 IST**), the Parashara's Light convention (`data-pack-extra.md` confirms sunrise at 06:06:15). That gives **HL Virgo 20°43′** and **GL Leo 27°17′**, with HL in Virgo from −41 to +19 min. Under that convention the Moon joins the HL only | Imprecise (convention) | State the sunrise convention, and say the double occupation depends on it |
| 20 | L249 | "Saturn returns to Aries, the natal AL, around 2028" | Saturn enters Aries on 3 Jun 2027 (IST), retrogrades into Pisces 20 Oct 2027, and re-enters on 23 Feb 2028 | Imprecise | "enters Aries Jun 2027, settles there from Feb 2028" |
| 21 | L254 | The Aries antardasha (Feb – Dec 2028) is "coinciding with Saturn's return over it" | Saturn is *in* Aries then. The exact return (19°34′) is on 29 Apr 2029, inside the **Pisces** antardasha (Dec 2028 – Oct 2029) | Imprecise | "coinciding with Saturn's transit of the AL; the exact return falls in the next sub-period" |
| 22 | L284 | "All four variants agree…" | See #10 | Overreach | As #10 |
| 23 | L29; data-pack L13 | The engine labels Jupiter "PiK" in the 7-karaka scheme | This is an **engine bug**. `astro/chart.py:164` uses `["AK","AmK","BK","MK","PiK","GK","DK"]`, but the 7-karaka scheme has PK (Putrakaraka) in 5th place and no PiK. Ch. 02 correctly flags it | Wrong (engine) | Fix the label list in `chart.py`, then regenerate the data pack |
| — | §1, §3, §4, §6 | Karaka ranks and gaps; all padas and exceptions; houses from the AL; argala; all Chara durations and dates; all four variant tables | Reproduced exactly. All 12 K.N. Rao durations check out (8, 4, 2, 9, 2, 2, 10, 1, 2, 6, 11, 7), as do the SJC odd/even durations | OK | — |

### 1.4 `03-nakshatra-nadi-kp.md`

| # | Line | Claim | Engine says | Severity | Suggested correction |
|---|---|---|---|---|---|
| 24 | L189 | Placidus house placements "hold across ±15 min" | At −15 min, KP cusp 4 is at Aries 19°24′, so Saturn (KP 19°40′) falls in the **4th**, not the 3rd. The switch is at about −14 min (21:21) | Imprecise | "hold from about −14 to +15 min; before 21:21 Saturn moves into the Placidus 4th" |
| 25 | L249, L259, L277 | Mars sub from −1.5 to +1.5 (21:33.5 – 21:36.5) | KP ayanamsa: −1.75 to +1.25 (21:33:15 – 21:36:15) | Imprecise (30-second grid) | Use the 15-second figure |
| 26 | L236 | 11th-cusp sub lords listed as "Mercury, Ketu, Venus, Sun or Moon" | At −15 min the 11th cusp is Sa/**Ju** (L216) | Imprecise | Add Jupiter |
| 27 | L6 | [Robust] is defined as "holds across ±15 min" | Every other chapter uses −43 to +66 min | Inconsistent | Align with the master map, or rename the tag |
| — | §1.1, §1.2, §3.2 table | Nakshatras, padas, ganas, motivations; the tara cycle (Chitra #14; Karma nakshatra Dhanishta); star-lord significations | Correct | OK | — |
| — | L149–156 | Jupiter and Saturn ingress table (IST) | Matches the engine to the day | OK | — |

### 1.5 `04-timing.md`

| # | Line | Claim | Engine says | Severity | Suggested correction |
|---|---|---|---|---|---|
| 28 | L30 | Neecha-bhanga support includes "Mars … occupies Libra, Saturn's exaltation sign" | This is not in the PD, JP or BPHS lists. The condition is about the *lord* of Libra (Venus) | Imprecise | Drop the clause, or label it non-classical |
| 29 | L92–99 | Saturn ingresses: Aries 2 Jun 2027, Gemini 30 May 2032, Cancer 12 Jul 2034, Scorpio 12 Dec 2043 | These are UT dates. In IST: **3 Jun 2027** (05:28), **31 May 2032** (03:01), **13 Jul 2034** (04:24), and **11 Dec 2043** (23:24). The last one is a day early even in UT terms | Imprecise | Switch the chapter to IST |
| 30 | L67, L116, L163 | "exact [Jupiter] return 27 Apr 2035" | 27 Apr 22:51 UT = **28 Apr 2035, 04:21 IST** | Imprecise | "28 Apr 2035 (IST)" |
| 31 | L109, L156 | Jupiter in Virgo 26 Nov 2027 – 26 Dec 2028 "over the natal Moon" | That is the sign only. Jupiter stations retrograde at Virgo 3°16′ on 12 Jan 2028. Its **exact conjunctions with the Moon (28°32′ Virgo) are 16 Dec 2028, 10 Apr 2029 and 16 Aug 2029** | Imprecise | Give the exact dates. These fall in Ju/Ke and the Saturn return year, not in 2028 |
| 32 | L61 | Rahu "transits the natal Moon for almost the whole antardasha" | That is the sign only. Rahu is exactly on the Moon on **13 Feb 2033**. It is exactly on Mars on 4 Jan 2033, which falls in the Libra row | Imprecise | Add the exact dates |
| 33 | L118–119 | Jupiter in Cancer 16 Sep 2037 – 7 Oct 2038; Leo then Virgo, Oct 2038 – Dec 2040 | Omits the return to Gemini, **17 Jan – 11 May 2038**, and to Cancer, **3 Mar – 2 Jun 2039** | Imprecise | Add both |
| 34 | L138 | Virgo (the 7th lord's sign) double transits: Nov 2027 – Feb 2028 and Jul 2034 – Apr 2035 | Also **15 Apr – 27 Aug 2036**, 4 Nov 2039 – 5 Apr 2040, and 30 Jun – 3 Dec 2040 | Imprecise (omission) | Add them |
| — | L38–72 | Antardasha and pratyantar dates and bands; time and arc fractions (38.89% and 39.05%); the 360-day-year shifts | Reproduced exactly | OK | — |
| — | L136–142 | Double-transit windows | Match the engine to within its 2-day sampling | OK | — |
| — | L174–177 | Yogini sequence and sub-periods | Reproduced (Mangala first, start 31 Jan; Siddha/Ulka now; Sankata sub-periods as listed) | OK | — |
| — | L126, L132 | Half nodal return 21 May 2027 (true) or 10 Jun (mean); nodal return 19 Oct 2036 (true) or 27 Sep (mean); Sade Sati from 27 Aug 2036 | Reproduced | OK | — |

### 1.6 `05-western-cycles-philosophers.md`

| # | Line | Claim | Engine says | Severity | Suggested correction |
|---|---|---|---|---|---|
| 35 | L20, L165 | "Saturn rules the rising sign in every case from about −143 min to +87 min, tropical **or sidereal**" | Tropical: Capricorn from −143, Aquarius to +87. **Sidereal: Sagittarius, ruled by Jupiter, until −43.5 min.** Both zodiacs are Saturn-ruled only from **−43.5 to +87 min** | **Wrong** | "−43 to +87 min in both zodiacs (tropical alone −143 to +87)" |
| 36 | L22, L52 | Spirit enters Gemini "at about +14 min" | **+11.5 min** (21:46:30) | Imprecise | "+11.5 min" |
| 37 | L61 | Jupiter crossed natal Venus on 12 Sep 2026 and opposed the Asc on 26 Jul 2026 | Both are **sidereal** dates. Tropical: Venus on **10 Sep 2026**, Asc opposition on **24 Jul 2026** | **Wrong (frame)** | Use the tropical dates |
| 38 | L68 | Age-30 row: "Saturn squares Venus (May 2029)" | 13 May 2029 falls in the **age-29** year (22 Jun 2028 – 21 Jun 2029) | **Wrong** | Move it to the age-29 row |
| 39 | L101 | Saturn return "27 Apr 2029 (single exact pass)" | **26 Apr 2029**, 05:58 UT. The single pass is confirmed | Imprecise (1 day) | "26 Apr 2029" |
| 40 | L105 | Jupiter return "14 May 2023; next 27 Apr 2035" | Both are the sidereal dates. Tropical: **12 May 2023** (as ch. 07 L211 correctly says) and **26 Apr 2035** (IST; 25 Apr UT) | **Wrong (frame)** | Use the tropical dates |
| 41 | L93–102 | Other exact-hit dates | Engine (IST): Saturn square Sun 6 Jun and **19** Aug 2025, 21 Feb 2026. Neptune square Sun **22** Apr and 22 Sep 2025, **22** Feb 2026. Pluto conjunct Neptune 5 Feb, 16 Aug, **12** Dec 2026. Pluto conjunct Asc **9** Apr and **3** Jun 2026, then **1** Feb, **26** Aug, **7** Dec 2027. Saturn conjunct Jupiter **5** Apr 2028. Saturn square Venus **13** May, square Uranus 19 May, opposite MC **23** May 2029 | Imprecise (1–2 days, mostly late) | Recompute by bisection. The 1–2 day drift suggests coarse sampling |
| 42 | L135 | Barbault 1999 = 797 | That is the 1 Jul value. The data pack's 790 is for the birth date. All of ch. 05's values are 1 Jul samples | Imprecise (label) | Say "sampled 1 July" |
| — | L13–17, L21, L34–57 | Lots table; the 1999 solar ingress (01:20 IST); sect; whole-sign houses; aspects and orbs; tropical Aquarius window (−20 to +87); profection signs; Rudhyar phase (111.6°) | Reproduced | OK | — |
| — | L95–108 | Neptune and Pluto sextiles; Uranus trine and conjunction windows; the past Uranus contacts | Reproduced | OK | — |
| — | L139 | Great conjunctions on 28 May 2000 (22° Taurus), 21 Dec 2020 (0° Aquarius) and 31 Oct 2040 (17° Libra) | Reproduced | OK | — |

### 1.7 Chapters 06–09, 11 and 12

| # | File, line | Claim | Engine says | Severity | Suggested correction |
|---|---|---|---|---|---|
| 43 | 06 L11, 09 L8 | Robust "21:05 to 22:41" | See #1 | **Wrong** | "20:51 – 22:41" |
| 44 | 06 L128–131; 07 L113, L132–133 | Saturn into Sagittarius "27 Jan 2017", into Pisces "30 Mar 2025", into Leo "**28 Aug 2036**", into Scorpio "12 Dec 2043" | In IST: **26 Jan 2017** (19:31), **29 Mar 2025** (21:45), **27 Aug 2036** (20:37), **11 Dec 2043** (23:24) | **Wrong** (1 day) | Correct the dates. Ch. 00 and 04 already have 27 Aug 2036 |
| 45 | 06 L86 | "its neecha-bhanga is cancelled five to six times over" | It is the *debilitation* that is cancelled | Wording | "its debilitation is cancelled…" |
| 46 | 06 L375 | "Every school in chapters 01–05 converged on" a chart that "starts low and builds" | Ch. 05's Hellenistic reading has Saturn *supported* in a Venus-ruled sign, with the sect benefic as its ruler, not starting low | Overreach | "The Vedic schools converge on it; the Hellenistic reading frames Saturn as supported, not fallen" |
| 47 | 06 L82 | "No eclipse falls close to the birth date" | The nearest were a partial lunar eclipse on 28 Jul 1999 (+36 days) and the total solar eclipse of 11 Aug 1999 (+50 days) | OK (state the gap) | Add the distances |
| 48 | 07 L169 | The 21 Jun 2020 eclipse fell "on the 21st birthday" | The birthday is 22 Jun. The eclipse was the day before | Imprecise | "on the eve of the 21st birthday" |
| 49 | 07 L200, L207, L212 | §7.4 Western overlays tagged [Robust] | It includes Saturn over the Asc (31 Jan 2021, IST 1 Feb), Saturn over the MC, and Pluto on the Asc, all of which are angle contacts and time-sensitive (ch. 05 L110). Pluto's first hit is **9 Apr 2026** (IST), not 8 Apr | Imprecise (tag) | Tag the angle hits [Time-sensitive] |
| 50 | 08 L84, L88 | Tri-rashi pati for a Sagittarius varsha lagna at night is Saturn, so Saturn "holds two offices" | The standard Tajika Neelakanthi table gives fire signs Sun/Jupiter (Aries), Jupiter/Sun (Leo) and **Saturn by day / Jupiter by night (Sagittarius)**. A night chart therefore gets **Jupiter**. Ch. 08 already uses Jupiter for the Aries night chart in 2027 (L161), so 2026 is inconsistent. The year lord is still Saturn, because Jupiter is in the blind 8th, but with one office, not two | **Probably wrong** (verify against JHora or PL) | Office-holder = Jupiter; Varshesha = Saturn, as the only office-holder that aspects the lagna |
| 51 | 08 L270, L353, L380 | "Transit Jupiter on the natal Moon" (Jan – Apr 2028); "Jupiter's arrival on the Moon (26 Nov 2027)"; "Jupiter → Virgo 26 Nov (9th, on the natal Moon)" | On 26 Nov 2027 Jupiter enters Virgo at 0°, which is 28.5° from the Moon. It stations at Virgo 3°16′ on 12 Jan 2028. The exact conjunctions are **16 Dec 2028, 10 Apr 2029 and 16 Aug 2029** | **Wrong** (as worded) | "Jupiter enters the Moon's sign"; give the exact dates |
| 52 | 08 L148 | Jupiter "two days before entering Leo" | It enters Leo on 26 Jun 2027 at 05:19 IST, about 3 days after the return | Trivial | "three days" |
| 53 | 11 L20 | "Western transits: … Saturn enters sidereal Aries on 2 Jun 2027" | A sidereal ingress in a Western list, given as a UT date (3 Jun IST) | Imprecise | Move it to the Vedic list and use 3 Jun |
| 54 | 11 L42 | Saturn–Neptune conjunction at 0°44′ Aries on 20 Feb 2026 | 0°45′, at 16:52 UT | Trivial | — |
| 55 | 12 L22 | "Rahu on the lagna (from **26 Nov 2026**)" | **25 Nov 2026, 19:15 IST** (true node; the mean node enters on 5 Dec). Every other chapter says 25 Nov | **Wrong** | "25 Nov 2026" |
| 56 | 12 L22 | Jun 2027 – mid-2029: "Jupiter in Leo, 12th from the Moon" | Jupiter is in Leo only 26 Jun – 26 Nov 2027 and 28 Feb – 24 Jul 2028. Otherwise it is in Virgo, then Libra from 26 Dec 2028 | Imprecise | Give the actual sequence |
| 57 | 12 L23 | Jupiter in Scorpio "Sep 2030 – Oct 2031" | Scorpio 25 Jan – 1 May 2030, 23 Sep 2030 – 17 Feb 2031, and 14 Jun – 15 Oct 2031, with **Sagittarius in between** | Imprecise | Give the three spans |
| — | 06 | Manglik counts; Kaal Sarp split (3–4); tithi (Shukla Dashami), karana (Taitila), yoga (Parigha); gandanta distances; combustion; graha yuddha (closest pair Jupiter–Saturn, 14.4°); nadi, yoni and vashya | Correct | OK | — |
| — | 07 | Saturn sign periods 2000–2025; Jupiter returns (1 Jun 2011 IST / 31 May UT, and 14 May 2023); Rahu over Ketu (1 Nov 2008 UT), over the lagna (15 Apr 2009) and over the Moon (27 Jul 2014); nodal return 18 Mar 2018; Saturn over the Moon 2 Nov 2011; over the lagna 4 Feb 2021; over Ketu 21 Jan 2022; Jupiter–Saturn conjunction at 6°20′ Capricorn; tropical Saturn cycle dates; Chara Libra sub-periods; Yogini sub-periods | Reproduced | OK | — |
| — | 08 | Sidereal returns (22 Jun 2026 19:47:39; 23 Jun 2027 01:57:46); varsha lagnas (Sagittarius 14°33′, Aries 1°41′); all return positions; Muntha; Mudda arithmetic; pratyantars; stations; tropical solar returns (10:10 and 15:56 IST; their Ascendants and MCs) | Reproduced | OK | — |
| — | 09 | D9 and D10 degrees; dasamsa deities; every varga lagna window; D60 parts and deity reversals; mean node 21°24′; khara points | Reproduced | OK | — |

---

## 2. Cross-chapter contradictions

**Genuine** means the schools really do differ. That is fine, and the chapters should present it as a difference. **Error** means one chapter is wrong, or the chapters are inconsistent for no reason.

| # | Topic | Where | What disagrees | Type | Resolution |
|---|---|---|---|---|---|
| C1 | Saturn's condition | 01, 04, 06 vs 05 | Debilitated (sidereal Aries) vs supported in Venus's sign (tropical Taurus) | **Genuine**, between zodiacs | 05 handles it well. 06 L375 and 00 L135 ("survives in both") paper over it |
| C2 | Jupiter's mahadasha | 01, 04, 09 | Functional malefic (BPHS 34) vs benefic in a kendra | **Genuine** | Presented well |
| C3 | Rahu beside Venus | 01, 03, 06 | Yoga-giving node (BPHS 34) vs eclipsing conjunction | **Genuine** | Presented well |
| C4 | Neecha-bhanga conditions | 00 L40–46, 01 L31–41, 04 L30 | Three different lists. The 6th item is D10 exaltation in 00, the navamsa-lord rule in 01, and "Mars in Libra" in 04 | **Error** | Use 01's table everywhere and add the independence caveat (#16) |
| C5 | Robustness of AL and UL | 01 L16 vs 00 L27, 02 L94 | Moderate vs Robust | **Error** | Robust |
| C6 | Definition of [Robust] | 03 L6 vs all others | ±15 min vs −43 to +66 min | **Error** | Align the definitions |
| C7 | KP Mars-sub window | 00, 03, 04, sensitivity file | 21:33:30–36:30; −1.5/+1.5; −1.0/+1.5 | **Error** (ayanamsa and grid) | KP ayanamsa: 21:33:15 – 21:36:15 |
| C8 | Saturn into Aries | 00, 04, 11: 2 Jun; 03, 08, 12: 3 Jun | UT vs IST | **Error** (convention) | Use IST, 3 Jun |
| C9 | Rahu into the lagna | 00, 04, 08, 11: 25 Nov; 12: 26 Nov | — | **Error** in 12 | 25 Nov |
| C10 | Jupiter return 2023 | 05: 14 May; 07: 12 May | Sidereal date in a tropical table | **Error** in 05 | 12 May (tropical) |
| C11 | Saturn return | 00, 04: 29 Apr; 05: 27 Apr | Sidereal vs (mis-dated) tropical | Partly genuine, partly error | Sidereal 29 Apr, tropical **26 Apr**. Say which is which wherever "late April 2029" is used |
| C12 | The current Chara sign | 02, 07 | Cancer (K.N. Rao, Ketu) vs Libra or Leo (other variants) | **Genuine** (method) | Keep it as a stated disagreement, but drop "all four agree" (#10) |
| C13 | Tone of 2027 | 04 L39 (Ju/Me favourable), 08 L420 (Nov 2026 – Apr 2027 constructive) vs 00 L110 ("three systems agree" 2027–29 is testing) | The dasha reads neutral-to-good; the pressure comes from transits (Saturn) and Yogini | Mostly genuine, but overstated | Say "the transits and Yogini mark 2027–29 as pressured; Vimshottari's Ju/Me does not" |
| C14 | Is Aug 2029 – Apr 2032 the strongest window? | 00, 04, 06, 12 vs 04 §4.5 | Yogini's Sankata MD runs through it | **Genuine** tension | Present Yogini as a dissent at mahadasha level |
| C15 | Weight of the second Sade Sati | 04 L81 vs 06 L135 | Lighter (Saturn is the lagna lord) vs heavier (low bindus) | **Genuine** | 06 presents it well |
| C16 | HL and GL | 02 vs engine | Sunrise 06:02 vs 06:06 | Convention | State the convention (#19) |
| C17 | What the 8-karaka scheme changes | 00 L129 vs 02 L33–36 | "Parents and children" vs parents only | **Error** in 00 | #9 |
| C18 | Sakata yoga | 06 (present) vs 01 and 00 (silent) | — | **Error** (omission) | #17 |
| C19 | Lord of the 2026–27 year | 08 (Tajika: Saturn) vs 05 (profection: Venus) | — | **Genuine** (different systems) | Fine. Note it in 00 |
| C20 | Mercury's strength | 01 ("dead" avastha, neutral) vs 09 (vargottama, pushkara, exalted in D60) | — | **Genuine** (layers) | Fine |

---

## 3. Overreach audit

### 3.1 Beyond what the traditions say

- **D10 exaltation as a neecha-bhanga condition** (00 L46) and **"Mars in Libra"** (04 L30). Neither is in the classical lists.
- **"Independent" cancellation conditions** (01 L54). They are logically linked (#16). Counting the same placement twice inflates the case.
- **Modern career mappings presented through classical vocabulary:**
  - "Rahu + Mercury → computing and networks" (03 L118). This one is flagged as modern, which is fine.
  - Chitra → "designer, maker, analyst" (00 L68, 03 L267). This is Sutton's modern gloss, not the Taittiriya Brahmana's.
  - "Technical design, systems engineering, or the business and finance of technical products" (09 L217).
  - "Exchange or partner risk … fits a trading business literally" (12 L27). This is **post-hoc fitting**: the reading was written after the business was known.
- **"5th house empty → speculative gains via partnerships, not solo bets"** (12 L14). The classical texts give no such rule.
- **Citations the chapters admit they can't pin down.** Chapter and verse numbers are hedged in 01 L3 and 02 L10, which is good. But several attributions are written as quotations: Rath's "the lagna is what you are…" (02 L113), Rao's views (01 L50, 09 L159). These should carry "as commonly reported" unless a page reference is added.

### 3.2 Barnum statements (would fit almost anyone)

Each of these reads as personal, but would ring true for most people of this age and background. They should be labelled as such, or dropped from the "robust core".

| Where | Statement |
|---|---|
| 00 L51; 01 L54 | "competence that is built slowly and earned, not given" |
| 00 L68; 03 L40 | "shadow is perfectionism and restlessness" |
| 00 L73; 02 L114–115 | "a reserved self… seen as principled, older than his years" |
| 02 L146 | "he takes commitment seriously and holds it together himself" |
| 03 L48 | "a mind that recovers from setbacks" |
| 06 L308 | "a quick, wiry, driven system that does well with routine, warmth, regular meals and sleep" |
| 06 L334 | "a capable, active mother, likely with work or responsibilities outside the home" |
| 06 L351 | "an early life of adjustment, comparison and outsider feeling" |
| 07 L34 | Rahu MD "pulls the native outward: toward others, toward the unfamiliar, toward peers" (ages 4–22) |
| 04 L47, L52 | "Expect consolidation, not expansion"; "Discernment matters" |
| 08 L381 | "Review commitments; the year closes thoughtfully, and is supported" |
| 11 L30 | Already correctly flagged by that chapter itself |

### 3.3 [Robust] tags that are really time- or convention-sensitive

- **07 §7.4 (L200)** tags the whole section Robust, yet it holds angle contacts (#49).
- **03 §3.2 (L183, L189)** tags Placidus placements Robust. They break at −14 min (#24), and they depend on choosing Placidus.
- **02 L94**: AL and the padas are "Robust within the Capricorn window". That is correct, but they also depend on the **exception rule** (AL Aries with it, Cancer without). That is a convention dependency, so the tag should be [Moderate] by ch. 09's own definition.
- **Whole-chapter tags on interpretations.** 06 B1–B11 tags "Robust" on facts, then hangs interpretations on them, such as "the kind of partner, as the texts describe it" (06 L195). The *fact* is robust. The *trait* is not robust in any testable sense.
- **00 L27** puts "double transits" in the Robust layer. As sign-level events that is fair. But their effects are read through houses counted from the lagna, and the lagna is the very thing that breaks at −43 min.

### 3.4 Over-confident timing

- **"The strongest window in the chart"** (00 L111), **"High" confidence for 2030–31** (04 L158–159), and **"the strongest payoff window in every system checked"** (12 L23). Yogini dissents (C14), and the Western timers don't single out 2030–32.
- **"The most likely window for partnership or commitment events"** (04 L144). The 7th-house double transits plus Ju/Ve plus the 2034–35 window add up to about **26 months** in 2030–35. For a man aged 31–36, the base rate of some partnership milestone in a 26-month span is already high.
- **"March to mid-April 2027 the most natural time to begin partnership or creative ventures"** (08 L402). It rests on a pratyantar boundary (±3 weeks), a Mudda period and one station. It is muhurta advice, so it is not even a prediction, and it should be framed as a suggestion.
- **"Three systems agree"** (00 L110). One of the three is a transit reading, and one is Yogini. Vimshottari's antardasha for most of 2027–28 reads favourably in ch. 04.

### 3.5 Multiple routes to "confirmation"

The chapters use at least 15 timing tools: Vimshottari at three levels; Chara in four variants; Yogini; Tajika (varshaphal, Mudda, sahams); Jupiter, Saturn and node transits; double transits on eight houses; ashtakavarga; eclipses; stations; profections; solar returns; progressions; Western outer-planet transits; and KP.

Measured on the engine, **a K.N. Rao double transit is active on at least one of the 1st, 2nd, 4th, 5th, 7th, 9th, 10th or 11th houses on 60% of days between Oct 2026 and Dec 2040**. Pratyantar and Mudda boundaries come every few weeks. Something will always be "active" (see §4.2).

---

## 4. The skeptic's case (briefly, and fairly)

This reading has been unusually careful. It separates fact from interpretation, it tags birth-time sensitivity, and it reports where the masters split. A skeptic would still raise six points. They are worth stating plainly, not to dismiss the exercise, but because they set the standard any claim here should meet.

### 4.1 Tropical vs sidereal: both cannot be literally true about sign meanings

The two zodiacs now differ by about 24°. So for roughly four placements in five, a planet's sign is different. Here the Sun is Gemini or Cancer, the Moon Virgo or Libra, and Saturn is either *debilitated* (sidereal Aries) or *comfortable* in a friend's sign (tropical Taurus).

If sign qualities came from the sky, at most one of these can be right about this Saturn. The usual reply is that each zodiac is a self-consistent symbolic language with its own rules (05 L73). That is a coherent position, but it gives up the claim that the *sky* determines the meaning. And if both systems "work" equally well for the same person, that is what one would expect if the work is being done by the reader's interpretation rather than the sky.

### 4.2 Multiple comparisons

With 15+ techniques, dozens of variants, eight "important" houses and bands of ±3 weeks, any month will contain some activated factor. Any life event can then be matched after the fact. The engine figure (60% of days under at least one relevant double transit) is one tool only. Adding pratyantars, Mudda, eclipses, stations, profections and node contacts takes coverage close to 100%.

The fix is not to use fewer tools. It is to **state in advance which tool predicts what, in which window, and what would count as a miss** (§5).

### 4.3 Unfalsifiability through cancellation

This chart shows the pattern clearly:

- Saturn is debilitated, which is bad, then cancelled five or six ways, which is good. Struggle confirms the debility, success confirms the cancellation, and late success confirms "rise after fall".
- The chart is Manglik by the Venus count, but cancelled by Jupiter.
- Sakata is present, but mitigated.
- Gaja Kesari is absent, but Jupiter is in a kendra from the lagna.
- Rahu with Venus either enhances or spoils.

When every factor has a counter-factor, no outcome can count against the reading. The question to ask of each "yes, but" is: *what life outcome would this claim forbid?* If the answer is "none", the claim is not a prediction.

### 4.4 The key empirical tests

- **Carlson (1985, *Nature* 318:419–425).** This was a double-blind test whose protocol astrologers helped design and approved. They matched natal charts to California Psychological Inventory profiles at chance level, despite predicting beforehand that they would do far better. Ertel (2009) argued for a small effect in one ranking sub-test. Even on his reading the effect is far below what practitioners claim.
- **Dean & Kelly (2003, *J. Consciousness Studies* 10(6–7)).** About 2,100 Londoners born 3–9 March 1958, often minutes apart, were followed on 110 variables (IQ, personality, behaviour, occupation) at ages 11, 16 and 23. The "time twins" were **no more alike than unrelated people**.
  - This is the most direct test of this report's own premise. The report assumes that a few minutes of birth time change the D9, D10 and KP readings. Dean & Kelly found that minutes, and even days, made no measurable difference.
- **Gauquelin (1955 onward).** This is the one striking positive result. Mars in the sectors just past rising or culmination was more common in the charts of eminent sports champions (the "Mars effect").
  - It is contested. The Comité Para (1976) found the effect but disputed its cause. The US test by CSICOP (1979–80) did not find it. The French CFEPP study (published 2000) did not find it either. Critics have raised data-selection issues.
  - **Even taken at face value, it supports none of this reading's techniques.** Gauquelin himself found nothing for signs, aspects in the usual sense, or houses as astrologers use them.
- **Also relevant:**
  - Narlikar et al. (2009, *Current Science* 96:641): Vedic astrologers could not tell the charts of gifted children from those of children with intellectual disabilities better than chance.
  - Large sun-sign and personality datasets (e.g. Hartmann, Reuter & Nyborg 2006, *Personality and Individual Differences*) show no link.

### 4.5 What would count as a fair test of this reading

1. **Pre-register.** The table in §5 is dated 18 Oct 2026. Do not edit it after the fact. Score each row when its window closes, and count misses exactly as hits are counted.
2. **Define the hit before the window opens.** "Career restructuring" must mean something observable: a new employer, a role or title change, or a pivot or shutdown of the venture. It must not mean whatever happened.
3. **Compare with base rates.** Many predictions here describe things that happen to most people aged 27–35, such as job moves, relationships and relocations. A hit is impressive only if the predicted window is narrow compared with how often such events occur. Better still, score against a **decoy**: the same predictions read from a chart cast six hours later, or a month earlier, and see whether the real chart beats it.
4. **Blind the retrodictions.** For ch. 07, Udai first writes his own dated turning points for 2003–2026, with no reading in front of him. A third party then scores how well ch. 07's period descriptions match them, against the descriptions for two decoy birth times. This is the individual-scale version of Carlson.
5. **Use the rectification honestly.** If the dated events push the birth time to 21:45, the D9, D10 and KP readings change. The pre-registered predictions, though, are **not re-scored** after rectification. Otherwise rectification becomes a way to absorb misses.
6. **Hold the reading as what it says it is.** As 00 L156 and 06 B12 put it, this is an accurate account of what the traditions say about this sky. It is a vocabulary for reflection and a calendar for planned reviews. It is not a validated forecast. Exploring a tradition with open eyes is a perfectly good reason to read it.

---

## 5. Pre-registration table

*Registered 18 Oct 2026. Dates are at the recorded 21:35 IST. Rows marked ±3 wk carry the Vimshottari birth-time band. Score each row Hit, Miss or Unclear when its window closes. Record the evidence at the time. Rows P1–P2 are retrodictions and can be scored now, but Udai should write his own account first, before re-reading chs. 04 and 07.*

| ID | Claim (source) | Window | Counts as a hit | Base-rate caution |
|---|---|---|---|---|
| **P1** | The Jupiter mahadasha begins: a felt change of chapter (study, mentor, move, role) (03 L261, 04 L189, 07 L236) | **7 Sep – 25 Oct 2021** (±15 min band) | A datable turning point inside the window. If it is within ±3 days of 7 Sep, 1 Oct or 25 Oct, record which one, since that also rectifies the birth time | Age 22 is graduation and first-job age for most of the cohort |
| **P2** | The Ju/Me antardasha begins: contracts, study, partnership agreements (04 L38–41) | **9 May – 26 Jun 2026** | A signed agreement, a course or study start, or a partnership formed inside the window | Moderate |
| **P3** | Most constructive near-term stretch: agreements, recognition, creative or partnership milestones. Ju/Me/Ve pratyantar, Venus Mudda, and Jupiter stationing on Venus on 13 Apr 2027 (08 L265, L351, L402) | **14 Nov 2026 – 30 Apr 2027**, peak 1 Mar – 30 Apr 2027 | At least one signed partnership, contract, funding agreement or public creative milestone with its date inside the peak window | High for an active founder; score the *peak* window only |
| **P4** | Identity or role redefinition: Rahu on the lagna from 25 Nov 2026, and the nodal reversal exact 21–24 May 2027 (04 L42, 11 L22–33) | **25 Nov 2026 – 16 Sep 2027** | A change of title, field, company or public identity (a rebrand, a pivot, a new role) | High; must be a change made *within* the window, not a continuation |
| **P5** | Heavier home, property or family responsibility as Saturn enters Aries and rises in the annual chart (08 L169–173, L375–379; 04 L156) | **3 Jun – 20 Oct 2027** | A concrete new obligation: a property purchase or move, a family caregiving duty, or a major home-related commitment | Moderate |
| **P6** | 2027–29 is the testing stretch: Saturn ashtama and return, Yogini Sankata (00 L110, 04 L47) | **3 Jun 2027 – 8 Aug 2029** | At the end of 2032, Udai ranks each year 2026–2032 by difficulty *without re-reading this file*. Hit if his two hardest years fall in 2027–29 | Self-report; write the ranking before scoring |
| **P7** | Career restructuring, then a climb: 10th-house double transits with the Saturn return (04 L157, 06 L235) | **26 Dec 2028 – 24 Jan 2030** | A job change, a role or title change, or a venture pivot, restructuring or exit beginning inside the window | High at age 29–30; the "then a climb" part is scored under P8 |
| **P8** | The strongest career and gains window: Ju/Ve, Jupiter in Scorpio, double transits on the 5th, 7th and 11th (00 L111, 04 L49–52, 12 L23) | **13 Aug 2029 – 13 Apr 2032** (start band 16 Jul – 7 Sep 2029) | The single largest professional advance or financial gain of 2026–2035 *begins* inside this window. Decide in 2036 | It covers 2.7 of the 10 years, so a chance hit is about 27% |
| **P9** | Partnership or commitment event in the 7th-house double-transit windows inside Ju/Ve, or the second window with Ju/Ma (04 L138, L144; 06 L211–212) | **23 Sep 2030 – 16 Feb 2031 · 14 Jun – 14 Oct 2031 · 5 Mar – 30 May 2032 · 13 Jul 2034 – 5 Apr 2035** | An engagement, marriage or equivalent formal long-term commitment dated inside one of these windows. If already committed before 2030, score a formal milestone (wedding, cohabitation, child decision) instead | The windows total about 26 months; compare with the base rate for ages 31–36 |
| **P10** | Gains via networks or the 11th house: 11th-house double transits with Jupiter and Rahu in Scorpio (06 L258, 12 L12) | **23 Sep 2030 – 16 Feb 2031 · 14 Jun – 14 Oct 2031** | A raise, funding round, sale or other income event at least 25% above the previous 12 months' run-rate, dated inside the windows | About 9 months in total; a narrow and therefore fairly informative test |

**Not registered, but worth recording.** The Saturn mahadasha from 1 Oct 2037 (±3 weeks) and the second Sade Sati (27 Aug 2036 – 11 Dec 2043) are described as "a demanding apprenticeship, then slow-built authority". That is too far off, and too vague, to score well.

**Retrodiction to score blind:** "2009–11 stand out in memory as the heavy years" (07 L53). Udai rates each year 2005–2015 first, then checks.

---

## 6. Fix list: the most important errors

In priority order. Line numbers are as of 18 Oct 2026, 06:21.

1. **`00-master-map.md` L27**, plus `06-doshas-and-hard-questions.md` L11 and `09-vargas-deep-dive.md` L8. The robust window is **20:51 – 22:41**, not 21:05 – 22:41.
2. **`05-western-cycles-philosophers.md` L61 and L105.** These are sidereal Jupiter dates in a tropical chapter. Use the tropical ones: Venus 10 Sep 2026; Asc opposition 24 Jul 2026; returns 12 May 2023 and 26 Apr 2035.
3. **`05-western-cycles-philosophers.md` L20 and L165.** Saturn rules the rising sign in *both* zodiacs only from −43 to +87 min, not from −143.
4. **`05-western-cycles-philosophers.md` L101 and L102, and L68.** The tropical Saturn return is **26 Apr 2029**. The squares fall on 13, 19 and 23 May 2029. The May 2029 square belongs in the **age-29** row.
5. **`00-master-map.md` L40–46.** Remove "Saturn is exalted in the D10" from the neecha-bhanga list. Harmonise with `01-parashari.md` L31–41, and fix `04-timing.md` L30.
6. **`01-parashari.md` L115.** "11th > 10th > 1st" fails (25 < 27).
7. **`01-parashari.md` L102.** Five planets are in kendras, not four.
8. **`01-parashari.md` L54 and L160.** The neecha-bhanga conditions are not independent: three placements satisfy five or six rules.
9. **`08-annual-and-near-term.md` L270, L353 and L380.** Jupiter is not "on the natal Moon" in Nov 2027 – Apr 2028. The exact conjunctions are 16 Dec 2028, 10 Apr 2029 and 16 Aug 2029. The sign-level wording in `04-timing.md` L109 and L156 should be fixed the same way.
10. **`08-annual-and-near-term.md` L84 and L88.** The Sagittarius night tri-rashi pati is Jupiter (per the Neelakanthi table). Saturn stays year lord, but with one office. Verify against JHora.
11. **`12-talis-business-reading.md` L22.** Rahu enters the lagna on **25 Nov 2026**, not 26 Nov. The Jupiter sequence in L22–23 also needs correcting.
12. **`06-doshas-and-hard-questions.md` L128, L129 and L131, and `07-retrospective-1999-2026.md` L113, L132 and L133.** Saturn's ingresses in IST are 26 Jan 2017, 29 Mar 2025, **27 Aug 2036** and 11 Dec 2043.
13. **`00-master-map.md` L111 and L131, and `02-jaimini.md` L284.** "All systems / all four variants agree" overstates. Yogini's Sankata mahadasha dissents, and the SJC variants put Leo in the 2030s.
14. **`astro/chart.py:164`.** The 7-karaka label list should read `PK`, not `PiK`. Then regenerate `data-pack.md` L13.
15. **Convention.** Put every chapter on IST dates. Most of the remaining one-day disagreements (Saturn into Aries 2 vs 3 Jun 2027, the Jupiter return 27 vs 28 Apr 2035) disappear.
