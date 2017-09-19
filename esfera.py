#encoding: UTF-8
#Nazdira Abigail Cerda del Prado A01375428
#Descripción: Diseño TopDown para calcular diámetro, volumen y área de una esfera

def calcularDiam(radio):
    diam=radio*2
    return diam

def calcularVol(radio):
    vol=(4*3.141516*(radio**3))/3
    return vol

def calcularArea(radio):
    area=(4*3.141516*(radio**2))
    return area

def main():
    radio=float(input("Radio de la esfera:"))
    diametro=float(calcularDiam(radio))
    volumen=float(calcularVol(radio))
    areauno=float(calcularArea(radio))
    print("El diámetro de la esfera es de:", format(diametro,".2f"))
    print("El volumen de la esfera es de:", format(volumen,".2f"))
    print("El área de la esfera es de", format(areauno,".2f"))

main()