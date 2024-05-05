"""
created on 8 Abril 07:45:23  2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa un filtro de partículas, una técnica de estimación
utilizada en sistemas de localización y seguimiento. Este filtro estima el
estado de un sistema basado en observaciones ruidosas y un modelo de movimiento.
Utiliza un conjunto de partículas para representar la distribución de
probabilidad del estado del sistema. En cada paso de tiempo, las partículas se
desplazan según el modelo de movimiento, se actualizan con la información de la
observación actual y se reponderan de acuerdo con su ajuste a la observación.
Finalmente, se estima el estado del sistema utilizando la media ponderada de
las partículas.
"""
import numpy as np
# Importamos la biblioteca NumPy para operaciones matriciales

class FiltroParticulas:
    def __init__(self, cantidad_particulas, limite_superior_espacio_estado):
        self.cantidad_particulas = cantidad_particulas  # Número de partículas
        self.limite_superior_espacio_estado = limite_superior_espacio_estado  # Límite superior del espacio de estado
        # Inicializamos las partículas aleatorias uniformemente en el intervalo [0, limite_superior_espacio_estado)
        self.particulas = np.random.uniform(0, limite_superior_espacio_estado, cantidad_particulas)
        # Inicializamos los pesos de las partículas uniformemente
        self.pesos = np.ones(cantidad_particulas) / cantidad_particulas

    def predecir(self, desplazamiento):
        # Movemos las partículas según el modelo de movimiento (aquí, solo se suma el desplazamiento)
        self.particulas += desplazamiento
        # Manejamos el desbordamiento del límite superior del espacio de estado
        self.particulas %= self.limite_superior_espacio_estado

    def actualizar(self, medicion, varianza_sensor):
        # Calculamos la probabilidad de la medición para cada partícula usando una distribución Gaussiana
        verosimilitudes = 1 / np.sqrt(2 * np.pi * varianza_sensor) * np.exp(-0.5 * ((medicion - self.particulas) ** 2) / varianza_sensor)
        # Actualizamos los pesos multiplicando por la probabilidad de la medición
        self.pesos *= verosimilitudes
        # Normalizamos los pesos para que sumen 1
        self.pesos /= np.sum(self.pesos)

    def reponderar(self):
        # Resampleamos las partículas basadas en sus pesos
        indices = np.random.choice(np.arange(self.cantidad_particulas), size=self.cantidad_particulas, p=self.pesos)
        self.particulas = self.particulas[indices]
        self.pesos = np.ones(self.cantidad_particulas) / self.cantidad_particulas

    def estimar_estado(self):
        # Estimamos el estado utilizando la media de las partículas ponderadas por sus pesos
        estado_estimado = np.sum(self.particulas * self.pesos)
        return estado_estimado

# Parámetros del filtro de partículas
cantidad_particulas = 1000  # Número de partículas
limite_superior_espacio_estado = 10  # Límite superior del espacio de estado
varianza_sensor = 0.1  # Varianza del sensor

# Crear el filtro de partículas
filtro = FiltroParticulas(cantidad_particulas, limite_superior_espacio_estado)

# Simulación
desplazamientos = np.random.normal(1, 0.5, 100)  # Generar desplazamientos aleatorios
# Generar mediciones ruidosas (en este caso, una señal sinusoidal con ruido gaussiano)
mediciones_verdaderas = np.sin(np.linspace(0, 2*np.pi, 100)) + np.random.normal(0, np.sqrt(varianza_sensor), 100)

# Actualizar el filtro de partículas y estimar el estado en cada paso de tiempo
for desplazamiento, medicion in zip(desplazamientos, mediciones_verdaderas):
    filtro.predecir(desplazamiento)  # Predicción del estado futuro basada en el modelo de movimiento
    filtro.actualizar(medicion, varianza_sensor)  # Actualización basada en la medición actual
    filtro.reponderar()  # Reponderación de las partículas basada en los pesos actualizados
    estado_estimado = filtro.estimar_estado()  # Estimación del estado basada en las partículas y pesos
    print("Estado estimado:", estado_estimado)  # Imprimir la estimación del estado en cada paso de tiempo
