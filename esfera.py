#encoding: utf-8
#written by Jordan González Bustamante
#Este programa te pide el radio de una esfera y calcula diámetro, volumen y área

#En esta función calculamos el diámetro, volumen y área según los datos ingresados
def calcularEsfera(radio):
    diametro = radio * 2
    volumen = 4/3 * (3.1416 * (radio**3))
    area = 4 * (3.1416 * (radio**2))
    return diametro, volumen, area

#En main, pedimos el radio de la esfera para posteriormente llamar a la función anterior.
def main():
    radio = float(input("Escribe el radio de la esfera : "))
    diametro, volumen, area = calcularEsfera(radio)
    print("Esfera con radio : %.2f" % radio)
    print("Diametro : %.2f" % diametro)
    print("Volúmen  : %.2f" % volumen)
    print("Área     : %.2f" % area)

main()

