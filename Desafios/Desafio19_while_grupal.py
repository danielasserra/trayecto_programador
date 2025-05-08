# Desafio Grupal While

# 🔹 Recolección de Datos
# Cada participante encuestado deberá proporcionar la siguiente información:
#  ✔️ Nombre
#  ✔️ Edad (debe ser 16 años o más)
#  ✔️ Región de procedencia (América, Europa, Asia)
#  ✔️ Área de preferencia (MUS, LIT, ART)
# El sistema deberá permitir ingresar los datos de los participantes (no se sabe cuántos) 
# mediante la terminal.


# 🔹 Análisis de Datos
# A partir de las respuestas, se deben calcular las siguientes métricas:
# 1️⃣ Cantidad de participantes provenientes de América que votaron por "Música (MUS)" 
# y cuya edad esté entre 18 y 30 años (inclusive).
# 2️⃣ Porcentaje de participantes que NO votaron por Literatura (LIT), 
# siempre y cuando: 
#   Provengan de Europa.
#   Su edad esté entre 25 y 40 años.


# 3️⃣ Participante de Asia con mayor edad: Mostrar su nombre y el área de preferencia 
# que votó.

# 4️⃣ Porcentajes totales según área de pertenencia.

# 5️⃣ Edad promedio de los europeos


# 🔹 Requisitos del Programa
# ✔️ Los datos deben solicitarse y validarse correctamente.
# ✔️ Presentar los resultados de manera clara y organizada en pantalla.

condicion = input("Desea contestar la encuesta (si/no): ")
i_america_preferencia = 0
i_america = 0
i_europa = 0
i_asia =0
i_lit = 0
i = 0
asia_mayor_edad = 0
bandera_primera = False
suma_edad = 0
porcentaje_lit = 0
asia_nombre = ""
edad_promedio_europeos = 0

while condicion == "si":
    # 🔹 Recolección de Datos

    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    region = input("Ingrese su region de procedencia(America,Europa,Asia): ")
    area_de_preferencia = input("Ingrese su area (Mus, Lit, Art): ")

        #total de participantes
    i +=1

    
    if region == "America":
        # 4️⃣ Porcentajes totales según área de pertenencia.
        i_america += 1

        # 1️⃣ Cantidad de participantes provenientes de América que votaron por "Música (MUS)" 
        # y cuya edad esté entre 18 y 30 años (inclusive).
        if area_de_preferencia == "Mus" and edad >= 18 and edad <= 30:
            i_america_preferencia += 1

    if region == "Europa":
        # 4️⃣ Porcentajes totales según área de pertenencia.
        i_europa += 1

        # 2️⃣ Porcentaje de participantes que NO votaron por Literatura (LIT), 
            # siempre y cuando: 
            #   Provengan de Europa.
            #   Su edad esté entre 25 y 40 años.
        if area_de_preferencia != "Lit" and edad >= 25 and edad <= 40:
            i_lit += 1
            porcentaje_lit = i_lit / i * 100
        
        # 5️⃣ Edad promedio de los europeos
        suma_edad += edad


    if region == "Asia":
        # 4️⃣ Porcentajes totales según área de pertenencia.
        i_asia += 1

    # 3️⃣ Participante de Asia con mayor edad: Mostrar su nombre y el área de preferencia 
    # que votó.
        if asia_mayor_edad < edad or bandera_primera == False:
             asia_mayor_edad = edad
             asia_nombre = nombre
             asia_preferencia = area_de_preferencia

             bandera_primera == True
        
        if asia_mayor_edad < edad:
            asia_mayor_edad = edad
            asia_nombre = nombre
            asia_preferencia = area_de_preferencia
    
    condicion = input("¿Desea ingresar otra respuesta? (si/no)")

    ############# FUERA DEL WHILE

# 4️⃣ Porcentajes totales según área de pertenencia.
porcentaje_america = i_america / i * 100
porcentaje_asia = i_asia / i * 100
porcentaje_europa = i_europa / i * 100

# 5️⃣ Edad promedio de los europeos
if i_europa > 0:
    edad_promedio_europeos = suma_edad / i_europa 

print(f"Cantidad de participantes provenientes de América que votaron por 'Música (MUS)' y cuya edad esté entre 18 y 30 años (inclusive) es {i_america_preferencia}") 
print(f"Porcentaje de participantes que NO votaron por Literatura (LIT), siempre y cuando: Provengan de Europa y su edad esté entre 25 y 40 años es {porcentaje_lit}")
print(f"Participante de Asia con mayor edad: Mostrar su nombre y el área de preferencia que votó: {asia_nombre} y {asia_mayor_edad} años")
print(f"Porcentajes totales segun el area de pertenencia: \n"
      f"America {porcentaje_america}\n"
      f"Asia: {porcentaje_asia}\n"
      f"Europa: {porcentaje_europa}")
print(f"Edad promedio de los europeos {edad_promedio_europeos}")