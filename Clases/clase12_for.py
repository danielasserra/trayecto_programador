# # Estructuras repetitivas FOR

# # While se utiliza cuando no conocemos la cantidad de operaciones (trabaja con banderas o condiciones)
# # For se usa cuando conocemos la cantidad de iteraciones (ej. lista, que conocemos la cant de elementos q hay)
# # For es como una version abreviada del while

# # funcion "range" devuelve un rango de valores
# rango = range(5) # 0, 1, 2, 3, 4
# # cantidad de elementos menos uno
# # el cero está incluído pero el cinco no

# # el rango me va a permitir saber cuántas veces tengo que iterar
# # es como el contador del while (variable de control)

# # print(list(rango)) 

# # Puedo modificar el rango para que empiece en un lugar y termine en otro: 
# rango = range(0, 5, 1)
# # admite tres parametros: donde empieza, donde termina y el incremento
# print(list(rango)) 

# rango = range(1, 10, 2) # 1, 3 , 5, 7, 9
# # que empiece en 1, termine en 10 y vaya de 2 en 2

# # descendente
# rango = range (10, 1, 1)
# # no funciona

# #--------------------------------------------


# rango = range(0, 10, 1) 
# # FOR reune en el rango todas las inicializaciones que hago en while

# # ES LO MISMO QUE:

# i = 0
# while i < 10:
#     i += 1

# #----------------------------------------------


# # DECRECIENTE

# rango = range(10, 0, -1) 

# # ES LO MISMO QUE:

# i = 10
# while i > 0:
#     i -= 1
    
# #---------------------------------------------

# # for puede trabajar variable de control

# # Daniela Serra
# # FOR
# # EJERCICIO 1
# for i in range(10):
#     print(i+1) #va a mostrar los numeros del 0 al 10

# #-----------------------------------------------

# # Daniela Serra
# # FOR
# # EJERCICIO 2
# for i in range(10, 0, -1):
#     print(i) #va a mostrar los numeros del 10 al 1
    
# #-----------------------------------------------

# # Daniela Serra
# # FOR
# # ejercicio 3. Ingresar un numero.  Mostrar los números desde 0 hasta el número ingresado.

# numero = int(input("Ingrese un numero: "))

# for i in range (0, numero):
#     print(i)

# #-----------------------------------------------

# # Daniela Serra
# # FOR
# # ejercicio 4 
# # Ingresar un número y mostrar la tabla de multiplicar de ese número. 

# numero = int(input("Ingrese un numero: "))

# for i in range (0, 11):
#     multiplicacion = numero * i
#     print(f"{numero} x {i} = {multiplicacion}")

#-----------------------------------------------

# # EJEMPLO BREAK 
# for i in range (0,15):
#     numero = int(input("numero: "))
#     if numero % 2 != 0: # si es impar
#         break

# print("fin") 

#-----------------------------------------------

# # EJEMPLOO CONTINUE

# for i in range (1, 101, 1):
#     if i % 2 != 0: # si es impar
#         continue   # no mostrarlo
#     print(i)

#-----------------------------------------------

# # Daniela Serra
# # FOR. Ejercicio 5. 
# # # Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0.
# # # Mostrar la suma y el promedio de todos los números.

# suma = 0
# contador = 0

# for i in range (10):
#     numero = int(input("Ingrese un numero: "))
#     if numero == 0:
#         break
#     suma += numero
#     contador += 1

# if contador > 0:
#     promedio = suma / contador
#     print(f"suma: {suma}, promedio: {promedio}")
# else:
#     print("No se ingresaron numeros!!!!")

#-----------------------------------------------

# # Daniela Serra
# # FOR
# # ejercicio 6
# # Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)

# for i in range (1, 11):
#     if i % 3 == 0:
#         print(i)

# for i in range (3, 11, 3):
#     print(i)
# #-----------------------------------------------

# # Daniela Serra
# # FOR ejercicio 7
# # Mostrar los números pares que hay desde la unidad hasta el número 50

# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

#-----------------------------------------------

# # Daniela Serra
# # FOR ejercicio 9
# # Ingresar un número. Mostrar todos los divisores que hay desde el 1 
# # hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

# numero = int(input("ingrese un numero: "))
# contador_divisores = 0

# for i in range (1, numero + 1, 1):
#     if numero % i == 0: # es divisor del nunero
#         print(i)
#         contador_divisores += 1
# print(contador_divisores)

#-----------------------------------------------

# for i in range(5):
#     for j in range(3):
#         print("(i):(j)")

# # por cada iteración de i, jota itera 3 veces
# # sirve para ordenar listas

#-----------------------------------------------

# # Daniela Serra
# # FOR ejercicio 8
# # Realizar un programa que permita mostrar una pirámide de números. 

# numero = int(input("Ingrese un numero: "))

# for i in range(1, numero + 1):
#     for j in range (1, i + 1):
#         print(j, end = "")
#     print()
    

# tarea 8, 10 y 11

