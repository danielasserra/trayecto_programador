# # Daniela Serra
# # Repetitivas While - Validaciones
# # Ejercicio 13
# 
# # Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. 
# # Tendrá intentos indeterminados.

# clave_correcta = int(input("Elija su clave numérica: "))

# clave_ingresada = int(input("Ingrese su clave: "))

# while clave_ingresada != clave_correcta:
#     print("Clave incorrecta. Inténtelo nuevamente")
#     clave_ingresada = int(input("Ingrese su clave: "))

# print("¡Clave correcta! Acceso concedido")

#--------------------------------------------------

# # Daniela Serra
# # Repetitivas While - Validaciones
# # Ejercicio 14

# # Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. 
# # Solo tendrá 3 intentos.

# i = 0

# clave_correcta = int(input("Elija su clave numérica: "))

# clave_ingresada = int(input("Ingrese su clave: "))

# while i < 3:
#     if clave_correcta != clave_ingresada:
#         print("La clave ingresada es incorrecta. Inténtelo nuevamente")
#         clave_ingresada = int(input("Ingrese su clave: "))
#     else:
#         print("¡Clave correcta! Acceso concedido")
    
#     i += 1

# if clave_correcta != clave_ingresada:
#     print("Ha alcanzado la cantidad máxima de intentos permitidos.\n"
#           "Comuníquese con su proveedor para reestablecer la contraseña")

#--------------------------------------------------

# # Daniela Serra
# # Repetitivas While - Validaciones
# # Ejercicio 15

# Pedir al usuario el ingreso de una nota. 
# La misma debe estar comprendida entre 1 y 10 inclusive.

nota = input("Ingrese la nota: ")
nota = int(nota)

while nota < 1 or nota > 10:
    print("Nota incorrecta. Inténtelo nuevamente")
    nota = input("Ingrese la nota: ")
    nota = int(nota)

print("Nota ingresada")