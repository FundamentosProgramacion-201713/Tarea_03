#encoding: UTF-8
#Autor: Luis Alfonso Alcántara López Ortega, A01374785

def calcularPago(asientosA, asientosB, asientosC):

    precioA = 400 * asientosA
    precioB = 250 * asientosB
    precioC = 135 * asientosC

    totalPago = round(float(precioA + precioB + precioC), 2)

    return totalPago


def main():

    numeroBoletosA = int(input("Número de boletos de clase A: "))
    numeroBoletosB = int(input("Número de boletos de clase B: "))
    numeroBoletosC = int(input("Número de boletos de clase C: "))

    resultado = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)

    print("El costo total es: $", resultado, sep="")

main()