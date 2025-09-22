# # Desafío: Calculadora Básica
# Enunciado:
# Crea un programa que funcione como una calculadora básica interactiva. 
# El programa debe mostrar un menú con las siguientes opciones:
# Sumar, Restar, Multiplicar, Dividir y Salir
# Cada operación debe ser implementada dentro de una función diferente, 
# que reciba dos números como parámetros y retorne el resultado de la 
# operación.
# El programa debe funcionar en un bucle, permitiendo al usuario 
# realizar varias operaciones hasta que decida salir.

# Requisitos:
# Usar una función para cada operación matemática: 
# sumar, restar, multiplicar, dividir.
# El menú debe repetirse hasta que el usuario elija la opción 5 (salir).
# Si la opción es válida (1 a 4), se deben:
# Solicitar dos números al usuario.
# Llamar a la función correspondiente.
# Mostrar el resultado en el formato:
# 2 * 2 = 4  (usando el operador correspondiente según la opción).
# Controlar que no se divida entre cero.
# Si se elige la opción 5, mostrar un mensaje de despedida y finalizar el programa.
# Si se elige una opción no válida, mostrar un mensaje de error.


#--------------------------------------------------------------------#
#--------------------- CREACION DE FUNCIONES ------------------------#
#--------------------------------------------------------------------#

def sumar(primer_numero:int, segundo_numero:int) -> int:
    """sumar dos numeros

    Args:
        primer_numero (int): numero ingresado
        segundo_numero (int): numero ingresado

    Returns:
        int: suma de los numeros
    """
    return primer_numero + segundo_numero
#####
print(sumar(2,2))

# -------------------------

def restar(primer_numero:int, segundo_numero:int) -> int:
    """restar dos numeros

    Args:
        primer_numero (int): numero ingresado
        segundo_numero (int): numero ingresado

    Returns:
        int: resta de los numeros
    """
    return primer_numero - segundo_numero

# -------------------------

def multiplicar(primer_numero:int, segundo_numero:int) -> int:
    """multiplicar dos numeros

    Args:
        primer_numero (int): numero ingresado
        segundo_numero (int): numero ingresado

    Returns:
        int: multiplicacion de los numeros
    """
    return primer_numero * segundo_numero

# -------------------------

def dividir(primer_numero:int, segundo_numero:int) -> float:
    """dividir dos numeros

    Args:
        primer_numero (int): numero ingresado
        segundo_numero (int): numero ingresado

    Returns:
        float: division de los numeros
    """
    return primer_numero / segundo_numero


salir = "no"

while salir == "no":
    print("=== CALCULADORA BÁSICA ===")
    print (" 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Salir")

    operacion = int(input("Ingrese el numero de la operacion que desea realizar: "))
    while operacion < 1 or operacion > 5:
        operacion = int(input("Seleccione una operación válida (entre 1 y 5): "))

    if operacion == 5:
        print("Gracias por utilizar la calculadora")
        break

    primer_numero = int(input("Ingrese el primer numero: "))
    segundo_numero = int(input("Ingrese el segundo numero: "))

    if operacion == 1:
        print(f"{primer_numero} + {segundo_numero} = {sumar(primer_numero, segundo_numero)}")

    elif operacion == 2:
        print(f"{primer_numero} - {segundo_numero} = {restar(primer_numero, segundo_numero)}")

    elif operacion == 3:
        print(f"{primer_numero} x {segundo_numero} = {multiplicar(primer_numero, segundo_numero)}")

    elif operacion == 4:
        if segundo_numero != 0:
            print(f"{primer_numero} / {segundo_numero} = {dividir(primer_numero, segundo_numero)}")
        else: 
            while segundo_numero == 0:
                print("No se puede dividir por cero. Ingrese nuevamente los numeros.")
                primer_numero = int(input("Ingrese el primer numero: "))
                segundo_numero = int(input("Ingrese el segundo numero: "))
            print(f"{primer_numero} / {segundo_numero} = {dividir(primer_numero, segundo_numero)}")

    
    salir = input("¿Desea realizar otra cuenta? (si/no): ").lower()
    while salir != "si" and salir != "no":
        salir = input("Respuesta inválida. ¿Desea realizar otra cuenta? (si/no): ").lower()

