#encode:UTC-8
#Autor: José Antonio Gómez Mora
#Lee el radio de una esfera e imprime diámetro, volúmen, y área.
import math

#calcula el diametro de la esfera con el parametro radio
def calculaDiametro(radio):
    diametro= radio*2
    return diametro

#calcula el volumen de la esfera con el parametro radio
def calculaVolumen(radio):
    volumen=(4/3)*math.pi*radio**3
    return volumen

#calcula el area con el parametro radio
def calculaArea(radio):
    area=(math.pi*radio**2)*4
    return area

def main():
    radio=int(input("Ingresa el radio de la esfera: "))
    diametro=calculaDiametro(radio)
    volumen=calculaVolumen(radio)
    area=calculaArea(radio)
    print("Esfera con radio:",radio)
    print("Diámetro: %.2F"%(diametro))
    print("Volúmen: %.2F"%(volumen))
    print("Área: %.2F"%(area))

main()
