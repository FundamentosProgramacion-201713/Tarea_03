#encoding: UTF-8

#gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que calcula cuanto kilometros por litro y millas por galon rinde de acuerdo a lo indicado por el usario, aproximar
# cuantos litro se necsita por una cantidad de kilometos dada por el usuario.

def calcularrendimientoKmL(km, l):
    rendimientoKilometroLitro = km / l
    return rendimientoKilometroLitro

def convertirKmaMi(km):
    kilometroconvertido = km / 1.609344
    return kilometroconvertido

def convertirLaGal(l):
    litrosconvertidos = l * .264172051
    return litrosconvertidos

def calcularrendimientoMiGal(Mi,Gal):
    rendimientoMillaGalon = Mi / Gal
    return rendimientoMillaGalon

def calcularaproximadoL(km1,l,kmesp):
    prediccionlitros = (kmesp*l)/km1
    return prediccionlitros

def main():
    kilometros = float(input("Teclea los kilómetros recorridos: "))
    litros = float(input("Teclea los litros utilizados: "))
    print("Si recorres %.2f Kms con %.2f litros de gasolina, el rendimiento es:" % (kilometros,litros))

    rendiKml = calcularrendimientoKmL(kilometros,litros)
    print("%.2f km/l" % rendiKml)

    millas = convertirKmaMi(kilometros)
    galones = convertirLaGal(litros)
    rendiMiGal = calcularrendimientoMiGal(millas,galones)
    print("%.2f Mi/gal" % rendiMiGal)

    kilometrosesperados = float(input("¿Cuántos kilómetrso va a recorrer?: "))
    aproximacionL = calcularaproximadoL(kilometros,litros,kilometrosesperados)
    print("para recorrer %.2f kilometros usted necesita %.2f litros de gasolina" % (kilometrosesperados, aproximacionL))

main()
