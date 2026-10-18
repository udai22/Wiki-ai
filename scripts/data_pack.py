"""Build the chart data pack that interpretive readings work from.
Usage: python scripts/data_pack.py > reports/udai/data-pack.md"""
import sys
from datetime import datetime
sys.path.insert(0, ".")
import swisseph as swe
from astro import ashtakavarga, cycles, dasha, vargas
from astro.chart import Chart, dms
from astro.constants import ABBR, SIGN_ABBR, SIGN_LORD, SIGNS

BIRTH = datetime(1999, 6, 22, 21, 35)
c = Chart(BIRTH, 5.5, 18.9667, 72.8167, name="Udai")
print("# Data pack — Udai, 22 Jun 1999 21:35 IST, Mumbai (18N58 72E49)\n")
print("Swiss Ephemeris, Lahiri ayanamsa, true node, whole-sign houses. All values computed by `astro/`.\n")
print("```\n" + c.summary() + "\n```\n")
speeds = {p: round(pt.speed, 3) for p, pt in c.points.items()}
print(f"Daily speeds (deg/day): {speeds}  (negative = retrograde; nodes always retrograde)\n")
sun = c.points["Sun"].lon
print("Angular distance from Sun: " + ", ".join(
    f"{p} {abs((pt.lon - sun + 180) % 360 - 180):.1f}°" for p, pt in c.points.items() if p != "Sun") + "\n")

print("## Houses (whole sign) — sign, lord, lord's placement, occupants\n")
for h in range(1, 13):
    s = c.house_sign(h); lord = SIGN_LORD[s]
    print(f"- H{h} {SIGNS[s]}: lord {lord} in H{c.house_of(lord)} ({SIGN_ABBR[c.points[lord].sign]}, {c.dignity(lord)}); "
          f"occupants: {', '.join(c.occupants(h)) or '—'}")
SPECIAL = {"Mars": [4, 7, 8], "Jupiter": [5, 7, 9], "Saturn": [3, 7, 10], "Rahu": [5, 7, 9], "Ketu": [5, 7, 9]}
print("\n## Graha drishti (Parashari aspects; node aspects per some authorities)\n")
for p in c.points:
    hs = [(c.house_of(p) + a - 2) % 12 + 1 for a in SPECIAL.get(p, [7])]
    print(f"- {p} (H{c.house_of(p)}) aspects houses {hs}: " + "; ".join(
        f"H{h}[{', '.join(c.occupants(h))}]" for h in hs if c.occupants(h)))
print("\n## Rashi drishti (Jaimini sign aspects)\n")
def rashi_aspects(s):
    mode = s % 3
    if mode == 0: return [x for x in range(12) if x % 3 == 1 and x != (s + 1) % 12]
    if mode == 1: return [x for x in range(12) if x % 3 == 0 and x != (s - 1) % 12]
    return [x for x in range(12) if x % 3 == 2 and x != s]
for s in range(12):
    occ = [p for p in c.points if c.points[p].sign == s]
    if occ: print(f"- {SIGN_ABBR[s]} ({', '.join(occ)}) aspects " + ", ".join(SIGN_ABBR[x] for x in rashi_aspects(s)))

print("\n## Divisional charts (sign of each point)\n")
names = ["Ascendant"] + list(c.points)
print("| D | " + " | ".join(ABBR[n] for n in names) + " |\n|" + "---|" * (len(names) + 1))
for n, (vn, use, _) in vargas.VARGAS.items():
    vc = vargas.varga_chart(c, n)
    print(f"| D{n} {vn} ({use}) | " + " | ".join(SIGN_ABBR[vc[x]] for x in names) + " |")
vg = [p for p in c.points if vargas.varga_sign(c.points[p].lon, 9) == c.points[p].sign]
print(f"\nVargottama (same sign D1 & D9): {', '.join(vg)}\n")
print("## Arudhas\n\n" + ", ".join(f"{'AL' if h == 1 else ('UL' if h == 12 else f'A{h}')}={SIGN_ABBR[c.arudha(h)]}" for h in range(1, 13)) + "\n")
print("## Ashtakavarga\n\n```\n" + ashtakavarga.table(c) + "\n```\n")
print("## Vimshottari (maha/antar)\n\n```")
for p in dasha.vimshottari(c, 2):
    if p.end.year >= 1999 and p.start.year <= 2060: print("  " * (len(p.lords) - 1) + str(p))
print("```\n")
t = Chart(BIRTH, 5.5, 18.9667, 72.8167, ayanamsa="tropical")
print("## Tropical / Western positions (for Hellenistic & modern readings)\n")
print(f"- Asc {dms(t.asc.deg)} {SIGNS[t.asc.sign]}, MC {dms(t.mc.deg)} {SIGNS[t.mc.sign]}")
for p, pt in list(t.points.items()) + list(t.outer.items()):
    print(f"- {p} {dms(pt.deg)} {SIGNS[pt.sign]}{' R' if pt.retrograde else ''}")
print(f"- Placidus cusps: " + ", ".join(f"{i+1}:{dms(x % 30)} {SIGN_ABBR[int(x // 30)]}" for i, x in enumerate(t.placidus_cusps)))
print(f"- Sect: night chart (Sun below horizon)\n")
print("## Cycles at birth\n")
print(f"- Chizhevsky solar phase at birth: {cycles.chizhevsky_phase(1999.47)}")
print(f"- Barbault index 1999: {cycles.barbault_index(1999, 6, 22):.0f}")
print(f"- Last Jupiter-Saturn conjunction before birth: 1980-81 (Libra); next: 28 May 2000 (Taurus)")
