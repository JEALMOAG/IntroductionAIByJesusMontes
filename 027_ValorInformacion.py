"""
created on 2 april 11:08:34 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código proporciona una estructura para modelar y tomar decisiones en un
contexto de incertidumbre utilizando la teoría de la utilidad esperada.
Se definen clases para representar eventos, decisiones y opciones, junto
con funciones para calcular la utilidad esperada de las opciones y el valor
de obtener información adicional antes de tomar una decisión.
El código permite calcular la utilidad esperada de diferentes opciones
y determinar si adquirir información adicional antes de decidir puede aumentar
el valor esperado de la decisión.

"""
class Suceso:  # Define una clase llamada Suceso para representar un suceso en el contexto de la toma de decisiones
    def __init__(self, probabilidad, resultado_bueno, resultado_malo):  # Define el método de inicialización con la probabilidad del suceso y sus resultados buenos y malos
        self.probabilidad = probabilidad  # Asigna la probabilidad del suceso al atributo probabilidad de la instancia
        self.resultado_bueno = resultado_bueno  # Asigna el resultado bueno al atributo resultado_bueno de la instancia
        self.resultado_malo = resultado_malo  # Asigna el resultado malo al atributo resultado_malo de la instancia

class Eleccion:  # Define una clase llamada Eleccion para representar una elección en el contexto de la toma de decisiones
    def __init__(self, nombre):  # Define el método de inicialización con el nombre de la elección
        self.nombre = nombre  # Asigna el nombre de la elección al atributo nombre de la instancia

class Alternativa:  # Define una clase llamada Alternativa para representar una alternativa en el contexto de la toma de decisiones
    def __init__(self, nombre, resultados):  # Define el método de inicialización con el nombre de la alternativa y sus resultados
        self.nombre = nombre  # Asigna el nombre de la alternativa al atributo nombre de la instancia
        self.resultados = resultados  # Asigna los resultados de la alternativa al atributo resultados de la instancia

def calcular_utilidad(alternativa, suceso_bueno, suceso_malo):  # Define una función para calcular la utilidad esperada de una alternativa dada un suceso bueno y uno malo
    utilidad = alternativa.resultados[0] * suceso_bueno.probabilidad + alternativa.resultados[1] * suceso_malo.probabilidad  # Calcula la utilidad esperada de la alternativa
    return utilidad  # Devuelve la utilidad esperada de la alternativa

def calcular_valor_informacion(alternativa_a, alternativa_b, suceso_bueno, suceso_malo, suceso_informacion):  # Define una función para calcular el valor de obtener información adicional antes de tomar una elección
    utilidad_sin_info = max(calcular_utilidad(alternativa_a, suceso_bueno, suceso_malo), calcular_utilidad(alternativa_b, suceso_bueno, suceso_malo))  # Calcula la utilidad esperada sin obtener información adicional

    utilidad_con_info = calcular_utilidad(alternativa_a, suceso_bueno, suceso_malo) * suceso_informacion.probabilidad \
                        + calcular_utilidad(alternativa_b, suceso_bueno, suceso_malo) * suceso_informacion.probabilidad  # Calcula la utilidad esperada con información adicional

    return utilidad_con_info - utilidad_sin_info  # Calcula y devuelve el valor de la información como la diferencia entre la utilidad con y sin información adicional

if __name__ == "__main__":  # Comprueba si el script se está ejecutando directamente
    # Definir sucesos
    suceso_bueno = Suceso(probabilidad=0.8, resultado_bueno=100, resultado_malo=0)  # Define un suceso bueno con su probabilidad y resultados buenos y malos
    suceso_malo = Suceso(probabilidad=0.2, resultado_bueno=20, resultado_malo=0)  # Define un suceso malo con su probabilidad y resultados buenos y malos
    suceso_informacion = Suceso(probabilidad=0.5, resultado_bueno=0, resultado_malo=0)  # Define un suceso de información adicional con su probabilidad y resultados buenos y malos

    # Definir alternativas
    alternativa_a = Alternativa(nombre="Alternativa A", resultados=(100, 0))  # Define la alternativa A con su nombre y resultados
    alternativa_b = Alternativa(nombre="Alternativa B", resultados=(50, 50))  # Define la alternativa B con su nombre y resultados

    # Calcular el valor de la información
    valor_informacion = calcular_valor_informacion(alternativa_a, alternativa_b, suceso_bueno, suceso_malo, suceso_informacion)  # Calcula el valor de obtener información adicional antes de tomar una elección

    print("El valor de obtener información adicional es:", valor_informacion)  # Imprime el valor de la información calculado
