#encoding: UTF-8
# Autor: Daniel Sahuer
# Calcula volumen, área y diámetro de una esfera

import math

def calcularDiametro(diametro): #Calcula el diámetro
    totalDiametro = diametro * 2
    return totalDiametro #Regresar


def calcularVolumen(volumen): #Calcula el volumen
    totalVolumen = (4/3) * math.pi * (volumen ** 3)
    return totalVolumen #Regresar


def calcularArea(area): #Calcula el área
    totalArea = 4 * math.pi * (area ** 2)
    return totalArea #Regresar


def main():
    radio = float(input("Escribe el radio de la esfera: "))

    diametro = calcularDiametro(radio)
    volumen = calcularVolumen(radio)
    area = calcularArea(radio)

    print("Esfera con radio: %d\nDiametro: %.2f\nVolumen: %.2f\nArea: %.2f" %(radio,diametro,volumen,area))

main()