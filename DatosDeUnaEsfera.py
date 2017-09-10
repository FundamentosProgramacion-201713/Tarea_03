# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González
# Matrícula: A01745998
# Descripción: Calcula diámetro, volumen y área de una esfera con base en su radio.

# calcula diámetro
def calcularDiámetro(radio):
    diametro = radio * 2
    return diametro

# calcula volumen
def calcularVolumen(radio):
    volumen = (4/3) * 3.1416 * radio ** 3
    return volumen

# calcula área de la superficie
def calcularArea(radio):
    area = 4 * 3.1416 * radio ** 2
    return area

# lee radio de la esfera e imprime radio, diámetro, volumen y área de la superficie
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