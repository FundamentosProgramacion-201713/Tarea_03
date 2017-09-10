#enconding: UTF-8
#Alejandro Chávez Campos, A01374974
#Este programa es para calcular el precio total, de acuerdo al número de asientos, de acuerdo a su clasificación.

def calcularPago(asientosA,asientosB, asientosC):#Calcula el pago total a raíz del número de boletos de los distintos tipos.
    boletoA= asientosA*400
    boletoB=asientosB*250
    boletoC=asientosC*135
    totalPago= boletoA+boletoB+boletoC
    return totalPago


def main (): #Programa principal
    numeroBoletosA=float(input("Número de boletos de clase A: "))
    numeroBoletosB=float(input("Número de boletos de clase B: "))
    numeroBoletosC=float(input("Número de boletos de clase C: "))
    asientosA=numeroBoletosA
    asientosB=numeroBoletosB
    asientosC=numeroBoletosC
    pagoTotal= calcularPago (asientosA,asientosB, asientosC)
    print (("El costo total es: $%.2f")%(pagoTotal))
main()