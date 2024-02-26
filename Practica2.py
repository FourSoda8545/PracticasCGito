# Practica2 

import math

def area_cuadrado(lado):
    return lado**2

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return math.pi * radio**2


# Solicitar datos al usuario
lado_cuadrado = float(input("Ingrese el lado del cuadrado: "))
base_triangulo = float(input("Ingrese la base del triángulo: "))
altura_triangulo = float(input("Ingrese la altura del triángulo: "))
radio_circulo = float(input("Ingrese el radio del círculo: "))


# Calcular áreas
area_cuadrado_resultado = area_cuadrado(lado_cuadrado)
area_triangulo_resultado = area_triangulo(base_triangulo, altura_triangulo)
area_circulo_resultado = area_circulo(radio_circulo)


# Mostrar resultados
print ("Área del cuadrado:", area_cuadrado_resultado)
print ("Área del triángulo:", area_triangulo_resultado)
print ("Area de circulo:", area_circulo_resultado) 

