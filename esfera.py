#Autor: Mónica Monserrat Palacios Rodríguez
# Datos de una esfera
#include<stdio.h>

def diametro(radio):
    diametroTotal = (2*radio) #Se multiplica el radio por dos para calcular el diámetro de la esfera
    return diametroTotal #Se guarda temporalmente el valor

def volumen(radio):
    volumenTotal = ((4/3)*3.1416*(radio**3)) #Se aplica la fórmula del volumen con respecto al radio
    return volumenTotal #Se guarda temporalmente el valor

def area (radio):
    areaTotal = (4*(3.1416*(radio**2))) #Se aplica la fórmula del área con respecto al radio
    return areaTotal #Se guarda temporalmente el valor

def main():
    rad = float(input("Escribe el radio de la esfera: ", )) #Se pide al usuario que determine el radio
    diametroTotal = diametro(rad) #Se llama a la función diametroTotal para proceder con un valor asignado a radio
    volumenTotal = volumen(rad) #Se llama a la función volumenTotal para proceder con un valor asignado a radio
    areaTotal = area(rad) #Se llama a la función areaTotal para proceder con un valor asignado a radio
    print("Esfera con raidio:", rad) #Se imprimen los valores para cada dato
    print("Diámetro: ", "{0:.2f}".format(diametroTotal))
    print("Volumen:", "{0:.2f}".format(volumenTotal))
    print("Área:", "{0:.2f}".format(areaTotal))

main() #Se llama a la función main

