"""
created on 8 Abril 18:15:56 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código genera datos de ejemplo con dos clusters utilizando la función
make_blobs. Luego, inicializa y entrena un modelo de mezcla de Gaussianas
(Gaussian Mixture Model - GMM) con dos componentes utilizando el algoritmo
Expectation-Maximization (EM) a través de la clase GaussianMixture de
scikit-learn. Después de entrenar el modelo, predice a qué cluster pertenece
cada muestra en los datos de entrada y obtiene las medias y matrices de
covarianza de los clusters identificados. Finalmente, imprime las medias y
matrices de covarianza de los clusters.
"""
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# Genera datos de ejemplo con dos clusters
datos, _ = make_blobs(n_samples=1000, centers=2, cluster_std=1.5, random_state=42)
# La función make_blobs genera datos de puntos con clusters.

# Inicializa el modelo de mezcla de Gaussianas con dos componentes
modelo_gmm = GaussianMixture(n_components=2, random_state=42)
# Crea una instancia del modelo de mezcla de Gaussianas con 2 componentes.
# GaussianMixture es el estimador de scikit-learn que implementa el algoritmo EM para mezcla de Gaussianas.

# Entrena el modelo utilizando el algoritmo EM
modelo_gmm.fit(datos)
# Entrena el modelo de mezcla de Gaussianas utilizando los datos.

# Obtiene las etiquetas de cluster asignadas a cada muestra
etiquetas = modelo_gmm.predict(datos)
# Predice el cluster al que pertenece cada muestra en los datos.

# Obtiene las medias y matrices de covarianza de los clusters
medias = modelo_gmm.means_
covarianzas = modelo_gmm.covariances_
# Obtiene las medias y matrices de covarianza de los clusters identificados por el modelo.

print("Medias de los clusters:")
print(medias)
print("\nMatrices de covarianza de los clusters:")
print(covarianzas)
# Imprime las medias y matrices de covarianza de los clusters identificados por el modelo.
