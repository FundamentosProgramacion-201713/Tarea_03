# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González
# Matrícula: A01745998
# Descripción: Lee kilómetros recorridos y gasolina utilizada e imprime rendimiento y datos para próximo viaje.

def calcularRendimientokml(kilometrosR,gasolinaU):
    rendimientokml = kilometrosR / gasolinaU
    return rendimientokml

def calcularRendimientomigal(kilometrosR, gasolinaU):
    rendimientomigal = (kilometrosR / 1.609344) / (gasolinaU * 0.264172051)
    return rendimientomigal

def calcularlitrosANecesitar(kilometrosV,rendimientokml):
    litrosANecesitar = kilometrosV * (1 / rendimientokml)
    return litrosANecesitar

def main():
    kilometrosR = float(input("Teclea el número de km recorridos: "))
    gasolinaU = float(input("Teclea el número de litros de gasolina usados: "))
    print(" ")
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es: " % (kilometrosR, gasolinaU))
    rendimientokml = calcularRendimientokml(kilometrosR,gasolinaU)
    rendimientomigal = calcularRendimientomigal(kilometrosR,gasolinaU)
    print("%.2f km/l" % (rendimientokml))
    print("%.2f mi/gal" % (rendimientomigal))
    print(" ")
    kilometrosV = float(input("¿Cuántos kilómetros vas a recorrer? "))
    print(" ")
    litrosANecesitar = calcularlitrosANecesitar(kilometrosV,rendimientokml)
    print("Para recorrer %d km necesitas %.2f litros de gasolina" % (kilometrosV,litrosANecesitar))

main()
