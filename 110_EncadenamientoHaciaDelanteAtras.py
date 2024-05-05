"""
Created on 17 April  12:29:19 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este código implementa una base de conocimientos que permite agregar afirmaciones
 y reglas, y realizar inferencia hacia adelante y hacia atrás para responder 
 consultas sobre las afirmaciones. Las afirmaciones son hechos sobre relaciones
 familiares, mientras que las reglas representan implicaciones lógicas sobre esas
 relaciones. El ejemplo de uso muestra cómo se puede utilizar esta base de conocimientos
 para inferir relaciones familiares como la abuelidad a partir de relaciones
 parentales como la paternidad.
'''
class KnowledgeBase:
    def __init__(self):
        # Inicializa la base de conocimientos con listas vacías de afirmaciones y reglas
        self.assertions = []  # Lista para almacenar afirmaciones
        self.rules = []       # Lista para almacenar reglas

    def add_assertion(self, assertion):
        # Agrega una afirmación a la base de conocimientos
        self.assertions.append(assertion)  # Añade una nueva afirmación a la lista de afirmaciones

    def add_rule(self, rule):
        # Agrega una regla a la base de conocimientos
        self.rules.append(rule)  # Añade una nueva regla a la lista de reglas

    def forward_inference(self, query):
        # Realiza inferencia hacia adelante para responder una consulta
        inferred_assertions = set()  # Conjunto para almacenar afirmaciones inferidas
        agenda = [query]             # Agenda para procesar

        while agenda:
            # Extrae la afirmación actual de la agenda
            current_assertion = agenda.pop(0)
            # Si la afirmación ya está en la base de conocimientos, continúa con la siguiente afirmación
            if current_assertion in self.assertions:
                continue

            # Agrega la afirmación a las afirmaciones inferidas
            inferred_assertions.add(current_assertion)

            # Itera sobre las reglas para ver si alguna puede ser aplicada
            for rule in self.rules:
                # Verifica si todos los antecedentes de la regla están en las afirmaciones inferidas
                if all(p in inferred_assertions for p in rule.antecedents):
                    # Agrega el consecuente de la regla a la agenda
                    agenda.append(rule.consequent)

        return inferred_assertions

    def backward_inference(self, query):
        # Realiza inferencia hacia atrás para responder una consulta
        agenda = [(query, [])]  # Agenda con la consulta y un camino vacío

        while agenda:
            # Extrae la afirmación actual y el camino de la agenda
            current_assertion, path = agenda.pop(0)
            # Si la afirmación ya está en la base de conocimientos, continúa con la siguiente afirmación
            if current_assertion in self.assertions:
                continue

            # Actualiza el camino con la afirmación actual
            path = path + [current_assertion]

            # Itera sobre las reglas para ver si alguna puede ser aplicada
            for rule in self.rules:
                # Verifica si el consecuente de la regla coincide con la afirmación actual
                if rule.consequent == current_assertion:
                    # Obtiene los antecedentes de la regla
                    sub_goals = rule.antecedents
                    # Crea un nuevo camino con la regla aplicada
                    new_path = path.copy()
                    new_path.append(rule)
                    # Agrega los antecedentes a la agenda con el nuevo camino
                    agenda.extend([(p, new_path) for p in sub_goals])

        return path


class Rule:
    def __init__(self, antecedents, consequent):
        # Inicializa una regla con sus antecedentes y consecuente
        self.antecedents = antecedents  # Antecedentes de la regla
        self.consequent = consequent    # Consecuente de la regla


# Ejemplo de uso
if __name__ == "__main__":
    kb = KnowledgeBase()

    # Afirmaciones
    kb.add_assertion("padre(jose, pedro)")
    kb.add_assertion("padre(pedro, maria)")

    # Reglas
    kb.add_rule(Rule(["padre(X, Y)"], "abuelo(X, Z)"))

    # Consulta
    query = "abuelo(jose, maria)"

    # Inferencia hacia adelante
    inferred_assertions = kb.forward_inference(query)
    print("Afirmaciones inferidas con inferencia hacia adelante:", inferred_assertions)

    # Inferencia hacia atrás
    path = kb.backward_inference(query)
    print("Camino encontrado con inferencia hacia atrás:")
    for step in path:
        if isinstance(step, Rule):
            print("Aplicar regla:", step.antecedents, "->", step.consequent)
        else:
            print("Afirmación:", step)

