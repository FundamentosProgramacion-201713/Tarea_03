#encoding UTF-8
#Autor: Joaquin Rios Corvera A01375441

#Calcula el pago de las horas normales de un trabajador
def calcularPagoNormal(pagoPorHora, horasNormal):
    total = pagoPorHora * horasNormal
    return total

#Calcula el pago de las horas extras de un trabajador
def calcularPagoExtra(pagoPorHora, horasExtra):
    total = pagoPorHora * horasExtra * 1.5
    return total

def calcularPagoTotal(pagoNormal, pagoExtra):
    total = pagoNormal + pagoExtra
    return total

def main():
    print("")
    horasNormal = int(input("Teclea las horas normales trabajadas: "))
    horasExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))
    print("")

    pagoNormal = calcularPagoNormal(pagoPorHora, horasNormal)
    pagoExtra = calcularPagoExtra(pagoPorHora, horasExtra)
    pagoTotal = calcularPagoTotal(pagoNormal, pagoExtra)

    print("Pago normal: $%.2f" %pagoNormal)
    print("Pago extra: $%.2f" %pagoExtra)
    print("-----------------------")
    print("Pago total: $%.2f" %pagoTotal)

main()