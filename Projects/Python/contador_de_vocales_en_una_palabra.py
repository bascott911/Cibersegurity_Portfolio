#Este programa es un contador de vocales en una palabra,
#el usuario ingresa una palabra y el programa contará el número de vocales en la palabra.

#Escoger la opción de contar las vocales en una palabra
print("Bienvenido a contar las vocales en una palabra")
palabra = str(input("Ingrese una palabra: "))

#Declarar el número de vocales en la palabra
vocales = 0

#Bucle para contar las vocales en la palabra
for letra in palabra:
    if letra.lower() in "aeiou":
        vocales += 1

#Si la palabra ingresada es una palabra, se muestra el número de vocales en la palabra
if palabra.isalpha():
        print("La cantidad de vocales en la palabra es:", vocales)
        print("La Palabra ingresada es:", palabra)
        print("Gracias por usar el contador de vocales en una palabra :)")

#Si la palabra ingresada no es una palabra, se muestra un mensaje de error
else:
    print("No es una palabra valida, por favor ingrese una palabra valida")