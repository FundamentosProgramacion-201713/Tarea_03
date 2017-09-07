# encoding: UTF-8

# Autor: Iván Alejandro Dumas Martínez
# Descripción: Este programa lee las horas normales, horas extra y pago por hora de un trabajador y calcula el total semanal

def calcularPagoNormal(pagoHora, hrsNormal): # Función que calcula el pago por las horas normales trabajadas
    pagoNormal = pagoHora * hrsNormal
    return pagoNormal


def calcularPagoExtra(pagoHora, hrsExtra): # Función que calcula el pago por las horas extra trabajadas
    pagoExtra = pagoHora * 1.5 * hrsExtra
    return pagoExtra


def main(): # Función principal
    hrsNormal = int(input("Teclea las horas normales trabajadas: "))
    hrsExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: $"))
    pagoNormal = calcularPagoNormal(pagoHora, hrsNormal)
    pagoExtra = calcularPagoExtra(pagoHora, hrsExtra)
    pagoTotal = pagoNormal + pagoExtra
    print ("""Pago normal: $%.2f
Pago extra: $%.2f
----------------------
Pago total: $%.2f""" % (pagoNormal, pagoExtra, pagoTotal))


# Llamar a la función principal
main()
