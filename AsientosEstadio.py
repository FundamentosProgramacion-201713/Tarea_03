#Autor: Andrea Montero Rivas, A01374496
# Este programa ayuda a calcular el pago total dependiendo del asiento

def calcularPago(asientosA, asientosB, asientosC):
    totalPago = 400 * asientosA + 250 * asientosB + 135 * asientosC
    return totalPago

def main():
    numerosBoletosA = int(input("Cuantos boletos de asiento A:",))
    numerosBoletosB = int(input("Cuantos boletos de asiento B:",))
    numerosBoletosC = int(input("Cuantos boletos de asiento C:",))
    totalPago = calcularPago(numerosBoletosA, numerosBoletosB, numerosBoletosC)
    print("el total a pagar es:", totalPago)

main()