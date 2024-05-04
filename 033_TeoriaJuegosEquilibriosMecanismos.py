"""
created on 3 april 17:22:35 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa el "dilema del prisionero", un escenario de teoría
de juegos donde dos jugadores deben decidir entre cooperar o traicionar.
Cada jugador elige su acción y, según las elecciones de ambos, se determinan
las recompensas para cada uno. El código solicita las decisiones de los
jugadores, calcula las recompensas según las elecciones y muestra los resultados
"""
def dilema_del_prisionero(jugador_uno, jugador_dos):
    # Diccionario que mapea las combinaciones de elecciones a las recompensas
    recompensas = {
        ("cooperar", "cooperar"): (3, 3),        # Ambos cooperan, ambos reciben una recompensa alta
        ("cooperar", "traicionar"): (0, 5),      # Jugador 1 coopera, Jugador 2 traiciona, Jugador 1 recibe la peor recompensa y Jugador 2 la mejor
        ("traicionar", "cooperar"): (5, 0),      # Jugador 1 traiciona, Jugador 2 coopera, Jugador 1 recibe la mejor recompensa y Jugador 2 la peor
        ("traicionar", "traicionar"): (1, 1)    # Ambos traicionan, ambos reciben una recompensa baja
    }
    # Obtener las recompensas para las elecciones dadas
    recompensa_jugador_uno, recompensa_jugador_dos = recompensas[(jugador_uno, jugador_dos)]
    return recompensa_jugador_uno, recompensa_jugador_dos

# Función principal del programa
def principal():
    print("Bienvenido al dilema del prisionero.")
    print("Jugador 1, ¿cooperar (c) o traicionar (t)?")
    eleccion_jugador_uno = input().strip().lower()   # Obtener la elección del jugador 1 y limpiarla
    print("Jugador 2, ¿cooperar (c) o traicionar (t)?")
    eleccion_jugador_dos = input().strip().lower()   # Obtener la elección del jugador 2 y limpiarla

    # Validar las elecciones de los jugadores
    if eleccion_jugador_uno not in ["c", "t"] or eleccion_jugador_dos not in ["c", "t"]:
        print("Por favor, introduce 'c' para cooperar o 't' para traicionar.")
        return

    # Convertir las elecciones a texto para una mejor legibilidad
    if eleccion_jugador_uno == "c":
        eleccion_jugador_uno_texto = "cooperar"
    else:
        eleccion_jugador_uno_texto = "traicionar"

    if eleccion_jugador_dos == "c":
        eleccion_jugador_dos_texto = "cooperar"
    else:
        eleccion_jugador_dos_texto = "traicionar"

    # Llamar a la función que simula el juego y obtener las recompensas
    recompensa_jugador_uno, recompensa_jugador_dos = dilema_del_prisionero(eleccion_jugador_uno_texto, eleccion_jugador_dos_texto)
    # Mostrar las recompensas para cada jugador
    print(f"Jugador 1 obtiene {recompensa_jugador_uno} puntos.")
    print(f"Jugador 2 obtiene {recompensa_jugador_dos} puntos.")

# Verificar si el script se está ejecutando directamente y llamar a la función principal
if __name__ == "__main__":
    principal()
