"""
Created on 27 march 20:59:09 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''

Este código implementa la búsqueda en amplitud (BFS) en un grafo utilizando 
una clase en Python. La clase Graph representa el grafo y proporciona métodos
para agregar aristas y realizar la búsqueda BFS desde un nodo inicial hasta un 
nodo objetivo. La búsqueda BFS se realiza utilizando una cola para explorar 
los nodos en orden de cercanía al nodo inicial. Una vez que se encuentra el 
nodo objetivo, se imprime un mensaje indicando que se ha encontrado.
'''
from collections import defaultdict, deque

# Clase que representa un grafo
class Graph:
    # Inicializador de la clase
    def __init__(self):
        # Diccionario para almacenar las listas de adyacencia de los nodos del grafo
        self.adjacency_lists = defaultdict(list)

    # Método para agregar una arista al grafo
    def add_edge(self, u, v):
        # Agrega el nodo 'v' a la lista de adyacencia del nodo 'u'
        self.adjacency_lists[u].append(v)

    # Método para realizar una búsqueda en amplitud (BFS)
    def bfs(self, start, goal):
        # Conjunto para almacenar los nodos visitados
        visited = set()
        # Cola para almacenar los nodos que se van a visitar
        queue = deque()

        # Agrega el nodo inicial a la cola y lo marca como visitado
        queue.append(start)
        visited.add(start)

        # Mientras haya nodos en la cola
        while queue:
            # Obtiene el primer nodo de la cola
            current_node = queue.popleft()
            # Imprime el nodo que se está visitando en ese momento
            print("Visiting node:", current_node)

            # Si el nodo actual es el objetivo, termina la búsqueda
            if current_node == goal:
                print("¡Objetivo encontrado!")
                return True

            # Explora los nodos vecinos del nodo actual
            for neighbor in self.adjacency_lists[current_node]:
                # Si el vecino no ha sido visitado, lo agrega a la cola y lo marca como visitado
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        # Si se llega aquí, no se encontró el objetivo
        print("No se encontró el objetivo.")
        return False

# Ejemplo de uso
# Crea un objeto de la clase Graph
graph = Graph()
# Agrega algunas aristas al grafo
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

# Define el nodo inicial y el nodo objetivo
start_node = 2
goal_node = 3

# Imprime un mensaje indicando que se realizará la búsqueda BFS
print("Search BFS:")
# Llama al método bfs para realizar la búsqueda en el grafo
graph.bfs(start_node, goal_node)
