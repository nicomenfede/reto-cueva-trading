"""Mide la ficha técnica de XAUUSD (activos/xauusd.md) con el CSV curado.
Desde 2012: antes, el horario del servidor no es estable. Solo lee datos y escribe en pantalla.
Uso: python codigo/xauusd_ficha_tecnica.py
"""
import numpy as np
import pandas as pd

INICIO = "2012-01-01"
d = pd.read_csv("datos/xauusd_1h_mt5.csv", parse_dates=["fecha"]).set_index("fecha")
d = d[d.index >= pd.Timestamp(INICIO, tz="UTC")]
d.index = d.index.tz_convert("America/New_York")
d["rango_pct"] = (d.high - d.low) / d.open * 100
d["ret"] = np.log(d.close).diff()
d = d.iloc[1:]

# Día de sesión: empieza a las 17:00 de Nueva York
sesion = (d.index.tz_localize(None) + pd.Timedelta(hours=7)).normalize()
dia = d.groupby(sesion).agg(open=("open", "first"), high=("high", "max"), low=("low", "min"),
                            close=("close", "last"), velas=("close", "size"))
dia = dia[(dia.velas >= 12) & (dia.index.weekday < 5)]
dia["ret"] = np.log(dia.close).diff()
dia["rango_usd"] = dia.high - dia.low
dia["rango_pct"] = dia.rango_usd / dia.open * 100
dia = dia.iloc[1:]

print("HISTORIA", d.index[0], d.index[-1], "velas", len(d), "dias", len(dia))
print("\nRANGO DIARIO")
print(" toda: mediana %.2f%% media %.2f%%" % (dia.rango_pct.median(), dia.rango_pct.mean()))
u = dia.tail(252)
print(" ultimos 252 dias: mediana %.2f%% = %.1f USD" % (u.rango_pct.median(), u.rango_usd.median()))
print(dia.groupby(dia.index.year).rango_pct.median().round(2).to_dict())

print("\nRANGO POR HORA NY (mediana %, toda / ultimos 3 anios / velas)")
r3 = d[d.index >= d.index[-1] - pd.Timedelta(days=1095)]
t = pd.DataFrame({"toda": d.groupby(d.index.hour).rango_pct.median(),
                  "u3": r3.groupby(r3.index.hour).rango_pct.median(),
                  "n": d.groupby(d.index.hour).size()}).round(3)
print(t.to_string())
top = d.groupby([d.index.year, d.index.hour]).rango_pct.median().unstack()
print("hora de mayor rango por anio:", top.idxmax(axis=1).to_dict())

print("\nMEJORES Y PEORES DIAS (% cierre a cierre)")
p = (np.exp(dia.ret) - 1) * 100
print(p.nlargest(5).round(2).to_string()); print(p.nsmallest(5).round(2).to_string())
print("\nMAYORES VELAS DE 1H (%)")
ph = (np.exp(d.ret) - 1) * 100
print(ph.abs().nlargest(6).index.strftime("%Y-%m-%d %H:%M NY").tolist(), ph.loc[ph.abs().nlargest(6).index].round(2).tolist())

print("\nLINEA BASE")
print(" velas 1h al alza %.1f%% (planas %.1f%%)" % ((d.close > d.open).mean() * 100, (d.close == d.open).mean() * 100))
print(" dias al alza %.1f%%" % ((dia.close > dia.open).mean() * 100))


def razon_varianzas(x, q):
    """Lo-MacKinlay: razón de varianzas y su z robusto a volatilidad cambiante."""
    x = np.asarray(x.dropna()); n = len(x); mu = x.mean(); e = x - mu
    v1 = (e ** 2).sum() / (n - 1)
    s = np.convolve(x, np.ones(q), "valid")
    m = q * (n - q + 1) * (1 - q / n)
    vq = ((s - q * mu) ** 2).sum() / m
    vr = vq / v1
    theta = 0.0
    den = (e ** 2).sum() ** 2
    for j in range(1, q):
        delta = n * ((e[j:] ** 2) * (e[:-j] ** 2)).sum() / den
        theta += (2 * (q - j) / q) ** 2 * delta
    return vr, np.sqrt(n) * (vr - 1) / np.sqrt(theta)


for nombre, x, qs in (("1 HORA", d.ret, (2, 6, 24)), ("DIARIO", dia.ret, (2, 5, 20))):
    print("\nPERSONALIDAD", nombre)
    a = x.autocorr(1); n = x.count()
    print(" autocorrelacion lag1 %.4f (ruido +-%.4f)" % (a, 2 / np.sqrt(n)))
    for q in qs:
        print(" razon varianzas q=%d: %.3f z=%.2f" % ((q,) + razon_varianzas(x, q)))
    q = qs[-1]
    anual = {int(y): (round(float(g.autocorr(1)), 3), round(float(razon_varianzas(g, q)[0]), 2), round(float(razon_varianzas(g, q)[1]), 1))
             for y, g in x.groupby(x.index.year) if g.count() > 3 * q}
    print(" por anio (autocorr, RV q=%d, z):" % q, anual)
    print(" anios autocorr>0: %d de %d · RV>1: %d de %d · |z|>2: %d" % (
        sum(v[0] > 0 for v in anual.values()), len(anual), sum(v[1] > 1 for v in anual.values()), len(anual),
        sum(abs(v[2]) > 2 for v in anual.values())))

print("\nSPREAD EN PUNTOS (el que guarda MT5 en cada vela; 1 punto = 0,01 USD)")
c = pd.read_csv("datos/crudos/xauusd_1h_mt5.csv", parse_dates=["time"]).set_index("time")
c = c[c.index >= "2025-11-05"]
c.index = c.index.tz_localize("Europe/Athens", ambiguous="NaT", nonexistent="NaT").tz_convert("America/New_York")
print(" ultimo anio mediana", c.spread.median(), "p95", c.spread.quantile(.95), "max", c.spread.max())
print(" por hora NY:", c.groupby(c.index.hour).spread.median().to_dict())
