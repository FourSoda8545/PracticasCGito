# Practica11

# Pedir un número entre 0 y 9,999 y decir cuantas cifras tiene

numero = int(input("Ingrese un número entre 0 y 9,999: "))

if 0 <= numero <= 9999:
    cifras = len(str(numero).strip("0"))
    print("El número ingresado tiene", cifras, "cifras")
