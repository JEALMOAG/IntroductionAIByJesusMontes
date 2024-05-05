"""
Created on 17 April  03:31:48 2024
@author: Jesus Alejandro Montes Aguila 
"""
'''
Este código proporciona recomendaciones de actividades basadas en el clima actual.
 Define una base de conocimiento que mapea diferentes tipos de clima a las
 actividades recomendadas para ese clima. Luego, proporciona una función 
 recomendar_actividad que toma el clima actual como entrada y devuelve las 
 actividades recomendadas para ese clima. Finalmente, imprime las actividades 
 recomendadas para el clima actual.
'''
base_conocimiento = {
    "soleado": ["hacer picnic", "jugar al voleibol"],  # Si está soleado, se recomienda hacer un picnic o jugar al voleibol
    "lluvioso": ["ver una película en casa", "cocinar algo nuevo"],  # Si está lluvioso, se recomienda ver una película en casa o cocinar algo nuevo
    "nublado": ["visitar un museo", "hacer manualidades"]  # Si está nublado, se recomienda visitar un museo o hacer manualidades
}

# Reglas para determinar qué actividad recomendar basada en el clima
def recomendar_actividad(clima):
    if clima in base_conocimiento:  # Verifica si el clima dado está en la base de conocimiento
        return base_conocimiento[clima]  # Devuelve las actividades recomendadas para ese clima
    else:
        return ["No se encontraron actividades recomendadas para este clima."]  # Si el clima no está en la base de conocimiento, devuelve un mensaje de error

# Clima actual (entrada del usuario)
clima_actual = "soleado"  # Puedes cambiar esto según el clima actual

# Obtener recomendación de actividad
recomendaciones = recomendar_actividad(clima_actual)  # Llama a la función para obtener las recomendaciones de actividad

# Imprimir recomendaciones
print("Actividades recomendadas para el clima", clima_actual + ":")  # Imprime el clima actual
for actividad in recomendaciones:  # Itera sobre cada actividad recomendada
    print("- " + actividad)  # Imprime la actividad recomendada con un guion antes
