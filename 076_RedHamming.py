"""
created on 11 Abril 01:34:14 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
Este código implementa una red de Hamming, un modelo de red neuronal artificial
utilizado para clasificación binaria. La función activacion_hamming calcula la
activación de la red de Hamming dada una entrada y unos pesos dados.
La entrada y los pesos se proporcionan como matrices NumPy. El resultado de la
activación se imprime al final.
"""
import numpy as np

# Función de activación de la red de Hamming
def activacion_hamming(entrada, pesos):
    return np.dot(entrada, pesos)

# Datos de entrada y pesos
entrada = np.array([1, -1, 1])
pesos = np.array([[1, -1, 1],
                  [-1, 1, -1],
                  [1, -1, 1]])

# Calcula la activación de la red de Hamming
activacion = activacion_hamming(entrada, pesos)
print("Activación de la red de Hamming:", activacion)
