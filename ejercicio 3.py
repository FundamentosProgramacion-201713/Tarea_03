# Autor: LuisMiguel Baqueiro
# Matricula: 1745997
def calcularPagoNormal(hN, pH):
    pagoNormal = hN * pH
    return pagoNormal
def calcularPagoExtra(hE):
    pagoExtra = hE * 75
    return pagoExtra
def calcularPagoTotal(b, a):
    total = a + b
    return total
def main():
    hN = int(input("Teclea las horas normales trabajadas: "))
    hE = int(input("Teclea las horas extras trabahadas: "))
    pH = int(input("Teclea el pago por hora: "))
    print("")
    print("pago normal: $%.2f" % calcularPagoNormal(hN, pH))
    print("pago extra: $%.2f" % calcularPagoExtra(hE))
    print("-" * 24)
    print("pago total: $%.2f" % calcularPagoTotal(calcularPagoNormal(hN, pH), calcularPagoExtra(hE)))
main()