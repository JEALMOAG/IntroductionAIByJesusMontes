"""
created on 6 april 06:35:46 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código simula la predicción del clima utilizando una cadena de Markov.
Utiliza una matriz de transición para modelar las probabilidades de transición
entre diferentes condiciones climáticas (soleado, nublado, lluvioso).
La función predecir_clima_actual selecciona la condición climática futura
basada en la matriz de transición y la condición actual. El programa imprime
la condición climática actual y predice las condiciones climáticas para los
próximos 5 días.
"""
import numpy as np

# Definimos la matriz de transición de condiciones climáticas
matriz_climatica = np.array([[0.8, 0.1, 0.1],  # Soleado -> Soleado, Nublado, Lluvioso
                              [0.2, 0.6, 0.2],  # Nublado -> Soleado, Nublado, Lluvioso
                              [0.3, 0.3, 0.4]]) # Lluvioso -> Soleado, Nublado, Lluvioso

# Definimos las condiciones climáticas
condiciones_climaticas = ['Soleado', 'Nublado', 'Lluvioso']

# Función para predecir la condición climática actual
def predecir_clima_actual(condicion_actual):
    clima_futuro = np.random.choice(condiciones_climaticas, p=matriz_climatica[condicion_actual])
    return clima_futuro

def main():
    # Definimos la condición climática actual
    condicion_actual = np.random.randint(0, 3)  # Seleccionamos una condición inicial aleatoria
    
    # Imprimimos la condición climática actual
    print("Condición climática actual:", condiciones_climaticas[condicion_actual])
    
    # Predecimos y mostramos el clima futuro para los próximos 5 días
    for i in range(1, 6):
        print(f"Día {i}: {predecir_clima_actual(condicion_actual)}")
        condicion_actual = condiciones_climaticas.index(predecir_clima_actual(condicion_actual))

if __name__ == "__main__":
    main()
