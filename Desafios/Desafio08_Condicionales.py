# # Daniela Serra
# # Desafío condicionales
# # Ejercicio A: "Corto"

# El supermercado CORTOⓇ necesita un programa que calcule el total a pagar por un cliente,
# aplicando impuestos y descuentos según el tipo de cliente y el monto de compra.

# Datos ingresados por el cliente

cliente = input("Ingrese el tipo de cliente (VIP, regular, empleado): ").lower()
productos = int(input("Ingrese la cantidad de productos: "))
gasto = float(input("Ingrese el monto de la compra: ")) # total antes de impuestos

# inicializacion de variables
descuento = 0
IVA = 0.21


# condiciones
if gasto < 50000 and productos > 15:
    descuento = 0.05
elif cliente == "vip":
    if gasto >= 80000:
        descuento = 0.15
        if productos > 20:
            descuento += 0.05
elif cliente == "regular":
    if gasto >= 100000 or productos > 25:
        descuento = 0.10
elif cliente == "empleado":
    descuento = 0.20

# monto de descuento / desc aplicado
monto_descuento = gasto * descuento

# monto total antes de impuestos / subtotal con desc
subtotal = gasto - monto_descuento

# monto de iva
monto_iva = subtotal * IVA

# total con iva
total = subtotal + monto_iva

# Mostrar en pantalla el desglose del cálculo
print (f"\n----- Resumen de la venta -----\n"
       f"\nTipo de cliente: {cliente}\n"
       f"Cantidad de productos comprados: {productos}\n"
       f"Monto total de la compra: ${gasto:.2f}\n"
       f"Descuento aplicado: ${monto_descuento:.2f}\n"
       f"Subtotal: ${subtotal:.2f}\n"
       f"IVA: ${monto_iva:.2f}\n"
       f"Total final a pagar: ${total:.2f}\n"
        "\n-------------------------------")