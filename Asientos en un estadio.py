#encoding: UTF-8
#Autor: Luis Fernando Figueroa Rendon, A01746139

#Calcular el total a pagar de la compra de boletos para el estadio.

def main():
    boletosa= int(input("Numero de boletos de clase A: "))
    boletosb= int(input("Numero de boletos de clase B: "))
    boletosc= int(input("Numero de boletos de clase C: "))

#Funcion que calcula el total a pagar por los boletos comprados.
    def calcularPago (asientosA, asientosB, asientosC):
        totalA=400*asientosA
        totalB=250*asientosB
        totalC=135*asientosC
        totalPago=totalA+totalB+totalC
        return totalPago

    print("El costo total es: $ %.2f" %(calcularPago(boletosa, boletosb, boletosc)))

main()

