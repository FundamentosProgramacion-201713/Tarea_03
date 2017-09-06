#ecoding:UTF-8
#Autor: Angel Ramírez Martínez
#Descripción: A partir del radio se calcula el Diámetro, Volumen, Área y se imprimen los resultados.
from math import pi

# Calcula el diámetro de la esfera a partir del radio que se recibe como parámetro.
def calculardiametroEsfera(radio):
    diametro = radio * 2
    return diametro


# Calcula el volumen de la esfera a partir del radio que se recibe como parámetro.
def calcularvolumenEsfera(radio):
    volumen = 4/3 * pi * radio**3
    return volumen


# Calcula el área de la esfera a partir del radio que se recibe como parámetro.
def calcularareaEsfera(radio):
    area = 4 * pi * radio**2
    return area

# Esta función main llama a las funciones anteriores e imprime el radio, el diametro, el volumen y el área.
def main():
    r = float(input('Escribe el radio de la esfera: '))
    print('Esfera con radio: ', (r))
    d = calculardiametroEsfera(r)
    print('Diámetro: %.2f'%(d))
    v = calcularvolumenEsfera(r)
    print('Volumen: %.2f'%(v))
    a = calcularareaEsfera(r)
    print('Área: %.2f'%(a))
main()