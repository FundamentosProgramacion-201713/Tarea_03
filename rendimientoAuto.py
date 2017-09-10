#encoding: UTF-8

#Autor: Roberto Téllez Perezyera
"""
Este programa calcula el rendimiento de un auto en kilómetros por litro y millas por galón. Después, indica al usuario
la cantidad de litros requerida para recorrer cierta distancia.
"""


#Calcula el rendimiento del auto a partir de los primeros datos introducidos por el usuario
def calcularRendimientoKmL(kmTraveled, gasLitersUsed):
    rendimientoKm = kmTraveled / gasLitersUsed
    return rendimientoKm


#Convierte kilómetros a millas
def convertirKilometrosaMillas(kmTraveled):
    millas = (kmTraveled / 1.609344)
    return millas


#Convierte litros a galones
def convertirLitrosaGalones(gasLitersUsed):
    galones = (gasLitersUsed * 0.264172051)
    return galones


#Calcula el rendimiento en millas / galón, usando los valores ya convertidos
def calcularRendimientoMGP(mi, g):
    rendimientoMPG = (mi / g)
    return rendimientoMPG


#Se calculan los litros de gasolina necesaria para recorrer la cantidad dada de kilómetros, considerando el rendimiento
#del auto
def calcularGasolinaNecesaria(kmToBeTraveled, rendimientoKm):
    reqdGas = kmToBeTraveled / rendimientoKm
    return reqdGas


def main() :
    kmTraveled = float(input("Teclea el número de km recorridos: "))
    gasLitersUsed = float(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKm = calcularRendimientoKmL (kmTraveled, gasLitersUsed)
    mi = convertirKilometrosaMillas (kmTraveled)
    g = convertirLitrosaGalones (gasLitersUsed)
    rendimientoMPG = calcularRendimientoMGP (mi, g) #MPG (abreviatura en inglés para 'millas por galón')
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es: " % (kmTraveled, gasLitersUsed))
    print("%.2f km/l" % (rendimientoKm))
    print("%.2f mi/gal" % (rendimientoMPG))
    print(" ")
    kmToBeTraveled = float(input("¿Cuántos kilómetros vas a recorrer? "))
    gasToBeUsed = calcularGasolinaNecesaria (kmToBeTraveled, rendimientoKm)
    print("Para recorrer %d km. necesitas %.2f litros de gasolina." % (kmToBeTraveled, gasToBeUsed))


#llamamos a main para que pida y almacene datos, haga cálculos, e imprima los resultados deseados
main()
