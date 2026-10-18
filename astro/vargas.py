"""Divisional charts (vargas), BPHS ch. 6-7. Each returns the varga sign (0..11) for a
sidereal longitude. `varga_deg` gives the position within the varga sign, as shown
by Parashara's Light (e.g. "As 04:27" in the D3)."""
from __future__ import annotations

MOVABLE, FIXED, DUAL = 0, 1, 2


def _mode(sign):  # 0 movable, 1 fixed, 2 dual
    return sign % 3


def _odd(sign):   # Aries (0) counts as the 1st (odd) sign
    return sign % 2 == 0


def d1(lon):
    return int(lon // 30)


def d2(lon):  # Hora: Sun's hora = Leo, Moon's hora = Cancer
    s, d = int(lon // 30), lon % 30
    first_half = d < 15
    return 4 if first_half == _odd(s) else 3


def d3(lon):  # Drekkana: 1st, 5th, 9th from the sign
    s, d = int(lon // 30), lon % 30
    return (s + 4 * int(d // 10)) % 12


def d4(lon):  # Chaturthamsa: 1st, 4th, 7th, 10th
    s, d = int(lon // 30), lon % 30
    return (s + 3 * int(d // 7.5)) % 12


def d7(lon):  # Saptamsa: odd from the sign, even from the 7th
    s, d = int(lon // 30), lon % 30
    start = s if _odd(s) else s + 6
    return (start + int(d // (30 / 7))) % 12


def d9(lon):  # Navamsa: continuous 3°20' parts from Aries
    return int(lon // (30 / 9)) % 12


def d10(lon):  # Dasamsa: odd from the sign, even from the 9th
    s, d = int(lon // 30), lon % 30
    start = s if _odd(s) else s + 8
    return (start + int(d // 3)) % 12


def d12(lon):  # Dwadasamsa: from the sign itself
    s, d = int(lon // 30), lon % 30
    return (s + int(d // 2.5)) % 12


def d16(lon):  # Shodasamsa: movable Aries, fixed Leo, dual Sagittarius
    s, d = int(lon // 30), lon % 30
    return ([0, 4, 8][_mode(s)] + int(d // (30 / 16))) % 12


def d20(lon):  # Vimsamsa: movable Aries, fixed Sagittarius, dual Leo
    s, d = int(lon // 30), lon % 30
    return ([0, 8, 4][_mode(s)] + int(d // 1.5)) % 12


def d24(lon):  # Chaturvimsamsa: odd from Leo, even from Cancer
    s, d = int(lon // 30), lon % 30
    return ((4 if _odd(s) else 3) + int(d // 1.25)) % 12


def d27(lon):  # Bhamsa: continuous from Aries
    return int(lon // (30 / 27)) % 12


def d30(lon):  # Parashari Trimsamsa: unequal parts ruled by the five true planets
    s, d = int(lon // 30), lon % 30
    if _odd(s):
        table = [(5, 0), (10, 10), (18, 8), (25, 2), (30, 6)]   # Ar Aq Sg Ge Li
    else:
        table = [(5, 1), (12, 5), (20, 11), (25, 9), (30, 7)]   # Ta Vi Pi Cp Sc
    for limit, sign in table:
        if d < limit:
            return sign
    return table[-1][1]


def d40(lon):  # Khavedamsa: odd from Aries, even from Libra
    s, d = int(lon // 30), lon % 30
    return ((0 if _odd(s) else 6) + int(d // 0.75)) % 12


def d45(lon):  # Akshavedamsa: movable Aries, fixed Leo, dual Sagittarius
    s, d = int(lon // 30), lon % 30
    return ([0, 4, 8][_mode(s)] + int(d // (30 / 45))) % 12


def d60(lon):  # Shashtiamsa: from the sign itself
    s, d = int(lon // 30), lon % 30
    return (s + int(d * 2)) % 12


VARGAS = {
    1: ("Rasi", "body, overall life", d1), 2: ("Hora", "wealth", d2),
    3: ("Drekkana", "siblings, courage", d3), 4: ("Chaturthamsa", "property, fortune", d4),
    7: ("Saptamsa", "children", d7), 9: ("Navamsa", "spouse, dharma, inner strength", d9),
    10: ("Dasamsa", "career", d10), 12: ("Dwadasamsa", "parents", d12),
    16: ("Shodasamsa", "vehicles, comforts", d16), 20: ("Vimsamsa", "spiritual life", d20),
    24: ("Chaturvimsamsa", "learning", d24), 27: ("Bhamsa", "strengths/weaknesses", d27),
    30: ("Trimsamsa", "misfortunes", d30), 40: ("Khavedamsa", "maternal legacy", d40),
    45: ("Akshavedamsa", "paternal legacy, character", d45), 60: ("Shashtiamsa", "past karma", d60),
}


def varga_sign(lon: float, n: int) -> int:
    return VARGAS[n][2](lon % 360)


def varga_deg(lon: float, n: int) -> float:
    """Longitude within the varga sign (equal-division vargas only)."""
    part = 30 / n
    return (lon % 30 % part) / part * 30


def varga_chart(chart, n: int) -> dict[str, int]:
    out = {"Ascendant": varga_sign(chart.asc.lon, n)}
    out.update({p: varga_sign(pt.lon, n) for p, pt in chart.points.items()})
    return out
