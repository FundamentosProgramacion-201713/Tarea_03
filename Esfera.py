#Autor: Gabriela Mariel Vargas Franco A01745775
#encoding: UTF-8
#Lee el radio de una esfera y calcula el diametro, volumen y área.
import math

#Calcula y guarda en la variable calcularDiametro
def calcularDiametro(diametro):

    calcularDiametro=(diametro*2)

    #Regresar calcularDiametro
    return calcularDiametro

#calcula y guarda en calcularVolumen
def calcularVolumen(volumen):

    calcularVolumen=((4/3)*math.pi*(volumen*volumen*volumen))

    #Regresar calcularVolumen
    return calcularVolumen

#Calcula y guarda calcularArea
def calcularArea(area):
    calcularArea=4*(math.pi)*(area*area)
#Regresar calcularArea
    return calcularArea

def main():
    radio=float(input("Escribe el radio de la esfera:"))
    print("Esfera con radio:",radio)
    cD=calcularDiametro(radio)
    print("Diametro:",format(cD,".2f"))
    cV=calcularVolumen(radio)
    print("Volumen:",format(cV,".2f"))
    cV=calcularArea(radio)
    print("Area:",format(cV,".2f"))




main()
