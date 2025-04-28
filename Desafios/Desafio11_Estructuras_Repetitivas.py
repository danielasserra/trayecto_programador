# Daniela Serra
# Integrador Estructuras Repetitivas

# Permitir que el usuario ingrese todos los números que desee. 
# Los mismos deben estar comprendidos entre -10000 y 10000, y deben 
# ser distintos de 0. Determinar:
#   La suma acumulada de los números negativos.
#   La suma acumulada de los números positivos.
#   La cantidad de números negativos ingresados.
#   El promedio de los números positivos.
#   El número positivo más grande.
#   El porcentaje de números negativos ingresados, respecto del total de ingresos

# Inicializacion de variables: 
condicion = "si"
suma_negativos = 0
suma_positivos = 0
i_total = 0
i_negativos = 0
i_positivos = 0
positivo_max = 0
promedio_positivos = 0


# Dato ingresado por el usuario
condicion = input("¿Desea ingresar un número? (si/no): ").lower()

# Validación
while condicion != "si" and condicion != "no":
    print("Respuesta inválida. Debe ser 'si' o 'no'")
    condicion = input("¿Desea ingresar un número? (si/no): ").lower()

if condicion == "no":
    print("La próxima vez será")

elif condicion == "si":

    while condicion == "si":
        numero = int(input("Ingrese un numero entre -10000 y 10000, y distinto de 0: "))
    
        while numero < -10000 or numero > 10000 or numero == 0:
            print("Numero incorrecto. Inténtelo nuevamente")
            numero = int(input("Ingrese un numero entre -10000 y 10000, y distinto de 0: "))
    
        if numero < 0:
            suma_negativos += numero
            i_negativos += 1

        elif numero > 0:
            suma_positivos += numero
            if positivo_max < numero:
                positivo_max = numero 
            i_positivos += 1
    
        i_total += 1
    
        condicion = input("¿Desea ingresar otro numero? (si/no): ").lower()

        while condicion != "si" and condicion != "no":
            print("Respuesta inválida. Debe ser 'si' o 'no'")
            condicion = input("¿Desea ingresar un número? (si/no): ").lower()

    if i_positivos > 0: 
        promedio_positivos = suma_positivos / i_positivos
    else:
        promedio_positivos = 0

    porcentaje_negativos = (i_negativos / i_total) * 100

    print(f"La suma acumulada de los números negativos es {suma_negativos}\n"
          f"La suma acumulada de los números positivos es {suma_positivos}\n"
          f"La cantidad de números negativos ingresados es {i_negativos}\n"
          f"El promedio de los números positivos es {promedio_positivos:.2f}\n"
          f"El número positivo más grande es {positivo_max}\n"
          f"El porcentaje de números negativos ingresados, respecto del total de ingresos es {porcentaje_negativos:.2f}")