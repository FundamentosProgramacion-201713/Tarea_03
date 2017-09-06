#encoding: UTF-8
#Autor: Aaron Tonatiuh Villanueva Guzmán
#Este programa recibe el radio de una esfera y calcula su volumen, diámetro y área.
import math

def calculos(radio):
    areaEsfera=4 * math.pi * (radio**2)
    volumenEsfera= ( 4 * math.pi * (radio**3)) / 3
    diametroEsfera= radio * 2
    return(areaEsfera, volumenEsfera, diametroEsfera)

def Main():
    radio= float(input("Escribe el radio de la esfera: "))
    calculosfinales=calculos(radio)
    print("Esfera con radio", radio)
    print(calculosfinales)

Main()
