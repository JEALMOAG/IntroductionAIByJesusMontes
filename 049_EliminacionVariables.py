"""
created on 6 april 09:23:12 2024
@author:Jesus Alejandro Montes Aguila
"""
"""

El código define y utiliza un modelo de red bayesiana para representar las
relaciones probabilísticas entre una enfermedad ('E'), un síntoma ('S')
y un tratamiento ('T'). Se definen las probabilidades condicionales de la
enfermedad, el síntoma y el tratamiento dados ciertos estados anteriores.
Luego, se realiza una inferencia para calcular la probabilidad marginal de la
enfermedad, eliminando las otras variables (síntoma y tratamiento) del modelo.
Finalmente, se imprime el resultado de la inferencia.
"""
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definimos la estructura de la red bayesiana
modelo = BayesianModel([('E', 'S'), ('E', 'T')])  # E: enfermedad, S: síntoma, T: tratamiento

# Definimos las probabilidades condicionales
cpd_enfermedad = TabularCPD('E', 2, [[0.01], [0.99]])  # P(E)
cpd_sintoma = TabularCPD('S', 2, [[0.9, 0.8],  # P(S | E)
                                   [0.1, 0.2]],
                         evidence=['E'], evidence_card=[2])
cpd_tratamiento = TabularCPD('T', 2, [[0.7, 0.3],  # P(T | E)
                                    [0.3, 0.7]],
                           evidence=['E'], evidence_card=[2])

# Añadimos las probabilidades condicionales al modelo
modelo.add_cpds(cpd_enfermedad, cpd_sintoma, cpd_tratamiento)

# Verificamos la validez del modelo
modelo.check_model()

# Creamos un objeto de inferencia para hacer consultas en la red
inferencia = VariableElimination(modelo)

# Calculamos la probabilidad marginal de la enfermedad (E) eliminando las otras variables (S y T)
marginal_enfermedad = inferencia.query(variables=['E'])

# Imprimimos el resultado de la inferencia
print(marginal_enfermedad)
