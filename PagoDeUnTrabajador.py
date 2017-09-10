# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González
# Matrícula: A01745998
# Descripción: Calcula pago normal, por horas extra y pago total a un empleado.

# calcula pago por horas normales
def calcularPagoN(horasN, pagoPorHora):
    pagoN = horasN * pagoPorHora
    return pagoN

# calcula pago por horas extra
def calcularPagoE(horasE, pagoPorHora):
    pagoE = horasE * pagoPorHora * 1.5
    return pagoE

# lee horas normales y extras, calcula pago total e imprime pago normal, pago extra y pago total
def main():
    horasN = int(input("Teclea las horas normales trabajadas: "))
    horasE = int(input("Teclea las horas extra trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))
    pagoN = calcularPagoN(horasN, pagoPorHora)
    pagoE = calcularPagoE(horasE, pagoPorHora)
    pagoT = pagoN + pagoE
    print(" ")
    print("Pago normal: $%.2f" % (pagoN))
    print("Pago extra: $%.2f" % (pagoE))
    print("-----------------------")
    print("Pago total: $%.2f" % (pagoT))

main()