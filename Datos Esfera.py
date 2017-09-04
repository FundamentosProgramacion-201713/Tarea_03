#encoding: UTF-8
#Omar Israel Galván García A01745810
#Este programa pregunta por el radio de una esfera e imprime su diámetro,volumen y área.
pi = 3.1416

def calculaDiametro(radio):   # esta función pide al usuario el radio y calcula su diametro multiplicandolo por dos
    diametro =  radio * 2
    return  diametro

def calculaVolumen(radio):   #esta función pide al usuario el radio y calcula su volumen con la formula:
    volumen = (4 * pi * radio**3)/3   #  (4*pi*radio) /3
    return volumen

def calculaArea(radio):    #esta función pide al usuario el radio y calcula su área: 4*pi*radio**2
    area = (4 * pi * (radio**2))
    return area


def main():    #la función principal main ejecuta el programa, lee datos e imprime los resultados
    radio = float(input("Escribe el radio de la esfera: "))
    print("Esfera con radio:",radio)
    diametro = calculaDiametro(radio)
    volumen = calculaVolumen(radio)
    area = calculaArea(radio)
    print("Diámetro: %.2f"%(diametro))
    print("Volumen: %.2f"%(volumen))
    print("Area: %.2f"% (area))


main()

