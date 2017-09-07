# UFT-8
#Autor: Javier León Alcántara
# Leé el radio e imprime diámetro, volumen y área

from math import *


def diametroEsfera(radio):  #Calcula el diametro
     diametro = radio * 2
     return diametro


def volumenEsfera(radio):   #Calcula el volumen
     volumen = (4/3) * pi * (radio**3)
     return volumen


def areaEsfera(radio):      #Calcula el area
     area = 4 * pi * (radio**2)
     return area


def main():                 #Emplea las otras funciones e imprime su resultado
     radio = float(input("Escribe el radio de la esfera: "))
     print("Esfera con radio:",(radio))

     diametro = diametroEsfera(radio)
     print("Diámetro: %.2f"%(diametro))

     volumen = volumenEsfera(radio)
     print("Volumen: %.2f"%(volumen))

     area = areaEsfera(radio)
     print("Área: %.2f"%(area))

main()