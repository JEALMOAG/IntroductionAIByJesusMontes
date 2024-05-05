"""
created on 11 Abril 23:45:12 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código utiliza NLTK para construir un modelo de lenguaje basado en trigramas
a partir del corpus "Sentido y sensibilidad" de Jane Austen.
Luego, este modelo se utiliza para predecir la siguiente palabra en una oración
dada las dos palabras anteriores. Esto se logra mediante el uso de un
diccionario para almacenar las frecuencias de los trigramas y luego normalizando
estas frecuencias. Finalmente, se implementa una función para predecir la
siguiente palabra en función de las dos palabras anteriores, y se genera una
oración aleatoria utilizando este modelo.
"""
# Importar las bibliotecas necesarias
import nltk  # Importar la biblioteca NLTK (Natural Language Toolkit)
from nltk.util import ngrams  # Importar la función ngrams de NLTK para dividir el texto en n-gramas
from collections import defaultdict  # Importar la clase defaultdict del módulo collections para crear diccionarios predeterminados
import random  # Importar el módulo random para generar números aleatorios

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')  # Descargar el tokenizador de NLTK
nltk.download('gutenberg')  # Descargar el corpus Gutenberg de NLTK (que contiene libros de dominio público)
nltk.download('averaged_perceptron_tagger')  # Descargar el etiquetador de NLTK

# Cargar un corpus de ejemplo (Gutenberg Corpus)
corpus = nltk.corpus.gutenberg.sents('austen-sense.txt')  # Cargar las oraciones del libro "Sentido y sensibilidad" de Jane Austen

# Crear un modelo de lenguaje basado en trigramas
modelo = defaultdict(lambda: defaultdict(lambda: 0))  # Crear un diccionario predeterminado anidado para almacenar las frecuencias de los trigramas

# Iterar sobre cada oración en el corpus y construir el modelo de trigramas
for oracion in corpus:
    trigramas = ngrams(oracion, 3, pad_left=True, pad_right=True)  # Dividir cada oración en trigramas
    for w1, w2, w3 in trigramas:  # Iterar sobre los trigramas
        modelo[(w1, w2)][w3] += 1  # Incrementar la frecuencia del siguiente palabra en el trigramas actual

# Normalizar las frecuencias
for w1_w2 in modelo:  # Iterar sobre cada par de palabras
    total_ocurrencias = float(sum(modelo[w1_w2].values()))  # Calcular el número total de ocurrencias de las palabras siguientes
    for w3 in modelo[w1_w2]:  # Iterar sobre las palabras siguientes
        modelo[w1_w2][w3] /= total_ocurrencias  # Normalizar las frecuencias dividiendo por el total de ocurrencias

# Función para predecir la siguiente palabra
def predecir_palabra_siguiente(palabra1, palabra2):
    probabilidades_palabra_siguiente = modelo[(palabra1, palabra2)]  # Obtener las probabilidades de las palabras siguientes dado el par de palabras actual
    if not probabilidades_palabra_siguiente:  # Verificar si no hay palabras siguientes
        return None  # Devolver None si no hay palabras siguientes en el modelo
    palabras_siguientes, probabilidades = zip(*probabilidades_palabra_siguiente.items())  # Separar las palabras siguientes y sus probabilidades
    return random.choices(palabras_siguientes, probabilidades)[0]  # Devolver una palabra siguiente seleccionada aleatoriamente según sus probabilidades

# Ejemplo de uso
palabras_actuales = ('Es', 'un')  # Definir las palabras iniciales
for _ in range(10):  # Generar 10 palabras más
    palabra_siguiente = predecir_palabra_siguiente(*palabras_actuales)  # Predecir la siguiente palabra dado el par de palabras actuales
    if palabra_siguiente is None:  # Verificar si no hay palabra siguiente
        break  # Salir del bucle si no hay palabra siguiente
    print(palabra_siguiente, end=' ')  # Imprimir la palabra siguiente
    palabras_actuales = (palabras_actuales[1], palabra_siguiente)  # Actualizar el par de palabras actuales para la siguiente iteración
