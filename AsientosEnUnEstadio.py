# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González
# Matrícula: A01745998
# Descripción: Calcula el pago para cada tipo de asiento en un estadio y total por los boletos.

# calcula pago por tipo de asiento y pago total
def calcularPago(asientosA, asientosB, asientosC):
    totalA = asientosA * 400
    totalB = asientosB * 250
    totalC = asientosC * 135
    total = totalA + totalB + totalC
    return total

# lee número de boletos por cada clase e imprime el costo total
def main():
    asientosA = int(input("Número de boletos de clase A: "))
    asientosB = int(input("Número de boletos de clase B: "))
    asientosC = int(input("Número de boletos de clase C: "))
    total = calcularPago(asientosA, asientosB, asientosC)
    print("El costo total es: $%.2f" % (total))

main()