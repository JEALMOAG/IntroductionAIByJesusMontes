"""
Created on 16 April  02:18:32 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código proporciona una clase llamada InferenciaLogicaProposicional que 
permite realizar inferencias sobre la lógica proposicional. Puedes agregar
 cláusulas lógicas y luego consultar si una expresión lógica específica es 
 verdadera, falsa o insatisfacible. Utiliza la biblioteca SymPy para manipular 
 símbolos y expresiones lógicas en Python.
'''
# Import the necessary functions and classes from the SymPy library
from sympy import symbols, Not, Or, And, satisfiable

# Define a class for Propositional Logic Inference
class PropositionalLogicInference:
    def __init__(self):
        pass

    # Method to perform inference
    def infer(self, clauses, query):
        # Add the negation of the query to the clauses
        clauses.append(Not(query))
        
        # Convert the clauses into a single expression
        expression = And(*clauses)
        
        # Check if the expression is unsatisfiable
        if not satisfiable(expression):
            return "Unsatisfiable"
        
        # Check if the query is satisfied
        if satisfiable(And(*clauses)):
            return "True"
        else:
            return "False"

# Example of usage
if __name__ == "__main__":
    # Create an instance of the PropositionalLogicInference class
    inference = PropositionalLogicInference()
    
    # Define symbols
    p, q, r = symbols('p q r')
    
    # Define clauses (set of logical expressions)
    clauses = [Or(p, q), Or(Not(p), r), Or(Not(q), Not(r))]
    
    # Query (a logical expression to be checked)
    query = r
    
    # Perform inference
    result = inference.infer(clauses, query)
    print("The result of the inference is:", result)


