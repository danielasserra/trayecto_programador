# CONDICIONALES
# ANEXO
# 
# EJERCICIO 1
#
# Escribe un programa que pregunte al usuario su edad y 
# si tiene licencia de conducir. Si la edad es mayor o igual a 18 y 
# tiene licencia de conducir, muestra un mensaje que diga "Puedes conducir". 
# De lo contrario, muestra un mensaje que diga "No puedes conducir".

# edad = int(input("Ingrese su edad: "))
# registro = input("¿Tiene registro? (si o no): ")

# if edad >= 18 and registro == "si":
#     print("Usted puede conducir")
# else:
#     print("Usted no puede conducir")

################################################3

# EJERCICIO 2
#Escribe un programa que pregunte al usuario si tiene un título universitario 
# o si tiene experiencia laboral. Si tiene un título universitario o experiencia 
# laboral, muestra un mensaje que diga "Eres elegible para el trabajo". 
# De lo contrario, muestra un mensaje que diga "No eres elegible para el trabajo".

# titulo_universitario = input("¿Tiene Título Universitario? (si o no): ")
# experiencia_laboral = input("¿Tiene experiencia laboral? (si o no): ")

# if titulo_universitario == "si" or experiencia_laboral == "si":
#     print("Eres elegible para el trabajo")
# else:
#     print("No eres elegible para el trabajo")

#############################################

# EJERCICIO 3
#Escribe un programa que pregunte al usuario si es un estudiante 
# regular. Si no es un estudiante regular, muestra un mensaje que 
# diga "Debes ser un estudiante regular para acceder a este recurso". 
# De lo contrario, muestra un mensaje que diga "Acceso permitido".

# estudiante_regular = input("¿es estudiante regular? (si o no): ")

# if not estudiante_regular == "si":
#     #estudiante_regular != "si"
#     print("Debes ser un estudiante regular para acceder a este recurso")
# else:
#     print("Acceso permitido")

##############################################

# EJERCICIO 4
# Escribe un programa que pregunte al usuario su edad, 
# si tiene licencia de conducir y si tiene un título universitario. 
# Si la edad es mayor o igual a 18, tiene licencia de conducir y 
# tiene un título universitario, muestra un mensaje que diga 
# "Eres elegible para el trabajo y puedes conducir". 
# De lo contrario, muestra un mensaje que diga "No eres elegible 
# para el trabajo o no puedes conducir".

# edad = int(input("Edad: "))
# registro = input("¿Tenes licencia de conducir? (si o no): ")
# titulo_universitario = input("¿Tiene Título Universitario? (si o no): ")

# if edad >= 18 and registro == "si" and titulo_universitario == "si":
#     print("Eres elegible para el trabajo y puedes conducir")
# else:
#     print("No eres elegible para el trabajo o no puedes conducir")

################################################

# EJERCICIO 5

# Escribe un programa que reciba dos números y determine si:
# o    Ambos números son positivos. Si ambos números son 
# positivos, imprimir "Ambos positivos".
# o    Al menos uno de los dos números es negativo. Si al 
# menos uno de los dos números es negativo, imprimir 
# "Al menos uno negativo".
# o    Ninguno de los dos números es cero. Si ninguno de los 
# dos números es cero, imprimir "Ningún número es cero".

# primer_numero = float(input("Ingrese un numero: "))
# segundo_numero = float(input("Ingrese otro numero: "))

# if primer_numero > 0 and segundo_numero > 0:
#     print("Ambos positivos")
# if primer_numero < 0 or segundo_numero < 0:
#     print("Al menos uno es negativo")
# if not primer_numero == 0 and not segundo_numero == 0:
#     # primer_numero != 0 and segundo_numero != 0:
#     print("Ningun numero es cero")

################################

# EJERCICIO 6

#  Un banco quiere desarrollar un sistema de evaluación de crédito 
# para determinar si un cliente es elegible para un préstamo. 

# DATOS INGRESADOS POR EL CLIENTE
# # 
# #  Edad del cliente (mayor o igual a 25 años)
# edad = int(input("Ingrese su edad: ")) 

# # Ingreso mensual del cliente (mayor o igual a $3,000)
# ingreso = float(input("¿Cual es su ingreso mensual? ")) 

# # Historial crediticio del cliente (bueno o malo)
# historial = input("¿cuál es su historial crediticio? (bueno o malo): ")

# # Tipo de empleo del cliente (empleado o empresario)
# empleo = input("¿Cuál es su tipo de empleo? (empleado o empresario): ")

# # # El sistema debe asignar un puntaje de crédito basado en los 
# # # siguientes criterios:

# puntaje = 0

# # # Edad: 10 puntos si el cliente tiene 25 años o más, 
# # # # 0 puntos de lo contrario
# # if edad >= 25:
# #     puntos_edad = 10
# # else:
# #     puntos_edad = 0

# if edad >= 25:
#     puntaje += 10

# # # Ingreso mensual: 20 puntos si el cliente tiene un ingreso 
# # # mensual de $3,000 o más, 0 puntos de lo contrario

# # if ingreso >= 3000:
# #     puntos_ingreso = 20
# # else:
# #     puntos_ingreso = 0

# if ingreso >= 3000:
#     puntaje += 20

# # # Historial crediticio: 30 puntos si el cliente tiene un 
# # # historial crediticio bueno, 0 puntos de lo contrario

# # if historial == "bueno":
# #     puntos_historial = 30
# # else: 
# #     puntos_historial = 0

# if historial == "bueno":
#     puntaje += 30

# # # Tipo de empleo: 40 puntos si el cliente es empleado, 
# # # 20 puntos si es empresario

# # if empleo == "empleado":
# #     puntos_empleo = 40
# # if empleo == "empresario":
# #     puntos_empleo = 20

# if empleo == "empleado":
#     puntaje += 40
# else:
#     puntaje += 20

# # # Si el cliente suma 40 punto o más “Está aprobado para recibir 
# # # el crédito”, de lo contrario “No tiene un crédito preaprobado”

# # credito = puntos_edad + puntos_ingreso + puntos_historial + puntos_empleo

# # if credito >= 40:
# #     print("Está aprobado para recibir el crédito")
# # else:
# #     print("No tiene un credito")

# if puntaje >= 40:
#     print("Está aprobado para recibir el crédito")
# else:
#     print("No tiene un crédito preaprobado")


###############################

# EJERCICIO 7

#   (versión con operadores lógicos) Un banco quiere desarrollar un sistema de 
# evaluación de crédito para determinar si un cliente es elegible para un préstamo.

# DATOS INGRESADOS POR EL CLIENTE

# # Edad del cliente (mayor o igual a 25 años)
# edad = int(input("Ingrese su edad: ")) 

# # Ingreso mensual del cliente (mayor o igual a $3,000)
# ingreso = float(input("¿Cual es su ingreso mensual? ")) 

# # Historial crediticio del cliente (bueno o malo)
# historial = input("¿cuál es su historial crediticio? (bueno o malo): ")

# # Tipo de empleo del cliente (empleado o empresario)
# empleo = input("¿Cuál es su tipo de empleo? (empleado o empresario): ")

# # El sistema debe determinar si el cliente es elegible para un préstamo basado en 
# # las siguientes condiciones:

# # Si el cliente tiene 25 años o más y un ingreso mensual de $3,000 o más, 
# # es elegible para un préstamo

# if edad >= 25 and ingreso >= 3000:
#     print("Es elegible para un préstamo")

# # Si el cliente tiene un historial crediticio bueno o es un empresario, 
# # es elegible para un préstamo con una tasa de interés más baja

# if historial == "bueno" or empleo == "empresario":
#     print("Es elegible para un préstamo con tasa de interes más baja")

# # Si el cliente no cumple con ninguna de las condiciones anteriores, 
# # no es elegible para un préstamo

# if not edad >= 25 or not ingreso >= 3000 or not historial == "bueno" or not empleo == "empresario":
#     print("No es elegible para el préstamo")


