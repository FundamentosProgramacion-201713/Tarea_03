# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González
# Matrícula: A01745998
# Descripción: Calcula tipo de asiento en un estadio e imprime el total.

def calcularPago(asientosA, asientosB, asientosC):
    totalA = asientosA * 400
    totalB = asientosB * 250
    totalC = asientosC * 135
    total = totalA + totalB + totalC
    return total

def main():
    asientosA = int(input("Inserte el número de asientos  de clase A: "))
    asientosB = int(input("Inserte el número de asientos  de clase B: "))
    asientosC = int(input("Inserte el número de asientos  de clase C: "))
    total = calcularPago(asientosA, asientosB, asientosC)
    print("Número de boletos de clase A: ",asientosA)
    print("Número de boletos de clase B: ",asientosB)
    print("Número de boletos de clase C: ",asientosC)
    print("El costo total es: $%.2f" % (total))

main()