#encoding: UTF-8
#Nazdira Abigail Cerda del Prado A01375428
#Descripción: Diseño TopDown para calcular costo total por boletos de clase A, clase B y clase C.

A=400
B=250
C=135

def calcularPago (boletosa,boletosb,boletosc):
    totalpago=(A*boletosa)+(B*boletosb)+(C*boletosc)
    return totalpago

def main():
    boletosa=float(input("Número de boletos en clase A:"))
    boletosb=float(input("Número de boletos en clase B:"))
    boletosc=float(input("Número de boletos en clase C:"))
    calcpago=float(calcularPago(boletosa,boletosb,boletosc))
    print("El costo total es: $",calcpago)

main()