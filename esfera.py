# encoding: UTF-8

# Autor: Iván Alejandro Dumas Martínez
# Descripción: Este programa imprime el valor del diametro, volumen y área de una esfera con base en su radio

# Librerias
from math import *


def calcularDiametro(radio): # Función para calcular el Diametro de la esfera
    diametro = radio * 2
    return diametro


def calcularVolumen(radio):
    volumen = (4 / 3) * pi * (radio ** 3) # Función para calcular el Volumen de la esfera
    return volumen


def calcularArea(radio): # Función para calcular el Área de la esfera
    area = 4 * pi * (radio ** 2)
    return area


def main(): # Función principal
    radio = float(input("Escribe el radio de la esfera: "))
    diametro = calcularDiametro(radio)
    volumen = calcularVolumen(radio)
    area = calcularArea(radio)
    print("""Esfera con radio: %g
Diametro : %.2f
Volumen: %.2f
Área: %.2f""" % (radio, diametro, volumen, area))

# Llamar a función principal
main()
