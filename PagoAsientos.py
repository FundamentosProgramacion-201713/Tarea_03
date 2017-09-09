#encoding UTF-8
#Autor: Joaquin Rios Corvera A01375441

#Calcula el total a pagar con base en la cantidad de boletos de cada tipo
def calcularPago(asientosA, asientosB, asientosC):
    totalPago = asientosA * 400 + asientosB * 250 + asientosC * 135
    return totalPago

def main():
    numeroBoletosA = int(input("Número de boletos de clase A: "))
    numeroBoletosB = int(input("Número de boletos de clase B: "))
    numeroBoletosC = int(input("Número de boletos de clase C: "))

    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    round(totalPago, 2)

    print("El costo total es: $%.2f" %totalPago)

main()