# Practirca12

# Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien...

#Declaracion de Variables

numero = float(input("Ingresa un número del 0 al 10: "))

#Proceso

if numero < 0 or numero > 10:
    print("Error: El número ingresado no está en el rango válido (0-10).")
else:
    if numero <= 3:
        print("Insuficiente")
    elif numero <= 7:
        print("Suficiente")
    else:
        print("Bien")
