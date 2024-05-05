"""
created on 11 Abril 18:51:23 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código utiliza la biblioteca NLTK (Natural Language Toolkit) para analizar
sintácticamente una oración dada utilizando una gramática probabilística.
Primero, define una gramática probabilística de contexto libre (PCFG) que
describe las reglas de producción y las probabilidades asociadas con la
gramática del lenguaje. Luego, utiliza un parser Viterbi para generar árboles
de análisis sintáctico posibles para la oración proporcionada.
Finalmente, imprime los árboles de análisis sintáctico generados para la
oración dada.
"""
import nltk
from nltk import GramaticaPCFG
from nltk import ParserViterbi

# Definir una gramática probabilística
gramatica_pcfg = GramaticaPCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.7] | VP PP [0.3]
    PP -> P NP [1.0]
    V -> "vio" [0.4] | "comió" [0.6]
    NP -> "Juan" [0.2] | "María" [0.3] | "Bob" [0.5]
    P -> "con" [1.0]
""")

# Crear un parser Viterbi con la gramática
parser = ParserViterbi(gramatica_pcfg)

# Ejemplo de una oración para analizar
oracion = "Juan vio Bob con María"

# Tokenizar la oración
tokens = nltk.word_tokenize(oracion)

# Realizar el análisis sintáctico
arboles = parser.parse(tokens)

# Imprimir los árboles de análisis sintáctico posibles
for arbol in arboles:
    print(arbol)
