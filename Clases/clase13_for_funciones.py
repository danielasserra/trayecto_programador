# FOR
# FUNCIONES

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

# ------------------------------------------------

# # # Daniela Serra
# # # FOR ejercicio 10
# numero = int(input("ingrese un numero: "))
# contador_divisores = 0

# for i in range (1, numero + 1, 1):
#     if numero % i == 0: # es divisor del nunero
#         contador_divisores += 1

# if contador_divisores == 2:
#     print("es primo")
# else:
#     print("no es primo")

# # CON BANDERA 

# numero = int(input("ingrese un numero: "))
# bandera_divisores = False

# for i in range (2, numero):
#     if numero % i == 0: # es divisor del nunero
#         bandera_divisores = True
#         break
# if bandera_divisores == False:        
#     print("El numero es primo")
# else:
#     print("El numero no es primo")

#---------------------------------------------

# # Daniela Serra
# # For. Ejercicio 11.
# # Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. 
# # Informar cuántos números primos se encontraron.

# numero = int(input("ingrese un numero: "))
# contador_primos = 0

# for i in range (2, numero + 1):
#     bandera_primo = True
#     for j in range (2, i):
#         if i % j == 0: # es divisor del nunero
#             bandera_primo = False
#             break
#         if bandera_primo == True:
#             print(i)
#             contador_primos += 1

# print("se encontraron", contador_primos, "numeros primos")
# #------------------------------------------------

# # FUNCIONES

# # Una funcion que sume dos numeros

# # Hasta ahora vimos:
# un_numero = int(input("ingrese un numero: "))
# otro_numero = int(input("ingrese otro numero: "))
# suma = un_numero + otro_numero
# print("la suma es:", suma)

# ######## FUNCIONES ########

# def sumar_1():
#     un_numero = int(input("ingrese un numero: "))
#     otro_numero = int(input("ingrese otro numero: "))
#     suma = un_numero + otro_numero
#     print("la suma es:", suma) # el print muestra q hizo con el proceso pero no lo puedo modificar


# #funciones nulas: no devuelve nada, no hace nada
# # no hay entradas ni salidas, hace todo la fn

# #-------------------


# # otro tipo de funcion q haga lo mismo. 
# # en vez de pedir los numeros en la fn, vendran x parametro. 
# # se los paso en la llamada a la fn

# def sumar_2(un_numero, otro_numero):
#     suma = un_numero + otro_numero
#     print("la suma es:", suma)


# #-------------------

# def sumar_3():
#     un_numero = int(input("ingrese un numero: "))
#     otro_numero = int(input("ingrese otro numero: "))
#     suma = un_numero + otro_numero

#     return suma # no quiero mostrar la suma, la voy a usar para algo. debo guardar el resultado


# #-------------------

# def sumar_4(un_numero, otro_numero):
#     suma = un_numero + otro_numero
#     return suma




# ####################### MAIN #####################

# sumar_1() #llamar la funciom para q haga algo


# #-------------------


# sumar_2(5, 9)

# un_numero = int(input("ingrese un numero: "))
# otro_numero = int(input("ingrese otro numero: "))
# sumar_2(un_numero, otro_numero)

# import random
# un_numero = random.randint()
# otro_numero = random.randint()
# sumar_2(un_numero, otro_numero)


# #-------------------


# resultaedo = sumar_3()
# print("la suma es", resultado)

# if resultado > 20:
#     print("mayor")
# else:
#     print("menor")


# #-------------------

# # SUMAR 4

# resultado_4 = sumar_4(4,2)
# print(resultado_4)
# if resultado_4 == 22:
#     print("el loco")


####--------------------------------------------------

# Ejercicio: Crear una funcion para que al ingresar un numero, nos diga si es par

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


numero = int(input("ingrese un numero: "))
par = es_par(numero)
if par == True:
    print("Es par")
else:
    print("No es par")