#encoding: UTF-8

#Autor: Roberto Téllez Perezyera
#Este programa calcula el total a pagar al comprar asientos de una o hasta tres clases diferentes en un estadio.
#Primera práctica de uso de funciones fuera del salón de clases.


#Multiplica la cantidad de boletos (por clase) por sus respectivos precios. Calcula el total a pagar.
def calcularPago(qBoletoClaseA, qBoletoClaseB, qBoletoClaseC) :
    asientosA = 400 * qBoletoClaseA
    asientosB = 250 * qBoletoClaseB
    asientosC = 135 * qBoletoClaseC
    totalPago = asientosA + asientosB + asientosC
    return totalPago

#aquí definimos las lecturas que hará el programa, los calculos a realizar con funciones, y los resultados a entregar
def main() :
    qBoletoClaseA = int(input("Número de boletos de clase A: "))
    qBoletoClaseB = int(input("Número de boletos de clase B: "))
    qBoletoClaseC = int(input("Número de boletos de clase C: "))
    totalPago = calcularPago(qBoletoClaseA, qBoletoClaseB, qBoletoClaseC)
    print ("El costo total es: $%.2f" % (totalPago))


main()