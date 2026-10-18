"""Birth-time sensitivity: which chart factors hold steady across an uncertain birth
time and which flip, and exactly when.

The masters treat chart factors at different scales of time-sensitivity:
  - planets in signs/houses (whole-sign): change every ~2 hours (lagna sign)
  - lagna nakshatra pada / navamsa (D9) lagna: ~12-15 min
  - D10 career lagna: ~10 min; D12 ~8 min; D24 ~5 min; D30 varies
  - D60 shashtiamsa lagna (Parashara's 'most important' varga): ~2 min
  - KP sub lord of the ascendant: a few minutes to ~20 min
  - Moon nakshatra (dasha sequence): ~1 day; dasha dates: ~2 days per hour of error
So a reading should lean on the slow factors and treat the fast ones as hypotheses
to be tested against life events (rectification).
"""
from __future__ import annotations

from datetime import datetime, timedelta

from . import dasha, kp, vargas
from .chart import Chart, dms
from .constants import NAKSHATRAS, SIGN_ABBR

FACTORS = [
    ("Lagna sign (D1)", lambda c: SIGN_ABBR[c.asc.sign]),
    ("Lagna nakshatra-pada", lambda c: f"{NAKSHATRAS[c.asc.nakshatra]}-{c.asc.pada}"),
    ("Lagna KP star/sub", lambda c: "/".join(x[:2] for x in kp.lords(c.asc.lon)[:2])),
    ("Lagna KP sub-sub", lambda c: kp.lords(c.asc.lon)[2][:2]),
    ("D2 Hora lagna", lambda c: SIGN_ABBR[vargas.varga_sign(c.asc.lon, 2)]),
    ("D3 Drekkana lagna", lambda c: SIGN_ABBR[vargas.varga_sign(c.asc.lon, 3)]),
    ("D4 lagna", lambda c: SIGN_ABBR[vargas.varga_sign(c.asc.lon, 4)]),
    ("D7 Saptamsa lagna", lambda c: SIGN_ABBR[vargas.varga_sign(c.asc.lon, 7)]),
    ("D9 Navamsa lagna", lambda c: SIGN_ABBR[vargas.varga_sign(c.asc.lon, 9)]),
    ("D10 Dasamsa lagna", lambda c: SIGN_ABBR[vargas.varga_sign(c.asc.lon, 10)]),
    ("D12 lagna", lambda c: SIGN_ABBR[vargas.varga_sign(c.asc.lon, 12)]),
    ("D16 lagna", lambda c: SIGN_ABBR[vargas.varga_sign(c.asc.lon, 16)]),
    ("D20 lagna", lambda c: SIGN_ABBR[vargas.varga_sign(c.asc.lon, 20)]),
    ("D24 lagna", lambda c: SIGN_ABBR[vargas.varga_sign(c.asc.lon, 24)]),
    ("D30 Trimsamsa lagna", lambda c: SIGN_ABBR[vargas.varga_sign(c.asc.lon, 30)]),
    ("D60 Shashtiamsa lagna", lambda c: SIGN_ABBR[vargas.varga_sign(c.asc.lon, 60)]),
    ("Moon sign", lambda c: SIGN_ABBR[c.points["Moon"].sign]),
    ("Moon nakshatra-pada", lambda c: f"{c.points['Moon'].nak_name}-{c.points['Moon'].pada}"),
    ("Moon D9", lambda c: SIGN_ABBR[vargas.varga_sign(c.points["Moon"].lon, 9)]),
    ("Arudha Lagna", lambda c: SIGN_ABBR[c.arudha(1)]),
    ("Upapada (A12)", lambda c: SIGN_ABBR[c.arudha(12)]),
    ("Placidus 10th cusp sign", lambda c: SIGN_ABBR[int(c.placidus_cusps[9] // 30)]),
]


def chart_at(base: Chart, minutes: float) -> Chart:
    return Chart(base.local + timedelta(minutes=minutes), base.tz, base.lat, base.lon,
                 base.ayanamsa_name, name=base.name)


def sweep(base: Chart, before: int = 60, after: int = 60, step: float = 0.5):
    """For each factor: list of (offset_minutes, value) change points across the window."""
    offsets = [i * step for i in range(int(-before / step), int(after / step) + 1)]
    charts = {o: chart_at(base, o) for o in offsets}
    out = {}
    for name, f in FACTORS:
        vals = [(o, f(charts[o])) for o in offsets]
        changes, prev = [vals[0]], vals[0][1]
        for o, v in vals[1:]:
            if v != prev:
                changes.append((o, v))
                prev = v
        out[name] = changes
    return out


def window(changes, at: float = 0.0):
    """The [start, end) offsets during which the factor keeps its value at `at`."""
    start, end = None, None
    for i, (o, v) in enumerate(changes):
        nxt = changes[i + 1][0] if i + 1 < len(changes) else None
        if o <= at and (nxt is None or at < nxt):
            start, end = o, nxt
    return start if start != changes[0][0] else None, end


def report(base: Chart, before: int = 60, after: int = 60) -> str:
    res = sweep(base, before, after)
    lines = [f"Birth-time sensitivity, {before} min before to {after} min after "
             f"{base.local:%d %b %Y %H:%M}",
             f"{'factor':26} {'value now':16} {'holds from':>11} {'to':>8}   changes in window"]
    for name, ch in res.items():
        s, e = window(ch)
        now = next(v for o, v in reversed(ch) if o <= 0)
        s_txt = f"{s:+.1f}m" if s is not None else f"<-{before}m"
        e_txt = f"{e:+.1f}m" if e is not None else f">+{after}m"
        near = [(o, v) for o, v in ch[1:] if o != s and abs(o) <= 30]
        others = ", ".join(f"{o:+.0f}m:{v}" for o, v in near[:10]) + (" ..." if len(near) > 10 else "")
        lines.append(f"{name:26} {now:16} {s_txt:>11} {e_txt:>8}   {others}")
    return "\n".join(lines)


def dasha_shift(base: Chart, offsets=(-60, -30, -15, 0, 15, 30, 60)) -> str:
    rows = ["Vimshottari start dates vs birth-time offset"]
    for o in offsets:
        c = chart_at(base, o)
        ps = [p for p in dasha.vimshottari(c, 2) if p.start.year >= 2020 and p.start.year <= 2031]
        txt = "  ".join(f"{p.label} {p.start:%d %b %Y}" for p in ps if len(p.lords) <= 2)
        rows.append(f"  {o:+4d}m  asc {dms(c.asc.deg)} {SIGN_ABBR[c.asc.sign]}  " + txt)
    return "\n".join(rows)


def scenarios(base: Chart, offsets=(-30, -20, -15, -10, -5, 0, 5, 10, 15, 20, 30)) -> str:
    """Key lagna-dependent factors at a grid of candidate birth times."""
    keys = ["Lagna nakshatra-pada", "Lagna KP star/sub", "D9 Navamsa lagna", "D10 Dasamsa lagna",
            "D7 Saptamsa lagna", "D12 lagna", "D3 Drekkana lagna", "D2 Hora lagna",
            "D30 Trimsamsa lagna", "D60 Shashtiamsa lagna", "Placidus 10th cusp sign"]
    fmap = dict(FACTORS)
    head = f"{'offset':>7} {'time':>6} {'asc':>12} " + " ".join(f"{k.split()[0]:>10}" for k in keys)
    rows = [head]
    for o in offsets:
        c = chart_at(base, o)
        rows.append(f"{o:+6d}m {c.local:%H:%M} {dms(c.asc.deg)} {SIGN_ABBR[c.asc.sign]} "
                    + " ".join(f"{fmap[k](c):>10.10}" for k in keys))
    return "\n".join(rows)
