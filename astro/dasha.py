"""Vimshottari dasha (BPHS ch. 46-53): a 120-year cycle of planetary periods.

The starting period is the lord of the Moon's birth nakshatra; the unelapsed fraction
of that nakshatra gives the balance of the first period. Sub-periods (antardasha,
pratyantardasha) divide each period in the same proportions as the whole cycle.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta

import swisseph as swe

from .constants import DASHA_ORDER, DASHA_YEARS, NAK_LORD, NAK_SPAN

# Year length matters: ~365.2422 (tropical) reproduces Parashara's Light; some programs
# use 365.25 (Julian) or 360 (savana). Results differ by days to weeks over decades.
YEAR_DAYS = 365.2422


@dataclass
class Period:
    lords: tuple[str, ...]   # e.g. ("Jupiter", "Saturn") = Ju maha / Sa antar
    start: datetime
    end: datetime

    @property
    def label(self) -> str:
        return "/".join(l[:2] for l in self.lords)

    def __str__(self):
        return f"{self.label:12} {self.start:%d %b %Y %H:%M}  ->  {self.end:%d %b %Y}"


def _subperiods(lords, start, years, depth):
    out = []
    first = DASHA_ORDER.index(lords[-1])
    t = start
    for i in range(9):
        lord = DASHA_ORDER[(first + i) % 9]
        sub_years = years * DASHA_YEARS[lord] / 120
        end = t + timedelta(days=sub_years * YEAR_DAYS)
        p = Period(lords + (lord,), t, end)
        out.append(p)
        if depth > 1:
            out.extend(_subperiods(p.lords, t, sub_years, depth - 1))
        t = end
    return out


def _moon_lon(jd, flags):
    return swe.calc_ut(jd, swe.MOON, flags)[0][0]


def _moon_at(target, jd, flags):
    """Julian day when the Moon reaches `target` longitude, starting near jd."""
    for _ in range(30):
        diff = (_moon_lon(jd, flags) - target + 180) % 360 - 180
        if abs(diff) < 1e-9:
            break
        jd -= diff / 13.18
    return jd


def elapsed_fraction(chart, method: str = "time") -> float:
    """How far through its birth nakshatra the Moon is.

    "arc": fraction of the 13°20' arc covered (the textbook method).
    "time": fraction of the time the Moon spends in that nakshatra (used by
            Parashara's Light; differs by up to ~1% because the Moon's speed varies).
    """
    lon = chart.points["Moon"].lon
    nak = int(lon // NAK_SPAN)
    if method == "arc":
        return (lon % NAK_SPAN) / NAK_SPAN
    s = _moon_at(nak * NAK_SPAN, chart.jd - 0.5, chart.flags)
    e = _moon_at(((nak + 1) * NAK_SPAN) % 360, chart.jd + 0.5, chart.flags)
    return (chart.jd - s) / (e - s)


def vimshottari(chart, depth: int = 2, method: str = "time") -> list[Period]:
    """All periods from the theoretical start of the birth mahadasha.

    depth=1 mahadashas only, 2 adds antardashas, 3 adds pratyantardashas.
    """
    birth = chart.local
    nak = int(chart.points["Moon"].lon // NAK_SPAN)
    elapsed_frac = elapsed_fraction(chart, method)
    lord = NAK_LORD[nak]
    start = birth - timedelta(days=elapsed_frac * DASHA_YEARS[lord] * YEAR_DAYS)
    periods, t = [], start
    first = DASHA_ORDER.index(lord)
    for i in range(10):  # 10 so the cycle covers a full life after the birth balance
        l = DASHA_ORDER[(first + i) % 9]
        end = t + timedelta(days=DASHA_YEARS[l] * YEAR_DAYS)
        periods.append(Period((l,), t, end))
        if depth > 1:
            periods.extend(_subperiods((l,), t, DASHA_YEARS[l], depth - 1))
        t = end
    return periods


def current(periods: list[Period], when: datetime) -> list[Period]:
    """The running period at each level for a moment in time."""
    return sorted((p for p in periods if p.start <= when < p.end), key=lambda p: len(p.lords))
