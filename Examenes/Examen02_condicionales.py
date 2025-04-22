# Daniela Serra
# Examen Condicionales
# 21/04/25

# Datos ingresados por el usuario
categoria = input("Ingrese la categoría de su restaurante (🥗 'Económico', 🍔 'Estándar' o 🍷 'Gourmet'): ").lower()
ingresos = float(input("¿Cuáles son sus ingresos totales en dólares? U$D"))
dia_mas_pedidos = input("¿Cuál es el día con más pedidos (fin de semana o dia laboral)? ")

# Inicialización de variables
comision = 0
bonificacion = 0
mensaje = ""

# Comisión
if categoria == "economico":
    comision = 0.18
elif categoria == "estandar":
    comision = 0.12
elif categoria == "gourmet":
    comision = 0.08

# Bonificación por Día con Más Pedidos:
if dia_mas_pedidos == "fin de semana":
    bonificacion = 0.05

# Ingresos Netos: 🧮 Se calculan restando la comisión y sumando la bonificación (si aplica).
monto_comision = ingresos * comision
monto_bonificacion = ingresos * bonificacion
ingresos_netos = ingresos - monto_comision + monto_bonificacion

# 🎁 Beneficio Especial:

if ingresos_netos > 10000:
    mensaje = "El restaurante recibe una campaña de marketing gratuita 📈"
elif ingresos_netos >= 5000:
    mensaje = "El restaurante recibe un paquete promocional de descuentos 🎫"
else:
    mensaje = "No se otorgan beneficios adicionales" 

# El sistema debe mostrar en pantalla:
print(f"Ingresos netos: ${ingresos_netos:.2f}\n"
      f"Beneficio Especial: {mensaje}")