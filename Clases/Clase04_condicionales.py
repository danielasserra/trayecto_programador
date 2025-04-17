# Condicionales

# if condicion:
#     sentencias # se van a ejecutar si la condicion es verdadera


# valor = 5 > 3
# print(type(valor))
# print(valor)

# numero_uno = 6
# numero_dos = 3

# if numero_uno > numero_dos :
#     print("Es mayor")
# else:
#     print("Es menor o igual")

########################################

# Daniela Serra
# Condicionales
# Ejercicio 1. 
# 
# A partir del ingreso de una edad, 
# si coincide con 18, mostrar "Usted tiene 18 años"

# edad = int(input("Ingrese su edad: "))
# if edad == 18:
#     print("Usted tiene 18 años")

###################################

# # Daniela Serra
# # Condicionales
# # # Ejercicio 2. 
# # # 
# # # A partir del ingreso de una edad, 
# # # determinar si la persona es mayor de edad. Si es mayor o igual que 18, 
# # # momstrará el mensaje "Usted es mayor de edad"

# edad = int(input("Ingrese su edad: "))
# if edad >= 18:
#     print("Usted es mayor de edad")

#################################

# Daniela Serra
# Condicionales
# Ejercicio 3: 
# 
# A partir del ingreso de una edad, determinar 
# si la persona es mayor de edad o no. Si es mayor de 18 
# se mostrará el mensaje “UD ES MAYOR DE EDAD” caso contrario 
# “UD ES MENOR DE EDAD”.

# edad = int(input("Ingrese su edad: "))
# if edad >= 18:
#     print("UD es mayor de edad")
# else:
#     print("UD es menor de edad")

##################################

# Daniela Serra
# Condicionales
# Ejercicio 4: 
# 
# A partir del ingreso de la altura de un 
# basquetbolista determinar si es pivot o no. 
# Para serlo el mismo deberá medir más de 1.80 metros.

# altura = float(input("Ingrese la altura del basquetbolista: "))
# if altura >= 1.80:
#     print("Es pivot")

######################

# Daniela Serra
# Condicionales
# Ejercicio 5: 
# 
# Pedirle al usuario su edad, determinar 
# si el usuario es adolescente (edad entre 13 y 17 inclusive)

# adolescente = int(input("Ingrese su edad: "))
# if adolescente >= 13 and adolescente <= 17:
#     print("Usted es adolescente")
# else:
#     print("Ud. no es adolescente")

##################################

# # Daniela Serra
# # Condicionales
# # Ejercicio 6: 
# # 
# # Pedirle al usuario su edad, 
# # determinar si el usuario NO es adolescente.

# no_adolescente = int(input("Ingrese su edad: "))
# if no_adolescente <=13 or no_adolescente >= 17:
#     print("Ud no es adolescente")
# else:
#     print("ud es adolescente")


##################################

# Daniela Serra
# Condicionales
# Ejercicio 7
# Pedirle al usuario su edad, determinar si es mayor 
# (18 años o más), niño/a (menor de 10), pre-adolescente 
# (edad entre 10 y 13 años inclusive) o adolescente 
# (edad entre 13 y 17 años).

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("UD es mayor de edad")
if edad < 10:
     print("Ud es niño/a")
if edad >= 10 and edad <= 13:
    print("Ud es preadolescente")
if edad >13 and edad <=17:
    print("Usted es adolescente")