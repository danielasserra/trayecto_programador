# Daniela Serra
# Desafío 2: Construcciones CFP

# Una empresa de construcción requiere un programa que facilite el cálculo de 
# materiales necesarios para llevar a cabo distintos trabajos. 
# Las especificaciones son las siguientes:

# Construcción de un piso rectangular:
# Calcular la cantidad de metros cuadrados de baldosas necesarios para cubrir la superficie del piso.
# Por cada metro cuadrado de contrapiso, se utilizan 3 bolsas de arena, 1 bolsa de cemento y ½ litro de agua.

# Cercado de un terreno rectangular:
# Calcular la cantidad de metros de alambre de púas necesarios para rodear el terreno con 5 hiladas de alambre.

# El programa debe solicitar las medidas correspondientes


# Para la construccion del piso rectangular:
# Metros cuadrados necesarios de baldosas:
base_piso = float(input("Ingrese los metros de largo de piso: "))
altura_piso = float(input("Ingrese los metros de ancho del piso: "))
superficie_piso = base_piso * altura_piso

# Bolsas de arena
# 1 metro     ------ 3 bolsas
# superficie_piso -- x
bolsas_arena = superficie_piso / 3

# Bolsas de cemento
bolsas_cemento = superficie_piso

# agua
agua = superficie_piso * 0.5

# Cercado del terreno
# calcular el perímetro y multiplicar por 5, porq son 5 hileras
cercado = (base_piso * 2 + altura_piso * 2) / 5

print(f"Los metros cuadrados necesarios de baldosas son: {superficie_piso:.2f}. \n" 
      f"La cantidad necesaria de bolsas de arena es de {bolsas_arena:.2f} bolsas. \n"
      f"La cantidad necesaria de bolsas de cemento es: {bolsas_cemento:.2f}. \n"
      f"La cantidad necesaria de agua es de {agua:.2f}. \n"
      f"La cantidad de metros de alambre de púa necesaria es: {cercado:.2f}")


