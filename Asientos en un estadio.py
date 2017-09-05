#encode: UTF-8
# Autor: David Ramírez Ríos, A01338802

#Calcular boletos en un estadio

def calcularPago (asientosA, asientosB, asientosC):

    totalPago = asientosA * 400 + asientosB * 250 + asientosC * 135
    return totalPago

def main ():

    numeroBoletosA = int (input("Número de asientos clase A: "))
    numeroBoletosB = int (input("Número de asientos clase B: "))
    numeroBoletosC = int (input("Número de asientos clase C: "))

    pago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)

    print("El costo total es: $%.2f" % (pago))

main()
