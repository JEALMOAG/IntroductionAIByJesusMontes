# -*- coding: utf-8 -*-
"""
Created on 25 march 20:04:37 2024
@author: Jesus Alejandro Mntes Aguila
"""
'''

Este código implementa una función de búsqueda en profundidad limitada (DFS) en un grafo.
 El objetivo de la búsqueda es encontrar un camino desde un nodo de inicio hasta un nodo objetivo, 
 respetando un límite máximo de profundidad. El grafo se representa como un diccionario donde las 
 claves son los nodos y los valores son listas de nodos vecinos. La función DFS recorre el grafo en 
 profundidad, manteniendo un registro de nodos visitados y utilizando una pila para explorar los nodos
 vecinos. Si encuentra el nodo objetivo dentro del límite de profundidad, devuelve el camino encontrado.
 Si no encuentra un camino dentro del límite de profundidad, devuelve un mensaje indicando que no se encontró 
 un camino.
'''

def dfs_limit(graph, start, goal, max_depth):  # Define una función de búsqueda en profundidad limitada.
    visited_nodes = set()  # Conjunto para mantener un registro de nodos visitados.
    stack = [(start, [start], 0)]  # Pila para realizar la búsqueda en profundidad con el nivel de profundidad.
    while stack:  # Mientras haya nodos en la pila.
        node, path, depth = stack.pop()  # Sacar el nodo, el camino asociado y el nivel de profundidad de la pila.
        if node not in visited_nodes:  # Si el nodo no ha sido visitado.
            if node == goal:  # Si se encuentra el nodo objetivo.
                return path  # Devolver el camino.
            if depth < max_depth:  # Verificar el límite de profundidad.
                visited_nodes.add(node)  # Marcar el nodo como visitado.
                for neighbor in graph[node]:  # Iterar sobre los vecinos del nodo.
                    stack.append((neighbor, path + [neighbor], depth + 1))  # Agregar vecinos a la pila con el nivel de profundidad actualizado.
    return "No se encontró un camino dentro del límite de profundidad."  # Si no se encuentra un camino al objetivo dentro del límite de profundidad, devuelve un mensaje de error.

# Ejemplo de grafo
graph = {
    'A': ['B', 'C'],  # Nodo A tiene vecinos B y C.
    'B': ['A', 'D', 'E'],  # Nodo B tiene vecinos A, D y E.
    'C': ['A', 'F'],  # Nodo C tiene vecinos A y F.
    'D': ['B'],  # Nodo D tiene vecino B.
    'E': ['B', 'F'],  # Nodo E tiene vecinos B y F.
    'F': ['C', 'E']  # Nodo F tiene vecinos C y E.
}

start_node = 'A'  # Nodo de inicio.
goal_node = 'F'   # Nodo objetivo.
max_depth = 2  # Profundidad máxima permitida.
print("Resultado de la búsqueda:", dfs_limit(graph, start_node, goal_node, max_depth))  # Imprime el resultado de la búsqueda en profundidad limitada.