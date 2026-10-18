"""Special points: sunrise/sunset, upagrahas, sphutas, special lagnas, Yogi/Avayogi,
and Sripati (bhava chalit) houses.

Conventions are set to reproduce Parashara's Light 9.0 (PL) where we could check:
  * Sunrise/sunset are "Hindu" ones: the centre of the disc on the true horizon, with no
    refraction (swe.BIT_HINDU_RISING). With these, Gulika and Mandi match PL to the arcminute.
  * Gulika = lagna rising at the END of Saturn's portion (1/8 of the day or night, whose
    portions start from the weekday lord by day and from the 5th weekday lord by night).
  * Mandi = lagna rising at the Phaladeepika/BPHS ghati after sunrise (day) or sunset
    (night), scaled to the actual length of that day or night (30 "ghatis").
  * PL's "Be" point is the Beeja sphuta (Sun + Venus + Jupiter), not the Bhrigu Bindu.
"""
from __future__ import annotations

import swisseph as swe

from .constants import NAK_LORD, NAK_SPAN, SIGN_LORD

# Weekday lords, index 0 = Sunday
WEEKDAY_LORD = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
# Chaldean order used for horas (each hour's lord is the next in this list)
HORA_ORDER = ["Sun", "Venus", "Mercury", "Moon", "Saturn", "Jupiter", "Mars"]

# Ghati (of 30 in a day/night) at which Mandi rises, by weekday (Sun..Sat). Phaladeepika 25.
MANDI_DAY_GHATI = [26, 22, 18, 14, 10, 6, 2]
MANDI_NIGHT_GHATI = [10, 6, 2, 26, 22, 18, 14]


# ---------------------------------------------------------------- sun times
def _event(chart, jd, rsmi, hindu=True):
    flag = swe.BIT_HINDU_RISING if hindu else 0
    return swe.rise_trans(jd, swe.SUN, rsmi | flag, (chart.lon, chart.lat, 0),
                          1013.25, 15, swe.FLG_SWIEPH)[1][0]


def sun_times(chart, hindu: bool = True) -> dict:
    """Sunrise before birth, the sunset after that sunrise, and the next sunrise (JD UT).

    `is_day` says whether birth falls between sunrise and sunset. The Vedic weekday runs
    from sunrise to sunrise, so a birth before sunrise belongs to the previous weekday.
    """
    if getattr(chart, "_sun_times", {}).get(hindu):
        return chart._sun_times[hindu]
    rise = _event(chart, chart.jd - 1.2, swe.CALC_RISE, hindu)
    while True:  # last sunrise at or before birth
        nxt = _event(chart, rise + 0.01, swe.CALC_RISE, hindu)
        if nxt > chart.jd:
            break
        rise = nxt
    sset = _event(chart, rise + 0.01, swe.CALC_SET, hindu)
    rise2 = _event(chart, sset + 0.01, swe.CALC_RISE, hindu)
    # swe.day_of_week: 0 = Monday. Convert to 0 = Sunday, using the sunrise's civil date.
    wd = (swe.day_of_week(rise + chart.tz / 24) + 1) % 7
    out = {"sunrise": rise, "sunset": sset, "next_sunrise": rise2,
           "is_day": chart.jd < sset, "weekday": wd, "vara_lord": WEEKDAY_LORD[wd]}
    if not hasattr(chart, "_sun_times"):
        chart._sun_times = {}
    chart._sun_times[hindu] = out
    return out


def asc_at(chart, jd: float) -> float:
    """Sidereal ascendant at a given JD (UT) for the chart's place."""
    return swe.houses_ex(jd, chart.lat, chart.lon, b"P", chart.flags)[1][0] % 360


def jd_to_local(chart, jd):
    from datetime import datetime, timedelta
    y, m, d, h = swe.revjul(jd)
    return datetime(y, m, d) + timedelta(hours=h + chart.tz)


# ---------------------------------------------------------------- upagrahas
def gulika_mandi(chart) -> dict:
    t = sun_times(chart)
    wd = t["weekday"]
    if t["is_day"]:
        start, length, first = t["sunrise"], t["sunset"] - t["sunrise"], wd
        mandi_gh = MANDI_DAY_GHATI[wd]
    else:
        start, length, first = t["sunset"], t["next_sunrise"] - t["sunset"], (wd + 4) % 7
        mandi_gh = MANDI_NIGHT_GHATI[wd]
    part = length / 8
    k = (6 - first) % 7  # which portion (0-based) Saturn rules
    sat_start = start + k * part
    return {
        "Gulika": asc_at(chart, sat_start + part),                 # end of Saturn's portion (PL)
        "Gulika (start of portion)": asc_at(chart, sat_start),
        "Gulika (middle of portion)": asc_at(chart, sat_start + part / 2),
        "Mandi": asc_at(chart, start + length * mandi_gh / 30),    # Phaladeepika ghati (PL)
        "saturn_portion": (sat_start, sat_start + part),
    }


def sun_upagrahas(chart) -> dict:
    """BPHS ch. 3: the five 'non-luminous' points derived from the Sun."""
    sun = chart.points["Sun"].lon
    dhuma = (sun + 133 + 20 / 60) % 360
    vyatipata = (360 - dhuma) % 360
    parivesha = (vyatipata + 180) % 360
    indrachapa = (360 - parivesha) % 360
    upaketu = (indrachapa + 16 + 40 / 60) % 360
    return {"Dhuma": dhuma, "Vyatipata": vyatipata, "Parivesha": parivesha,
            "Indrachapa": indrachapa, "Upaketu": upaketu}


# ---------------------------------------------------------------- sphutas
def sphutas(chart) -> dict:
    p = {k: v.lon for k, v in chart.points.items()}
    return {
        "Beeja": (p["Sun"] + p["Venus"] + p["Jupiter"]) % 360,         # PL "Be"
        "Kshetra": (p["Moon"] + p["Mars"] + p["Jupiter"]) % 360,
        "Bhrigu Bindu": ((p["Rahu"] + ((p["Moon"] - p["Rahu"]) % 360) / 2)) % 360,
    }


# ---------------------------------------------------------------- special lagnas
INDU_KALAS = {"Sun": 30, "Moon": 16, "Mars": 6, "Mercury": 8, "Jupiter": 10,
              "Venus": 12, "Saturn": 1}


def special_lagnas(chart) -> dict:
    t = sun_times(chart)
    sun_rise = swe.calc_ut(t["sunrise"], swe.SUN, chart.flags)[0][0]
    hours = (chart.jd - t["sunrise"]) * 24
    ghatis = hours * 2.5
    hora = (sun_rise + hours * 30) % 360          # 1 sign per hora (2.5 ghatis)
    ghatika = (sun_rise + ghatis * 30) % 360      # 1 sign per ghati
    bhava = (sun_rise + hours * 15) % 360         # 1 sign per 5 ghatis

    # Pranapada (BPHS 3): 1 sign per 15 vighatis, counted from a point fixed by the Sun's sign
    sun = chart.points["Sun"]
    vighatis = ghatis * 60
    base = sun.lon + [0, 240, 120][sun.sign % 3]   # movable / fixed / dual
    pranapada = (base + vighatis * 2) % 360

    # Indu lagna: kalas of 9th lords from lagna and Moon, remainder by 12, counted from Moon
    moon = chart.points["Moon"]
    l9 = SIGN_LORD[(chart.asc.sign + 8) % 12]
    m9 = SIGN_LORD[(moon.sign + 8) % 12]
    r = (INDU_KALAS[l9] + INDU_KALAS[m9]) % 12 or 12
    indu = (moon.sign + r - 1) % 12

    # Sri lagna: lagna + the elapsed fraction of the Moon's nakshatra, scaled to 360
    frac = (moon.lon % NAK_SPAN) / NAK_SPAN
    sri = (chart.asc.lon + frac * 360) % 360

    return {"Hora Lagna": hora, "Ghatika Lagna": ghatika, "Bhava Lagna": bhava,
            "Pranapada": pranapada, "Indu Lagna sign": indu, "Sri Lagna": sri,
            "Varnada Lagna sign": varnada(chart.asc.sign, int(hora // 30)),
            "_indu_detail": (l9, m9, r)}


def varnada(lagna_sign: int, hl_sign: int) -> int:
    """Varnada lagna (Jaimini, as taught by Sanjay Rath / JHora).

    Count to the lagna from Aries (odd lagna) or backward from Pisces (even lagna); same for
    the Hora lagna. Add the counts if both are odd or both even, else take the difference;
    count the result from Aries (odd lagna) or backward from Pisces (even lagna).
    """
    def count(s):
        return s + 1 if s % 2 == 0 else 12 - s
    a, b = count(lagna_sign), count(hl_sign)
    same = (lagna_sign % 2) == (hl_sign % 2)
    n = (a + b) if same else abs(a - b)
    n = n % 12 or 12
    return (n - 1) % 12 if lagna_sign % 2 == 0 else (12 - n) % 12


def yogi(chart) -> dict:
    yp = (chart.points["Sun"].lon + chart.points["Moon"].lon + 93 + 1 / 3) % 360
    ay = (yp + 186 + 2 / 3) % 360
    return {"Yogi point": yp, "Yogi": NAK_LORD[int(yp // NAK_SPAN)],
            "Duplicate Yogi": SIGN_LORD[int(yp // 30)],
            "Avayogi point": ay, "Avayogi": NAK_LORD[int(ay // NAK_SPAN)]}


# ---------------------------------------------------------------- Sripati / bhava chalit
def sripati(chart) -> dict:
    """Sripati bhavas: each quadrant from lagna to IC to descendant to MC to lagna is
    trisected to give the bhava madhyas (mid-points); the sandhis (house boundaries)
    lie half-way between successive madhyas. Returns madhyas, sandhis (sandhi[i] is the
    start of house i+1) and each graha's bhava."""
    asc, mc = chart.asc.lon, chart.mc.lon
    ic, dsc = (mc + 180) % 360, (asc + 180) % 360
    madhya = []
    for a, b in ((asc, ic), (ic, dsc), (dsc, mc), (mc, asc)):
        span = (b - a) % 360
        madhya += [(a + span * k / 3) % 360 for k in range(3)]
    sandhi = [(madhya[i - 1] + ((madhya[i] - madhya[i - 1]) % 360) / 2) % 360
              for i in range(12)]
    houses = {}
    for p, pt in chart.points.items():
        for i in range(12):
            if (pt.lon - sandhi[i]) % 360 < (sandhi[(i + 1) % 12] - sandhi[i]) % 360:
                houses[p] = i + 1
    return {"madhya": madhya, "sandhi": sandhi, "house": houses}
