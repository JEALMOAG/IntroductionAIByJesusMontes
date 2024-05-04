"""
created on 4 april 15:23:17 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código simula el lanzamiento de una moneda y calcula la probabilidad
de obtener un resultado deseado, como "Cara" o "Cruz", después de un número
especificado de lanzamientos. Utiliza una función para simular el lanzamiento
de la moneda y otra función para calcular la probabilidad de obtener el
resultado deseado en base a un número de lanzamientos dado. Finalmente,
imprime la probabilidad calculada.
"""
import random

def lanzamiento_moneda():
    # Simula el lanzamiento de una moneda.
    # Devuelve 'Cara' o 'Cruz'.
    resultado_lanzamiento = random.choice(['Cara', 'Cruz'])
    return resultado_lanzamiento

def calcular_probabilidad(num_lanzamientos, resultado_deseado):
    # Realiza num_lanzamientos y calcula la probabilidad de obtener el resultado deseado.
    conteo_resultado_deseado = 0
    for _ in range(num_lanzamientos):
        resultado = lanzamiento_moneda()
        if resultado == resultado_deseado:
            conteo_resultado_deseado += 1
    
    probabilidad = conteo_resultado_deseado / num_lanzamientos
    return probabilidad

# Parámetros del juego
num_lanzamientos = 1000
resultado_deseado = 'Cara'

# Calcula la probabilidad de obtener 'Cara' en num_lanzamientos
probabilidad_cara = calcular_probabilidad(num_lanzamientos, resultado_deseado)

# Imprime el resultado
print(f"Después de {num_lanzamientos} lanzamientos, la probabilidad de obtener '{resultado_deseado}' es: {probabilidad_cara}")
