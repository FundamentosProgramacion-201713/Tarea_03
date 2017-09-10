#uncoding: UTF-8
#Autor: Ana María López Soto
#Descripción: Este programa calcúla el volumen, área y diámetro de una esfera.


#Calcúla el diámetro de la esfera
def calcularDiametro(radio) :
    diametro = radio * 2
    return diametro


#Calcúla el volumen de la esfera
def calcularVolumen(radio):
    volumen = (4/3) * 3.1416 * (radio ** 3)
    return volumen


#Calcúla el área de la esfera
def calcularArea(radio):
    area = 4 * 3.1416 * (radio ** 2)
    return area


def main():
    radio = float(input("Ingrese el radio de la esfera: "))
    diametro = calcularDiametro(radio)
    volumen = calcularVolumen(radio)
    area = calcularArea(radio)
    print("Esfera con radio:", radio)
    print("Diámetro:", diametro)
    print("Volumen:", "{:.2f}".format(volumen))
    print("Área:", "{:.2f}".format(area))

main()