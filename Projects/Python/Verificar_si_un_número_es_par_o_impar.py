#Escogida de opcciones para verificar si un número es par o impar
print("Bienvenido a la verificación de si un número es par o impar")
print("Escoja una opcion:")
print("1. Verificar si un número es par")
print("2. Verificar si un número es impar")
print("3. Salida")
opcion = int(input("Opcion: "))

#decir la opción escogida por el usuario
print("Usted ha escogido la opción: ", opcion)

#Funciones para verificar si un número es par o impar
def verificar_si_un_número_es_par():
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número no es par")

def verificar_si_un_número_es_impar():
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        print("El número no es impar")
    else:
        print("El número es impar")

#Si escoge la opción 1, se verifica si un número es par, si escoje la opción 2, 
#se verifica si un número es impar, si escoje la opción 3, se sale del programa,
#si escoje una opción no valida, se muestra un mensaje de error y se sale del programa
if opcion == 1:
    verificar_si_un_número_es_par()
elif opcion == 2:
    verificar_si_un_número_es_impar()
elif opcion == 3:
    print("Saliendo de la verificación de si un número es par o impar")
else:
    print("Opcion no valida, por favor escoja una opcion valida")