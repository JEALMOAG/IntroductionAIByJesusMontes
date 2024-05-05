"""
Created on 29 march 21:10:01 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código implementa un algoritmo de búsqueda con retroceso para resolver problemas 
de restricción (CSP). Define una clase `CSP` que toma una lista de variables,
 un diccionario de dominios y un diccionario de restricciones como entrada.
 Luego, busca una solución consistente para el CSP utilizando el algoritmo de
 búsqueda con retroceso. El ejemplo de uso crea una instancia del problema CSP 
 y encuentra una solución para el mismo..
'''
class CSP:
    def __init__(self, lista_variables, dominios, restricciones):
        # Inicialización de la clase con las variables, dominios y restricciones.
        self.lista_variables = lista_variables  # Lista de variables en el problema CSP.
        self.dominios = dominios  # Diccionario que mapea cada variable a su conjunto de dominio.
        self.restricciones = restricciones  # Diccionario que mapea cada variable a las variables con las que tiene restricciones.

    def es_consistente(self, variable, asignacion):
        # Verifica si asignar un valor a la variable es consistente con las restricciones.
        for vecino in self.restricciones.get(variable, []):
            # Para cada variable vecina de la variable actual:
            if vecino in asignacion and asignacion[vecino] == asignacion[variable]:
                # Si la variable vecina está asignada y tiene el mismo valor que la variable actual:
                return False  # La asignación no es consistente.
        return True  # La asignación es consistente.

    def busqueda_con_retroceso(self, asignacion={}):
        # Implementación del algoritmo de búsqueda con retroceso.
        if len(asignacion) == len(self.lista_variables):
            return asignacion  # Si la asignación es completa, se ha encontrado una solución.
        var = next((v for v in self.lista_variables if v not in asignacion), None)
        # Selecciona una variable no asignada.
        for valor in self.dominios[var]:
            # Para cada valor en el dominio de la variable seleccionada:
            if self.es_consistente(var, {**asignacion, var: valor}):
                # Si la asignación de ese valor es consistente con las asignaciones actuales:
                asignacion[var] = valor  # Asigna ese valor a la variable.
                resultado = self.busqueda_con_retroceso(asignacion)
                # Realiza una búsqueda recursiva con la nueva asignación.
                if resultado is not None:
                    return resultado  # Si se encuentra una solución, devuelve la asignación.
                del asignacion[var]  # Si no se encuentra una solución, elimina la asignación.
        return None  # No se encontró una solución.


# Ejemplo de uso
if __name__ == "__main__":
    # Definición de variables, dominios y restricciones del problema CSP.
    lista_variables = ['A', 'B', 'C', 'D']  # Nombres de las variables en el problema CSP.
    dominios = {
        'A': ['Red', 'Green', 'Blue'],  # Valores posibles para la variable A.
        'B': ['Red', 'Green', 'Blue'],  # Valores posibles para la variable B.
        'C': ['Red', 'Green', 'Blue'],  # Valores posibles para la variable C.
        'D': ['Red', 'Green', 'Blue']   # Valores posibles para la variable D.
    }
    restricciones = {
        'A': ['B', 'C'],     # Restricciones de la variable A.
        'B': ['A', 'C', 'D'],  # Restricciones de la variable B.
        'C': ['A', 'B', 'D'],  # Restricciones de la variable C.
        'D': ['B', 'C']      # Restricciones de la variable D.
    }
    # Creación de una instancia del problema CSP y ejecución del algoritmo de búsqueda con retroceso.
    csp = CSP(lista_variables, dominios, restricciones)
    solucion = csp.busqueda_con_retroceso()
    if solucion:
        print("Solución encontrada:")
        for variable, valor in solucion.items():
            print(f"{variable}: {valor}")
    else:
        print("No se encontró solución.")

