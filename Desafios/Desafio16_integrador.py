# Daniela Serra
# Integrador:
    # Variables y tipos de datos
    # Entrada de datos
    # Condicionales (if, else)
    # Bucles (while)
    # Validaciones
    # Contadores, acumuladores
    # Bandera
    # Cálculos (promedios, máximos, mínimos, porcentajes)

# 💼 Ejercicio Integrador: Encuesta de empleabilidad juvenil

# Una ONG desea relevar datos sobre la empleabilidad de jóvenes. 
# No se sabe cuántos encuestados habrá. Por cada persona, 
# se deben ingresar los siguientes datos:

# Nombre
# Edad (entre 18 y 35 años)
# ¿Está actualmente trabajando? (responder "si" o "no")
# Cantidad de trabajos previos (mayor o igual a 0)
# ¿Finalizó sus estudios secundarios? (responder "si" o "no")

# Al finalizar el relevamiento, se debe informar:
# 👩‍💼 Nombre del encuestado más joven que trabaja actualmente
# 📉 Nombre y edad del encuestado con más trabajos previos
# 🎓 Porcentaje de encuestados que finalizaron sus estudios
# 💼 Promedio de trabajos previos entre quienes actualmente no trabajan
# 👥 Cantidad total de encuestados

condicion = "si"
bandera_primera = True # primera vez que se corre el bucle
nombre_mas_joven = "" # Nombre del encuestado más joven 
edad_mas_joven = 0 # edad del encuestado más joven que trabaja
mas_trabajos = 0
nombre_mas_trabajos = "" 
edad_mas_trabajos = 0
suma_trabajo_previo = 0
termino_estudios = 0 #Porcentaje de encuestados que finalizaron sus estudios
promedio_trabajo_previo = 0 # Promedio de trabajos previos entre quienes actualmente no trabajan
i_secundario = 0
i_no_trabaja = 0
i = 0 # cant total encuestados


print("\n 💼 Bienvenido a la encuesta sobre Empleabilidad Juvenil 💼")

condicion = input("¿Desea responder la encuesta? (si/no): ")

# Validación de condicion
while condicion != "si" and condicion != "no":
    print("Respuesta inválida. Debe ser 'si' o 'no'. Inténtelo nuevamente")
    condicion = input("¿Desea responder la encuesta? (si/no): ")

# si la respuesta es no
if condicion == "no":
    print("\nEsperamos que pueda participar de la encuesta la próxima vez")

# si la respuesta es si
elif condicion == "si":

    # mientras la condicion sea si
    while condicion == "si":
        
        # Ingreso de datos del usuario:
        nombre = input("Ingrese su nombre: ")

        edad = int(input("Ingrese su edad (entre 18 y 35 años): "))
        # Validación de edad
        while edad < 18 or edad > 35:
            print("No pertenece al rango etáreo de la encuesta. Inténtelo nuevamente")
            edad = int(input("Ingrese su edad (entre 18 y 35 años): "))

        trabaja = input("¿Está trabajando actualmente? (si/no): ")
        # Validación de estado laboral
        while trabaja != "si" and trabaja != "no":
            print("Respuesta inválida. Debe ser 'si' o 'no'. Inténtelo nuevamente")
            trabaja = input("¿Está trabajando actualmente? (si/no): ")

        trabajo_previo = int(input("¿Cuantos trabajos previos ha tenido? "))
        # Validación de trabajos previos
        while trabajo_previo < 0:
            print("Respuesta inválida. La cantidad de trabajos anteriores no puede ser negativa. Inténtelo nuevamente")
            trabajo_previo = int(input("¿Cuantos trabajos previos ha tenido? "))   

        secundario = input("¿Finalizó sus estudios secundarios? (si/no)")
        # Validación de finalización de estudios
        while secundario != "si" and secundario != "no":
            print("Respuesta inválida. Debe ser 'si' o 'no'. Inténtelo nuevamente.")
            secundario = input("¿Finalizó sus estudios secundarios? (si/no)")

        # Durante la primer vuelta del bucle asignar valor a las variables
        if bandera_primera == True:
            nombre_mas_joven = nombre # Nombre del encuestado más joven
            edad_mas_joven = edad # edad del encuestado más joven
            mas_trabajos_previos = trabajo_previo # cantidad de trabajos anteriores

            bandera_primera = False
        
        # Nombre del encuestado más joven que trabaja
        if trabaja == "si":
            if edad <= edad_mas_joven:
                nombre_mas_joven = nombre

        # Nombre y edad del encuestado con más trabajos previos
        if mas_trabajos <= trabajo_previo:
            mas_trabajos = trabajo_previo
            nombre_mas_trabajos = nombre
            edad_mas_trabajos = edad

        # Cantidad de encuestados que finalizaron sus estudios
        if secundario == "si":
            i_secundario += 1
        
        if trabaja == "no":
            suma_trabajo_previo += trabajo_previo
            i_no_trabaja += 1

        # Cantidad total de encuestados
        i += 1
        

        # continuar o finalizar bucle
        condicion = input("¿Desea ingresar otra respuesta? (si/no): ")
        # Validación de condicion
        while condicion != "si" and condicion != "no":
            print("Respuesta inválida. Debe ser 'si' o 'no'. Inténtelo nuevamente")
            condicion = input("¿Desea ingresar otra respuesta? (si/no): ")

    # Porcentaje de encuestados que finalizaron sus estudios
    if i > 0:
        termino_estudios = i_secundario / i * 100

    # Promedio de trabajos previos entre quienes actualmente no trabajan
    if i_no_trabaja > 0:
        promedio_trabajo_previo = suma_trabajo_previo / i_no_trabaja

    print("\n------------------- Resultados de la encuesta -------------------\n"
          f"\n👩‍💼 Nombre del encuestado más joven que trabaja actualmente: {nombre_mas_joven}\n"
          f"📉 Nombre del encuestado con más trabajos previos: {nombre_mas_trabajos}\n"
          f"📅 Edad del encuestado con más trabajos previos: {edad_mas_trabajos}\n"
          f"🎓 Porcentaje de encuestados que finalizaron sus estudios: {termino_estudios:.2f}\n"
          f"💼 Promedio de trabajos previos entre quienes actualmente no trabajan: {promedio_trabajo_previo:.2f}\n"
          f"👥 Cantidad total de encuestados:{i}\n"
          "----------------------- Gracias por participar ---------------------\n")