# Daniela Serra
# Integrador Repetitivas

# De los jugadores participantes en un torneo de ajedrez (no se sabe cuántos), 
# se registra:

# nombre
# la edad (mayor de 10 años)
# la cantidad de partidas ganadas (no menor a cero) que obtuvieron en el torneo.
# Categoria Jr, Sr, Ssr

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
bandera_sr = True
bandera_ssr = True
bandera_jr = True
suma_partidas_ganadas = 0


condicion = input("¿Desea registrar datos de un participante del torneo? (si/no): ").lower()
#VALIDAR

if condicion == "no":
    print("\nTe esperamos en el próximo torneo.\n")

elif condicion == "si":

    while condicion == "si":
        
        nombre = input("Ingrese el nombre del jugador: ").capitalize()

        edad = input("Ingrese la edad del jugador: ")
        #Validacion Edad
        if edad.isdigit: 
            edad = int(edad)
            if edad < 10:
                print("No tiene edad suficiente para participar. Debe ser mayor de 10 años")
                edad = input("Ingrese la edad del jugador: ")
        else:
            print("Respuesta inválida. La edad debe estar expresada en números.")
            edad = input("Ingrese la edad del jugador: ")

        partidas_ganadas = int(input("Ingrese la cantidad de partidas ganadas en el torneo: "))
        #Validar

        categoria = input("Ingrese la categoria a la que corresponde (JR, SR, SRR): ").upper()
        #VALIDAR

        # a. Nombre del jugador con más partidas ganadas.
        while i == 0 or max_partidas < partidas_ganadas:
            max_partidas = partidas_ganadas
            max_nombre = nombre

        if categoria == "SR":

        # d. El promedio de edades por categoria
            suma_sr += edad
            i_sr += 1
            
            # e. Porcentaje de partidas ganadas por categoría
            if bandera_sr == True or partidas_ganadas_sr < partidas_ganadas:
                partidas_ganadas_sr = partidas_ganadas

                bandera_sr = False


        elif categoria == "JR":
        # d. El promedio de edades por categoria
            suma_jr += edad
            i_jr += 1

            # e. Porcentaje de partidas ganadas por categoría
            if bandera_jr == True or partidas_ganadas_jr < partidas_ganadas:
                partidas_ganadas_jr = partidas_ganadas

                bandera_jr = False

        elif categoria == "SSR":
        # d. El promedio de edades por categoria
            suma_ssr += edad
            i_ssr += 1

            # e. Porcentaje de partidas ganadas por categoría
            if bandera__ssr == True or partidas_ganadas_ssr < partidas_ganadas:
                partidas_ganadas_ssr = partidas_ganadas

                bandera_ssr = False


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

        # e. Porcentaje de partidas ganadas por categoría
        suma_partidas_ganadas += partidas_ganadas
    
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
        
    # e. Porcentaje de partidas ganadas por categoría
    porcentaje_sr = partidas_ganadas_sr / suma_partidas_ganadas * 100
    porcentaje_ssr = partidas_ganadas_ssr / suma_partidas_ganadas * 100
    porcentaje_jr = partidas_ganadas_jr / suma_partidas_ganadas * 100

    # Informar en pantalla:
    print(f"a. El nombre del jugador con más partidas ganadas es {max_nombre} con un total de {max_partidas} partidas ganadas")
    print(f"b. El nombre del jugador Ssr con menos partidas ganadas es: {min_nombre_ssr} con un total de {min_partidas_ssr} y su edad es {min_edad_ssr}.")
    print(f"c. El promedio de edades de los jugadores es {promedio_edades}")
    print(f"d. Promedio de edades por categoria: \n"
            f"\tSR: {promedio_sr:.2f}% \n"
            f"\tSSR: {promedio_ssr:.2f}% \n"
            f"\tJR: {promedio_jr:.2f}% \n")
    print(f"e. Porcentaje de partidas ganadas por categoría: \n"
            f"\tSR: {porcentaje_sr:.2f}% \n"
            f"\tSSR: {porcentaje_ssr:.2f}% \n"
            f"\tJR: {porcentaje_jr:.2f}% \n")