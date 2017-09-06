#encoding: UTF-8
#Autor: Irving Fuentes Aguilera
#Descripción: Programa que calcula el pago por semana de un trabajador

def calcularPago(horas, pago):
    pagoNormal= pago* horas

    return pagoNormal

def calcularPagoExtra(horasExtra, pago):
    pagoExtra= (pago*1.50) * horasExtra

    return pagoExtra

def calcularPagoTotal(pagoExtra, pagoNormal):
    pagoTotal= pagoNormal + pagoExtra

    return pagoTotal



def main():
    horas=int(input("Teclear las horas trabajadas:"))
    horasExtra=int(input("Teclear las horas extra trabajadas:"))
    pago=int(input("Teclear el pago por hora: "))
    pagoNormal=calcularPago(horas, pago)
    pagoExtra= calcularPagoExtra(horasExtra, pago)
    pagoTotal=calcularPagoTotal(pagoExtra, pagoNormal)
    print("Pago normal:$ ",pagoNormal)
    print("Pago extra:$ ", pagoExtra)
    print("-------------------")
    print("Pago total:$ ", pagoTotal)

main()