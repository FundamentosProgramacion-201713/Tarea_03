#encoding-UTF-8
#AUTOR: José Antonio Vázquez Gabián
#Este programa calcula el rendimiento de un auto despues de que sube la gasolina en su valor de millas por hora.

def calcularRendimiento(km, litros):
     r = km / litros
     return r
#En esta funcion hacemos la conversion
def calcularConversion(km, litros):
    millas = km / 1.609344
    galones = litros * 0.264172051
    rendimiento = millas / galones
    return rendimiento
#En esta funcion calculamos los litros necesarios para recorrer el kilometraje
def calcularLitros(km, r):
    litros = km / r
    return litros
def main():
    kmRecorridos = float(input("Teclea el número de km recorridos: "))
    gasolinaUsada = float(input("Teclea el número de litros de gasolina usados: "))
    print("")
    rendimiento = round(calcularRendimiento(kmRecorridos, gasolinaUsada), 2)
    rendimiento2 = round(calcularConversion(kmRecorridos, gasolinaUsada), 2)
    print("Si recorres 350 kms con 23 litros de gasolina, el rendimiento es:")
    print(rendimiento, "km/l")
    print(rendimiento2, "mi/gal")
    print("")
    km = float(input("¿Cuántos kilómetros vas a recorrer? "))
    litros = calcularLitros(km, rendimiento)
    print("")
    print("Para recorrer", km ,"km. necesitas", round(litros, 2), "litros de gasolina" )
main()