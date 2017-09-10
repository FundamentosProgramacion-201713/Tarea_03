# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González
# Matrícula: A01745998
# Descripción: Lee las horas normales, las horas extras y el pago por hora de un trabajador.

def calcularPagoN(horasN, pagoPorHora):
    pagoN = horasN * pagoPorHora
    return pagoN


def calcularPagoE(horasE, pagoPorHora):
    pagoE = horasE * pagoPorHora * 1.5
    return pagoE


def main():
    horasN = int(input("Teclea las horas normales trabajadas: "))
    horasE = int(input("Teclea las horas extra trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))
    pagoN = calcularPagoN(horasN, pagoPorHora)
    pagoE = calcularPagoE(horasE, pagoPorHora)
    pagoT= pagoN + pagoE
    print(" ")
    print("Pago normal: $%.2f" % (pagoN))
    print("Pago extra: $%.2f" % (pagoE))
    print("-----------------------")
    print("Pago total: $%.2f" % (pagoT))

main()