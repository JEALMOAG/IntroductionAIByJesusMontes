"""
created on 3 april 11:17:45 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa un modelo de Proceso de Decisión de Markov Parcialmente
Observado (POMDP) utilizando Python y NumPy. Define una clase POMDP que
representa un POMDP con sus estados, acciones, observaciones, probabilidades
de transición, probabilidades de observación, recompensas y factor de descuento.
Utiliza el algoritmo de iteración de valor para encontrar la política óptima
y la función de valor asociada. El ejemplo al final del código ilustra cómo
utilizar la clase POMDP con parámetros específicos.
"""
import numpy as np
# Importa la librería numpy para operaciones matemáticas

class POMDP:  # Define una clase para el POMDP
    def __init__(self, estados, acciones, observaciones, probabilidades_transicion, probabilidades_observacion, recompensas, factor_descuento):
        # Inicializa los atributos de la clase con los parámetros dados
        self.estados = estados  # Estados posibles del POMDP
        self.acciones = acciones  # Acciones posibles del POMDP
        self.observaciones = observaciones  # Observaciones posibles del POMDP
        self.prob_transicion = probabilidades_transicion  # Probabilidades de transición del POMDP
        self.prob_observacion = probabilidades_observacion  # Probabilidades de observación del POMDP
        self.recompensas = recompensas  # Recompensas del POMDP
        self.factor_descuento = factor_descuento  # Factor de descuento del POMDP

    def iteracion_valor(self, epsilon=0.01):
        # Implementa el algoritmo de iteración de valor para encontrar la política óptima
        V = {s: 0 for s in self.estados}  # Inicializa la función de valor V arbitrariamente para cada estado

        while True:
            delta = 0  # Inicializa el cambio en la función de valor en esta iteración
            for s in self.estados:  # Para cada estado s en los estados posibles
                v = V[s]  # Almacena el valor actual de V[s]
                # Calcula el nuevo valor de V[s] como el máximo valor Q(s, a) para todas las acciones a
                V[s] = max([self.calcular_valor_q(s, a, V) for a in self.acciones])
                # Actualiza delta al máximo cambio en V[s] en esta iteración
                delta = max(delta, abs(v - V[s]))
            # Si el cambio en V[s] es menor que epsilon, se considera que ha convergido y se termina el bucle
            if delta < epsilon:
                break

        # Una vez convergido, extrae la política óptima
        politica = {}
        for s in self.estados:
            # Para cada estado, selecciona la acción que maximiza Q(s, a) como la acción óptima
            politica[s] = max(self.acciones, key=lambda a: self.calcular_valor_q(s, a, V))
        
        return V, politica

    def calcular_valor_q(self, estado, accion, V):
        # Calcula el valor Q(s, a) para un estado y una acción dados
        valor_q = sum([
            # Suma sobre todos los posibles estados siguientes
            self.prob_transicion[estado][accion][siguiente_estado] *
            (self.recompensas[estado][accion][siguiente_estado] +
            self.factor_descuento * V[siguiente_estado])
            for siguiente_estado in self.estados  # Para cada estado siguiente en los estados posibles
        ])
        return valor_q

    def observar(self, estado, accion, observacion):
        # Calcula la creencia posterior basada en la observación
        creencia = {}
        for siguiente_estado in self.estados:  # Para cada estado siguiente en los estados posibles
            # Calcula la creencia como la suma ponderada de la creencia anterior y la probabilidad de transición y observación
            creencia[siguiente_estado] = sum([
                self.prob_transicion[estado][accion][siguiente_estado] *
                self.prob_observacion[accion][siguiente_estado][observacion] *
                (self.recompensas[estado][accion][siguiente_estado] +
                self.factor_descuento * V[siguiente_estado])
                for estado in self.estados  # Para cada estado en los estados posibles
            ])
        return creencia

# Ejemplo de POMDP
estados = ['Soleado', 'Lluvioso']  # Define los estados posibles
acciones = ['Quedarse', 'Moverse']  # Define las acciones posibles
observaciones = ['Soleado', 'Lluvioso']  # Define las observaciones posibles
probabilidades_transicion = {
    'Soleado': {'Quedarse': {'Soleado': 0.8, 'Lluvioso': 0.2}, 'Moverse': {'Soleado': 0.2, 'Lluvioso': 0.8}},
    'Lluvioso': {'Quedarse': {'Soleado': 0.4, 'Lluvioso': 0.6}, 'Moverse': {'Soleado': 0.6, 'Lluvioso': 0.4}}
}  # Define las probabilidades de transición
probabilidades_observacion = {
    'Quedarse': {
        'Soleado': {'Soleado': 0.8, 'Lluvioso': 0.2},
        'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}
    },
    'Moverse': {
        'Soleado': {'Soleado': 0.6, 'Lluvioso': 0.4},
        'Lluvioso
