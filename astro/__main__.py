"""Command line: python -m astro <command> [options]

  chart     natal positions, dignity, avastha, karakas, KP lords, vargas, ashtakavarga
  dasha     Vimshottari periods (use --depth 1/2/3 and --year to zoom in)
  transits  today's (or --on date) gochara against the natal chart
  cycles    solar phase (Chizhevsky), Barbault index, great conjunctions

Example (the reference chart from the Parashara's Light screenshots):
  python -m astro chart --date 1999-06-22 --time 21:35 --tz 5.5 --place mumbai
"""
import argparse
from datetime import datetime, timedelta, timezone

from . import ashtakavarga, cycles, dasha, kp, transits, vargas
from .chart import Chart, dms
from .constants import ABBR, NAKSHATRAS, SIGN_ABBR

PLACES = {  # lat, lon (classical atlas values, as Parashara's Light uses)
    "mumbai": (18.9667, 72.8167), "delhi": (28.65, 77.2167), "bangalore": (12.9833, 77.5833),
    "chennai": (13.0833, 80.2833), "kolkata": (22.5333, 88.3667), "london": (51.5, -0.1167),
    "new york": (40.7167, -74.0), "dubai": (25.2667, 55.3333), "singapore": (1.2833, 103.85),
}


def local_now(tz: float) -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(hours=tz)


def build(a) -> Chart:
    lat, lon = (a.lat, a.lon) if a.lat is not None else PLACES[a.place.lower()]
    when = datetime.strptime(f"{a.date} {a.time}", "%Y-%m-%d %H:%M")
    return Chart(when, a.tz, lat, lon, a.ayanamsa, a.node, a.name)


def cmd_chart(c: Chart, a):
    print(c.summary())
    print("\nKP lords (star/sub/sub-sub)")
    for name, pt in [("Ascendant", c.asc)] + list(c.points.items()):
        print(f"  {ABBR[name]}  {pt.pada},{'/'.join(ABBR[x] for x in kp.lords(pt.lon))}")
    print("\nArudhas: " + "  ".join(
        f"{'AL' if h == 1 else f'A{h}'}={SIGN_ABBR[c.arudha(h)]}" for h in range(1, 13)))
    print("\nVargas (sign of each point)")
    names = ["Ascendant"] + list(c.points)
    print("  D    " + " ".join(f"{ABBR[n]:>4}" for n in names))
    for n in vargas.VARGAS:
        vc = vargas.varga_chart(c, n)
        print(f"  D{n:<4}" + " ".join(f"{SIGN_ABBR[vc[x]]:>4}" for x in names))
    print("\nAshtakavarga\n" + ashtakavarga.table(c))


def cmd_dasha(c: Chart, a):
    periods = dasha.vimshottari(c, a.depth, a.method)
    for p in periods:
        if a.year and not (p.start.year <= a.year <= p.end.year):
            continue
        print("  " * (len(p.lords) - 1) + str(p))
    print("\nNow:", " | ".join(p.label for p in dasha.current(periods, local_now(c.tz))))


def cmd_transits(c: Chart, a):
    when = datetime.strptime(a.on, "%Y-%m-%d %H:%M") if a.on else local_now(c.tz)
    print(f"Gochara on {when:%d %b %Y %H:%M}   ({transits.sade_sati(c, when)})")
    print("  planet   sign   deg   fromMo fromLg  BAV SAV  kaksha(bindu)")
    for r in transits.gochara(c, when):
        k = f"{r['kaksha']}({r['kaksha_bindu']})" if "kaksha" in r else ""
        print(f"  {r['planet']:8} {r['sign']:4} {r['deg']:6.2f}{' R' if r['retro'] else '  '} "
              f"{r['from_moon']:>4} {r['from_lagna']:>6}  {r.get('bav', ''):>4} {r['sav']:>3}  {k}")


def cmd_cycles(c, a):
    y = datetime.now().year + (datetime.now().timetuple().tm_yday / 365.25)
    print("Chizhevsky solar phase now:", cycles.chizhevsky_phase(y))
    print("\nBarbault cyclic index (lower = outer planets clustered)")
    for yr in range(1900, 2051, 10):
        v = cycles.barbault_index(yr)
        print(f"  {yr}  {v:6.0f}  " + "#" * int(v / 25))
    print("\nJupiter-Saturn conjunctions 1900-2100")
    for d, where in cycles.great_conjunctions(1900, 2100):
        print(f"  {d}  {where}")
    print("\nReference cycle lengths (years)")
    for k, v in {**cycles.DEWEY_CYCLES, **cycles.PLANETARY_PERIODS}.items():
        print(f"  {v:7.2f}  {k}")


def main():
    ap = argparse.ArgumentParser(prog="astro", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["chart", "dasha", "transits", "cycles"])
    ap.add_argument("--date", default="1999-06-22")
    ap.add_argument("--time", default="21:35")
    ap.add_argument("--tz", type=float, default=5.5, help="hours east of UTC (IST = 5.5)")
    ap.add_argument("--place", default="mumbai", help=", ".join(PLACES))
    ap.add_argument("--lat", type=float)
    ap.add_argument("--lon", type=float)
    ap.add_argument("--name", default="")
    ap.add_argument("--ayanamsa", default="lahiri")
    ap.add_argument("--node", default="true", choices=["true", "mean"])
    ap.add_argument("--depth", type=int, default=2)
    ap.add_argument("--method", default="time", choices=["time", "arc"])
    ap.add_argument("--year", type=int, help="dasha: only show periods spanning this year")
    ap.add_argument("--on", help="transits: 'YYYY-MM-DD HH:MM' local time")
    a = ap.parse_args()
    c = build(a)
    {"chart": cmd_chart, "dasha": cmd_dasha, "transits": cmd_transits, "cycles": cmd_cycles}[a.command](c, a)


if __name__ == "__main__":
    main()
