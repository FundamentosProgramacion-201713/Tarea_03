#encoding: UTF-8
#Especificaciones del programa: Otroga el costo total de los boletos.
#Autor: Ernesto Ibhar Guevara Gomez
#Matricua: A01746121
def LeerboletosA():
    boletosA= int(input("Numero de boletos clase A: "))
    return boletosA
def LeerboletosB():
    boletosB=int(input("Numero de boletos clase B: "))
    return boletosB
def LeerboletosC():
    boletosC=int(input("Numero de boletos clase C: "))
    return boletosC
def CalcularboletosA(boletosA):
    Asientosa=boletosA * 400
    return Asientosa
def CalcularboletosB(boletosB):
    Asientosb=boletosB * 250
    return Asientosb
def CalcularboletosC(boletosC):
    Asientosc=boletosC * 135
    return Asientosc

def TotalPago(boletosA,boletosB,boletosC):
    Totalpagar=CalcularboletosA(boletosA) + CalcularboletosB(boletosB) + CalcularboletosC(boletosC)
    return Totalpagar


def main():
    numerodeboletosA=LeerboletosA()
    numerodeboletosB=LeerboletosB()
    numerodeboletosC= LeerboletosC()
    Totalapagar= TotalPago(numerodeboletosA,numerodeboletosB,numerodeboletosC)
    print("El costo total es: ", Totalapagar)


main()