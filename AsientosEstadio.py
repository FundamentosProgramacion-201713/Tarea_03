#encoding: UTF-8
#Autor: Dora Gabriela Lizárraga González A01229599
#Con este programa se podrá calcular el costo total al comprar diferentes asientos en un estadio

#Esta función calcula el costo total
def calcularPago(asientosA,asientosB,asientosC):
    costoA = asientosA*400
    costoB = asientosB*250
    costoC = asientosC*135
    costoTotal = costoA+costoB+costoC
    return (costoTotal)

#Esta función lee los valores de las variables, ejecuta las otras funciones e imprime el resultado
def main():
    asientosA = float(input('Número de boletos de clase A: '))
    asientosB = float(input('Número de boletos de clase B: '))
    asientosC = float(input('Número de boletos de clase C: '))
    costoTotal = calcularPago(asientosA,asientosB,asientosC)
    print('El costo total es: $', costoTotal )

main()