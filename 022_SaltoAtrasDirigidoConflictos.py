"""
created on 1 april 15:23:45 2024
@author Jesus Alejandro Montes Aguila
"""
"""
El código implementa un algoritmo para resolver problemas
de satisfacción de restricciones (CSP), utilizando el método
de Salto Atrás Dirigido por Conflictos. Define clases para representar
el problema y las restricciones, y utiliza estas clases para encontrar
una solución que cumpla con las restricciones establecidas.
"""
# Definición de la clase ProblemaRestricciones
class ProblemaRestricciones:
    # Constructor de la clase
    def __init__(self, variables, dominios):
        # Inicialización de las variables y dominios
        self.variables = variables
        self.dominios = dominios
        self.restricciones = {}

    # Método para agregar una restricción al problema
    def agregar_restriccion(self, restriccion):
        # Itera sobre las variables en el alcance de la restricción
        for var in restriccion.ambito:
            # Verifica si la variable no está en las restricciones
            if var not in self.restricciones:
                # Si no está, crea una lista vacía para esa variable
                self.restricciones[var] = []
            # Agrega la restricción a la lista de restricciones de la variable
            self.restricciones[var].append(restriccion)

    # Método para verificar si una asignación es consistente con las restricciones
    def consistente(self, var, valor, asignacion):
        # Itera sobre las restricciones asociadas a la variable
        for restriccion in self.restricciones.get(var, []):
            # Verifica si la restricción se satisface con el valor dado y la asignación actual
            if not restriccion.satisfecha(valor, asignacion):
                return False
        return True

    # Método para Salto Atrás Dirigido por Conflictos
    def salto_atras_dirigido_por_conflictos(self, asignacion={}, nivel=0):
        # Verifica si la asignación actual cubre todas las variables
        if len(asignacion) == len(self.variables):
            return asignacion
        # Selecciona una variable no asignada
        var = self.seleccionar_variable_no_asignada(asignacion)
        # Itera sobre los valores en el dominio de la variable
        for valor in self.ordenar_valores_dominio(var, asignacion):
            # Verifica si el valor es consistente con la asignación actual
            if self.consistente(var, valor, asignacion):
                # Asigna el valor a la variable
                asignacion[var] = valor
                # Realiza la búsqueda recursiva con la nueva asignación
                resultado = self.salto_atras_dirigido_por_conflictos(asignacion, nivel)
                # Si se encuentra una solución, la devuelve
                if resultado is not None:
                    return resultado
                # Si no se encuentra una solución, deshace la asignación
                del asignacion[var]
        # Si no se encuentra ninguna solución, devuelve None
        return None

    # Método para seleccionar una variable no asignada
    def seleccionar_variable_no_asignada(self, asignacion):
        # Itera sobre las variables y devuelve la primera no asignada
        for var in self.variables:
            if var not in asignacion:
                return var

    # Método para ordenar los valores del dominio de una variable
    def ordenar_valores_dominio(self, var, asignacion):
        # Devuelve los valores del dominio sin ordenar
        return self.dominios[var]


# Definición de la clase Restriccion (base para otras restricciones)
class Restriccion:
    # Constructor de la clase
    def __init__(self, ambito):
        # Inicialización del alcance de la restricción
        self.ambito = ambito

    # Método para verificar si la restricción se satisface con la asignación dada
    def satisfecha(self, asignacion):
        # Este método será implementado en subclases
        raise NotImplementedError


# Definición de la subclase RestriccionDistinto
class RestriccionTodosDistintos(Restriccion):
    # Método para verificar si el valor dado es diferente a los valores asignados
    def satisfecha(self, valor, asignacion):
        # Verifica si el valor está presente en los valores asignados
        if valor in asignacion.values():
            return False
        return True


# Bloque principal del programa
if __name__ == "__main__":
    # Definición de las variables y dominios
    variables = ['A', 'B', 'C']
    dominios = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}
    # Creación de la instancia del problema CSP
    problema = ProblemaRestricciones(variables, dominios)

    # Agrega restricciones al problema CSP
    problema.agregar_restriccion(RestriccionTodosDistintos(['A', 'B']))
    problema.agregar_restriccion(RestriccionTodosDistintos(['B', 'C']))

    # Realiza la búsqueda utilizando Salto Atrás Dirigido por Conflictos para encontrar una solución
    solucion = problema.salto_atras_dirigido_por_conflictos()
    # Imprime la solución encontrada o un mensaje indicando que no se encontró solución
    if solucion is not None:
        print("Solución encontrada:", solucion)
    else:
        print("No se encontró solución.")
