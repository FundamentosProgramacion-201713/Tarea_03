#enconding: UTF-8
#Alejandro Chávez Campos, A01374974
#Este programa es para calcular el diámetro, volumen y área de una esfera a partir de su radio.


def calcularDiametro(radioEsfera): #Calcula el diametro a partir del radio.
    diametro=radioEsfera*2
    return diametro


def calcularVolumen(radioEsfera): #Calcula el volumen apartir del radio.
    volumen=(4*3.1416*(radioEsfera)**3)/3
    return volumen


def calcularArea(radio):#Calcula el area a partir del radio.
    area=4*3.1416*(radio**2)
    return area


def main():#Este es el programa principal
    strRadioEsfera=input("Escribe el radio de la esfera: ")
    print ("Esfera con radio:",strRadioEsfera)
    radioEsfera=float (strRadioEsfera)
    diametro=calcularDiametro(radioEsfera)
    print(("Diametro: %.2f")%(diametro))
    volumen=calcularVolumen(radioEsfera)
    print (("Volumen: %.2f")%(volumen))
    area= calcularArea(radioEsfera)
    print(("Area: %.2f")%(area))
main()