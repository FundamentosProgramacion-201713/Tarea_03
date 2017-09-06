#encoding: UTF-8
#Autor: Irving Fuentes Aguilera
#Descripción: Programa que calcula el volumen, diámetro y área de una esfera

from math import *

def calcularVolumen(radio):
    volumen=(4/3) * (pi) * (radio)**3

    return volumen


def calcularDiametro(radio):
    diametro=radio/2

    return diametro

def calcularArea(radio):
    area= 4 * pi * radio**2

    return area


def main():
    radio=float(input("Introducir radio de la esfera: "))
    volumen=calcularVolumen(radio)
    diametro=calcularDiametro(radio)
    area=calcularArea(radio)
    print(" El volumen es %.2f cm**3" % (volumen))
    print(" El diamtro es %.2f cm" % (diametro))
    print(" El área es %.2f cm**2" % (area))

main()
