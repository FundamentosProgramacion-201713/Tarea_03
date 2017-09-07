#encoding: UTF-8
#Autor: Rodrigo Rivera Salinas A01375000
#Descripcion: Calcular el rendimiento de un automovil a partir de la gasolina dada y los km dados

def gasyL(kilometros,litros):       #se va a dividir los km y los litros y se van a guardar
    gaseL=kilometros/litros
    return gaseL
def millas(kilometros):             #se van a transformar de kilometros a millas y se va a guardar
    m=kilometros/1.609344
    return m
def gal(litros):                     #se va a trasformar de litros a galones y se va a guardar
    g=litros*0.264172051
    return g
def kilometrosrecorrer(kilometros,litros,q):   #se hace la operacion entre los kilometros,los litros y la cantidad que se desea recorer y se guarda
    kpr=(q*litros)/kilometros
    return kpr
def main():                         #pide datos al usuario, imprime lo que se le pide y llama a las funciones para guardarlas en una variable
    kilome=int(input("dar km"))
    gaso=int(input("dar litros de gasolina usados"))
    print("si recorres", kilome, "con", gaso, "el rendimiento es:")
    kmyl=gasyL(kilome,gaso)
    print(kmyl,"km/l")
    miga=millas(kilome)/gal(gaso)
    print(miga, "m/gal")
    kilomearecorrer=int(input("km a recorrer:  "))
    kar=kilometrosrecorrer(kilome,gaso,kilomearecorrer)
    print("para recorerr", kilomearecorrer,  "necesitas", kar, "L de gasolina")
main()


