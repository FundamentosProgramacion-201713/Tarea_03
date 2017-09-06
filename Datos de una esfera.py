#encoding: UTF-8
#Autor: Aaron Tonatiuh Villanueva Guzmán
#Este programa recibe el radio de una esfera y calcula su volumen, diámetro y área.
import math

#Esta función realiza todos los calculos necesarios para saber la información requerida de la esfera. Regresa los valores con un tuple que después se desempaquetará.
def calculos(radio):
    arEsfera=4 * math.pi * (radio**2)
    volEsfera= ( 4 * math.pi * (radio**3)) / 3
    diaEsfera= radio * 2
    return(arEsfera, volEsfera, diaEsfera)

#Esta función Main lee el radio de la esfera para poder realizar los calculos pertinentes con la función calculos. Además, desempaqueta el tuple de calculos e imprime los resultados con formato.
def Main():
    radio= float(input("Escribe el radio de la esfera: "))
    areaEsfera, volumenEsfera, diametroEsfera=calculos(radio)
    print("Esfera con radio", radio)
    print("Diametro: %.2f"% diametroEsfera)
    print("Volumen: %.2f"% volumenEsfera)
    print("Area: %.2f"% areaEsfera)

Main()
