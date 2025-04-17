# # Daniela Serra
# # Condicionales ANEXO
# # Ejercicio 8

# # Escribe un programa que pregunte al usuario su edad,
# # si tiene entrada y si está acompañado por un adulto. 

# edad= int(input("Ingrese su edad: "))
# entrada = input("¿Tiene entrada? (si / no): ")
# acompañado = input("¿Lo acompaña un adulto? (si/no): ")
# # Si tiene 15 años o más y tiene entrada, o si está acompañado, 
# # muestra un mensaje que diga "Puedes ingresar al evento". 
# # De lo contrario, # muestra "No puedes ingresar al evento".

# if edad >= 15 and entrada == "si" or acompañado == "si":
#     print("Puedes ingresar al evento")
# else:
#     print("No puedes ingresar al evento")

#----------------------------------------------------------------

# # Daniela Serra
# # Condicionales ANEXO
# # Ejercicio 9

# # Escribe un programa que pregunte al usuario si tiene cuenta bancaria, 
# # si está verificada y si tiene saldo disponible. Si tiene cuenta verificada y 
# # saldo mayor a cero, muestra "Puedes realizar compras". Si tiene cuenta pero 
# # no verificada, muestra "Debes verificar tu cuenta". En cualquier otro caso,
# # muestra "No tienes una cuenta válida".

# cuenta = input("¿tiene cuenta bancaria? (si/no): ").title()
# verificada = input("su cuenta está verificada? (si/no): ").title()
# 

# if cuenta == "Si" and verificada == "Si" and saldo == "Si":
#     print("Puedes realizar compras")
# elif cuenta == "Si" and verificada == "No" and saldo == "Si":
#     print("Debes verificar tu cuenta")
# else:
#     print("No tienes una cuenta válida")

#-----------------------------------------------------------------

# # Daniela Serra
# # Condicionales ANEXO
# # Ejercicio 10

# # Escribe un programa que pregunte al usuario tres notas 
# # (del 1 al 10). Si las tres son mayores o iguales a 6, 
# # mostrar "Promocionás la materia". 
# # Si al menos una es menor a 4, mostrar "Desaprobado". 
# # En cualquier otro caso, mostrar "Regular".

# primera_nota = int(input("Ingrese una nota: "))
# segunda_nota = int(input("Ingrese otra nota: "))
# tercera_nota = int(input("Ingrese uotra nota mas: "))

# if primera_nota >= 6 and segunda_nota >= 6 and tercera_nota >= 6:
#     print("Promocionás la materia")
# elif primera_nota < 4 or segunda_nota < 4 or tercera_nota < 4:
#     print("Desaprobado")
# else:
#     print("Regular")

#-------------------------------------------------------------------

# # Daniela Serra
# # Condicionales ANEXO
# # Ejercicio 11

# # Escribe un programa que pregunte si el usuario quiere ver una película (sí o no), 
# # y si tiene saldo en su cuenta. Si responde que sí y tiene saldo, mostrar 
# # "Reproduciendo película". Si responde que sí pero sin saldo, mostrar 
# # "Saldo insuficiente". Si responde que no, mostrar "Película no seleccionada".

# pelicula = input("¿Quiere ver una película? (si/no): ").title()
# saldo = input("¿tiene saldo? (si/no): ").title()

# if pelicula == "Si" and saldo == "Si":
#     print("Reproduciendo película")
# elif pelicula == "Si" and saldo == "No":
#     print("Saldo insuficiente")
# else:
#     

#-------------------------------------------------------------------

# # Daniela Serra
# # Condicionales ANEXO
# # Ejercicio 12

# Escribe un programa que pregunte al usuario si tiene pase sanitario y 
# si tiene entrada para un concierto. Si tiene ambos, mostrar "Acceso total". 
# Si tiene entrada pero no pase, mostrar "No puedes ingresar sin pase". 
# Si no tiene entrada, mostrar "Debes comprar una entrada".

pase_sanitario = input("¿Tiene pase sanitario? (si/no): ").title()
entrada = input("¿Tiene entrada para el concierto? (si/no): ").title()

if pase_sanitario == "Si" and entrada == "Si":
    print("Acceso total")
elif pase_sanitario == "No" and entrada == "Si":
    print("No puedes ingresar sin pase")
else:
    print("Debes comprar una entrada")
