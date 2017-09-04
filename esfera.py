#encoding: UTF-8
#Autor: Luis Alfonso Alcántara López Ortega, A01374785

# Importar las librerías de matemáticas para poder utilizar PI
from math import *

# Función para calcular el diámetro de una esfera teniendo el radio como parámetro
def calcularDiametro(radio):

    diametro = radio * 2

    return diametro

# Función para calcular el volumen de una esfera teniendo el radio como parámetro
def calcularVolumen(radio):

    volumen = round((4/3) * pi * radio**3, 2)

    return volumen

# Función para calcular el área de una esfera teniendo el radio como parámetro
def calcularArea(radio):

    area = round(4 * pi * (radio**2), 2)

    return area

def main():

    radio = float(input("Escribe el radio de la esfera: "))
    diametro = calcularDiametro(radio)
    volumen = calcularVolumen(radio)
    area = calcularArea(radio)

    print("Esfera con radio:", radio)
    print("Diametro:", diametro)
    print("Volumen", volumen)
    print("Area", area)


main()