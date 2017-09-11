# encoding:  UTF-8

# Autor: Jean Paul Esquivel Lobato     A01376152
# Descripción: Cálcular los datos de una esfera



#Cálcular del diametro

def diametro (radio):
    diame = radio *2
    return diame


#Cálcular el volumen

def volumen (radio):
    volu = ((1.333)*(3.1416))*((radio)**3)
    return volu


#Cálcular el área

def area (radio):
    are = 4*(3.14)*((radio)*(radio))
    return are


#Función principal
def main():
    radio = float(input("Teclea el radio de la esfera: "))
    print("Esfera con radio: ", radio)
    dia = diametro(radio)
    print("Diametro: %.2f" % (dia))
    vo = volumen(radio)
    print("Volumen: %.2f" % (vo))
    a = area(radio)
    print("Area: %.2f" % (a))


main()