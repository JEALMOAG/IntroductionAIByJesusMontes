"""
Created on 27 march 22:14:09 2024
@author: Jesus Alejandro Montes Aguila 
"""

'''
El código implementa el algoritmo de búsqueda primero el mejor en un grafo ponderado.
 Utiliza una cola de prioridad para explorar los nodos de manera que siempre se expande 
 el nodo con la menor heurística. El objetivo es encontrar un camino desde un nodo inicial 
 hasta un nodo objetivo.
'''
import heapq  # Importamos el módulo heapq para usar colas de prioridad

# Definición de la estructura del grafo como un diccionario
graph = {
    'A': {'B': 5, 'C': 10},  # Desde el nodo 'A' se puede ir a 'B' con peso 5 y a 'C' con peso 10
    'B': {'D': 15, 'E': 20},  # Desde 'B' se puede ir a 'D' con peso 15 y a 'E' con peso 20
    'C': {'F': 25},  # Desde 'C' se puede ir a 'F' con peso 25
    'D': {},  # 'D' no tiene vecinos
    'E': {'F': 30},  # Desde 'E' se puede ir a 'F' con peso 30
    'F': {}  # 'F' no tiene vecinos
}

# Función de búsqueda primero el mejor
def best_first_search(graph, start, goal):
    frontier = []  # Creamos una cola de prioridad vacía para almacenar los nodos a expandir
    heapq.heappush(frontier, (0, [start]))  # Insertamos el nodo inicial en la cola de prioridad con una heurística inicial de 0 y un camino que solo contiene el nodo inicial
    visited = set()  # Creamos un conjunto para almacenar los nodos visitados

    while frontier:  # Mientras haya nodos en la frontera para explorar
        _, current_path = heapq.heappop(frontier)  # Extraemos el nodo con menor heurística de la frontera
        current_node = current_path[-1]  # Obtenemos el nodo actual del camino

        if current_node == goal:  # Si hemos llegado al nodo objetivo
            return current_path  # Devolvemos el camino hasta el objetivo

        visited.add(current_node)  # Marcamos el nodo actual como visitado

        for neighbor, weight in graph[current_node].items():  # Iteramos sobre los vecinos del nodo actual
            if neighbor not in visited:  # Si el vecino no ha sido visitado
                new_path = list(current_path)  # Creamos un nuevo camino que es una copia del camino actual
                new_path.append(neighbor)  # Agregamos el vecino al nuevo camino
                heuristic_value = weight  # La heurística en este caso es el peso del arco hasta el vecino
                heapq.heappush(frontier, (heuristic_value, new_path))  # Insertamos el nuevo camino en la frontera con su heurística correspondiente

    return None  # Si no se encuentra un camino al objetivo, devolvemos None

# Ejemplo de uso
start = 'A'  # Nodo inicial
goal = 'F'  # Nodo objetivo

path = best_first_search(graph, start, goal)  # Realizamos la búsqueda del camino
if path:
    print("I've found the objective way':", path)  # Si se encuentra un camino, lo imprimimos
else:
    print("I've not found the objective way")  # Si no se encuentra un camino, mostramos un mensaje indicando que no se encontró
