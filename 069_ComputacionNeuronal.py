"""
created on 9 Abril 15:57:34 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código define una neurona artificial con una función de activación sigmoide
y la utiliza para calcular la salida de la neurona dados unos pesos y un sesgo
predefinidos, así como una entrada. La neurona se define como una clase con un
método para calcular la salida (feedforward). Se realiza un cálculo de la
salida de la neurona y se imprime el resultado.
"""
import numpy as np  # Importa la biblioteca numpy para operaciones numéricas eficientes

# Definición de la función de activación sigmoide
def sigmoide(x):
    return 1 / (1 + np.exp(-x))  # La función de activación sigmoide retorna el valor de la función 1 / (1 + e^(-x))

# Definición de la neurona artificial
class Neurona:
    def __init__(self, pesos_neurona, sesgo_neurona):  # Método de inicialización de la clase Neurona
        self.pesos_neurona = pesos_neurona  # Inicializa los pesos de la neurona
        self.sesgo_neurona = sesgo_neurona  # Inicializa el sesgo de la neurona
    
    def feedforward(self, entrada_neurona):  # Método para calcular la salida de la neurona
        total_neurona = np.dot(self.pesos_neurona, entrada_neurona) + self.sesgo_neurona  # Calcula el total ponderado de las entradas más el sesgo
        return sigmoide(total_neurona)  # Aplica la función de activación sigmoide al total y retorna la salida de la neurona

# Pesos y sesgo para la neurona
pesos_neurona = np.array([0.5, -0.5])  # Define los pesos de las conexiones sinápticas
sesgo_neurona = 0.2  # Define el sesgo de la neurona

# Entrada para la neurona
entrada_neurona = np.array([0.3, 0.8])  # Define la entrada de la neurona

# Creación de la neurona
neurona = Neurona(pesos_neurona, sesgo_neurona)  # Crea una instancia de la clase Neurona con los pesos y sesgo dados

# Cálculo de la salida de la neurona
salida_neurona = neurona.feedforward(entrada_neurona)  # Calcula la salida de la neurona dada la entrada

# Impresión de la salida
print("Salida de la neurona:", salida_neurona)  # Imprime la salida de la neurona
