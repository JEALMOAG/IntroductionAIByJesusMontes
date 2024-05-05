"""
Created on 28 march 20:17:05 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este código implementa el algoritmo de búsqueda tabú para encontrar 
la solución óptima de una función objetivo dada. Utiliza una estrategia de
 exploración local iterativa, evitando ciclos mediante una lista tabú. 
 La solución encontrada y su valor se imprimen al final de la ejecución.
 Los parámetros de entrada pueden ajustarse según las necesidades del problema.
'''
def objective_function(x):  # Función objetivo (puede ser cualquier función)
    return (x - 2) ** 2 + 5

def generate_neighbor(x, delta):  # Función para generar vecinos
    return x + delta

def tabu_search(obj_func, initial_x, max_iter, delta, tabu_tenure):  # Implementación del algoritmo de búsqueda tabú
    best_solution = initial_x  # Almacena la mejor solución encontrada
    best_value = obj_func(initial_x)  # Almacena el valor de la función en la mejor solución
    current_solution = initial_x  # Almacena la solución actual
    current_value = best_value  # Almacena el valor actual de la función
    tabu_list = []  # Lista de soluciones prohibidas (tabú)

    for _ in range(max_iter):  # Realiza un número máximo de iteraciones
        neighbors = [generate_neighbor(current_solution, delta), generate_neighbor(current_solution, -delta)]  # Genera dos vecinos: uno con un incremento y otro con un decremento
        neighbors = [(neighbor, obj_func(neighbor)) for neighbor in neighbors if neighbor not in tabu_list]  # Evalúa los vecinos y filtra aquellos que están en la lista tabú
        if not neighbors:  # Si no hay vecinos disponibles, termina el algoritmo
            break
        neighbors.sort(key=lambda x: x[1])  # Ordena los vecinos según el valor de la función objetivo
        best_neighbor, best_neighbor_value = neighbors[0]  # Obtiene el mejor vecino y su valor
        
        # Si el valor del mejor vecino es mejor que el mejor valor actual, actualiza la mejor solución
        if best_neighbor_value < best_value:
            best_solution = best_neighbor
            best_value = best_neighbor_value
        
        current_solution = best_neighbor  # Actualiza la solución actual
        current_value = best_neighbor_value  # Actualiza el valor actual
        tabu_list.append(current_solution)  # Agrega la solución actual a la lista tabú
        
        # Si la lista tabú excede la longitud especificada, elimina el elemento más antiguo
        if len(tabu_list) > tabu_tenure:
            tabu_list.pop(0)

    return best_solution, best_value

initial_x = 0  # Punto inicial de la búsqueda
max_iter = 100  # Número máximo de iteraciones
delta = 0.1  # Tamaño del paso para generar vecinos
tabu_tenure = 5  # Duración máxima de prohibición de soluciones (lista tabú)

# Ejecución del algoritmo
best_solution, best_value = tabu_search(objective_function, initial_x, max_iter, delta, tabu_tenure)

print("Best solution found:", best_solution)  # Imprime la mejor solución
print("Best solution foud Value :", best_value)  # Imprime el valor
