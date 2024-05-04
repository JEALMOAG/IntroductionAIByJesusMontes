"""
created on 4 april 09:18:34 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa un agente que interactúa con un entorno de
Bandit Multi-Brazo. El agente utiliza la estrategia Epsilon-Greedy para
seleccionar acciones, equilibrando la exploración y la explotación.
Cada acción tiene una recompensa asociada, y el agente actualiza sus estimaciones
de los valores de las acciones a medida que interactúa con el entorno.
La interacción se realiza a lo largo de un número de pasos definido, acumulando
las recompensas obtenidas para evaluar el rendimiento del agente.
"""
import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas

class AgenteExploradorEpsilon:
    def __init__(self, num_opciones, epsilon=0.1):
        self.num_opciones = num_opciones  # Número de opciones disponibles para el agente
        self.epsilon = epsilon  # Parámetro epsilon para la estrategia epsilon-greedy
        self.valores_opcion = np.zeros(num_opciones)  # Valor estimado de cada opción
        self.contadores_opcion = np.zeros(num_opciones)  # Número de veces que se ha seleccionado cada opción

    def seleccionar_opcion(self):
        if np.random.rand() < self.epsilon:  # Exploración: con probabilidad epsilon
            opcion = np.random.randint(self.num_opciones)  # Se elige una opción aleatoria
        else:  # Explotación: con probabilidad 1-epsilon
            opcion = np.argmax(self.valores_opcion)  # Se elige la opción con el mayor valor estimado
        return opcion

    def actualizar_valor_opcion(self, opcion, recompensa):
        self.contadores_opcion[opcion] += 1  # Se incrementa el contador de la opción seleccionada
        # Se actualiza el valor estimado de la opción mediante una media ponderada
        self.valores_opcion[opcion] += (recompensa - self.valores_opcion[opcion]) / self.contadores_opcion[opcion]

# Entorno de bandit multi-armado simple
class BanditMultiBrazo:
    def __init__(self, num_opciones):
        self.num_opciones = num_opciones  # Número de opciones en el bandit multi-brazo
        # Valores reales de cada opción (extraídos de una distribución normal)
        self.valores_opcion_real = np.random.normal(loc=0, scale=1, size=num_opciones)

    def obtener_recompensa(self, opcion):
        # La recompensa es una muestra de una distribución normal con media igual al valor real de la opción
        return np.random.normal(loc=self.valores_opcion_real[opcion], scale=1)

# Ejemplo de uso
num_opciones = 5  # Número de opciones en el bandit multi-brazo
num_pasos = 1000  # Número de pasos de interacción agente-entorno
epsilon = 0.1  # Parámetro epsilon para la estrategia epsilon-greedy

bandit = BanditMultiBrazo(num_opciones)  # Crear el bandit multi-brazo
agente = AgenteExploradorEpsilon(num_opciones, epsilon)  # Crear el agente epsilon-greedy

recompensa_total = 0  # Inicializar la recompensa total acumulada

# Iterar sobre los pasos de interacción agente-entorno
for _ in range(num_pasos):
    opcion = agente.seleccionar_opcion()  # El agente selecciona una opción
    recompensa = bandit.obtener_recompensa(opcion)  # El entorno devuelve la recompensa para la opción seleccionada
    agente.actualizar_valor_opcion(opcion, recompensa)  # El agente actualiza su estimación del valor de la opción
    recompensa_total += recompensa  # Se acumula la recompensa obtenida

print("Recompensa total obtenida:", recompensa_total)  # Imprimir la recompensa total obtenida

