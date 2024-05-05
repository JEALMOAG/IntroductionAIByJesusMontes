"""
created on 8 Abril 23:22:46 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código utiliza un modelo de HMM (Modelo Oculto de Markov) para predecir
estados ocultos y observaciones futuras en una secuencia de datos.
Se define un modelo HMM con una matriz de covarianza diagonal y dos estados
ocultos. Luego, se entrena el modelo con una secuencia de observaciones y se
realizan predicciones sobre los estados ocultos y las observaciones futuras.
Los resultados de las predicciones se imprimen al final..
"""
import numpy as np
from hmmlearn import hmm

# Definición del modelo HMM con matriz de covarianza diagonal y 2 estados ocultos
modelo_HMM = hmm.GaussianHMM(n_componentes=2, tipo_covarianza="diag")
# Creamos una instancia del modelo HMM utilizando la clase GaussianHMM de la biblioteca hmmlearn.
# Especificamos que queremos utilizar una matriz de covarianza diagonal con tipo_covarianza="diag".
# También especificamos que queremos 2 estados ocultos con n_componentes=2.

# Datos de entrada (secuencia de observaciones)
secuencia_observaciones = np.array([[1.0], [2.0], [3.0], [4.0], [5.0]])
# Creamos un arreglo numpy que contiene una secuencia de observaciones.
# Cada observación es un arreglo de una dimensión (un escalar) y representa un punto en nuestra secuencia de datos.

# Entrenamiento del modelo HMM
modelo_HMM.fit(secuencia_observaciones)
# Entrenamos el modelo HMM utilizando el método fit().
# Pasamos nuestra secuencia de observaciones como argumento para entrenar el modelo.

# Predicción del estado oculto y las observaciones
estados_ocultos_predichos = modelo_HMM.predict(secuencia_observaciones)
# Utilizamos el método predict() para predecir los estados ocultos correspondientes a la secuencia de observaciones.

observaciones_predichas, _ = modelo_HMM.sample(len(secuencia_observaciones))
# Utilizamos el método sample() para generar nuevas observaciones a partir del modelo entrenado.
# En este caso, generamos el mismo número de observaciones que el tamaño de nuestra secuencia original.

# Resultados
print("Estados ocultos predichos:", estados_ocultos_predichos)
print("Observaciones predichas:", observaciones_predichas)
# Imprimimos los estados ocultos y las observaciones predichas por el modelo.




