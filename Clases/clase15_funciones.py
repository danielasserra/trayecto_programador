# clase 15 Funciones

# Minificamos para que sea mas facil leerlo
# Si logro dividir el programa en fn mas pequeñas (modulos), es mas facil detectar errores
# reutilizacion: puedo utilizar la funcion en distintas circunstancias
# independencia: qué tan independiente es la fn. Depende de otras fns?
#                   buscar balance entre acoplamiento y cohesion.
#               no esta acoplada: no le importa de donde vienen los parametros ni el retorno
# anatomia: palabra reservada "def"
#           nombre snake case minuscula
#           verbo en infinitivo para diferenciar el nombre de funcion del de variable

# definicion y desarrollo: creo la funcion
# llamada: invocacion de la funcion

# #--------------------------------------

# # cada parametro definido se llama "parametro formal", siempre es el mismo
# # y el que yo le paso es "parametro actual"
# # el parametro actual es el que va a cambiar, puede  haber mas de uno

# def restar(numero_a, numero_b):
#     resultado = numero_a - numero_b
#     return resultado

# # al llamar la fn
# primer_numero = 5
# segundo_numero = 3
# r = restar(primer_numero,segundo_numero)
# print(r)
# # el parametro actual viaja por un tubito hasta el parametro formal A y el 3 al parametro formal B
# # EL PASAJE DE PARÁMETROS ES POSICIONAL: la posicion en que ubico los parámetros importa

# # se puede revertir el pasaje de parámetros posicional en Python
# # Python permite recibir parametros por nombre
# r = restar(numero_b=segundo_numero, numero_a=primer_numero)
# print(r)

# #-------------------------------------

# ----------------------------------------- #
###---------- PARAMETRO OPCIONAL ----------###
# ----------------------------------------- #

# def crear_boton(fondo, fondo_seleccionado, borde, borde_seleccionado, texto, texto_seleccionado):
#     print("algo")

# crear_boton("rojo", "azul", "amarillo", "verde", "violeta", "naranja")

# # pasar parametros x nombre para no equivocarme cuando son demasiados parámetros
# # hace legible el código, dejo impactado a qué parámetro corresponde cada valor.

# crear_boton(fondo = "rojo",
#             fondo_seleccionado= "azul",
#             borde="amarillo",
#             borde_seleccionado="verde",
#             texto="violeta",
#             texto_seleccionado="naranja")

# # puedo decir q el color de texto seleccionado es opcional. EJ
# def crear_boton(fondo, fondo_seleccionado, borde, borde_seleccionado, 
#                 texto, texto_seleccionado = "Negro"):
#     print("algo")
# # Significa q si no paso el parámetro de texto seleccionado, no pasa nada, es opcional. EJ
# crear_boton(fondo = "rojo",
#             fondo_seleccionado= "azul",
#             borde="amarillo",
#             borde_seleccionado="verde",
#             texto="violeta")


# #-------------------------------------------

# # ----------------------------------------- #
# ###---------- PARAMETRO OPCIONAL ----------###
# # ----------------------------------------- #

# ##### OTRO EJEMPLO ########

# def calcular_precio_con_iva(valor_sin_iva):
#     resultado = valor_sin_iva * 1.21
#     return resultado
# print(calcular_precio_con_iva(1000))

# def calcular_precio_con_iva(valor_sin_iva, iva):
#     resultado = valor_sin_iva * (1+(iva/100))
#     return resultado
# print(calcular_precio_con_iva(1000, 21))
# print(calcular_precio_con_iva(1000, 10.5))


# # el iva mayormente es 21%, así que lo dejamos opcional:
# def calcular_precio_con_iva(valor_sin_iva, iva = 21):
#     resultado = valor_sin_iva * (1+(iva/100))
#     return resultado
# print(calcular_precio_con_iva(1000))
# print(calcular_precio_con_iva(1000, 10.5))

# # ------------------------------------------ #
# ###---------- PARAMETRO OPCIONAL ----------###

# #---- parametro formal con valor por defecto, se transforma en un valor opcional #----

# #-- Del lado derecho de un parametro opcional, no pueden haber parametros obligatorios #--

# # No es una muy buena práctica pasar parámetros opcionales

# # ------------------------------------------ #


# # Python no es lenguaje declarativo (declarar y tipar variable)
# contador = 0 

# # En C:
# # int contador = 0

# # EJ

# def saludar_alumno(nombre, apellido, altura_cms, edad):
#     altura_mts = altura_cms / 100
#     print(f"El alumno se llama {nombre} {apellido}, tiene {edad} años y mide {altura_cms} metros")

# #############

# # Llamar funcion

# nombre = "Juan"
# apellido = "Gomez"
# edad = 23
# altura = "179" # Error, tipo de dato str en vez de int

# saludar_alumno(nombre, apellido, altura, edad)

# # El error en la fn es no indicar qué tipo de dato se está esperando.
# # En la mayoria de los lenguajes, a la variable ponerle el tipo de dato que representa
# # En Python no. Pero Python me deja ADORNAR

# # ------------------------------------------- #
# # -------------    ADORNOS    --------------- #
# # ------------------------------------------- #

# def saludar_alumno(nombre: str, apellido: str, altura_cms: int, edad: int): # ADORNOS
#     altura_mts = altura_cms / 100
#     print(f"El alumno se llama {nombre} {apellido}, tiene {edad} años y mide {altura_mts} metros")

# nombre = "Juan"
# apellido = "Gomez"
# edad = 23
# altura = int("179")
# saludar_alumno(nombre, apellido, altura, edad)

# # SI NO PONGO NADA, DEVUELVE "NONE"
# # SI NO PONGO NADA, DEVUELVE EL RETURN
# saludar_alumno()

# # ------------------------------------------------------------------

# # Return bool:

# def saludar_alumno(nombre: str, apellido: str, altura_cms: int, edad: int) -> bool: # ADORNOS
#     if type (altura_cms) == int:
#         altura_mts = altura_cms / 100
#         print(f"El alumno se llama {nombre} {apellido}, tiene {edad} años y mide {altura_mts} metros")
#     else:
#         print("Hubo un error")


# # No conviene hacerlo así

# ########### MEJOR:

# def saludar_alumno(nombre: str, apellido: str, altura_cms: int, edad: int) -> bool: # ADORNOS
#     exito = False
#     if type (altura_cms) == int:
#         altura_mts = altura_cms / 100
#         print(f"El alumno se llama {nombre} {apellido}, tiene {edad} años y mide {altura_mts} metros")
#         exito = True
    
#     return exito

# nombre = "Juan"
# apellido = "Gomez"
# edad = 23
# altura = int("179")
# saludar_alumno(nombre, apellido, altura, edad)

# if not saludar_alumno:
#     print("hubo un error")

# ### ASI ES COMO PYTHON COMPRUEBA QUE NO HAYA ERROR EN LOS TIPOS DE DATOS


# # -----------------------------------------------------------------------------------------


# #           # ------------------------------------------- #
# # # -------------    VARIABLES LOCALES Y GLOBALES    --------------- #
# #           # ------------------------------------------- #

# def funcion():
#     variable = 5 # alcance de una variable
#     print(numero)

# ############ FUERA DE LA FN ###############

# # Cualquier variable que declaro fuera de la funcion, puede verla la fn
# numero = 5 # no esta bien
# funcion()

# #### MUY MALA PRACTICA DECLARAR VARIABLE GLOBAL
# ## si desaparece la variable, se rompe la fn

# # Esta fn está acoplada al módulo main, especificamente a la variable. Si desaparece, deja de funcionar

# # NO USAMOS VARIABLES GLOBALES
# # GENERAN GRADO PATOLÓGICO DE ACOPLAMIENTO

# #----------- FORMA CORRECTA:
# funcion(5)

# # ---------------------------------------
# def funcion():
#     numero = 1000 # alcance de una variable
#     print(numero) 

# numero = 5
# print(numero) # muestra 5
# funcion() # llama a la fn, vale 1000
# print(numero) # sale de la fn, vale 5



# ################################

# ## DECLARAR VARIABLE GLOBAL

# def funcion():
#     global numero 
#     numero = 1000 # alcance de una variable
#     print(numero) 

# numero = 5
# print(numero) # muestra 5
# funcion() # llama a la fn, vale 1000
# print(numero) # sale de la fn, vale 1000

# # -------------------------------------------------------------

# #           # ------------------------------------------- #
# # # -------------    DOCUMENTACION    --------------- #
# #           # ------------------------------------------- #

# Cada lenguaje trae herramientas para poder documentar
# extensiones "autodocstring"
# Si la fn está bien adornada, toma los adornos como referencia
# Con tres juegos de comillas, lo completa automáticamente
# Al llamar a la fn, además de los adornos, me muestra la info que proporciono
# Borrar lo que puso autodoc y escribir lo que corresponda
### TODAS LAS FN TIENEN QUE ESTAR DOCUMENTADAS ###
# EJEMPLO

def saludar_alumno(nombre: str, apellido: str, altura_cms: int, edad: int) -> bool: # ADORNOS
    """_summary_ 
    ------------- ACA VA LA DESCRIPCION DE LA FN. ------------------
    EJ. Muestra los datos del estudiante con la altura en Mts.

    Args:
    -------------- DESCRIPCION DE LOS PARÁMETROS DE ENTRADA -----------
        nombre (str): _description_
        apellido (str): _description_
        altura_cms (int): ------- altura del estudiante en cms --------
        edad (int): _description_

    Returns:
    ------------- QUÉ DEVUELVE LA FN? QUÉ SIGNIFICA? ----------------------
        bool: _description_
        -------- EJ. True si está todo bien. False si hay errores ----------
    """
    exito = False
    if type (altura_cms) == int:
        altura_mts = altura_cms / 100
        print(f"El alumno se llama {nombre} {apellido}, tiene {edad} años y mide {altura_mts} metros")
        exito = True

saludar_alumno()


