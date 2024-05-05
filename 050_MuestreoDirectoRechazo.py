"""
created on 6 april 12:34:12 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código estima el valor de Pi utilizando dos métodos de muestreo:
directo y por rechazo. En el método de muestreo directo, genera puntos aleatorios
y calcula la proporción de puntos dentro de un círculo inscrito en un cuadrado.
En el método de muestreo por rechazo, genera puntos aleatorios y los "rechaza"
si caen fuera del círculo. Ambos métodos utilizan una cantidad específica de
puntos aleatorios para la estimación y luego imprimen las estimaciones obtenidas
de Pi.
"""
import random  # Importa la biblioteca random para generar números aleatorios
import math    # Importa la biblioteca math para realizar operaciones matemáticas

# Función para estimar pi utilizando muestreo directo
def estimar_pi_muestreo_directo(cantidad_puntos):
    puntos_dentro_circulo = 0  # Inicializa el contador de puntos dentro del círculo
    for _ in range(cantidad_puntos):  # Repite el proceso para generar cantidad_puntos puntos aleatorios
        x = random.uniform(0, 1)  # Genera una coordenada x aleatoria en el rango [0, 1)
        y = random.uniform(0, 1)  # Genera una coordenada y aleatoria en el rango [0, 1)
        distancia_al_centro = math.sqrt(x**2 + y**2)  # Calcula la distancia al centro del punto generado
        if distancia_al_centro <= 1:  # Si la distancia es menor o igual a 1, el punto está dentro del círculo
            puntos_dentro_circulo += 1  # Incrementa el contador de puntos dentro del círculo
    return 4 * puntos_dentro_circulo / cantidad_puntos  # Devuelve la estimación de pi

# Función para estimar pi utilizando muestreo por rechazo
def estimar_pi_muestreo_por_rechazo(cantidad_puntos):
    puntos_dentro_circulo = 0  # Inicializa el contador de puntos dentro del círculo
    puntos_totales = 0  # Inicializa el contador de puntos totales generados
    while puntos_totales < cantidad_puntos:  # Repite el proceso hasta generar cantidad_puntos puntos
        x = random.uniform(0, 1)  # Genera una coordenada x aleatoria en el rango [0, 1)
        y = random.uniform(0, 1)  # Genera una coordenada y aleatoria en el rango [0, 1)
        distancia_al_centro = math.sqrt(x**2 + y**2)  # Calcula la distancia al centro del punto generado
        if distancia_al_centro <= 1:  # Si la distancia es menor o igual a 1, el punto está dentro del círculo
            puntos_dentro_circulo += 1  # Incrementa el contador de puntos dentro del círculo
        puntos_totales += 1  # Incrementa el contador de puntos totales generados
    return 4 * puntos_dentro_circulo / puntos_totales  # Devuelve la estimación de pi

# Cantidad de puntos para la estimación de pi
cantidad_puntos = 100000

# Estimación de pi utilizando muestreo directo
pi_estimado_directo = estimar_pi_muestreo_directo(cantidad_puntos)
print("Estimación de pi utilizando muestreo directo:", pi_estimado_directo)

# Estimación de pi utilizando muestreo por rechazo
pi_estimado_rechazo = estimar_pi_muestreo_por_rechazo(cantidad_puntos)
print("Estimación de pi utilizando muestreo por rechazo:", pi_estimado_rechazo)
