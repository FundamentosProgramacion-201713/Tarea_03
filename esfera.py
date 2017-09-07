#encode: UTF-8

#Autor: Natalia Meraz Tostado   A01745008
#Descripción: calcular el diámetro, volumen y área de una esfera

radio = float(input("Escribe el radio de la esfera: "))

def calcularDiametro(radio):        #calcula el diametro de la esfera
    diametro = 2 * radio
    return diametro

def calcularVolumen(radio):         #calcula el volumen de la esfera
    volumen = (4/3) * (3.1416) * (radio**3)
    return volumen

def calcularArea(radio):            #calcula el area de la esfera
    area = 4 * 3.1416 * (radio**2)
    return area

def main():
    diametro = calcularDiametro(radio)
    volumen = calcularVolumen(radio)
    area = calcularArea(radio)
    print("Esfera con radio: %.2f" % radio)
    print("Diámetro: %.2f" % diametro)
    print("Volumen: %.2f" % volumen)
    print("Área: %.2f" % area)

main()