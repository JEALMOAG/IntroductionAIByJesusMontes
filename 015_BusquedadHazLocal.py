"""
Created on 29 march 12:19:14 2024
@author: Jesus Alejandro Montes Aguila 
"""

'''

Este código implementa el algoritmo de Búsqueda de Haz Local (Hill Climbing)
 para encontrar la solución óptima de una función objetivo dada. La función
 objetivo se define como 
𝑓(𝑥)=𝑥4−3𝑥3+2𝑥2+𝑥 
El algoritmo comienza desde un punto inicial y busca iterativamente un mejor 
vecino dentro de un rango determinado alrededor del punto actual. Si el valor
 de la función en el vecino es menor que el valor actual, el algoritmo se mueve 
 hacia ese vecino. El proceso se repite durante un número máximo de iteraciones.
 Finalmente, se devuelve la mejor solución encontrada junto con el valor de la 
 función en esa solución.
'''
import numpy as np
# Definición de la función objetivo (puede ser cualquier función)
def objective_function(x):
    return x**4 - 3 * x**3 + 2 * x**2 + x

# Algoritmo de Búsqueda de Haz Local (Hill Climbing)
def hill_climbing(func_obj, initial_x, step_size, max_iterations):
    current_x = initial_x
    
    # Iterar sobre el número máximo de iteraciones
    for _ in range(max_iterations):
        current_value = func_obj(current_x)
        
        # Generar un vecino
        neighbor = current_x + np.random.uniform(-step_size, step_size)
        
        # Evaluar el vecino
        neighbor_value = func_obj(neighbor)
        
        # Actualizar la solución si el vecino es mejor
        if neighbor_value < current_value:
            current_x = neighbor
    
    return current_x, func_obj(current_x)

# Parámetros
initial_x = 2  # Punto inicial
step_size = 0.1  # Tamaño del paso
max_iterations = 1000  # Número máximo de iteraciones

# Ejecución del algoritmo
best_solution, best_value = hill_climbing(objective_function, initial_x, step_size, max_iterations)

# Imprimir la mejor solución y su valor
print("Best solution found:", best_solution)
print("Best solution value found:", best_value)

