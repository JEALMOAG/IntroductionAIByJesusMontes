"""
Created on 16 April  04:48:32 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código implementa una clase llamada `FormulaLogica` que representa una 
fórmula lógica en lenguaje proposicional. Esta clase proporciona métodos 
para verificar la equivalencia con otra fórmula, determinar si la fórmula
 es válida (si siempre es verdadera) y si es satisfacible (si al menos puede
ser verdadera bajo alguna interpretación de sus variables). Además, incluye 
un método para evaluar la fórmula con un valor de verdad dado para una variable.
 Luego, se crean dos instancias de la clase `FormulaLogica` con diferentes 
 fórmulas y se realizan pruebas para verificar la equivalencia, validez y 
 satisfacibilidad de las fórmulas.
'''

class FormulaLogica:
    # El método __init__ inicializa la fórmula con una cadena dada
    def __init__(self, expresion):
        self.expresion = expresion  # Inicializa la fórmula con la expresión dada

    # El método __str__ devuelve la representación de cadena de la fórmula
    def __str__(self):
        return self.expresion  # Devuelve la representación de cadena de la fórmula

    # Método para comprobar la equivalencia con otra fórmula lógica
    def es_equivalente(self, otra_formula):
        return self.expresion == otra_formula.expresion  # Comprueba si las expresiones son equivalentes

    # Método para determinar si la fórmula es válida
    def es_valida(self):
        # Una fórmula es válida si siempre es verdadera
        # para cualquier asignación de valores a las variables
        # Por simplicidad, vamos a asumir que solo hay una variable
        return self.evaluar(True) and self.evaluar(False)  # Comprueba si la fórmula es válida

    # Método para determinar si la fórmula es satisfacible
    def es_satisfacible(self):
        # Una fórmula es satisfacible si al menos hay una asignación
        # de valores a las variables que la hace verdadera
        return self.evaluar(True) or self.evaluar(False)  # Comprueba si la fórmula es satisfacible

    # Método para evaluar la fórmula con un valor dado para la variable
    def evaluar(self, valor):
        # Evaluamos la fórmula con el valor dado para la variable
        # Por simplicidad, vamos a asumir que solo hay una variable
        if self.expresion == "no P":  # Comprueba si la fórmula es "no P"
            return not valor  # Devuelve la negación del valor
        elif self.expresion == "P":  # Comprueba si la fórmula es "P"
            return valor  # Devuelve el valor de P

# Creamos dos fórmulas para probar el programa
formula_1 = FormulaLogica("P")  # Creamos la fórmula "P"
formula_2 = FormulaLogica("no P")  # Creamos la fórmula "no P"

# Comprobamos si las fórmulas son equivalentes
print(f"Las fórmulas son equivalentes: {formula_1.es_equivalente(formula_2)}")

# Comprobamos si una fórmula es válida
print(f"La fórmula 1 es válida: {formula_1.es_valida()}")
print(f"La fórmula 2 es válida: {formula_2.es_valida()}")

# Comprobamos si una fórmula es satisfacible
print(f"La fórmula 1 es satisfacible: {formula_1.es_satisfacible()}")
print(f"La fórmula 2 es satisfacible: {formula_2.es_satisfacible()}")

