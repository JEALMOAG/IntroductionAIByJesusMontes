"""
created on 6 april 09:23:12 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código implementa una red bayesiana para modelar la relación entre una
enfermedad (E) y un síntoma (S). Utiliza la biblioteca pgmpy para definir
la estructura de la red y las probabilidades condicionales asociadas.
Luego, realiza una consulta de inferencia para determinar la probabilidad
de la enfermedad dada la observación de un síntoma específico.
"""
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definimos la estructura de la red bayesiana
modelo = BayesianModel([('E', 'S')])  # E: enfermedad, S: síntoma

# Definimos las probabilidades condicionales
prob_enfermedad = TabularCPD('E', 2, [[0.01], [0.99]])  # P(E)
prob_sintoma = TabularCPD('S', 2, [[0.9, 0.8],  # P(S | E)
                                    [0.1, 0.2]],
                          evidence=['E'], evidence_card=[2])

# Añadimos las probabilidades condicionales al modelo
modelo.add_cpds(prob_enfermedad, prob_sintoma)

# Verificamos la validez del modelo
modelo.check_model()

# Creamos un objeto de inferencia para hacer consultas en la red
inferencia = VariableElimination(modelo)

# Consultamos la probabilidad de la enfermedad dado los síntomas observados
resultado = inferencia.query(variables=['E'], evidence={'S': 1})

# Imprimimos el resultado de la inferencia
print(resultado)
