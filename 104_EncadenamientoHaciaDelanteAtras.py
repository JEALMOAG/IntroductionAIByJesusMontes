"""
Created on 16 April  13:07:09 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código implementa dos algoritmos de inferencia en lógica proposicional: 
    encadenamiento hacia adelante y encadenamiento hacia atrás. Utiliza reglas
    y una base de conocimiento para inferir si una meta puede ser demostrada a 
    partir de las reglas dadas y los hechos conocidos. El encadenamiento hacia 
    adelante agrega hechos a la base hasta que no puede inferir más, mientras 
    que el encadenamiento hacia atrás intenta demostrar la meta retrocediendo 
    a través de las reglas.
'''
# Define una función para el encadenamiento hacia adelante
def forward_chaining(knowledge_base, rules):
    while True:
        something_changed = False
        # Itera sobre todas las reglas
        for rule in rules:
            # Verifica si todos los antecedentes de la regla están en la base de conocimiento
            antecedents_true = all(premise in knowledge_base for premise in rule[0])
            consequent = rule[1]
            # Si todos los antecedentes son verdaderos y el consecuente no está en la base de conocimiento, agrégalo
            if antecedents_true and consequent not in knowledge_base:
                knowledge_base.append(consequent)
                something_changed = True
        # Si no se agregaron nuevos hechos en esta iteración, salimos del bucle
        if not something_changed:
            break
    # Devuelve la base de conocimiento final
    return knowledge_base

# Define una función para el encadenamiento hacia atrás
def backward_chaining(goal, rules, knowledge_base):
    # Si la meta ya está en la base de conocimiento, devuelve True
    if goal in knowledge_base:
        return True
    # Si la meta no está en la base de conocimiento, intenta probarla utilizando las reglas
    for rule in rules:
        consequent = rule[1]
        if goal == consequent:
            antecedents = rule[0]
            # Verifica si todos los antecedentes pueden ser probados recursivamente
            if all(backward_chaining(premise, rules, knowledge_base) for premise in antecedents):
                return True
    # Si ninguna regla puede probar la meta, devuelve False
    return False

# Base de conocimiento inicial
knowledge_base = ['P', 'Q']

# Definición de reglas
rules = [(['P'], 'R'),
         (['R'], 'S'),
         (['Q'], 'T'),
         (['S', 'T'], 'U')]

# Encadenamiento hacia adelante
print("Encadenamiento hacia adelante:")
forward_result = forward_chaining(knowledge_base, rules)
print("Base de conocimiento final:", forward_result)

# Encadenamiento hacia atrás
print("\nEncadenamiento hacia atrás:")
goal = 'U'
backward_result = backward_chaining(goal, rules, knowledge_base)
print("¿Se puede demostrar la meta?", backward_result)
