"""Checks the engine against values read off Parashara's Light 9.0 for the
reference chart: 22 Jun 1999 21:35 IST, Mumbai (18N58, 72E49), Lahiri, true node."""
from datetime import datetime

import numpy as np
import pytest

from astro import ashtakavarga, cycles, dasha, kp, transits, vargas
from astro.chart import Chart

C = Chart(datetime(1999, 6, 22, 21, 35), 5.5, 18.9667, 72.8167, name="reference")


def arcsec(dms_str):
    d, m, s = map(int, dms_str.split(":"))
    return d * 3600 + m * 60 + s


# name: (sign index, "DD:MM:SS" within sign) from the PL table
PL = {"Sun": (2, "06:57:34"), "Moon": (5, "28:32:23"), "Mars": (6, "02:41:34"),
      "Mercury": (3, "01:28:13"), "Jupiter": (0, "05:12:44"), "Venus": (3, "21:49:01"),
      "Saturn": (0, "19:34:28"), "Rahu": (3, "20:05:39"), "Ketu": (9, "20:05:39")}


@pytest.mark.parametrize("planet", PL)
def test_positions(planet):
    sign, pos = PL[planet]
    p = C.points[planet]
    assert p.sign == sign
    tol = 30 if planet in ("Rahu", "Ketu") else 3  # true-node models differ slightly
    assert abs(p.deg * 3600 - arcsec(pos)) < tol


def test_ascendant():
    assert C.asc.sign == 9 and abs(C.asc.deg * 3600 - arcsec("11:29:07")) < 10


def test_dignity_avastha_karakas():
    assert C.dignity("Saturn") == "Debilitated"
    assert C.dignity("Moon") == "Great friend"
    assert C.dignity("Sun") == "Friend" and C.dignity("Mercury") == "Neutral"
    assert [C.avastha(p) for p in ("Sun", "Moon", "Mercury", "Saturn")] == \
        ["Youth", "Infant", "Dead", "Old"]
    assert C.chara_karakas() == {"AK": "Moon", "AmK": "Venus", "BK": "Saturn", "MK": "Sun",
                                 "PiK": "Jupiter", "GK": "Mars", "DK": "Mercury"}


def test_nakshatra_kp():
    assert C.asc.nak_name == "Shravana" and kp.lords(C.asc.lon) == ("Moon", "Mars", "Saturn")
    assert kp.lords(C.points["Moon"].lon) == ("Mars", "Saturn", "Ketu")
    assert kp.lords(C.points["Venus"].lon) == ("Mercury", "Sun", "Jupiter")
    assert kp.lords(C.points["Ketu"].lon) == ("Moon", "Ketu", "Rahu")


def test_sarvashtakavarga_matches_samudaya_panel():
    assert ashtakavarga.sarva(C) == [31, 26, 27, 28, 24, 24, 25, 38, 26, 27, 32, 29]


def test_arudhas():
    # AL Aries; 2P Gem; 3P/9P Tau; 4P/10P Cap; 5P/11P Vir; 6P/12P Leo; 7P Sco; 8P Ari
    expect = {1: 0, 2: 2, 3: 1, 4: 9, 5: 5, 6: 4, 7: 7, 8: 0, 9: 1, 10: 9, 11: 5, 12: 4}
    assert {h: C.arudha(h) for h in range(1, 13)} == expect


def test_d3_dreshkana():
    d3 = vargas.varga_chart(C, 3)
    assert d3 == {"Ascendant": 1, "Sun": 2, "Moon": 1, "Mars": 6, "Mercury": 3, "Jupiter": 0,
                  "Venus": 11, "Saturn": 4, "Rahu": 11, "Ketu": 5}
    assert abs(vargas.varga_deg(C.asc.lon, 3) - (4 + 27 / 60)) < 0.05


def test_vimshottari_matches_pl():
    maha = [p for p in dasha.vimshottari(C, 1) if len(p.lords) == 1]
    pl = {"Rahu": datetime(2003, 10, 2, 9, 46), "Jupiter": datetime(2021, 10, 1, 18, 24),
          "Saturn": datetime(2037, 10, 1, 15, 24), "Venus": datetime(2080, 10, 1, 1, 20)}
    for p in maha:
        if p.lords[0] in pl and p.start.year > 2000:
            assert abs((p.start - pl[p.lords[0]]).total_seconds()) < 30 * 60


def test_transit_kakshas_5_jan_2025():
    rows = {r["planet"]: r for r in transits.gochara(C, datetime(2025, 1, 5, 15, 28))}
    assert (rows["Sun"]["kaksha"], rows["Sun"]["kaksha_bindu"], rows["Sun"]["bav"]) == ("Mercury", 1, 6)
    assert (rows["Mars"]["kaksha"], rows["Mars"]["kaksha_bindu"]) == ("Jupiter", 0)
    assert (rows["Jupiter"]["kaksha"], rows["Jupiter"]["kaksha_bindu"]) == ("Venus", 1)
    assert rows["Saturn"]["sav"] == 32


def test_cycles_find_planted_cycle():
    rng = np.random.default_rng(0)
    t = np.arange(300)
    x = 100 + 0.2 * t + 6 * np.sin(2 * np.pi * t / 9.6) + rng.normal(0, 3, 300)
    best = cycles.dewey_scan(x, np.arange(5, 30, 0.2), trend_window=21, top=1)[0]
    assert abs(best.period - 9.6) < 0.3 and best.bartels_p < 0.01


def test_great_conjunction_2020():
    dates = [d for d, _ in cycles.great_conjunctions(2019, 2022)]
    assert dates == ["2020-12-21"]


def test_birth_time_windows():
    from astro import rectify
    res = rectify.sweep(C, 60, 70, step=0.5)
    assert rectify.window(res["Lagna sign (D1)"]) == (-43.5, 66.0)
    s, e = rectify.window(res["D9 Navamsa lagna"])
    assert -6 <= s <= -5 and 6.5 <= e <= 7.5
    assert len(res["Moon nakshatra-pada"]) == 1  # Moon stays in Chitra-2 all window
