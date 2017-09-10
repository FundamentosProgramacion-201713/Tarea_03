# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González
# Matrícula: A01745998
# Descripción: Calcula rendimiento de un auto en km/l y mi/gal, además de los litros necesarios para un viaje próximo.

# calcula rendimiento en km/l
def calcularRendimientoKmL(kilometrosR,gasolinaU):
    rendimientoKmL = kilometrosR / gasolinaU
    return rendimientoKmL

# calcula rendimiento en mi/gal
def calcularRendimientoMiGal(kilometrosR, gasolinaU):
    rendimientoMiGal = (kilometrosR / 1.609344) / (gasolinaU * 0.264172051)
    return rendimientoMiGal

# calcula litros que va a necesitar el auto para su próximo viaje
def calcularlitrosANecesitar(kilometrosV,rendimientoKmL):
    litrosANecesitar = kilometrosV * (1 / rendimientoKmL)
    return litrosANecesitar

# lee km recorridos, l de gasolina usados y km a recorrer e imprime rendimiento en km/l, mi/gal y l para el próximo viaje
def main():
    kilometrosR = float(input("Teclea el número de km recorridos: "))
    gasolinaU = float(input("Teclea el número de litros de gasolina usados: "))
    print(" ")
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es: " % (kilometrosR, gasolinaU))
    rendimientoKmL = calcularRendimientoKmL(kilometrosR,gasolinaU)
    rendimientoMiGal = calcularRendimientoMiGal(kilometrosR,gasolinaU)
    print("%.2f km/l" % (rendimientoKmL))
    print("%.2f mi/gal" % (rendimientoMiGal))
    print(" ")
    kilometrosV = float(input("¿Cuántos kilómetros vas a recorrer? "))
    print(" ")
    litrosANecesitar = calcularlitrosANecesitar(kilometrosV,rendimientoKmL)
    print("Para recorrer %d km necesitas %.2f litros de gasolina" % (kilometrosV,litrosANecesitar))

main()