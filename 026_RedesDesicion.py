"""
created on 2 April 09:31:06 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código proporciona clases y funciones para modelar y tomar decisiones en una
red de decisión. Utiliza las clases Suceso, Eleccion, y Alternativa para
representar eventos, decisiones, y opciones respectivamente.
La función calcular_ganancia calcula la ganancia esperada de una alternativa
basada en eventos buenos y malos, y tomar_decision selecciona la mejor
alternativa entre dos basada en la ganancia esperada. Finalmente,
en el ejemplo de uso, se crean sucesos y alternativas, y se toma una decisión
entre dos alternativas....
"""
class Suceso:  # Define una clase llamada Suceso para representar un suceso en la red de decisión
    def __init__(self, probabilidad, buen_resultado, mal_resultado):  # Define el método de inicialización con probabilidad y resultados buenos y malos
        self.probabilidad = probabilidad  # Asigna la probabilidad del suceso al atributo probabilidad de la instancia
        self.buen_resultado = buen_resultado  # Asigna el resultado bueno al atributo buen_resultado de la instancia
        self.mal_resultado = mal_resultado  # Asigna el resultado malo al atributo mal_resultado de la instancia

class Eleccion:  # Define una clase llamada Eleccion para representar una elección en la red de decisión
    def __init__(self, nombre):  # Define el método de inicialización con el nombre de la elección
        self.nombre = nombre  # Asigna el nombre de la elección al atributo nombre de la instancia

class Alternativa:  # Define una clase llamada Alternativa para representar una alternativa en la red de decisión
    def __init__(self, nombre, resultados):  # Define el método de inicialización con el nombre de la alternativa y sus resultados
        self.nombre = nombre  # Asigna el nombre de la alternativa al atributo nombre de la instancia
        self.resultados = resultados  # Asigna los resultados de la alternativa al atributo resultados de la instancia

def calcular_ganancia(alternativa, suceso_bueno, suceso_malo):  # Define una función para calcular la ganancia esperada de una alternativa
    ganancia = alternativa.resultados[0] * suceso_bueno.probabilidad + alternativa.resultados[1] * suceso_malo.probabilidad  # Calcula la ganancia esperada
    return ganancia  # Devuelve la ganancia esperada de la alternativa

def tomar_decision(alternativa_a, alternativa_b, suceso_bueno, suceso_malo):  # Define una función para tomar una decisión entre dos alternativas
    ganancia_alternativa_a = calcular_ganancia(alternativa_a, suceso_bueno, suceso_malo)  # Calcula la ganancia esperada de la alternativa A
    ganancia_alternativa_b = calcular_ganancia(alternativa_b, suceso_bueno, suceso_malo)  # Calcula la ganancia esperada de la alternativa B

    if ganancia_alternativa_a > ganancia_alternativa_b:  # Comprueba si la ganancia esperada de la alternativa A es mayor que la de la alternativa B
        return alternativa_a.nombre  # Devuelve el nombre de la alternativa A como la mejor alternativa
    elif ganancia_alternativa_b > ganancia_alternativa_a:  # Comprueba si la ganancia esperada de la alternativa B es mayor que la de la alternativa A
        return alternativa_b.nombre  # Devuelve el nombre de la alternativa B como la mejor alternativa
    else:  # Si las ganancias esperadas son iguales
        return "Ambas alternativas tienen la misma ganancia esperada."  # Devuelve un mensaje indicando que ambas alternativas son igualmente buenas

if __name__ == "__main__":  # Comprueba si el script se está ejecutando directamente
    # Definir sucesos
    suceso_bueno = Suceso(probabilidad=0.8, buen_resultado=100, mal_resultado=0)  # Crea un suceso bueno con probabilidad 0.8 y resultados buenos y malos
    suceso_malo = Suceso(probabilidad=0.2, buen_resultado=20, mal_resultado=0)  # Crea un suceso malo con probabilidad 0.2 y resultados buenos y malos

    # Definir alternativas
    alternativa_a = Alternativa(nombre="Alternativa A", resultados=(100, 0))  # Crea la alternativa A con nombre y resultados
    alternativa_b = Alternativa(nombre="Alternativa B", resultados=(50, 50))  # Crea la alternativa B con nombre y resultados

    # Tomar decisión
    decision = tomar_decision(alternativa_a, alternativa_b, suceso_bueno, suceso_malo)  # Llama a la función para tomar una decisión entre las alternativas
    print("La mejor alternativa es:", decision)  # Imprime la mejor alternativa encontrada
