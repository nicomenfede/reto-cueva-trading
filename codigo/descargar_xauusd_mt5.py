"""Descarga XAUUSD en velas de 1 hora desde MetaTrader 5 (MT5 abierto y con sesión iniciada).
Guarda el crudo tal cual, con las fechas en la hora del servidor del bróker.
Uso: python codigo/descargar_xauusd_mt5.py
"""
import MetaTrader5 as mt5
import pandas as pd

SIMBOLO = "XAUUSD"
MAX_VELAS = 99999  # pedir 100000 da "Invalid params"; MT5 entrega las que tenga
SALIDA = "datos/crudos/xauusd_1h_mt5.csv"

if not mt5.initialize(timeout=30000):
    raise SystemExit(f"No se pudo conectar con MT5: {mt5.last_error()}")
mt5.symbol_select(SIMBOLO, True)
velas = mt5.copy_rates_from_pos(SIMBOLO, mt5.TIMEFRAME_H1, 0, MAX_VELAS)
error = mt5.last_error()
mt5.shutdown()
if velas is None or len(velas) == 0:
    raise SystemExit(f"MT5 no devolvió velas: {error}")

df = pd.DataFrame(velas)
df["time"] = pd.to_datetime(df["time"], unit="s")
df = df.rename(columns={"tick_volume": "volume"})
df[["time", "open", "high", "low", "close", "volume", "spread"]].to_csv(SALIDA, index=False)
print(f"{len(df)} velas · {df['time'].iloc[0]} a {df['time'].iloc[-1]} · {SALIDA}")
