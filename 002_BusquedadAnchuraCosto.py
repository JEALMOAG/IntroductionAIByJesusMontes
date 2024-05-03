"""
Created on 25 march 15:44:30 2024
@author: Jesus Alejandro Mntes Aguila
"""

import heapq  # Importa la clase heapq para usar colas de prioridad
import random  # Importa la clase random para generar números aleatorios

class Grafo:  # Definición de la clase Grafo
    def __init__(self):  # Constructor de la clase Grafo
        self.vertices = {}  # Inicializa un diccionario para almacenar los vértices y sus aristas

    def agregar_vertice(self, vertice):  # Método para agregar un vértice al grafo
        if vertice not in self.vertices:  # Verifica si el vértice no está en el grafo
            self.vertices[vertice] = {}  # Si no está, agrega el vértice al diccionario con un diccionario vacío para las aristas

    def agregar_arista(self, inicio, fin, costo):  # Método para agregar una arista entre dos vértices con un costo
        self.agregar_vertice(inicio)  # Agrega el vértice de inicio al grafo si no está presente
        self.agregar_vertice(fin)  # Agrega el vértice de fin al grafo si no está presente
        self.vertices[inicio][fin] = costo  # Agrega la arista desde el vértice de inicio al vértice de fin con el costo dado
        self.vertices[fin][inicio] = costo  # Agrega la arista desde el vértice de fin al vértice de inicio con el costo dado

    def costo_uniforme(self, inicio, destino):  # Método para encontrar el costo mínimo desde un vértice de inicio a un vértice de destino
        cola_prioridad = [(0, inicio)]  # Inicializa una cola de prioridad con una tupla que contiene el costo actual y el vértice de inicio
        visitados = set()  # Inicializa un conjunto para almacenar los nodos visitados

        while cola_prioridad:  # Mientras la cola de prioridad no esté vacía
            costo, nodo = heapq.heappop(cola_prioridad)  # Obtiene el nodo con el menor costo de la cola de prioridad
            if nodo not in visitados:  # Si el nodo no ha sido visitado
                visitados.add(nodo)  # Marca el nodo como visitado
                if nodo == destino:  # Si el nodo actual es el destino
                    return costo  # Devuelve el costo acumulado hasta el nodo de destino
                for vecino, costo_arista in self.vertices[nodo].items():  # Para cada vecino del nodo actual y su costo de arista
                    if vecino not in visitados:  # Si el vecino no ha sido visitado
                        nuevo_costo = costo + costo_arista  # Calcula el nuevo costo acumulado para llegar al vecino
                        heapq.heappush(cola_prioridad, (nuevo_costo, vecino))  # Agrega el vecino y su nuevo costo a la cola de prioridad

# Ejemplo de uso
mi_grafo = Grafo()  # Crea una instancia de la clase Grafo
mi_grafo.agregar_arista("A", "B", 5)  # Agrega una arista desde el vértice A al vértice B con un costo de 5
mi_grafo.agregar_arista("B", "C", 3)  # Agrega una arista desde el vértice B al vértice C con un costo de 3
mi_grafo.agregar_arista('A', 'B', 1)  # Agrega aristas al mi_grafo
mi_grafo.agregar_arista('A', 'C', 5)# Agrega aristas al mi_grafo
mi_grafo.agregar_arista('B', 'D', 3)# Agrega aristas al mi_grafo
mi_grafo.agregar_arista('C', 'D', 2)# Agrega aristas al mi_grafo
mi_grafo.agregar_arista('C', 'E', 6)# Agrega aristas al mi_grafo
mi_grafo.agregar_arista('D', 'E', 4)# Agrega aristas al mi_grafomi_grafo.agregar_arista('A', 'B', 1)  # Agrega aristas al mi_grafo
mi_grafo.agregar_arista('A', 'C', 5)# Agrega aristas al mi_grafo
mi_grafo.agregar_arista('B', 'D', 3)# Agrega aristas al mi_grafo
mi_grafo.agregar_arista('C', 'D', 2)# Agrega aristas al mi_grafo
mi_grafo.agregar_arista('C', 'E', 6)# Agrega aristas al mi_grafo
mi_grafo.agregar_arista('D', 'E', 4)# Agrega aristas al mi_grafo
# Agrega más aristas con costos aleatorios

resultado = mi_grafo.costo_uniforme("A", "C")  # Encuentra el costo mínimo desde el vértice A al vértice C
if resultado:  # Si se encuentra un camino
    print(f"El costo mínimo desde A hasta C es: {resultado}")  # Imprime el costo mínimo
else:  # Si no se encuentra un camino
    print("No se encontró un camino desde A hasta C.")  # Imprime un mensaje indicando que no se encontró un camino

