"""
created on 5 april 15:34:11 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código simula un problema de probabilidad utilizando la regla de Bayes para
calcular la probabilidad de que una bola de cierto color provenga de una de
dos urnas. Se definen probabilidades a priori para cada urna y probabilidades
condicionales de obtener un color dado el contenido de cada urna. Luego,
se implementa una función para calcular la probabilidad utilizando la regla
de Bayes, considerando la urna seleccionada y el color elegido. Finalmente,
se imprime la probabilidad calculada para el caso específico del color verde
y la urna 1.
"""
# Definimos las probabilidades a priori
prob_urna_uno = 0.5
prob_urna_dos = 0.5

# Definimos las probabilidades condicionales: P(Color | Urna)
prob_color_dado_urna_uno = {'rojo': 0.2, 'verde': 0.4, 'azul': 0.4}
prob_color_dado_urna_dos = {'rojo': 0.5, 'verde': 0.3, 'azul': 0.2}

# Función para calcular la probabilidad usando la regla de Bayes
def calcular_probabilidad_bayes(color, urna):
    # Verificamos la urna seleccionada y obtenemos la probabilidad condicional correspondiente
    if urna == 1:
        prob_color_dado_urna = prob_color_dado_urna_uno[color]
        prob_urna = prob_urna_uno
    else:
        prob_color_dado_urna = prob_color_dado_urna_dos[color]
        prob_urna = prob_urna_dos
    
    # Aplicamos la regla de Bayes para calcular la probabilidad de que la bola sea de ese color y de esa urna
    prob_color = prob_color_dado_urna * prob_urna
    return prob_color

def main():
    color_elegido = 'verde'  # Color elegido
    urna_elegida = 1  # Urna elegida

    # Calculamos la probabilidad usando la regla de Bayes
    probabilidad = calcular_probabilidad_bayes(color_elegido, urna_elegida)

    # Imprimimos el resultado
    print(f"La probabilidad de que la bola verde provenga de la urna {urna_elegida} es: {probabilidad}")

if __name__ == "__main__":
    main()
