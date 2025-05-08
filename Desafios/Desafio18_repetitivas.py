# Daniela Serra
# Integrador Repetitivas

# De los jugadores participantes en un torneo de ajedrez (no se sabe cuántos), 
# se registra:

# nombre
# la edad (mayor de 10 años)
# la cantidad de partidas ganadas (no menor a cero) que obtuvieron en el torneo.
# Categoria Jr, Sr, Ssr

# Informar:
# a. Nombre del jugador con más partidas ganadas. (maximo general, de todos los jugadores. Guardar el nombre)
# b. Nombre y edad del jugador Ssr con menos partidas ganadas.
# c. El promedio de edades de los jugadores.
# d. El promedio de edades por categoria
# e. Porcentaje de partidas ganadas por categoría.

# a. Nombre del jugador con más partidas ganadas.
i = 0 #contador general
max_partidas = 0
max_nombre = ""

# b. Nombre y edad del jugador Ssr con menos partidas ganadas.
min_partidas_ssr = 0
min_nombre_ssr = ""
min_edad_ssr = 0

# c. El promedio de edades de los jugadores.
suma_edades = 0

# d. El promedio de edades por categoria
suma_ssr = 0
i_ssr = 0
promedio_ssr = 0
suma_jr = 0
i_jr = 0
promedio_jr = 0
suma_sr = 0
i_sr = 0
promedio_sr = 0

# e. Porcentaje de partidas ganadas por categoría.
partidas_ganadas_sr = 0
partidas_ganadas_ssr = 0
partidas_ganadas_jr = 0



condicion = input("¿Desea registrar datos de un participante del torneo? (si/no): ")
#VALIDAR

if condicion == "no":
    "Te esperamos en el próximo torneo."

elif condicion == "si":

    while condicion == "si":
        
        nombre = input("Ingrese el nombre del jugador: ").capitalize

        edad = input("Ingrese la edad del jugador: ")
        #VALIDAR

        partidas_ganadas = int(input("Ingrese la cantidad de partidas ganadas en el torneo: "))
        #Validar

        categoria = input("Ingrese la categoria a la que corresponde (JR, SR, SRR): ").upper
        #VALIDAR

        # a. Nombre del jugador con más partidas ganadas.
        while i == 0 or max_partidas == 0:
            max_partidas = partidas_ganadas
            max_nombre = nombre
        
        if max_partidas < partidas_ganadas:
            max_partidas = partidas_ganadas
            max_nombre = nombre


        if categoria == "SR":

        # d. El promedio de edades por categoria
            suma_sr += edad
            i_sr += 1
            
            # e. Porcentaje de partidas ganadas por categoría
            if partidas_ganadas_sr < partidas_ganadas:
                partidas_ganadas_sr = partidas_ganadas


        if categoria == "JR":
        # d. El promedio de edades por categoria
            suma_jr += edad
            i_jr += 1

            # e. Porcentaje de partidas ganadas por categoría
            if partidas_ganadas_jr < partidas_ganadas:
                partidas_ganadas_jr = partidas_ganadas

        if categoria == "SSR":
        # d. El promedio de edades por categoria
            suma_ssr += edad
            i_ssr += 1

            # e. Porcentaje de partidas ganadas por categoría
            if partidas_ganadas_sr < partidas_ganadas:
                partidas_ganadas_sr = partidas_ganadas


        # b. Nombre y edad del jugador Ssr con menos partidas ganadas.
            while i == 0 or min_partidas_ssr == 0:
                min_partidas_ssr = partidas_ganadas
                min_nombre_ssr = nombre
                min_edad_ssr = edad
            
            if min_partidas_ssr > partidas_ganadas:
                min_partidas_ssr = partidas_ganadas
                min_nombre_ssr = nombre
                min_edad_ssr = edad
        
        # c. El promedio de edades de los jugadores.
        suma_edades += edad
        i += 1
    
    #------------------------- FUERA DE WHILE -----------------------

    # c. El promedio de edades de los jugadores.
    promedio_edades = suma_edades / i

    # d. El promedio de edades por categoria
    if i_sr > 0:
        promedio_sr = suma_sr / i_sr
    if i_ssr > 0:
        promedio_ssr = suma_ssr / i_ssr
    if i_jr > 0:
        promedio_jr = suma_jr / i_jr

        ########### FALTA TERMINAR E Y VALIDAR