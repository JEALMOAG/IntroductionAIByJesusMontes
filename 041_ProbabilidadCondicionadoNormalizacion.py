"""
created on 4 april 23:43:13 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código proporciona funciones para calcular la probabilidad condicionada 
P(A∣B) dados P(A∩B) y P(B), así como para normalizar un conjunto de datos
para que tengan media 0 y desviación estándar 1. Luego, se ilustra un ejemplo
de cálculo de probabilidad condicionada y normalización de datos.
"""
import numpy as np

# Definimos una función para calcular la probabilidad condicionada
def calcular_probabilidad_condicionada(evento_A, evento_B):
    """
    Calcula la probabilidad condicionada P(A|B) dada P(A∩B) y P(B).
    """
    return evento_A / evento_B

# Definimos una función para normalizar un conjunto de datos
def normalizar_datos(datos):
    """
    Normaliza un conjunto de datos para que tengan media 0 y desviación estándar 1.
    """
    media = np.mean(datos)
    desviacion_estandar = np.std(datos)
    datos_normalizados = (datos - media) / desviacion_estandar
    return datos_normalizados

# Ejemplo de cálculo de probabilidad condicionada
# Supongamos que P(B) = 0.6 y P(A∩B) = 0.3
probabilidad_B = 0.6
probabilidad_A_interseccion_B = 0.3

# Calculamos P(A|B)
probabilidad_A_dado_B = calcular_probabilidad_condicionada(probabilidad_A_interseccion_B, probabilidad_B)
print("La probabilidad condicionada P(A|B) es:", probabilidad_A_dado_B)

# Ejemplo de normalización de datos
# Supongamos que tenemos un conjunto de datos
datos = np.array([1, 2, 3, 4, 5])

# Normalizamos los datos
datos_normalizados = normalizar_datos(datos)
print("Datos normalizados:", datos_normalizados)

