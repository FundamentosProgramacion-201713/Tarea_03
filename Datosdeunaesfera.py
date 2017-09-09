#Encoding: UTF-8

#Autor: Alberto López Reyes
'''Descripción: Este programa calcula e imprime el radio, diámetro, volúmen, y área de una esfera al ser otorgado el radio
de dicha figura.'''

import math

    #Esta función calcula el díametro de la esfera al recibir el radio de la figura.
def calcularDiámetro(fltRadio):
    fltDiámetro = fltRadio * 2
    return fltDiámetro

    #Esta función calcula el volumen de la esfera al recibir el radio de la figura.
def calcularVolumen(fltRadio):
    fltVolumen = (4/3) * math.pi * fltRadio**3
    return fltVolumen

    #Esta función calcula el área de la esfera al recibir el radio de la figura.
def calcularÁrea(fltRadio):
    fltÁrea = 4 * math.pi * fltRadio**2
    return fltÁrea

    #Esta función principal pide el radio de una esfera para otorgárselo a las funciones "calcularDiámetro",
    #"calcularVolumen", y "calcularÁrea" para recibir el diámetro, volúmen y área de dicha figura. El radio, junto las
    #tres cantidades recibidas, son posteriormente impresas.
def main():
    strRadio = input("Escribe el radio de la esfera: ")
    fltRadio = float(strRadio)

    fltDiámetro = calcularDiámetro(fltRadio)
    fltVolumen = calcularVolumen(fltRadio)
    fltÁrea = calcularÁrea(fltRadio)

    print("Esfera con radio: "+strRadio)
    print("Diámetro: "+format(fltDiámetro, '.2f'))
    print("Volumen: "+format(fltVolumen, '.2f'))
    print("Área: "+format(fltÁrea, '.2f'))

    #Se acciona la función "main".
main()
