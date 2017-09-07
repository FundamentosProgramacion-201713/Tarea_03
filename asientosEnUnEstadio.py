#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: te indica el total a pagar por el numero y clase de los asienntos que quieres comprar

def calcularPago(asientosA, asientosB, asientosC) :
    asientosA = numeroBoletosA * 400
    asientosB = numeroBoletosB * 250
    asientosC = numeroBoletosC * 135
    totalPago = asientosA + asientosB + asientosC
    return totalPago




def main () :
    numeroBoletosA = float(input("Número de boletos de clase A:"))
    numeroBoletosB = float(input("Número de boletos de clase B:"))
    numeroBoletosC = float(input("Número de boletos de clase C:"))

    print("El costo total es $%.2f" % totalPago)

main()