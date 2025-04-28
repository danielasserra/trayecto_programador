# condicion = ""
# sentencias_a_repetir = ""

# while condicion:
#     sentencias_a_repetir

# Clase 07
# REPETITIVAS WHILE

# Daniela Serra
# While
# # Ejercicio 01
# # Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

# contador = 0

# while contador < 10:
#     print(contador + 1)
#     # contador = contador + 1
#     contador += 1

# print("FIN")

#--------------------------------------------
# Daniela Serra
# While
# Ejercicio 02
# Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

# contador = 0
# numero = 10

# # Opcion 1

# while contador < 10:
#     print(numero)
#     numero -= 1
#     contador += 1

# print("FIN")

# # Opcion 2

# contador = 10
# while contador > 0:
#     print(contador)
#     contador -= 1
# print("FIN")

#--------------------------------------------
# # Daniela Serra
# # While
# # Ejercicio 03
# # Mostrar la suma de los números desde el 1 hasta el 10.

# contador = 0
# suma = 0

# while contador <= 10:
#      suma += contador
#      contador += 1
# print(f"{suma}")


#--------------------------------------------

# Daniela Serra
# While
# # Ejercicio 04
# # Mostrar la suma de los números pares desde el 1 hasta el 10.

# # SOLUCION ALGORÍTMICA
# # Busqueda: está evaluando si el numero es par.
# i = 0 # contador = 0 --- variable de control
# suma_pares = 0

# while i <= 10:
#     if i % 2 == 0:
#         suma_pares += i
#     i += 1

# print(f"La suma de los numeros pares del 1 al 10 es: {suma_pares}")

# # SOLUCION ARITMÉTICA
# # Logica matemática
# # Ventaja: no hace las diez iteraciones, hace la mitad
# i = 0 # contador = 0 --- variable de control
# suma_pares = 0

# while i < 10:
#     i += 2
#     suma_pares += i

# print(f"La suma de los numeros pares del 1 al 10 es: {suma_pares}")

#--------------------------------------------

# Daniela Serra
# # While
# # Ejercicio 05
# # Solicitar el ingreso de 5 números, calcular la suma de los números ingresados 
# # y el promedio. Mostrar la suma y el promedio por pantalla.

# # ENTRADA: pedir un numero (se repite)
# # PROCESO: acumular (se repite)
# # SALIDA: mostrar la suma (no se repite)

# contador = 0
# acumulador = 0

# while contador < 5:
#     numero = int(input("Ingrese un numero: "))
#     acumulador += numero
#     contador += 1

# promedio = acumulador / contador
# print(f"La suma de sus numeros es {acumulador}\n"
#       f"El promedio de sus numeros es {promedio}")

#--------------------------------------------

# Daniela Serra
# While
# Ejercicio 06
# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).
# Calcular la suma de los números ingresados y el promedio de los mismos.


# NO FUNCIONA
# i = 0
# suma = 0

# while i != "no" :
#     numero_ingresado = int(input("Ingrese un número o escriba 'no' para terminar: "))
#     suma += numero_ingresado
#     i += 1

# promedio = suma / i

# print(f"La suma de los numeros ingresados es: {suma} y su promedio es {promedio}")

# NO FUNCIONA
# i = 0
# suma = 0

# while True:
#     numero_ingresado = int(input("Ingrese un número o escriba 'no' para terminar: "))

#     if numero_ingresado == "no":
#         break

#     suma += numero_ingresado
#     i += 1

# promedio = suma / i

# print(f"La suma de los numeros ingresados es: {suma} y su promedio es {promedio}")

# FUNCIONA
# cantidad = 1
# contador = 0
# suma = 0

# while contador < cantidad:
#     numero = int(input("ingrese numero: "))

#     eleccion = input("quiere seguir?")
#     if eleccion == "si":
#         cantidad += 1
    
#     suma += numero
#     contador += 1

# promedio = suma / contador
# print(f"La suma de los numeros ingresados es: {suma} y su promedio es {promedio}")



# FUNCIONA MEJOR

# contador = 0
# suma = 0
# eleccion = "si"

# while eleccion == "si":
#     numero = int(input("ingrese numero: "))
#     suma += numero
#     contador += 1
#     eleccion = input("quiere seguir?")

# promedio = suma / contador
# print(f"La suma de los numeros ingresados es: {suma} y su promedio es {promedio}")

#--------------------------------------------

# Daniela Serra
# While
# Ejercicio 06
# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).
# Calcular la suma de los números ingresados y el promedio de los mismos.

condicion = "si"
suma = 0
i = 0

while condicion == "si":
    numero = int(input("Ingrese un numero: "))
    suma += numero
    condicion = input("¿Desea continuar? (si/no): ")
    i += 1

promedio = suma / i

print(f"La suma de los numeros ingresados es {suma}")
print(f"El promedio de los numeros ingresados es {promedio}")


# Tarea: ejercicios del 1 al 7