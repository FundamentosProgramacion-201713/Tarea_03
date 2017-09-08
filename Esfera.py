#enocding UTF-8
#Autor: Leonardo Castillejos Vite
#Descripción: Un programa que lee el radio de la esfera e imprime el diámetro, el volumen y el área

from math import pi
def calcularDiametroEsfera (radio):
    diametro = radio * 2
    return diametro

def calcularVolumenEsfera (radio):
    volumen = (4/3) * pi * radio**3
    return volumen

def calcularAreaEsfera (radio):
    area = 4 * pi * radio**2
    return area

def main():
    radio = float(input("Escribe el radio de la esfera: "))
    diametro = calcularDiametroEsfera(radio)
    volumen = calcularVolumenEsfera(radio)
    area = calcularAreaEsfera(radio)
    print("Esfera con radio: ", radio)
    print("Diametro: %.2f" %(diametro))
    print("Volumen: %.2f" % (volumen))
    print("Area: %.2f" %(area))

main()
