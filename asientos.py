# encoding: UTF-8

# Autor: Iván Alejandro Dumas Martínez
# Descripción: Este programa calcula el total a pagar con base en la cantidad de boletos que el usuario desee

def calcularPago(asientosA, asientosB, asientosC): # Función que calcula el total a pagar por los boletos que el usuario desee con base en la zona que elija
    totalPago = asientosA * 400 + asientosB * 250 + asientosC * 135
    return totalPago


def main(): # Función principal
    asientosA = int(input("Número de asientos que desea de clase A: "))
    asientosB = int(input("Número de asientos que desea de clase B: "))
    asientosC = int(input("Número de asientos que desea de clase C: "))
    totalPago = (calcularPago(asientosA, asientosB, asientosC))
    print("El costo total es: $%.2f" % (totalPago))


# Llamar a a función principal
main()
