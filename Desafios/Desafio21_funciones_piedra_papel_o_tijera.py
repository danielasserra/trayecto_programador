
# Piedra, Papel o Tijera - Desafío de Programación

# El clásico juego de la infancia, donde dos jugadores eligen entre tres elementos 
# y la victoria se determina según las siguientes reglas:
# Piedra aplasta Tijera → 🏆 Gana la Piedra
# Tijera corta Papel → 🏆 Gana la Tijera
# Papel envuelve Piedra → 🏆 Gana el Papel
# Si ambos jugadores eligen el mismo elemento, la ronda termina en empate.

# 📌 Reglas del Juego
# La partida se juega al mejor de 3 rondas.
# Si un jugador (humano o máquina) logra dos aciertos seguidos, 
# la partida finaliza automáticamente.
# En caso de empate en las 3 rondas, el juego continuará hasta que haya un ganador.

# ------------------------------------------------------------------------------------#
# --------------------------- DECLARACION DE FUNCIONES -------------------------------#
# ------------------------------------------------------------------------------------#

import random

def verificar_ganador_ronda(jugador:int, maquina:int) -> str:
    """Determina quién ganó la ronda según las elecciones del jugador y la máquina.


    Args:
        jugador (int): Elección del jugador (1 para Piedra, 2 para Papel, 3 para Tijera).
        maquina (int): Elección de la máquina (1 para Piedra, 2 para Papel, 3 para Tijera).

    Returns:
        str: 
            "Jugador" → Si el jugador gana la ronda.
            "Máquina" → Si la máquina gana la ronda.
            "Empate" → Si ambos eligen el mismo elemento.

    """
    if jugador == maquina:
        resultado = "Empate"

    if (jugador == 1 and maquina == 3) or \
       (jugador == 2 and maquina == 1) or \
       (jugador == 3 and maquina == 2):
        resultado = "Jugador"
    else:
        resultado = "Maquina"
    
    return resultado
        


def verificar_estado_partida(aciertos_jugador: int, aciertos_maquina: int, ronda_actual: int) -> bool:
    """Determina si la partida sigue en curso o ya ha finalizado

    Args:
        aciertos_jugador (int): Cantidad de rondas ganadas por el jugador
        aciertos_maquina (int): Cantidad de rondas ganadas por la máquina.
        ronda_actual (int): Número de la ronda actual.

    Returns:
        bool: 
            True → Si la partida sigue en curso.
            False → Si la partida ha finalizado (porque alguien ganó dos veces seguidas o se jugaron todas las rondas).
    """
    estado_partida = True

    if ronda_actual < 2:
        pass
    elif ronda_actual == 2 and (aciertos_jugador == 2 or aciertos_maquina == 2):
        estado_partida = False #esta parte no es necesaria, se deja para reforzar entendimiento
    elif aciertos_maquina == aciertos_jugador:
        estado_partida = True
    else:
        estado_partida = False
    
    return estado_partida


def verificar_ganador_partida(aciertos_jugador: int, aciertos_maquina: int) -> str:
    """Determina quién ganó la partida comparando los aciertos finales.


    Args:
        aciertos_jugador (int): Cantidad de rondas ganadas por el jugador.
        aciertos_maquina (int): Cantidad de rondas ganadas por la máquina

    Returns:
        str: 
            "Jugador" → Si el jugador tiene más aciertos.
            "Máquina" → Si la máquina tiene más aciertos.

    """

    if aciertos_jugador > aciertos_maquina:
        ganador_partida = "Jugador"
    elif aciertos_jugador < aciertos_maquina:
        ganador_partida = "Maquina"
    else:
        ganador_partida = "Empate"

    return ganador_partida


def mostrar_elemento(eleccion:int) -> str:
    """Convierte la elección numérica en un texto legible.

    Args:
        eleccion (int): Número de elección (1 para Piedra, 2 para Papel, 3 para Tijera)

    Returns:
        str: 
            "Piedra" cuando su elección == 1.
            "Papel" cuando su elección == 2.
            "Tijera" cuando su  elección == 3.

    """
    elemento = ""
    if eleccion == 1:
        elemento = "Piedra"
    elif eleccion == 2:
        elemento = "Papel"
    elif eleccion == 3:
        elemento = "Tijera"
    return elemento


def jugar_piedra_papel_tijera() -> str:

    # Inicia una partida donde el jugador compite contra la máquina.
    

    print("¡Bienvenido a Piedra, Papel o Tijera!")
    
    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda_actual = 0

    while verificar_estado_partida(aciertos_jugador,aciertos_maquina,ronda_actual) == True:
        
            ronda_actual += 1

            # En cada ronda, el jugador elige una opción y la máquina genera una elección aleatoria.
            jugador = int(input("\nIngrese su eleccion (1 para Piedra, 2 para Papel, 3 para Tijera): "))
            # validación 
            while jugador < 1 or jugador > 3:
                print("Respuesta inválida. Inténtelo nuevamente.")
                jugador = int(input("\nIngrese su eleccion (1 para Piedra, 2 para Papel, 3 para Tijera): "))
            print(f"\nEl jugador ha elegido {mostrar_elemento(jugador)}")

            # Se recomienda usar random.randint(1,3) para la elección de la máquina.
            maquina = random.randint(1, 3)
            print(f"\nLa máquina ha elegido {mostrar_elemento(maquina)}")

            if verificar_ganador_ronda(jugador, maquina) == "Jugador":
                aciertos_jugador += 1
            elif verificar_ganador_ronda(jugador, maquina) == "Maquina":
                aciertos_maquina += 1

            print(f"\nHa ganado la ronda {ronda_actual}: {verificar_ganador_ronda(jugador, maquina)}")
            print(f"aciertos_maquina = {aciertos_maquina}, aciertos jugador = {aciertos_jugador}")

    return verificar_ganador_partida(aciertos_jugador,aciertos_maquina)

ganador = jugar_piedra_papel_tijera()

print(f"El ganador de la partida es {ganador}")




# 📌 Requisitos del Código
# ✅ Todas las funciones deben estar correctamente modularizadas.
# ✅ Se debe validar que el jugador solo ingrese valores válidos (1, 2 o 3).
# ✅ Se deben manejar posibles errores de entrada de datos.
# ✅ Se recomienda usar random.randint(1,3) para la elección de la máquina.
# ✅ Mostrar mensajes claros en cada ronda indicando los elementos elegidos y el estado de la partida.
# ✅ Crear tantos módulos como considere necesario y reutilizar los propios.


