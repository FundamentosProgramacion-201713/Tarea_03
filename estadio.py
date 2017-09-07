#encode: UTF-8

#Autor: Natalia Meraz Tostado   A01745008
#Descripción: Calcula cuantos boletos quiere ccomprar alguien e imprime un total a pagar

claseA = int(400)
claseB = int(250)
claseC = int(135)
numeroBoletosA = (int(input("Número de boletos de clase A: ")))
numeroBoletosB = (int(input("Número de boletos de clase B: ")))
numeroBoletosC = (int(input("Número de boletos de clase C: ")))

def calcularAsientosA(numeroBoletosA):          #calcular el costo de cada asiento A
    asientosA = claseA * numeroBoletosA
    return asientosA

def calcularAsientosB(numeroBoletosB):           #calcular el costo de cada asiento B
    asientosB = claseB * numeroBoletosB
    return asientosB

def calcularAsientosC(numeroBoletosC):            #calcular el costo de cada asiento C
    asientosC = claseC * numeroBoletosC
    return asientosC

def calcularPago(asientosA, asientosB, asientosC):      # calcular el total a pagar de los boletos
    totalPago = asientosA + asientosB + asientosC
    return totalPago

def main():
    asientosA = calcularAsientosA(numeroBoletosA)
    asientosB = calcularAsientosB(numeroBoletosB)
    asientosC = calcularAsientosC(numeroBoletosC)
    totalPago = calcularPago(asientosA, asientosB, asientosC)
    print("El costo total es: $%.2f" % totalPago)

main()

