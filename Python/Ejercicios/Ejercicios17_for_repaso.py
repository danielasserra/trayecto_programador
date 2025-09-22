# # # Ejercicio 1
# # # Mostrar los números ascendentes desde el 1 al 10

# for i in range(10):
#     print(i+1)

# # ------------------------

# # Ejercicio 2
# # Mostrar los números descendentes desde el 10 al 1

# for i in range (10, 0, -1):
#     print(i)

# # ------------------------

# # Ejercicio 3
# # Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

# numero = int(input("Ingrese un numero: "))

# for i in range(numero + 1):
#     print(i)

# # --------------------------

## EJERCICIO 4
# # Ingresar un número y mostrar la tabla de multiplicar de ese número.

# numero = int(input("Ingrese un numero: "))

# for i in range(11):
#     resultado = numero * i
#     print(numero, "X", i, "=", resultado)

## ------------------------------------

## Ejercicio 5
# # Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. 
# # Mostrar la suma y el promedio de todos los números.

# suma = 0
# contador = 0

# for i in range(10):
#     numero = int(input("Ingrese un numero: "))
#     if numero == 0:
#         break
#     suma += numero
#     contador += 1
    
# if contador != 0:
#     promedio = suma / contador
# print(suma, promedio)

## ------------------------------------

## Ejercicio 6
# # Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)

# for i in range(1, 11):
#     if i % 3 == 0:
#         print(i)

## ------------------------------------

## Ejercicio 7
# # Mostrar los números pares que hay desde la unidad hasta el número 50 

# for i in range(51):
#     if i % 2 == 0:
#         print(i)

## ------------------------------------

## Ejercicio 8
## Realizar un programa que permita mostrar una pirámide de números. 

# numero = int(input("Ingrese un numero: "))

# for i in range(1, numero + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

## ------------------------------------

## Ejercicio 9
## Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el 
# # número ingresado. Mostrar la cantidad de divisores encontrados.

# numero = int(input("Ingrese un numero "))

# cantidad_divisores = 0

# for i in range(1, numero + 1):
#     if numero % i == 0:
#         print(i)
#         cantidad_divisores += 1
# print(f"Cantidad de divisores encontrados: {cantidad_divisores}")

## ------------------------------------

## Ejercicio 10
# # Ingresar un número. Determinar si el número es primo o no.

# numero = int(input("Ingrese un numero: "))
# es_primo = True

# for i in range(2, numero):
#     if numero % i == 0:
#         es_primo = False
#         break
# if es_primo == True:
#     print("Es primo")
# else:
#     print("No es primo")

## ------------------------------------

## Ejercicio 11
# # Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. 
# # Informar cuántos números primos se encontraron.

# numero = int(input("Ingrese un numero: "))
# contador_primos = 0

# for i in range (1, numero + 1):
#     contador_divisores = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             contador_divisores += 1
#     if contador_divisores == 2:
#         contador_primos += 1
#         print(i)
# print(f"Se encontraron {contador_primos} numeros primos entre 1 y {numero}")

## ------------------------------------

## Ejercicio 11
# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. 
# Informar cuántos números primos se encontraron.

numero = int(input("Ingrese un numero: "))
contador_primos = 0

for i in range(1, numero + 1):
    contador_divisores = 0
    for j in range(1, i + 1):
        if i % j == 0:
            contador_divisores += 1
    if contador_divisores == 2:
        contador_primos += 1
        print(i)
print(f"La cantidad de numeros primos entre 1 y {numero} es {contador_primos}")