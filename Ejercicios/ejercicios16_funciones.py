# # Daniela Serra
# # Funciones. Ejercicio 1

# # Escribir una función que calcule el área de un rectángulo. 
# # La función recibe la base y la altura y retorna el área. 

# def area_rectangulo(base, altura):
#     area = base * altura
#     return area

# # Llamar funcion
# base = int(input("base: "))
# altura = int(input("altura: "))
# print(area_rectangulo(base, altura))

# #-------------------------------------------

# # Daniela Serra
# # Funciones. Ejercicio 2

# # Escribe una función que calcule el área de un círculo. 
# # La función debe recibir el radio como parámetro y devolver el área.
# import math

# def calcular_area_circulo(radio):
#     resultado = math.pi * radio ** 2
#     return resultado

# # Llamar funcion
# radio = int(input("radio: "))
# print(f"{(calcular_area_circulo(radio)):.2f}")

#-------------------------------------------

# Daniela Serra
# Funciones. Ejercicio 3

# Crea una función que verifique si un número dado es par o impar. 
# La función debe imprimir un mensaje indicando si el número es par o impar.

def par_o_impar(numero):
    if numero % 2 == 0:
        mensaje = "Es par"
    else:
        mensaje = "Es impar"
    
    return mensaje

# Llamar funcion

numero = int(input("ingrese un numero: "))
print(par_o_impar(numero))

#-------------------------------------------

# Daniela Serra
# Funciones. Ejercicio 3

# Crea una función que verifique si un número dado es par o impar. 
# La función retorna True si el número es par, False en caso contrario.


