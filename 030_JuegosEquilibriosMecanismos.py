"""
created on 2 april 23:12:05 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código proporciona una implementación de un Proceso de Decisión de Markov
(MDP) y utiliza el algoritmo de iteración de valor para encontrar la política
óptima en un entorno dado. La clase MDP representa el entorno, con métodos
para inicializar el MDP y ejecutar la iteración de valor. La iteración de valor
calcula los valores óptimos de los estados y deriva la política óptima a
partir de estos valores. Finalmente, se imprime la política óptima.
"""

import numpy as np  # Importa la librería NumPy

class MDP:  # Define una clase para el Proceso de Decisión de Markov (MDP)
    def __init__(self, n_estados, n_acciones, probabilidades_transicion, recompensas, gamma=0.9):
        """
        Inicializa el MDP.

        Args:
            n_estados (int): Número de estados.
            n_acciones (int): Número de acciones.
            probabilidades_transicion (numpy.array): Matriz de probabilidades de transición.
            recompensas (numpy.array): Matriz de recompensas.
            gamma (float): Factor de descuento.
        """
        self.n_estados = n_estados  # Guarda el número de estados en el MDP
        self.n_acciones = n_acciones  # Guarda el número de acciones en el MDP
        self.probabilidades_transicion = probabilidades_transicion  # Guarda la matriz de probabilidades de transición
        self.recompensas = recompensas  # Guarda la matriz de recompensas
        self.gamma = gamma  # Guarda el factor de descuento

    def iteracion_valor(self, epsilon=0.0001):
        """
        Realiza el algoritmo de iteración de valor para encontrar la política óptima.

        Args:
            epsilon (float): Umbral de convergencia.

        Returns:
            numpy.array: Política óptima.
        """
        V = np.zeros(self.n_estados)  # Inicializa los valores de los estados a 0
        while True:  # Bucle hasta que se alcance la convergencia
            delta = 0  # Variable para rastrear el cambio máximo en los valores de los estados
            for s in range(self.n_estados):  # Itera sobre cada estado en el MDP
                v = V[s]  # Almacena el valor actual del estado
                # Calcula el valor de un estado como el máximo valor esperado sobre todas las acciones posibles
                V[s] = max(self.calcular_valor_q(s, a, V) for a in range(self.n_acciones))
                delta = max(delta, abs(v - V[s]))  # Actualiza el cambio máximo
            if delta < epsilon:  # Si la diferencia entre los valores de los estados es menor que epsilon, se detiene
                break

        # Calcula la política óptima a partir de los valores de los estados
        politica = np.zeros((self.n_estados, self.n_acciones))
        for s in range(self.n_estados):
            # Encuentra la mejor acción para cada estado según los valores actuales de los estados
            mejor_accion = np.argmax([self.calcular_valor_q(s, a, V) for a in range(self.n_acciones)])
            politica[s, mejor_accion] = 1  # Asigna probabilidad 1 a la mejor acción
        return politica

    def calcular_valor_q(self, estado, accion, V):
        """
        Calcula el valor Q para un par (estado, acción).

        Args:
            estado (int): Estado.
            accion (int): Acción.
            V (numpy.array): Valores de los estados.

        Returns:
            float: Valor Q.
        """
        # Calcula el valor Q para el par (estado, acción) utilizando la ecuación de Bellman
        return sum(self.probabilidades_transicion[estado, accion, nuevo_estado] * (self.recompensas[estado, accion, nuevo_estado] + self.gamma * V[nuevo_estado]) for nuevo_estado in range(self.n_estados))


# Definición del MDP de ejemplo
n_estados = 3  # Número de estados
n_acciones = 2  # Número de acciones
probabilidades_transicion = np.array([[[0.7, 0.3, 0.0], [1.0, 0.0, 0.0]], [[0.0, 1.0, 0.0], [0.8, 0.2, 0.0]], [[0.8, 0.2, 0.0], [0.0, 0.0, 1.0]]])
recompensas = np.array([[[10, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, -50]]])
mdp = MDP(n_estados, n_acciones, probabilidades_transicion, recompensas)

# Ejecución del algoritmo de iteración de valor para obtener la política óptima
politica_optima = mdp.iteracion_valor()

print("Política óptima:")
print(politica_optima)



