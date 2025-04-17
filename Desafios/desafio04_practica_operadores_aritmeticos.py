# # Desafío 4: Presupuesto de Viaje

# # Una agencia de viajes necesita calcular el costo total de un paquete turístico. Para ello, el programa debe solicitar:
# # Costo del pasaje por persona
# # Cantidad de personas
# # Costo del hospedaje por noche
# # Cantidad de noches
# # Costo estimado de comida por día
# # El programa debe calcular y mostrar:
# # Costo total del pasaje (cantidad de personas × costo del pasaje).
# # Costo total del hospedaje (cantidad de noches × costo por noche).
# # Costo total de comida (cantidad de días × costo estimado por día).
# # Costo total del viaje (suma de los tres costos anteriores).

# pasaje = float(input("ingrese el valor del pasaje x persona: "))
# cant_personas = int(input("ingrese la cant de pers q viajan: "))
# hospedaje = float(input("Ingrese el costo del hospedaje por noche: "))
# cant_noches = int(input("Ingrese la cantidad de noches de la estadia: "))
# comida = float(input("ingrese el gasto estimado en comida por dia: "))

# total_pasajes = pasaje * cant_personas
# total_hospedaje = hospedaje * cant_noches
# total_comida = comida * cant_noches
# total_viaje = total_pasajes + total_comida + total_hospedaje

# print(f"El costo total de los pasajes es de: {total_pasajes:.2f} \n"
#       f"El costo total del hospedaje es de: {total_hospedaje:.2f} \n"
#       f"El costo total de comida es de: {total_comida:.2f} \n"
#       f"El costo total del viaje es de: {total_viaje:.2f} \n")


################

# Desafío 5: Cálculo de Materiales para una Pared
# Un albañil necesita saber cuántos materiales comprar para construir una pared rectangular. Se ingresan:
# Altura de la pared (en metros)
# Ancho de la pared (en metros)
# El programa debe calcular:
# Cantidad de ladrillos necesarios, sabiendo que cada ladrillo mide 0.20 m de alto por 0.40 m de ancho.
# Cantidad de mezcla de cemento y arena, considerando que por cada metro cuadrado de pared se requieren:
# 8 kg de cemento
# 15 kg de arena
# 10 litros de agua

# Altura_pared = float(input("Ingrese la altura de la pared en metros: "))
# Ancho_pared = float(input("Ingrese el ancho de la pared en metros: "))

# #cantidad de ladrillos
# superficie_pared = Ancho_pared * Altura_pared #base*altura
# superficie_ladrillos = 0.40 * 0.20
# cant_ladrillos = superficie_pared / superficie_ladrillos|||

# # cantidad de cemento, arena y agua
# cant_cemento = superficie_pared * 8
# cant_arena = superficie_pared * 15
# cant_agua = superficie_pared * 10

# print(f"La cantidad necesaria de ladrillos es de: {cant_ladrillos:.2f} \n"
#       f"La cantidad de materiales necesaria es la siguiente: \n"
#       f"Cemento: {cant_cemento} \n"
#       f"Arena: {cant_arena} \n"
#       f"Agua: {cant_agua}")

####################

# Ejercicio 1: Perímetro y Área de un Círculo
# Realizar un programa que solicite el radio de un círculo y calcule: area y perimetro

# import math

# radio = float(input("Ingrese el radio de un círculo: "))

# #area pi*radio2

# area = math.pi * pow (radio, 2)

# # perimetro 2 * pi * radio

# perimetro = 2 * math.pi * radio

# print(f"perimetro = {perimetro:.2f}, area = {area:.2f}")

##############

# Pedir al usuario los dos catetos de un triángulo rectángulo y calcular: hipotenusa, perimetro y area

# import math

# cateto_mayor = float(input("Ingrese el cateto mayor: "))
# cateto_menor = float(input("Ingrese el cateto menor: "))

# hipotenusa = math.sqrt(pow(cateto_mayor,2) + pow(cateto_menor,2))

# perimetro = cateto_mayor + cateto_menor + hipotenusa

# area = (cateto_menor * cateto_mayor) / 2

# print(f"Resultados del triángulo: \n"
#       f" - Hipotenusa: {hipotenusa:.2f} \n"
#       f" - Perímetro: {perimetro:.2f} \n"
#       f" - Área: {area:.2f}")

#######################

# Ejercicio 3: Cálculo de Promedios con Mensaje Personalizado
# Solicitar el nombre, apellido y tres notas de un alumno. Calcular su promedio y mostrar:

# Si el promedio es mayor o igual a 7 → "Felicitaciones, [nombre], aprobaste con un promedio de X."

# Si el promedio es menor a 7 → "Lo siento, [nombre], necesitas mejorar. Tu promedio es X."

nombre_alumno = input("Ingrese nombre y apellido del alumno: ")
primer_nota = float(input("Ingrese primera nota: "))
segunda_nota = float(input("Ingrese segunda nota: "))
tercera_nota = float(input("Ingrese tercera nota: "))

promedio = (primer_nota + segunda_nota + tercera_nota) / 3

print(f"El promedio del alumno {nombre_alumno} es: {promedio}")