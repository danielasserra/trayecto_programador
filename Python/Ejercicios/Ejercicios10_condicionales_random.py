# # Daniela Serra
# # Condicionales con random
# # Ejercicio E: "Suerte o Susto"

import random

print("Bienvenido al sorteo *Suerte o Susto*")

# Datos ingresados por el usuario
participa = input("¿Participa del sorteo (si/no): ").lower()
nombre = input("Ingrese su nombre para participar del sorteo: ").capitalize()

if participa == "si":
    numero = random.randint(1, 100)
    print(f"\n¡Hola {nombre}! Tu número es: {numero}")
    if numero >= 1 and numero <= 10:
        print("Gana un viaje sorpresa")
    elif numero <= 30:
        print("Gana un cupón de descuento del 50%")
    elif numero <= 60:
        print("No gana nada, pero puede volver a intentarlo")
    elif numero <= 90:
        print("Pierde una vida virtual (solo por diversión 😅)")
    elif numero <= 100:
        print("Susto digital (emoji misterioso 😱👻🕷️)")
else:
    print("Usted no participa del sorteo")