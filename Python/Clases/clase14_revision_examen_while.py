repetir = True

while repetir:

    nombre = ""
    suma_edad_eu_am = 0
    contador_eu_am = 0
    contador_af_as = 0

    votos_prevost = 0
    votos_tagle = 0
    votos_turkson = 0

    nombre_am = 0
    edad_am = 0
    voto_am = ""

    total_votos = 0
    porcentaje_prevost = 0
    porcentaje_tagle = 0
    porcentaje_turkson = 0


    # solicitud de datos
    continuar = True

    while continuar:
        
        nombre = input("Ingrese su nombre: ")
        # Evaluar que no esté vacio el nombre
        while nombre == "":
            if nombre == "":
                nombre = input("Ingrese su nombre: ")

        
        edad = int(input("edad: "))
        edad_valida = False
        while edad_valida == False:
            if edad >= 65:
                edad_valida = True
            else:
                edad = int(input("la edad no puede ser menor a 65: "))


        region = input("Region: ").lower()
        while region != "america" and region != "europa" and region != "oceania" and region != "asia" and region != "africa":
            region = input("Region inválida. Vuelva a intentarlo: ")

        voto = input("voto: ").lower()
        while voto != "prevost" and voto != "tagle" and voto != "turkson":
            voto = input("elija entre los candidatos disponibles: ").lower()
        
        # 1. contabilizar cardenales de europa o america:
        if (region == "europa" or region == "america") and edad >= 70 and edad < 80:
            contador_eu_am += 1
            suma_edad_eu_am += edad

        # 2. % de votos emitidos x africa y asia
        if (region == "africa" or region == "asia") and edad < 75:
            contador_af_as += 1

        # 3
        if voto == "prevost":
            votos_prevost += 1
        elif voto == "tagle":
            votos_tagle += 1
        else:
            votos_turkson += 1

        # 4    
        if (edad_am < edad or edad_am == 0) and region == "america":
            edad_am = edad
            nombre_am = nombre
            voto_am = voto
        
        respuesta = input("desea cargar otro voto (s/n): ")
        if respuesta != "s":
            continuar = False

    mayor_votos = votos_prevost
    candidato_mayor = "prevost"

    if votos_tagle > votos_prevost:
        mayor_votos = votos_tagle
        candidato_mayor = "tagle"
    elif votos_tagle == votos_prevost:
        candidato_mayor = "empate"
    
    if votos_turkson > votos_prevost:
        mayor_votos = votos_turkson
        candidato_mayor = "turkson"
    elif votos_turkson == votos_prevost:
        candidato_mayor = "empate"


    if total_votos > 0:
        porcentaje_prevost = votos_prevost / total_votos * 100
        porcentaje_tagle = votos_tagle / total_votos * 100
        porcentaje_turkson = votos_turkson / total_votos * 100


    if candidato_mayor == "empate":
        print("Hubo empate. la votacion se reinicia")
    else:
        repetir = False

    print(f"habemus papam {candidato_mayor}")
    print(f"porcentaje de votos: \nPrevost{porcentaje_prevost}% \nTagle: {porcentaje_tagle}% \nTurkson: {porcentaje_turkson}%")

    if contador_eu_am > 0:
        promedio = suma_edad_eu_am / contador_eu_am
        print(f"el promedio de europeos y americanos es {promedio}")
    else:
        print("No se ingresaron candidatos europeos ni americanos")
    
    if contador_af_as > 0:
        porcentaje_af_as = contador_af_as / total_votos * 100
        print(f"El porcentaje de votants de af o asia es de: {porcentaje_af_as}")

    if edad_am == 0:
        print("No se ingresaron candidatos americanos")
    else:
        print(f"el candidato am de menor edad es {nombre_am}, edad {edad_am}, voto {voto_am}")
