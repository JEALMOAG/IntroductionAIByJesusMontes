"""
created on 4 april 12:34:09 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código proporciona una implementación de la búsqueda de política en un
entorno de aprendizaje por refuerzo utilizando el algoritmo de iteración de
valor. Utiliza la estrategia de valoración de estados para encontrar la política
óptima. El algoritmo busca iterativamente los valores de los estados hasta que
convergen por debajo de un umbral predefinido. Luego, utiliza estos valores
para determinar la política óptima, que es la estrategia que maximiza el valor
esperado de las acciones en cada estado. El ejemplo de uso demuestra cómo se
puede aplicar este algoritmo en un problema de modelo de transiciones y
recompensas predefinidos.
"""
import numpy as np

class EstrategiaPolitica():
    def __init__(self, num_estados, num_acciones, factor_descuento=0.9, umbral_convergencia=1e-5):
        self.num_estados = num_estados  # Número de estados
        self.num_acciones = num_acciones  # Número de acciones
        self.factor_descuento = factor_descuento  # Factor de descuento
        self.umbral_convergencia = umbral_convergencia  # Umbral de convergencia
        self.V = np.zeros(num_estados)  # Valores de los estados

    def encontrar_politica(self, modelo_transiciones, recompensas):
        while True:
            delta = 0
            # Iterar sobre todos los estados
            for s in range(self.num_estados):
                v = self.V[s]  # Almacenar el valor actual del estado
                # Calcular el nuevo valor del estado como el máximo de los valores futuros
                self.V[s] = max([sum([p * (recompensas[s][a] + self.factor_descuento * self.V[s1]) for (p, s1) in modelo_transiciones[s][a]]) for a in range(self.num_acciones)])
                # Calcular la diferencia de valores para verificar la convergencia
                delta = max(delta, abs(v - self.V[s]))
            # Comprobar si se ha alcanzado la convergencia
            if delta < self.umbral_convergencia:
                break

        # Construir la política óptima basada en los valores de los estados
        politica = np.zeros(self.num_estados, dtype=int)
        for s in range(self.num_estados):
            # Para cada estado, elegir la acción que maximice el valor esperado
            politica[s] = np.argmax([sum([p * (recompensas[s][a] + self.factor_descuento * self.V[s1]) for (p, s1) in modelo_transiciones[s][a]]) for a in range(self.num_acciones)])

        return politica


# Ejemplo de uso
if __name__ == "__main__":
    # Definición de modelo de transiciones y recompensas
    num_estados = 3  # Número de estados
    num_acciones = 2  # Número de acciones

    # Modelo de transiciones: especifica las probabilidades de transición y los estados alcanzables dado un estado-acción
    modelo_transiciones = [
        # Estado 0
        [[(0.8, 0), (0.2, 1)],  # Acción 0
         [(0.1, 0), (0.9, 1)]],  # Acción 1
        # Estado 1
        [[(0.7, 0), (0.3, 2)],  # Acción 0
         [(0.5, 0), (0.5, 2)]],  # Acción 1
        # Estado 2
        [[(0.6, 2), (0.4, 2)],  # Acción 0
         [(0.0, 0), (1.0, 2)]]   # Acción 1
    ]

    # Recompensas: especifica las recompensas asociadas a cada estado-acción
    recompensas = [
        [-1, 0],  # Estado 0
        [-1, -1], # Estado 1
        [0, 1]    # Estado 2
    ]

    # Crear instancia de la clase EstrategiaPolitica
    estrategia_politica = EstrategiaPolitica(num_estados, num_acciones)

    # Encontrar la política óptima
    politica_optima = estrategia_politica.encontrar_politica(modelo_transiciones, recompensas)

    # Imprimir la política óptima encontrada
    print("Política óptima encontrada:", politica_optima)
