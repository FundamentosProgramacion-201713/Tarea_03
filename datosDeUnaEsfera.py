#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: con el valor del radio dado por el usuario vamos a devolver su diametro, volumen y su area

import math

def calcDiamtetro(radio):
    diametro = 2 * radio
    return diametro


def calcVolumen(radio):
    volumen = 4/3 * math.pi*radio ** 3
    return volumen


def calcArea(radio):
    area = 4 * math.pi *radio ** 2
    return area

def main () :
    radio = float(input("Escribe el radio de la esfera:"))
    print("Esfera con radio:", radio)
    print("Dimetro: %.2f" % calcDiamtetro(radio))
    print("Volumen: %.2f" % calcVolumen(radio))
    print("Area: %.2f" % calcArea(radio))

main ()
