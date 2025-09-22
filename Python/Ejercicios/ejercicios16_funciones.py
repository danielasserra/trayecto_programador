# # Daniela Serra
# # Funciones. Ejercicio 1

# # Escribir una función que calcule el área de un rectángulo. 
# # La función recibe la base y la altura y retorna el área. 

# def calcular_area_rectangulo(base:int, altura:int):
#     """La FN calcula el area de un rectangulo

#     Args:
#         base (int): numero de base del rectangulo
#         altura (int): numero de altura del rectangulo

#     Returns:
#         int: area del rectangulo
#     """
#     area = base * altura
#     return area
    
# # Llamar funcion
# base = int(input("base: "))
# altura = int(input("altura: "))
# print(calcular_area_rectangulo(base, altura))

# #-------------------------------------------

# # Daniela Serra
# # Funciones. Ejercicio 2

# # Escribe una función que calcule el área de un círculo. 
# # La función debe recibir el radio como parámetro y devolver el área.
# import math

# def calcular_area_circulo(radio:int):
#     """La FN calcula el area de un circulo


#     Args:
#         radio (int): numero del radio

#     Returns:
#          int: el area del circulo

#     """
#     resultado = math.pi * radio ** 2
#     return resultado

# # Llamar funcion
# radio = int(input("radio: "))
# print(f"{(calcular_area_circulo(radio)):.2f}")

# #-------------------------------------------

# # Daniela Serra
# # Funciones. Ejercicio 3

# # Crea una función que verifique si un número dado es par o impar. 
# # La función debe imprimir un mensaje indicando si el número es par o impar.

# def par_o_impar(numero:int):
#     """la función verifica si un número dado es par o impar

#     Args:
#         numero (int): numero ingresado por el usuario

#     Returns:
#         str: informa si es par o impar
#     """
#     if numero % 2 == 0:
#         mensaje = "Es par"
#     else:
#         mensaje = "Es impar"
    
#     return mensaje

# # Llamar funcion

# numero = int(input("ingrese un numero: "))
# print(par_o_impar(numero))

# #-------------------------------------------

# # Daniela Serra
# # Funciones. Ejercicio 4

# # Crea una función que verifique si un número dado es par o impar. 
# # La función retorna True si el número es par, False en caso contrario.

# def par_o_impar_booleano(numero:int):
#     """la función verifica si un número dado es par o impar

#     Args:
#         numero (int): numero ingresado por el usuario

#     Returns:
#         bool: True es par, false es impar
#     """
#     if numero % 2 == 0:
#         mensaje = True
#     else:
#         mensaje = False
#     return mensaje

# # Llamar función
# numero = 7
# print(par_o_impar_booleano(numero))

# #-------------------------------------------

# # Daniela Serra
# # Funciones. Ejercicio 5

# # Define una función que encuentre el máximo de tres números. 
# # La función debe aceptar tres argumentos y devolver el número más grande.

# def calcular_valor_maximo(un_numero:int, otro_numero:int, otro_numero_mas:int):
#     """Define una función que encuentre el máximo de tres números.

#     Args:
#         un_numero (int): numero ingresado por el usuario
#         otro_numero (int): numero ingresado por el usuario
#         otro_numero_mas (int): numero ingresado por el usuario

#     Returns:
#         int: devuelve el numero mas grande de los tres
#     """
#     if un_numero > otro_numero and un_numero > otro_numero_mas:
#         mas_grande = un_numero
#     elif otro_numero > un_numero and otro_numero > otro_numero_mas:
#         mas_grande = otro_numero
#     elif otro_numero_mas > otro_numero and otro_numero_mas > un_numero:
#         mas_grande = otro_numero_mas
#     return mas_grande

# # # Llamar función

# un_numero = 5
# otro_numero = 60
# otro_numero_mas = 27
# print(calcular_valor_maximo(un_numero, otro_numero, otro_numero_mas))

##-------------------------------------------

# # Daniela Serra
# # Funciones. Ejercicio 6

# # Diseña una función que calcule la potencia de un número. 
# # La función debe recibir la base y el exponente como argumentos y devolver el resultado.

# def potenciar_el_numero(numero:int):
#     """función que calcule la potencia de un número.

#     Args:
#         numero (int): numero ingresado por el usuario

#     Returns:
#         int: la potencia del numero ingresado
#     """
#     resultado = numero ** 2
#     return resultado

# # Llamar función
# numero = 8
# print(potenciar_el_numero(numero))

#-------------------------------------------

# # Daniela Serra
# # Funciones. Ejercicio 7

# # Opcion 1

# def verificar_primo(numero:int):
#     """Crear una función que reciba un número y retorne 
#     True si el número es primo, False en caso contrario.

#     Args:
#         numero (int): numero ingresado por el usuario

#     Returns:
#         bool: True si el número es primo, False en caso contrario
#     """
#     contador_divisores = 0
#     for i in range (1, (numero + 1)):
#         if numero % i == 0:
#             contador_divisores += 1
#     if contador_divisores == 2:
#         es_primo = True
#     else:
#         es_primo = False
    
#     return es_primo

# print(verificar_primo(numero=29))

# # #              ----------------

# # # Opcion 2
# # # CON BANDERA 

# def verificar_primo_flag(numero:int):
#     """Crear una función que reciba un número y retorne 
#     True si el número es primo, False en caso contrario.

#     Args:
#         numero (int): numero ingresado por el usuario

#     Returns:
#         bool: True si el número es primo, False en caso contrario
#     """
#     bandera_divisores = False

#     for i in range (2, numero):
#         if numero % i == 0: # no es primo
#             bandera_divisores = False
#             break
#         else:
#             bandera_divisores = True
#     return bandera_divisores
# print(verificar_primo_flag(numero=29))

#-------------------------------------------

# # Daniela Serra
# # Funciones. Ejercicio 8

# Crear una función que (utilizando la función del punto 11 de la guía de For), 
# muestre todos los números primos comprendidos entre entre la unidad y 
# un número ingresado como parámetro. La función retorna la cantidad de 
# números primos encontrados.

# Guia For 11. Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. 
# Informar cuántos números primos se encontraron.

# def mostrar_numeros_primos(numero):
#     for i in range (1, numero + 1):
#         for j in range ()

# # --------------------------------------------------------

# # Ejercicio 10

# # Crear una función que le solicite al usuario el ingreso de un número entero y 
# # lo retorne.

# def pedir_numero():
#     numero = int(input("ingrese un numero: "))
#     return numero

# # -------------------------------------------------------

# # # Ejercicio 11
# # Crear una función que le solicite al usuario el ingreso de un número 
# # flotante y lo retorne.

# def pedir_numero_flotante():
#     numero_flotante = int(input("Ingrese un numero flotante: "))
#     return numero_flotante

# # Ejercicio 12
# # Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

# def pedir_cadena():
#     cadena = input("Ingrese una cadena: ")
#     return cadena

# -----------------------------------------------------------------

# Ejercicio 13
# Especializar las funciones del punto 10, 11 y 12 para hacerlas reutilizables. 
# Agregar validaciones.

def pedir_dato(mensaje, mensaje_error, tipo = int, min = None, max = None, len_min = None):
    dato = input(mensaje)
    while dato < min or dato > max:
        dato = input(mensaje_error)
    while len(dato) < 5:
        dato = input(mensaje_error)
    return dato


numero = pedir_dato("Ingrese el numero: ", "Numero incorrecto. Reingrese el numero", min = 0, max = 100) # 0 - 100
numero_flotante = pedir_dato("Ingrese el numero flotante: ", "Numero incorrecto. Reingrese el numero", min = 0, max = 100) # 0 - 100
cadena = pedir_dato("Ingrese cadena: ", "Cadena incorrecta. Reingrese la cadena", len_min = 5) # len 5