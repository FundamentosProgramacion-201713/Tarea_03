#encoding UTF-8
#Autor:Pablo Garcia Morales
#Programa para calcular ccuántos boletos quiere comprar para cada tipo de asiento y que imprima el total a pagar.

def claseA(numeroBoletosA):
    claseA=numeroBoletosA*400
    return claseA


def claseB(numeroBoletosB):
    claseB=numeroBoletosB*250
    return claseB



def claseC(numeroBoletosC):
    claseC=numeroBoletosC*135
    return claseC


def calcularPago(asientosA,asientosB,asientosC):
    totalpago = asientosA+asientosB+asientosC
    return totalpago


def main():
    numeroBoletosA= int(input("Número de boletos de clase A: "))
    numeroBoletosB= int(input("Número de boletos de clase B: "))
    numeroBoletosC= int(input("Número de boletos de clase C: "))
    asientosA=claseA(numeroBoletosA)
    asientosB=claseB(numeroBoletosB)
    asientosC=claseC(numeroBoletosC)
    calculartotalPago= calcularPago(asientosA, asientosB, asientosC)
    print("El costo total es: $%.2f" % (calculartotalPago))

main()




