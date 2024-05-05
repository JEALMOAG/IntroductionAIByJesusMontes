"""
Created on 16 April  00:14:32 2024
@author: Jesus Alejandro Montes Aguila
"""
'''
El código proporciona una base de conocimiento para reglas de tráfico, 
permitiendo agregar reglas viales y verificar la validez de proposiciones 
específicas según estas reglas. Cada regla puede contener premisas y una
 conclusión, y el sistema puede ser consultado para determinar si una 
 proposición dada es verdadera de acuerdo con las reglas establecidas.
'''
class BaseConocimiento:
    def __init__(self):
        self.hechos = set()  # Conjunto para almacenar las reglas viales conocidas
        self.reglas = []      # Lista para almacenar las reglas de tráfico

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)  # Agrega una regla vial conocida al conjunto de reglas

    def agregar_regla(self, premisas, conclusion):
        self.reglas.append((premisas, conclusion))  # Agrega una regla de tráfico a la lista de reglas

    def consultar(self, proposicion):
        return self._evaluar(proposicion)  # Consulta si una proposición es válida según las reglas viales

    def _evaluar(self, proposicion):
        if proposicion in self.hechos:  # Si la proposición es una regla vial conocida, devuelve Verdadero
            return True

        for premisas, conclusion in self.reglas:  # Recorre todas las reglas de tráfico
            if all(p in self.hechos for p in premisas):  # Si todas las premisas de la regla son reglas conocidas
                self.hechos.add(conclusion)  # Agrega la conclusión como nueva regla conocida
                return conclusion == proposicion  # Devuelve Verdadero si la proposición coincide con la conclusión de la regla

        return False  # Si la proposición no se puede probar con las reglas viales conocidas, devuelve Falso

# Ejemplo de uso
if __name__ == "__main__":
    base_conocimiento = BaseConocimiento()
    base_conocimiento.agregar_hecho("Conducir en exceso de velocidad")  # Agrega una regla vial conocida
    base_conocimiento.agregar_hecho("Conducir bajo los efectos del alcohol")  # Agrega una regla vial conocida
    base_conocimiento.agregar_regla(["Conducir en exceso de velocidad", "Conducir bajo los efectos del alcohol"], "Multado")  # Agrega una regla de tráfico
    
    print(base_conocimiento.consultar("Multado"))  # Consulta si la proposición "Multado" es válida según las reglas viales (Salida: True)
    print(base_conocimiento.consultar("Conducir en exceso de velocidad"))  # Consulta si la proposición "Conducir en exceso de velocidad" es válida (Salida: True)
    print(base_conocimiento.consultar("Conducir de forma segura"))  # Consulta si la proposición "Conducir de forma segura" es válida (Salida: False)
