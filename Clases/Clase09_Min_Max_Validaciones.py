# # Clase 9
# # Maximos y Minimos

# minimo = -1000
# maximo = 1000
# i = 0

# while i < 3:
#     numero = int(input("Ingrese un numero: "))

#     if numero > maximo:
#         maximo = numero

#     if numero < minimo:
#         minimo = numero

#     i += 1

# print(f"{maximo} y {minimo}")

# # Inicializar variables con max y min relativos es incorrecto porque me puedo ir de rango

#-------------------------------
# minimo = float("inf")
# maximo = float("inf")
# i = 0

# while i < 3:
#     numero = int(input("Ingrese un numero: "))

#     if numero > maximo:
#         maximo = numero

#     if numero < minimo:
#         minimo = numero

#     i += 1

# print(f"{maximo} y {minimo}")

# # qué vale inf?
# # qué pasa si cambio de lenguaje?

#--------------------------------

# numero = int(input("Ingrese un numero: "))

# minimo = numero
# maximo = numero
# i = 0

# while i < 3:
#     numero = int(input("Ingrese un numero: "))

#     if numero > maximo:
#         maximo = numero

#     if numero < minimo:
#         minimo = numero

#     i += 1

# print(f"{maximo} y {minimo}")

# # Cumple el objetivo pero al analizar lo que hacen, no cierra
# # Repite código

# -----------------------------------

# i = 0

# while i < 3:
#     numero = int(input("Ingrese un numero: "))

#     if i == 0: # Esto es redundante, sólo se cumplirá la primera vez
#         maximo = numero
#         minimo = numero
#     else:
#         if numero > maximo:
#             maximo = numero

#         if numero < minimo:
#             minimo = numero

#     i += 1

# print(f"{maximo} y {minimo}")

# # Está bastante bien, el impacto es mínimo, pero se puede hacer mejor

# #---------------------------------------------

# i = 0

# while i < 3:
#     numero = int(input("Ingrese un numero: "))
    
#     if i == 0 or numero > maximo:
#         maximo = numero

#     if i == 0 or numero < minimo:
#         minimo = numero

#     i += 1

# print(f"{maximo} y {minimo}")

# # equivalente al anterior pero más corto
# # mejora el algoritmo anterior
# # mantiene redundancia en la pregunta

#----------------------------------------

# minimo = 0
# maximo = 0
# i = 0

# while i < 3:
#     numero = int(input("Ingrese un numero: "))
    
#     if numero > maximo or i == 0:
#         maximo = numero

#     if numero < minimo or i == 0:
#         minimo = numero

#     i += 1

# print(f"{maximo} y {minimo}")

# # -------------------------------

# minimo = 0
# maximo = 0

# i = 0
# bandera_primero = False

# while i < 3:
#     numero = int(input("Ingrese un numero: "))
    
#     if numero > maximo or bandera_primero == False:
#         maximo = numero

#     if numero < minimo or bandera_primero == False:
#         minimo = numero
    
#     bandera_primero = True

#     i += 1

# print(f"{maximo} y {minimo}")

# -----------------------------------------------------

# # VALIDACIONES

# # Asegurarnos que dentro de la variable tendremos un valor adecuado
# # dentro del contexto en el que se desarrolla esa variable

# # OPCION 1
# clave = input("Ingrese la clave: ") #CFP6
# while clave != "CFP6": # Tengo que preguntar por lo que no quiero que ocurra
#     clave = input("Reingrese la clave: ")

# # OPCION 2
# clave = input("Ingrese la clave: ") #CFP6
# while not (clave == "CFP6"): # Tengo que preguntar por lo que no quiero que ocurra
#     clave = input("Reingrese la clave: ")

# print("Bienvenido")

# # -------------------------------------------------

nota = int(input("Ingrese nota: "))

while nota < 1 or nota > 10:
    nota = int(input("Reingrese nota: "))

#-----------------------------------------------

color = input("ingrese un color (rojo, azul, amarillo): ")

while color != "rojo" and color != "azul" and color != "amarillo":
    color = input("reingrese un color (rojo, azul, amarillo): ")


# Tarea: Guia completa. Integradores.