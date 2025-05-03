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
# validacion edad
while edad < 18 or edad > 90:
    print("No corresponde al rango etáreo solicitado")
    edad = int(input("Ingrese su edad (entre 18 y 90 años): "))

estado_civil = int(input("Ingrese el NUMERO correspondiente a su estado civil: \n "
                         " “1. Soltero/a” \n" 
                         " “2. Casado/a” \n" 
                         " “3. Divorciado/a” \n" 
                         " “4. Viudo/a” \n" 
                         ""))
# Validacion estado civil
while estado_civil < 1 or estado_civil > 4:
    print("No corresponde a una de las opciones")
    estado_civil = int(input("Ingrese el NUMERO correspondiente a su estado civil: \n "
                         " “1. Soltero/a” \n" 
                         " “2. Casado/a” \n" 
                         " “3. Divorciado/a” \n" 
                         " “4. Viudo/a” \n" 
                         ""))

# Mensaje estado civil
if estado_civil == 1:
    mensaje = "1. Soltero/a"
elif estado_civil == 2:
    mensaje = "2. Casado/a"
elif estado_civil == 3:
    mensaje = "3. Divorciado/a"
elif estado_civil == 4:
    mensaje = "4. Viudo"

legajo = int(input("Ingrese su numero de legajo (valor numérico de 4 cifras, sin ceros a la izquierda): "))
# validacion legajo
while legajo < 1000 or legajo > 9999:
    print("Legajo invalido. Vuelva a intentarlo")
    legajo = int(input("Ingrese su numero de legajo (valor numérico de 4 cifras, sin ceros a la izquierda): "))

print("Los datos ingresados son \n"
      f"Apellido: {apellido} \n"
      f"Edad: {edad} \n"
      f"Estado civil: {mensaje}\n"
      f"Legajo n°: {legajo}") 