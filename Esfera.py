#encoding: UTF-8
#Autor: Eduardo Roberto Müller Romero, A01745219
#Escribe un programa que lea el radio de una esfera y que calcule el diametro el volumen y el área.

def main():
    radio = leerRadio()
    diametro = calcularDiametro(radio)
    volumen = calcularVolumen(radio)
    area = calcularelArea(radio)
    print("Radio de la Esfera:", radio)
    print("Diámetro de la Esfera:", diametro)
    print("Volumen de la Esfera:", "%.2f" %volumen)
    print("Área de la Esfera:", "%.2f" %area)

def leerRadio():
    radio = int(input("Radio de la Esfera: "))
    return radio

def calcularDiametro(radio):
    diametro = radio * 2
    return diametro

def calcularVolumen(radio):
    volumen = (4 * 3.1416 * (radio ** 3)) / 3
    return volumen

def calcularelArea(radio):
    area = 4 * 3.1416 * (radio ** 2)
    return area

main()