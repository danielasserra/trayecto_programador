# from colorama import *

# color = input("Ingrese un color: ")

# if color == "rojo":
#     print(Fore.RED + "ROJO")
# if color == "azul":
#     print(Fore.BLUE + "AZUL")
# if color == "verde":
#     print(Fore.GREEN + "VERDE")

# # EFICIENCIA VS EFICACIA

# if color == "rojo":
#     print(Fore.RED + "ROJO")
# else:
#     if color == "azul":
#         print(Fore.BLUE + "AZUL")
#     else:
#         print(Fore.GREEN + "VERDE")

# # Con esta estructura evitamos que el procesador haga preguntas 
# # redundantes o sin sentido porque son mutuamente excluyentes. 
# # Si funciona ROJO sale del programa. Si no, busca nuevamnete. 
# # Si funciona AZUL no chequea else.

# # ELIF

# if color == "rojo":
#     print(Fore.RED + "ROJO")
# elif color == "azul":
#     print(Fore.BLUE + "AZUL")
# elif color == "amarillo":
#     print(Fore.YELLOW + "AMARILLO")
# else:
#     print(Fore.GREEN + "VERDE")


# match color:
#     case "rojo":
#         print(Fore.RED + "ROJO")
#     case "azul":
#         print(Fore.BLUE + "AZUL")
#     case _: #"verde": (es el caso default, no está el dato validado, 
#             # si ingresan cualquier cosa, que no sea los casos anteriores sale esta respuesta)
#         print(Fore.GREEN + "VERDE")

#############################################

# Daniela Serra
# Condicionales
# Ejercicio 7
# Pedirle al usuario su edad, determinar si es mayor 
# (18 años o más), niño/a (menor de 10), pre-adolescente 
# (edad entre 10 y 13 años inclusive) o adolescente 
# (edad entre 13 y 17 años).

# edad = int(input("Ingrese su edad: "))
    
# if edad < 10:
#     print("Niño/a")
# elif edad >= 10 and edad <=13:
#     print("Es preadolescente")
# elif edad <= 17: # edad >13 and edad <= 17:
#     print("Es adolescente")
# else:
#     print("UD es mayor de edad")

# Evitar preguntar dos veces por lo mismo
# Evitar preguntar lo que no se cumplió antes.
# Ej. >13 and edad <= 17
# Ordenar segun el contexto 
# x ej. en una primaria empezar por edad 10,
# en universidad empezar x 18.

######################################

# Daniela Serra
# Condicionales
# Ejercicio 8
# A partir del ingreso de la altura en centímetros de un jugador 
# de baloncesto, el programa deberá determinar la posición del 
# jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

# altura = float(input("Ingrese la altura en cm: "))

# if altura < 160:
#     print("Base")
# elif altura <= 179:
#     print("Escolta")
# elif altura <= 199:
#     print("Alero")
# else:
#     print("Ala-Pivot o Pivot")

# Tarea: Cómo generar un número aleatorio
# Cómo generar un numero aleatorio entre 1 y 10
# Intentar hacer todos los ejercicios de condicionales

