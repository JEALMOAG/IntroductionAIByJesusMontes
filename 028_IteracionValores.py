"""
created on 2 april 15:14:07 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código proporcionado resuelve un problema
de decisión de Markov utilizando el algoritmo
de iteración de valores. Este algoritmo se utiliza
para encontrar los valores óptimos de los estados y
las acciones óptimas en un proceso de decisión secuencial,
donde las decisiones se toman en función de probabilidades
de transición y ganancias asociadas a cada acción en cada
estado. El programa comienza definiendo las ganancias y las
probabilidades de transición, luego itera sobre los valores
de los estados hasta que convergen o se alcanza el número máximo
de iteraciones permitidas. Finalmente, imprime los valores óptimos
de los estados y las acciones óptimas en cada estado.
"""
import numpy as np
# Importación de la biblioteca NumPy

# Definición de la matriz de utilidades
utilidades = np.array([[4, 2],
                       [3, 6],
                       [8, 1]])

# Definición de las probabilidades de transición
probabilidades_transicion = np.array([[1, 0, 0],
                                      [0.8, 0.1, 0.1],
                                      [0, 0, 1]])

# Parámetro de descuento
factor_descuento = 0.9

# Inicialización de los valores de los estados
valores_estados = np.zeros(utilidades.shape[0])

# Definición de la función de iteración de valores
def iteracion_valores():
    global valores_estados  # Se utiliza la palabra clave global para modificar la variable valores definida fuera de la función
    valores_previos = np.copy(valores_estados)  # Copia de los valores actuales para su uso en la actualización
    for estado in range(utilidades.shape[0]):  # Iteración sobre todos los estados
        valores_estados[estado] = max([sum([probabilidades_transicion[estado, nuevo_estado] * (utilidades[estado, accion] + factor_descuento * valores_previos[nuevo_estado])
                                    for nuevo_estado in range(utilidades.shape[0])])
                               for accion in range(utilidades.shape[1])])

# Iteración de valores hasta convergencia
iteracion = 0  # Inicialización del contador de iteración
epsilon = 1e-6  # Criterio de convergencia
max_iteraciones = 1000  # Número máximo de iteraciones permitidas
while True:  # Bucle infinito
    iteracion_valores()  # Llamada a la función de iteración de valores
    iteracion += 1  # Incremento del contador de iteración
    if np.max(np.abs(valores_estados - np.zeros(utilidades.shape[0]))) < epsilon or iteracion >= max_iteraciones:  # Verificación de convergencia o máximo de iteraciones alcanzado
        break  # Salir del bucle

# Impresión de los valores óptimos de los estados
print("Valores óptimos de los estados:")
for i, valor in enumerate(valores_estados):  # Iteración sobre los valores óptimos de los estados
    print(f"Estado {i+1}: {valor}")  # Impresión de cada valor óptimo

# Determinación de las acciones óptimas en cada estado
acciones_optimas = np.argmax([[sum([probabilidades_transicion[estado, nuevo_estado] * (utilidades[estado, accion] + factor_descuento * valores_estados[nuevo_estado])
                                    for nuevo_estado in range(utilidades.shape[0])])
                               for accion in range(utilidades.shape[1])]
                             for estado in range(utilidades.shape[0])], axis=1)

# Impresión de las acciones óptimas en cada estado
print("\nAcciones óptimas en cada estado:")
for i, accion in enumerate(acciones_optimas):  # Iteración sobre las acciones óptimas
    print(f"Estado {i+1}: Acción {accion+1}")  # Impresión de cada acción óptima
