"""
Created on 30 march 18:14:04 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código implementa un Problema de Satisfacción de Restricciones (CSP) y
 utiliza el algoritmo de comprobación hacia adelante (forward checking) 
 para propagar restricciones cuando se asigna un valor a una variable.
 Permite modelar y resolver problemas donde se deben satisfacer restricciones 
 entre variables, como en el caso de asignar colores a regiones adyacentes sin
 que tengan el mismo color.
'''
class Constraint:
    def __init__(self, variable1, variable2):
        # Inicializa una restricción entre dos variables.
        self.variable1 = variable1  # Variable 1 de la restricción.
        self.variable2 = variable2  # Variable 2 de la restricción.

    def satisfies_constraint(self, value1, value2):
        # Comprueba si dos valores cumplen la restricción (no pueden ser iguales).
        return value1 != value2  # Devuelve True si los valores son diferentes, False en caso contrario.


class CSP:
    def __init__(self, variables, domain):
        # Inicializa una instancia de CSP con un conjunto de variables y su dominio.
        self.variables = variables  # Lista de variables del problema CSP.
        self.domain = domain  # Diccionario que asigna a cada variable su conjunto de valores posibles.
        self.constraints = []  # Lista para almacenar las restricciones del problema.

    def add_constraint(self, constraint):
        # Agrega una restricción al problema CSP.
        self.constraints.append(constraint)  # Añade la restricción a la lista de restricciones.

    def forward_checking(self, variable, value):
        # Realiza comprobación hacia adelante para propagar las restricciones cuando se asigna un valor a una variable.
        for constraint in self.constraints:
            # Itera sobre todas las restricciones del problema.
            if constraint.variable1 == variable:
                # Si la primera variable de la restricción es la variable actual:
                neighbor = constraint.variable2  # Identifica la variable vecina.
                for val in self.domain[neighbor]:
                    # Itera sobre los valores del dominio de la variable vecina.
                    if not constraint.satisfies_constraint(value, val):
                        # Si el valor asignado y el valor de la variable vecina no cumplen la restricción:
                        self.domain[neighbor].remove(val)
                        # Elimina el valor de la lista de valores posibles de la variable vecina.


# Define the variables and their domain (available colors).
variables = {'A', 'B', 'C', 'D'}  # Conjunto de variables del problema CSP.
domain = {'A': ['red', 'green', 'blue'],  # Diccionario que asigna a cada variable su conjunto de valores posibles.
          'B': ['red', 'green', 'blue'],
          'C': ['red', 'green', 'blue'],
          'D': ['red', 'green', 'blue']}

# Create a CSP (Constraint Satisfaction Problem).
csp = CSP(variables, domain)  # Instanciamos un objeto CSP con las variables y el dominio definidos.

# Add constraints (adjacent regions cannot have the same color).
csp.add_constraint(Constraint('A', 'B'))  # Agregamos una restricción entre las variables 'A' y 'B'.
csp.add_constraint(Constraint('A', 'C'))  # Agregamos una restricción entre las variables 'A' y 'C'.
csp.add_constraint(Constraint('B', 'C'))  # Agregamos una restricción entre las variables 'B' y 'C'.
csp.add_constraint(Constraint('B', 'D'))  # Agregamos una restricción entre las variables 'B' y 'D'.
csp.add_constraint(Constraint('C', 'D'))  # Agregamos una restricción entre las variables 'C' y 'D'.

# Suppose we assign a color to region A.
variable = 'A'  # Seleccionamos la variable 'A'.
value = 'red'  # Asignamos el valor 'red' a la variable 'A'.

# Apply forward checking to propagate constraints
csp.forward_checking(variable, value)  # Realizamos la propagación de restricciones.

# Show the updated domain after propagation
print("Dominio después de la comprobación hacia adelante:")
for variable, values in csp.domain.items():
    # Iteramos sobre todas las variables y sus valores posibles en el dominio actualizado.
    print(variable + ":", values)  # Imprimimos la variable y sus valores posibles después de la propagación.
