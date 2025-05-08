# Clase 11

# Codigo completo: https://www.onlinegdb.com/8-Ca1C9gpo

# Integrador Repetitivas.

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

seguir = "si"
bandera_primera = False
bandera_primer_Ssr = False
minimo_partida = 0
maxima_partida = 0
acumulador_edades = 0
porcentaje_edades = 0 
i = 0
acumulador_edades_sr = 0
acumulador_edades_jr = 0
acumulador_edades_ssr = 0
contador_jr = 0
contador_sr = 0
contador_ssr = 0

while seguir == "si":

    # Ingreso y validacion de datos
    nombre = input("Ingrese nombre: ")

    edad = int(input("Ingrese edad: "))
    while edad < 10:
        edad = int(input("Ingrese edad: "))

    partidas_ganadas = int(input("ingrese partidas ganadas: "))
    while partidas_ganadas < 0:
        partidas_ganadas = int(input("ingrese partidas ganadas: "))
    
    categoria = input("Ingrese categoria (Jr, Ssr, Sr): ")
    while categoria != "Jr" and categoria != "Ssr" and categoria != "Sr":
        categoria = input("Ingrese categoria (Jr, Ssr, Sr): ")

    seguir = input("¿Desea continuar ingresando? si/no: ")
    while seguir != "si" and seguir != "no":
        seguir = input("¿Desea continuar ingresando? si/no: ")

    # a. Nombre del jugador con más partidas ganadas.
    if partidas_ganadas > maxima_partida or bandera_primera == False:
        maxima_partida = partidas_ganadas
        nombre_mejor_jugador = nombre
        bandera_primera = True

    # c. El promedio de edades de los jugadores.
    acumulador_edades += edad
    i += 1

    # d. El promedio de edades por categoria
    if categoria == "Sr":
        acumulador_edades_sr += edad
        contador_sr += 1

    elif categoria == "Jr":
        acumulador_edades_jr += edad
        contador_jr += 1

    else:
        acumulador_edades_ssr += edad
        contador_ssr += 1

         # b. Nombre y edad del jugador Ssr con menos partidas ganadas.
        if partidas_ganadas > minimo_partida or contador_ssr == 1:
            minimo_partida = partidas_ganadas
            edad_peor_jugador_ssr = edad
            nombre_peor_jugador_ssr = nombre
            bandera_primer_Ssr = True



################### FUERA DEL WHILE ########################

# c. El promedio de edades de los jugadores.
porcentaje_edades = acumulador_edades / i

# d. El promedio de edades por categoria
if contador_sr > 0:
    promedio_sr = acumulador_edades_sr / contador_sr
if contador_ssr > 0:
    promedio_ssr = acumulador_edades_ssr / contador_ssr
if contador_jr > 0:
    promedio_jr = acumulador_edades_jr / contador_jr

print(f"a. El nombre del jugador con más partidas ganadas es {nombre_mejor_jugador}")

if bandera_primer_Ssr == True:
    print(f"b. El jugador Ssr con menos partidas ganadas es {nombre_peor_jugador_ssr}, edad {edad_peor_jugador_ssr} años")
else:
    print("b. No se pudo calcular el mínimo porque no se ingresó ningun Ssr")

print("d. promedios por categoria:")
print(f"\tSRR: {promedio_ssr}")
print(f"\tJR: {promedio_jr}") # \t = tabulación
if contador_sr > 0:
    print(f"\tSR: {promedio_sr}")
else:
    print("no se ingresaron sr")