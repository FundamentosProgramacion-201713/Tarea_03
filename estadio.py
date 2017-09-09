#encoding-UTF-8
#AUTOR: José Antonio Vázquez Gabián
#Este programa calcula el costo total de asientos adquiridos según su clase y número.

#Esta función calcula y guarda en la variable totalPago el total a pagar
def calcularPago(asientosA, asientosB, asientosC):
    precioA=asientosA*400
    precioB=asientosB*250
    precioC=asientosC*135
    totalPago= precioA +precioB +precioC
    return totalPago
 #Esta función captura el número de boletos comprados de cada clase e imprime el costo total
def main() :
     numeroBoletosA = int(input("Leer el número de asientos de clase A: "))
     numeroBoletosB = int(input("Leer el número de asientos de clase B: "))
     numeroBoletosC = int(input("Leer el número de asientos de clase C: "))
     total = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
     print("El costo total es : $ %d.00" % total)

main()