# # Daniela Serra
# # Funciones. Ejercicio 1

# # Escribir una función que calcule el área de un rectángulo. 
# # La función recibe la base y la altura y retorna el área. 

# def calcular_area_rectangulo(base, altura):
#     # resultado = base * altura
#     # return resultado
#     return base * altura

# # Llamar la funcion
# # Pedir datos al usuario
# base_rectangulo = int(input("Ingrese la medida de la base: "))
# altura_rectangulo = int(input("Ingrese la medida de la altura: "))

# resultado = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
# print(f"la superficie es {resultado}")

#--------------------------------------------------

# Daniela Serra
# Funciones. Ejercicio 9

# Crear una función que imprima la tabla de multiplicar de un número recibido 
# como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) 
# para definir el rango de multiplicación. Por defecto es del 1 al 10


def tabla_multiplicar(valor, inicio, fin):
    mensaje = ""
    for i in range (inicio, fin + 1):
        resultado = valor * i
        mensaje += f"{valor} x {i} = {resultado}\n"
    return mensaje

valor = int(input("valor: "))
inicio = int(input("numero de inicio: "))
fin = int(input("numero de finalizacion: "))
resultado = tabla_multiplicar(valor, inicio, fin)

print(resultado)
print(tabla_multiplicar(valor, inicio, fin))

