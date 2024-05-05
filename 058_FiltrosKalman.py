"""
created on 7 Abril 21:34:49 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa un Filtro de Kalman para estimar el estado de un sistema
dinámico a partir de mediciones ruidosas. Utiliza matrices y vectores para
representar el estado del sistema, las mediciones y las incertidumbres asociadas
. El filtro predice el siguiente estado del sistema y lo actualiza en función
de las mediciones observadas. El proceso se repite para cada observación,
proporcionando una estimación precisa del estado del sistema a lo largo del
tiempo.
"""
import numpy as np  # Importamos la biblioteca NumPy para operaciones matriciales

class FiltroKalman:
    def __init__(self, estado_inicial, covarianza_inicial, matriz_transicion, covarianza_proceso, matriz_observacion, covarianza_observacion):
        self.x = estado_inicial  # Estado inicial
        self.P = covarianza_inicial  # Covarianza inicial
        self.A = matriz_transicion    # Matriz de transición de estado
        self.Q = covarianza_proceso    # Covarianza del proceso
        self.H = matriz_observacion    # Matriz de observación
        self.R = covarianza_observacion    # Covarianza de la observación

    def predecir(self):
        # Predicción del siguiente estado
        self.x = np.dot(self.A, self.x)  # Actualizamos el estado prediciendo el siguiente estado
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q  # Actualizamos la covarianza

    def actualizar(self, z):
        # Actualización del estado basado en la observación
        y = z - np.dot(self.H, self.x)  # Calculamos la diferencia entre la observación y la predicción
        S = np.dot(np.dot(self.H, self.P), self.H.T) + self.R  # Calculamos la covarianza de la innovación
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))  # Calculamos la ganancia de Kalman
        self.x = self.x + np.dot(K, y)  # Actualizamos el estado usando la ganancia de Kalman
        self.P = self.P - np.dot(np.dot(K, self.H), self.P)  # Actualizamos la covarianza

# Definir las matrices y vectores necesarios para el filtro de Kalman
intervalo_tiempo = 1.0  # Intervalo de tiempo entre mediciones
matriz_transicion = np.array([[1, intervalo_tiempo], [0, 1]])  # Matriz de transición de estado (modelo de movimiento)
matriz_observacion = np.array([[1, 0]])           # Matriz de observación (modelo de medición)
covarianza_proceso = np.array([[0.1, 0], [0, 0.1]])  # Covarianza del proceso (ruido del proceso)
covarianza_observacion = np.array([[1]])                 # Covarianza de la observación (ruido de la medición)

# Condiciones iniciales
estado_inicial = np.array([[0], [0]])  # Estado inicial (posición y velocidad)
covarianza_inicial = np.eye(2)             # Covarianza inicial (incertidumbre inicial)

# Crear el filtro de Kalman
filtro_kalman = FiltroKalman(estado_inicial, covarianza_inicial, matriz_transicion, covarianza_proceso, matriz_observacion, covarianza_observacion)

# Simular un objeto moviéndose y realizar la estimación con el filtro de Kalman
observaciones = [1, 2, 3, 4, 5]  # Observaciones de posición del objeto
for z in observaciones:
    filtro_kalman.predecir()        # Predicción del siguiente estado
    filtro_kalman.actualizar(np.array([[z]]))  # Actualización basada en la observación
    print("Estimación de posición:", filtro_kalman.x[0, 0])  # Mostrar la estimación de posición
