#KEOPS

# Area pirámide (para calcular cuanto cartón vamos a necesitar):
# Area total = suma del area de su base y la suma del área de sus caras

# area de la base  (lado * lado = base_keops * base_keops)

# area del triángulo (base * altura / 2 = base_keops * altura_keops / 2) 

# AREA TOTAL = area de la base + (area del triángulo * 4)


# Datos que ingresa el usuario
base_keops = float(input("Ingrese el valor del lado de la base de la pirámide: "))
altura_keops = float(input("Ingrese el valor de la altura de la pirámide: "))
# Para ello el usuario ingresará: el grosor en cm y la densidad del cartón en g/cm3.
grosor = float(input("Ingrese el grosor en cm: "))
densidad = float(input("Ingrese la densidad en g/cm3: "))

# KEOPS
# Calculo del área
area_base_keops = base_keops * base_keops
area_triangulo_keops = base_keops * altura_keops / 2
area_keops = area_base_keops + (area_triangulo_keops * 4)

# KEFREN
# Kefren es el 95% de la base de Keops
base_kefren = base_keops * 0.95
altura_kefren = altura_keops * 0.95

# Calculo del área
area_base_kefren = base_kefren * base_kefren
area_triangulo_kefren = base_kefren * altura_kefren / 2
area_kefren = area_base_kefren + (area_triangulo_kefren * 4)

# MICERINOS datos
base_micerinos = base_keops * (1 - 0.5 * (base_keops/100))
altura_micerinos = altura_keops * (1 - 0.5 * (altura_keops /100))

# Calculo area
area_base_micerinos = base_micerinos * base_micerinos
area_triangulo_micerinos = base_micerinos * altura_micerinos / 2
area_micerinos = area_base_micerinos + (area_triangulo_micerinos * 4)


# Pasar de cm2 a mts2: Metros cuadrados = Centímetros cuadrados / 10000
area_keops_mts = area_keops / 10000
area_kefren_mts = area_kefren / 10000
area_micerinos_mts = area_micerinos / 10000

# area total}
area_total = area_keops + area_kefren + area_micerinos

print(f"La cantidad de cartón necesario para cada pirámide (expresado en mt2) es: \n"
      f"Keops {area_keops_mts:.2f}. \n"
      f"Kefren {area_kefren_mts:.2f} \n"
      f"Micerinos {area_micerinos_mts:.2f} \n"
      f"La cantidad de cartón total necesaria es de: {area_total:.2f}")


# El peso de cada pirámide (expresado en Kg).
# El peso de las 3 pirámides (expresado en Kg).



# superficie * grosor = volumen de cartón
volumen_carton_keops = area_keops * grosor
volumen_carton_kefren = area_kefren * grosor
volumen_carton_micerinos = area_micerinos * grosor

# densidad * volumen = peso
peso_kefren = densidad * volumen_carton_kefren * 0.01
peso_keops = densidad * volumen_carton_keops * 0.01
peso_micerinos = densidad * volumen_carton_micerinos * 0.01

print(f"El peso de las piramides es de: \n"
      f"Keops: {peso_keops:.2f} \n"
      f"Kefren: {peso_kefren:.2f} \n"
      f"Micerinos: {peso_micerinos:.2f}")