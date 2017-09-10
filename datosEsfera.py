#encoding: UTF-8

#Autor: Roberto Téllez Perezyera
#Este programa calcula tres datos de una esfera y regresa los resultados no enteros con dos cifras significativas.

import math


#Calcula y regresa el valor del diámetro en función del radio.
def calcularDiametro(r):
    d = 2 * r
    return d


#Calcula y regresa el volumen en función del radio dado.
def calcularVolumen(r):
    v = 4/3 * math.pi * (r**3)
    return v


#Calcula el área de la esfera en función del radio dado.
def calcularArea(r):
    a = 4 * math.pi * (r**2)
    return a


#Aquí hacemo la lectura, almacenamiento y escritura de datos.
def main() :
    r = float(input("Escribe el radio de la esfera: "))
    diametro = calcularDiametro(r)
    volumen = calcularVolumen(r)
    area = calcularArea(r)
    print ("Esfera con radio: ", r)
    print ("Diámetro: %.2f" % (diametro))
    print ("Volumen: %.2f" % (volumen))
    print ("Área: %.2f" % (area))

#concluimos llamando a main para que se ejecute el código dentro de ésta
main()
