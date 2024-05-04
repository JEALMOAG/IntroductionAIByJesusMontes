# -*- coding: utf-8 -*-
"""
Created on 25 march 23:48:14 2024
@author: Jesus Alejandro Mntes Aguila
"""
'''
El código implementa una búsqueda en profundidad iterativa para encontrar un 
camino desde un nodo de inicio hasta un nodo objetivo en un grafo dado.
Se establece una profundidad máxima para la búsqueda y se realiza la búsqueda 
iterativa con límites de profundidad crecientes hasta que se encuentra un camino
 o se alcanza la profundidad máxima permitida. Si se encuentra un camino, se 
 imprime; de lo contrario, se muestra un mensaje indicando que no se encontró
 ningún camino dentro del límite de profundidad especificado.
 
 
El objetivo del código es realizar una búsqueda en profundidad iterativa para
 encontrar un camino desde un nodo de inicio hasta un nodo objetivo en un grafo
 dado, utilizando límites de profundidad crecientes hasta alcanzar un máximo predefinido.
'''
def dfs_iterative(graph, inicio, objetivo, max_profundidad):
    for limite_profundidad in range(1, max_profundidad + 1):
        resultado = dfs_limit(graph, inicio, objetivo, limite_profundidad)
        if resultado is not None:
            return resultado
    return "No se encontró un camino dentro de la profundidad máxima."

def dfs_limit(graph, inicio, objetivo, max_profundidad):
    visitados = set()
    pila = [(inicio, [inicio], 0)]
    while pila:
        nodo, camino, profundidad = pila.pop()
        if nodo not in visitados:
            if nodo == objetivo:
                return camino
            if profundidad < max_profundidad:
                visitados.add(nodo)
                for vecino in graph[nodo]:
                    pila.append((vecino, camino + [vecino], profundidad + 1))
    return None

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
    'G': ['C', 'F', 'I'],
    'H': ['D'],
    'I': ['G', 'J'],
    'J': ['I']
}

nodo_inicio = 'A'
nodo_objetivo = 'I'
max_profundidad = 4

resultado = dfs_iterative(grafo, nodo_inicio, nodo_objetivo, max_profundidad)
if resultado:
    print("Camino encontrado:", resultado)
else:
    print("No se encontró un camino desde", nodo_inicio, "hasta", nodo_objetivo)
