# GUIA CONDICIONALES
# 
# # Daniela Serra
# # IF 8

# # A partir del ingreso de la altura en centímetros de un jugador de baloncesto, 
# # el programa deberá determinar la posición del jugador en la cancha, considerando 
# # los siguientes parámetros:
# # Menos de 160 cm: Base
# # Entre 160 cm y 179 cm: Escolta
# # Entre 180 cm y 199 cm: Alero
# # 200 cm o más: Ala-Pívot o Pívot

# altura = float(input("Ingrese la altura en cm: "))

# if altura < 160:
#     print("Base")

# if altura >= 179:
#     print("Escolta")

# if altura >= 199:
#     print("Alero")

# if altura >= 200:
#     print("Ala-Pivot o Pivot")

################################################

# # Daniela Serra
# # CONDICIONALES EJERCICIO 9

# # Los argentinos nativos y por opción desde los dieciséis (16) años 
# # y los argentinos naturalizados desde los dieciocho (18) años 
# # están habilitados a votar. A partir del ingreso de la edad del 
# # usuario y el estado (si es naturalizado o nativo), se deberá informar 
# # si es o no posible que la persona concurra a votar en base a la 
# # información suministrada.

# edad = int(input("Ingrese su edad: "))
# estado = input("¿Es usted nativo o naturalizado? ")

# if (edad >= 16 and estado == "nativo") or (edad >= 18 and estado == "naturalizado"):
#     print("La persona puede concurrir a votar")
# else:
#     print ("La persona no puede concurrir a votar")

###############################

# # Daniela Serra
# # CONDICIONALES EJERCICIO 10

# # Ingresar el sueldo, estado civil (casado o soltero) y cantidad de 
# # hijos de un empleado. Determinar si el empleado debe o no pagar el 
# # impuesto a las ganancias. El mismo no se pagará si el empleado es 
# # casado con hijos y sus ingresos son menores a $2200000.

# sueldo = float(input("Ingrese el sueldo: "))
# estado_civil = input("Ingrese su estado civil (casado o soltero): ")
# hijos = int(input("Ingrese la cantidad de hijos que tiene: "))

# if estado_civil == "casado" and hijos > 0 and sueldo < 2200000:
#     print("El empleado no paga impuesto a las ganancias")
# else:
#     print("El empleado paga impuesto a las ganancias")

####################################

# # Daniela Serra
# # CONDICIONALES EJERCICIO 11

# import random

# numero = random.randint(1,10)

# print(numero)

#####################################

# Daniela Serra
# CONDICIONALES EJERCICIO 12

# Calcular una nota aleatoria entre el 1 y el 10 inclusive, 
# para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota es ...

import random 
nota = random.randint(1, 10)

# Opcion 1
if nota >= 6:
    print(f"Promoción directa, la nota es {nota}")
elif nota >= 4:
    print(f"Aprobado, la nota es {nota}")
else:
    print(f"Desaprobado, la nota es {nota}")

# Opcion 2

if nota >= 6:
    mensaje="Promoción directa"
elif nota >= 4:
    mensaje= "Aprobado"
else:
    mensaje= "Desaprobado"

print(f"{mensaje}. La nota es {nota}")

# Opcion 3

match nota:
    case n if n >= 6:
        print(f"Promoción directa, la nota es {nota}")
    case n if n >= 4:
        print(f"Aprobado, la nota es {nota}")
    case _:
        print(f"Desaprobado, la nota es {nota}")

##################################

