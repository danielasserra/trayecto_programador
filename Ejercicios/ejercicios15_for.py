# Daniela Serra
# For. Ejercicio 10

# Ingresar un número. Determinar si el número es primo o no.
#  solo es divisible por 1 y por sí mismo

# # Opcion 1 
# numero = int(input("Ingrese un número: "))
# suma_resto_cero = 0

# # Para saber si un número es primo basta con dividirlo por los números primos menores que él 
# # hasta llegar a un cociente igual o menor que el divisor. 
# # Si ninguna de estas divisiones es exacta, el número es primo
# for i in range(1, numero):
#     if numero % i == 0:
#         suma_resto_cero += 1
# if suma_resto_cero > 2:
#     print("El número no es primo")
# else:
#     print("El número es primo")
    
# # Opcion 2
# numero = int(input("Ingrese un numero: "))

# if numero < 2:
#     print("El numero no es primo")
# else:
#     es_primo = True
    
#     for i in range(2, int(numero ** 0.5) + 1):
#         if numero % i == 0:
#             es_primo = False
#             break
        
#     if es_primo == True:
#         print("El numero es primo")
#     else:
#         print("El numero no es primo")

#---------------------------------------------

# Daniela Serra
# For. Ejercicio 11.
# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. 
# Informar cuántos números primos se encontraron.

numero = int(input("Ingrese un numero: "))
suma_primos = 0

for i in range (1, numero + 1):
    if numero % i == 0:
        print(numero)
        suma_primos += 1

print(suma_primos)