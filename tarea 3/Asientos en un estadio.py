# coding: UTF-8
# autor: Eduardo Gallegos Solís
# Programa que ayuda a calcular el total a pagar, dependiendo la demanda de boletos.

def calcularPago(asientosA, asientosB, asientosC):
    # calcula el total que se pagará por los asientos solicitados
    totalPago = (asientosC * 135) + (asientosB * 250) + (asientosA *400)
    return totalPago

def main():
    numeroBoletosA = int(input("Número de boletos de clase A:"))
    numeroBoletosB = int(input("Número de boletos de clase B:"))
    numeroBoletosC = int(input("Número de boletos de clase C:"))
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es de: $ %.2f" %(totalPago))

main()