"""
created on 5 april 13:46:06 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código simula el lanzamiento de dos monedas y calcula la probabilidad de que
ambas monedas muestren "Cara". Primero, define una función para lanzar una
moneda y otra función para realizar el experimento de lanzar dos monedas.
Luego, realiza un número especificado de experimentos y cuenta los casos en
los que ambas monedas muestran "Cara". Finalmente, calcula la probabilidad de
que ambas monedas muestren "Cara" y la imprime.
"""
import numpy as np
# Importa la biblioteca numpy para generar números aleatorios

def lanzar_moneda():
    # Simula el lanzamiento de una moneda. Devuelve 'Cara' o 'Cruz'.
    resultado = np.random.choice(['Cara', 'Cruz'])  # Selecciona aleatoriamente entre 'Cara' y 'Cruz'
    return resultado

def realizar_experimento():
    # Simula el experimento de lanzar dos monedas y verifica si los resultados son independientes.
    moneda1 = lanzar_moneda()  # Lanza la primera moneda
    moneda2 = lanzar_moneda()  # Lanza la segunda moneda

    return moneda1, moneda2  # Devuelve los resultados de los lanzamientos de las dos monedas

def calcular_probabilidad_independencia(n_experimentos):
    # Realiza n_experimentos y cuenta los casos donde los resultados son independientes.
    independientes = 0  # Inicializa el contador para contar los casos donde ambas monedas muestran 'Cara'
    for _ in range(n_experimentos):  # Realiza un número de experimentos dado
        resultado1, resultado2 = realizar_experimento()  # Realiza un experimento de lanzar dos monedas
        if resultado1 == 'Cara' and resultado2 == 'Cara':  # Verifica si ambas monedas muestran 'Cara'
            independientes += 1  # Incrementa el contador si ambas monedas muestran 'Cara'

    probabilidad_independencia = independientes / n_experimentos  # Calcula la probabilidad de independencia condicional
    return probabilidad_independencia

def main():
    n_experimentos = 10000  # Número de experimentos a realizar
    probabilidad_independencia = calcular_probabilidad_independencia(n_experimentos)  # Calcula la probabilidad de independencia condicional

    print("Probabilidad de obtener cara en ambas monedas (Independencia Condicional):", probabilidad_independencia)  # Imprime la probabilidad de independencia condicional

if __name__ == "__main__":
    main()
