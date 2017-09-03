#encoding: UTF-8

#gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que calcula Diametro, Volumen y Area de una a a partir del radio qe proporcione el usuario

from math import pi

def diametroEsf(radiod):
    valorDiametro = radiod * 2
    return valorDiametro

def volumenEsf(radiov):
    valorVolumen = (4/3)*pi*(radiov**3)
    return valorVolumen

def areaEsf(radioa):
    valorArea = 4*pi*(radioa**2)
    return valorArea

def main():
    radiog = float(input("Escribe el radio de la esfera: "))
    print("Esfera con radio: %.2f " % radiog)
    diametro = diametroEsf(radiog)
    print("Diámetro: %.2f " % diametro)
    volumen = volumenEsf(radiog)
    print("Volumen: %.2f " % volumen)
    area = areaEsf(radiog)
    print("Área: %.2f " % area)

main()


