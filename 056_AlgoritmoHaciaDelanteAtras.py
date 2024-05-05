"""
created on 7 Abril 15:27:45 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa una red bayesiana y un algoritmo para realizar inferencias probabilísticas utilizando el algoritmo de propagación hacia adelante y hacia atrás.

La clase Nodo representa un nodo en la red bayesiana, con métodos para agregar padres e hijos.
La clase RedBayesiana representa la red bayesiana en sí, con métodos para agregar nodos y arcos, y para realizar la propagación hacia adelante y hacia atrás.
La propagación hacia adelante inicializa las probabilidades de los nodos basándose en las probabilidades de los padres.
La propagación hacia atrás actualiza las probabilidades de los nodos basándose en la evidencia proporcionada y las probabilidades de los hijos.
El ejemplo final muestra cómo crear una red bayesiana y realizar inferencias sobre ella.
"""
class Nodo:  # Define una clase llamada Nodo para representar un nodo en la red bayesiana

    def __init__(self, nombre):  # Define el constructor de la clase Nodo que se ejecuta al crear un nuevo objeto Nodo
        self.nombre = nombre  # Asigna el nombre del nodo
        self.padres = []  # Inicializa una lista vacía para almacenar los nodos padres
        self.hijos = []  # Inicializa una lista vacía para almacenar los nodos hijos
        self.probabilidad = None  # Inicializa la probabilidad del nodo como None

    def agregar_padre(self, padre):  # Define un método para agregar un nodo padre al nodo actual
        self.padres.append(padre)  # Agrega el nodo padre a la lista de padres del nodo actual

    def agregar_hijo(self, hijo):  # Define un método para agregar un nodo hijo al nodo actual
        self.hijos.append(hijo)  # Agrega el nodo hijo a la lista de hijos del nodo actual


class RedBayesiana:  # Define una clase llamada RedBayesiana para representar una red bayesiana

    def __init__(self):  # Define el constructor de la clase RedBayesiana que se ejecuta al crear un nuevo objeto RedBayesiana
        self.nodos = {}  # Inicializa un diccionario vacío para almacenar los nodos de la red bayesiana

    def agregar_nodo(self, nombre):  # Define un método para agregar un nuevo nodo a la red bayesiana
        self.nodos[nombre] = Nodo(nombre)  # Crea un nuevo objeto Nodo con el nombre dado y lo agrega al diccionario de nodos

    def agregar_arco(self, padre, hijo):  # Define un método para agregar un arco dirigido entre dos nodos en la red bayesiana
        self.nodos[padre].agregar_hijo(self.nodos[hijo])  # Agrega el nodo hijo a la lista de hijos del nodo padre
        self.nodos[hijo].agregar_padre(self.nodos[padre])  # Agrega el nodo padre a la lista de padres del nodo hijo

    def hacia_adelante(self):  # Define un método para realizar la propagación hacia adelante en la red bayesiana
        for nombre_nodo in self.nodos:  # Itera sobre todos los nodos en la red bayesiana
            nodo = self.nodos[nombre_nodo]  # Obtiene el nodo actual
            if not nodo.padres:  # Si el nodo no tiene padres
                nodo.probabilidad = 0.5  # Establece la probabilidad del nodo en 0.5 (arbitrariamente)
            else:  # Si el nodo tiene padres
                nodo.probabilidad = 1.0  # Inicializa la probabilidad del nodo en 1.0
                for padre in nodo.padres:  # Itera sobre todos los padres del nodo
                    nodo.probabilidad *= padre.probabilidad  # Actualiza la probabilidad del nodo multiplicando las probabilidades de los padres

    def hacia_atras(self, consulta, evidencia):  # Define un método para realizar la propagación hacia atrás en la red bayesiana
        for nombre_nodo in self.nodos:  # Itera sobre todos los nodos en la red bayesiana
            nodo = self.nodos[nombre_nodo]  # Obtiene el nodo actual
            if nombre_nodo in evidencia:  # Si el nodo está presente en la evidencia
                nodo.probabilidad = evidencia[nombre_nodo]  # Actualiza la probabilidad del nodo con el valor de la evidencia

        for nombre_nodo in reversed(list(self.nodos.keys())):  # Itera sobre todos los nodos en orden inverso
            nodo = self.nodos[nombre_nodo]  # Obtiene el nodo actual
            if nombre_nodo != consulta:  # Si el nodo no es el nodo de consulta
                suma = 0.0  # Inicializa la suma de las probabilidades de los hijos
                for hijo in nodo.hijos:  # Itera sobre todos los hijos del nodo
                    suma += hijo.probabilidad  # Agrega la probabilidad del hijo a la suma
                nodo.probabilidad *= suma  # Actualiza la probabilidad del nodo multiplicándola por la suma de las probabilidades de los hijos

# Ejemplo de uso
red_bayesiana = RedBayesiana()  # Crea un nuevo objeto RedBayesiana
red_bayesiana.agregar_nodo("A")  # Agrega un nodo "A" a la red bayesiana
red_bayesiana.agregar_nodo("B")  #
