################# MUESTRA EL MENU
def menu(mensaje:str)->str:
    """Muestra el menu

    Returns:
        str: menu
    """
    mensaje
    return mensaje



####### seleccionar qué tipo de entrada quiere comprar: BIEN
def pedir_numero(mensaje:str, num_min:int, num_max:int) -> int:  # min max en programa
    """Selecciona qué tipo de entrada quiere comprar

    Args:
        mensaje (str): El usuario ingresa un numero q corresponde al tipo de entrada q quiere comprar
        num_min (int): Numero mínimo elegible
        num_max (int): Numero máximo elegible

    Returns:
        int: Numero que corresponde al tipo de entrada que quiere comprar el usuario
    """

    mensaje_int = 0

    mensaje_error = ("Respuesta inválida. Inténtelo nuevamente\n"
                     f"Debe seleccionar entre {num_min} y {num_max}:\n")

    while not mensaje.isdigit():
        print(mensaje_error)
        mensaje = input("¿Qué tipo de entrada desea comprar? ")

    mensaje_int = int(mensaje)
    print(mensaje_int)
    
    while mensaje_int < num_min or mensaje_int > num_max:
        print(mensaje_error)
        mensaje = input("¿Qué tipo de entrada desea comprar? ")
        while not mensaje.isdigit():
            print(mensaje_error)
            mensaje = input("¿Qué tipo de entrada desea comprar? ")
        mensaje_int = int(mensaje)
        print(mensaje_int)
        
    return mensaje_int


###### VALIDAR NOMBRE: BIEN
def pedir_cadena(mensaje:str, mensaje_error:str) -> str: #bien
    """VALIDACIÓN: Nombre del usuario
        Pide el ingreso de una cadena que no esté vacía

    Args:
        mensaje (str): Nombre que ingresa el usuario
        mensaje_error (str): mensaje de error isalpha

    Returns:
        str: La misma cadena (nombre del usuario)
    """
    
    while not mensaje.isalpha():
        print(mensaje_error)
    
        mensaje = input("Ingrese su nombre: ")

    return mensaje

### EDAD
def es_menor(edad:str, mensaje_error:str) -> bool:
    """Indica si es menor o mayor de edad

    Args:
        edad (str): edad ingresada por el usuario
        mensaje_error (str): mensaje de error isdigit

    Returns:
        bool: True = menor, False = mayor
    """
    menor_de_edad = False
    while not edad.isdigit():
        print(mensaje_error)
        edad = input("Ingrese edad: ")
    
    edad_int = int(edad)

    if edad_int < 18:
        menor_de_edad = True
    
    return menor_de_edad

### PRECIO UNITARIO SEGUN TIPO
def calcular_precio(tipo:int) -> float:
    """PRECIO UNITARIO SEGUN TIPO

    Args:
        tipo (int): viene de pedir_numero(), ingresado x usuario

    Returns:
        float: informa el precio de la entrada elegida x el usuario
    """
    if tipo == 1:
        precio_unitario = 100
    elif tipo == 2:
        precio_unitario = 200
    elif tipo == 3:
        precio_unitario = 50
    
    return precio_unitario

def calcular_total(cantidad:str, precio_unitario: float, mensaje_error: str) -> float:
    """precio total de entradas
    cantidad x precio unitario

    Args:
        cantidad (str): ingresa usuario cantidad de entradas a comprar
        precio_unitario (float): viene de calcular_precio
        mensaje_error (str): mensaje de error isdigit

    Returns:
        float: monto total por las entradas
    """
    while not cantidad.isdigit():
        print(mensaje_error)
        cantidad = input("Reingrese la cantidad de entradas que desea comprar: ")
    
    cantidad_int = int(cantidad)

    return cantidad_int * precio_unitario

def seguir(mensaje: str, valor_esperado: str) -> bool:
    if mensaje == valor_esperado:
        return True



###########

# def comprar_entradas(nombre:str, edad: int, mensaje: str, tipo:int, cantidad:int, total:float):
#     print("\n===== VENTA DE ENTRADAS =====\n"
#           f"Nombre: {nombre}\n"
#           f"Edad: {edad}\n"
#           f"{mensaje}\n"
#           f"Elige una opcion {tipo}\n" 
#           f"¿Cuantas entradas deseas? {cantidad}\n")






# inicializacion variables

mensaje_menu = ("\n====== TIPO DE ENTRADA ======\n"
          "     1. General - $100\n" 
          "     2. VIP     - $200\n" 
          "     3. Niños   - $50"
          "\n------------------------------\n")


mensaje_error_isalpha = "Respuesta invalida. Debe contener sólo letras, sin caracteres especiales ni números"

mensaje_error_isdigit = "Respuesta inválida. Debe contener sólo numerosnum_min, sin caracteres especiales ni letras"

while True:
    #def1
    print(menu(mensaje_menu)) 
    #def2
    mensaje = input("¿Qué tipo de entrada desea comprar (1, 2, 3)? ")
    resultado_pedir_num = pedir_numero(mensaje, 1, 3)
    print("tipo de entrada", resultado_pedir_num)
    #def3
    nombre = input("nombre: ")
    resultado_pedir_cad = pedir_cadena(nombre, mensaje_error_isalpha)
    print("nombre: ", resultado_pedir_cad)
    # def4
    edad = input("edad: ")
    reultado_es_menor = es_menor(edad, mensaje_error_isdigit)
    print("edad: ", reultado_es_menor)
    # def5 precio unitario
    resultado_calcular_precio = calcular_precio(resultado_pedir_num)
    print("precio x entrada", resultado_calcular_precio)
    # def6 calc tot
    cantidad = input("¿Cuantas entradas deseas? ")
    resultado_calcular_total = (calcular_total(cantidad, resultado_calcular_precio, mensaje_error_isdigit))
    print("total ", resultado_calcular_total)
    # def7 seguir
    continuar = input("¿Desea realizar otra compra? (si/no): ").lower()
    sigue_o_no = "si"
    resultado_seguir = seguir(continuar, sigue_o_no)
    print(resultado_seguir)