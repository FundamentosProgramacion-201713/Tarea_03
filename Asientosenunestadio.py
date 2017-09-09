#Encoding: UTF-8

#Autor: Alberto López Reyes
'''Descripción: Este programa calcula e imprime el costo total de boletos al ser otorgado la cantidad de boletos clase A,
clase B, y clase C que se quieren pagar.'''

    #Esta función calcula el total a pagar de boletos al recibir la cantidad de boletos clase A, clase B, y clase C.
def calcularPago(asientosA, asientosB, asientosC):
    intPagoClaseA = asientosA * 400
    intPagoClaseB = asientosB * 250
    intPagoClaseC = asientosC * 135
    fltTotalPago = float(intPagoClaseA + intPagoClaseB + intPagoClaseC)
    return fltTotalPago

    #Esta función principal pide el número de boletos clase A, clase B, y clase C para obtener e imprimir el valor del
    #total a pagar a partir de la función "calcularPago".
def main():
    asientosA = int(input("Número de boletos de clase A: "))
    asientosB = int(input("Número de boletos de clase B: "))
    asientosC = int(input("Número de boletos de clase C: "))

    fltTotalPago = calcularPago(asientosA, asientosB, asientosC)

    print("El costo total es: $"+format(fltTotalPago, '.2f'))

    #Se acciona la función "main".
main()
