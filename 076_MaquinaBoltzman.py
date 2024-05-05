"""
created on 10 Abril 22:45:09 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa una función para calcular la activación de una máquina
de Boltzmann, un modelo probabilístico en el campo del aprendizaje automático.
La función activacion_boltzmann toma una entrada, pesos y sesgos como argumentos
y devuelve la activación de la máquina de Boltzmann para esa entrada dada una
configuración específica de pesos y sesgos. Luego, se utiliza un conjunto de
datos de ejemplo junto con los pesos y sesgos proporcionados para calcular la
activación de la máquina de Boltzmann y se imprime el resultado.
"""
import numpy as np

# Función de activación de la máquina de Boltzmann
def activacion_boltzmann(x, pesos, sesgo):
    energia = -0.5 * np.dot(np.dot(x, pesos), x) - np.dot(sesgo, x)
    return 1 / (1 + np.exp(-2 * energia))

# Datos de entrada, pesos y sesgo
entrada = np.array([1, -1, 1])
pesos = np.array([[0, 1, -1],
                  [1, 0, -1],
                  [-1, -1, 0]])
sesgo = np.array([0, 0, 0])

# Calcula la activación de la máquina de Boltzmann
activacion = activacion_boltzmann(entrada, pesos, sesgo)
print("Activación de la máquina de Boltzmann:", activacion)
