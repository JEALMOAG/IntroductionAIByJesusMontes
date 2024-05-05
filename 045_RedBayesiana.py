"""
created on 5 april 17:46:24 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa una red bayesiana para modelar la relación entre una
enfermedad y un síntoma. Define las probabilidades condicionales de la
enfermedad y el síntoma, las agrega al modelo, verifica la validez del modelo
y realiza una consulta para calcular la probabilidad de la enfermedad dado el
síntoma utilizando la inferencia variable.
"""
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definimos la estructura de la red bayesiana
modelo = BayesianModel([('D', 'S')])  # D: enfermedad, S: síntoma

# Definimos las probabilidades condicionales
cpd_enfermedad = TabularCPD('D', 2, [[0.01], [0.99]])  # P(D)
cpd_sintoma = TabularCPD('S', 2, [[0.9, 0.8],  # P(S | D)
                                   [0.1, 0.2]],
                         evidence=['D'], evidence_card=[2])

# Añadimos las probabilidades condicionales al modelo
modelo.add_cpds(cpd_enfermedad, cpd_sintoma)

# Verificamos la validez del modelo
modelo.check_model()

# Creamos un objeto de inferencia para hacer consultas en la red
inferencia = VariableElimination(modelo)

# Consultamos la probabilidad de la enfermedad dado el síntoma
posterior = inferencia.query(variables=['D'], evidence={'S': 1})
print(posterior)
