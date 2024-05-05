"""
created on 11 Abril 13:34:00 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código proporcionado implementa una Gramática Probabilística Independiente
del Contexto (PCFG, por sus siglas en inglés) utilizando la clase
GramaticaProbabilisticaContextoIndependiente. Esta clase permite definir
reglas de producción para diferentes símbolos no terminales, junto con probabilidades
asociadas a estas reglas. Luego, el método generar_oracion() genera una oración
aleatoria siguiendo las reglas definidas, expandiendo recursivamente los
símbolos no terminales de acuerdo a las probabilidades especificadas.
Finalmente, el código ejemplifica el uso de esta clase definiendo una PCFG para
la generación de oraciones en español y generando una oración aleatoria.
"""
from collections import defaultdict  # Importa la clase defaultdict del módulo collections
import random  # Importa el módulo random para generar números aleatorios

class GramaticaProbabilisticaContextoIndependiente:  # Clase para la Gramática Probabilística Independiente del Contexto
    def __init__(self):  # Inicializa la clase
        self.reglas = defaultdict(list)  # Diccionario para almacenar las reglas de producción con listas vacías por defecto
        self.simbolo_inicial = None  # Símbolo inicial

    def agregar_regla(self, izquierda, derecha, probabilidad):  # Método para agregar una regla de producción
        self.reglas[izquierda].append((derecha, probabilidad))  # Agrega la regla de producción al diccionario

    def establecer_simbolo_inicial(self, simbolo_inicial):  # Método para establecer el símbolo inicial
        self.simbolo_inicial = simbolo_inicial  # Asigna el símbolo inicial

    def generar_oracion(self):  # Método para generar una oración aleatoria
        return self.expandir(self.simbolo_inicial)  # Llama al método expandir con el símbolo inicial como argumento

    def expandir(self, simbolo):  # Método para expandir un símbolo en una oración
        expansiones = self.reglas.get(simbolo, [])  # Obtiene las expansiones posibles del símbolo
        if not expansiones:  # Si no hay expansiones posibles
            return [simbolo]  # Retorna el símbolo como una palabra terminal
        derecha, probabilidades = zip(*expansiones)  # Separa las reglas de producción y las probabilidades en listas
        derecha_elegida = random.choices(derecha, probabilidades)[0]  # Elige una regla de producción según las probabilidades
        return sum((self.expandir(s) for s in derecha_elegida), [])  # Expande recursivamente cada símbolo en la regla

# Ejemplo de uso
gramatica = GramaticaProbabilisticaContextoIndependiente()  # Crea una instancia de la clase GramaticaProbabilisticaContextoIndependiente
gramatica.agregar_regla('S', ['NP', 'VP'], 0.8)  # Agrega una regla de producción para S
gramatica.agregar_regla('S', ['Aux', 'NP', 'VP'], 0.2)  # Agrega otra regla de producción para S
gramatica.agregar_regla('NP', ['Det', 'N'], 0.5)  # Agrega una regla de producción para NP
gramatica.agregar_regla('NP', ['Det', 'N', 'PP'], 0.3)  # Agrega otra regla de producción para NP
gramatica.agregar_regla('NP', ['Det', 'Adj', 'N'], 0.2)  # Agrega otra regla de producción para NP
gramatica.agregar_regla('VP', ['V', 'NP'], 0.6)  # Agrega una regla de producción para VP
gramatica.agregar_regla('VP', ['V', 'NP', 'PP'], 0.4)  # Agrega otra regla de producción para VP
gramatica.agregar_regla('PP', ['P', 'NP'], 1.0)  # Agrega una regla de producción para PP
gramatica.agregar_regla('Det', ['el'], 0.5)  # Agrega una regla de producción para Det
gramatica.agregar_regla('Det', ['un'], 0.5)  # Agrega otra regla de producción para Det
gramatica.agregar_regla('N', ['hombre'], 0.3)  # Agrega una regla de producción para N
gramatica.agregar_regla('N', ['perro'], 0.3)  # Agrega otra regla de producción para N
gramatica.agregar_regla('N', ['gato'], 0.2)  # Agrega otra regla de producción para N
gramatica.agregar_regla('N', ['telescopio'], 0.2)  # Agrega otra regla de producción para N
gramatica.agregar_regla('Adj', ['grande'], 0.5)  # Agrega una regla de producción para Adj
gramatica.agregar_regla('Adj', ['pequeño'], 0.5)  # Agrega otra regla de producción para Adj
gramatica.agregar_regla('V', ['comió'], 0.4)  # Agrega una regla de producción para V
gramatica.agregar_regla('V', ['vio'], 0.3)  # Agrega otra regla de producción para V
gramatica.agregar_regla('V', ['caminó'], 0.3)  # Agrega otra regla de producción para V
gramatica.agregar_regla('P', ['con'], 0.6)  # Agrega una regla de producción para P
gramatica.agregar_regla('P', ['en'], 0.4)  # Agrega otra regla de producción para P

gramatica.establecer_simbolo_inicial('S')  # Establece el símbolo inicial como 'S'
oracion = gramatica.generar_oracion()  # Genera una oración aleatoria
print(' '.join(oracion))  # Imprime la oración generada como una cadena de texto
