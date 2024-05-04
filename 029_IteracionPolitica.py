"""
created on 2 april 17:15:26 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
Este código implementa el algoritmo de evaluación de política iterativa
para encontrar los valores óptimos de los estados en un entorno de toma
de decisiones. Utiliza matrices para representar las recompensas y las
probabilidades de transición entre estados dado un conjunto de acciones.
La función evaluacion_politica itera sobre los estados, actualizando
iterativamente los valores basados en la política dada y las recompensas
esperadas, hasta que los valores convergen o se alcanza el número máximo de
iteraciones. Finalmente, imprime los valores óptimos de los estados.
"""
import numpy as np
# Definición del entorno
# Las filas representan estados y las columnas representan acciones
recompensas = np.array([
    [-1, -3],  # Estado 0: Acción 0 -> Recompensa -1, Acción 1 -> Recompensa -3
    [-2, 10],  # Estado 1: Acción 0 -> Recompensa -2, Acción 1 -> Recompensa 10
])

# Matriz de transiciones de estado
# T[s, a, s'] representa la probabilidad de pasar al estado 's'' al tomar la acción 'a' desde el estado 's'
transiciones = np.array([
    [[1, 0], [0, 1]],  # Desde el estado 0, Acción 0: 100% de probabilidad de permanecer en el estado 0
                       # Desde el estado 0, Acción 1: 100% de probabilidad de pasar al estado 1
    [[1, 0], [0, 1]]   # Desde el estado 1, Acción 0: 100% de probabilidad de permanecer en el estado 1
                       # Desde el estado 1, Acción 1: 100% de probabilidad de permanecer en el estado 1
])

# Definición de la política inicial
politica = np.ones((2, 2)) / 2  # 2 estados, 2 acciones

# Algoritmo de evaluación de política iterativa
def evaluacion_politica(politica, recompensas, transiciones, gamma=0.9, theta=0.0001):
    valores = np.zeros(len(recompensas))  # Inicializamos los valores de los estados a 0
    while True:  # Inicia un bucle que se ejecutará hasta que se cumpla una condición de convergencia
        cambio_maximo = 0  # Inicializa el valor de cambio máximo entre las iteraciones
        for s in range(len(recompensas)):  # Itera sobre cada estado en el problema
            v = valores[s]  # Almacena el valor actual del estado
            # Calcula el nuevo valor del estado utilizando la política y las recompensas
            valores[s] = sum(politica[s, a] * sum(transiciones[s, a, s1] * (recompensas[s, a] + gamma * valores[s1]) for s1 in range(len(recompensas))) for a in range(len(politica[s])))
            # Actualiza el valor de cambio máximo
            cambio_maximo = max(cambio_maximo, abs(v - valores[s]))
        if cambio_maximo < theta:  # Comprueba si se ha alcanzado la convergencia
            break  # Si el cambio es lo suficientemente pequeño, se detiene la iteración
    return valores  # Devuelve los valores de los estados calculados

# Ejecutar el algoritmo de evaluación de política
valores_estados = evaluacion_politica(politica, recompensas, transiciones)

print("Valores de los estados:")
print(valores_estados)
