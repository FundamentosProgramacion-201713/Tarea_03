#encoding-UTF-8
#AUTOR: José Antonio Vázquez Gabián
#Este programa calcula el diametro, radio y area de una esfera.

#En esta función calculamos el diámetro, volumen y área de una esfera
def calcularEsfera(radio):
    diametro = radio * 2
    volumen = 4/3 * (3.1416 * (radio**3))
    area = 4 * (3.1416 * (radio**2))
    return diametro, volumen, area
#En esta funcion pedimos el radio de la esfera mpara que la funcion calcularEsfera realice los calculos
def main():
    radio = float(input("Escribe el radio de la esfera: "))
    area, volumen, diametro = calcularEsfera(radio)
    print("Esfera con radio", radio)
    print("Diametro: %.2f" % diametro)
    print("Volumen: %.2f" % volumen)
    print("Area: %.2f" % area)
main()