#encode: UTF-8

#Autor: Natalia Meraz Tostado   A01745008
#Descripción: calcular el pago de un trabajador contando horas extra

horasNormales = int(input("Teclea las horas nomales trabajadas: "))
horasExtra = int(input("Teclea las horas extra trabajadas: "))
pago = int(input("Teclea el pago por hora: "))

def calcularPagoNormal(horasNormales, pago):        #calcula el pago por sus horas de trabajo normales
    pagoNormal = horasNormales * pago
    return pagoNormal

def calcularPagoExtra(horasExtra, pago):            #calcula el pago por sus horas de trabajo extra
    pagoExtra = ((pago/2) + pago) * horasExtra
    return pagoExtra

def calcularPagoTotal(pagoNormal, pagoExtra):          #calcula el pago total de sus horas de trabajo
    pagoTotal = pagoNormal + pagoExtra
    return pagoTotal

def main():
    pagoNormal = calcularPagoNormal(horasNormales, pago)
    pagoExtra = calcularPagoExtra(horasExtra, pago)
    pagoTotal = calcularPagoTotal(pagoNormal, pagoExtra)
    print("")
    print("Pago normal: $%.2f" % pagoNormal)
    print("Pago extra: $%.2f" % pagoExtra)
    print("------------------------------")
    print("Pago total: $%.2f" % pagoTotal)

main()