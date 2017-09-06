#encoding: UTF-8

#Autor: Javier Martínez Hernández  A01375496
#Descripción: Se calculará el costo por el tipo de asiento que quiera comprar

def calcularPago(asientosA, asientosB, asientosC):        #En la función se calculara el total a pagar
    asientosA=asientosA*400
    asientosB=asientosB*250
    asientosC=asientosC*135
    totalAPagar=asientosA+asientosB+asientosC
    return  totalAPagar

def main ():
    asientosA=int(input("Número de boletos de clase A: "))
    asientosB=int(input("Número de boletos de clase B: "))
    asientosC=int(input("Número de boletos de clase C: "))
    pagoTotal=calcularPago(asientosA,asientosB,asientosC)
    print("El costo total es: $ %.2f" %(pagoTotal))

main()
