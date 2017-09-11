#encoding: UTF-8
#Autor: Neftalí Rodríguez, A01375808.
#Calcula el total a pagar por núm de asientos A, asientos B y Asientos C.


#Calcula el pago total dependiendo el núm de asientos A, B y C.
def calcularPago(asientosA, asientosB, asientosC):
    totalpago = ((asientosA * 400) + (asientosB * 250) + (asientosC * 135))
    return totalpago

def main (): #Programa principal.

    numeroBoletosA = int(input("Número de boletos de la clase A: "))
    asientosA = numeroBoletosA

    numeroBoletosB = int(input("Número de boletos de la clase B: "))
    asientosB = numeroBoletosB

    numeroBoletosC = int(input("Número de boletos de la clase C: "))
    asientosC = numeroBoletosC

    totalpago = calcularPago (asientosA, asientosB, asientosC)
    print(("El costo total es: $%.2f") % (totalpago))

main()