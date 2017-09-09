#encoding: UTF-8
#Autor: Neftalí Rodríguez Martínez, A01375808.
#Entrega los datos de una esfera: Diámetro, Volumen y Área. Usamos pi de la la librería Math.

import math #Importamos librería math para después usar Pi.


def calcularDiametro(radio): #Calcula el diámetro de la esfera.
    diametro = radio * 2
    return diametro


def calcularVolumen(radio): #Calcula el volumen de la esfera.
    area = ((4/3) * math.pi * (radio ** 3))
    return area


def calcularArea(radio): #Calcula el area de la esfera.
    volumen = (4 * math.pi * (radio ** 2))
    return volumen


def main (): #Programa principal.

    radio = input("Escribe el radio de la esfera: ")
    print("Esfera con radio:", radio)
    radio = float(radio)

    diametro = calcularDiametro (radio)
    print ("Diametro: %.2f" % diametro)

    volumen = calcularVolumen (radio)
    print("Volumen: %.2f" % volumen)

    area = calcularArea (radio)
    print("Area: %.2f" % area)

main()