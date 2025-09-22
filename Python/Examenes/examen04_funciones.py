# ----- DANIELA SERRA ----- #
   # # EXAMEN FUNCIONES # #

def pedir_nombre(mensaje:str) -> str:
    """que pida el ingreso del nombre y valide que no esté vacío.

    Args:
        mensaje (str): nombre ingresado por usuario

    Returns:
        str: nombre
    """
    while mensaje == '':
        print("El nombre no puede estar vacío. Vuelva a intentarlo")
        mensaje = input("Ingrese su nombre: ")
    return mensaje

def pedir_numero(mensaje, minimo, maximo) -> float:
    """que pida el ingreso de un número y lo valide en el rango correspondiente.

#     Args:
#         mensaje (float): numero ingresado por el usuario
#         minimo (float): numero minimo del rango
#         maximo (float): numero maximo del rango

#     Returns:
#         float: numero ingresado"""

    mensaje_fl= float(mensaje)

    while mensaje_fl < minimo or mensaje_fl > maximo:
        print(f"Respuesta inválida. El número debe estar comprendido entre {minimo} y {maximo}")
        mensaje_fl = float(input("ingrese la nota: "))
    
    return mensaje_fl

# NO SE PUEDE VALIDAR isdigit PORQUE NO ACEPTA LA COMA NI EL PUNTO PARA EL FLOAT (!)

# def pedir_numero(mensaje: float, minimo: float, maximo: float) -> float:
#     """que pida el ingreso de un número y lo valide en el rango correspondiente.

#     Args:
#         mensaje (float): numero ingresado por el usuario
#         minimo (float): numero minimo del rango
#         maximo (float): numero maximo del rango

#     Returns:
#         float: numero ingresado
#     """
    
#     
#     # while not mensaje.isdigit():
#     #     print("Respuesta invalida. No acepta letras ni caracteres especiales, sólo numeros")
#     #     mensaje = input("Ingrese la nota: ")

#     mensaje_fl = int(mensaje)
 
#     if (mensaje_fl < minimo) or (mensaje_fl > maximo):
#         print(f"Respuesta inválida. El número debe estar comprendido entre {minimo} y {maximo}")
#         mensaje = input("Ingrese la nota: ")
#         # while not mensaje.isdigit():
#         #     print("Respuesta invalida. No acepta letras ni caracteres especiales, sólo numeros")
#         #     mensaje = input("Ingrese la nota: ")
        
#         mensaje_fl = float(mensaje)

#         return mensaje_fl

def calcular_promedio(nota_uno: float, nota_dos: float, nota_tres: float) -> float:
    """que reciba las 3 notas, que calcule y retorne el promedio de las mismas.

    Args:
        nota_uno (float): nota ingresada por el usuario
        nota_dos (float): nota ingresada por el usuario
        nota_tres (float): nota ingresada por el usuario

    Returns:
        float: promedio de las tres notas
    """
    promedio = (nota_uno + nota_dos + nota_tres) / 3
    return promedio

def clasificar_promedio(promedio: float) -> str:
    """Clasificar promedio segun calificacion: Sobresaliente, Aprobado, Aplazado, Reprobado

    Args:
        promedio (float): promedio de las notas que ingreso el usuario

    Returns:
        str: Clasificación del promedio
    """
    if promedio >= 8 and promedio < 10:
        mensaje = "Sobresaliente"
    elif promedio < 8:
        mensaje = "Aprobado"    
    elif promedio < 6:
        mensaje = "Aplazado"
    elif promedio < 4:
        mensaje = "Reprobado"

    return mensaje

def mostrar_resultado(nombre: str, promedio: float, clasificacion: str):
    print("--- Resultado ---")
    print(f"Nombre: {nombre}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Clasificación: {clasificacion}")




######################


condicion = "si"

if condicion == "no":
    print("Recuerde cargar las calificaciones de sus alumnos")
else:
    while condicion == "si":

        print("\n=== Evaluador de Rendimiento Académico ===\n")
        
        ##1 nombre
        nombre = input("Ingrese nombre y apellido del alumno: ")
        resultado_pedir_nombre = pedir_nombre(nombre)

        ##2 nota
        nota_uno = float(input("Ingrese la primera nota: "))
        resultado_pedir_numero = pedir_numero(nota_uno, 1, 10)
        
        ##3 promedio
        nota_dos = float(input("Ingrese la segunda nota: "))
        nota_tres = float(input("Ingrese la tercera nota: "))
        resultado_calcular_promedio = calcular_promedio(nota_uno, nota_dos, nota_tres)

        ##4 clasificacion
        resultado_clasificar_promedio = clasificar_promedio(resultado_calcular_promedio)

        ##5 mostrar resultado
        resultado_mostrar_resultado = mostrar_resultado(resultado_pedir_nombre, resultado_calcular_promedio, resultado_clasificar_promedio)

        
        
        print(resultado_mostrar_resultado)

        condicion = input("¿Desea ingresar otro alumno? (si/no): ").lower()
        while condicion != "si" and condicion != "no":
            print("Respuesta inválida. Debe responder 'si' o 'no'")
            condicion = input("¿Desea ingresar otro alumno? (si/no): ").lower()

