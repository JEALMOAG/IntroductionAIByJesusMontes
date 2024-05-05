"""
Created on 29 march 13:11:58 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
El código proporciona una implementación de un algoritmo genético para 
seleccionar la mejor ruta para la entrega de correos entre varias ubicaciones.
 Utiliza la distancia euclidiana entre las ubicaciones como función de aptitud
 y emplea operadores de selección de padres y cruce para evolucionar una 
 población de posibles rutas a lo largo de varias generaciones. Finalmente,
 devuelve la mejor ruta encontrada junto con el número de correos entregados en esa ruta.
'''
# Importación del módulo numpy como np
import numpy as np
# Lista de ubicaciones de oficinas de entrega (podría ser cualquier otro conjunto de ubicaciones)
delivery_offices = [(2, 3), (5, 7), (8, 1), (9, 6), (3, 9), (6, 2)]

# Función para calcular la distancia entre dos ubicaciones (en este caso, usamos la distancia euclidiana)
def calculate_distance(location1, location2):
    # Calcula la distancia euclidiana entre dos ubicaciones
    return np.sqrt((location1[0] - location2[0])**2 + (location1[1] - location2[1])**2)

# Función de aptitud: número de correos entregados en una ruta
def evaluate(route):
    # Inicializa el contador de correos entregados
    delivered_mails = 0
    # Itera sobre la longitud de la ruta
    for i in range(len(route) - 1):
        # Calcula la distancia entre los correos en la ruta
        distance_between_offices = calculate_distance(delivery_offices[route[i]], delivery_offices[route[i+1]])
        # Supongamos que se entrega un correo en cada ubicación, por lo que se incrementa el contador
        delivered_mails += 1
    return delivered_mails

# Algoritmo de selección de oficinas de entrega
def selection(num_employees, num_offices, num_generations):
    # Inicializa la población con permutaciones aleatorias de las ubicaciones de las oficinas de entrega
    population = np.zeros((num_employees, num_offices), dtype=int)
    for i in range(num_employees):
        population[i] = np.random.permutation(num_offices)
    # Inicializa la mejor solución y su aptitud como nulo y menos infinito, respectivamente
    best_solution = None
    best_fitness = float('-inf')
    
    # Itera sobre el número de generaciones especificado
    for _ in range(num_generations):
        # Calcula la aptitud de toda la población
        population_fitness = [evaluate(route) for route in population]
        # Encuentra el índice de la ruta con la mejor aptitud
        idx_best = np.argmax(population_fitness)
        # Actualiza la mejor solución y su aptitud si se encuentra una mejor ruta
        if population_fitness[idx_best] > best_fitness:
            best_fitness = population_fitness[idx_best]
            best_solution = population[idx_best]
        
        # Realiza la selección de padres y el cruce para generar la descendencia
        parents = select_parents(population, population_fitness)
        offspring = []
        for i in range(0, num_employees, 2):
            child1, child2 = crossover(parents[i], parents[i+1])
            offspring.append(child1)
            offspring.append(child2)
        
        # Actualiza la población con la nueva descendencia
        population = np.array(offspring)
    
    return best_solution, best_fitness

# Función de selección de padres: selección por torneo
def select_parents(population, population_fitness):
    # Inicializa la lista de padres
    parents = []
    # Itera sobre toda la población para seleccionar padres
    for _ in range(len(population)):
        # Selecciona dos rutas al azar
        idx1 = np.random.randint(0, len(population))
        idx2 = np.random.randint(0, len(population))
        # Agrega la ruta con la mejor aptitud como padre
        if population_fitness[idx1] > population_fitness[idx2]:
            parents.append(population[idx1])
        else:
            parents.append(population[idx2])
    return parents

# Función de cruce: cruce en un punto
def crossover(parent1, parent2):
    # Elije un punto de cruce aleatorio
    crossover_point = np.random.randint(1, len(parent1))
    # Realiza el cruce de los padres en el punto de cruce para generar dos hijos
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

# Parámetros del algoritmo de selección de oficinas de entrega
num_employees = 50
num_offices = len(delivery_offices)
num_generations = 100

# Ejecución del algoritmo de selección de oficinas de entrega
best_solution, best_fitness = selection(num_employees, num_offices, num_generations)

# Imprime el resultado
print("Mejor ruta encontrada:", best_solution)
print("Número de correos entregados en la mejor ruta:", best_fitness)
