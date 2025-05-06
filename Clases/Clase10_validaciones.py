# # Clase 10

# nombre = input("Ingrese el nombre (solo letras y entre 3 y 30 caracteres)")


# # len : mide la cantidad de caracteres

# # Funcion que me devuelve cuantos caracteres tiene el dato que ingresé
# # Sirve para medir el largo de la palabra
# # Solo sirve para string, no números
# cantidad_caracteres = len(nombre) 

# while len(nombre) < 3 or len(nombre) > 30 or not nombre.isalpha():
#     print("Nombre inválido. Inténtelo nuevamente")
#     nombre = input("Ingrese el nombre (solo letras y entre 3 y 30 caracteres)")

# print(f"Nombre guardado: {nombre}")

#     # # para asegurarnos de que todos los caracteres son letras:
#     # if nombre.isalpha: 
#     #     print(f"el nombre ingresado es {nombre}")
#     # else: 
#     #     print("el nombre no puede tener caracteres especiales")

# ##############-------------------------------------------------

# edad = int(input("Ingrese su edad (debe ser un numero entero y comprendido entre 0 y 110 años): "))

# while edad < 0 or edad > 100:
#     print("Edad inválida. Inténtelo nuevamente")
#     edad = int(input("Ingrese su edad (debe ser un numero entero y comprendido entre 0 y 110 años): "))

# Si la persona utiliza una letra, me tira error y no permite volver a ingresar la edad

#--------------------------------------------------------------------

# edad = input("Ingrese su edad (debe ser un numero entero y comprendido entre 0 y 110 años): ")

# while not edad.isdigit():
#     print("Edad no puede contener letras ni caracteres")
#     edad = input("Ingrese su edad (debe ser un numero entero y comprendido entre 0 y 110 años): ")

# if edad.isdigit():
#     edad_numero = int(edad)
#     while edad < 0 or edad > 100:
#         print("Edad inválida. Inténtelo nuevamente")       
#         edad = int(input("Ingrese su edad (debe ser un numero entero y comprendido entre 0 y 110 años): "))

# print(f"{edad_numero}")

# # MUY REPETITIVO.
# # No funciona

#----------------------------------------------------

# es_valido = False

# while not es_valido:
#     edad = input("Ingrese su edad (debe ser un numero entero y comprendido entre 0 y 110 años): ")

#     if edad.isdigit():
#         edad_int = int(edad)
#         if edad > 0 and edad < 110:
#             print(f"Edad: {edad_int}")
#             es_valido = True
#         else:
#             print("La edad debe estar entre 0 y 110 años")
    
#     else:
#         print("Ingresó caracteres inválidos para la edad")


# #--------------------------------------------------------
# tipo_factura = input("Ingrese el tipo de factura (A o B): ").upper()

# while tipo_factura != "A" and tipo_factura != "B":
#     print("Datos incorrectos. Inténtelo nuevamente")
#     tipo_factura = input("Ingrese el tipo de factura (A o B): ").upper()

# print(f"Tipo de factura {tipo_factura}")

#-----------------------------------------------------------


 
# contrasenia_correcta = False
# contrasenia_establecida = ""


# while contrasenia_correcta == False:

#     contrasenia = input("Ingrese la contraseña: ")
#     if contrasenia == contrasenia_establecida:
#         print("Contraseña correcta")
#         contrasenia_correcta = True
#     else:
#         print("Contraseña incorrecta. Vuelva a intentarlo")
#         contrasenia = input("Ingrese la contraseña: ")
# # ?????????????????????????


#---------------------------------------------------------

legajo = int(input("Ingrese su numero de legajo (numero entero de 5 digitos): "))

while legajo < 10000 or legajo > 99999:
    print("El legajo debe tener 5 dígitos")
    legajo = int(input("Ingrese su numero de legajo (numero entero de 5 digitos): "))
print (f"El numero de legajo es {legajo}")


## ----------------------------------------------------------

legajo = int(input("Ingrese su numero de legajo (numero entero de 5 digitos): "))

# while len(legajo) != 5:
#     if legajo.isdigit():
#         legajo = int(legajo)


while len(legajo) != 5 or not legajo.isdigit():
    legajo = int(input("Ingrese su numero de legajo (numero entero de 5 digitos): "))