#Autor: Andrea Montero Rivas, A01374496
# Este programa ayuda a medir eldiametro, volumen y area de una esfera

def medirDiametro(rad):
    diametro = rad * 2
    return diametro


def medirVolumen(rad):
    volumen=(4*3.14*(rad**3))/3
    return volumen


def medirArea(rad):
    area = 4*3.14*(rad**2)
    return area


def main():
    radio = float(input("escribe el radio de la esfera",))
    diametro = medirDiametro(radio)
    volumen = medirVolumen(radio)
    area = medirArea(radio)
    print(" %.2f de diametro, %.2f de volumen, %.2f de area " % (diametro, volumen, area))



main()