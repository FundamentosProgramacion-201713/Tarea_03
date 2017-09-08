#encoding: UTF-8
#Autor: Luis Alfonso Alcántara López Ortega, A01374785

#Función para calcular el rendimiento teniendo como parámetros los kilometros recorridos y litros utilizados
def calcularRendimiento(km, litros):

    rendimiento = km / litros

    return rendimiento

#Función para realizar la conversión de kilómetros por litro a millas por galón
def calcularRendimientoConversion(km, litros):

    millas = km / 1.609344
    galones = litros * 0.264172051
    rendimiento = millas / galones

    return rendimiento

#Función para calcular los litros necesarios para recorrer los kilómetros deseados
def calcularLitros(km, r):

    litros = km / r

    return litros


def main():

    kmRecorridos = float(input("Teclea el número de km recorridos: "))
    gasolinaUsada = float(input("Teclea el número de litros de gasolina usados: "))

    rendimiento = round(calcularRendimiento(kmRecorridos, gasolinaUsada), 2)

    rendimiento2 = round(calcularRendimientoConversion(kmRecorridos, gasolinaUsada), 2)

    print("Si recorres 350 kms con 23 litros de gasolina, el rendimiento es:")
    print(rendimiento, "km/l")
    print(rendimiento2, "mi/gal")

    km = float(input("¿Cuántos kilómetros vas a recorrer? "))

    litros = calcularLitros(km, rendimiento)

    print("Para recorrer", km ,"km. necesitas", round(litros, 2), "litros de gasolina" )

main()