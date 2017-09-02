# encoding: UTF-8

# Autor: Iván Alejandro Dumas Martínez
# Descripción: Este programa calcula el total a pagar con base en la cantidad de boletos que el usuario desee

def calcularPago(asientosA, asientosB, asientosC):
    totalPago = asientosA * 400 + asientosB * 250 + asientosC * 135
    return totalPago


def main():
    asientosA = int(input("Número de asientos que desea de clase A: "))
    asientosB = int(input("Número de asientos que desea de clase B: "))
    asientosC = int(input("Número de asientos que desea de clase C: "))
    totalPago = (calcularPago(asientosA, asientosB, asientosC))
    print("------------------------------------")
    print("El costo total es: $%.2f" % (totalPago))


main()
