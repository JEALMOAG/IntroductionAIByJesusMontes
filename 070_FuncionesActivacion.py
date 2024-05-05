"""
created on 9 Abril 18:03:12 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código define varias funciones de activación comúnmente utilizadas en redes
neuronales, como la función sigmoide, ReLU, tangente hiperbólica (tanh) y
softmax. Luego, genera datos de entrada y aplica estas funciones de activación
a esos datos. Finalmente, visualiza las curvas resultantes de las funciones de
activación en un gráfico.
"""
import numpy as np  # Importa la biblioteca numpy y la renombra como np
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib.pyplot y la renombra como plt

# Definición de las funciones de activación
def sigmoide(x):  # Define la función de activación sigmoide
    return 1 / (1 + np.exp(-x))

def relu(x):  # Define la función de activación ReLU
    return np.maximum(0, x)

def tangente_hiperbolica(x):  # Define la función de activación tangente hiperbólica (tanh)
    return np.tanh(x)

def softmax(x):  # Define la función de activación softmax
    valores_exp = np.exp(x - np.max(x, axis=0))  # Calcula los valores exponenciales de x
    return valores_exp / np.sum(valores_exp, axis=0)  # Calcula la función softmax de los valores exponenciales

# Datos de entrada
x = np.linspace(-5, 5, 100)  # Genera 100 puntos equidistantes entre -5 y 5 como valores de entrada

# Aplicación de las funciones de activación a los datos de entrada
y_sigmoide = sigmoide(x)  # Aplica la función sigmoide a los datos de entrada
y_relu = relu(x)  # Aplica la función ReLU a los datos de entrada
y_tanh = tangente_hiperbolica(x)  # Aplica la función tangente hiperbólica (tanh) a los datos de entrada
y_softmax = softmax(x)  # Aplica la función softmax a los datos de entrada

# Visualización de las funciones de activación
plt.figure(figsize=(10, 6))  # Crea una nueva figura con tamaño 10x6 pulgadas

plt.plot(x, y_sigmoide, label='Sigmoide', color='blue')  # Grafica la función sigmoide
plt.plot(x, y_relu, label='ReLU', color='red')  # Grafica la función ReLU
plt.plot(x, y_tanh, label='Tanh', color='green')  # Grafica la función tangente hiperbólica (tanh)
plt.plot(x, y_softmax, label='Softmax', color='purple')  # Grafica la función softmax

plt.title('Funciones de Activación')  # Establece el título del gráfico como 'Funciones de Activación'
plt.xlabel('x')  # Etiqueta el eje x como 'x'
plt.ylabel('y')  # Etiqueta el eje y como 'y'
plt.legend()  # Muestra la leyenda
plt.grid(True)  # Muestra la cuadrícula en el gráfico
plt.show()  # Muestra el gráfico
