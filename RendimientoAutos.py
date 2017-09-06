#encoding: UTF-8
# Autor: Daniel Sahuer
# Calcula km / litro, millas / litro y litros necesarios para recorrer una distancia en km.



def calcularkmxLitro(km,l): #Calcula kilómetros por litro
    total = km/l
    return total #Regresar


def calcularmixGal(km,l): #Calcula la conversión en millas por galón
    milla = km / 1.609344
    galon = 0.264172051 * l
    total = milla/galon
    return total #Regresar


def calcularTotalLitrosRecorrer(km,kmxLt): #Calcula gasolina necesaria al dividir el valor entre los kilómetros por litro
    total = km/kmxLt
    return total #Regresar


def main():
    numeroKm = int(input("Teclea el número de km recorridos: "))
    numeroLitros = int(input("Teclea el número de litros de gasolina usados: "))

    kmxLitro = calcularkmxLitro(numeroKm,numeroLitros)
    mixGal = calcularmixGal(numeroKm, numeroLitros)

    print("\nSi recorres %d kms con %d litros de gasolina, el rendimiento es:\n%.2f km/l\n%.2f mi/gal\n" % (numeroKm,numeroLitros,kmxLitro,mixGal))

    kmRecorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))

    totalLitrosRecorrer = calcularTotalLitrosRecorrer(kmRecorrer,kmxLitro)

    print("\nPara recorrer %d km. necesitas %.2f litros de gasolina" % (kmRecorrer,totalLitrosRecorrer))

main()