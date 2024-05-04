"""
created on 3 april 23:58:02 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
Este código implementa un agente de aprendizaje por refuerzo pasivo (APR)
que utiliza el algoritmo de Q-learning para aprender a tomar decisiones en
un entorno dado. El agente selecciona acciones y recibe recompensas basadas
en esas acciones. Luego, utiliza esas recompensas para actualizar sus estimacion
es de los valores Q, que representan el valor esperado de tomar una acción en
un estado dado. Después de un número de episodios de entrenamiento, el agente
prueba su desempeño seleccionando acciones basadas en los valores Q aprendidos
y calcula la recompensa promedio obtenida.
"""
import random  # Importa el módulo random para generar números aleatorios

# Definir la función de recompensa
def obtener_recompensa(accion):
    if accion == 'A':
        return random.choice([1, -1])  # Devuelve una recompensa aleatoria para la acción 'A'
    elif accion == 'B':
        return random.choice([-1, 1])  # Devuelve una recompensa aleatoria para la acción 'B'

# Inicializar valores
valores_Q = {'A': 0, 'B': 0}  # Inicializa los valores Q para cada acción en 0
factor_exploracion = 0.1  # Factor de exploración epsilon
tasa_aprendizaje = 0.1  # Tasa de aprendizaje
factor_descuento = 0.9  # Factor de descuento
num_episodios = 1000  # Número de episodios de entrenamiento

# Entrenamiento del agente
for _ in range(num_episodios):  # Bucle a través de cada episodio
    # Elegir una acción
    if random.random() < factor_exploracion:
        accion = random.choice(['A', 'B'])  # Explorar: elige una acción al azar
    else:
        accion = max(valores_Q, key=valores_Q.get)  # Explotar: elige la acción con el mayor valor Q
    
    # Obtener la recompensa
    recompensa = obtener_recompensa(accion)  # Obtiene la recompensa para la acción elegida
    
    # Actualizar el valor Q
    valores_Q[accion] = valores_Q[accion] + tasa_aprendizaje * (recompensa - valores_Q[accion])  # Actualiza el valor Q según la recompensa

# Probar el agente entrenado
recompensa_total = 0
for _ in range(100):  # Realizar 100 pruebas
    accion = max(valores_Q, key=valores_Q.get)  # Elige la acción con el mayor valor Q
    recompensa = obtener_recompensa(accion)  # Obtiene la recompensa para la acción elegida
    recompensa_total += recompensa  # Acumula la recompensa

print(f"Recompensa promedio: {recompensa_total / 100}")  # Imprime la recompensa promedio
