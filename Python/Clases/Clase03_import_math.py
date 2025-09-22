# # # Daniela Serra
# # E_S 11

#Realizar un programa que calcule la superficie de un círculo, dado el ingreso del radio.

# import math

# #entrada: radio
# #PI = 3.14
# radio = int(input("Ingrese un numero: "))

# #proceso: PI * r2
# superficie = math.pi * math.pow(radio, 2) # exponencial // radio ** 2
# #Calcular el perímetro.
# perimetro = 2 * math.pi * radio #propiedad conmutativa

# #salida: superficie del círculo
# print(f"La superficie del círculo es: {superficie}")
# print(f"El perímetro del círculo es: {perimetro:.2f}") #. Para que calcule solo dos decimales, dar formato en el print  :.2f significa que muestro dos decimales después de la coma


##########################################

#Investigar: qué es una constante y en qué se diferencia de una variable
#Biblioteca math de Python.


########################################

# Daniela Serra
# E_S 12

# A partir del ingreso de los dos catetos de un triángulo rectángulo, 
# calcular el valor de la hipotenusa.

# import math

# cateto_mayor = float(input("Ingrese el cateto mayor: "))
# cateto_menor = float(input("Ingrese el cateto menor: "))

# hipotenusa = raiz cuadrada de cateto_mayor al cuadrado + cateto_menor al cuadrado
# raiz cuadrada = potencia 0.5
# hipotenusa_sin_math = (cateto_mayor ** 2 + cateto_menor ** 2) ** 0.5
# hipotenusa_con_math = math.sqrt (pow(cateto_mayor, 2) + pow(cateto_menor, 2))
# sqrt = Square root = raiz cuadrada

# codigo prolijo = crear una variable que sume ambos catetos al cuadrado 
# suma_cuadrado_catetos = pow(cateto_menor,2) + pow(cateto_mayor,2)
# hipotenusa_variable = math.sqrt (suma_cuadrado_catetos)

# print(hipotenusa_sin_math)
# print(hipotenusa_con_math)
# print(hipotenusa_variable)

#####################################################
# Daniela Serra
# E_S 13

# Realizar un programa que calcule el promedio de un alumno, 
# a partir del ingreso de su nombre, apellido, 3 notas y 
# que muestre al final las leyendas pertinentes.  

# nombre_y_apellido = input("Ingrese nombre y apellido del alumno: ")

# primer_nota = float(input("Ingrese una calificación: "))
# segunda_nota = float(input("Ingrese otra calificación: "))
# tercera_nota = float (input("Ingrese otra calificación: "))

# promedio = (primer_nota + segunda_nota + tercera_nota)/3

# print(f"El promedio del alumno {nombre_y_apellido} es {promedio:.2f}")
#############################################}

# Daniela Serra
# E_S 14

# Realizar un programa que a partir del ingreso del sueldo de un empleado, 
# muestre dicho valor con un descuento del 15%.

sueldo = float(input("Ingrese el sueldo del empleado: "))

desc = (15*sueldo)/100
#otra forma
desc = sueldo * 0.15

sueldo_desc = sueldo - desc
#otra forma
sueldo_desc = sueldo * 0.85
# si en lugar de descontar el porcentaje, lo sumo
#(EJ. si hago compra al exterior, me cobran 15% de impuestos)
# sueldo_desc = sueldo*1.15


print(f"El sueldo del empleado con descuento del 15% es {sueldo_desc}")


