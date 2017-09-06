# encoding:UTF-8
# Autor: Carlos Pano Hernández

# Descripción: Este programa calcula el diámetro, volúmen y área superficial de una esfera con cualquier radio.

import math

def calcularDiametro(radio):
    diametro = 2*radio
    return diametro


def calcularVolumen(radio):
    volumen = (4/3)*math.pi*radio**3
    return volumen


def calcularArea(radio):
    area = 4*math.pi*(radio**2)
    return area

def main():
    radio = int(input("Escribe el radio de la esfera:"))
    print("Esfera con radio:", radio)

    d= calcularDiametro(radio)
    v= calcularVolumen(radio)
    a=calcularArea(radio)

    print("Diámetro: %.2f"%(d))
    print("Volumen: %.2f"%(v))
    print("Área: %.2f"%(a))


main()
