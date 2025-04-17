# Daniela Serra
# Desafío 3: Cálculo del Costo de Suscripción a un Servicio de Streaming

# Se ingresan los siguientes datos de un usuario: tipo de suscripción, antigüedad en la plataforma, 
# cantidad de horas de contenido consumido y el costo por hora. A partir de esta información, 
# se debe calcular y mostrar en pantalla:
# Costo Base: Se calcula multiplicando la cantidad de horas consumidas por el costo correspondiente por hora.
# Impuesto por Plataforma: Corresponde al 3% del costo base.
# Impuesto por Contenido Licenciado: Representa el 11% del costo base.
# Bono de Fidelidad: Representa el 10% del costo luego de descontarse los impuestos mencionados.
# Costo Final: Es el monto que pagará el usuario luego de aplicarse los impuestos y el bono de fidelidad.

#entradas
tipo_de_suscripcion = input("Ingrese el tipo de suscripción: ")
antiguedad_en_plataforma = float(input("Ingrese su antiguedad en la plataforma: "))
horas_contenido_consumido = float(input("Ingrese la cantidad de horas de contenido consumido: "))
costo_hora = float(input("Ingrese el costo por hora: "))

#proceso
costo_base = horas_contenido_consumido * costo_hora
impuesto = costo_base * 0.03
impuesto_contenido_licenciado = costo_base * 0.11
bono_fidelidad = costo_base * 0.10
costo_final = costo_base + impuesto + impuesto_contenido_licenciado - bono_fidelidad

# salida
print(f"El costo base del servicio es: {costo_base}. \n"
      f"El impuesto por plataforma es: {impuesto}. \n"
      f"El impuesto por contenido licenciado es: {impuesto_contenido_licenciado}. \n"
      f"El bono de fidelidad es {bono_fidelidad}. \n"
      f"El costo final es {costo_final}.")