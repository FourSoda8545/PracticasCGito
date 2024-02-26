# Practica6

# Escribe un programa en Python que solicite al usuario ingresar un número e indique si es positivo, negativo o cero.

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")