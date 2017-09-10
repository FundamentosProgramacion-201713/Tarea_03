#uncoding: UTF-8
#Autor: Ana María López Soto
#Descripción: Este programa calcúla la cantidad total a pagar dependiendo de los boletos seleccionados.


#Calcúla el pago total de los boletos
def calcularPago(asientosA, asientosB, asientosC) :
    totalPago = (asientosA * 400) + (asientosB * 250) + (asientosC * 135)
    return totalPago


def main():
    numeroBoletosA = int(input("Ingrese cantidad de asientos de clase A: "))
    numeroBoletosB = int(input("Ingrese cantidad de asientos de clase B: "))
    numeroBoletosC = int(input("Ingrese cantidad de asientos de clase C: "))
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $",totalPago)


main()