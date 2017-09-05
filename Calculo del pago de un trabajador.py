#encode: UTF-8
# Autor: David Ramírez Ríos, A01338802
# Calcular el pago semanal de un trabajador

def calcularPagoNormal (hora, pago):

    pagoNormal = hora * pago
    return pagoNormal

def calcularPagoExtra (extra, pago):

    pagoExtra = extra * pago * 1.5
    return pagoExtra

def main():

    hora = int (input("Teclea las horas normales trabajadas: "))
    extra = int (input("Teclea las horas extras trabajadas: "))
    pago = float (input("Teclea el pago por hora: "))

    pagoNormal = calcularPagoNormal(hora, pago)
    pagoExtra = calcularPagoExtra(extra, pago)
    pagoTotal = pagoExtra + pagoNormal

    print("Pago normal: $%.2f" % (pagoNormal))
    print("Pago extra: $%.2f" % (pagoExtra))
    print("----------------------------------")
    print("Pago total: $%.2f" % (pagoTotal))

main()