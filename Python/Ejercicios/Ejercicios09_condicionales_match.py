# # Daniela Serra
# # Condicionales con Match
# # Ejercicio 13

# # Escribe un programa que pregunte al usuario el nivel de batería de su celular 
# # (bajo, medio, alto). Según la respuesta, mostrar:
# #   Si es "bajo": "Carga tu celular pronto".
# #   Si es "medio": "Puedes seguir usándolo un rato más".
# #   Si es "alto": "Batería en buen estado".
# #   Si no coincide: "Nivel de batería no reconocido".

# bateria = input("¿Cuál es el nivel de batería de su celular? (bajo / medio / alto / otro): ")

# match bateria:
#     case "bajo":
#         print("Carga tu celular pronto")
#     case "medio":
#         print("Puedes seguir usándolo un rato más")
#     case "alto":
#         print("Batería en buen estado")
#     case _:
#         print("Nivel de bateria no reconocido")

#----------------------------------------------------------

# # Daniela Serra
# # Condicionales con Match
# # Ejercicio 14

# # Escribe un programa que pregunte al usuario el clima del día 
# # (soleado, lluvioso, nublado, nevado). Según el clima, mostrar 
# # una recomendación:
# #   Soleado: "No olvides tus gafas de sol".
# #   Lluvioso: "Lleva paraguas".
# #   Nublado: "Tal vez llueva, lleva abrigo".
# #   Nevado: "Abrígate mucho".
# #   Cualquier otro: "Clima no reconocido".

# clima = input("¿Cómo está el clima? (soleado, lluvioso, nublado, nevado): ")

# match clima:
#     case "soleado":
#         print("No olvides tus gafas de sol")
#     case "lluvioso":
#         print("Lleva paraguas")
#     case "nublado":
#         print("Tal vez llueva, lleva abrigo")
#     case "nevado":
#         print("abrigate mucho")
#     case _:
#         print("Clima no reconocido")

#----------------------------------------------------------

# # Daniela Serra
# # Condicionales con Match
# # Ejercicio 15

# Escribe un programa que pregunte al usuario una estación del año 
# (verano, otoño, invierno, primavera). Dependiendo de la estación, mostrar:
#   Verano: "Es tiempo de vacaciones y calor".
#   Otoño: "Las hojas caen y refresca".
#   Invierno: "Hace frío, ideal para chocolate caliente".
#   Primavera: "Todo florece".
#   Otro: "Estación no válida".

estacion = input("Nombre la estación del año (verano, otoño, invierno, primavera): ")

match estacion:
    case "verano":
        print("Es tiempo de vacaciones y calor")
    case "otoño":
        print("Las hojas caen y refresca")
    case "invierno":
        print("Hace frío, ideal para chocolate caliente")
    case "primavera":
        print("Todo florece")
    case _:
        print("Estación no válida")