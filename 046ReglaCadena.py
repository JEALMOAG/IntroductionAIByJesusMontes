"""
created on 5 april 20:45:34 2024
@author:Jesus Alejandro Montes Aguila
"""
"""

El código calcula la probabilidad conjunta de tres eventos, A, B y C, utilizando
la regla de la cadena de probabilidad condicional.
La función probabilidad_conjunta toma las probabilidades individuales de los
eventos A, B dado A y C dado B, y calcula la probabilidad conjunta de C dado A.
Luego, imprime el resultado.
"""
def probabilidad_conjunta(probabilidad_A, probabilidad_B_dado_A, probabilidad_C_dado_B):
    """
    Calcula la probabilidad conjunta de los eventos A, B y C utilizando la regla de la cadena.
    """
    probabilidad_B = probabilidad_B_dado_A * probabilidad_A  # P(B) = P(B|A) * P(A)
    probabilidad_C = probabilidad_C_dado_B * probabilidad_B  # P(C) = P(C|B) * P(B)
    return probabilidad_C

# Probabilidad de los eventos individuales
probabilidad_A = 0.5
probabilidad_B_dado_A = 0.7
probabilidad_C_dado_B = 0.4

# Calculamos la probabilidad conjunta de los eventos A, B y C
probabilidad_conjunta = probabilidad_conjunta(probabilidad_A, probabilidad_B_dado_A, probabilidad_C_dado_B)

print("La probabilidad conjunta de los eventos A, B y C es:", probabilidad_conjunta)
