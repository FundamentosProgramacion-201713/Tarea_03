#encode:UTC-8
#Autor: José Antonio Gómez Mora
#Lee el número de kilómetros recorridos y la cantidad de gasolina utilizada e imprime rendimiento km/L, mi/gal


def calculoKmL(kmRecorridos, litrosUsados):
    kmL=kmRecorridos/litrosUsados
    return kmL


def calculoMiGal(kmL):
    miGal=kmL*(3.7854/1.6093)
    return miGal


def calculoGasolina(kmRecorrer,kmL):
    gasolina=kmRecorrer/kmL
    return gasolina


def main():
    kmRecorridos=int(input("Ingresa el total de kilómetros recorridos: "))
    litrosUsados=int(input("Ingresa el total de litros de gasolina usados: "))
    kmL= calculoKmL(kmRecorridos,litrosUsados)
    miGal= calculoMiGal(kmL)

    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es:"%(kmRecorridos,litrosUsados))
    print("%.2f km/l"%(kmL))
    print("%.2f mi/gal"%(miGal))

    kmRecorrer=int(input("¿Cuántos kilómetros vas a recorrer?: "))
    gasolina=calculoGasolina(kmRecorrer,kmL)
    print("Para recorrer %d km, necesitas %.2f litros de gasolina"%(kmRecorrer,gasolina))

main()