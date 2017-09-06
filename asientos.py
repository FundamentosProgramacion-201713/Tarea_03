#encoding: UTF-8
# Autor: Daniel Sahuer
# Calcula el valor total de boletos para asientos con costos diferentes con respecto a su clase


def calcularPago(asientosA,asientosB, asientosC): #Calcula el pago total sumando el precio de cada asiento
    A = asientosA * 400
    B = asientosB * 250
    C = asientosC * 135
    totalPago = A + B + C
    return totalPago #Regresar


def main():
    numeroBoletosA = int(input("Número de boletos de clase A: "))
    numeroBoletosB = int(input("Número de boletos de clase B: "))
    numeroBoletosC = int(input("Número de boletos de clase C: "))

    resultado = calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)

    print("El costo total es: $%.2f" %(resultado))

main()