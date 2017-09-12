#encoding UTF-8
#Autor:Pablo Garcia Morales
#Programa que lea el radio de una esfera y que imprima: Diámetro, volúmen, Área




def diametroesfera(resfera):
    diametro=resfera*2
    return diametro


def volumenesfera(resfera):
    volumen=((resfera**3)*(4/3)*(3.1416))
    return volumen


def areaesfera(resfera):
    area=((resfera**2)*(4*3.1416))
    return area


def main():
    resfera=float(input("Escribe el radio de la esfera: "))
    desfera=diametroesfera(resfera)
    vesfera=volumenesfera(resfera)
    aesfera=areaesfera(resfera)
    print("Esfera con radio: " ,resfera)
    print("Diametro: %.2f" % (desfera))
    print("Volumen: %.2f" % (vesfera))
    print("Area: %.2f" % (aesfera))

main()







