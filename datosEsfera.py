#encoding UTF-8
#Autor: Joaquin Rios Corvera A01375441

import math

#Calcula el radio de un círculo con su radio
def calcularDiametro(radio):
    diametro = radio * 2
    return diametro

#Calcula el volumen de un círculo con su radio
def calcularVolumen(radio):
    volumen = (4/3) * math.pi * (radio**3)
    return volumen

#Calcula el área de un círculo con su radio
def calcularArea(radio):
    area = 4 * math.pi * (radio**2)
    return area

def main():
    radio = float(input("Escribe el radio de la esfera: "))

    diametro = calcularDiametro(radio)
    volumen = calcularVolumen(radio)
    area = calcularArea(radio)
    print("Esfera con radio:", radio)
    print("Diametro: %.2f" %diametro)
    print("Volumen: %.2f" %volumen)
    print("Area: %.2f" %area)

main()