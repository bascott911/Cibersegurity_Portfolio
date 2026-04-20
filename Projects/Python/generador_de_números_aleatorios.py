# Generador de números aleatorios 
import random

# Escoger la opción de generar un numero aleatorio
# Escoger la opción de generar un numero aleatorio entre un rango
print("Bienvenido al generador de números aleatorios")
print("Escoja una opcion:")
print("1. Generar un numero aleatorio")
print("2. Generar un numero aleatorio entre un rango")
print("3. Salida")
opcion = int(input("Opcion: "))

# Funciones para generar un numero aleatorio y generar un numero aleatorio entre un rango
def numero_aleatorio():
    print("Bienvenido a generar un numero aleatorio")
    numero = random.randint(1, 10000)
    print("El numero aleatorio es:", numero)

def numero_aleatorio_entre_rango():
    print("Bienvenido a generar un numero aleatorio entre un rango")
    rango = int(input("Ingrese el rango: "))
    numero = random.randint(1, rango)
    print("El numero aleatorio es:", numero)

#Si escoge la opción 1, se ejecuta la función numero_aleatorio, si escoje la opción 2, 
#se ejecuta la función numero_aleatorio_entre_rango, 
#si escoje la opción 3, se sale del programa, si escoje una opción no valida,
#se muestra un mensaje de error y se sale del programa
if opcion == 1:
    numero_aleatorio()
elif opcion == 2:
    numero_aleatorio_entre_rango()
elif opcion == 3:
    print("Saliendo de la generacion de numeros aleatorios")
else:
    print("Opción no válida, por favor seleccione una opción válida")    