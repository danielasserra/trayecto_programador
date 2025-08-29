# # for i in range(5):
# #     numero = input("...")

# # Este tipo de escalares me permite guardar un solo numero
# # que pasa si necesito ordenarlos, armar lista, mostrar solo los pares...?
# # Vamos a trabajarlo orientado a objetos

# # La lista se define con corchetes

# # lista = [] #lista vacia
# # lista = list() #lista vacia

# # # para harckodear una lista
# # lista = [5,9,7,8,6, True, "cadena"] # las listas son heterogeneas, pueden ser todos numeros, todos booleanos o combinaci´no de cosas
# # # se puede meter otra lista adentro (lista anidadda)

# # # las listas son objetos mutables: se pueden modificar, agregar o quitar elementos

# # # Las listas son indexables: para poder aceder 

# # #para acceder a cada elemento de la lista, usamos un índice:
# # print(lista[1])

# # # el primer elemento es la posición 0.
# # print(lista[0])

# # # si programo y me quiero ir de rango, antes de poder ejecutar me lo va a informar, por ej en C#
# # # en python va a intentear ejecutarse y cuando no pueda, porque está fuera de memoria, intento acceder a una posicion de memoria que no es de la variable, lanza excepcion y rompe el programa)

# # for i in range(0, len(lista), 1): #len para saber cuantos elementos tiene la lista
# #     print(lista[i]) #la variable de control del for va a ayudar a pararme dentro de cada uno de los elementos de la lista

# #     if lista[i] %2==0:
# #         print(lista[i]) # pares
    
# #     if [i] %2==0:
# #         print(lista[i]) #posiciones pares


# lista_num = []

# lista_num.append(66)
# lista_num.append(99)



# #print(len(lista_num))

# for i in range(5):
#     numero = int(input("numero"))
#     lista_num.append(numero)

# for i in range(0, len(lista_num), 1): #len para saber cuantos elementos tiene la lista
#     print(lista_num[i])

    #ingresar 5numeros, mostrar suma y promedio

# lista_numeros = []

# suma = 0
# numero = 0

# for i in range(5):
#     numero = int(input("numero: "))
#     lista_numeros.append(numero)

# for i in range(len(lista_numeros)):
#     suma += lista_numeros[i]

# promedio = suma / len(lista_numeros)

# print("suma = ", suma, "promedio = ", promedio)


#################### FUNCIONES

# CARGAR DATOS
#pasaje x valor: int, float, bool (es una copia del valor), no modifica el original
# inmutables


# pasaje x referencia (en python todo es x referencia), pasar la direccion d memoria, modifica original
# mutables

def cargar_lista(lista_numeros):
    for i in range(5):
        numero = int(input("numero: "))
        lista_numeros.append(numero)

def mostrar_lista(lista_numeros):
    for i in range(len(lista_numeros)):
        print(lista_numeros[i])

def mostrar_pares(lista_numeros):
    for i in range(len(lista_numeros)):
        if lista_numeros[i] %2==0:
            print(lista_numeros[i]) # pares

def sumar_numeros(lista_numeros):
    for i in range(len(lista_numeros)):
        suma = 0
        suma += lista_numeros[i]
    return suma

def calcuñar_promedio(lista_numeros):
    suma = sumar_numeros(lista_numeros)
    promedio = suma / len(lista_numeros)
    return promedio




lista = []
cargar_lista(lista)
mostrar_pares(lista)
mostrar_lista(lista)

promedio = calcuñar_promedio(lista)
print(promedio)
suma = sumar_numeros(lista)
print(suma)