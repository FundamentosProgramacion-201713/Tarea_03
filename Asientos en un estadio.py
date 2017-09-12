#Yerish Valdes Bernes A01375755
#Total a pagar por la compra de asientos en un estadio
def calcularPago(asientosA, asientosB, asientosC) :
    totalA=asientosA*400
    totalB = asientosB * 250
    totalC = asientosC * 135
    cuenta_total=totalA+totalB+totalC
    return cuenta_total

def main():
    claseA=int(input("Numero de asientos clase A:"))
    claseB=int(input("Numero de asientos clase B:"))
    claseD=int(input("Numero de asientos clase D:"))
    cuenta_total=calcularPago(claseA, claseB, claseD)
    print("El total a pagar por todos los boletos es de: %0.2f"%(cuenta_total))
main()