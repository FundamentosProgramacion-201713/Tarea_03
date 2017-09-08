# encoding UTF-8
# autor: Jaime Orlando López Ramos, A01374696
# Descripción: Programa que calcule el total a pagar de boletos para un partido de futbol, donde se encuentran 3
# secciones con diferente precio cada una, preguntando cuántos boletos se comprarán en cada sección


# Crear una función (calcularPago()), que calcule el pago total, tomando como parámetros el número de boletos de cada
# sección
def calcularPago(asientosA, asientosB, asientosC):
    totalPago = (asientosA * 400) + (asientosB * 250) + (asientosC * 135)
    return totalPago


#Crear una función main que lea el número de asientos en cada sección y llame a la función previamente creada, asigná-
#ndole una variable para poder imprimir el total del pago
def main():
    numeroBoletosA = int(input("Introduzca el número de boletos en la clase A: "))
    numeroBoletosB = int(input("Itroduzca el número de boletos en la clase B: "))
    numeroBoletosC = int(input("Introduzca el número de boletos en la clase C: "))
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El total a pagar es de", totalPago, "pesos")


main()