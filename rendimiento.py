# encoding: UTF-8

# Autor: Iván Alejandro Dumas Martínez
# Descripción: Este programa calcula el rendimiento de un automóvil con base en distintos factores

def convertirMillas(kilometros):
    millas = (kilometros * 0.62137119)
    return millas


def convertirGalon(litros):
    galones = (litros * 0.264172051)
    return galones


def calcularRendimientoKpL(kilometros, litros):
    rendimientoKpL = kilometros / litros
    return rendimientoKpL


def calcularRendimientoMpG(kilometros, litros):
    millas = convertirMillas(kilometros)
    galones = convertirGalon(litros)
    rendimientoMpG = millas/galones
    return rendimientoMpG


def calcularLitros(kilometros, rendimientoKpL):
    litros = kilometros / rendimientoKpL
    return litros


def main():
    km = float(input("Teclea el número de km recorridos: "))
    lt = float(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKpL = calcularRendimientoKpL(km, lt)
    rendimientoMpG = calcularRendimientoMpG(km, lt)
    print ("""
Si recorres %d kms con %d litros de gasolina, el rendimiento es:
%.2f km/l
%.2f mi/gal
""" % (km, lt, rendimientoKpL, rendimientoMpG))
    viaje = input("¿Cuántos kilometros vas a recorrer? ")
    litros = calcularLitros(viaje, rendimientoKpL)
    print ("\nPara recorrer %d km. necesitas %.2f litros de gasolina" % (viaje, litros))


main()
