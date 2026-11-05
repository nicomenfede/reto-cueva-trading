# Ficha técnica · XAUUSD (oro contra dólar)

Estado: MEDIDO con datos de la cuenta demo MetaQuotes-Demo. Faltan los costos de tu bróker real.
Última revisión: 2026-11-05.

Cómo leerla:
- **MEDIDO:** sale de datos/xauusd_1h_mt5.csv, desde enero de 2012 hasta el 2026-11-05.
  Se repite con `python codigo/xauusd_ficha_tecnica.py`.
- **CONOCIMIENTO GENERAL:** cómo funciona el mercado del oro. No es un resultado tuyo.
- **PENDIENTE:** falta el dato. No se inventa.

## Qué es
Precio de una onza de oro en dólares. Se opera sobre todo como CFD (un contrato que sigue
el precio, sin tener el oro) o al contado. No tiene una bolsa central: cada bróker da su
precio y su volumen es «de ticks», o sea, cuántas veces cambió el precio en ese bróker, no
cuánto oro se negoció.

## Personalidad

### ¿Tendencia o reversión a la media?
Resultado MEDIDO: **ninguna de las dos.** Ni en 1 hora ni en diario aparece un sesgo claro y
estable. Mirando solo los retornos anteriores, el precio se comporta casi como un camino al azar.

Tendencia significa que una subida suele seguir de más subida. Reversión a la media
significa que el precio tiende a volver a su promedio después de alejarse.

- **Autocorrelación** (si una vela se parece a la anterior; positiva: tendencia, negativa:
  reversión): 1 hora -0,008, apenas fuera de la banda de ruido (±0,007) y demasiado pequeña
  para importar. Diario 0,003, dentro del ruido (±0,032).
- **Razón de varianzas** (por encima de 1: tendencia; por debajo de 1: reversión). El valor z
  dice si se aleja del azar; hace falta más de 2 para tomarlo en serio.
  1 hora: 0,99 a 2 velas (z -1,0) · 0,99 a 6 (z -0,8) · 1,03 a 24 (z 0,8).
  Diario: 1,00 a 2 días (z 0,1) · 0,97 a 5 (z -0,6) · 0,90 a 20 (z -0,9).
- **Estabilidad año por año** (15 años): en 1 hora, la razón a 24 velas pasa de 1 en 8 años;
  en diario, la razón a 20 días pasa de 1 en 5 años. Ningún año llega a z 2.

Límite: esto mide el comportamiento promedio. No descarta una ventaja bajo una condición
concreta, como una hora o una noticia: eso lo prueba cada hipótesis en su fase 02.

### ¿En qué horario se mueve más?
Resultado MEDIDO: **de 08:00 a 10:59 de Nueva York.** Es la hora de mayor movimiento los 15 años.

Rango mediano por vela de 1 hora, en % del precio, hora de Nueva York (toda la muestra · últimos 3 años):
- 08:00 a 10:59, el pico: 0,39 a 0,41 · 0,42 a 0,50
- 11:00: 0,29 · 0,36
- 02:00 a 04:59, mañana de Londres: 0,21 a 0,25 · 0,27 a 0,28
- 20:00 a 21:59, sesión asiática: 0,19 a 0,21 · 0,27 a 0,33
- 14:00 a 16:59, final de Nueva York: 0,12 a 0,18 · 0,14 a 0,21
- 23:00 a 00:59, lo más tranquilo de la noche: 0,13 a 0,14 · 0,20 a 0,21

Sorpresa frente a lo esperado: en los últimos 3 años, las 21:00 de Nueva York se mueven más que
la mañana de Londres. La sesión asiática ya no es la parte tranquila que se suponía.

Horas clave, en hora local de cada ciudad (CONOCIMIENTO GENERAL):
- 08:00 Londres: empieza la sesión europea.
- 10:30 y 15:00 Londres: subastas del precio de referencia del oro (LBMA).
- 08:20 Nueva York: apertura tradicional del oro en COMEX, la bolsa de futuros.
- 08:30 Nueva York: salen muchos datos de EE. UU.
- 14:00 Nueva York: decisión de tasas de la Reserva Federal, los días que la hay.

### ¿Qué lo mueve?
CONOCIMIENTO GENERAL. Son fuerzas, no reglas: a veces fallan o chocan entre sí.
- **Tasas reales de EE. UU.** (tasa de interés menos inflación): el oro no paga intereses,
  así que suele sufrir cuando suben y mejorar cuando bajan.
- **Dólar:** el oro se cotiza en dólares, y suele moverse al contrario.
- **Reserva Federal y datos de EE. UU.:** decisiones de tasas, inflación (IPC) y empleo (NFP).
- **Miedo:** guerras, crisis financieras o caídas fuertes de la bolsa pueden llevar dinero
  al oro como refugio.
- **Bancos centrales:** sus compras y ventas pesan en el fondo del mercado.
- **Fondos cotizados de oro (ETF) y futuros:** las entradas y salidas de grandes inversores.
- **Demanda física:** joyería e inversión, sobre todo en China e India.

## Lo que dicen los datos
MEDIDO. Un día de sesión empieza a las 17:00 de Nueva York.
- Historia usada: 2012-01-02 a 2026-11-05 · 87.250 velas de 1 hora · 3.828 días.
- Calidad: APTA CON AVISOS (resultados/xauusd_1h_mt5_calidad.md).
- Rango diario mediano: 1,23 % en toda la muestra. Últimos 252 días: 2,17 % (96,1 USD).
- Por año: entre 0,88 % (2018) y 2,22 % (2026). El año 2026 es el más agitado de la muestra.
- Línea base, velas de 1 hora al alza: 50,3 %.
- Línea base, días al alza: 51,7 %.
- Mejores días: 2026-02-03 +6,17 % · 2016-06-24 +4,75 % · 2020-03-24 +4,70 %.
- Peores días: 2013-04-15 -9,06 % · 2026-01-30 -8,96 % · 2020-08-11 -5,67 %.
- Mayor vela de 1 hora: 2026-01-29 10:00 Nueva York, -5,71 %.
- Días extremos: PENDIENTE de que confirmes en el gráfico que son reales.

## Lo que dice tu bróker
De la cuenta demo MetaQuotes-Demo, consultada el 2026-11-05. No son los costos de un bróker real.
- Bróker real: PENDIENTE. Símbolo en la demo: XAUUSD.
- Spread (diferencia entre compra y venta) guardado por MT5 en el último año: mediana 4 puntos
  (0,04 USD), 10 puntos en el 5 % más alto de las velas. Junto a la pausa diaria llega a 140 puntos.
  Es un dato de demo y por vela: no sirve como costo final de la fase 04.
- Comisión por operación: PENDIENTE (MT5 no la entrega en las especificaciones del símbolo).
- Swap (costo por dejar la operación abierta de noche): compra -12,6 puntos, venta -4,6 puntos.
- Tamaño del contrato: 100 onzas. Lote mínimo y paso: 0,01.
- Hora del servidor: Europe/Athens (GMT+2 en invierno, GMT+3 en verano). Comprobada: los datos de
  empleo de EE. UU. (08:30 Nueva York) caen en la vela de las 15:00 del servidor desde 2012.
- Pausa diaria: 17:00 a 18:00 de Nueva York. Desde abril de 2026 se ve de 16:00 a 18:00.

## Avisos para el backtest
- El spread se abre en noticias y en la pausa diaria: un costo fijo puede quedarse corto.
- El precio puede saltar entre el viernes y el domingo: un stop no garantiza el precio de salida.
- El precio y el volumen de ticks cambian según la fuente: mejor medir con los datos de tu bróker.
- Un nivel de precio de hace años no se compara con el de hoy: mide el movimiento en %.
- Antes de 2012, el horario del servidor no es estable y faltan velas nocturnas: no uses esas
  fechas para reglas por hora. El CSV curado las conserva, pero esta ficha no las usa.
- Antes de octubre de 2010 no hay spread guardado (viene en 0).
- La volatilidad de 2026 es casi el doble de la habitual: un stop fijo en dólares no significa lo
  mismo en 2018 que hoy.
- Esta ficha miró toda la historia, incluido lo que luego sería fuera de muestra. Si una idea nace
  de lo que ves aquí, esa idea ya conoce esos años: pruébala también con datos que no haya visto,
  como otro activo.
