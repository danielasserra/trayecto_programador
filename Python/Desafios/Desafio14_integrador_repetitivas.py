# Daniela Serra
# Integrador Repetitivas.

# De los jugadores participantes en un torneo de ajedrez (no se sabe cuántos), 
# se registra:

# nombre
# la edad (mayor de 10 años)
# la cantidad de partidas ganadas (no menor a cero) que obtuvieron en el torneo.

# Informar:
# Nombre del jugador con más partidas ganadas.
# Nombre y edad del jugador con menos partidas ganadas.
# El promedio de edades de los jugadores.
# El total de partidas ganadas.

condicion = "si"
bandera_primera = True
mas_partidas_ganadas = 0
menos_partidas_ganadas = 0
jugador_mas_ganadas = "No se ingresaron datos"
jugador_menos_ganadas = "No se ingresaron datos"
edad_menos_ganadas = 0
suma_edades = 0
suma_partidas_ganadas = 0
i = 0

condicion = input("¿Desea ingresar los datos del jugador? (si/no) ")

# Validación ingreso de datos del jugador
while condicion != "si" and condicion != "no":
    print("Respuesta inválida. Debe responder 'si' o 'no'. Inténtelo nuevamente")
    condicion = input("¿Desea ingresar los datos del jugador? (si/no) ")    

# si no desea ingresar ningun jugador
if condicion == "no":
    print("Esperamos verte en el próximo torneo")

# si desea ingresar datos de jugadores
elif condicion == "si":
    
    # mientras desee ingresar datos de jugadores
    while condicion == "si":
        # ingresa el nombre, primeras letras mayusculas
        nombre = input("Ingrese el nombre del jugador: ").capitalize()

        # ingresa la edad 
        edad = int(input("Ingrese la edad del jugador (debe ser mayor a 10 años): "))
        
        # Validacion edad
        while edad < 10:
            print("No alcanza la edad mínima para participar del torneo. Inténtelo nuevamente")
            edad = int(input("Ingrese la edad del jugador (debe ser mayor a 10 años): "))    

        suma_edades += edad

        # Cantidad de partidas ganadas
        partidas_ganadas = int(input("Ingrese la cantidad de partidas que ha ganado: "))

        while partidas_ganadas < 0:
            print("Respuesta inválida. La cantidad de partidas ganadas no puede ser menor a cero. Inténtelo nuevamente")
            partidas_ganadas = int(input("Ingrese la cantidad de partidas que ha ganado: "))    

        # Suma partidas ganadas
        suma_partidas_ganadas += partidas_ganadas

        # Asignar valores máximos y mínimos de partidas ganadas, nombre y edad para inicializar variables
        if bandera_primera == True:
            mas_partidas_ganadas = partidas_ganadas
            jugador_mas_ganadas = nombre
            menos_partidas_ganadas = partidas_ganadas
            jugador_menos_ganadas = nombre
            edad_menos_ganadas = edad

            bandera_primera = False

        # Determinar qué jugador ganó más partidas
        if mas_partidas_ganadas < partidas_ganadas:
            mas_partidas_ganadas = partidas_ganadas
            # guardar nombre del jugador con más partidas ganadas
            jugador_mas_ganadas = nombre

        # Determinar qué jugador ganó menos partidas
        if menos_partidas_ganadas > partidas_ganadas:
            menos_partidas_ganadas = partidas_ganadas
            # nombre del jugador con menos partidas ganadas
            jugador_menos_ganadas = nombre
            # edad del jugador con menos partidas ganadas
            edad_menos_ganadas = edad 

        # contador de jugadores ingresados
        i += 1

        # continuar o finalizar el bucle
        condicion = input("¿Desea ingresar otro jugador? (si/no): ")

        # Validación de condición
        while condicion != "si" and condicion != "no":
            print("Respuesta inválida. Debe responder 'si' o 'no'. Inténtelo nuevamente")
            condicion = input("¿Desea ingresar los datos del jugador? (si/no) ")    

    # Dentro del ELIF fuera del WHILE
    
    # Promedio de edades:
    if i > 0:
        promedio_edades = suma_edades / i
    
    # PRINT EN ELIF NO EN WHILE
    print("\n-------------- Estadísticas del torneo --------------\n"
          f"\nNombre del jugador con más partidas ganadas: {jugador_mas_ganadas}\n"
          f"Nombre del jugador con menos partidas ganadas: {jugador_menos_ganadas}\n"
          f"Edad del jugador con menos partidas ganadas: {edad_menos_ganadas}\n"
          f"Promedio de edad de los jugadores: {promedio_edades:.2f}\n"
          f"Total de partidas ganadas: {suma_partidas_ganadas}\n"
          "\n------------------------------------------------------\n")