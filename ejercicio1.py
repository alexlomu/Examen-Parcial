#Creamos una lista con las consonantes
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



