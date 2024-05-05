"""
created on 10 Abril 17:06:45 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa una red neuronal artificial con una capa oculta para
resolver el problema XOR. Utiliza la biblioteca NumPy para operaciones
numéricas eficientes. Comienza definiendo la función sigmoide y su derivada.
Luego, genera datos de entrada y salida para el problema XOR. Posteriormente,
inicializa los pesos y sesgos de la red. A continuación, entrena la red
utilizando el algoritmo de retropropagación del error durante un número
específico de épocas. Finalmente, imprime los pesos y sesgos finales, así como
las predicciones finales de la red.
"""
import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas eficientes

# Definición de la función de activación sigmoide y su derivada
def sigmoide(x):
    return 1 / (1 + np.exp(-x))  # Definición de la función sigmoide

def derivada_sigmoide(x):
    return x * (1 - x)  # Derivada de la función sigmoide

# Datos de entrada y salida
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Matriz de entrada: características
y = np.array([[0], [1], [1], [0]])  # Matriz de salida: etiquetas

# Inicialización de pesos y sesgos
np.random.seed(1)  # Fijamos la semilla aleatoria para reproducibilidad
tamanio_entrada = 2  # Tamaño de la capa de entrada
tamanio_oculta = 4  # Tamaño de la capa oculta
tamanio_salida = 1  # Tamaño de la capa de salida
tasa_aprendizaje = 0.1  # Tasa de aprendizaje para ajustar los pesos

# Pesos para la capa oculta y la capa de salida
pesos_entrada_oculta = np.random.uniform(size=(tamanio_entrada, tamanio_oculta))  # Pesos para la capa oculta
pesos_oculta_salida = np.random.uniform(size=(tamanio_oculta, tamanio_salida))  # Pesos para la capa de salida

# Sesgos para la capa oculta y la capa de salida
sesgo_oculta = np.random.uniform(size=(1, tamanio_oculta))  # Sesgo para la capa oculta
sesgo_salida = np.random.uniform(size=(1, tamanio_salida))  # Sesgo para la capa de salida

# Entrenamiento de la red neuronal utilizando retropropagación del error
epocas = 10000  # Número de épocas de entrenamiento
for epoca in range(epocas):  # Para cada época de entrenamiento
    # Forward propagation (propagación hacia adelante)
    entrada_oculta = np.dot(X, pesos_entrada_oculta) + sesgo_oculta  # Entrada ponderada a la capa oculta
    salida_oculta = sigmoide(entrada_oculta)  # Salida de la capa oculta
    salida = np.dot(salida_oculta, pesos_oculta_salida) + sesgo_salida  # Entrada ponderada a la capa de salida
    salida_predicha = sigmoide(salida)  # Salida de la capa de salida
    
    # Cálculo del error
    error = y - salida_predicha  # Error entre la salida deseada y la salida predicha
    
    # Backpropagation (retropropagación)
    delta_salida = error * derivada_sigmoide(salida_predicha)  # Delta de error en la capa de salida
    error_oculta = delta_salida.dot(pesos_oculta_salida.T)  # Error en la capa oculta
    delta_oculta = error_oculta * derivada_sigmoide(salida_oculta)  # Delta de error en la capa oculta
    
    # Actualización de pesos y sesgos
    pesos_oculta_salida += salida_oculta.T.dot(delta_salida) * tasa_aprendizaje  # Actualización de pesos de la capa de salida
    pesos_entrada_oculta += X.T.dot(delta_oculta) * tasa_aprendizaje  # Actualización de pesos de la capa oculta
    sesgo_salida += np.sum(delta_salida, axis=0, keepdims=True) * tasa_aprendizaje  # Actualización del sesgo de la capa de salida
    sesgo_oculta += np.sum(delta_oculta, axis=0, keepdims=True) * tasa_aprendizaje  # Actualización del sesgo de la capa oculta

# Imprimir los resultados finales
print("Pesos de la capa oculta:")
print(pesos_entrada_oculta)  # Imprimir los pesos de la capa oculta
print("\nPesos de la capa de salida:")
print(pesos_oculta_salida)  # Imprimir los pesos de la capa de salida
print("\nSesgo de la capa oculta:")
print(sesgo_oculta)  # Imprimir el sesgo de la capa oculta
print("\nSesgo de la capa de salida:")
print(sesgo_salida)  # Imprimir el sesgo de la capa de salida

# Predicción final
print("\nPredicciones finales:")
print(salida_predicha)  # Imprimir las predicciones finales




