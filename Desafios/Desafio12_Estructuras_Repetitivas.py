# Daniela Serra
# Integrador Estructuras Repetitivas

# Análisis de temperaturas extremas
# Permitir que el usuario ingrese temperaturas en grados Celsius 
# (pueden ser negativas o positivas). Los valores deben estar entre -50 y 60, 
# y el ingreso termina cuando el usuario escribe "no".

# Calcular y mostrar:
# 🌡️ La temperatura mínima registrada.
# 🔥 La temperatura máxima registrada.
# 🧮 El promedio de todas las temperaturas.
# ❄️ La cantidad de temperaturas bajo cero.
# 🔥 La cantidad de temperaturas iguales o mayores a 30°C.
# 📊 El porcentaje de temperaturas bajo cero respecto al total.

# 💡 Requisitos:
# Validar que la temperatura esté entre -50 y 60.
# No se debe permitir ingresar 0 como temperatura (así practicás esa validación también).
# El programa debe preguntar: ¿Desea ingresar otra temperatura? (si/no).

# Inicializacion de variables
condicion = "si"
bandera_primera = True
i = 0
i_bajo_cero = 0
i_calor = 0
minimo = 0
maximo = 0
suma = 0

# Datos ingresados por el usuario
condicion = input("¿Desea ingresar temperaturas? (si/no): ").lower()

# Validacion
while condicion != "si" and condicion != "no":
    print("Respuesta inválida. Debe ser 'si' o 'no'")
    condicion = input("¿Desea ingresar temperaturas? (si/no): ").lower()

if condicion == "no":
    print("La próxima será")

else:

    while condicion == "si":
        temperatura = int(input("Ingrese la temperatura en grados celsius (valores entre -50° y 60°): "))
        # Validación de datos
        while temperatura < -50 or temperatura > 60 or temperatura == 0:
            print("Respuesta inválida. Los valores deben estar entre -50° y 60°")
            temperatura = int(input("Ingrese la temperatura en grados celsius (valores entre -50° y 60°): "))
    
        # Max Min
        if bandera_primera == True or temperatura < minimo:
            minimo = temperatura
    
        if bandera_primera == True or temperatura > maximo:
            maximo = temperatura
            bandera_primera = False

        # suma de temperaturas para promedio
        suma += temperatura
    
        # contador
        i += 1

        # cantidad de temperaturas bajo 
        if temperatura < 0:
            i_bajo_cero += 1
    
        # cantidad de temperaturas iguales o mayores a 30°C.
        if temperatura >= 30:
            i_calor += 1

        # condicion
        condicion = input("¿Desea ingresar otra temperatura? (si/no): ").lower()
        
        # validación
        while condicion != "si" and condicion != "no":
            print("Respuesta inválida. La respuesta debe ser 'si' o 'no'")
            condicion = input("¿Desea ingresar otra temperatura? (si/no)").lower()


    # promedio de todas las temperaturas
    if i > 0:
        promedio_temperatura = suma / i
    else:
        promedio_temperatura = 0

    # porcentaje de temperaturas bajo cero respecto al total.
    if i_bajo_cero > 0:
        porcentaje_bajo_cero = (i_bajo_cero / i) * 100

    # Calcular y mostrar:
    print(f"La temperatura mínima registrada es {minimo}°C\n"
        f"La temperatura máxima registrada es {maximo}°C\n"
        f"El promedio de todas las temperaturas es {promedio_temperatura:.2f}\n"
        f"La cantidad de temperaturas bajo cero es {i_bajo_cero}\n"
        f"La cantidad de temperaturas iguales o mayores a 30°C es {i_calor}\n"
        f"El porcentaje de temperaturas bajo cero respecto al total es {porcentaje_bajo_cero:.2f}")


