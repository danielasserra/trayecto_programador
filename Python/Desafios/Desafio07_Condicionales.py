# # Daniela Serra
# # Desafío condicionales
# # Ejercicio B: "Gotita S.A."

# Facturación del Servicio de Agua Potable
# Este sistema de facturación contempla una tarifa base que incluye un cargo fijo 
# y un costo variable por metro cúbico consumido. Además, se aplican bonificaciones 
# y recargos dependiendo del consumo y la categoría del usuario. 
# En algunos casos especiales, también pueden otorgarse descuentos adicionales.
# A continuación, se detallan las reglas del sistema de facturación y los cálculos 
# necesarios para determinar el monto final a pagar.

# Precios fijos
CARGO_FIJO = 7000
METRO = 200

# Inicialización de variables
bonificacion = 0
recargo = 0

# Datos ingresados por el usuario
cliente = input("¿Es usted cliente residencial, comercial o industrial? ")
consumo = int(input("Ingrese la cantidad de agua consumida en m3: "))

# Subtotal de consumo.
metro_consumo = METRO * consumo
subtotal = metro_consumo + CARGO_FIJO

# Cliente Residencial:
if cliente == "residencial":
    if consumo < 30:
        bonificacion = 0.1
    elif consumo > 80:
        recargo = 0.15
    if subtotal < 35000:
        bonificacion += 0.05

# Cliente Comercial:
if cliente == "comercial":
    if consumo > 300:
        bonificacion = 0.12
    elif consumo > 150:
        bonificacion = 0.08
    elif consumo < 50:
        recargo = 0.05

# Cliente Industrial:
if cliente == "industrial":
    if consumo > 1000:
        bonificacion = 0.3
    elif consumo > 500:
        bonificacion = 0.2
    elif consumo < 200:
        recargo = 0.1

# bonificaciones
total_bonificaciones = subtotal * bonificacion

# recargos
total_recargos = subtotal * recargo

# Subtotal, con recargos y bonificaciones.
subtotal_final = subtotal + total_recargos - total_bonificaciones

# IVA
iva = subtotal_final * 0.21

# Total final a pagar
total = subtotal_final + iva

# Mostrar en pantalla el desglose de los cálculos.
print (f"\n----- Resumen de la venta -----\n"
       f"Subtotal de consumo: ${subtotal:.2f}\n"
       f"Bonificaciones: ${total_bonificaciones:.2f}\n"
       f"Recargos: ${total_recargos:.2f}\n"
       f"Subtotal: ${subtotal_final:.2f}\n"
       f"IVA: ${iva:.2f}\n"
       f"Total final a pagar: ${total:.2f}")