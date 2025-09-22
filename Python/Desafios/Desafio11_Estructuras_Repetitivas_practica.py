# Daniela Serra
# Integrador Estructuras Repetitivas (otra vez para practicar)

# Permitir que el usuario ingrese todos los números que desee. 
# Los mismos deben estar comprendidos entre -10000 y 10000, y deben 
# ser distintos de 0. Determinar:
#   -La suma acumulada de los números negativos.
#   -La suma acumulada de los números positivos.
#   -La cantidad de números negativos ingresados.
#   -El promedio de los números positivos.
#   -El número positivo más grande.
#   El porcentaje de números negativos ingresados, respecto del total de ingresos

# Inicialización de variables
condicion = "si"
i = 0
i_negativos = 0
i_positivos = 0
suma_negativos = 0
suma_positivos = 0
positivo_mayor = 0
promedio_positivos = 0

# Datos ingresados por el usuario
condicion = input("¿Desea ingresar un número? ").lower()

if condicion != "si" and condicion != "no":
    print("Respuesta inválida. Se espera 'si' o 'no'")
    condicion = input("¿Desea ingresar un número? ").lower()

if condicion == "no":
    print("La próxima será")

elif condicion == "si":

    while condicion == "si":
        numero = int(input("Ingrese un numero entre -10000 y 10000, distinto de 0: "))

        # Validacion
        while numero < -10000 or numero > 10000 or numero == 0:
            print("Respuesta inválida. El rango es entre -10000 y 10000, además debe ser distinto a 0")
            numero = int(input("Ingrese un numero entre -10000 y 10000, distinto de 0 "))
    
        # Si los numeros son negativos 
        if numero < 0:
            # suma de negativos
            suma_negativos += numero

            # contador de negativos
            i_negativos += 1

        # Si los numeros son positivos
        elif numero > 0:
            # encontrar el positivo más grande
            if positivo_mayor < numero:
                positivo_mayor = numero
            
            # suma de positivos
            suma_positivos += numero

            # contador de positivos
            i_positivos += 1

        # contador
        i += 1

        condicion = input("¿Desea ingresar otro numero? (si/no) ").lower()

        # Validacion
        if condicion != "si" and condicion != "no":
            print("Respuesta inválida. Se espera 'si' o 'no'")
            condicion = input("¿Desea ingresar otro numero? (si/no) ")
    
    # promedio de positivos
    if i_positivos > 0:
        promedio_positivos = suma_positivos / i_positivos
    
    # porcentaje de negativos respecto al total
    porcentaje_negativos = (i_negativos / i) * 100

    # Mostrar en pantalla
    print(f"La suma acumulada de los números negativos es {suma_negativos}")
    print(f"La suma acumulada de los números positivos es {suma_positivos}")
    print(f"La cantidad de números negativos ingresados es {i_negativos}")
    print(f"El promedio de los números positivos es {promedio_positivos:.2f}")
    print(f"El número positivo más grande es {positivo_mayor}")
    print(f"El porcentaje de números negativos ingresados, respecto del total de ingresos {porcentaje_negativos:.2f}%")