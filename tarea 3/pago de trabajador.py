# coding: UTF-8
# autor: Eduardo Gallegos Solís
# Calcula el pago semanal de un trabajador.

def calcularPagoNormal (horasNorales, salarioPorHora):
    #calcula el salario por las horas normlaes trabajadas
    salarioNormal = horasNorales * salarioPorHora
    return salarioNormal

def calcularPagoExtra (horasExtras, salarioPorHora):
    # calcula el salario por horas extras
    salarioExtra = horasExtras * (salarioPorHora * 1.5)
    return salarioExtra
def calcularPagoTotal (salarioNormal, salarioExtra):
    # calcula el pago que recibirá el trabajador
    pagoTotal = salarioNormal + salarioExtra
    return pagoTotal

def main():
    horasNormales = int(input("Teclea las horas normales trabajadas:"))
    horasExtras = int(input("Teclea las horas extras trabajadas:"))
    pagoPorHora = int(input("Teclea el pago por hora:"))
    salarioNormal = calcularPagoNormal(horasNormales, pagoPorHora)
    salarioExtra = calcularPagoExtra(horasExtras, pagoPorHora)
    pagoTotal = calcularPagoTotal(salarioNormal,salarioExtra)
    print("")
    print("Pago normal: %.2f" %salarioNormal)
    print("Pago extra: %.2f" %salarioExtra)
    print("-------------------------")
    print("Pago total: %.2f" %pagoTotal)

main()