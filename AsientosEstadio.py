# encode UFT-8
# Autor: Luis Enrique Neri Pérez
# Programa que permita determinar el costo de los boletos de tres clases diferentes, usando funciones

def calcularPago(boletosClaseA, boletosClaseB, boletosClaseC): #Esta función calcula el precio del total de boletos de cada clase y suma los tres costos para obtener el total
    claseA = 450 * boletosClaseA
    claseB = 250 * boletosClaseB
    claseC = 135 * boletosClaseC
    totalPago = claseA + claseB + claseC
    return totalPago


def main(): #Esta función solicita el número de boletos de cada clase, llama a la función calcularPago e imprime el total a pagar
    boletosClaseA = int(input("Ingrese el número de boletos Clase A: "))
    boletosClaseB = int(input("Ingrese el número de boletos Clase B: "))
    boletosClaseC = int(input("Ingrese el número de boletos Clase C: "))
    totalPago = calcularPago(boletosClaseA,boletosClaseB, boletosClaseC)
    print("")
    print("El costo total es : $%.2f" % (totalPago))


main()
