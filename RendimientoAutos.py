#encoding: UTF-8
#Autor: Irving Fuentes Aguilera
#Descripción: Programa que calcula el rendimiento de la gasolina de
# un coche y calcula cuantos litros necesitará para cierto recorrido

def calcularRendimientoLitros(kmRecorridos, litrosusados):
    rendimientoLitros= kmRecorridos/litrosusados

    return rendimientoLitros


def calcularRendimientoGalones(kmRecorridos, litrosUsados):
    milla= kmRecorridos / 1.609344
    galon= litrosUsados * 0.264172051
    rendimientoG= milla/galon

    return rendimientoG


def calcularLitrosRecorrido(recorridoKm, rendimientoLitros):
    recorrido= recorridoKm/rendimientoLitros

    return recorrido


def main():
    kmRecorridos= float(input("Teclea el # de km recorridos: "))
    litrosUsados= float(input("Teclea el # de litros consumidos: "))
    rendimientoLitros= calcularRendimientoLitros(kmRecorridos, litrosUsados)
    rendimientoGalones= calcularRendimientoGalones(kmRecorridos, litrosUsados)
    print("")
    print("Si recorres %.2f kms con %.2f lts de gasolina,  el rendimiento es: " % (kmRecorridos, litrosUsados))
    print("%.2f km/l" % (rendimientoLitros))
    print("%.2f mi/gal" % (rendimientoGalones))
    print("")
    recorridoKm= float(input("¿Cuántos kilómetros vas a recorrer? "))
    recorridoLt= calcularLitrosRecorrido(recorridoKm, rendimientoLitros)
    print("")
    print("Para recorrer %.2f km necesitas %.2f litros de gasolina" % (recorridoKm, recorridoLt))



main()
