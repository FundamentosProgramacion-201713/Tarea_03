# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González
# Matrícula: A01745998
# Descripción: Lee radio de una esfera e imprime: diámetro, volumen y área.

def calcularDiámetro(radio):
    diametro = radio * 2
    return diametro

def calcularVolumen(radio):
    volumen = (4/3) * 3.1416 * radio ** 3
    return volumen

def calcularArea(radio):
    area = 4 * 3.1416 * radio ** 2
    return area

def main():
    radio = float(input("Escribe el radio de la esfera: "))
    diametro = calcularDiámetro(radio)
    volumen = calcularVolumen(radio)
    area = calcularArea(radio)
    print("Esfera con radio: ",radio)
    print("Diámetro: %.2f" % (diametro))
    print("Volumen: %.2f" % (volumen))
    print("Área: %.2f" % (area))

main()