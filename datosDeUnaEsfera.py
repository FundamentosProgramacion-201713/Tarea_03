#AUTOR: JOSÉ HEINZ MÖLLER SANTOS

import math

#calcula el diametro de la esfera
def calcularDiametroEsfera(radio):
    r = radio * 2
    return r

#calcula el volumen de la esfera
def calcularVolumenEsfera(radio):
    v = (4/3) * (math.pi) * (radio**3)
    return v

#calcula el area de la esfera
def calcularAreaEsfera(radio):
    a = 4 * (radio**2) * (math.pi)
    return a

#Es la función principal, lee los datos e imprime los resultados.
def main():
    radio = float(input("Radio de la esfera: "))

    diametro = float(calcularDiametroEsfera(radio))
    volumen = float(calcularVolumenEsfera(radio))
    area = float(calcularAreaEsfera(radio))

    print("Radio Esfera: %.1f"%radio)
    print("Diametro de Esfera: %.2f"%diametro)
    print("Volumen de Esfera: %.2f"%volumen)
    print("area de Esfera: %.2f"%area)

main()