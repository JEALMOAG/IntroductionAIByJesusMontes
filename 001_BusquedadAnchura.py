# -*- coding: utf-8 -*-
"""
Created on 25 march 13:44:30 2024
@author: Jesus Alejandro Mntes Aguila
"""


# Este código define una clase para representar un grafo y proporciona métodos para agregar vértices,
# agregar aristas entre vértices y realizar un recorrido en amplitud (BFS) para encontrar
# un camino entre dos vértices.

from collections import deque  # Importa la clase deque de la biblioteca collections

class Grafo:  # Definición de la clase Grafo
    def __init__(self):  # Constructor de la clase Grafo
        self.vertices = {}  # Inicializa un diccionario para almacenar los vértices y sus aristas
    
    def agregar_vertice(self, vertice):  # Método para agregar un vértice al grafo
        # Método para agregar un vértice al grafo
        if vertice not in self.vertices:  # Verifica si el vértice no está en el grafo
            self.vertices[vertice] = []  # Si no está, lo agrega al diccionario con una lista vacía de aristas
    
    def agregar_arista(self, vertice1, vertice2):  # Método para agregar una arista entre dos vértices
        # Método para agregar una arista entre dos vértices
        if vertice1 in self.vertices and vertice2 in self.vertices:  # Verifica si ambos vértices existen en el grafo
            self.vertices[vertice1].append(vertice2)  # Agrega el vértice2 a la lista de aristas del vértice1
            self.vertices[vertice2].append(vertice1)  # Agrega el vértice1 a la lista de aristas del vértice2
    
    def bfs(self, inicio, objetivo):  # Método de búsqueda en amplitud (BFS) en el grafo
        # Método de búsqueda en amplitud (BFS) en el grafo
        if inicio not in self.vertices or objetivo not in self.vertices:  # Verifica si los vértices dados existen en el grafo
            return None  # Si alguno de los vértices no existe, devuelve None
        
        visitados = set()  # Conjunto para almacenar los nodos visitados
        cola = deque()  # Crea una cola usando la clase deque
        cola.append((inicio, [inicio]))  # Agrega la tupla (inicio, [inicio]) a la cola
        
        while cola:  # Mientras la cola no esté vacía
            nodo_actual, camino = cola.popleft()  # Obtiene el nodo y el camino asociado de la cola
            visitados.add(nodo_actual)  # Marca el nodo como visitado
            if nodo_actual == objetivo:  # Si el nodo actual es el objetivo
                return camino  # Devuelve el camino hasta el objetivo
            
            for vecino in self.vertices[nodo_actual]:  # Para cada vecino del nodo actual
                if vecino not in visitados:  # Si el vecino no ha sido visitado
                    cola.append((vecino, camino + [vecino]))  # Agrega el vecino y su camino al final de la cola
                    visitados.add(vecino)  # Marca el vecino como visitado

# Example of usage
graph = Grafo()  # Crea una instancia de la clase Grafo
graph.agregar_vertice('A')  # Agrega vértices al grafo
graph.agregar_vertice('B')  # Agrega vértices al grafo
graph.agregar_vertice('C')  # Agrega vértices al grafo
graph.agregar_arista('A', 'B')  # Agrega aristas al grafo
graph.agregar_arista('B', 'C')  # Agrega aristas al grafo

start = 'A'  # Nodo inicial de la búsqueda
goal = 'C'  # Nodo objetivo de la búsqueda
path = graph.bfs(start, goal)  # Realiza una búsqueda en amplitud desde el nodo inicial al objetivo
if path:  # Si se encontró un camino
    print(f"Se encontró un camino de {start} a {goal}: {' -> '.join(path)}")  # Imprime el camino encontrado
else:  # Si no se encontró un camino
    print(f"No se encontró un camino de {start} a {goal}.")  # Imprime un mensaje de que no se encontró camino

