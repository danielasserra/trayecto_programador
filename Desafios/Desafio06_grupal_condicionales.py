# Desafío CONDICIONALES

consumo = int(input("Ingrese la cantidad de m3 consumidos: "))
cliente = input("¿qué tipo de cliente es? (Residencial/Comercial/Industrial): ")

cargo_fijo = 7000
costo_metro = 200
bonificacion = 0
recargo = 0
subtotal = 0

#Cliente Residencial
if cliente == "Residencial":
    if consumo < 30:
        bonificacion = 0.1
    elif consumo > 80:
        recargo = 0.15


# Cliente Comercial
elif cliente == "Comercial":
    if consumo > 300:
        bonificacion = 0.12
    elif consumo > 150:
        bonificacion = 0.08
    elif consumo < 50:
        recargo = 0.05

# Cliente Industrial:

elif cliente == "Industrial":
    if consumo > 1000:
        bonificacion = 0.3
    elif consumo > 500:
        bonificacion = 0.2
    elif consumo < 200:
        recargo = 0.1


subtotal = consumo * costo_metro + cargo_fijo


# Casos especiales:
if cliente == "Residencial" and subtotal < 35000:
    bonificacion = 0.05


descuento = subtotal * bonificacion
recargo_calculo = subtotal * recargo
recargo_total = subtotal + recargo_calculo

total = subtotal + recargo_calculo - descuento
total_iva =  total * 0.21

total_final = total + total_iva

print(f"El total bruto es {subtotal}\n"
      f"Las bonificaciones son de {descuento}\n"
      f"El recargo es de {recargo_calculo}\n"
      f"El subtotal con recargos y bonificaciones es de {total}\n"
      f"El iva es de {total_iva}\n"
      f"El total final a pagar es de {total_final}")