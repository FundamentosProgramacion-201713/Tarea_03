#encode: UTF-8
# Autor: David Ramírez Ríos, A01338802
# Calcular el rendimiento promedio de un auto y gasolina necesaria para recorrido de km

def calcularRendimiento (kilometro, litro):

    rendimiento = kilometro / litro
    return rendimiento

def convertirMG (kilometro, litro):

    millas = kilometro / 1.609344
    galon = litro * .264172051
    rendimientoM = millas / galon
    return rendimientoM

def main ():

    kilometros = int (input("Teclea el número de km recorridos: "))
    litros = int (input("Teclea el número de litros de gasolina usados: "))

    rendimiento = calcularRendimiento(kilometros, litros)
    rendimientoM = convertirMG(kilometros, litros)

    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es:" % (kilometros, litros))
    print("%.2f km/l" % (rendimiento))
    print("%.2f mi/gal" % (rendimientoM))


    kmR = int (input("¿Cuántos km vas a recorrer? "))

    litrosN = kmR / rendimiento

    print("Para recorrer %d km. necesitas %.2f litros de gasolina" % (kmR, litrosN))

main()


