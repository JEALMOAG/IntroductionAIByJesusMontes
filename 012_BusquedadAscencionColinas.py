"""
Created on 28 march 17:49:05 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este script implementa un algoritmo de ascenso de colinas (hill climbing) 
para encontrar la mejor posición en una lista de ciudades de México, utilizando
 una función objetivo predefinida. El algoritmo busca iterativamente en una 
 lista de ciudades, evaluando su valor objetivo y actualizando la mejor 
 posición encontrada. Finalmente, imprime la mejor posición encontrada 
 junto con su valor correspondiente.
'''
import random  # Importación del módulo random para generar números aleatorios

def objective_function(position):
    # Definición de la función objetivo que evalúa una posición en un diccionario predefinido
    evaluation = {
        'CDMX': 0.0, 'Guadalajara': 0.1, 'Monterrey': 0.2, 'Puebla': 0.3, 'Tijuana': 0.4,
        'CDMX': 0.1, 'Guadalajara': 0.2, 'Monterrey': 0.3, 'Puebla': 0.4, 'Tijuana': 0.5,
        'CDMX': 0.2, 'Guadalajara': 0.3, 'Monterrey': 0.4, 'Puebla': 0.5, 'Tijuana': 0.6,
        'CDMX': 0.3, 'Guadalajara': 0.4, 'Monterrey': 0.5, 'Puebla': 0.6, 'Tijuana': 0.7,
        'CDMX': 0.4, 'Guadalajara': 0.5, 'Monterrey': 0.6, 'Puebla': 0.7, 'Tijuana': 0.8,
    }
    return evaluation.get(position, 0.0)  # Devuelve la evaluación de la posición o 0.0 si la posición no existe

def hill_climbing_with_objective(max_iter, cities):
    best_position = None  # Almacenará la mejor posición encontrada
    best_value = float('-inf')  # Almacenará el mejor valor encontrado

    for _ in range(max_iter):  # Realiza un número máximo de iteraciones
        position = random.choice(cities)  # Selecciona una posición aleatoria de la lista de ciudades
        current_value = objective_function(position)  # Evalúa la función objetivo en la posición actual

        if current_value > best_value:  # Comprueba si el valor actual es mejor que el mejor valor encontrado hasta ahora
            best_value = current_value  # Actualiza el mejor valor
            best_position = position  # Actualiza la mejor posición

    return best_position, best_value  # Devuelve la mejor posición y su valor

if __name__ == "__main__":
    cities = ['CDMX', 'Guadalajara', 'Monterrey', 'Puebla', 'Tijuana']  # Lista de ciudades
    max_iter = 1000  # Número máximo de iteraciones

    # Ejecución del algoritmo de escalada de colinas con la función objetivo
    best_position, best_value = hill_climbing_with_objective(max_iter, cities)

    # Imprime el resultado
    print(f"The best position found is {best_position} with a value of {best_value}.")
