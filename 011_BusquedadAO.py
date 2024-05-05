"""
Created on 28 march 14:27:41 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este código implementa el algoritmo de búsqueda AO* (Adaptative A*) para
 encontrar el camino óptimo en un grafo ponderado. Utiliza una heurística
 para guiar la búsqueda hacia el objetivo de manera eficiente. El grafo y
 los nodos de inicio y objetivo están definidos en el código. El algoritmo
 busca el camino óptimo teniendo en cuenta los costos y la heurística definida.
 Si encuentra un camino al objetivo, lo imprime; de lo contrario,
 informa que no se encontró ningún camino.
'''
# Importación del módulo heapq para usar colas de prioridad
import heapq  

# Definición de la estructura del grafo
graph = {
    'A': {'B': 5, 'C': 10},  # Nodo A con conexiones a B y C, con costos respectivos
    'B': {'D': 15, 'E': 20},  # Nodo B con conexiones a D y E, con costos respectivos
    'C': {'F': 25},           # Nodo C con conexión a F, con costo
    'D': {},                  # Nodo D sin conexiones salientes
    'E': {'F': 30},           # Nodo E con conexión a F, con costo
    'F': {}                   # Nodo F sin conexiones salientes
}

# Función de búsqueda AO*
def ao_star_search(graph, start, goal, alpha):
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
                total_cost = current_cost + cost + alpha * heuristic(neighbor, goal)  # Se calcula el costo total hasta el vecino
                heapq.heappush(frontier, (total_cost, neighbor, new_path))      # Se añade el vecino a la frontera con su costo total

    return None  # No se encontró el objetivo

# Función de heurística (distancia euclidiana)
def heuristic(current_node, goal_node):
    coordinates = {  # Coordenadas de los nodos en un sistema de coordenadas ficticio
        'A': (0, 0),
        'B': (1, 0),
        'C': (0, 1),
        'D': (2, 0),
        'E': (1, 1),
        'F': (2, 1)
    }
    x1, y1 = coordinates[current_node]    # Coordenadas del nodo actual
    x2, y2 = coordinates[goal_node]  # Coordenadas del nodo objetivo
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # Distancia euclidiana entre los nodos

# Ejemplo de uso
start = 'A'       # Nodo inicial
goal = 'F'     # Nodo objetivo
alpha = 0.5        # Factor de adaptación heurística

path = ao_star_search(graph, start, goal, alpha)  # Se realiza la búsqueda de AO* para encontrar el camino
if path:
    print("Se encontró un camino al objetivo:", path)  # Se imprime el camino si se encuentra
else:
    print("No se encontró un camino al objetivo.")       # Se informa si no se encuentra un camino
