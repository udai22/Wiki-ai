"""Krishnamurti Paddhati (KP) star/sub/sub-sub lords.

Each nakshatra is split into 9 unequal subs proportional to the Vimshottari years,
starting with the nakshatra's own lord. Parashara's Light shows these as e.g.
"1,Mo/Ma/Sa" = pada 1, star lord Moon, sub lord Mars, sub-sub lord Saturn.
"""
from .constants import DASHA_ORDER, DASHA_YEARS, NAK_LORD, NAK_SPAN


def _split(start_lord, offset, span):
    i0 = DASHA_ORDER.index(start_lord)
    acc = 0.0
    for i in range(9):
        lord = DASHA_ORDER[(i0 + i) % 9]
        width = span * DASHA_YEARS[lord] / 120
        if offset < acc + width or i == 8:
            return lord, offset - acc, width
        acc += width


def lords(lon: float) -> tuple[str, str, str]:
    lon %= 360
    nak = int(lon // NAK_SPAN)
    star = NAK_LORD[nak]
    sub, off, width = _split(star, lon % NAK_SPAN, NAK_SPAN)
    subsub, _, _ = _split(sub, off, width)
    return star, sub, subsub
