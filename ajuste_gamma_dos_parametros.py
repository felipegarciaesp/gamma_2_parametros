import numpy as np
from scipy.stats import gamma

# Tus valores
lista_valores = [
    2650.0, 750.0, 2400.0, 1700.0, 1650.0, 1600.0, 3000.0, 1750.0, 1300.0, 1100.0,
    850.0, 1500.0, 950.0, 610.0, 850.0, 1500.0, 1250.0, 1300.0, 1950.0, 2100.0,
    800.0, 1250.0, 850.0, 1100.0, 1400.0, 1750.0, 700.0, 3200.0, 390.0, 2800.0
]

# Ajuste gamma de dos parámetros (loc=0)
shape, loc, scale = gamma.fit(lista_valores, floc=0)

print("Resultados para gamma de dos parámetros (loc=0):")
print(f"  shape (k)  = {shape}")
print(f"  loc        = {loc}")
print(f"  scale (θ)  = {scale}")

# Media y desviación estándar teóricas
media = shape * scale
desv_std = np.sqrt(shape) * scale
print(f"  Media teórica      = {media}")
print(f"  Desv. estándar teórica = {desv_std}")

# Para comparar: media y std muestral de tus datos
media_muestra = np.mean(lista_valores)
std_muestra = np.std(lista_valores, ddof=1)
print(f"  Media muestral     = {media_muestra}")
print(f"  Desv. estándar muestral = {std_muestra}")