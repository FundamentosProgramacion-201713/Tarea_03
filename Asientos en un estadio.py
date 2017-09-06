#encoding: UTF-8
#Autor: Aaron Tonatiuh Villanueva Guzmán
#Este programa calcula el costo total de asientos adquiridos según su clase y número.

#Esta función procesa el costo del número comprado de asientos según su clase a partir de la variable definida por el texto.
def calcularPago(asientosA, asientosB, asientosC):
    costoA= asientosA*400
    costoB= asientosB*250
    costoC= asientosC*135
    totalPago = costoA + costoB + costoC
    return totalPago

#Esta función captura el número de asientos comprados de cada clase e imprime el costo total
def main():
    claseA = int(input("Número de boletos de clase A: "))
    claseB = int(input("Número de boletos de clase B: "))
    claseC = int(input("Número de boletos de clase C: "))
    total=calcularPago(claseA, claseB, claseC)
    print("El costo total es de: $% .2f "% total)
main()