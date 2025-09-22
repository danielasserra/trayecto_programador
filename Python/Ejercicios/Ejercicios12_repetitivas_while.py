# # Daniela Serra
# # Repetitivas While
# # Ejercicio 07

# # Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).
# # Calcular la suma de los números positivos y el producto de los negativos.

# eleccion = "si"
# suma = 0
# producto = 1
# contador_negativos = 0

# while eleccion == "si":
#     numero = int(input("Ingrese un número: "))
#     if numero > 0:
#         suma += numero
#     else:
#         producto *= numero
#         contador_negativos += 1
#     eleccion = input("¿Desea continuar? ")

# print(f"La suma de los numeros positivos es {suma}")
      
# if contador_negativos > 0:
#     print(f"El producto de los numeros negativos es {producto}")
# else:
#     print("No se ingresaron números negativos")

#--------------------------------------------

# Daniela Serra
# Repetitivas While
# Ejercicio 08

# Ingresar valores de compras hasta que el usuario lo decida. 
# Determinar el 10% del total.

subtotal = 0
eleccion = "si"

while eleccion == "si":
    precio = float(input("Ingrese el precio del producto: $"))
    subtotal += precio
    eleccion = input("¿Desea ingresar otro producto? (si/no) ")

porcentaje = subtotal * 0.1

print(f"El 10% del total es ${porcentaje:.2f}")

#--------------------------------------------

# # Daniela Serra
# # Repetitivas While
# # Ejercicio 09

# # Ingresar 20 números. Determinar el porcentaje de números positivos y negativos ingresados.

# i = 0
# positivos = 0
# negativos = 0

# while i < 20:
#     numero = int(input("Ingrese un número: "))
#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1

#     i += 1

# porcentaje_positivos = (positivos / i) * 100
# porcentaje_negativos = (negativos / i) * 100

# print(f"El porcentaje de numeros positivos es: {porcentaje_positivos}%\n"
#       f"El porcentaje de numeros negativos es: {porcentaje_negativos}%")

#--------------------------------------------

# # Daniela Serra
# # Repetitivas While
# # Ejercicio 10

# # Ingresar números hasta que el usuario lo decida. 
# # Determinar el porcentaje de números positivos y negativos ingresados.

# i = 0
# positivos = 0
# negativos = 0
# eleccion = "si"

# while eleccion == "si":
#     numero = int(input("Ingrese un numero: "))
#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1
#     i += 1
#     eleccion = input("¿Desea ingresar otro número? (si/no) ").lower()

# if i > 0:
#     porcentaje_positivos = (positivos / i) * 100
#     porcentaje_negativos = (negativos / i) * 100

#     print(f"El porcentaje de números positivos es {porcentaje_positivos:.2f}\n"
#           f"El porcentaje de números negativos es {porcentaje_negativos:.2f}")
# else:
#     print("No se ingresaron números")

#--------------------------------------------

# # Daniela Serra
# # Repetitivas While
# # Ejercicio 11

# # Se ingresa la edad y el género (Femenino - Masculino - Otro) de 10 personas. 
# # Determinar:
# #   El promedio de edades de los masculinos.
# #   Porcentaje de personas de cada género.

# i = 0
# f = 0
# m = 0
# o = 0
# edad_m = 0

# while i < 10:
#     edad = int(input("Ingrese la edad: "))
#     genero = input("Ingrese el género (f / m / o): ").lower()
    
#     if genero == "m":
#         m += 1
#         edad_m += edad
#     elif genero == "f":
#         f += 1
#     elif genero == "o":
#         o += 1
    
#     i += 1

# promedio_edad_m = edad_m / m
# porcentaje_femenino = (f / i) * 100
# porcentaje_masculino = (m / i) * 100
# porcentaje_otro = (o / i) * 100

# print(f"El promedio de edades de los masculinos es {promedio_edad_m}\n"
#       f"El porcentaje de personas de cada género es:\n"
#       f"Femenino: {porcentaje_femenino:.2f}%\n"
#       f"Masculino: {porcentaje_masculino:.2f}%\n"
#       f"Otro: {porcentaje_otro}%\n")

#--------------------------------------------

# Daniela Serra
# Repetitivas While
# Ejercicio 12

# Ingresar 10 números enteros. Determinar el máximo y el mínimo.

# ----------  OPCION 1  -------------

i = 0
bandera_primera_vez = True

while i < 10:
    numero = int(input("Ingrese un numero: "))
    if bandera_primera_vez == True:
        maximo = numero
        minimo = numero
        bandera_primera_vez = False

    if maximo < numero:
        maximo = numero
    
    if minimo > numero:
        minimo = numero

    i += 1

print(f"El número máximo es {maximo} y el mínimo es {minimo}")

# ----------  OPCION 2  -------------

i = 0
maximo = None
minimo = None

while i < 10:
    numero = int(input("Ingrese un numero: "))

    if maximo == None or maximo < numero:
        maximo = numero
    if minimo == None or minimo > numero:
        minimo = numero
    
    i += 1

print(f"El numero maximo ingresado es: {maximo} y el numero minimo es: {minimo}")