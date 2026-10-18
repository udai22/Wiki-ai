"""Cycle analysis toolkit: Edward R. Dewey's methods, Chizhevsky's solar-cycle phases,
and planetary cycles (Jupiter-Saturn 'great conjunctions', Barbault's cyclic index).

Dewey's workflow (Foundation for the Study of Cycles, 1941-):
  1. detrend: divide the series by a centred moving average (ratio-to-trend)
  2. search: scan candidate periods (periodogram)
  3. test:   Bartels test - is the cycle's amplitude consistent across segments?
  4. synthesize: add the surviving sine waves and project forward
Caveat that Dewey himself stressed: scanning many periods guarantees some spurious
peaks. Only trust cycles that pass Bartels *and* hold up on data not used to find them.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
import swisseph as swe


# ---------------------------------------------------------------- Dewey methods
def ratio_to_trend(x, window: int) -> np.ndarray:
    """Dewey's detrending: value / centred moving average. NaN at the edges."""
    x = np.asarray(x, float)
    if window % 2 == 0:  # 2xN centred average for even windows
        k = np.r_[0.5, np.ones(window - 1), 0.5] / window
    else:
        k = np.ones(window) / window
    ma = np.convolve(x, k, mode="same")
    half = len(k) // 2
    ma[:half] = np.nan
    ma[len(x) - half:] = np.nan
    return x / ma


def fit_sine(x, period: float):
    """Least-squares sine of a fixed period. Returns (amplitude, phase, fitted)."""
    x = np.asarray(x, float)
    t = np.arange(len(x))
    ok = ~np.isnan(x)
    w = 2 * math.pi / period
    A = np.c_[np.cos(w * t), np.sin(w * t), np.ones(len(t))]
    coef, *_ = np.linalg.lstsq(A[ok], x[ok], rcond=None)
    amp = math.hypot(coef[0], coef[1])
    phase = math.atan2(-coef[1], coef[0])
    return amp, phase, A @ coef


def periodogram(x, periods) -> list[tuple[float, float]]:
    """Amplitude of the best-fitting sine at each candidate period, strongest first."""
    res = [(p, fit_sine(x, p)[0]) for p in periods]
    return sorted(res, key=lambda r: -r[1])


def bartels(x, period: float) -> float:
    """Bartels test (1935): probability the cycle is chance.

    Splits the data into whole cycles, fits each one's amplitude vector, and compares
    the length of their sum with what random phases would give. Values below 0.05
    are conventionally 'significant'; Dewey favoured < 0.01 (1 in 100).
    """
    x = np.asarray(x, float)
    p = int(round(period))
    n = len(x) // p
    if n < 2:
        return float("nan")
    w = 2 * math.pi / period
    vecs = []
    for i in range(n):
        seg = x[i * p:(i + 1) * p]
        t = np.arange(i * p, (i + 1) * p)
        ok = ~np.isnan(seg)
        if ok.sum() < 3:
            continue
        s = seg[ok] - seg[ok].mean()
        a = 2 / ok.sum() * np.sum(s * np.cos(w * t[ok]))
        b = 2 / ok.sum() * np.sum(s * np.sin(w * t[ok]))
        vecs.append(complex(a, b))
    if len(vecs) < 2:
        return float("nan")
    vecs = np.array(vecs)
    expected = math.sqrt(np.mean(np.abs(vecs) ** 2) * len(vecs))
    observed = abs(vecs.sum())
    return math.exp(-(observed / expected) ** 2)


def synthesize(x, periods, horizon: int = 0) -> np.ndarray:
    """Sum of fitted sines for the given periods, extended `horizon` steps ahead."""
    x = np.asarray(x, float)
    t = np.arange(len(x) + horizon)
    ok = ~np.isnan(x)
    cols = [np.ones(len(t))]
    for p in periods:
        w = 2 * math.pi / p
        cols += [np.cos(w * t), np.sin(w * t)]
    A = np.c_[tuple(cols)]
    coef, *_ = np.linalg.lstsq(A[:len(x)][ok], x[ok], rcond=None)
    return A @ coef


@dataclass
class CycleReport:
    period: float
    amplitude: float
    bartels_p: float


def dewey_scan(x, periods, trend_window: int | None = None, top: int = 5) -> list[CycleReport]:
    """The full Dewey pipeline: detrend, periodogram, Bartels-test the strongest peaks."""
    y = ratio_to_trend(x, trend_window) if trend_window else np.asarray(x, float)
    return [CycleReport(p, a, bartels(y, p)) for p, a in periodogram(y, periods)[:top]]


# Cycles Dewey's Foundation catalogued as recurring across unrelated series (years)
DEWEY_CYCLES = {
    "Kitchin (inventory)": 3.42, "Dewey 'stock market' 41-month": 41 / 12,
    "Juglar (investment)": 9.0, "Dewey 9.6-year (lynx, tent caterpillars, salmon)": 9.6,
    "Schwabe (sunspot)": 11.1, "Dewey 17.75-year": 17.75, "Dewey 18.2-year": 18.2,
    "Kuznets (building)": 18.33, "Hale (magnetic solar)": 22.2, "Kondratiev wave": 54.0,
}

# Mean synodic/orbital periods (years) that cycle researchers compare against
PLANETARY_PERIODS = {
    "Jupiter orbit": 11.862, "Saturn orbit": 29.457, "Jupiter-Saturn synodic": 19.859,
    "Jupiter-Saturn trigon (3 conjunctions)": 59.58, "Saturn-Uranus synodic": 45.36,
    "Saturn-Neptune synodic": 35.87, "Saturn-Pluto synodic": 33.4,
    "Jupiter-Uranus synodic": 13.81, "Uranus-Neptune synodic": 171.4,
    "Lunar node (Rahu) cycle": 18.613, "Metonic": 19.0, "Saros": 18.03,
}


# ---------------------------------------------------------------- Chizhevsky
# Approximate solar-cycle minima (decimal years, SILSO 13-month smoothed sunspot number)
SOLAR_MINIMA = [1755.2, 1766.5, 1775.5, 1784.7, 1798.3, 1810.6, 1823.3, 1833.9, 1843.5,
                1855.9, 1867.2, 1878.9, 1890.2, 1902.0, 1913.6, 1923.6, 1933.8, 1944.2,
                1954.3, 1964.9, 1976.5, 1986.8, 1996.4, 2008.9, 2019.9]

# Chizhevsky (1924): each ~11-yr cycle has four phases; share of 'mass excitability'
# events he tallied in each. Phase lengths are his idealised 3/2/3/3 years.
CHIZHEVSKY_PHASES = [("I. minimum excitability", 3, 0.05), ("II. rising excitability", 2, 0.20),
                     ("III. maximum excitability", 3, 0.60), ("IV. declining excitability", 3, 0.15)]


SOLAR_MAXIMA = [1761.5, 1769.7, 1778.4, 1788.1, 1805.2, 1816.4, 1829.9, 1837.2, 1848.1,
                1860.1, 1870.6, 1883.9, 1894.1, 1906.2, 1917.6, 1928.4, 1937.4, 1947.4,
                1958.2, 1968.9, 1979.9, 1989.6, 2001.9, 2014.3, 2024.8]


def chizhevsky_phase(year: float) -> dict:
    """Which Chizhevsky phase a decimal year falls in.

    Phases are anchored on the observed maximum of the running cycle: III spans the
    3 years centred on the maximum, II the 2 years before it, I runs from the minimum
    up to II, and IV from the end of III to the next minimum.
    """
    i = max(k for k, m in enumerate(SOLAR_MINIMA) if m <= year)
    mx = SOLAR_MAXIMA[i]
    if year >= mx + 1.5:
        name = CHIZHEVSKY_PHASES[3]
    elif year >= mx - 1.5:
        name = CHIZHEVSKY_PHASES[2]
    elif year >= mx - 3.5:
        name = CHIZHEVSKY_PHASES[1]
    else:
        name = CHIZHEVSKY_PHASES[0]
    return {"solar_cycle": i + 1, "minimum": SOLAR_MINIMA[i], "maximum": mx,
            "phase": name[0], "historical_share_of_events": name[2]}


# ---------------------------------------------------------------- planetary cycles
def _lon(jd, body):
    return swe.calc_ut(jd, body, swe.FLG_SWIEPH)[0][0]  # tropical geocentric


def conjunctions(body_a: int, body_b: int, start_year: int, end_year: int,
                 step_days: float = 5.0) -> list[float]:
    """Julian days of geocentric conjunctions between two bodies (refined by bisection)."""
    jd = swe.julday(start_year, 1, 1)
    end = swe.julday(end_year, 1, 1)

    def sep(j):
        return (_lon(j, body_a) - _lon(j, body_b) + 180) % 360 - 180

    out, prev = [], sep(jd)
    while jd < end:
        j2 = jd + step_days
        cur = sep(j2)
        if prev * cur < 0 and abs(prev - cur) < 180:  # sign change, not wraparound
            lo, hi = jd, j2
            for _ in range(40):
                mid = (lo + hi) / 2
                if sep(lo) * sep(mid) <= 0:
                    hi = mid
                else:
                    lo = mid
            out.append((lo + hi) / 2)
        jd, prev = j2, cur
    return out


def great_conjunctions(start_year=1800, end_year=2100) -> list[tuple[str, str]]:
    """Jupiter-Saturn conjunctions (Abu Ma'shar's backbone of mundane astrology).
    Retrograde loops give triple conjunctions; all passes are listed."""
    res = []
    for jd in conjunctions(swe.JUPITER, swe.SATURN, start_year, end_year):
        y, m, d, _ = swe.revjul(jd)
        lon = _lon(jd, swe.JUPITER)
        res.append((f"{y:04d}-{m:02d}-{d:02d}", f"{int(lon % 30)}° {_SIGN[int(lon // 30)]} (tropical)"))
    return res


_SIGN = ["Ari", "Tau", "Gem", "Can", "Leo", "Vir", "Lib", "Sco", "Sag", "Cap", "Aqu", "Pis"]


def barbault_index(year: int, month: int = 1, day: int = 1) -> float:
    """André Barbault's cyclic index: sum of the angular separations (0-180°) of the
    10 pairs among Jupiter, Saturn, Uranus, Neptune, Pluto. Low values = clustering,
    which Barbault linked to world crises (notable lows: early 1940s, 1982-83, 2020-21)."""
    jd = swe.julday(year, month, day)
    bodies = [swe.JUPITER, swe.SATURN, swe.URANUS, swe.NEPTUNE, swe.PLUTO]
    lons = [_lon(jd, b) for b in bodies]
    tot = 0.0
    for i in range(5):
        for j in range(i + 1, 5):
            d = abs(lons[i] - lons[j]) % 360
            tot += min(d, 360 - d)
    return tot
