"""
Created on 30 march 12:15:08 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código implementa un solucionador de Problemas de Satisfacción de Restricciones
 (CSP) utilizando el algoritmo de búsqueda con retroceso. Un CSP consiste en asignar 
 valores a un conjunto de variables sujetas a ciertas restricciones. La clase `CSP`
 inicializa el problema con variables, dominios y restricciones, y luego busca una
 asignación que cumpla con todas las restricciones mediante el 
 método `backtracking_search`. Si se encuentra una solución, se muestra; de lo
 contrario, se indica que no se encontró ninguna solución.
'''
class CSP:
    def __init__(self, variables, domains, constraints):
        # Inicialización de la clase CSP con variables, dominios y restricciones.
        self.variables = variables  # Lista de variables del problema CSP.
        self.domains = domains  # Diccionario que mapea cada variable a su conjunto de dominio.
        self.constraints = constraints  # Diccionario que mapea cada variable a las variables con las que tiene restricciones.

    def is_consistent(self, variable, assignment):
        # Verifica si asignar un valor a la variable es consistente con las restricciones.
        for neighbor in self.constraints.get(variable, []):
            # Para cada variable vecina de la variable actual:
            if neighbor in assignment and assignment[neighbor] == assignment[variable]:
                # Si la variable vecina está asignada y tiene el mismo valor que la variable actual:
                return False  # La asignación no es consistente.
        return True  # La asignación es consistente.

    def backtracking_search(self, assignment={}):
        # Implementación del algoritmo de búsqueda con retroceso.
        if len(assignment) == len(self.variables):
            return assignment  # Si la asignación es completa, se ha encontrado una solución.
        var = next((v for v in self.variables if v not in assignment), None)
        # Selecciona una variable no asignada.
        for value in self.domains[var]:
            # Para cada valor en el dominio de la variable seleccionada:
            if self.is_consistent(var, {**assignment, var: value}):
                # Si la asignación de ese valor es consistente con las asignaciones actuales:
                assignment[var] = value  # Asigna ese valor a la variable.
                resultado = self.backtracking_search(assignment)
                # Realiza una búsqueda recursiva con la nueva asignación.
                if resultado is not None:
                    return resultado  # Si se encuentra una solución, devuelve la asignación.
                del assignment[var]  # Si no se encuentra una solución, elimina la asignación.
        return None  # No se encontró una solución.


# Ejemplo de uso
if __name__ == "__main__":
    # Definición de variables, dominios y restricciones del problema CSP.
    variables = ['A', 'B', 'C', 'D']  # Nombres de las variables del problema CSP.
    domains = {
        'A': ['Rojo', 'Verde', 'Azul'],  # Valores posibles para la variable A.
        'B': ['Rojo', 'Verde', 'Azul'],  # Valores posibles para la variable B.
        'C': ['Rojo', 'Verde', 'Azul'],  # Valores posibles para la variable C.
        'D': ['Rojo', 'Verde', 'Azul']   # Valores posibles para la variable D.
    }
    restricciones = {
        'A': ['B', 'C'],     # Restricciones de la variable A.
        'B': ['A', 'C', 'D'],  # Restricciones de la variable B.
        'C': ['A', 'B', 'D'],  # Restricciones de la variable C.
        'D': ['B', 'C']      # Restricciones de la variable D.
    }
    # Creación de una instancia del problema CSP y ejecución del algoritmo de búsqueda con retroceso.
    csp = CSP(variables, domains, restricciones)
    solucion = csp.backtracking_search()
    if solucion:
        print("Solución encontrada:")
        for variable, valor in solucion.items():
            print(f"{variable}: {valor}")
    else:
        print("No se encontró solución.")