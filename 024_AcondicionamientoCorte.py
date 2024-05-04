"""
Created on 1 april 19:14:23 2024
@author: Jesus Alejandro Mntes Aguila
"""
"""
El código proporciona una implementación de un Problema de Satisfacción de Restricciones (PSR)
y el algoritmo de búsqueda atrás para resolverlo. Define restricciones binarias
entre variables y permite verificar si una asignación de valores a las variables
satisface las restricciones. El código también incluye un ejemplo de uso para resolver
un problema específico de PSR.
"""
class Restriccion:
    def __init__(self, variable1, variable2, condicion):  
        self.variable1 = variable1  
        self.variable2 = variable2  
        self.condicion = condicion  
    
    def satisfecha(self, asignacion):  
        if self.variable1 not in asignacion or self.variable2 not in asignacion:  
            return True
        return self.condicion(asignacion[self.variable1], asignacion[self.variable2])  

def no_igual(a, b):  
    return a != b

def igual(a, b):  
    return a == b

class ProblemaSR:
    def __init__(self, variables, dominios):  
        self.variables = variables  
        self.dominios = dominios  
        self.restricciones = {}  
        for var in self.variables:  
            self.restricciones[var] = []  
        
        for var in self.variables:
            if var not in self.dominios:
                raise LookupError("Cada variable debe tener un dominio asignado.")
    
    def agregar_restriccion(self, restriccion):  
        for var in restriccion.variable1, restriccion.variable2:  
            if var not in self.variables:  
                raise LookupError("Variable en la restricción no está en el ProblemaSR.")
            self.restricciones[var].append(restriccion)  
    
    def consistente(self, variable, valor, asignacion):  
        for restriccion in self.restricciones[variable]:  
            if not restriccion.satisfecha(asignacion):  
                return False  
        return True  
    
    def búsqueda_atrás(self, asignación={}):  
        if len(asignación) == len(self.variables):  
            return asignación  
        no_asignadas = [var for var in self.variables if var not in asignación]  
        primera = no_asignadas[0]  
        for valor in self.dominios[primera]:  
            if self.consistente(primera, valor, asignación):  
                asignación[primera] = valor  
                resultado = self.búsqueda_atrás(asignación)  
                if resultado is not None:  
                    return resultado  
                del asignación[primera]  
        return None  

# Ejemplo de uso:
variables = ['A', 'B', 'C']  
dominios = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}  

problema = ProblemaSR(variables, dominios)  
problema.agregar_restriccion(Restriccion('A', 'B', no_igual))  
problema.agregar_restriccion(Restriccion('B', 'C', igual))  

solución = problema.búsqueda_atrás()  
if solución:  
    print("Solución encontrada:")  
    for variable, valor in solución.items():  
        print(f"{variable}: {valor}")  
else:  
    print("No se encontró solución para el problema.")  
