"""
Created on 28 march 11:23:44 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este código implementa el algoritmo de búsqueda A* para encontrar el camino 
más corto en un grafo ponderado. Utiliza una heurística basada en la distancia 
euclidiana para estimar el costo desde cada nodo hasta el nodo objetivo. 
El algoritmo comienza desde el nodo inicial y explora los nodos vecinos,
 moviéndose hacia el nodo con el costo más bajo más la estimación heurística.
 Si encuentra el nodo objetivo, devuelve el camino óptimo; de lo contrario, 
 informa que no se encontró un camino.
'''
import heapq  # Importing the heapq module for priority queue implementation

# Definición de la estructura del grafo
graph = {
    'A': {'B': 5, 'C': 10},  # Nodo A con conexiones a B y C, con costos respectivos
    'B': {'D': 15, 'E': 20},  # Nodo B con conexiones a D y E, con costos respectivos
    'C': {'F': 25},           # Nodo C con conexión a F, con costo
    'D': {},                  # Nodo D sin conexiones salientes
    'E': {'F': 30},           # Nodo E con conexión a F, con costo
    'F': {}                   # Nodo F sin conexiones salientes
}

# Función de búsqueda A*
def a_star_search(graph, start, goal):
    frontier = []  # Lista de prioridad para nodos frontera
    heapq.heappush(frontier, (0, start, [start]))  # Inicialización con el nodo inicial y su costo 0
    visited = set()  # Conjunto para mantener los nodos ya visitados

    while frontier:
        current_cost, current_node, current_path = heapq.heappop(frontier)  # Se extrae el nodo con menor costo de la frontera

        if current_node == goal:
            return current_path  # Se encontró el objetivo, se devuelve el camino

        visited.add(current_node)  # Se marca el nodo actual como visitado

        for neighbor, cost in graph[current_node].items():  # Se recorren los vecinos del nodo actual
            if neighbor not in visited:  # Si el vecino no ha sido visitado
                new_path = list(current_path)  # Se crea un nuevo camino basado en el camino actual
                new_path.append(neighbor)         # Se añade el vecino al nuevo camino
                total_cost = current_cost + cost + heuristic(neighbor, goal)  # Se calcula el costo total hasta el vecino
                heapq.heappush(frontier, (total_cost, neighbor, new_path))      # Se añade el vecino a la frontera con su costo total

    return None  # No se encontró el objetivo

# Función de heurística (distancia euclidiana)
def heuristic(current_node, goal_node):
    coordenadas = {  # Coordenadas de los nodos en un sistema de coordenadas ficticio
        'A': (0, 0),
        'B': (1, 0),
        'C': (0, 1),
        'D': (2, 0),
        'E': (1, 1),
        'F': (2, 1)
    }
    x1, y1 = coordenadas[current_node]    # Coordenadas del nodo actual
    x2, y2 = coordenadas[goal_node]  # Coordenadas del nodo objetivo
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # Distancia euclidiana entre los nodos

# Ejemplo de uso
start = 'A'       # Nodo inicial
goal = 'F'     # Nodo objetivo

path = a_star_search(graph, start, goal)  # Se realiza la búsqueda de A* para encontrar el camino
if path:
    print("I've found the objective way:", path)  # Se imprime el camino si se encuentra
else:
    print("I've found the objective way.")       # Se informa si no se encuentra un camino
