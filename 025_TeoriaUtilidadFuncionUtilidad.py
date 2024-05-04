"""
created on 1 april 22:13:21 2024
@author: Jesus Alejandro Montes Aguila
"""
"""
El código define una clase FuncionUtilidadLineal que calcula la utilidad lineal dada una cantidad y
una función de utilidad lineal con un coeficiente y un corte. Además,
proporciona una función tomar_decision que elige la mejor opción basada
en la función de utilidad lineal dada un conjunto de opciones con cantidades
asociadas. El ejemplo de uso crea una instancia de la función de utilidad
lineal, define un conjunto de opciones y determina la mejor opción basada en
la utilidad calculada.
"""
class FuncionUtilidadLineal:  # Define una clase llamada FuncionUtilidadLineal
    def __init__(self, coeficiente, corte):  # Define el método de inicialización con coeficiente e intersección
        self.coeficiente = coeficiente  # Asigna el valor de coeficiente al atributo coeficiente de la instancia
        self.corte = corte  # Asigna el valor de corte al atributo corte de la instancia

    def calcular_utilidad(self, cantidad):  # Define un método para calcular la utilidad
        return self.coeficiente * cantidad + self.corte  # Calcula la utilidad lineal

def tomar_decision(funcion_utilidad, opciones):  # Define una función para tomar decisiones
    mejor_opcion = None  # Inicializa la mejor opción como nula
    mejor_utilidad = float('-inf')  # Inicializa la mejor utilidad como negativa infinita
    for opcion, cantidad in opciones.items():  # Itera sobre las opciones y cantidades proporcionadas
        utilidad_opcion = funcion_utilidad.calcular_utilidad(cantidad)  # Calcula la utilidad de la opción actual
        if utilidad_opcion > mejor_utilidad:  # Comprueba si la utilidad actual es mejor que la mejor utilidad encontrada hasta ahora
            mejor_opcion = opcion  # Actualiza la mejor opción
            mejor_utilidad = utilidad_opcion  # Actualiza la mejor utilidad
    return mejor_opcion  # Devuelve la mejor opción encontrada

# Ejemplo de uso:
if __name__ == "__main__":  # Comprueba si el script se está ejecutando directamente
    funcion_utilidad = FuncionUtilidadLineal(coeficiente=0.5, corte=0)  # Creamos una función de utilidad lineal
    opciones = {"Opción A": 10, "Opción B": 20, "Opción C": 15}  # Definimos las opciones y sus cantidades asociadas
    mejor_opcion = tomar_decision(funcion_utilidad, opciones)  # Tomamos la decisión basada en la función de utilidad
    print("La mejor opción es:", mejor_opcion)  # Imprime la mejor opción encontrada
