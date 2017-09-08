# Autor: Saúl Rodrigo Toral Luna
# Matrícula: A01745007
# Leer el radio de una esfera e imprimir su diametro volumen y área

#Importar la libería de matemáticas
from math import *

#Calcular el Diametro
def calcularDiametro(radio):
    diametro = radio * 2
    return diametro

#Calcular el Volumen
def calcularVolumen(radio):
    volumen = (4 * pi * (radio**3)) / 3
    return volumen

#Calcular el Area
def calcularArea(radio):
    area = (4 * pi * (radio**2))
    return area

def main():
# Ingresar el radio de la esfera a calcular
    radio_de_Esfera = float(input("Escribe el radio de la esfera: "))
# Imprimir los resultados de cada función
    print("Esfera con radio: %.2f " % radio_de_Esfera)
    print("Diametro: %.2f " % calcularDiametro(radio_de_Esfera))
    print("Volumen: %.2f " % calcularVolumen(radio_de_Esfera))
    print("Area: %.2f " % calcularArea(radio_de_Esfera))
main()
