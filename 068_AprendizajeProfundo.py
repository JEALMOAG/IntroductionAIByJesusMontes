"""
created on 9 Abril 15:57:34 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código define y entrena un modelo de red neuronal utilizando TensorFlow.
Se crea un modelo secuencial con capas densas y se compila con el optimizador
Adam y la función de pérdida de entropía cruzada binaria. Luego, se generan
datos de ejemplo y se entrena el modelo con ellos durante 10 épocas.
Finalmente, se evalúa el modelo y se imprime su precisión.
"""
import tensorflow as tf  # Importa la biblioteca TensorFlow y la renombra como tf
from tensorflow.keras import Secuencial  # Importa la clase Secuencial del módulo keras dentro de TensorFlow
from tensorflow.keras.layers import Densa  # Importa la capa Densa del módulo layers dentro de keras en TensorFlow

# Definición del modelo de red neuronal
red_neuronal = Secuencial([  # Crea un modelo secuencial de capas
    Densa(64, activation='relu', input_shape=(10,)),  # Agrega una capa densa con 64 unidades y función de activación ReLU como la primera capa con entrada de forma (10,)
    Densa(64, activation='relu'),  # Agrega una segunda capa densa con 64 unidades y función de activación ReLU
    Densa(1, activation='sigmoid')  # Agrega una capa densa con 1 unidad y función de activación sigmoide
])

# Compilación del modelo
red_neuronal.compile(optimizer='adam',  # Compila el modelo con el optimizador Adam
               loss='binary_crossentropy',  # Usa la función de pérdida binary_crossentropy
               metrics=['accuracy'])  # Utiliza la métrica de precisión (accuracy)

# Datos de ejemplo
X_entrenamiento = tf.random.normal(shape=(1000, 10))  # Genera datos de entrada de forma aleatoria con distribución normal
y_entrenamiento = tf.random.uniform(shape=(1000, 1), minval=0, maxval=2, dtype=tf.int32)  # Genera etiquetas de forma aleatoria con distribución uniforme

# Entrenamiento del modelo
red_neuronal.fit(X_entrenamiento, y_entrenamiento, épocas=10, tamaño_lote=32)  # Entrena el modelo durante 10 épocas con un tamaño de lote de 32

# Evaluación del modelo
pérdida, precisión = red_neuronal.evaluate(X_entrenamiento, y_entrenamiento)  # Evalúa el modelo con los datos de entrenamiento
print("Precisión del modelo:", precisión)  # Imprime la precisión del modelo
