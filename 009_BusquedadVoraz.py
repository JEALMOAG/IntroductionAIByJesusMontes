"""
Created on 28 march 00:29:44 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código implementa un algoritmo de búsqueda voraz (greedy search) en un grafo
 dado, utilizando una heurística de distancia euclidiana para dirigir la búsqueda 
 hacia el objetivo. El algoritmo busca un camino desde un nodo de inicio hasta 
 un nodo objetivo, expandiendo los nodos vecinos en función de la heurística y
 priorizando los caminos más prometedores. Si encuentra un camino al objetivo,
 lo devuelve; de lo contrario, indica que no se encontró un camino.
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

# Función de búsqueda voraz
def greedy_search(graph, start, goal):
    frontier = []  # Creamos una cola de prioridad vacía para almacenar los nodos a expandir
    heapq.heappush(frontier, (0, [start]))  # Insertamos el nodo inicial en la cola de prioridad con una heurística inicial de 0 y un camino que solo contiene el nodo inicial
    visited = set()  # Creamos un conjunto para almacenar los nodos visitados

    while frontier:  # Mientras haya nodos en la frontera para explorar
        _, current_path = heapq.heappop(frontier)  # Extraemos el nodo con menor heurística de la frontera
        current_node = current_path[-1]  # Obtenemos el nodo actual del camino

        if current_node == goal:  # Si hemos llegado al nodo objetivo
            return current_path  # Devolvemos el camino hasta el objetivo

        visited.add(current_node)  # Marcamos el nodo actual como visitado

        for neighbor, _ in graph[current_node].items():  # Iteramos sobre los vecinos del nodo actual
            if neighbor not in visited:  # Si el vecino no ha sido visitado
                new_path = list(current_path)  # Creamos un nuevo camino que es una copia del camino actual
                new_path.append(neighbor)  # Agregamos el vecino al nuevo camino
                heuristic_value = euclidean_distance(neighbor, goal)  # Calculamos la heurística para el vecino
                heapq.heappush(frontier, (heuristic_value, new_path))  # Insertamos el nuevo camino en la frontera con su heurística correspondiente

    return None  # Si no se encuentra un camino al objetivo, devolvemos None

# Función para calcular la distancia euclidiana entre dos puntos en el grafo
def euclidean_distance(current_node, goal_node):
    # Se asume que los nodos son coordenadas en un plano
    coordinates = {
        'A': (0, 0),
        'B': (1, 0),
        'C': (0, 1),
        'D': (2, 0),
        'E': (1, 1),
        'F': (2, 1)
    }
    x1, y1 = coordinates[current_node]  # Obtenemos las coordenadas del nodo actual
    x2, y2 = coordinates[goal_node]  # Obtenemos las coordenadas del nodo objetivo
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # Calculamos y devolvemos la distancia euclidiana entre los dos nodos

# Ejemplo de uso
start = 'A'  # Nodo inicial
goal = 'F'  # Nodo objetivo

path = greedy_search(graph, start, goal)  # Realizamos la búsqueda del camino
if path:
    print("I've found the objective way:", path)  # Si se encuentra un camino, imprimimos el camino encontrado
else:
    print("I've not found the objective way.")  # Si no se encuentra un camino, mostramos un mensaje indicando que no se encontró
