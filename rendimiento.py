# encoding: UTF-8

# Autor: Iván Alejandro Dumas Martínez
# Descripción: Este programa calcula el rendimiento de un automóvil con base en distintos factores

def convertirMillas(kilometros): # Función que convierte de kilometros a millas
    millas = (kilometros * 0.62137119)
    return millas


def convertirGalon(litros): # Función que convierte de litros a galones
    galones = (litros * 0.264172051)
    return galones


def calcularRendimientoKpL(kilometros, litros): # Función que calcula el rendimiento en kilometros por litros
    rendimientoKpL = kilometros / litros
    return rendimientoKpL


def calcularRendimientoMpG(kilometros, litros): # Función que calcula el rendimiento en millas por galón
    millas = convertirMillas(kilometros)
    galones = convertirGalon(litros)
    rendimientoMpG = millas/galones
    return rendimientoMpG


def calcularLitros(kilometros, rendimientoKpL): # Función que calcula los litros que se necesitan para x kilometros con base en el rendimiento ya obtenido
    litros = kilometros / rendimientoKpL
    return litros


def main(): # Función principal
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


#Llamar a función principal
main()
