#encoding: UTF-8
#Autor: Rodrigo Rivera Salinas A01375000
#Descripcion: Obtener diametro,area y volumen de una esfera

def volumen(radio):           #Apartir del radio dado por el usuario, se mete a la formula y se guarda el volumen
    v=(4/3)*(3.14)*(radio**3)
    return v
def area(radio):              #Apartir del radio dado por el usuario, se mete a la formula y se guarda el area
    a=(4)*(3.14)*(radio**2)
    return a
def perimtro(radio):          #Apartir del radio dado por el usuario, se mete a la formula y se guarda el perimetro
    p=(2)*(radio)
    return p
def main():  #pide datos al usuario, imprime lo que se le pide y llama a las funciones para guardarlas en una variable
    radio=float(input("dar radio"))
    print("esfera de radio", radio)
    vol=volumen(radio)
    are=area(radio)
    peri = perimtro(radio)
    print("Diametro: ", peri)
    print("volumen: ", vol)
    print("area:", are)

main()
