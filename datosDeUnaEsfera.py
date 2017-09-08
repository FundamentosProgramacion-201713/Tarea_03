#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: con el valor del radio dado por el usuario vamos a devolver su diametro, volumen y su area

#sirve para importar la libreria math cuando sea llamada, en este caso para pedir pi con math.pi
import math

#con base al radio se crea la operación para calcular el diametro y regresar diametro
def calcDiamtetro(radio):
    diametro = 2 * radio
    return diametro

#con base al radio se crea la operación para calcular el volumen y regresar volumen
def calcVolumen(radio):
    volumen = 4/3 * math.pi*radio ** 3
    return volumen

#con base al radio se crea la operación para calcular el area y regresar area
def calcArea(radio):
    area = 4 * math.pi *radio ** 2
    return area

# se lee el radio dado por el usuario y se imprime el radio que tiene la esfera, el diametro, su volumen y el area que se obtendra llamando a las funciónes calcDiamtetro(radio), calcVolumen(radio), calcArea(radio)
def main () :
    radio = float(input("Escribe el radio de la esfera: "))
    print("Esfera con radio: ", radio)
    print("Dimetro: %.2f" % calcDiamtetro(radio))
    print("Volumen: %.2f" % calcVolumen(radio))
    print("Area: %.2f" % calcArea(radio))

#llama a la función main
main ()
