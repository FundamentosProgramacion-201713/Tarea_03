#encoding UTF-8
#Autor:Pablo Garcia Morales
#Programa que lea las horas normales, las horas extra y el pago por hora de un trabajador.


def pagoN(horasN, pagoH):
    pagonormal=horasN*pagoH
    return pagonormal


def pagoE(horasE):
    horasextra=horasE*75
    return horasextra

def pagoT(pagoNormal, pagoExtra):
    pagoTotal=pagoNormal+pagoExtra
    return pagoTotal


def main():
    horasN=int(input("Teclea las horas normales trabajadas: "))
    horasE=int(input("Teclea las horas extra trabajadas: "))
    pagoH=int(input("Teclea el pago por hora: "))
    pagoNormal=pagoN(horasN,pagoH)
    pagoExtra=pagoE(horasE)
    pagoTotal=pagoT(pagoNormal,pagoExtra)
    print("Pago normal: $%.2f" % pagoNormal )
    print("Pago extra: $%.2f" % pagoExtra)
    print("-" * 24)
    print("Pago total: $%.2f" % pagoTotal)



main()



