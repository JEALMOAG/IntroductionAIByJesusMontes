"""
created on 7 Abril 18:57:26 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código presenta una implementación de un Modelo Oculto de Markov (HMM) en
Python. Define una clase HMM que inicializa el modelo con parámetros como
estados, observaciones, matrices de transición y de emisión, y distribución
inicial de probabilidades de los estados. Utiliza el algoritmo de avance para
calcular la probabilidad de una secuencia de observaciones dada y proporciona
un método para obtener esta probabilidad.
"""

import numpy as np
# Importar la biblioteca NumPy para manipulación de matrices

class HMM:
    def __init__(self, estados, observaciones, matriz_transicion, matriz_emision, distribucion_inicial):
        # Inicializar el HMM con los parámetros dados
        self.estados = estados  # Lista de nombres de los estados del HMM
        self.observaciones = observaciones  # Lista de nombres de las observaciones del HMM
        self.matriz_transicion = matriz_transicion  # Matriz de transición entre estados
        self.matriz_emision = matriz_emision  # Matriz de emisión de observaciones por estados
        self.distribucion_inicial = distribucion_inicial  # Distribución inicial de probabilidades de los estados

    def avance(self, secuencia_observaciones):
        T = len(secuencia_observaciones)  # Longitud de la secuencia de observaciones
        N = len(self.estados)  # Número de estados en el HMM

        # Inicializar la matriz de avance (forward) alpha
        alpha = np.zeros((T, N))

        # Paso de inicialización
        alpha[0, :] = self.distribucion_inicial * self.matriz_emision[:, self.observaciones.index(secuencia_observaciones[0])]

        # Paso de recursión
        for t in range(1, T):
            for j in range(N):
                alpha[t, j] = np.sum(alpha[t - 1, :] * self.matriz_transicion[:, j]) * \
                              self.matriz_emision[j, self.observaciones.index(secuencia_observaciones[t])]

        return alpha

    def verosimilitud(self, secuencia_observaciones):
        # Calcular la probabilidad total de una secuencia de observaciones usando el algoritmo de avance
        return np.sum(self.avance(secuencia_observaciones)[-1, :])

# Definir los estados y las observaciones
estados = ['Despejado', 'Nublado']  # Dos estados posibles del tiempo
observaciones = ['Seco', 'Humedo']   # Dos observaciones posibles del tiempo

# Definir la matriz de transición
matriz_transicion = np.array([[0.7, 0.3],  # Probabilidades de transición de estado a estado
                               [0.4, 0.6]])

# Definir la matriz de emisión
matriz_emision = np.array([[0.9, 0.1],  # Probabilidades de observar cada observación en cada estado
                            [0.2, 0.8]])

# Definir la distribución inicial de probabilidades de los estados
distribucion_inicial = np.array([0.6, 0.4])  # Probabilidad inicial de estar en cada estado

# Crear el modelo HMM con los parámetros definidos
modelo_hmm = HMM(estados, observaciones, matriz_transicion, matriz_emision, distribucion_inicial)

# Calcular la probabilidad de una secuencia de observaciones dada
secuencia_observaciones = ['Seco', 'Humedo', 'Seco']  # Ejemplo de secuencia de observaciones
verosimilitud = modelo_hmm.verosimilitud(secuencia_observaciones)
print("La probabilidad de la secuencia de observaciones es:", verosimilitud)
