# # Daniela Serra
# # Desafío condicionales
# # Ejercicio D: "CloudBox"

# Se solicita al usuario:

plan = input("Ingrese el tipo de plan (personal / profesional / corporativo): ").lower()
gigas_extra = int(input("Ingrese la cantidad de gigas extra solicitados: "))
cliente = int(input("Ingrese la antiguedad en meses: "))

# Inicializacion de variables
tarifa = 0 # precio base
descuento = 0
recargo = 0

# constantes
IVA = 0.21

# antiguedad
if cliente > 24:
    tipo_cliente = "ancestral"
elif cliente > 6:
    tipo_cliente = "antiguo"
else:
    tipo_cliente = "nuevo"
    
# Descuentos
if plan == "personal":
    tarifa = 3000
    if tipo_cliente == "nuevo":
        descuento = 0.10
elif plan == "profesional":
    tarifa = 7000
    if tipo_cliente == "nuevo" and not gigas_extra:
        descuento = 0.05
elif plan == "corporativo":
    tarifa = 15000
    if tipo_cliente == "antiguo":
        descuento = 0.15          

# descuento en cualquier plan con antiguedad > 24 meses
if tipo_cliente == "ancestral":
        descuento += 0.05

# cada 100 gigas extra += 500
cantidad_gigas_extra = gigas_extra / 100
costo_gigas_extra = cantidad_gigas_extra * 500

# monto tarifa + gigas extra consumidos
tarifa_mas_gigas = tarifa + costo_gigas_extra

# Recargo > 2TB (2048 gigas)
if cantidad_gigas_extra > 2048:
    recargo = 0.12

# desc aplicados
monto_descuento = tarifa_mas_gigas * descuento

# recargos
monto_recargo = tarifa_mas_gigas * recargo

# subtotal
subtotal = tarifa_mas_gigas + monto_recargo - monto_descuento

# iva
monto_iva = subtotal * IVA

# total a pagar
total = subtotal + monto_iva

# Mostrar:
print("\n--------- Resumen de venta ------------\n"
      f"Precio base del plan: ${tarifa}\n"
      f"Costo por espacio extra: ${costo_gigas_extra:.2f}\n"
      f"Descuentos aplicados: ${monto_descuento:.2f}\n"
      f"Recargos aplicados: ${monto_recargo:.2f}\n"
      f"IVA: ${monto_iva:.2f}\n"
      f"Total a pagar: ${total}\n"
      "\n--------- Gracias por su compra ------------\n")