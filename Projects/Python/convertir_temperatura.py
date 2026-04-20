# Programa para convertir temperatura entre Celsius y Fahrenheit
# Escoger la opción de la conversión de temperatura
print("Bienvenido a la conversion de temperatura") 
print("Escoja una opcion:")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
opcion = int(input("Opcion: "))

#Funciones para la conversion de temperatura
def celsius_a_fahrenheit():
    print("Bienvenido a la conversion de Celsius a Fahrenheit") 
    c = int(input("Ingrese la temperatura en grados Celsius: "))
    f = (c * 9) / 5 + 32
    print("La temperatura en grados Fahrenheit es: ", f)

def fahrenheit_a_celsius():
    print("Bienvenido a la conversion de Fahrenheit a Celsius") 
    f = int(input("Ingrese la temperatura en grados Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print("La temperatura en grados Celsius es: ", c)

#Si escoge la opción 1, se ejecuta la función celsius_a_fahrenheit, si escoje la opción 2,
#se ejecuta la función fahrenheit_a_celsius,
#si escoje una opción no valida, se muestra un mensaje de error y se sale del programa
if opcion == 1: 
    celsius_a_fahrenheit()
elif opcion == 2:
    fahrenheit_a_celsius()
else:
    print("Opción no válida, por favor seleccione una opción válida")