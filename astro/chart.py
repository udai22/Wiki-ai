"""Natal chart calculation on top of the Swiss Ephemeris.

Swiss Ephemeris (Astrodienst, Zurich) is the reference-grade ephemeris used by most
serious astrology software. Without the optional .se1 data files it falls back to the
built-in Moshier ephemeris (~1 arcsecond for planets), which is plenty for charts.
Drop Astrodienst's .se1 files in ./ephe for full JPL-derived precision.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from datetime import datetime, timedelta

import swisseph as swe

from .constants import (ABBR, DEBILITATION, EXALTATION, MOOLATRIKONA, NAK_LORD, NAK_SPAN,
                        NAKSHATRAS, NATURAL_ENEMIES, NATURAL_FRIENDS, SIGN_ABBR, SIGN_LORD, SIGNS)

_EPHE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ephe")
swe.set_ephe_path(_EPHE)

AYANAMSAS = {
    "lahiri": swe.SIDM_LAHIRI,          # Indian government standard (Chitrapaksha)
    "raman": swe.SIDM_RAMAN,
    "krishnamurti": swe.SIDM_KRISHNAMURTI,
    "fagan_bradley": swe.SIDM_FAGAN_BRADLEY,
    "yukteshwar": swe.SIDM_YUKTESHWAR,
    "true_chitra": swe.SIDM_TRUE_CITRA,
    "tropical": None,
}

_SWE_IDS = {"Sun": swe.SUN, "Moon": swe.MOON, "Mars": swe.MARS, "Mercury": swe.MERCURY,
            "Jupiter": swe.JUPITER, "Venus": swe.VENUS, "Saturn": swe.SATURN}
OUTER = {"Uranus": swe.URANUS, "Neptune": swe.NEPTUNE, "Pluto": swe.PLUTO}


def dms(deg: float) -> str:
    """Format degrees within a sign as DD:MM:SS (truncated, like most Indian software)."""
    total = int(deg * 3600 + 1e-6)
    return f"{total // 3600:02d}:{total % 3600 // 60:02d}:{total % 60:02d}"


@dataclass
class Point:
    name: str
    lon: float               # sidereal (or tropical) longitude 0..360
    speed: float = 0.0       # deg/day
    sign: int = field(init=False)
    deg: float = field(init=False)
    nakshatra: int = field(init=False)
    pada: int = field(init=False)

    def __post_init__(self):
        self.lon %= 360
        self.sign = int(self.lon // 30)
        self.deg = self.lon - self.sign * 30
        self.nakshatra = int(self.lon // NAK_SPAN)
        self.pada = int((self.lon % NAK_SPAN) // (NAK_SPAN / 4)) + 1

    @property
    def retrograde(self) -> bool:
        return self.speed < 0 and self.name not in ("Rahu", "Ketu")

    @property
    def nak_name(self) -> str:
        return NAKSHATRAS[self.nakshatra]

    @property
    def nak_lord(self) -> str:
        return NAK_LORD[self.nakshatra]

    def __str__(self):
        r = " R" if self.retrograde else ""
        return (f"{ABBR.get(self.name, self.name):3}{dms(self.deg)} {SIGN_ABBR[self.sign]} "
                f"{self.nak_name} p{self.pada}{r}")


class Chart:
    """A sidereal chart. `when` is local civil time; `tz` is hours east of UTC."""

    def __init__(self, when: datetime, tz: float, lat: float, lon: float,
                 ayanamsa: str = "lahiri", node: str = "true", name: str = ""):
        self.name, self.local, self.tz, self.lat, self.lon = name, when, tz, lat, lon
        self.utc = when - timedelta(hours=tz)
        u = self.utc
        self.jd = swe.julday(u.year, u.month, u.day,
                             u.hour + u.minute / 60 + u.second / 3600, swe.GREG_CAL)
        self.ayanamsa_name = ayanamsa
        flags = swe.FLG_SWIEPH | swe.FLG_SPEED
        if AYANAMSAS[ayanamsa] is not None:
            swe.set_sid_mode(AYANAMSAS[ayanamsa])
            flags |= swe.FLG_SIDEREAL
            self.ayanamsa = swe.get_ayanamsa_ut(self.jd)
        else:
            self.ayanamsa = 0.0
        self.flags = flags

        self.points: dict[str, Point] = {}
        for p, pid in _SWE_IDS.items():
            xx, _ = swe.calc_ut(self.jd, pid, flags)
            self.points[p] = Point(p, xx[0], xx[3])
        node_id = swe.MEAN_NODE if node == "mean" else swe.TRUE_NODE
        xx, _ = swe.calc_ut(self.jd, node_id, flags)
        self.points["Rahu"] = Point("Rahu", xx[0], xx[3])
        self.points["Ketu"] = Point("Ketu", xx[0] + 180, xx[3])
        self.outer = {p: Point(p, swe.calc_ut(self.jd, pid, flags)[0][0],
                               swe.calc_ut(self.jd, pid, flags)[0][3])
                      for p, pid in OUTER.items()}

        cusps, ascmc = swe.houses_ex(self.jd, lat, lon, b"P", flags)
        self.asc = Point("Ascendant", ascmc[0])
        self.mc = Point("MC", ascmc[1])
        self.placidus_cusps = list(cusps)

    # ---- houses (whole-sign, the Parashari default) ----
    def house_of(self, planet: str) -> int:
        return (self.points[planet].sign - self.asc.sign) % 12 + 1

    def house_sign(self, house: int) -> int:
        return (self.asc.sign + house - 1) % 12

    def occupants(self, house: int) -> list[str]:
        return [p for p in self.points if self.house_of(p) == house]

    # ---- dignity ----
    def temporal_friend(self, a: str, b: str) -> bool:
        """Tatkalika friendship: b in 2,3,4,10,11,12 from a."""
        d = (self.points[b].sign - self.points[a].sign) % 12 + 1
        return d in (2, 3, 4, 10, 11, 12)

    def compound_relation(self, a: str, b: str) -> str:
        if a == b:
            return "Own"
        nat = 1 if b in NATURAL_FRIENDS[a] else -1 if b in NATURAL_ENEMIES[a] else 0
        score = nat + (1 if self.temporal_friend(a, b) else -1)
        return {2: "Great friend", 1: "Friend", 0: "Neutral", -1: "Enemy", -2: "Great enemy"}[score]

    def dignity(self, planet: str) -> str:
        p = self.points[planet]
        if planet in EXALTATION and p.sign == EXALTATION[planet][0]:
            return "Exalted"
        if planet in DEBILITATION and p.sign == DEBILITATION[planet][0]:
            return "Debilitated"
        if planet in ("Rahu", "Ketu"):
            return "Neutral"
        mt = MOOLATRIKONA.get(planet)
        if mt and p.sign == mt[0] and mt[1] <= p.deg < mt[2]:
            return "Moolatrikona"
        lord = SIGN_LORD[p.sign]
        if lord == planet:
            return "Own sign"
        return self.compound_relation(planet, lord)

    # ---- Baladi avastha (age state), BPHS ch. 45 ----
    def avastha(self, planet: str) -> str:
        p = self.points[planet]
        states = ["Infant", "Youth", "Adult", "Old", "Dead"]
        i = min(int(p.deg // 6), 4)
        return states[i] if p.sign % 2 == 0 else states[4 - i]

    # ---- Jaimini chara karakas (7-karaka scheme) ----
    def chara_karakas(self) -> dict[str, str]:
        names = ["AK", "AmK", "BK", "MK", "PiK", "GK", "DK"]
        seven = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
        ranked = sorted(seven, key=lambda p: self.points[p].deg, reverse=True)
        return dict(zip(names, ranked))

    # ---- Arudha padas (Jaimini/Parashara) ----
    def arudha(self, house: int) -> int:
        """Sign index of the arudha of a house (A1 = Arudha Lagna)."""
        hs = self.house_sign(house)
        lord = SIGN_LORD[hs]
        ls = self.points[lord].sign
        dist = (ls - hs) % 12
        a = (ls + dist) % 12
        # exception: arudha may not fall in the house itself or the 7th from it
        if a == hs:
            a = (hs + 9) % 12
        elif a == (hs + 6) % 12:
            a = (a + 9) % 12
        return a

    def summary(self) -> str:
        lines = [f"{self.name}  {self.local:%d %b %Y %H:%M:%S}  tz {self.tz:+}  "
                 f"lat {self.lat:.4f} lon {self.lon:.4f}",
                 f"Ayanamsa ({self.ayanamsa_name}): {dms(self.ayanamsa)}",
                 f"  {self.asc}  [Lagna]"]
        kk = {v: k for k, v in self.chara_karakas().items()}
        for name, p in self.points.items():
            lines.append(f"  {p}  H{self.house_of(name):<2} {self.dignity(name):13}"
                         f"{self.avastha(name):7}{kk.get(name, '')}")
        return "\n".join(lines)
