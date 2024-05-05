"""
created on 7 Abril 08:45:12 2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código genera y visualiza la evolución temporal de la media y la varianza de
un proceso estacionario. Para ello, primero define los parámetros del proceso,
luego genera muestras aleatorias de este proceso, calcula la media y la
varianza a lo largo del tiempo, y finalmente grafica estos valores para
mostrar cómo cambian con el tiempo.
"""
import numpy as np  
import matplotlib.pyplot as plt  

# Definición de parámetros del proceso estacionario
media = 0  
desviacion_estandar = 1  
num_muestras = 1000  
num_pasos = 100  

# Generar muestras del proceso estacionario
muestras = np.random.normal(media, desviacion_estandar, size=(num_muestras, num_pasos))

# Calcular la media y la varianza a través del tiempo
media_tiempo = np.mean(muestras, axis=0)  
varianza_tiempo = np.var(muestras, axis=0)  

# Graficar la media y la varianza a través del tiempo
pasos_tiempo = np.arange(num_pasos)  
plt.figure(figsize=(10, 6))  
plt.plot(pasos_tiempo, media_tiempo, label='Media')  
plt.plot(pasos_tiempo, varianza_tiempo, label='Varianza')  
plt.xlabel('Tiempo')  
plt.ylabel('Valor')  
plt.title('Evolución de la Media y la Varianza en un Proceso Estacionario')  
plt.legend()  
plt.grid(True)  
plt.show()  
