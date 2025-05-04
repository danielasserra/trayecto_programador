# Daniela Serra
# Integrador Repetitivas. Encuesta de hábitos de lectura

# Una biblioteca pública realiza una encuesta a sus visitantes. 
# No se sabe cuántos encuestados habrá, pero se desea registrar 
# los siguientes datos por persona:

# Nombre
# Edad (mayor o igual a 12 años)
# Cantidad de libros leídos en el último año (0 o más)

# Al finalizar, mostrar:
# - 📘 Nombre del encuestado que más libros leyó
# - 📕 Nombre y edad del que menos libros leyó
# 📊 Promedio de libros leídos por persona
# - 👥 Cantidad total de encuestados
# 📈 Porcentaje de personas que leyeron más de 10 libros

# Inicialización de variables
condicion = "si" # desea ingresar datos
bandera_primera = True # primer vuelta del bucle
suma_libros = 0 # total de libros leidos
mas_libros = 0 # leyó más libros (maximo)
menos_libros = 0 # leyó menos libros (mínimo)
nombre_mas_libros = "" # nombre de quien leyó más libros
nombre_menos_libros = "" # nombre de quien leyó menos libros
edad_menos_libros = 0 # edad de quien leyó menos libros
promedio_libros = 0 # promedio de libros leídos por persona
mas_diez = 0 # 📈 Porcentaje de personas que leyeron más de 10 libros
i = 0 # total de encuestados
i_diez = 0 # encuestados que leyeron diez libros o más


print("\n***** ✍️  Bienvenido a la encuesta para visitantes de la Biblioteca ✍️  *****\n")

condicion = input("¿Desea responder la encuesta? (si/no): ")
while condicion != "si" and condicion != "no":
    print("Respuesta inválida. Debe ser 'si' o 'no'. Inténtelo nuevamente")
    condicion = input("¿Desea responder la encuesta? (si/no): ")

# si responde que no
if condicion == "no":
    print("\n🙌 Esperamos que pueda responder la encuesta en otra ocasión 🙌\n")

# si responde que sí
elif condicion == "si":

    # bucle: mientras la condición sea sí...
    while condicion == "si":
        
        nombre = input("Ingrese su nombre: ").capitalize()
        
        edad = int(input("Ingrese su edad: "))
        while edad < 12:
            print("No tiene la edad mínima necesaria para responder la encuesta. Inténtelo nuevamente.")
            edad = int(input("Ingrese su edad: "))
        
        libros_leidos = int(input("Ingrese la cantidad de libros leídos en el último año: "))
        while libros_leidos < 0:
            print("Respuesta inválida. La cantidad de libros leídos no puede ser negativa. Inténtelo nuevamente.")
            libros_leidos = int(input("Ingrese la cantidad de libros leídos en el último año: "))


        # si es la primera vuelta del bucle
        if bandera_primera == True:
            # establecer máx y min
            mas_libros = libros_leidos
            menos_libros = libros_leidos

            nombre_mas_libros = nombre # nombre de quien leyó más libros
            nombre_menos_libros = nombre # nombre de quien leyó menos libros
            edad_menos_libros = edad # edad de quien leyó menos libros
            
            bandera_primera = False # apagar bandera primera vuelta del bucle

        # comparar y establecer nuevo máximo y nombre
        if mas_libros < libros_leidos:
            mas_libros = libros_leidos
            nombre_mas_libros = nombre

        # comparar y establecer nuevo minimo, edad y nombre
        if menos_libros > libros_leidos:
            menos_libros = libros_leidos
            nombre_menos_libros = nombre
            edad_menos_libros = edad

        # cantidad de encuestados que leyeron más de 10 libros
        if libros_leidos > 10:
            i_diez += 1

        # Cantidad total de libros leídos
        suma_libros += libros_leidos

        # cantidad total de encuestados
        i += 1

        # continuar o finalizar bucle
        condicion = input("¿Desea cargar otra respuesta? (si/no): ")
        while condicion != "si" and condicion != "no":
            print("Respuesta inválida. Debe responder 'si' o 'no'. Inténtelo nuevamente.")
            condicion = input("¿Desea cargar otra respuesta? (si/no): ")

    # Dentro de ELIF fuera de WHILE

    # 📊 Promedio de libros leídos por persona
    promedio_libros = suma_libros / i

    # 📈 Porcentaje de personas que leyeron más de 10 libros
    mas_diez = i_diez * 100 / i

    # Mostrar por consola
    print("\n---------------------- Resultado de la encuesta -----------------------\n"
          f"\n📘 Nombre del encuestado que más libros leyó: {nombre_mas_libros}\n"
          f"📕 Nombre del que menos libros leyó: {nombre_menos_libros}\n"
          f"📅 Edad del que menos libros leyó: {edad_menos_libros}\n"
          f"📊 Promedio de libros leídos por persona: {promedio_libros:.2f}\n"
          f"👥 Cantidad total de encuestados: {i}\n"
          f"📈 Porcentaje de personas que leyeron más de 10 libros: {mas_diez:.2f}\n"
          "\n---------------------- Gracias por participar --------------------------\n")