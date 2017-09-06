#encoding:UTF-8
#Autor: Carlos Pano Hernández

#Descripción: Este programa calcula el precio total de acuerdo al número de boletos requeridos por sección.

#Cálculo de precioA
def calcularPagoA(AsientosA):
    aA=400*AsientosA
    return aA

#PrecioB
def calcularPagoB(AsientosB):
    aB=250*AsientosB
    return aB

#PrecioC
def calcularPagoC(AsientosC):
    aC=135*AsientosC
    return aC

#PrecioTotal
def calcularTotal(a,b,c):
    total=a+b+c
    return total

#Función main
def main():
    a=calcularPagoA(int(input("Número de boletos de clase A:")))
    b=calcularPagoB(int(input("Número de boletos de clase B:")))
    c=calcularPagoC(int(input("Número de boletos de clase C:")))
    precioFinal=calcularTotal(a,b,c)
    print("El costo total es: $ %.2f"%(precioFinal))

#Principal
main()
