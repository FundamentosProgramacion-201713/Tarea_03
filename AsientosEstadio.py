#encoding: UTF-8
#Autor: Irving Fuentes Aguilera
#Descripción: Programa que calcula el total a pagar de unos boletos

PRECIOA= 400
PRECIOB= 250
PRECIOC= 135

def calcularTotal(asientosA, asientosB, asientosC):
    totalPago= (asientosA*PRECIOA) + (asientosB*PRECIOB) + (asientosC*PRECIOC)

    return totalPago


def main():
    asientosA=int(input("Introducir # de boletos Clase A: "))
    asientosB=int(input("Introducir # de boletos Clase B: "))
    asientosC=int(input("Introducir # de boletos Clase C: "))
    total=calcularTotal(asientosA, asientosB, asientosC)
    print(total)

main()



