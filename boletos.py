#encoding UTF-8
#Anaid Fernanda Labat González A01746289
#Descripción: Calcular el costo total de boletos

def calcularPago (asientosA, asientosB, asientosC):
    pagoTotal=(asientosA*400)+(asientosB*250)+(asientosC*135)
    return pagoTotal

def main():
    numeroBoletosA=int(input("Número de boletos de clase A:"))

    numeroBoletosB=int(input("Número de boletos de clase B:"))

    numeroBoletosC=int(input("Número de boletos de clase C:"))

    total= calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)
    print("El costo total es:",total)
main()