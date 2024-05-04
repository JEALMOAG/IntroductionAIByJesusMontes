"""
Created on 25 march 17:58:30 2024
@author: Jesus Alejandro Mntes Aguila
"""
'''

Este código implementa un algoritmo de búsqueda en profundidad (DFS) para encontrar un camino entre un nodo 
de inicio y un nodo objetivo en un grafo dado. Utiliza una pila para explorar los nodos de manera recursiva, 
manteniendo un registro de los nodos visitados. El objetivo es encontrar un camino desde el nodo de inicio hasta 
el nodo objetivo en el grafo proporcionado.
El objetivo del código es implementar un algoritmo de búsqueda en profundidad (DFS) para encontrar un camino
entre un nodo de inicio y un nodo objetivo en un grafo dado.
'''
import heapq

def dfs(grafo, inicio, objetivo): # Definimos una función de búsqueda en profundidad (DFS) que toma un grafo, un nodo de inicio y un nodo objetivo como entrada.
    nodos_visitados = set() # Conjunto para mantener un registro de los nodos visitados.
    pila_nodos = [(inicio, [inicio])] # Pila para realizar la búsqueda en profundidad, iniciada con el nodo de inicio.
    while pila_nodos: # Mientras haya nodos en la pila.
        (nodo, camino) = pila_nodos.pop() # Sacar el nodo y su camino asociado de la pila.
        if nodo not in nodos_visitados: # Si el nodo no ha sido visitado.
            if nodo == objetivo: # Si el nodo es el objetivo, devolver el camino.
                return camino
            nodos_visitados.add(nodo) # Marcar el nodo como visitado.
            for vecino in grafo[nodo]: # Agregar los vecinos del nodo a la pila con el camino actualizado.
                pila_nodos.append((vecino, camino + [vecino]))
    return None # Si no se encuentra un camino al objetivo, devolver None.

grafo = { # Definimos el grafo como un diccionario de listas de adyacencia.
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

nodo_inicio = 'A' # Nodo de inicio para la búsqueda.
nodo_objetivo = 'F' # Nodo objetivo para la búsqueda.

# Imprimir el camino encontrado por la búsqueda en profundidad.
print("Camino encontrado:", dfs(grafo, nodo_inicio, nodo_objetivo)) # Llamada a la función dfs y muestra el resultado.
