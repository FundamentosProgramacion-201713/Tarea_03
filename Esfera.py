# encode UFT-8
# Autor: Luis Enrique Neri Pérez
# Programa que lea el radio e imprima el diametro, area y volumen de una esfera usando funciones
import math
def calcularDiametro(radio): #Esta función calcula el diámetro de la esfera
    diametro = 2 * radio
    return diametro

def calcularArea(radio): #Esta función calcua el área de la esfera
    area = 4 * math.pi * (radio ** 2)
    return area

def calcularVolumen(radio): #Esta función calula el volúmen de la esfera
    volumen = 4/3 * math.pi * (radio**3)
    return volumen

def main(): #Esta funció solicita el redio de la esfera, llama a las unciones calcularDiametro, calcularArea y calcularVolumen, posteriormente imprime el resultado
    radio = float(input("Ingrese el radio de la esfera: "))
    diametro = calcularDiametro(radio)
    area = calcularArea(radio)
    volumen = calcularVolumen(radio)
    print("")
    print("ESFERA CON RADIO %.2f m" % radio)
    print("Diametro: %.2f m" % diametro)
    print("Área: %.2f m² " % area)
    print("Volúmen: %.2f m³" % volumen)

main()