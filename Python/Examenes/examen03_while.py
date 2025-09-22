# Daniela Serra
# Examen 12/05/25
# Habemus Papam - El Cónclave Papal en Acción

# Requisitos del Sistema del Cónclave
#  El registro de votos y la validación de datos serán realizadas siguiendo estrictamente 
# las normas canónicas.
#  Los resultados se presentarán con la claridad y la solemnidad que exige este evento trascendental.
#  Cuando un candidato alcance la mayoría necesaria, se anunciará la histórica frase: HABEMUS PAPAM. 
# La fumata blanca indicará al mundo que la Iglesia tiene un nuevo líder espiritual.

# Inicialización de variables

# contador gral
i = 0

# 1.
suma_edad_eu_am = 0
i_eu_am = 0
promedio_eu_am = 0

# 2.
i_af_as = 0
porcentaje_af_as = 0

# 3.
prevost = 0
tagle = 0
turkson = 0
habemus_mensaje = ""

# 4.
porcentaje_prevost = 0
porcentaje_tagle = 0
porcentaje_turkson = 0

# 5.
edad_america = 0
nombre_america = ""
voto_america = ""
bandera_primera = True

condicion = input("¿Desea emitir su voto? (si/no): ").lower()
while condicion != "si" and condicion != "no":
    print("Respuesta inválida. Inténtelo nuevamente.")
    condicion = input("¿Desea emitir su voto? (si/no): ").lower()

if condicion == "si":
    
    while condicion == "si":
        nombre = input("Ingrese su nombre: ")
        if not nombre.isalpha():
            print("El nombre sólo debe contener letras. Inténtelo nuevamente")
            nombre = input("Ingrese su nombre: ")
        
        #  Su edad (debe ser mayor o igual a 65 años para participar).
        edad = input("Ingrese su edad: ")
        if not edad.isdigit():
            print("La edad sólo debe contener numeros. Inténtelo nuevamente")
            edad = input("Ingrese su edad: ")
        else: 
            edad = int(edad)
            while edad < 65:
                print("No tiene suficiente edad para votar")
                edad = int(input("Ingrese su edad: "))
        
        #  Su región de procedencia (Europa, América, África, Asia, Oceanía).
        procedencia = input("Ingrese su región de procedencia (Europa, América, África, Asia, Oceanía): ").upper()
        while procedencia != "EUROPA" and procedencia != "AMERICA" and procedencia != "AFRICA" and procedencia != "ASIA" and procedencia != "OCEANIA":
            print("Respuesta inválida, la region de procedencia debe ser Europa, América, África, Asia, Oceanía")
            procedencia = input("Ingrese su región de procedencia (Europa, América, África, Asia, Oceanía): ").upper()
        
        #  Su voto para el próximo Papa (entre 3 opciones: PREVOST - TAGLE - TURKSON).
        voto = input("Emita su voto para el próximo Papa (PREVOST - TAGLE - TURKSON): ").upper()
        while voto != "PREVOST" and voto != "TAGLE" and voto != "TURKSON":
            print("Respuesta inválida. Debe votar por PREVOST, TAGLE o TURKSON")
            voto = input("Emita su voto para el próximo Papa (PREVOST - TAGLE - TURKSON): ").upper()
        
        i += 1
        
        if procedencia == "AMERICA":
            #  1. Promedio de edad de cardenales de nacionalidad Europea o Americana cuya edad esté entre 70 y 80 años.
            if procedencia == "EUROPA" and (edad >= 70 and edad <= 80):
                suma_edad_eu_am += edad
                i_eu_am += 1
            
            #  5. Nombre, edad y elección del cardenal de nacionalidad Americana con menor edad.
            if edad_america > edad or bandera_primera == True:
                edad_america = edad
                nombre_america = nombre
                voto_america = voto
                
                bandera_primera = False
            
        #  2. Porcentaje de votos emitidos por candidatos de África o Asia, siempre que los votantes tengan 
        # entre 65  y 75 años.
        if procedencia == "AFRICA" or procedencia == "ASIA" and (edad >= 65 and edad <= 75):
            i_af_as += 1
        
        #  3. (Habemus Papam). El candidato con más votos será anunciado como el nuevo Papa. No habrá empates. 
        
        if voto == "PREVOST":
            prevost += 1
        elif voto == "TAGLE":
            tagle += 1
        elif voto == "TURKSON":
            turkson += 1
        
        if prevost > tagle and prevost > turkson:
            habemus_mensaje = "3. Habemus Papam. El candidato con más votos es Prevost"
        elif tagle > prevost and tagle > turkson:
            habemus_mensaje = "3. Habemus Papam. El candidato con más votos es Tagle"
        elif turkson > tagle and turkson > prevost:
            habemus_mensaje = "3. Habemus Papam. El candidato con más votos es Turkson"
        else:
            habemus_mensaje = "3. No Habemus Papam. Hubo empate. Deberá votarse nuevamente"
      
        # continuar o finalizar el while
        condicion = input("¿Desea emitir su voto? (si/no): ").lower()
        while condicion != "si" and condicion != "no":
            print("Respuesta inválida. Inténtelo nuevamente.")
            condicion = input("¿Desea emitir su voto? (si/no): ").lower()
    
    ####################### FUERA DEL WHILE
    
    if i > 0:
        #  2. Porcentaje de votos emitidos por candidatos de África o Asia, siempre que los votantes tengan 
        # entre 65 y 75 años.
        porcentaje_af_as = i_af_as / i * 100
    
        #  4. Distribución porcentual de votos para cada uno de los postulados.
        porcentaje_prevost = prevost / i * 100
        porcentaje_tagle = tagle / i * 100
        porcentaje_turkson = turkson / i * 100
    
    
    # Mostrar en pantalla
    print("\n--------------------------Resultados de la votación--------------------------\n")
    # 1. Promedio de edad de cardenales de nacionalidad Europea o Americana cuya edad esté entre 70 y 80 años.
    if i_eu_am > 0:
        promedio_eu_am = suma_edad_eu_am / i_eu_am
        print (f"1. El promedio de edad de los cardenales de Europa y America entre 70 y 80 es {promedio_eu_am:.2f}")
    else:
        print("1. No hay votantes de Europa o América entre 70 y 80 años")

    #  2. Porcentaje de votos emitidos por candidatos de África o Asia, siempre que los votantes tengan entre 65 y 75 años
    if i > 0:
        print(f"2. El porcentaje de votos emitidos por candidatos de Africa y Asia entre 65 y 75 años es {porcentaje_af_as:.2f}%")
    else:
        print(f"2. No hay votantes de Africa o Asia entre 65 y 75 años")
    #  3. (Habemus Papam). El candidato con más votos será anunciado como el nuevo Papa. No habrá empates. 
    print(f"{habemus_mensaje}")
    
    #  4. Distribución porcentual de votos para cada uno de los postulados.
    print("4. Distribución porcentual de votos para cada uno de los postulados:")
    print(f"\tPrevost: {porcentaje_prevost:.2f}%")
    print(f"\tTagle: {porcentaje_tagle:.2f}%")
    print(f"\tTurkson: {porcentaje_turkson:.2f}%")
    
    #  5. Nombre, edad y elección del cardenal de nacionalidad Americana con menor edad.
    if edad_america > 0:
        print(f"5. El cardenal de nacionalidad americana con menor edad es {nombre_america} con {edad_america} años y votó a {voto}")
    else:
        print(f"5. No hay votantes de América")
    
    print("\n-------------------------------------------------------------------------\n")

# Condición. Si no desea votar:
else:
    print("Lo esperamos en la próxima elección")