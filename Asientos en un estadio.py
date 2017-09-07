# UFT-8
#Autor: Javier León Alcántara
# Calcula el total a pagar por boletos comprados

def calcularPago(asientosA, asientosB, asientosC):    #Calcula el total a pagar

      totalA = asientosA * 400
      totalB = asientosB * 250
      totalC = asientosC * 135

      totalPago = totalA + totalB + totalC

      return (totalPago)


def main():    #Pide los datos, los envía a la función calcularPago e imprime el total

      numeroBoletosA = int(input("Número de boletos de clase A: "))
      numeroBoletosB = int(input("Número de boletos de clase B: "))
      numeroBoletosC = int(input("Número de boletos de clase C: "))

      totalPago= calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)

      print("El costo total es: $%.2f" %(totalPago))


main()
