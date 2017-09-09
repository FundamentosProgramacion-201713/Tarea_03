#Encoding: UTF-8
#Autor:Luis Daniel Rivera Salinas
#Matricula: A01374997
#Descripcion: Al ingresar el radio de una esfera, imprime el diametro, volumen y area

from math import pi

def volumen(radio): #Dado el radio, se calcula el volumen por medio de la formula del volumen ((3/4)*pi*r**3)
    volumenTotal = (4/3)*(pi)*(radio**3)
    return volumenTotal

def area(radio): #Dado el radio, se calcula el area por medio de la formula del area (4*pi*(r**2))
    area = (4)*(pi)*(radio**2)
    return area

def diametro(radio): #Dado el radio, se calcula el diametro por medio de la formula (r*2)
    diametro = (2)*(radio)
    return diametro

def main(): #Ingresa el radio e imprime el radio, diametro, volumen y area
    radio = float(input("Escribe el radio de la esfera: "))
    print("Esfera con radio: ", radio)
    print("Diametro: ", "%.2f"%diametro(radio))
    print("Volumen: ", "%.2f"%volumen(radio))
    print("Area:", "%.2f"%area(radio))

main()