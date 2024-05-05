"""
created on 8 Abril 15:34:08 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código utiliza el conjunto de datos Iris para entrenar un clasificador
Naïve Bayes Gaussiano y evaluar su precisión. Primero, divide los datos en
conjuntos de entrenamiento y prueba. Luego, entrena el clasificador con los
datos de entrenamiento y realiza predicciones en el conjunto de prueba.
Finalmente, calcula la precisión del modelo comparando las etiquetas reales
con las predicciones y la imprime.
"""
from sklearn.datasets import load_iris  # Importa la función para cargar el conjunto de datos Iris
from sklearn.model_selection import train_test_split  # Importa la función para dividir el conjunto de datos en entrenamiento y prueba
from sklearn.naive_bayes import GaussianNB  # Importa el clasificador Naïve Bayes Gaussiano
from sklearn.metrics import accuracy_score  # Importa la función para calcular la precisión del modelo

# Cargar el conjunto de datos Iris
iris = load_iris()  # Carga el conjunto de datos Iris

X = iris.data  # Características (longitud y ancho del sépalo y del pétalo)
y = iris.target  # Etiquetas (especies de iris)

# Dividir el conjunto de datos en entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)
# Divide aleatoriamente el conjunto de datos en conjuntos de entrenamiento y prueba,
# reservando el 20% de los datos para pruebas y utilizando una semilla aleatoria para reproducibilidad

# Crear un clasificador Naïve Bayes Gaussiano
bayesiano_ingenuo = GaussianNB()  # Crea una instancia del clasificador Naïve Bayes Gaussiano

# Entrenar el clasificador
bayesiano_ingenuo.fit(X_entrenamiento, y_entrenamiento)  # Entrena el clasificador con los datos de entrenamiento

# Realizar predicciones en el conjunto de prueba
predicciones = bayesiano_ingenuo.predict(X_prueba)  # Realiza predicciones utilizando el conjunto de prueba

# Calcular la precisión
precision = accuracy_score(y_prueba, predicciones)  # Calcula la precisión comparando las etiquetas verdaderas con las predicciones
print("Precisión:", precision)  # Imprime la precisión del modelo
