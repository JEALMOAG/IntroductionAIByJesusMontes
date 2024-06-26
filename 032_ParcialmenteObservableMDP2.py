"""
created on 3 april 14:06:05 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa una Red Bayesiana Dinámica (RBD)
y un algoritmo para calcular la utilidad esperada en función de
decisiones y evidencia. La clase NodoRB define un nodo en la RBD
con sus características, mientras que la clase RedBayesianaDinamica
representa la red completa y calcula la utilidad esperada.
El ejemplo muestra cómo usar estas clases para modelar un problema de
toma de decisiones y calcular la utilidad esperada.

"""
class NodoRB():
    def __init__(self, nombre, valores_posibles, padres=[], probabilidad={}, utilidad={}):
        self.nombre = nombre  # Etiqueta del nodo
        self.valores_posibles = valores_posibles  # Valores que puede tomar el nodo
        self.padres = padres  # Lista de nodos padres
        self.probabilidad = probabilidad  # Probabilidades condicionales del nodo
        self.utilidad = utilidad  # Utilidades asociadas a cada valor del nodo

    def obtener_utilidad(self, valor):
        return self.utilidad[valor]  # Obtiene la utilidad asociada a un valor del nodo

    def obtener_probabilidad(self, valor, **padres):
        clave_padres = tuple(padres[variable] for variable in self.padres)  # Obtiene los valores de los nodos padres
        return self.probabilidad[clave_padres][valor]  # Obtiene la probabilidad condicional del nodo dado los valores de los padres


class RedBayesianaDinamica():
    def __init__(self, nodos=[]):
        self.nodos = nodos  # Lista de nodos en la red bayesiana

    def obtener_utilidad_esperada(self, decisiones, **evidencia):
        utilidad_total = 0
        for decision in decisiones:
            evidencia_actual = evidencia.copy()
            evidencia_actual.update(decision)
            utilidad_total += decision['utilidad']  # Añade la utilidad de la decisión actual
            # Calcula la utilidad esperada sumando la utilidad de cada nodo condicionada a la evidencia actual
            for nodo in self.nodos:
                if nodo.nombre not in decision:
                    probabilidad = nodo.obtener_probabilidad(evidencia_actual[nodo.nombre], **evidencia_actual)
                    utilidad = nodo.obtener_utilidad(evidencia_actual[nodo.nombre])
                    utilidad_total += probabilidad * utilidad
        return utilidad_total


# Ejemplo de uso
if __name__ == "__main__":
    # Definición de nodos y sus relaciones
    mercado = NodoRB('Mercado', ['Alto', 'Bajo'])
    inversion = NodoRB('Inversion', ['Si', 'No'], padres=['Mercado'],
                       probabilidad={('Alto',): {'Si': 0.6, 'No': 0.4}, ('Bajo',): {'Si': 0.2, 'No': 0.8}},
                       utilidad={'Si': 100, 'No': 0})

    red_bayesiana = RedBayesianaDinamica([mercado, inversion])  # Creación de la red bayesiana

    # Definición de decisiones posibles y sus utilidades
    decisiones = [{'Mercado': 'Alto', 'Inversion': 'Si', 'utilidad': 100},
                  {'Mercado': 'Alto', 'Inversion': 'No', 'utilidad': 0},
                  {'Mercado': 'Bajo', 'Inversion': 'Si', 'utilidad': 100},
                  {'Mercado': 'Bajo', 'Inversion': 'No', 'utilidad': 0}]

    # Cálculo de la utilidad esperada
    utilidad_esperada = red_bayesiana.obtener_utilidad_esperada(decisiones)
    print("La utilidad esperada es:", utilidad_esperada)
