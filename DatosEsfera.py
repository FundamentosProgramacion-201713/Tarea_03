# encoding:UTF-8
# Autor: Carlos Pano Hernández

# Descripción: Este programa calcula el diámetro, volúmen y área superficial de una esfera con cualquier radio.

#Importación de mate
import math

#Funciones/ Cálculo de diámetro
def calcularDiametro(radio):
    diametro = 2*radio
    return diametro

#Volumen
def calcularVolumen(radio):
    volumen = (4/3)*math.pi*radio**3
    return volumen

#Area
def calcularArea(radio):
    area = 4*math.pi*(radio**2)
    return area

#FunciónMain
def main():
    radio = int(input("Escribe el radio de la esfera:"))
    print("Esfera con radio:", radio)

    d= calcularDiametro(radio)
    v= calcularVolumen(radio)
    a=calcularArea(radio)

    print("Diámetro: %.2f"%(d))
    print("Volumen: %.2f"%(v))
    print("Área: %.2f"%(a))

#Principal
main()
