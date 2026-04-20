#Este programa es una calculadora básica, 
#el usuario puede elegir entre suma, resta, multiplicación y división.

#Escogida de opciones para la calculadora básica
print("Bienvenido a la calculadora basica")
print("Escoja una opcion:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Salida") 
opcion = int(input("Opcion: "))

#Funciones para la calculadora básica.
#Suma de dos numeros 
def suma():
    print("Bienvenido a suma")
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    resultado = numero1 + numero2
    print("La suma es:", resultado)
    
#Resta de dos numeros
def resta():
    print("Bienvenido a resta")
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    resultado = numero1 - numero2
    print("La resta es:", resultado)

#Multiplicación de dos numeros
def multiplicacion():
    print("Bienvenido a multiplicacion")
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    resultado = numero1 * numero2
    print("La multiplicacion es:", resultado)

#Division de dos numeros
def division():
    print("Bienvenido a division")
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    resultado = numero1 / numero2
    print("La division es:", resultado)

#Salida de la calculadora básica
def salida():  
    print("Gracias por usar la calculadora, hasta luego!")

#Si escoge la opción 1, se ejecuta la función suma, si escoje la opción 2, se ejecuta la función resta,
#si escoje la opción 3, se ejecuta la función multiplicacion, si escoje la opción 4, 
#se ejecuta la función division,
#si escoje la opción 5, se ejecuta la función salida, si escoje una opción no valida, 
#se muestra un mensaje de error y se sale del programa
if opcion == 1:
    suma()
elif opcion == 2:
    resta()
elif opcion == 3:
    multiplicacion()
elif opcion == 4:
    division()
elif opcion == 5:
    salida()
else:
    print("Opcion no valida, por favor escoja una opcion valida")