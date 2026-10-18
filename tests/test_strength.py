"""Shadbala, upagrahas and special points for the reference chart, checked against
Parashara's Light 9.0 (22 Jun 1999 21:35 IST, Mumbai, Lahiri, true node)."""
from datetime import datetime

import swisseph as swe

from astro import special, strength
from astro.chart import Chart

C = Chart(datetime(1999, 6, 22, 21, 35), 5.5, 18.9667, 72.8167, name="reference")
PL_RATIO = {"Sun": 1.51, "Moon": 1.36, "Mars": 1.71, "Mercury": 0.94, "Jupiter": 1.12,
            "Venus": 1.50, "Saturn": 0.99}


def arcmin(lon, sign, deg, minute):
    return abs(lon - (sign * 30 + deg + minute / 60)) * 60


def test_gulika_mandi_match_pl():
    g = special.gulika_mandi(C)
    assert arcmin(g["Gulika"], 8, 26, 18) < 1.5      # PL "Gk 26:18 PSh"
    assert arcmin(g["Mandi"], 8, 17, 2) < 1.5        # PL "Man 17:02 PSh"


def test_be_is_beeja_sphuta():
    s = special.sphutas(C)
    assert arcmin(s["Beeja"], 6, 3, 59) < 1.5        # PL "Be 03:59 Cht"
    assert int(s["Beeja"] // (360 / 27)) == 13       # Chitra
    assert arcmin(s["Bhrigu Bindu"], 6, 3, 59) > 600  # the Bhrigu Bindu is elsewhere


def test_sun_upagrahas():
    u = special.sun_upagrahas(C)
    sun = C.points["Sun"].lon
    assert abs((u["Upaketu"] - sun) % 360 - 330) < 1e-9   # Upaketu = Sun - 30
    assert abs(u["Dhuma"] + u["Vyatipata"] - 360) < 1e-9


def test_shadbala_ratios_close_to_pl():
    sb = strength.shadbala(C)
    exact = {"Mercury", "Jupiter", "Venus", "Saturn"}
    for p, want in PL_RATIO.items():
        got = sb[p]["ratio"]
        if p in exact:
            assert round(got, 2) == want, (p, got)
        else:  # Sun, Moon, Mars: residuals of 3-11 virupas remain (see data-pack-extra.md)
            assert abs(got - want) < 0.035, (p, got)
    rank = sorted(PL_RATIO, key=lambda p: -sb[p]["ratio"])
    assert rank == sorted(PL_RATIO, key=lambda p: -PL_RATIO[p])


def test_shadbala_components():
    sb = strength.shadbala(C)
    assert abs(sb["Saturn"]["uchcha"]) < 0.5           # deep debilitation
    assert abs(sb["Sun"]["naisargika"] - 60) < 1e-9
    assert sb["Mercury"]["natonnata"] == 60
    assert sb["Jupiter"]["tribhaga"] == 60
    assert all(sb[p]["yuddha"] == 0 for p in sb)        # no planetary war in this chart
    for p, r in sb.items():
        assert abs(r["ishta"] ** 2 - r["uchcha"] * strength.chesta(C, p, strength.Options())) < 1e-6


def test_special_lagnas_and_yogi():
    sl = special.special_lagnas(C)
    assert sl["Indu Lagna sign"] == 0                   # Aries
    assert sl["Varnada Lagna sign"] == 2                # Gemini
    y = special.yogi(C)
    assert (y["Yogi"], y["Duplicate Yogi"], y["Avayogi"]) == ("Saturn", "Jupiter", "Moon")


def test_sripati_matches_swiss_and_chalit_shifts():
    sp = special.sripati(C)
    cusps = swe.houses_ex(C.jd, C.lat, C.lon, b"S", C.flags)[0]
    assert all(abs(((a - b) + 180) % 360 - 180) < 1e-6 for a, b in zip(sp["sandhi"], cusps))
    moved = {p: (C.house_of(p), h) for p, h in sp["house"].items() if C.house_of(p) != h}
    assert moved == {"Mars": (10, 9), "Jupiter": (4, 3)}


def test_vimshopaka_range():
    v = strength.vimshopaka(C)
    assert all(0 < x <= 20 for row in v.values() for x in row.values())
