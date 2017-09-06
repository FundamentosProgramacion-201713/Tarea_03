#encoding: UTF-8

#Autor: Javier Martínez Hernández  A01375496
#Descripción: se dará el diametro, area y volumen de una esfera



def calcularDiametroEsf(radioEsfera):           #Se calculará el diametro de la esfera
    diametroEsfera=radioEsfera*2
    return diametroEsfera

def calcularVolumenEsf(radioEsfera):            #Se calculará el Volumen de la esfera
    volumenEsfera=4/3*3.1416*radioEsfera**3
    return volumenEsfera

def calcularAreaEsf(radioEsfera):                #Se calculará el Area de la esfera
    areaEsfera=4*3.1416*radioEsfera**2
    return areaEsfera


def main():
    radioEsfera=float(input("Ingresa el radio de la esfera: "))
    diametroEsfera=calcularDiametroEsf(radioEsfera)
    volumenEsfera=calcularVolumenEsf(radioEsfera)
    areaEsfera=calcularAreaEsf(radioEsfera)
    print("esfera con radio: %.1f \nDiametro: %.2f \nVolumen: %.2f \nArea: %.2f" % (radioEsfera,diametroEsfera,volumenEsfera,areaEsfera))
main()