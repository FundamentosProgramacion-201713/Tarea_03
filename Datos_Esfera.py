#Autor: Maria Fernanda Torres Velazquez A01746537
#El siguiente programa, lee el radio de una esfera e imprime el diametro, volumen y area de la misma

#Funcion que recibe como parametro la medida del radio de una esfera y regresa el diametro
def calcularDiametro (radio):
    diam= radio*2
    return diam

#Funcion que recibe como parametro la medida del radio de una esfera y regresa el area
def calcularArea (radio):
    pi= 3.1416
    area= 4*pi*(radio**2)
    return area

#Funcion que recibe como parametro la medida del radio de una esfera y regresa el volumen
def calcularVolumen (radio):
    pi= 3.1416
    volumen= ((4*pi)/3)*(radio**3)
    return volumen

#Funcion principal en la que se introduce la longitud del radio de la esfera y lo envia a las funciones calcularArea,Volumen y Diametro,
# para que estas regresen el diamtero, volumen y area.

def main():
    r = float(input("Longiud del radio de la esfera en metros: "))
    diam= calcularDiametro(r)
    a= calcularArea (r)
    v= calcularVolumen (r)
    print("Diametro: %.2f metros" % (diam))
    print("Volumen: %.2f metros cubicos" % (v))
    print("Area: %.2f metros cuadrados" % (a))

#Llama a la funcion main (programa principal)
main()

