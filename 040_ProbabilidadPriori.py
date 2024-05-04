"""
created on 4 april 20:56:06 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código calcula la probabilidad a priori de obtener un número par al lanzar
un dado. Utiliza una función para calcular esta probabilidad dividiendo el
número de eventos de interés por el tamaño del espacio muestral. Luego,
en la función principal, se aplica esta función al evento de obtener un número
par y se imprime el resultado.
"""
def probabilidad_a_priori(evento, espacio_muestral):
    # Calcula la probabilidad a priori de un evento dado el espacio muestral.
    conteo_evento = sum(1 for e in espacio_muestral if e in evento)
    return conteo_evento / len(espacio_muestral)

def main():
    # Espacio muestral de lanzar un dado
    muestra_espacial = [1, 2, 3, 4, 5, 6]

    # Evento de interés: obtener un número par
    evento_par = [2, 4, 6]

    # Calcula la probabilidad a priori del evento de obtener un número par
    p_a_priori_par = probabilidad_a_priori(evento_par, muestra_espacial)

    # Imprime el resultado
    print("Probabilidad a priori de obtener un número par:", p_a_priori_par)

if __name__ == "__main__":
    main()
