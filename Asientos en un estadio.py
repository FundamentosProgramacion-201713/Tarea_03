#encoding: UTF-8
#Autor: Luis Fernando Figueroa Rendon, A01746139

#Calcular el total a pagar de la compra de boletos para el estadio.

ba= int(input("Numero de boletos de clase A: $"))
bb= int(input("Numero de boletos de clase B: $"))
bc= int(input("Numero de boletos de clase C: $"))

def calcularPago (asientosA, asientosB, asientosC):
    aA=400*asientosA
    aB=250*asientosB
    aC=135*asientosC
    totalPago=aB+aB+aC
    return totalPago

def main():
    print("El costo total es: $", calcularPago(ba, bb, bc))

main()

