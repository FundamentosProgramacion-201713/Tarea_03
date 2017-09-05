# coding: UTF-8
# autor: Eduardo Gallegos Solís
# Calcula el diámetro, volumen y área de una esfera.


def calcularDiametro (radio):
    # calcula el diámetro de la esfera
    medidaDiametro = radio * 2
    return medidaDiametro

def calcularVolumen (radio):
    # calcula el volumen de la esfera
    medidaVolumen = (4/3)* 3.14159 * (radio**3)
    return medidaVolumen

def calcularArea (radio):
    #calcula el área de la esfera
    medidaArea = 4 * 3.14159 * (radio**2)
    return medidaArea

def main():
    radio = float(input("Escribe el radio de la esfera:"))
    diametro = calcularDiametro(radio)
    volumen = calcularVolumen(radio)
    area = calcularArea(radio)
    print("Esfera de radio: %.2f" %(radio))
    print("Diámetro: %.2f" %(diametro))
    print("Volumen: %.2f" %(volumen))
    print("Area: %.2f" %(area))

main()