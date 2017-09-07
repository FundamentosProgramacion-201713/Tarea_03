#encoding: UTF-8
#Especificaciones del programa: Programa que calcula el diametro, volumen y area de una esfera
#Autor: Ernesto Ibhar Guevara Gomez
#Matricua: A01746121
import math
def Leerradio():
    radio=float(input("Escribe el radio de la esfera: "))
    return radio
def Diametro(radio):
    diametro= radio * 2
    return diametro
def Volumen(radio):
    volumen=(4/3)* math.pi * (radio**3)
    return volumen
def Area(radio):
    area=4 * math.pi * (radio**2)
    return area
def main():
    radioo=Leerradio()
    Diametroo=Diametro(radioo)
    Volumenn=Volumen(radioo)
    Areaa=Area(radioo)
    print("Esfera con radio: ",radioo)
    print ("Diametro: %.2f"%(Diametroo))
    print("Volumen: %.2f"%(Volumenn))
    print("Area: %.2f"%(Areaa))
main()
