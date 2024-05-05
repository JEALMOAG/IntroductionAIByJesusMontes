"""
Created on 29 march 17:48:11 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este código simula una búsqueda en línea de una calificación específica en el
 contexto de un salón de clases en el Centro de Estudios Tecnológicos Industrial
 y de Servicios (CETI). El objetivo es encontrar una calificación particular
 dentro de un número máximo de intentos, generando calificaciones aleatorias
 en cada intento y verificando si coinciden con la calificación buscada.
 Si se encuentra la calificación objetivo, el programa muestra un mensaje
 de éxito junto con el número de intentos realizados; de lo contrario, muestra
 un mensaje indicando que la calificación no fue encontrada después de los 
 intentos máximos permitidos.
'''

import random  # Importa el módulo random para generar números aleatorios

# Definición de la función objetivo (en este caso, buscamos el número objetivo)
def funcion_objetivo(numero_buscar, numero_aleatorio):
    if numero_aleatorio == numero_buscar:  # Comprueba si el número aleatorio es igual al número objetivo
        return True  # Devuelve True si el número aleatorio es igual al número objetivo
    else:
        return False  # Devuelve False si el número aleatorio no es igual al número objetivo

# Implementación de la Búsqueda Online
def busqueda_online(numero_buscar, max_intentos):
    intentos = 0  # Inicializa el contador de intentos en 0
    encontrado = False  # Inicializa la variable encontrado como False
    
    # Mientras los intentos sean menores al máximo y no se haya encontrado el número objetivo
    while intentos < max_intentos and not encontrado:
        # Genera un número aleatorio como supuesta solución
        numero_aleatorio = random.randint(1, 30)  # Genera un número aleatorio entre 1 y 30
        
        # Evalúa si la supuesta solución es la solución correcta llamando a la función objetivo
        encontrado = funcion_objetivo(numero_buscar, numero_aleatorio)
        
        # Incrementa el contador de intentos
        intentos += 1
    
    return encontrado, intentos  # Devuelve True si se encontró el número objetivo y el número de intentos realizados

# Parámetros
numero_a_buscar = 5  # Define el número a buscar
max_intentos = 20  # Define el número máximo de intentos

# Ejecución de la búsqueda online
resultado, intentos_realizados = busqueda_online(numero_a_buscar, max_intentos)

# Imprime el resultado
if resultado:
    print(f"¡El número {numero_a_buscar} fue encontrado en {intentos_realizados} intentos!")  # Imprime un mensaje de éxito si se encontró el número objetivo
else:
    print(f"El número {numero_a_buscar} no fue encontrado después de {intentos_realizados} intentos.")  # Imprime un mensaje indicando que el número objetivo no fue encontrado después de los intentos máximos permitidos
