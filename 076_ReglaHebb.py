"""
created on 11 Abril 05:43:28 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa la regla de Hebb para ajustar los pesos de una red neuronal
. Esta regla establece que la fuerza de una conexión sináptica entre dos
neuronas se incrementa cuando ambas neuronas están activadas simultáneamente.
Se proporcionan dos vectores de entrada y se calculan los pesos combinando las
contribuciones individuales de cada entrada usando la regla de Hebb.
"""
import numpy as np

# Regla de Hebb para ajustar los pesos
def regla_hebb(x):
    return np.outer(x, x)

# Datos de entrada
entrada1 = np.array([1, -1, 1])
entrada2 = np.array([-1, 1, -1])

# Calcula los pesos usando la regla de Hebb
pesos = regla_hebb(entrada1) + regla_hebb(entrada2)
print("Pesos ajustados con la regla de Hebb:\n", pesos)
