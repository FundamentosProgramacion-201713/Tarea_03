#encoding: UTF-8

#gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que calcula el total a pagar por la compra de boletos en un estadio

def calcularPago(asientosA, asientosB, asientosC):
    totalPago = (asientosA * 400) + (asientosB * 250) + (asientosC * 135)
    return totalPago

def main():
    numeroBoletosA = float(input("Número de boletos de clase A: "))
    numeroBoletosB = float(input("Número de boletos de clase B: "))
    numeroBoletosC = float(input("Número de boletos de clase C: "))
    costoTotal = calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)
    print("El costo total es $%.2f " % costoTotal)

main()