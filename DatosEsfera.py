#encoding: UTF-8
#Autor: Dora Gabriela Lizárraga González A01229599
#Este programa le pide el radio de una esfera al usuario e imprime sus datos

import math

#Esta función calcula el diametro con respecto al radio
def diametroCirculo (radio):
    diametro = radio*2
    return (diametro)

#Esta función calcula el volumen con respecto al radio
def volumenCirculo (radio):
    volumen = ((4/3)*math.pi*radio**3)
    volumen = round(volumen,2)
    return (volumen)

#Esta función calcula el área con respecto al radio
def areaCirculo (radio):
    area = 4*math.pi*radio**2
    area = round(area,2)
    return (area)

#Esta función lee los valores de las variables, ejecuta las otras funciones e imprime el resultado
def main():
    radio = float(input('Escribe el radio de la esfera: '))
    diam = diametroCirculo(radio)
    vol = volumenCirculo(radio)
    area = areaCirculo(radio)
    print('Esfera con radio: ',radio)
    print('Diametro: ',diam)
    print('Volumen: ',vol)
    print('Área: ',area)

main()