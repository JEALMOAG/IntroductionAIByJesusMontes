"""
created on 10 Abril 19:23:00 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
Este código implementa un mapa autoorganizado de Kohonen (SOM) utilizando la
biblioteca MiniSom. Primero, se definen datos de ejemplo en 4 dimensiones.
Luego, se entrena el SOM con estos datos utilizando la función train_random
durante 1000 iteraciones. Se visualiza el SOM con un mapa de calor de las
neuronas y se proyectan los datos en el SOM, etiquetando cada neurona con el
índice del dato ganador más cercano.
"""
import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas
from minisom import MiniSom  # Importa MiniSom, una biblioteca para implementar SOM
import matplotlib.pyplot as plt  # Importa matplotlib para visualización
from matplotlib.gridspec import GridSpec  # Importa GridSpec para manejar la disposición de subtramas

# Datos de ejemplo (4 dimensiones)
datos = np.array([[0.2, 0.8, 0.1, 0.5],
                  [0.6, 0.3, 0.9, 0.2],
                  [0.5, 0.7, 0.3, 0.8],
                  [0.1, 0.4, 0.7, 0.3],
                  [0.9, 0.2, 0.5, 0.6],
                  [0.3, 0.6, 0.4, 0.7]])

# Tamaño del SOM
filas_som = 10  # Número de filas en el SOM
columnas_som = 10  # Número de columnas en el SOM

# Entrenamiento del SOM
som = MiniSom(filas_som, columnas_som, datos.shape[1], sigma=1.0, learning_rate=0.5)  # Crea una instancia de MiniSom
som.train_random(datos, 1000)  # Entrenamiento con 1000 iteraciones

# Mapa de calor de las neuronas
plt.figure(figsize=(12, 10))  # Crea una figura con el tamaño especificado
plt.pcolor(som.distance_map().T, cmap='bone_r')  # Plot de la distancia de cada neurona a sus vecinas
plt.colorbar()  # Agrega una barra de color para mostrar la escala de colores

# Plot de los datos en el SOM
plt.figure(figsize=(12, 10))  # Crea una nueva figura con el tamaño especificado
for i, d in enumerate(datos):  # Itera sobre los datos de entrada
    posicion_ganadora = som.winner(d)  # Encuentra la posición ganadora para el dato actual
    plt.text(posicion_ganadora[0]+0.5, posicion_ganadora[1]+0.5, str(i),
             color='k', fontdict={'weight': 'bold', 'size': 11})  # Etiqueta la posición ganadora con el índice del dato

plt.axis([0, filas_som, 0, columnas_som])  # Establece los límites del eje x e y
plt.gca().invert_yaxis()  # Invierte el eje y para que la numeración comience desde arriba
plt.title('Mapa Autoorganizado de Kohonen')  # Establece el título del gráfico
plt.show()  # Muestra el gráfico
