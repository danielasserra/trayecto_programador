# # # Daniela Serra
# # E_S 15

# Realizar un programa que permite ingresar el nombre de un producto, 
# el precio y que calcule y muestre el IVA de dicho producto y el total a pagar.

# nombre_producto = input("Ingrese el nombre del producto: ")
# precio_producto = float(input("Ingrese el precio del producto: "))
# iva = precio_producto * 0.21

# print(f"El iva del producto es: {iva} y el total a pagar es {precio_producto}")
# supongo que el total a pagar es el precio del producto que ingresaron por input

##############################

# Daniela Serra
# E_S 16

# Realizar un programa que a partir del ingreso de un sueldo y de un porcentaje de aumento, 
# calcule y muestre el sueldo con el aumento porcentual ingresado por el usuario.

# sueldo = float(input("Ingrese el sueldo del empleado: "))
# aumento = float(input("Ingrese el aumento porcentual del empleado: "))

# sueldo_con_aumento = (sueldo * aumento / 100) + sueldo

# print(f"El sueldo con aumento es de: {sueldo_con_aumento}")

###########################################

# # Daniela Serra
# # E_S 17

# # Realizar un programa que a partir del ingreso del importe de una compra, 
# # aplique un 25% de descuento. Mostrar por pantalla cuánto es el total a pagar 
# # y cuánto fue el descuento obtenido.

# importe_compra = float(input("Ingrese el importe de la compra: "))
# descuento = importe_compra * 0.25
# total_a_pagar = importe_compra * 0.75

# print(f"El total a pagar es de: {total_a_pagar:.2f} y el descuento obtenido fue de: {descuento:.2f}")

#############################

# # Daniela Serra
# # E_S 18

# En un hospital existen tres áreas: Cardiología, Pediatría y Traumatología. 
# El presupuesto anual del hospital se reparte conforme a la siguiente tabla:
# Cardiología 40%, Pediatría 45% y Traumatologia 15%
# Necesitamos saber cuánto dinero le corresponde a cada área.		

presupuesto = float(input("Ingrese el presupuesto del hospital: "))
cardiología = presupuesto * 0.40
pediatria = presupuesto * 0.45
traumatologia = presupuesto * 0.15

print (f"Con un presupuesto de {presupuesto}: {cardiología} corresponde a Cardiología; "
       f"{pediatria} corresponde a Pediatría y "
       f"{traumatologia} corresponde a Traumatología")