#AUTOR: PEDRO CORTÉS SOBERANES A01371919
#FUNCIÓN: CALCULAR DATOS DE UNA ESFERA

#Función: Sirve para calcular el diametro
def diametro (radio):
    diam = radio *2
    return diam

#Función: Sirve para calcular el volumen
def volumen (radio):
    vol = ((4/3)*(3.14))*(radio)
    return vol

#Función: Sirve para calcular el area
def area (radio):
    ar = 4*(3.14)*((radio)*(radio))
    return ar

def main():
    rad = float(input("Escribe el radio de la esfera: "))
    print("Esfera con radio: ", rad)
    dia = diametro(rad)
    print("Diametro: %.2f" % (dia))
    vo = volumen(rad)
    print("Volumen: %.2f" % (vo))
    a = area(rad)
    print("Area: %.2f" % (a))



main()
