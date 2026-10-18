"""Planetary and house strength: Shadbala, Ishta/Kashta phala, Vimshopaka bala and
Bhava bala, after BPHS ch. 27-28 and B.V. Raman, *Graha and Bhava Balas*.

All bala values are in virupas (shashtiamsas); 60 virupas = 1 rupa.

Where the texts allow more than one reading, `Options` switches between them. The
defaults are the combination that comes closest to Parashara's Light 9.0 on the reference
chart (see tests/test_strength.py and reports/udai/data-pack-extra.md).
"""
from __future__ import annotations

import math
from dataclasses import dataclass, replace

import swisseph as swe

from .constants import (DEBILITATION, MOOLATRIKONA, NATURAL_ENEMIES, NATURAL_FRIENDS,
                        SIGN_LORD)
from .special import HORA_ORDER, WEEKDAY_LORD, sripati, sun_times
from .vargas import varga_sign

SEVEN = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
REQUIRED_RUPAS = {"Sun": 5, "Moon": 6, "Mars": 5, "Mercury": 7, "Jupiter": 6.5,
                  "Venus": 5.5, "Saturn": 5}
NAISARGIKA = {"Sun": 60, "Moon": 360 / 7, "Venus": 300 / 7, "Jupiter": 240 / 7,
              "Mercury": 180 / 7, "Mars": 120 / 7, "Saturn": 60 / 7}
MALE, NEUTER, FEMALE = {"Sun", "Mars", "Jupiter"}, {"Mercury", "Saturn"}, {"Moon", "Venus"}
SAPTAVARGAS = (1, 2, 3, 7, 9, 12, 30)
# Saptavargaja points: moolatrikona, own, great friend, friend, neutral, enemy, great enemy
SV_POINTS = {"MT": 45, "Own": 30, "Great friend": 22.5, "Friend": 15, "Neutral": 7.5,
             "Enemy": 3.75, "Great enemy": 1.875}


@dataclass(frozen=True)
class Options:
    houses: str = "sign"            # kendradi bala: "sign" (whole sign), "sripati", "equal"
    mt_in_vargas: bool = False      # moolatrikona (45) also in divisional charts, by sign
    natonnata: str = "apparent"     # "apparent" (Sun's hour angle) or "sunset_mid" (night mid)
    moon_paksha_double: bool = True
    mercury_benefic: bool = True    # Mercury conjunct only Venus (benefic) and Rahu here
    hora: str = "equal"             # "equal" 1-hour horas from sunrise, or "unequal"
    abda_masa: str = "ahargana"     # "ahargana" (Raman's Kali-day count) or "none"
    ayana: str = "ecliptic"         # declination of the ecliptic point, or "true" (with latitude)
    sun_ayana_double: bool = True
    sun_moon_chesta: bool = True    # Sun's chesta = ayana bala, Moon's = paksha bala
    chesta: str = "mean"            # "mean" (seeghra kendra from modern mean elements)
    drik_full_jup_mer: bool = False # add Jupiter's and Mercury's aspects in full, not 1/4
    special_aspects: str = "raman"  # extra virupas for Ma 4/8, Ju 5/9, Sa 3/10


# ------------------------------------------------------------------ helpers
def _arc(a, b):
    d = abs(a - b) % 360
    return 360 - d if d > 180 else d


def compound(chart, a: str, b: str) -> str:
    return chart.compound_relation(a, b)


def _jd_tt(chart):
    return chart.jd + swe.deltat(chart.jd)


# ------------------------------------------------------------------ sthana bala
def uchcha(chart, p):
    s, d = DEBILITATION[p]
    return _arc(chart.points[p].lon, s * 30 + d) / 3


def varga_dignity(chart, p, n, opt: Options) -> str:
    lon = chart.points[p].lon
    s = varga_sign(lon, n)
    mt = MOOLATRIKONA.get(p)
    if mt and s == mt[0]:
        if n == 1:
            if mt[1] <= lon % 30 < mt[2]:
                return "MT"
        elif opt.mt_in_vargas:
            return "MT"
    lord = SIGN_LORD[s]
    if lord == p:
        return "Own"
    return compound(chart, p, lord)


def saptavargaja(chart, p, opt: Options):
    return sum(SV_POINTS[varga_dignity(chart, p, n, opt)] for n in SAPTAVARGAS)


def ojayugma(chart, p):
    rs = chart.points[p].sign
    ns = varga_sign(chart.points[p].lon, 9)
    want_even = p in ("Moon", "Venus")
    return sum(15 for s in (rs, ns) if (s % 2 == 1) == want_even)


def bhava_of(chart, p, scheme):
    if scheme == "sign":
        return chart.house_of(p)
    if scheme == "equal":   # equal houses with the lagna degree as the middle of house 1
        return int(((chart.points[p].lon - chart.asc.lon + 15) % 360) // 30) + 1
    return sripati(chart)["house"][p]


def kendradi(chart, p, opt: Options):
    h = bhava_of(chart, p, opt.houses)
    return 60 if h in (1, 4, 7, 10) else 30 if h in (2, 5, 8, 11) else 15


def drekkana(chart, p):
    k = int(chart.points[p].deg // 10)
    want = 0 if p in MALE else 1 if p in NEUTER else 2
    return 15 if k == want else 0


# ------------------------------------------------------------------ dig bala
def dig(chart, p):
    asc, mc = chart.asc.lon, chart.mc.lon
    weak = {"Sun": mc + 180, "Mars": mc + 180, "Jupiter": asc + 180, "Mercury": asc + 180,
            "Moon": mc, "Venus": mc, "Saturn": asc}[p]
    return _arc(chart.points[p].lon, weak) / 3


# ------------------------------------------------------------------ kala bala
def natonnata(chart, p, opt: Options):
    if p == "Mercury":
        return 60.0
    if opt.natonnata == "apparent":
        lst = swe.sidtime(chart.jd) * 15 + chart.lon
        ra = swe.calc_ut(chart.jd, swe.SUN, swe.FLG_SWIEPH | swe.FLG_EQUATORIAL)[0][0]
        ha = (lst - ra) % 360                   # 180 at apparent midnight
        from_midnight = abs(ha - 180)           # degrees of time; 180 = noon
    else:
        t = sun_times(chart)
        mid = (t["sunset"] + t["next_sunrise"]) / 2 if not t["is_day"] else \
            (t["sunrise"] + (t["sunrise"] - 1 + (t["sunset"] - t["sunrise"]))) / 2
        from_midnight = min(abs(chart.jd - mid) * 360, 180)
    day = from_midnight / 3                     # 0 at midnight, 60 at noon
    return day if p in ("Sun", "Jupiter", "Venus") else 60 - day


def is_benefic(chart, p, opt: Options):
    if p in ("Jupiter", "Venus"):
        return True
    if p == "Moon":
        return (chart.points["Moon"].lon - chart.points["Sun"].lon) % 360 < 180
    if p == "Mercury":
        return opt.mercury_benefic
    return False


def paksha(chart, p, opt: Options):
    a = _arc(chart.points["Moon"].lon, chart.points["Sun"].lon) / 3
    if p == "Moon":
        return a * (2 if opt.moon_paksha_double else 1)
    benefic = p in ("Jupiter", "Venus") or (p == "Mercury" and opt.mercury_benefic)
    return a if benefic else 60 - a


def tribhaga(chart, p):
    if p == "Jupiter":
        return 60
    t = sun_times(chart)
    if t["is_day"]:
        k = int(3 * (chart.jd - t["sunrise"]) / (t["sunset"] - t["sunrise"]))
        lord = ["Mercury", "Sun", "Saturn"][min(k, 2)]
    else:
        k = int(3 * (chart.jd - t["sunset"]) / (t["next_sunrise"] - t["sunset"]))
        lord = ["Moon", "Venus", "Mars"][min(k, 2)]
    return 60 if p == lord else 0


KALI_EPOCH_JD = 588465.5   # 18 Feb 3102 BCE (Julian), a Friday: Raman's ahargana epoch


def abda_masa_lords(chart):
    """Year and month lords by Raman's ahargana method: the weekday lord of the first day
    of the current 360-day 'year' and 30-day 'month' counted from the Kali epoch."""
    a = int(chart.jd + chart.tz / 24 + 0.5 - (KALI_EPOCH_JD + 0.5))
    fri = 5
    year = WEEKDAY_LORD[(fri + (a // 360) * 360) % 7]
    month = WEEKDAY_LORD[(fri + (a // 30) * 30) % 7]
    return year, month


def hora_lord(chart, opt: Options):
    t = sun_times(chart)
    if opt.hora == "equal":
        k = int((chart.jd - t["sunrise"]) * 24)
    elif t["is_day"]:
        k = int(12 * (chart.jd - t["sunrise"]) / (t["sunset"] - t["sunrise"]))
    else:
        k = 12 + int(12 * (chart.jd - t["sunset"]) / (t["next_sunrise"] - t["sunset"]))
    first = HORA_ORDER.index(t["vara_lord"])
    return HORA_ORDER[(first + k) % 7]


def lords_bala(chart, p, opt: Options):
    t = sun_times(chart)
    out = 0
    if opt.abda_masa == "ahargana":
        y, m = abda_masa_lords(chart)
        out += 15 * (p == y) + 30 * (p == m)
    out += 45 * (p == t["vara_lord"]) + 60 * (p == hora_lord(chart, opt))
    return out


def declination(chart, p, opt: Options):
    pid = {"Sun": swe.SUN, "Moon": swe.MOON, "Mars": swe.MARS, "Mercury": swe.MERCURY,
           "Jupiter": swe.JUPITER, "Venus": swe.VENUS, "Saturn": swe.SATURN}[p]
    if opt.ayana == "true":
        return swe.calc_ut(chart.jd, pid, swe.FLG_SWIEPH | swe.FLG_EQUATORIAL)[0][1]
    trop = (chart.points[p].lon + chart.ayanamsa) % 360
    eps = swe.calc_ut(chart.jd, swe.ECL_NUT)[0][0]
    return math.degrees(math.asin(math.sin(math.radians(eps)) * math.sin(math.radians(trop))))


def ayana(chart, p, opt: Options, doubled=True):
    k = declination(chart, p, opt)
    if p in ("Moon", "Saturn"):
        k = -k
    elif p == "Mercury":
        k = abs(k)
    v = (24 + k) / 48 * 60
    return v * 2 if (p == "Sun" and doubled and opt.sun_ayana_double) else v


# ------------------------------------------------------------------ chesta bala
def mean_longitudes(chart) -> dict:
    """Mean heliocentric longitudes (tropical, mean equinox of date), Meeus table 31.A,
    plus the mean Sun. Converted to the chart's sidereal zodiac."""
    T = (_jd_tt(chart) - 2451545.0) / 36525
    L = {"Mercury": 252.250906 + 149474.0722491 * T + 0.00030350 * T * T,
         "Venus": 181.979801 + 58519.2130302 * T + 0.00031014 * T * T,
         "Earth": 100.466457 + 36000.7698278 * T + 0.00030322 * T * T,
         "Mars": 355.433000 + 19141.6964471 * T + 0.00031052 * T * T,
         "Jupiter": 34.351519 + 3036.3027748 * T + 0.00022330 * T * T,
         "Saturn": 50.077444 + 1223.5110686 * T + 0.00051908 * T * T}
    L["Sun"] = L["Earth"] + 180
    return {k: (v - chart.ayanamsa) % 360 for k, v in L.items()}


def chesta(chart, p, opt: Options):
    if p == "Sun":
        return ayana(chart, "Sun", opt, doubled=False)
    if p == "Moon":
        return paksha(chart, "Moon", replace(opt, moon_paksha_double=False))
    m = mean_longitudes(chart)
    if p in ("Mercury", "Venus"):
        seeghra, madhya = m[p], m["Sun"]
    else:
        seeghra, madhya = m["Sun"], m[p]
    true = chart.points[p].lon
    # average of mean and true planet, taken along the short arc
    avg = (madhya + ((true - madhya + 180) % 360 - 180) / 2) % 360
    kendra = (seeghra - avg) % 360
    if kendra > 180:
        kendra = 360 - kendra
    return kendra / 3


# ------------------------------------------------------------------ drik bala
def drishti(angle: float, aspecting: str, special: str = "raman") -> float:
    """Sphuta drishti (BPHS 26) of a planet at distance `angle` (aspected - aspecting)."""
    d = angle % 360
    if d < 30 or d >= 300:
        v = 0.0
    elif d < 60:
        v = (d - 30) / 2
    elif d < 90:
        v = d - 60 + 15
    elif d < 120:
        v = (120 - d) / 2 + 30
    elif d < 150:
        v = 150 - d
    elif d < 180:
        v = (d - 150) * 2
    else:
        v = (300 - d) / 2
    if special == "raman":
        if aspecting == "Saturn" and (60 <= d < 90 or 270 <= d < 300):
            v += 45
        elif aspecting == "Jupiter" and (120 <= d < 150 or 240 <= d < 270):
            v += 30
        elif aspecting == "Mars" and (90 <= d < 120 or 210 <= d < 240):
            v += 15
    return v


def drik(chart, p, opt: Options):
    tot = 0.0
    target = chart.points[p].lon
    for q in SEVEN:
        if q == p:
            continue
        v = drishti(target - chart.points[q].lon, q, opt.special_aspects)
        sign = 1 if is_benefic(chart, q, opt) else -1
        full = opt.drik_full_jup_mer and (q == "Jupiter" or (q == "Mercury" and sign > 0))
        tot += sign * v * (1 if full else 0.25)
    return tot


# ------------------------------------------------------------------ yuddha
def yuddha(chart, pre: dict) -> dict:
    """Graha yuddha among Mars..Saturn within 1 degree: the planet with the more northern
    latitude wins and takes the difference of the two planets' strength so far."""
    out = {p: 0.0 for p in SEVEN}
    star = ["Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
    pid = {"Mars": swe.MARS, "Mercury": swe.MERCURY, "Jupiter": swe.JUPITER,
           "Venus": swe.VENUS, "Saturn": swe.SATURN}
    for i, a in enumerate(star):
        for b in star[i + 1:]:
            if _arc(chart.points[a].lon, chart.points[b].lon) < 1:
                la = swe.calc_ut(chart.jd, pid[a], chart.flags)[0][1]
                lb = swe.calc_ut(chart.jd, pid[b], chart.flags)[0][1]
                w, l = (a, b) if la > lb else (b, a)
                diff = abs(pre[a] - pre[b])
                out[w] += diff
                out[l] -= diff
    return out


# ------------------------------------------------------------------ shadbala
def shadbala(chart, opt: Options = Options()) -> dict:
    """Per-planet breakdown in virupas, total in rupas and the ratio to the minimum."""
    rows = {}
    for p in SEVEN:
        r = {"uchcha": uchcha(chart, p), "saptavargaja": saptavargaja(chart, p, opt),
             "ojayugma": ojayugma(chart, p), "kendradi": kendradi(chart, p, opt),
             "drekkana": drekkana(chart, p)}
        r["sthana"] = sum(r[k] for k in ("uchcha", "saptavargaja", "ojayugma", "kendradi",
                                          "drekkana"))
        r["dig"] = dig(chart, p)
        r["natonnata"] = natonnata(chart, p, opt)
        r["paksha"] = paksha(chart, p, opt)
        r["tribhaga"] = tribhaga(chart, p)
        r["lords"] = lords_bala(chart, p, opt)
        r["ayana"] = ayana(chart, p, opt)
        rows[p] = r
    pre = {p: r["sthana"] + r["dig"] + r["natonnata"] + r["paksha"] + r["tribhaga"]
           + r["lords"] + r["ayana"] for p, r in rows.items()}
    yud = yuddha(chart, pre)
    for p, r in rows.items():
        r["yuddha"] = yud[p]
        r["kala"] = sum(r[k] for k in ("natonnata", "paksha", "tribhaga", "lords", "ayana",
                                        "yuddha"))
        r["chesta"] = chesta(chart, p, opt) if (p not in ("Sun", "Moon") or opt.sun_moon_chesta) else 0
        r["naisargika"] = NAISARGIKA[p]
        r["drik"] = drik(chart, p, opt)
        r["total"] = r["sthana"] + r["dig"] + r["kala"] + r["chesta"] + r["naisargika"] + r["drik"]
        r["rupas"] = r["total"] / 60
        r["ratio"] = r["rupas"] / REQUIRED_RUPAS[p]
        cb = chesta(chart, p, opt)
        r["ishta"] = math.sqrt(max(r["uchcha"], 0) * max(cb, 0))
        r["kashta"] = math.sqrt(max(60 - r["uchcha"], 0) * max(60 - cb, 0))
    return rows


# ------------------------------------------------------------------ vimshopaka
VIMSHOPAKA_SCHEMES = {
    "shadvarga": {1: 6, 2: 2, 3: 4, 9: 5, 12: 2, 30: 1},
    "saptavarga": {1: 5, 2: 2, 3: 3, 7: 2.5, 9: 4.5, 12: 2, 30: 1},
    "dashavarga": {1: 3, 2: 1.5, 3: 1.5, 7: 1.5, 9: 1.5, 10: 1.5, 12: 1.5, 16: 1.5,
                   30: 1.5, 60: 5},
    "shodashavarga": {1: 3.5, 2: 1, 3: 1, 4: 0.5, 7: 0.5, 9: 3, 10: 0.5, 12: 0.5, 16: 2,
                      20: 0.5, 24: 0.5, 27: 0.5, 30: 1, 40: 0.5, 45: 0.5, 60: 4},
}
# BPHS 7: own/exalted/moolatrikona 20, great friend 18, friend 15, neutral 10,
# enemy 7, great enemy 5 (each scaled by the varga's weight / 20)
VIMSHOPAKA_POINTS = {"Own": 20, "Great friend": 18, "Friend": 15, "Neutral": 10,
                     "Enemy": 7, "Great enemy": 5}


def vimshopaka(chart) -> dict:
    from .constants import EXALTATION
    out = {}
    for p in SEVEN:
        lon = chart.points[p].lon
        row = {}
        for name, scheme in VIMSHOPAKA_SCHEMES.items():
            tot = 0.0
            for n, w in scheme.items():
                s = varga_sign(lon, n)
                lord = SIGN_LORD[s]
                if lord == p or s == EXALTATION[p][0] or s == MOOLATRIKONA[p][0]:
                    pts = 20
                else:
                    pts = VIMSHOPAKA_POINTS[compound(chart, p, lord)]
                tot += pts * w / 20
            row[name] = tot
        out[p] = row
    return out


# ------------------------------------------------------------------ bhava bala
NARA = {2, 5, 6, 10}          # Gemini, Virgo, Libra, Aquarius (+ first half of Sagittarius)
JALA = {3, 11}                # Cancer, Pisces (+ second half of Capricorn)
KEETA = {7}                   # Scorpio
# all others (Aries, Taurus, Leo, 2nd half Sag, 1st half Cap) are chatushpada (quadrupeds)


def _bhava_sign_class(lon):
    s, d = int(lon // 30), lon % 30
    if s in NARA or (s == 8 and d < 15):
        return "nara"
    if s in JALA or (s == 9 and d >= 15):
        return "jala"
    if s in KEETA:
        return "keeta"
    return "chatushpada"


def bhava_madhyas(chart, scheme="equal"):
    if scheme == "equal":
        return [(chart.asc.lon + 30 * i) % 360 for i in range(12)]
    return sripati(chart)["madhya"]


def bhava_bala(chart, opt: Options = Options(), scheme: str = "equal",
               sb: dict | None = None, occupation: bool = False) -> dict:
    """Bhava bala (Raman ch. on bhava bala) = bhavadhipati bala (shadbala of the lord)
    + bhava digbala + bhava drishti bala, in virupas."""
    sb = sb or shadbala(chart, opt)
    madhya = bhava_madhyas(chart, scheme)
    out = {}
    for i, m in enumerate(madhya):
        lord = SIGN_LORD[int(m // 30)]
        adhipati = sb[lord]["total"]
        cls = _bhava_sign_class(m)
        # strongest house for each class: nara 1st, jala 4th, keeta 7th, chatushpada 10th;
        # take the distance from the opposite (weakest) house madhya
        weak = {"nara": madhya[6], "jala": madhya[9], "keeta": madhya[0],
                "chatushpada": madhya[3]}[cls]
        digb = _arc(m, weak) / 3
        dr = 0.0
        for q in SEVEN:
            v = drishti(m - chart.points[q].lon, q, opt.special_aspects)
            sign = 1 if is_benefic(chart, q, opt) else -1
            full = q in ("Jupiter", "Mercury")
            dr += sign * v * (1 if full else 0.25)
        occ = 0
        if occupation:
            for q in SEVEN:
                if int(((chart.points[q].lon - m + 15) % 360) // 30) == 0:
                    occ += 60 if q in ("Jupiter", "Mercury") else -60 if q in ("Saturn", "Mars", "Sun") else 0
        total = adhipati + digb + dr + occ
        out[i + 1] = {"madhya": m, "lord": lord, "adhipati": adhipati, "dig": digb,
                      "drishti": dr, "occupation": occ, "total": total, "rupas": total / 60}
    return out
