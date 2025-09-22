# Daniela Serra
# CONDICIONALES EJERCICIO 13

# Una empresa que se dedica a la comercialización de lámparas de bajo consumo, 
# registra de sus ventas, los siguientes datos: marca y cantidad. 
# El precio de cada lamparita es de $7500 (Sin importar la marca).
# El programa deberá calcular el precio total de la venta, aplicando un descuento 
# si es que corresponde.

# Ingresa el Usuario
cantidad = int(input("Ingrese la cantidad de lamparitas que llevará: "))
marca = input("Ingrese la marca de la lámpara (ArgentinaLuz o FelipeLamparas u otra): ")

# Constante
PRECIO = 7500

# Inicialización de Variables
costo = PRECIO * cantidad
descuento = 0
ingresos_brutos = 0

#   A.  Si compra 6 lamparitas o más, tiene un descuento del 50%.
if cantidad >= 6:
    descuento = costo * 0.5

#   B.  Si compra 5 lamparitas marca “ArgentinaLuz” se aplica un 40% 
#       y si es de otra marca, el descuento es del 30%.
elif cantidad == 5:
    if marca == "ArgentinaLuz":
        descuento = costo * 0.4   
    else:
        descuento = costo * 0.3

#   C.  Si compra 4 lamparitas marca “ArgentinaLuz” o “FelipeLamparas” se 
#       hace un descuento del 25%, y si es de otra marca el descuento es del 20%.
elif cantidad == 4: 
    if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
        descuento = costo * 0.25
    else:
        descuento = costo * 0.2

#   D.  Si compra 3 lamparitas o menos, marca “ArgentinaLuz” el descuento es del 15%, 
#       si es “FelipeLamparas se hace un descuento del 10% y si es otra marca, 5%.

elif cantidad <= 3:
    if marca == "ArgentinaLuz":
        descuento = costo * 0.15
    elif marca == "FelipeLamparas":
        descuento = costo * 0.1
    else:
        descuento = costo * 0.05


# Precio con descuento
importe_final = costo - descuento

#   E.  Si el importe final con descuento suma más de $10500, se debe agregar 
#       el 10% de ingresos brutos.
if importe_final > 10500:
    ingresos_brutos = importe_final * 0.1
    importe_final = importe_final + ingresos_brutos
else:
    ingresos_brutos = "Exento"

# Informar: cantidad de lamparitas, marca, total sin descuento, descuento, 
# total con descuento, y si corresponde total de ingresos brutos y total a pagar.
print (f"\n----- Resumen de la venta -----\n"
       f"Cantidad de lamparitas: {cantidad} \n"
       f"Marca: {marca} \n"
       f"Total sin descuento {costo:.2f} \n"
       f"Descuento: {descuento:.2f} \n"
       f"Total de ingresos brutos {ingresos_brutos} \n"
       f"Total a pagar {importe_final:.2f} \n"
       f"---------------------------------\n")