import random

numero_secreto=random.randint(1,101)
cant_intentos=0
cant_max=10
adivinado=False

print("bienvenido al juego numero secreto ")

while not adivinado and cant_intentos<cant_max:
    entrada=input("introducir un numero del 0 a 99: ")
    numero=int(entrada)

    if numero==numero_secreto:
        print("has acertado el numero secreto")
        adivinado=True
    elif numero<numero_secreto:
        print("el numero es mayor al ingresado")
    else:
        print("el numero es menor al ingresado")
    cant_intentos=cant_intentos+1

if not cant_intentos<cant_max:
    print(f"has agotado los intentos, el numero secreto era: {numero_secreto}")