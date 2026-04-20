#Este programa es un juego de adivina el número, el usuario tiene que adivinar un número entre 1 y 10, 
#si el número es correcto, el programa le dirá que es correcto, 
#si el número es incorrecto, el programa le dirá que es incorrecto y le mostrará el número correcto.

import random

#Escoger la opción de la adivina el número
print("Bienvenido a la adivina el número")
print("Escoja una opcion:")
print("1. Adivina el número")
print("2. Salida")
opcion = int(input("Opcion: "))

#Función para adivinar el número
def adivina_el_número():
    numero = random.randint(1, 10) #Genera un número aleatorio entre 1 y 10 
    adivina = int(input("Adivina el número entre 1 y 10: ")) #El usuario ingresa el número que va a adivinar
#Si el número es correcto, se muestra un mensaje de correcto
    if numero == adivina:
        print("El número es correcto")
#Si el número es incorrecto, se muestra un mensaje de incorrecto y el número correcto
    else:
        print("El número es incorrecto. El número era:", numero)

#Si escoge la opción 1, se ejecuta la función adivina_el_número, si escoje la opción 2, se sale del programa, 
#si escoje una opción no valida, se muestra un mensaje de error y se sale del programa
if opcion == 1:
    adivina_el_número()
elif opcion == 2:
    print("Saliendo de la adivina el número")
else:
    print("Opcion no valida, por favor escoja una opcion valida")
