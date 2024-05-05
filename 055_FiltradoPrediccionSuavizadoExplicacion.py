"""
created on 7 Abril 12:19:09 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa un Filtro de Kalman, una técnica de estimación que utiliza
mediciones ruidosas para estimar el estado de un sistema dinámico.
Utiliza parámetros del modelo del sistema, como la matriz de transición de
estado y la covarianza del ruido, para predecir y actualizar el estado del
sistema en función de las mediciones. Finalmente, grafica la posición verdadera
, las mediciones ruidosas y la posición estimada por el filtro de Kalman a lo
largo del tiempo.
"""
import numpy as np
import matplotlib.pyplot as plt

class FiltroKalman:
    def __init__(self, A, B, H, Q, R, estado_inicial):
        # Inicializa el Filtro de Kalman con los parámetros del modelo y el estado inicial.
        self.A = A  # Matriz de transición de estado
        self.B = B  # Matriz de control
        self.H = H  # Matriz de observación
        self.Q = Q  # Covarianza del ruido de proceso
        self.R = R  # Covarianza del ruido de medición
        self.estado = estado_inicial  # Estado inicial
        self.covarianza = np.eye(len(estado_inicial))  # Covarianza inicial

    def predecir(self, entrada_control=None):
        # Predice el siguiente estado.
        if entrada_control is not None:
            self.estado = np.dot(self.A, self.estado) + np.dot(self.B, entrada_control)
        else:
            self.estado = np.dot(self.A, self.estado)
        self.covarianza = np.dot(np.dot(self.A, self.covarianza), self.A.T) + self.Q

    def actualizar(self, medida):
        # Actualiza el estado basado en la medición.
        innovacion = medida - np.dot(self.H, self.estado)
        covarianza_innovacion = np.dot(np.dot(self.H, self.covarianza), self.H.T) + self.R
        ganancia_kalman = np.dot(np.dot(self.covarianza, self.H.T), np.linalg.inv(covarianza_innovacion))
        self.estado += np.dot(ganancia_kalman, innovacion)
        self.covarianza = np.dot(np.eye(len(self.estado)) - np.dot(ganancia_kalman, self.H), self.covarianza)

# Parámetros del modelo del sistema
dt = 0.1  # Intervalo de tiempo entre las actualizaciones
A = np.array([[1, dt], [0, 1]])  # Matriz de transición de estado
B = np.array([[0.5*dt**2], [dt]])  # Matriz de control
H = np.array([[1, 0]])  # Matriz de observación
Q = np.array([[0.1, 0], [0, 0.1]])  # Covarianza del ruido de proceso
R = np.array([[1]])  # Covarianza del ruido de medición

# Estado inicial y medición inicial
estado_inicial = np.array([0, 0])  # [posición, velocidad]
medicion_inicial = np.array([0])  # Posición medida inicialmente

# Crear el Filtro de Kalman
fk = FiltroKalman(A, B, H, Q, R, estado_inicial)

# Simulación de movimiento y medición
num_pasos = 100
posiciones_verdaderas = []
mediciones = []
posiciones_filtradas = []

for i in range(num_pasos):
    posicion_verdadera = 0.5 * 9.8 * dt**2 * i**2  # Movimiento simulado del objeto (caída libre)
    medicion = posicion_verdadera + np.random.normal(0, 1)  # Simular medición con ruido gaussiano
    fk.predecir()  # Predicción del siguiente estado
    fk.actualizar(medicion)  # Actualización del estado basado en la medición
    posiciones_verdaderas.append(posicion_verdadera)
    mediciones.append(medicion)
    posiciones_filtradas.append(fk.estado[0])

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(range(num_pasos), posiciones_verdaderas, label='Posición Verdadera')
plt.plot(range(num_pasos), mediciones, label='Medición Ruidosa', marker='o', linestyle='', color='r')
plt.plot(range(num_pasos), posiciones_filtradas, label='Posición Filtrada', linestyle='--', color='g')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Filtro de Kalman: Predicción y Estimación de Posición')
plt.legend()
plt.grid(True)
plt.show()
