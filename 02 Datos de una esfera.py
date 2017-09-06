##encoding: UTF-8

# Autor: Edgar Alexis González Amador, A01746540
# Descripcion: Escribe un programa que lea el radio de una esfera y que imprima:
#- Diámetro.
#- Volumen.
#- Área.


import math

#Función que permite calcular el diametro a partir del doble del radio
def calcularDiametro(radio):
    diametro = radio*2
    return diametro

#Función que permite calcular el volumen de una esfera a partir de un radio introducido
def calcularVolumen(radio):
    volumen = ((4/3)*math.pi) * (float(radio)**3)
    return volumen

#Función que permite calcular el area de una esfera a partir de un radio introducido
def calcularArea(radio):
    area = (4*math.pi) * (radio**2)
    return area

#Main, función principal en la que se llama a las funciones anteriores y se piden e imprimen datos.
def main():
    radio = float(input("Escribe el radio de la esfera: "))
    diametro = calcularDiametro(radio)
    volumen = calcularVolumen(radio)
    area = calcularArea(radio)
    print("Esfera con radio: ",radio)
    print("Diametro: %.2f"%(diametro))
    print("Volumen: %.2f"%(volumen))
    print("Area: %.2f"%(area))

main()