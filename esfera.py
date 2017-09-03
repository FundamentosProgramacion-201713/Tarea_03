#ecoding:UTF-8
#Autor: Angel Ramírez Martínez
#Descripción: A partir del radio se calcula el Diámetro, Volumen, Área y se imprimen los resultados.
from math import pi

# Calcula el diámetro de la esfera a partir del radio que se recibe como parámetro.
def diametroEsfera(radio):
    diametro = radio * 2
    return diametro


# Calcula el volumen de la esfera a partir del radio que se recibe como parámetro.
def volumenEsfera(radio):
    volumen = 4/3 * pi * radio**3
    return volumen


# Calcula el área de la esfera a partir del radio que se recibe como parámetro.
def areaEsfera(radio):
    area = 4 * pi * radio**2
    return area


def main():
    r = float(input('Escribe el radio de la esfera: '))
    print('Esfera con radio: ', (r))
    d = diametroEsfera(r)
    print('Diámetro: %.2f'%(d))
    v = volumenEsfera(r)
    print('Volumen: %.2f'%(v))
    a = areaEsfera(r)
    print('Área: %.2f'%(a))
main()