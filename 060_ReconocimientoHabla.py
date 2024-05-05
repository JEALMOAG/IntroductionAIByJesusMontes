"""
created on 8 Abril 10:23:12  2024
@author:Jesus Alejandro Montes Aguila
"""
"""
El código es un programa que utiliza el reconocimiento de voz para dibujar
formas gráficas (círculos o cuadrados) en una ventana creada con Pygame.
Primero, inicializa Pygame y crea una ventana. Luego, espera a que el usuario
hable un comando de voz ("círculo" o "cuadrado"). Cuando se reconoce un
comando, dibuja la forma correspondiente en la ventana y muestra el resultado.
El usuario puede cerrar la ventana con la tecla "Esc" o haciendo clic en el
botón de cierre.
"""
# Importar las bibliotecas necesarias
import speech_recognition as sr  # Biblioteca para el reconocimiento de voz
import pygame  # Biblioteca para la creación de gráficos por computadora
import sys  # Biblioteca para interactuar con el sistema operativo

# Inicializar Pygame
pygame.init()  # Inicializar Pygame
ventana = pygame.display.set_mode((800, 600))  # Crear una ventana de 800x600 píxeles
pygame.display.set_caption('Gráficos con Reconocimiento de Voz')  # Establecer el título de la ventana

# Función para representar gráficamente un círculo
def dibujar_circulo(x, y):
    pygame.draw.circle(ventana, (255, 0, 0), (x, y), 50)  # Dibujar un círculo rojo en la posición especificada

# Función para representar gráficamente un cuadrado
def dibujar_cuadrado(x, y):
    pygame.draw.rect(ventana, (0, 255, 0), pygame.Rect(x-50, y-50, 100, 100))  # Dibujar un cuadrado verde en la posición especificada

# Función principal
def principal():
    reconocedor = sr.Recognizer()  # Crear un objeto para el reconocimiento de voz
    comando_reconocido = False  # Bandera para indicar si se ha reconocido un comando

    ejecutando = True  # Bandera para indicar si el programa está en ejecución
    while ejecutando:  # Bucle principal del programa
        for evento in pygame.event.get():  # Iterar sobre los eventos pygame
            if evento.type == pygame.QUIT:  # Si se presiona el botón de cierre de la ventana
                ejecutando = False  # Establecer la bandera de ejecución en False
            elif evento.type == pygame.KEYDOWN:  # Si se presiona una tecla
                if evento.key == pygame.K_ESCAPE:  # Si la tecla presionada es 'Esc'
                    ejecutando = False  # Establecer la bandera de ejecución en False

        if not comando_reconocido:  # Si no se ha reconocido un comando
            with sr.Microphone() as fuente:  # Abrir el micrófono
                print("Diga un comando ('circular' o 'cuadrado'):")  # Solicitar al usuario que hable un comando
                audio = reconocedor.listen(fuente)  # Escuchar el audio del micrófono

            try:  # Intentar reconocer el audio
                comando = reconocedor.recognize_google(audio)  # Reconocer el comando usando Google Speech Recognition
                print("Comando reconocido:", comando)  # Imprimir el comando reconocido
                
                if "circular" in comando:  # Si el comando es "círculo"
                    dibujar_circulo(400, 300)  # Dibujar un círculo en la posición especificada
                elif "cuadrado" in comando:  # Si el comando es "cuadrado"
                    dibujar_cuadrado(400, 300)  # Dibujar un cuadrado en la posición especificada
                else:  # Si el comando no es reconocido
                    print("Comando no reconocido")  # Imprimir un mensaje indicando que el comando no es reconocido
                
                pygame.display.flip()  # Actualizar la pantalla después de dibujar
                comando_reconocido = True  # Establecer la bandera de comando reconocido en True

            except sr.UnknownValueError:  # Si no se puede entender el audio
                print("No se pudo entender el audio")  # Imprimir un mensaje indicando que no se pudo entender el audio
            except sr.RequestError as e:  # Si hay un error en la solicitud
                print("Error al solicitar resultados; {0}".format(e))  # Imprimir el error de la solicitud

    pygame.quit()  # Cerrar Pygame
    sys.exit()  # Salir del programa

if __name__ == "__main__":  # Si este script es el programa principal
    principal()  # Llamar a la función principal
