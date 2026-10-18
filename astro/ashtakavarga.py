"""Ashtakavarga (BPHS ch. 66-72): each planet's benefic points (bindus) by sign.

For each of the seven planets, eight contributors (seven planets + Lagna) donate a
bindu to particular houses counted from themselves. Summing the seven
Bhinnashtakavargas gives the Sarvashtakavarga (Samudaya), always totalling 337.
Signs with 28+ are considered supportive for transits; below 25 weak.
"""
from __future__ import annotations

from .constants import SIGN_ABBR

CONTRIB = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Ascendant"]

BAV_RULES = {
    "Sun": [[1, 2, 4, 7, 8, 9, 10, 11], [3, 6, 10, 11], [1, 2, 4, 7, 8, 9, 10, 11],
            [3, 5, 6, 9, 10, 11, 12], [5, 6, 9, 11], [6, 7, 12], [1, 2, 4, 7, 8, 9, 10, 11],
            [3, 4, 6, 10, 11, 12]],
    "Moon": [[3, 6, 7, 8, 10, 11], [1, 3, 6, 7, 10, 11], [2, 3, 5, 6, 9, 10, 11],
             [1, 3, 4, 5, 7, 8, 10, 11], [1, 4, 7, 8, 10, 11, 12], [3, 4, 5, 7, 9, 10, 11],
             [3, 5, 6, 11], [3, 6, 10, 11]],
    "Mars": [[3, 5, 6, 10, 11], [3, 6, 11], [1, 2, 4, 7, 8, 10, 11], [3, 5, 6, 11],
             [6, 10, 11, 12], [6, 8, 11, 12], [1, 4, 7, 8, 9, 10, 11], [1, 3, 6, 10, 11]],
    "Mercury": [[5, 6, 9, 11, 12], [2, 4, 6, 8, 10, 11], [1, 2, 4, 7, 8, 9, 10, 11],
                [1, 3, 5, 6, 9, 10, 11, 12], [6, 8, 11, 12], [1, 2, 3, 4, 5, 8, 9, 11],
                [1, 2, 4, 7, 8, 9, 10, 11], [1, 2, 4, 6, 8, 10, 11]],
    "Jupiter": [[1, 2, 3, 4, 7, 8, 9, 10, 11], [2, 5, 7, 9, 11], [1, 2, 4, 7, 8, 10, 11],
                [1, 2, 4, 5, 6, 9, 10, 11], [1, 2, 3, 4, 7, 8, 10, 11], [2, 5, 6, 9, 10, 11],
                [3, 5, 6, 12], [1, 2, 4, 5, 6, 7, 9, 10, 11]],
    "Venus": [[8, 11, 12], [1, 2, 3, 4, 5, 8, 9, 11, 12], [3, 5, 6, 9, 11, 12],
              [3, 5, 6, 9, 11], [5, 8, 9, 10, 11], [1, 2, 3, 4, 5, 8, 9, 10, 11],
              [3, 4, 5, 8, 9, 10, 11], [1, 2, 3, 4, 5, 8, 9, 11]],
    "Saturn": [[1, 2, 4, 7, 8, 10, 11], [3, 6, 11], [3, 5, 6, 10, 11, 12],
               [6, 8, 9, 10, 11, 12], [5, 6, 11, 12], [6, 11, 12], [3, 5, 6, 11],
               [1, 3, 4, 6, 10, 11]],
}


def bhinna(chart) -> dict[str, list[int]]:
    """Bhinnashtakavarga: planet -> 12 bindu counts indexed by sign (Aries=0)."""
    pos = {p: chart.points[p].sign for p in CONTRIB[:-1]}
    pos["Ascendant"] = chart.asc.sign
    out = {}
    for planet, rules in BAV_RULES.items():
        row = [0] * 12
        for contributor, houses in zip(CONTRIB, rules):
            for h in houses:
                row[(pos[contributor] + h - 1) % 12] += 1
        out[planet] = row
    return out


def sarva(chart) -> list[int]:
    """Sarvashtakavarga (Samudaya): bindus per sign, total 337."""
    b = bhinna(chart)
    return [sum(b[p][s] for p in b) for s in range(12)]


def table(chart) -> str:
    b = bhinna(chart)
    head = "         " + " ".join(f"{s:>3}" for s in SIGN_ABBR) + "  tot"
    rows = [head] + [f"{p:8} " + " ".join(f"{v:>3}" for v in r) + f"  {sum(r):>3}"
                     for p, r in b.items()]
    sav = sarva(chart)
    rows.append("SAV      " + " ".join(f"{v:>3}" for v in sav) + f"  {sum(sav):>3}")
    return "\n".join(rows)
