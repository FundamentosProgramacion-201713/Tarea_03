# Autor: LuisMiguel Baqueiro
# Matricula: 1745997
import math
def calcularDiametro(radio):
    diametro = 2 * radio
    return diametro
def calcularVolumen(radio):
    volumen = (4/3) * math.pi * (radio ** 3)
    return volumen
def calcularArea(radio):
    area = math.pi * 4 * (radio ** 2)
    return area
def main():
    radio = float(input("Escribe el radio de la esfera: "))
    print("esfera con radio: %.1f" % radio)
    print("Diametro: %.2f" % calcularDiametro(radio))
    print("Volumen: %.2f" % calcularVolumen(radio))
    print("Area: %.2f" % calcularArea(radio))
main()