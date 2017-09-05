#encode: UTF-8
# Autor: David Ramírez Ríos, A01338802
# Calcular diametro, área, y volúmen de una esfera

from math import pi

def calcularDiametro (radio):

    diametro = 2 * radio
    return diametro

def calcularArea (radio):

    area = 4 * pi * radio ** 2
    return area

def calcularVolumen (radio):

    volumen = (4/3) * pi * radio ** 3
    return volumen

def main ():

    radio = float (input("Escribe el radio de la esfera: "))
    diametro = calcularDiametro(radio)
    area = calcularArea(radio)
    volumen = calcularVolumen(radio)

    print("Esfera con radio: ", (radio))
    print("Diametro: %.2f" % (diametro))
    print("Volumen: %.2f" % (volumen))
    print("Area: %.2f" % (area))

main()

