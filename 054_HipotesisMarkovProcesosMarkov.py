"""
created on 7 Abril 12:19:09 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código define una clase CadenaMarkov que representa y simula una cadena de
Markov. Esta clase permite inicializar la cadena con una matriz de transición
y una lista de estados, calcular el próximo estado de acuerdo con la matriz de
transición y generar una secuencia de estados a partir de un estado inicial.
En resumen, el código simula y genera secuencias de estados para una cadena de
Markov específica.
"""
import numpy as np

class CadenaMarkov:
    def __init__(self, matriz_transicion, estados):
        # Inicializa la cadena de Markov con la matriz de transición y los estados.
        self.matriz_transicion = matriz_transicion
        self.estados = estados
        self.num_estados = len(estados)

    def siguiente_estado(self, estado_actual):
        # Calcula el próximo estado de acuerdo con la matriz de transición.
        return np.random.choice(self.estados, p=self.matriz_transicion[estado_actual])

    def generar_estados(self, estado_inicial, num_pasos):
        # Genera una secuencia de estados de acuerdo con la matriz de transición.
        estado_actual = estado_inicial
        secuencia_estados = [estado_actual]
        for _ in range(num_pasos - 1):
            estado_actual = self.siguiente_estado(estado_actual)
            secuencia_estados.append(estado_actual)
        return secuencia_estados

# Definición de la matriz de transición y los estados
matriz_transicion = np.array([[0.7, 0.3], [0.4, 0.6]])  # Ejemplo de matriz de transición
estados = [0, 1]  # Ejemplo de estados: 0 y 1

# Crear la cadena de Markov
cadena_markov = CadenaMarkov(matriz_transicion, estados)

# Generar una secuencia de estados a partir de un estado inicial
estado_inicial = 0  # Estado inicial
num_pasos = 10  # Número de pasos en el tiempo
secuencia_estados = cadena_markov.generar_estados(estado_inicial, num_pasos)

print("Secuencia de estados generada por la cadena de Markov:")
print(secuencia_estados)
