"""Gochara (transits) read against the natal chart: house from Moon and Lagna,
Ashtakavarga bindus, kaksha (3°45' sub-division) lord, and Sade Sati status."""
from __future__ import annotations

from datetime import datetime

from .ashtakavarga import BAV_RULES, CONTRIB, bhinna, sarva
from .chart import Chart
from .constants import SIGN_ABBR

# Kaksha lords in order through each sign (8 × 3°45')
KAKSHA_LORDS = ["Saturn", "Jupiter", "Mars", "Sun", "Venus", "Mercury", "Moon", "Ascendant"]


def kaksha(lon: float) -> str:
    return KAKSHA_LORDS[int((lon % 30) // 3.75)]


def kaksha_bindu(natal: Chart, planet: str, lon: float) -> int:
    """1 if the kaksha lord donated a bindu to this sign in `planet`'s BAV."""
    lord = kaksha(lon)
    sign = int(lon // 30) % 12
    lord_sign = natal.asc.sign if lord == "Ascendant" else natal.points[lord].sign
    houses = BAV_RULES[planet][CONTRIB.index(lord)]
    return int(((sign - lord_sign) % 12) + 1 in houses)


def gochara(natal: Chart, when: datetime, tz: float | None = None) -> list[dict]:
    tz = natal.tz if tz is None else tz
    now = Chart(when, tz, natal.lat, natal.lon, natal.ayanamsa_name)
    bav, sav = bhinna(natal), sarva(natal)
    rows = []
    for p, pt in now.points.items():
        row = {"planet": p, "sign": SIGN_ABBR[pt.sign], "deg": round(pt.deg, 2),
               "retro": pt.retrograde,
               "from_moon": (pt.sign - natal.points["Moon"].sign) % 12 + 1,
               "from_lagna": (pt.sign - natal.asc.sign) % 12 + 1,
               "sav": sav[pt.sign]}
        if p in bav:
            row.update(bav=bav[p][pt.sign], kaksha=kaksha(pt.lon),
                       kaksha_bindu=kaksha_bindu(natal, p, pt.lon))
        rows.append(row)
    return rows


def sade_sati(natal: Chart, when: datetime) -> str:
    """Saturn transiting the 12th, 1st or 2nd from the natal Moon (~7.5 years)."""
    now = Chart(when, natal.tz, natal.lat, natal.lon, natal.ayanamsa_name)
    h = (now.points["Saturn"].sign - natal.points["Moon"].sign) % 12 + 1
    return {12: "Sade Sati: rising phase", 1: "Sade Sati: peak phase",
            2: "Sade Sati: setting phase", 4: "Kantaka/Ardhashtama Shani (4th)",
            8: "Ashtama Shani (8th)"}.get(h, f"No Sade Sati (Saturn {h}th from Moon)")
