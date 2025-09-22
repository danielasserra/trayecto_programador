# # FUNCIONES

# # # Daniela Serra
# # # Funciones. Ejercicio 8

# # Crear una función que (utilizando la función del punto 11 de la guía de For), 
# # muestre todos los números primos comprendidos entre entre la unidad y 
# # un número ingresado como parámetro. La función retorna la cantidad de 
# # números primos encontrados.

# # Guia For 11. Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. 
# # Informar cuántos números primos se encontraron.

# def mostrar_primos_hasta(numero):
#     contador = 0
#     for i in range (2, numero + 1):
#         bandera_primo = True
#         for j in range (2, i):
#             if i % j == 0:
#                 bandera_primo = False
#                 break
#         if bandera_primo == True:
#             print(i)
#             contador += 1
    
#     return contador
            

# # -----------------------------------------
# #     ---------- MINIFICAR ----------------
# # -----------------------------------------

# # SI HAY FOR DENTRO DE FOR HAY QUE REVISAR LA FN
# # Si hay demasiada identación, hay que intentar que el código se pueda simplificar
# # Que dentro de una fn se pueda llamar otras fn mas pequeñas COMPOSICION
# #
# # EJEMPLO CON LA FN ANTERIOR
# # MODULARIZAR: 
# def buscar_primos(numero:int) -> str:
#     contador = 0
#     cadena_primos = ""
#     for i in range(2, numero + 1):
#         bandera_primo = determinar_primo(i)
#         if bandera_primo == True:
#             cadena_primos = cadena_primos + str(i) + "\n"
#             contador += 1


# def determinar_primo(numero):
#     bandera_primo = True
#     for j in range (2, numero):
#         if numero % j == 0:
#             bandera_primo = False
#             break
#     return bandera_primo


# def mostrar_primos_hasta(numero):
#     contador, numeros_primos = buscar_primos(numero)
#     print(numeros_primos)
#     return contador

#     # contador = 0
#     # for i in range (2, numero + 1):
#     #     bandera_primo = determinar_primo(i)
#     #     if bandera_primo == True:
#     #         print(i)
#     #         contador += 1
    
#     # return contador

# ######## MAIN ############

# cantidad = mostrar_primos_hasta(19)
# print(f"cantidad encontrada {cantidad}")

# # TUPLA: conjunto de elemenots que pueden ser de distinto tipo y no se pueden modificar

# -----------------------------------------

# # Ejercicio 10

# # Crear una función que le solicite al usuario el ingreso de un número entero y 
# # lo retorne.

# def pedir_numero():
#     numero = int(input("ingrese un numero: "))
#     return numero


# # ######################################################
# # # Alumno (legajo, edad, nota)

# # # Puedo usar la fn "pedir_numero" para ingresar todos esos datos

# # legajo = pedir_numero()
# # edad = pedir_numero()
# # nota = pedir_numero()

# # hay que cambiar el texto del imput "ingrese un numero: "

# def pedir_numero(mensaje):
#     numero = int(input(mensaje))
#     return numero

# legajo = pedir_numero("Ingrese legajo: ") # 1000 y 2000
# # while legajo < 1000 or legajo > 2000:
# #     legajo = pedir_numero("Reingrese legajo: ") # 1000 y 2000

# edad = pedir_numero("Ingrese edad: ") # 1 y 10
# # while edad < 18 or edad > 55:
# #     edad = pedir_numero("Reingrese edad: ") # 1000 y 2000

# nota = pedir_numero("Ingrese nota: ") # 18 y 55
# # while nota < 1 or nota > 10:
# #     nota = pedir_numero("Reingrese nota: ") # 1000 y 2000


# LLevar la validación a la función

def pedir_numero(mensaje, minimo, maximo, mensaje_error):
    numero = int(input(mensaje))
    while numero < minimo or maximo > maximo:
        numero = int(input(mensaje_error))
        
    return numero

legajo = pedir_numero("Ingrese legajo: ", 1000, 2000, "Error, reingrese legajo") # 1000 y 2000
edad = pedir_numero("Ingrese edad: ", 18, 55, "Recorcholis, usted ha ingresado mal la edad") # 18 y 55
nota = pedir_numero("Ingrese nota: ", 1, 10, "Atencion, reingrese nota") # 1, 10

############################################

# ------------------------------------------------
#------------- Separar funciones en módulos -----------#
# ------------------------------------------------

# OPCION 1
# X ej: funciones q hacen cuentas aritmeticas, todas en un mismo archivo
# Creamso archivo MAIN, q es el principal y desde ahí llamamos las fns que están en otro lado
# TENEMOS QUE IMPORTAR EL MODULO al MAIN: "import + nombre_de_archivo" ej. import artméticas y para llamar a la fn artimeticas.sumar_1()
# import aritmeticas as a (alias, para que sea más corto)
# Se pone el nombre del archivo punto el nombre de la fn que estamos llamando

# OPCION 2
# from aritmeticas import * (todo)
# no tengo que poner el nomnbre del archivo, directamente aparece todo el listado de fn sumar_1()
# Desde el modulo aritmeticas traeré todo: variables, fns, globales, constantes, etc

# OPCION 3
# si no sé cuales voy a usar, traigo todo, pero si sé específicamente
# from aritmeticas import sumar_2(), sumar_4()

# Lo unico que validamos para una cadena de caracteres es el largo (len)
# TAREA: Hacer el ejercicio 6 con pow y con for
