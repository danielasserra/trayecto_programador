# Clase 08
# Correccion examen condicionales // REPETITIVAS WHILE

# categoria = input("Ingrese la categoria del restaurante ('Economico', 'Estandar', 'Gourmet'): ")
# ingresos_totales = float(input("Ingresos totales en dolares: USD"))
# dias_mas_pedidos = int(input("Dia con más pedidos (1. fin de semana o 2. dia laboral): "))

# if categoria == "economico":
#     porcentaje_comision = 0.18
# elif categoria == "estandar":
#     porcentaje_comision = 0.12
# elif categoria == "gourmet":
#     porcentaje_comision = 0.08
# else:
#     print("No es una categoria valida")

# comision = ingresos_totales * porcentaje_comision

# precio_parcial = ingresos_totales - comision

# if dias_mas_pedidos == 1:
#     bonificacion = 0.05

# valor_bonificacion = precio_parcial * bonificacion

# ingresos_netos = precio_parcial + valor_bonificacion

# if ingresos_netos > 10000:
#     mensaje = "el restaurante recibe una campaña de marketing gratuita"
# elif ingresos_netos > 5000:
#     mensaje = "el restaurante obtiene un paquete de descuentos"
# else:
#     mensaje = "no tiene beneficios adicionales"

# print(f"Las ganancias del restaurante son: USD{ingresos_netos:.2f}")
# print(f"{mensaje}")

# -----------------------------------------------------------

# Integrador Estructuras Repetitivas

# Permitir que el usuario ingrese todos los números que desee. 
# Los mismos deben estar comprendidos entre -10000 y 10000, y deben 
# ser distintos de 0. Determinar:
#   La suma acumulada de los números negativos.
#   La suma acumulada de los números positivos.
#   La cantidad de números negativos ingresados.
#   El promedio de los números positivos.
#   El número positivo más grande.
#   El porcentaje de números negativos ingresados, respecto del total de ingresos.

suma_negativos = 0
suma_positivos = 0
cantidad_negativos = 0
cantidad_positivos = 0
cantidad_total = 0
maximo = 0
eleccion = "si"

while eleccion == "si":
    numero = int(input("Ingrese un numero: "))

    while numero <-10000 or numero > 10000 or numero == 0:
        print("Numero incorrecto. Inténtelo nuevamente")
        numero = int(input("Ingrese un numero: "))

    if numero < 0:
        suma_negativos += numero
        cantidad_negativos += 1
    elif numero > 0:
        suma_positivos += numero
        cantidad_positivos += 1
        if maximo < numero:
            maximo = numero
    
    cantidad_total += 1
    eleccion = input("¿Desea ingresar otro numero? (si/no)")
    
if cantidad_positivos > 0:
    promedio_positivos = suma_positivos / cantidad_positivos
else:
    promedio_positivos = 0

porcentaje_negativos = (cantidad_negativos / cantidad_total) * 100

print(f"La suma acumulada de los números negativos es {suma_negativos}")
print(f"La suma acumulada de los números positivos es {suma_positivos}")
print(f"La cantidad de números negativos ingresados es {cantidad_negativos}")
print(f"El promedio de los números positivos es {promedio_positivos}")
print(f"El numero positivo más grande es {maximo}")
print(f"El porcentaje de números negativos ingresados, respecto del total de ingresos es {porcentaje_negativos}")