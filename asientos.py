#encode:UTC-8
#Autor: José Antonio Gómez Mora
#El programa lee el número de asientos de cada clase y regresa el total a pagar

#calcula el costo total con los parametros número de asientos tipo A, número de asientos tipo B y número de asientos tipo C
def calcularPago(asientosA, asientosB, asientosC):
    total=asientosA*400+asientosB*250+asientosC*135
    return total


def main():
    a=int(input("Ingresa el número de asientos tipo A: "))
    b=int(input("Ingresa el número de asientos tipo B: "))
    c=int(input("Ingresa el número de asientos tipo C: "))
    totalPago=calcularPago(a,b,c)
    print("Número de boletos clase A:",a)
    print("Número de boletos clase B:",b)
    print("Número de boletos clase C:",c)
    print("El costo total es:","$%d"%(totalPago))

main()