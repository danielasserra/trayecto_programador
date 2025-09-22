# Daniela Serra
# Anexo 1

# Crear un programa que permita cargar datos de ventas hasta que el usuario 
# indique que desea finalizar. Por cada venta, se debe pedir:
# Nombre del vendedor (no puede estar vacío ni tener menos de 3 caracteres)
# Legajo de vendedor (deben ser un número entero y tiene que tener 4 dígitos)
# Monto de venta (debe ser mayor a 0)
# Tipo de producto vendido (A, B, o C) 
# Comisiones por tipo:
# "A": 10%
# "B": 15%
# "C": 20%
# Al finalizar, mostrar:
# Nombre y legajo de vendedor 
# Comisión total pagada
# Valor total de venta
# Que tipo de producto vendio y que porcentaje de comisión le corresponde



# Inicio proceso

condicion = input("¿Desea cargar sus ventas? (si/no): ").lower()
while condicion != "si" and condicion != "no":
    print("Respuesta inválida. Debe ser 'si' o 'no'. Inténtelo nuevamente")
    condicion = input("¿Desea cargar sus ventas? (si/no): ").lower()

if condicion == "no":
    print("No olvide cargar sus ventas a la brevedad")

# si la condicion es si:
elif condicion == "si":

    # mientras la condicion sea si:
    while condicion == "si":

        # Variables
        comision = 0
        legajo_valido = False # bandera para el while
        monto_valido = False # bandera para validar el monto

        #ingrese nombre
        nombre = input("Ingrese el nombre del vendedor (no puede estar vacio ni tener menos de 3 caracteres): "). capitalize()
        
        # Validación nombre
        while len(nombre) < 3:
            print("Nombre inválido. Debe tener más de tres caracteres. Inténtelo nuevamente")
            nombre = input("Ingrese el nombre del vendedor (no puede estar vacio ni tener menos de 3 caracteres): ").capitalize()
        
        # Ingreso y Validacion Legajo
        
        while legajo_valido == False:

            # Ingreso de datos
            legajo = input ("Ingrese el legajo del vendedor (deben ser un número entero y tiene que tener 4 dígitos): ")

            # Si legajo no es un numero:
            if not legajo.isdigit():
                print("Numero de legajo inválido. Debe contener sólo dígitos.")
                
            # si no / Si es un numero
            else:
                # convertir str a int
                legajo = int(legajo)

                # si legajo es mayor a 1000 o menor a 9999
                if legajo >= 1000 and legajo <= 9999:
                    legajo_valido = True

        # Ingreso del monto de venta
        monto = input("Ingrese el monto de venta: ")
        
        # Validación del monto, que sea numero > 0
        while monto_valido == False:
            if monto.isdigit():
                monto = float(monto)

                if monto > 0:
                    monto_valido = True
                else:
                    print("El monto no puede ser negativo. Inténtelo nuevamente")
                    monto = input("Ingrese el monto de venta: ")
            else:
                print("El monto sólo debe contener numeros. Inténtelo nuevamente")
                monto = input("Ingrese el monto de venta: ")


        producto = input("Ingrese el tipo de producto vendido (A, B, C): ").upper()
        # Validacion de producto
        while producto != "A" and producto != "B" and producto != "C":
            print("Producto inválido. Inténtelo nuevamente")
            producto = input("Ingrese el tipo de producto vendido (A, B, C): ").upper()

        if producto == "A":
            comision = 0.10
        elif producto == "B":
            comision = 0.15
        elif producto == "C":
            comision = 0.20

        # Comision total pagada
        comision_total = monto * comision

        # valor total de la venta
        valor_venta = monto + comision_total
        
        print("\n------------- Detalles de la venta ----------------\n"
            f"Nombre del vendedor: {nombre}. Legajo n° {legajo}\n"
            f"Comision total pagada {comision_total:.2f}\n"
            f"Valor total de la venta {valor_venta:.2f}\n"
            f"El tipo de producto vendido es {producto} y el porcentaje de comision que le corresponde es {comision:.2f}\n"
            "------------------------------------------------------")
            
        condicion = input("¿Desea cargar más ventas? (si/no): ").lower()
        while condicion != "si" and condicion != "no":
            print("Respuesta inválida. Inténtelo nuevamente")
            condicion = input("¿Desea cargar más ventas? (si/no): ").lower()
    
    