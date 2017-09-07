#encoding: UTF-8

#Gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que calcula Diametro, Volumen y Area de una a a partir del radio qe proporcione el usuario

from math import pi
#Funcion que calcula el diametro de una esfera a partir del radio
def calculardiametroEsf(radiod):
    valorDiametro = radiod * 2
    return valorDiametro

#Funcion que calcula el volumen de una esfera a partir del radio
def calcularvolumenEsf(radiov):
    valorVolumen = (4/3)*pi*(radiov**3)
    return valorVolumen

#Funcion que calcula el area de una esfera a partir del radio
def calcularareaEsf(radioa):
    valorArea = 4*pi*(radioa**2)
    return valorArea
#Función principal main que lee inputsn, llama a las demas funciones e imprime
def main():
    radiog = float(input("Escribe el radio de la esfera: "))
    print("Esfera con radio: %.2f " % radiog)
    diametro = calculardiametroEsf(radiog)
    print("Diámetro: %.2f " % diametro)
    volumen = calcularvolumenEsf(radiog)
    print("Volumen: %.2f " % volumen)
    area = calcularareaEsf(radiog)
    print("Área: %.2f " % area)

main()


