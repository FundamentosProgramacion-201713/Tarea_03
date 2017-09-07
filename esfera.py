#Autor: Juan Sebastián Lozano Derbez

import math

def calcdiam(radio):
    diametro = (radio) * 2
    return diametro

def calcvol(radio):
    volumen = (4/3) * math.pi * (radio)**3
    return volumen

def calcar(radio):
    area = 4 * math.pi * (radio)**2
    return area

def main():
    radio = float(input("Cuál es el radio?: "))

    dm = calcdiam(radio)
    vm = calcvol(radio)
    ar = calcar(radio)

    print("---------------------")
    print('Diámetro: %.2f' % dm)
    print('Volúmen: %.2f' % vm)
    print('Área: %.2f' % ar)

main()