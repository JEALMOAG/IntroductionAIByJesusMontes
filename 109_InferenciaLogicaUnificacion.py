"""
Created on 17 April  09:24:42 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código proporciona funciones para unificar términos y variables en lógica de
 primer orden. Utiliza un algoritmo de unificación para encontrar una sustitución 
 que haga que dos términos sean idénticos. Esto puede ser útil en sistemas de 
 inferencia, resolución de problemas y procesamiento del lenguaje natural.
'''
def unify_var(variable, valor, sustitucion):

    # Si la variable ya está en la sustitución, unifica su valor con el nuevo valor.
    if variable in sustitucion:
        return unify(sustitucion[variable], valor, sustitucion)
    # Si el nuevo valor ya está en la sustitución, unifica la variable con su valor.
    elif valor in sustitucion:
        return unify(variable, sustitucion[valor], sustitucion)
    # Si no se ha encontrado ninguna coincidencia, asigna el valor de valor a la variable en la sustitución.
    else:
        sustitucion[variable] = valor
        return sustitucion

def unify(termino1, termino2, sustitucion):

    # Si la sustitución es None, la unificación no es posible, devuelve None.
    if sustitucion is None:
        return None
    # Si los términos termino1 y termino2 son idénticos, no hay necesidad de hacer nada, devuelve la sustitución.
    elif termino1 == termino2:
        return sustitucion
    # Si termino1 es una variable, unifica termino1 con termino2 usando la función unify_var.
    elif isinstance(termino1, str) and termino1.islower():
        return unify_var(termino1, termino2, sustitucion)
    # Si termino2 es una variable, unifica termino2 con termino1 usando la función unify_var.
    elif isinstance(termino2, str) and termino2.islower():
        return unify_var(termino2, termino1, sustitucion)
    # Si ambos termino1 y termino2 son listas, unifica cada elemento correspondiente de termino1 y termino2 recursivamente.
    elif isinstance(termino1, list) and isinstance(termino2, list):
        if len(termino1) != len(termino2):  # Si las listas tienen longitudes diferentes, la unificación no es posible.
            return None
        else:
            for t1, t2 in zip(termino1, termino2):
                sustitucion = unify(t1, t2, sustitucion)  # Llama a unify recursivamente para cada par de elementos.
            return sustitucion
    # Si no se cumple ninguna de las condiciones anteriores, la unificación no es posible, devuelve None.
    else:
        return None

# Ejemplo de uso
term1 = ['X', 'a', 'b']
term2 = ['X', 'A', 'B']
sust = {}

resultado = unify(term1, term2, sust)
print(resultado)
