# encoding: UTF-8
# Autor: Luis Alfonso Alcántara López Ortega, A01374785

# Función para calcular el pago por las horas normales trabajadas
def calcularPagoHorasNormales(horasNormales, pago):

    pagoHN = horasNormales * pago

    return pagoHN


# Función para calcular el pago por las horas extras trabajadas
def calcularPagoHorasExtras(horasExtras, pago):

    pagoHE = horasExtras * pago * 1.5

    return pagoHE

# Función para calcular el pago total por las horas normales y extras trabajadas
def calcularPagoTotal(pagoNormal, pagoExtra):
    total = pagoNormal + pagoExtra

    return total


def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pago = float(input("Teclea el pago por hora: "))

    pagoHorasNormales = calcularPagoHorasNormales(horasNormales, pago)
    pagoHorasExtras = calcularPagoHorasExtras(horasExtras, pago)
    pagoTotal = calcularPagoTotal(pagoHorasNormales, pagoHorasExtras)

    print("\nPago normal: $", pagoHorasNormales, sep="")
    print("Pago extra: $", pagoHorasExtras, sep="")
    print("-----------------------")
    print("Pago total: $", pagoTotal, sep="")


main()
