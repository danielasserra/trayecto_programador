# # Daniela Serra
# # Funciones

# # ------------------------------------------------

# # # Ejercicio 1

# def calcular_area_rectangulo(base: int, altura: int) -> int:
#     """Calcula el área de un rectángulo

#     Args:
#         base (int): Longitud de la base del rectangulo
#         altura (int): ALtura del rectangulo

#     Returns:
#         int: El area del rectangulo (base * altura)
#     """
#     area_rectangulo = base * altura
#     return area_rectangulo

# # ------------------------------------------------

# # # Ejercicio 2
# # Escribe una función que calcule el área de un círculo. 
# # La función debe recibir el radio como parámetro y devolver el área.

# import math

# def calcular_area_circulo(radio:float) -> float:
#     """Calcula el área de un círculo

#     Args:
#         radio (float): Longitud del radio del círculo

#     Returns:
#         float: area del circulo (math.pi * (radio ** 2))
#     """
#     return math.pi * (radio ** 2)

# # ------------------------------------------------

# # # Ejercicio 3

# def verificar_par_o_impar(numero:int) -> str:
#     """verifica si un número dado es par o impar

#     Args:
#         numero (int): numero ingresado

#     Returns:
#         str: Mensaje indicando si el número es par o impar
#     """
#     if numero % 2 == 0:
#         mensaje = "El número es par"
#     else:
#         mensaje = "El número es impar"
    
#     return mensaje

# # ------------------------------------------------

# # # Ejercicio 4

# def verificar_par_o_impar_bool(numero:int) -> bool:
#     """verificar si un número dado es par o impar

#     Args:
#         numero (int): Numero ingresado

#     Returns:
#         bool: retorna True si el número es par, False en caso contrario
#     """
#     es_par = True
#     if numero % 2 != 0:
#         es_par = False
#     return es_par

# # ------------------------------------------------

# # # Ejercicio 5

# def encontrar_maximo(primer_numero:int, segundo_numero:int, tercer_numero:int) -> int:
#     """Encontrar el máximo de tres números. 
#     La función debe aceptar tres argumentos y devolver el número más grande

#     Args:
#         primer_numero (int): Numero ingresado
#         segundo_numero (int): Numero ingresado
#         tercer_numero (int): Numero ingresado

#     Returns:
#         int: Devuelve el numero más grande de los tres
#     """
#     # Esta era mi solucion pero era incorrecta. "Else" daba más grande al tercer numero, aunq no lo fuera
#     # Ademas, es muy larga y repetitiva.
#     # mas_grande = 0
#     # if primer_numero > segundo_numero and primer_numero > tercer_numero:
#     #     mas_grande = primer_numero
#     # elif segundo_numero > primer_numero and segundo_numero > tercer_numero:
#     #     mas_grande = segundo_numero
#     # else:
#     #     mas_grande = tercer_numero
#     # return mas_grande

#     mas_grande = primer_numero

#     if segundo_numero > mas_grande:
#         mas_grande = segundo_numero
#     if tercer_numero > mas_grande:
#         mas_grande = tercer_numero
#     return mas_grande

# # ------------------------------------------------

# # # Ejercicio 6

# # Opcion 1 con **
# def calcular_potencia_1(base:int, exponente:int) -> int:
#     """calcular la potencia de un número usando **

#     Args:
#         base (int): Numero base
#         exponente (int): exponente

#     Returns:
#         int: base elevado al exponente 
#     """
#     return base ** exponente

# # Opcion 2 con pow
# def calcular_potencia_2(base:int, exponente:int) -> int:
#     """calcular la potencia de un número usando pow

#     Args:
#         base (int): Numero base
#         exponente (int): exponente

#     Returns:
#         int: base elevado al exponente 
#     """
#     import math
#     return pow(base, exponente)

# # Opcion 3 con for
# def calcular_potencia_3(base:int, exponente:int) -> int:
#     """calcular la potencia de un número usando un bucle for

#     Args:
#         base (int): Numero base
#         exponente (int): exponente

#     Returns:
#         int: base elevado al exponente 
#     """
#     resultado = 1
#     for i in range (exponente):
#         resultado *= base
#     return resultado

# # Opcion 3 con for

# def calcular_potencia_4(base, exponente):
#      """calcular la potencia de un número usando un bucle for

#     Args:
#         base (int): Numero base
#         exponente (int): exponente

#     Returns:
#         int: base elevado al exponente 
#     """
#      resultado = 1
#      for i in range(exponente):
#          resultado *= base
#      return resultado
# # ------------------------------------------------

# # # Ejercicio 7

# def verificar_primo_bool_1(numero: int) -> bool:
#     """Verifica si el numero es primo o no

#     Args:
#         numero (int): Numero Ingresado

#     Returns:
#         bool: retorna True si el número es primo, False en caso contrario
#     """
#     es_primo = True
#     if numero < 2:
#         es_primo = False
#     else:        
#         for i in range(2, numero):        
#             if numero % i == 0:
#                 es_primo = False
#                 break
#     return es_primo

# # ------------------------------------------------

# # # Ejercicio 7

# def verificar_primo_bool_2(numero:int) -> bool:
#     """Verificar si el numero es primo o no

#     Args:
#         numero (int): numero ingresado

#     Returns:
#         bool: True si el número es primo, false en caso contrario.
#     """
#     es_primo = True
#     if numero < 2:
#         es_primo = False
#     else:
#         for i in range(2, numero):
#             if numero % i == 0:
#                 es_primo = False
#                 break
#     return es_primo

# # ------------------------------------------------

# # # Ejercicio 8

# # Crear una función que (utilizando la función del punto 11 de la guía de For), 
# # muestre todos los números primos comprendidos entre entre la unidad 
# # y un número ingresado como parámetro. La función retorna la cantidad de números 
# # primos encontrados.

# def mostrar_numeros_primos(numero):
#     cantidad_primos = 0
#     for i in range (1, numero + 1):
#         divisores = 0

#         for j in range (1, i + 1):
#             if i % j == 0:
#                 divisores += 1

#         if divisores == 2:
#             cantidad_primos += 1
#             print(i)

#     print("cantidad primos:", cantidad_primos)
#     return cantidad_primos

# ############################################

# print(mostrar_numeros_primos(10))


# ------------------------------------------------

# # # Ejercicio 9

# # Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. 
# # La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. 
# # Por defecto es del 1 al 10.

# def imprimir_tabla_multiplicar(numero, inicio = 1, fin = 10):
#     for i in range (inicio, fin + 1):
#         multiplicacion = numero * i
#         print(numero, "x", i, "=", multiplicacion)

# #################################

# imprimir_tabla_multiplicar(5)

# # ------------------------------------------------

# # # Ejercicio 10
# # Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

# def solicitar_numero():
#     numero = int(input("Ingrese un numero: "))
#     return numero

# ###############################
# print(solicitar_numero())

# # ------------------------------------------------

# # # Ejercicio 11
# # Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

# def solicitar_numero_float():
#     numero = float(input("Ingrese un numero flotante: "))
#     return numero

# #################################
# print(solicitar_numero_float())

# # ------------------------------------------------

# # # Ejercicio 12
# # Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

# def solicitar_cadena():
#     cadena = input("ingrese cadena: ")
#     return cadena

# ########################################
# print(solicitar_cadena(cadena))

# ------------------------------------------------

# # Ejercicio 13
# Especializar las funciones del punto 10, 11 y 12 para hacerlas reutilizables. Agregar validaciones.

def reutilizar_funciones(mensaje, mensaje_error, tipo_dato):
    variable = input(mensaje)
    if (tipo_dato == "entero" and variable.isdigit()) or (tipo_dato == "flotante" and type(variable) == float) or (tipo_dato == "cadena"):
        return variable
    else: 
        return mensaje_error


numero = reutilizar_funciones("ingrese un numero:", "Error. Ingrese un numero", "entero")
print(numero)
flotante = reutilizar_funciones("ingrese un numero flotante:", "Error. Ingrese un numero flotante", "flotante")
print(flotante)
cadena = reutilizar_funciones("Ingrese una cadena:", "Error. Ingrese una cadena", "cadena")
print(cadena)
