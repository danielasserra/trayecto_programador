# Daniela Serra
# Examen 21/04/25
# 
# Cálculo del Costo de Membresía en un Gimnasio
# Un gimnasio ofrece diferentes planes en su membresía. 
# Para calcular el costo mensual de un usuario, se solicitan los siguientes datos: 
# tipo de membresía, tiempo de afiliación(cantidad de meses) y cantidad de horas de 
# entrenamiento utilizadas. La tarifa por hora es de $1500. 
# Con esta información, se deben calcular y mostrar los siguientes valores:

# Datos que ingresa el usuario
tipo_membresia = input("Ingrese el tipo de membresía: ").title()
tiempo_afiliacion = int(input("Ingrese el tiempo de afiliación en meses: "))
horas_entrenamiento = float(input("Ingrese la cantidad de horas de entrenamiento utilizadas: "))

#  La tarifa por hora es de $1500
tarifa = 1500

# Costo Base: Se obtiene multiplicando la cantidad de horas de entrenamiento por la tarifa por hora.
costo_base = horas_entrenamiento * tarifa

# Impuesto por Mantenimiento: Corresponde al 5% del costo base.
impuesto_mantenimiento = costo_base * 0.05

# Impuesto por Servicios Adicionales: Representa el 8% del costo base.
impuesto_servicios_adicionales = costo_base * 0.08

# Descuento por temporada: Se aplica un 12% sobre el monto total luego de los impuestos.
costo_mas_impuestos = costo_base + impuesto_mantenimiento + impuesto_servicios_adicionales
descuento_temporada = costo_mas_impuestos * 0.12

# Adicional por bebidas: Se cobra un plus de $1200 diarios (días hábiles) 
# en concepto de bebidas energéticas.
bebidas = 1200 * 5 * 4 # 5 días hábiles, 4 semanas

# Costo Mensual: Es el monto total que pagará el usuario luego de aplicar impuestos, 
# descuentos y adicionales.

costo_mensual = costo_mas_impuestos - descuento_temporada + bebidas

# Costo final: Sale de multiplicar el costo mensual por el tiempo de la afiliación.
costo_final = costo_mensual * tiempo_afiliacion

# El print debe tener una sola variable y se debe informar el tipo de membresía, 
# los valores por separado de cada costo y por último el costo final

mensaje = f"El tipo de membresía es {tipo_membresia}. \n"
mensaje += f"Los valores de cada categoría son: \n"
mensaje += f" - Tarifa por hora {tarifa} \n"
mensaje += f" - Costo base {costo_base} \n"
mensaje += f" - Impuesto por mantenimiento {impuesto_mantenimiento} \n"
mensaje += f" - Impuesto por servicios adicionales {impuesto_servicios_adicionales} \n"
mensaje += f" - Descuento por temporada {descuento_temporada} \n"
mensaje += f" - Adicional por bebidas {bebidas} \n"
mensaje += f" - Costo mensual {costo_mensual} \n"
mensaje += f" - Costo final {costo_final}"


print(f"{mensaje}")