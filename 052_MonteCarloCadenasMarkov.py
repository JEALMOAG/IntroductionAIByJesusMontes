"""
created on 6 april 20:56:23 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa el método de Monte Carlo para cadenas de Markov (MCMC)
con el objetivo de generar muestras de una cadena de Markov dada una matriz
de transición y una función de densidad de probabilidad. Comienza definiendo
la matriz de transición y las funciones necesarias, luego utiliza el algoritmo
MCMC para generar un número especificado de muestras. Finalmente, muestra algunas
de las muestras generadas.
"""
import random

# Definimos la matriz de transición de la cadena de Markov
# En este ejemplo, usaremos una matriz de transición simétrica
matriz_transicion = [[0.5, 0.5],
                     [0.5, 0.5]]

# Función para realizar una transición en la cadena de Markov
def transicion(estado_actual):
    estado_siguiente = random.choices([0, 1], weights=matriz_transicion[estado_actual])[0]
    return estado_siguiente

# Función de densidad de probabilidad (en este ejemplo, simplemente una distribución uniforme)
def funcion_densidad_probabilidad(estado):
    return 0.5

# Función de Monte Carlo para generar muestras de la cadena de Markov
def monte_carlo_mcmc(num_muestras):
    estado_actual = random.choice([0, 1])  # Seleccionamos un estado inicial aleatorio
    muestras = []
    for _ in range(num_muestras):
        estado_propuesto = transicion(estado_actual)
        ratio_aceptacion = funcion_densidad_probabilidad(estado_propuesto) / funcion_densidad_probabilidad(estado_actual)
        if random.random() < ratio_aceptacion:
            estado_actual = estado_propuesto
        muestras.append(estado_actual)
    return muestras

# Número de muestras a generar
num_muestras = 1000

# Generamos las muestras utilizando el método de Monte Carlo para cadenas de Markov
muestras = monte_carlo_mcmc(num_muestras)

# Imprimimos algunas muestras generadas
print("Algunas muestras generadas:", muestras[:10])
