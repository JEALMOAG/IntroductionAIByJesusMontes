"""
created on 6 april 15:36:26 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código simula el lanzamiento de una moneda sesgada y luego ajusta la
probabilidad de que la moneda sea justa basándose en los resultados.
Comienza lanzando la moneda varias veces, calcula la probabilidad de esos
resultados y actualiza la probabilidad a posteriori de que la moneda sea justa.
Finalmente, muestra los resultados, incluyendo la secuencia de lanzamientos y
la probabilidad a posteriori.
"""
import random

# Definimos la función para simular lanzamientos de una moneda
def lanzar_moneda(prob_caras):
    """
    Simula el lanzamiento de una moneda sesgada hacia caras.
    Retorna True si sale cara, False si sale cruz.
    """
    if random.random() < prob_caras:
        return True
    else:
        return False

# Definimos la función para calcular la verosimilitud de los datos observados
def calcular_verosimilitud(datos, prob_caras):
    """
    Calcula la verosimilitud de una secuencia de lanzamientos de moneda
    dada una cierta probabilidad de que la moneda sea justa.
    """
    verosimilitud = 1.0
    for resultado in datos:
        if resultado:  # Si es cara
            verosimilitud *= prob_caras
        else:          # Si es cruz
            verosimilitud *= 1 - prob_caras
    return verosimilitud

# Definimos la función para actualizar la probabilidad a posteriori
def actualizar_prob_a_posteriori(prob_previa, verosimilitud, const_normalizacion):
    """
    Actualiza la probabilidad a posteriori utilizando la ponderación de verosimilitud.
    """
    return (prob_previa * verosimilitud) / const_normalizacion

# Parámetros iniciales
prob_previa = 0.5  # Probabilidad a priori de que la moneda sea justa
prob_real_caras = 0.6  # Probabilidad real de que la moneda salga cara
num_lanzamientos = 10  # Número de lanzamientos

# Simulamos una secuencia de lanzamientos de la moneda
datos_observados = [lanzar_moneda(prob_real_caras) for _ in range(num_lanzamientos)]

# Calculamos la verosimilitud de los datos observados
verosimilitud = calcular_verosimilitud(datos_observados, prob_real_caras)

# Calculamos la constante de normalización
const_normalizacion = verosimilitud * prob_previa + (1 - verosimilitud) * (1 - prob_previa)

# Actualizamos la probabilidad a posteriori
probabilidad_posteriori = actualizar_prob_a_posteriori(prob_previa, verosimilitud, const_normalizacion)

# Mostramos los resultados
print("Secuencia de lanzamientos observada:", datos_observados)
print("Verosimilitud de los datos observados:", verosimilitud)
print("Probabilidad a posteriori de que la moneda sea justa:", probabilidad_posteriori)
