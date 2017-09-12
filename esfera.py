#encoding UTF-8
#Anaid Fernanda Labat González A01746289
#Descripción: Calcular el díametro, volumen y área de una esfera a partir del radio ingresado

from math import pi

def diametroE(rD):
    diametro=rD*2
    return diametro
def volumenE(rV):
    volumen=(4/3)*pi*(rV**3)
    return volumen
def areaE(rA):
    area=4*pi*(rA**2)
    return area

def main():
    radio=int(input("Escribe el radio de la esfera:"))
    print("Esfera con radio:",radio)
    diametro=diametroE(radio)
    print("Diámetro: %.2f" % diametro)
    volumen=volumenE(radio)
    print("Volumen: %.2f" % volumen)
    area=areaE(radio)
    print ("Area: %.2f"% area)

main()


