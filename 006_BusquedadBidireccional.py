# -*- coding: utf-8 -*-
"""
Created on 27 march 18:59:09 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código implementa un algoritmo de búsqueda bidireccional para encontrar un 
nodo de intersección entre dos puntos en un grafo. Utiliza dos conjuntos de nodos 
visitados y dos colas de nodos frontera, una para la búsqueda desde el inicio y 
otra desde el objetivo. El algoritmo expande los nodos de manera alternativa 
desde el inicio y el objetivo hasta que encuentra una intersección o no hay 
más nodos por explorar.
'''
def bidirectional_search(graph, start, goal):
    visited_start = set()  # Conjunto de nodos visitados desde el inicio
    visited_goal = set()   # Conjunto de nodos visitados desde el objetivo
    
    frontier_start = [start]  # Cola para nodos frontera desde el inicio
    frontier_goal = [goal]    # Cola para nodos frontera desde el objetivo
    
    while frontier_start and frontier_goal:  # Bucle para búsqueda bidireccional
        current_start = frontier_start.pop(0)  # Expansión desde el inicio
        visited_start.add(current_start)
        
        if current_start in visited_goal:  # Comprobar si el nodo actual está en el conjunto de nodos visitados desde el objetivo
            return current_start  # Si se encuentra, se ha encontrado una intersección, devolver el nodo
        
        current_goal = frontier_goal.pop(0)  # Expansión desde el objetivo
        visited_goal.add(current_goal)
        
        if current_goal in visited_start:  # Comprobar si el nodo actual está en el conjunto de nodos visitados desde el inicio
            return current_goal  # Si se encuentra, se ha encontrado una intersección, devolver el nodo
        
        for neighbor in graph[current_start]:  # Expandir sucesores del nodo actual desde el inicio
            if neighbor not in visited_start and neighbor not in frontier_start:
                frontier_start.append(neighbor)
        
        for neighbor in graph[current_goal]:  # Expandir sucesores del nodo actual desde el objetivo
            if neighbor not in visited_goal and neighbor not in frontier_goal:
                frontier_goal.append(neighbor)
    
    return None  # Si no se encuentra una intersección, devolver None

# Creación del grafo
graph = {
    'A': ['B', 'C'],  # Nodo A tiene vecinos B y C
    'B': ['A', 'D', 'E'],  # Nodo B tiene vecinos A, D y E
    'C': ['A', 'F'],  # Nodo C tiene vecinos A y F
    'D': ['B'],  # Nodo D tiene vecino B
    'E': ['B', 'F'],  # Nodo E tiene vecinos B y F
    'F': ['C', 'E']  # Nodo F tiene vecinos C y E
}

start_node = 'A'  # Nodo de inicio
goal_node = 'F'    # Nodo objetivo

print("Intersection Node:", bidirectional_search(graph, start_node, goal_node))  # Realizar búsqueda bidireccional e imprimir el nodo de intersección
