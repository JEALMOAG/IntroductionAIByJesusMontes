"""
created on 10 Abril 03:34:18  2024
@author:Jesus Alejandro Montes Aguila
"""
"""
Este código define tres tipos de redes neuronales simples: Perceptrón,
Adaline y Madaline. Cada una puede ser utilizada para resolver diferentes
tipos de problemas de clasificación. El código proporciona métodos para
entrenar estas redes y hacer predicciones con ellas. Además, incluye un
ejemplo de cómo usar cada una de estas redes para resolver problemas de
compuerta lógica AND, OR y XOR.
"""
import numpy as np  # Importa la biblioteca numpy y la renombra como np

class Perceptron:  # Define la clase Perceptrón
    def __init__(self, num_entradas, tasa_aprendizaje=0.01, epocas=100):  # Define el método de inicialización
        self.num_entradas = num_entradas  # Establece el número de entradas del perceptrón
        self.tasa_aprendizaje = tasa_aprendizaje  # Establece la tasa de aprendizaje
        self.epocas = epocas  # Establece el número de épocas
        self.pesos = np.zeros(num_entradas + 1)  # Inicializa los pesos del perceptrón con ceros
    
    def predecir(self, entradas):  # Define el método para hacer predicciones
        suma_ponderada = np.dot(entradas, self.pesos[1:]) + self.pesos[0]  # Calcula la suma ponderada de las entradas y los pesos
        return 1 if suma_ponderada > 0 else 0  # Devuelve 1 si la suma es mayor que cero, de lo contrario, devuelve 0
    
    def entrenar(self, entradas_entrenamiento, etiquetas):  # Define el método para entrenar el perceptrón
        for _ in range(self.epocas):  # Itera sobre el número de épocas
            for entradas, etiqueta in zip(entradas_entrenamiento, etiquetas):  # Itera sobre los datos de entrenamiento y las etiquetas
                prediccion = self.predecir(entradas)  # Realiza una predicción
                self.pesos[1:] += self.tasa_aprendizaje * (etiqueta - prediccion) * entradas  # Actualiza los pesos de las entradas
                self.pesos[0] += self.tasa_aprendizaje * (etiqueta - prediccion)  # Actualiza el sesgo

class Adaline:  # Define la clase Adaline
    def __init__(self, num_entradas, tasa_aprendizaje=0.01, epocas=100):  # Define el método de inicialización
        self.num_entradas = num_entradas  # Establece el número de entradas de Adaline
        self.tasa_aprendizaje = tasa_aprendizaje  # Establece la tasa de aprendizaje
        self.epocas = epocas  # Establece el número de épocas
        self.pesos = np.zeros(num_entradas + 1)  # Inicializa los pesos de Adaline con ceros
        
    def predecir(self, entradas):  # Define el método para hacer predicciones
        suma_ponderada = np.dot(entradas, self.pesos[1:]) + self.pesos[0]  # Calcula la suma ponderada de las entradas y los pesos
        return 1 if suma_ponderada > 0 else 0  # Devuelve 1 si la suma es mayor que cero, de lo contrario, devuelve 0
    
    def entrenar(self, entradas_entrenamiento, etiquetas):  # Define el método para entrenar Adaline
        for _ in range(self.epocas):  # Itera sobre el número de épocas
            for entradas, etiqueta in zip(entradas_entrenamiento, etiquetas):  # Itera sobre los datos de entrenamiento y las etiquetas
                prediccion = self.predecir(entradas)  # Realiza una predicción
                self.pesos[1:] += self.tasa_aprendizaje * (etiqueta - prediccion) * entradas  # Actualiza los pesos de las entradas
                self.pesos[0] += self.tasa_aprendizaje * (etiqueta - prediccion)  # Actualiza el sesgo

class Madaline:  # Define la clase Madaline
    def __init__(self, num_entradas, num_salidas, tasa_aprendizaje=0.01, epocas=100):  # Define el método de inicialización
        self.num_entradas = num_entradas  # Establece el número de entradas de Madaline
        self.num_salidas = num_salidas  # Establece el número de salidas de Madaline
        self.tasa_aprendizaje = tasa_aprendizaje  # Establece la tasa de aprendizaje
        self.epocas = epocas  # Establece el número de épocas
        self.pesos = np.zeros((num_entradas + 1, num_salidas))  # Inicializa los pesos de Madaline con ceros
        
    def predecir(self, entradas):  # Define el método para hacer predicciones
        suma_ponderada = np.dot(entradas, self.pesos[1:, :]) + self.pesos[0, :]  # Calcula la suma ponderada de las entradas y los pesos
        return np.where(suma_ponderada > 0, 1, 0)  # Devuelve 1 si la suma es mayor que cero, de lo contrario, devuelve 0
    
    def entrenar(self, entradas_entrenamiento, etiquetas):  # Define el método para entrenar Madaline
        for _ in range(self.epocas):  # Itera sobre el número de épocas
            for entradas, etiqueta in zip(entradas_entrenamiento, etiquetas):  # Itera sobre los datos de entrenamiento y las etiquetas
                prediccion = self.predecir(entradas)  # Realiza una predicción
                self.pesos[1:, :] += self.tasa_aprendizaje * np.outer(entradas, (etiqueta - prediccion))  # Actualiza los pesos de las entradas
                self.pesos[0, :] += self.tasa_aprendizaje * (etiqueta - prediccion)  # Actualiza el sesgo

# Ejemplo de uso

# Datos de entrada
X = np.array([[0, 0]
