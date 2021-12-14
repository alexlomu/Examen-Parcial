# Examen-Parcial
Esta es la direccion del repositorio [GitGub](https://github.com/alexlomu/Examen-Parcial)
https://github.com/alexlomu/Examen-Parcial
Para este examen hemos hecho dos juegos, en el primero compararemos cuantas palabras se forman a partir de otra empezando por consonantes y por vocales, luego compararemos estas puntuaciones y determinaremos un ganador
En el segundo juego tendremos un tablero de forma cuadrada en el que dos jugadores tendrán una torre en cada columna del tablero que solo podrán mover de forma vertical sin sobrepasar ni ocupar la posición de la torre del otro jugador, cuando un jugador es incapaz de mover ninguna de las torres pierde.
Estas son las capturas de los códigos ejecutandose:![Captura1](https://user-images.githubusercontent.com/91721507/145988847-23b93f35-c5f9-4cb7-95eb-dd06c394956a.JPG)
![Captura2](https://user-images.githubusercontent.com/91721507/145988874-2427da84-ff10-4587-826e-77807a25aba1.JPG)
Estas son los códigos sin ejecutar:
Ejercicio 1:
```#Creamos una lista con las consonantes
consonantes = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","ñ","z","x","c","v","b","n","m"]
#Creamos una lista con las vocales
vocales = ["a","e","i","o","u"]
puntuacion_stuart = 0
puntuacion_kevin = 0
#Hacemos una funcion que nos preguntara la palabra y la convertira en una lista
def palabra():
    global lista
    global palabra_escogida
    palabra_escogida = input("Por favor introduce una palabra: ")
    palabra_escogida = palabra_escogida.lower()
    lista = list(palabra_escogida)
    return lista
    
#Hacemos una funcion para la puntuacion de stuart
def stuart():
    global puntuacion_stuart
    for i in range(len(palabra_escogida)):
        if lista[i - 1] in consonantes:
            valor_1 = len(palabra_escogida) - (i-1)
            puntuacion_stuart += valor_1
    print("La puntuación de Stuart es:"+ str(puntuacion_stuart))
    return puntuacion_stuart
#Hacemos una funcion para la puntuacion de kevin
def kevin():
    global puntuacion_kevin
    for i in range(len(palabra_escogida)):
        if lista[i - 1] in vocales:
            valor_2 = len(palabra_escogida) - (i-1)
            puntuacion_kevin += valor_2
    print("La puntuación de Kevin es:" + str(puntuacion_kevin))
    return puntuacion_kevin
#Hacemos una funcion para comparar las puntuaciones y determinar un ganador
def comparar():
    if puntuacion_stuart < puntuacion_kevin:
        print("Ha ganado Kevin!")
    elif puntuacion_stuart > puntuacion_kevin:
        print("Ha ganado Stuart!")
    else:
        print("Los dos habeis obtenido la misma puntuacion, empate")
    re_match = input("Quereis volver a jugar? Responded si o no.")
    re_match.lower()
    if re_match == "si":
        play()
    if re_match == "no":
        print("Hasta la próxima!")
#Por ultimo la funcion del juego
def play():
    palabra()
    stuart()
    kevin()
    comparar()

play()
```
Ejercicio 2:
```
import math
import os
import random
import re
import sys
#
# Complete the 'verticalRooks' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
# 1. INTEGER_ARRAY r1
# 2. INTEGER_ARRAY r2
#
def verticalRooks(r1, r2):
 # Write your code here
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        t = int(input("Cuanto quieres que dure la partida?En segundos").strip("s"))
        for t_itr in range(t):
            n = int(input().strip())
            r1 = []
        for _ in range(n):
            r1_item = int(input().strip())
            r1.append(r1_item)
            r2 = []
        for _ in range(n):
            r2_item = int(input().strip())
            r2.append(r2_item)
            result = verticalRooks(r1, r2)
        fptr.write(result + '\n')
        fptr.close()
```
