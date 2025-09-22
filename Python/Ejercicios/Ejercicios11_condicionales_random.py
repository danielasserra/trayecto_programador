# # Daniela Serra
# # Condicionales con random
# # Ejercicio F: "Combate Épico"

# Objetivo: Simular un combate simple entre un jugador y un enemigo aleatorio, 
# usando condicionales y valores generados con la librería random.

import random

print("Bienvenido a ⚔️*Combate Epico*⚔️")

# Jugador 
jugador = input("Ingresá tu nombre: ").capitalize()
vida_jugador = random.randint(80, 120)
ataque_jugador = random.randint(15, 30)

# Enemigo
enemigo = random.choice(["Dragón", "Orco", "Hechicero", "Troll", "Espectro"])
vida_enemigo = random.randint(80, 120)
ataque_enemigo = random.randint(10, 25)

# Estado inicial del combate
print("\n--- Estado inicial del combate ---\n"
      f"Nombre del jugador: {jugador}\n"
      f"Vida del jugador: {vida_jugador}\n"
      f"Fuerza de ataque del jugador: {ataque_jugador}\n"
      "\n"
      f"Enemigo aleatorio encontrado: {enemigo}\n"
      f"Vida del enemigo: {vida_enemigo}\n"
      f"Fuerza de ataque del enemigo: {ataque_enemigo}\n")

# Primer turno
print(f"{jugador} ataca primero y hace {ataque_jugador} puntos de daño")
vida_enemigo -= ataque_jugador

# Segundo turno
print(f"{enemigo} contraataca y hace {ataque_enemigo} puntos de daño")
vida_jugador -= ataque_enemigo

# Resultado
print(f"{jugador} vida restante: {vida_jugador}\n"
      f"{enemigo} vida restante: {vida_enemigo}")

if vida_jugador > vida_enemigo:
    print("¡Felicitaciones! Ganaste 🏆")
elif vida_jugador < vida_enemigo:
      print(f"¡Perdiste! ☠️ Has sido derrotado por {enemigo}")
elif vida_jugador == vida_enemigo:
      print("¡Es un empate épico! 🤝")
