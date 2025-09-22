# Daniela Serra
# Desafío 1: Facturación CFP

# A partir del ingreso del precio de tres productos, calcular:
# La suma de todos los precios.
# El precio promedio.
# El precio final (la suma de todos los precios más el 21% de IVA)

primer_producto = float(input("Ingrese el precio del primer producto: "))
segundo_producto = float(input("Ingrese el precio del segundo producto: "))
tercer_producto = float(input("Ingrese el precio del tercer producto: "))

suma_precios = primer_producto + segundo_producto + tercer_producto
promedio_precios = suma_precios /3
precio_final = (suma_precios * 0.21) + suma_precios

print(f"La suma de todos los precios es {suma_precios:.2f}. "
      f"El precio promedio es {promedio_precios:.2f}. "
      f"El precio final, incluyendo el IVA es {precio_final:.2f}")