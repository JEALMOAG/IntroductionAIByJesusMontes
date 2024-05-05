"""
created on 10 Abril 06:23:45  2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código define y entrena un modelo de red neuronal para un problema de
separabilidad lineal utilizando TensorFlow y Keras. Primero, genera datos
de ejemplo que representan dos clases separables linealmente.
Luego, visualiza los datos y procede a definir un modelo de red neuronal con
una capa densa y activación sigmoide. Después, compila y entrena el modelo
utilizando los datos generados. Finalmente, evalúa el modelo en los datos de
entrenamiento y muestra la precisión obtenida.
"""
import numpy as np
# Importa la biblioteca numpy para operaciones numéricas
import matplotlib.pyplot as plt
# Importa la biblioteca matplotlib para visualización
import tensorflow as tf
# Importa la biblioteca TensorFlow para redes neuronales
from tensorflow.keras.models import Sequential
# Importa la clase Secuencial para crear modelos secuenciales
from tensorflow.keras.layers import Dense
# Importa la capa Densa para capas totalmente conectadas

# Generar datos de ejemplo para un problema de separabilidad lineal
np.random.seed(0)
# Fija la semilla aleatoria para reproducibilidad
num_muestras = 200
# Número de muestras de datos
X_datos = np.random.normal(loc=0, scale=1, size=(num_muestras, 2))
# Genera características de entrada con distribución normal
y_etiquetas = (X_datos[:, 0] + X_datos[:, 1] > 0).astype(int)
# Etiquetas: 1 si la suma de las características es positiva, 0 en otro caso

# Visualizar los datos
plt.figure(figsize=(8, 6))
# Configura el tamaño de la figura
plt.scatter(X_datos[:, 0], X_datos[:, 1], c=y_etiquetas, cmap='bwr', marker='o', edgecolors='k')  # Grafica los puntos de acuerdo a las etiquetas
plt.title('Datos de ejemplo para separabilidad lineal')
# Establece el título del gráfico
plt.xlabel('Característica 1')
# Etiqueta del eje x
plt.ylabel('Característica 2')
# Etiqueta del eje y
plt.show()  # Muestra el gráfico

# Definir el modelo de red neuronal
modelo = Sequential([
    # Crea un modelo secuencial
    Dense(1, activation='sigmoid', input_shape=(2,))
    # Agrega una capa densa con una neurona y función de activación sigmoide
])

# Compilar el modelo
modelo.compile(optimizer='adam',
               # Configura el optimizador Adam
              loss='binary_crossentropy',
               # Configura la función de pérdida de entropía cruzada binaria
              metrics=['accuracy'])
# Configura la métrica de precisión

# Entrenar el modelo
historial = modelo.fit(X_datos, y_etiquetas, epochs=100, verbose=0)
# Entrena el modelo en los datos de entrada y etiquetas

# Graficar la pérdida durante el entrenamiento
plt.figure(figsize=(8, 6))
# Configura el tamaño de la figura
plt.plot(historial.history['loss'])
# Grafica la pérdida durante el entrenamiento
plt.title('Pérdida durante el entrenamiento')
# Establece el título del gráfico
plt.xlabel('Época')
# Etiqueta del eje x
plt.ylabel('Pérdida')
# Etiqueta del eje y
plt.show()
# Muestra el gráfico

# Evaluar el modelo en los datos de entrenamiento
perdida, precision = modelo.evaluate(X_datos, y_etiquetas)
# Evalúa el modelo en los datos de entrada y etiquetas
print(f'Precisión en los datos de entrenamiento: {precision:.2f}')
# Imprime la precisión del modelo
