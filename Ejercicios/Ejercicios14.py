# Desafío: Encuesta de Preferencias Culturales en CFPGlobal

# Inicializacion de variables
# contador general
i = 0

# a.
i_mus = 0

# b.
i_lit = 0

# c.
bandera_primera = True
asia_max_edad = 0
asia_nombre = ""
asia_preferencia = ""

# d.
i_america = 0
i_europa = 0
i_asia = 0


condicion = input("¿Desea realizar la encuesta? (si/no)").lower()
#VALIDAR

if condicion == "no":
    print("La próxima vez será")

elif condicion == "si":
    
    while condicion == "si":
        
        #   Nombre
        nombre = input("Ingrese su nombre: ").upper()
        #VALIDAR isalpha
        
        #   Edad (debe ser 16 años o más)
        edad = input("Ingrese su edad: ")
        #Validar isdigit > 16
        
        #   Región de procedencia (América, Europa, Asia)
        region = input("Ingrese su region de procedencia (America / Europa / Asia): ").upper()
        #Validar
        
        #   Área de preferencia (MUS, LIT, ART)
        preferencia = input("Ingrese su area de procedencia (MUS / LIT / ART): ").upper()
        #validar
        
        # contador general
        i += 1
        
        # Procesos        
        if region == "AMERICA":
            #  a. Cantidad de participantes provenientes de América que votaron por "Música (MUS)" y 
            # cuya edad esté entre 18 y 30 años (inclusive).
            if preferencia == "MUS" and edad >= 18 and edad <= 30:
                i_mus += 1
            
            #  d. Porcentajes totales según área de pertenencia.
            i_america += 1
        
        if region == "EUROPA":
            #  b. Porcentaje de participantes que NO votaron por Literatura (LIT), siempre y cuando:
            #        Provengan de Europa.
            #        Su edad esté entre 25 y 40 años.
            if preferencia != "LIT" and edad >= 25 and edad <= 40:
                i_lit += 1
            
            #  d. Porcentajes totales según área de pertenencia.
            i_europa += 1
            
            #  e. Edad promedio de los europeos
            suma_edad_europeos += edad
                
        if region == "ASIA":
            #  c. Participante de Asia con mayor edad: Mostrar su nombre y el área de preferencia que votó.
            if asia_max_edad < edad or bandera_primera == True:
                asia_max_edad = edad
                asia_nombre = nombre
                asia_preferencia = preferencia
                
            #  d. Porcentajes totales según área de pertenencia.
            i_asia += 1
        
        # Continuar o finalizar while
        condicion = input("¿Desea realizar otra encuesta? (si/no)").lower()
        #validar
    
    ############## FUERA DE WHILE ###############
    
    if i > 0: 
        # b
        porcentaje_lit = i_lit / i * 100
        
        # d
        porcentaje_america = i_america / i * 100
        porcentaje_europa = i_europa / i * 100
        porcentaje_asia = i_asia / i * 100
        
        # e
        europa_edad_promedio = suma_edad_europeos / i_europa
        
    print(f"a. La cantidad de participantes provenientes de América que votaron MUS es: {i_mus}")
    print(f"b. Porcentaje de participantes que NO votaron por Literatura (LIT): {porcentaje_lit:.2f}%")
    print(f"c. Participante de Asia con mayor edad {asia_nombre} y preferencia {asia_preferencia}")
    print("d. Porcentajes totales según área de pertenencia:")
    print(f"America: {porcentaje_america:.2f}%")
    print(f"Europa: {porcentaje_europa:.2f}%")
    print(f"Asia: {porcentaje_asia:.2f}%")
    print(f"e. Edad promedio de los europeos {europa_edad_promedio:.2f}%")