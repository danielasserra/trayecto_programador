# Daniela Serra
# Integrador Validaciones.

# Una empresa dedicada a la toma de datos para realizar estadísticas y censos,
# nos pide realizar la carga y validación de datos.
 
# Los datos requeridos son:
# Apellido 
# Edad, entre 18 y 90 años inclusive.
# Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

# Una vez ingresados y validados los datos, mostrarlos por pantalla.

apellido = input("Ingrese su apellido: ").capitalize()

edad = int(input("Ingrese su edad (entre 18 y 90 años): "))
# Validacion edad
while edad < 18 or edad > 90:
    print("El rango etareo ingresado es incorrecto. Vuevla a intentarlo.")
    edad = int(input("Ingrese su edad (entre 18 y 90 años): "))


estado_civil = int(input("Seleccione el numero correspondiente a su estado civil: \n"
                        "1. “Soltero/a”\n"
                        "2. “Casado/a”\n"
                        "3. “Divorciado/a”\n"
                        "4. “Viudo/a”\n"))
# Vallidación Estado Civil
while estado_civil < 1 or estado_civil > 4:
    print("Respuesta inválida. Debe seleccionar un número del 1 al 4, correspondiente a su Estado Civil")
    estado_civil = int(input("Seleccione el numero correspondiente a su estado civil: \n"
                        "1. “Soltero/a”\n"
                        "2. “Casado/a”\n"
                        "3. “Divorciado/a”\n"
                        "4. “Viudo/a”\n"))
# Mensaje de salida Estado Civil
if estado_civil == 1:
    mensaje = "1. “Soltero/a”"
if estado_civil == 2:
    mensaje = "2. “Casado/a”"
if estado_civil == 3:
    mensaje = "3. “Divorciado/a”"
if estado_civil == 4:
    mensaje = "4. “Viudo/a”"

legajo = int(input("Ingrese su numero de legajo (valor numérico de 4 cifras, sin ceros a la izquierda): "))
while legajo < 1000 or legajo > 9999:
    print("Respuesta inválida. El legajo debe ser un número entre 1000 y 9999. Inténtelo nuevamente.")
    legajo = int(input("Ingrese su numero de legajo (valor numérico de 4 cifras, sin ceros a la izquierda): "))


print("\n---------- Sus datos ----------\n" 
      f"\nApellido: {apellido}\n"
      f"Edad: {edad}\n"
      f"Estado Civil: {mensaje}\n"
      f"Legajo n°: {legajo}\n"
      "\n--------------------------------")
