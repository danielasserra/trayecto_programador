# # Daniela Serra
# # Desafío condicionales
# # Ejercicio C: "Gerflix"

# Informacion solicitada al usuario
plan = input("Tipo de plan contratado (Básico, Estándar o Premium): ").lower()
dispositivos = int(input("Cantidad de dispositivos registrados: "))
tiempo = int(input("Tiempo de suscripción en meses: "))
estudiante = input("¿Es usted estudiante? (si/no): ").lower()

# inicialización de variables y constantes
tarifa = 0 # "subtotal"
descuento = 0
recargo = 0 # > 6 dispositivos
costo_por_dispositivo = 500
IVA = 0.21

# Condiciones para descuentos y recargos:
    # Usuario Activo
if tiempo > 24:
    descuento = 0.15
elif tiempo > 12:
    descuento = 0.10

    # Plan
if plan == "basico":
    tarifa = 5000
    if estudiante == "si":
        if dispositivos > 5:
            descuento += 0.10
        elif dispositivos >= 3:
            descuento += 0.07
        else:
            descuento += 0.03

elif plan == "estandar":
    tarifa = 8000
    if estudiante == "si" or (estudiante == "no" and dispositivos == 1):
        descuento += 0.15

elif plan == "premium":
    tarifa = 12000
    if estudiante == "si" and dispositivos >= 5 and dispositivos <= 9:
        descuento += 0.20
    else:
        descuento += 0.05

    # recargo por uso excesivo: +6 dispositivos
if dispositivos > 6:
    recargo = 0.20

# Precio por dispositivos
precio_dispositivos = dispositivos * costo_por_dispositivo

# precio base + dispositivos
tarifa_total = tarifa + precio_dispositivos

# Monto de descuentos y Recargos:
monto_descuento = tarifa_total * descuento
monto_recargo = tarifa_total * recargo
monto_iva = tarifa_total * IVA

# Subtotal con descuentos y recargos aplicados
subtotal = tarifa_total - monto_descuento + monto_recargo

# Total con IVA
total = subtotal + monto_iva

print("\n------ Resumen de la venta ------\n"
      f"\nPrecio base del plan ${tarifa:.2f}\n"
      f"Recargo por dispositivos adicionales ${precio_dispositivos:.2f}\n"
      f"Descuentos ${monto_descuento:.2f}\n"
      f"IVA aplicado ${monto_iva:.2f}\n"
      f"Total a pagar ${total:.2f}\n"
      "\n----- Gracias por su compra -----\n")