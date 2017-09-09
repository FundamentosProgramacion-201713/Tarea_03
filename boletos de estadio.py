#encoding: UTF-8
#Autor: Eduardo Roberto Müller Romero
#Descripción: Escribe un programa que calcule el precio según el tipo de boleto.


def main():
    boletosA = losboletosA()
    boletosB = losboletosB()
    boletosC = losboletosC()
    BoletoA = calcularBoletoA(boletosA)
    BoletoB = calcularBoletoB(boletosB)
    BoletoC = calcularBoletoC(boletosC)
    Total = BoletoA + BoletoB + BoletoC
    print("Precio por boletos tipo A", "$", BoletoA)
    print("Precio por boletos tipo B", "$", BoletoB)
    print("Precio por boletos tipo C", "$", BoletoC)
    print("Total a Pagar: ", Total)

def losboletosA():
    boletosA = int(input("N. de boletos de tipo A: "))
    return boletosA

def losboletosB():
    boletosB = int(input("N. de boletos de tipo B: "))
    return boletosB

def losboletosC():
    boletosC = int(input("n. de boletos de tipo C: "))
    return boletosC


def calcularBoletoA(boletosA):
    BoletosA = boletosA * 400
    return  BoletosA

def calcularBoletoB (boletosB):
    BoletosB = boletosB * 250
    return BoletosB

def calcularBoletoC(boletosC):
    BoletosC = boletosC * 135
    return BoletosC

main()