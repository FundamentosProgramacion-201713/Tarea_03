# encoding UTF-8
# Autor: Jaime Orlando López Ramos, A01374696
# Descripción: Un programa que lea el pago por hora del trabajador, las horas normales trabajadas y las
# horas extras trabajadas, para poder imprimir el pago por horas normales, el pago pr horas extras y el total de ambas


# Una función que calcule el pago total por las horas normales trabajadas, tomando como parámetros el pago por hora
# y las horas normales trabajadas. Multiplicando uno por el otro para poder regresar el pago por horas normales trabajadas
def calcularPagoNormal(phn, hnt):
    pagohn = phn * hnt
    return pagohn


# Una función que calcule el pago por horas extra trabajadas, tomando como parámteros las horas extra trabajas y el pago
# por una hora normal trabajada. Para calcularlo, la función multiplica el pago por hora normal y las horas extra
# trabajadas, para posteriormente multiplicar dicho resultado por 1.5 y poder regresar el valor del pago total por
# horas extra.
def calcularPagoExtra(phn, het):
    pagoE = (phn * het) * 1.5
    return pagoE


# Una función que calcule el pago total del trabajador, tomando como parámetros los pagos totales por horas extra y
# normales laboradas. Esta función suma dichos valores para poder regresar el pago total del trabajdor.
def calcularPagoTotal(pagoHoraN, pagoHoraE):
    pagoT = pagoHoraN + pagoHoraE
    return pagoT



# Una función main que lea el pago por hora normal, las horas extra trabajadas y las normales trabajadas. Posteriormente
#llamará a cada una de las funciónes pasadas, otorgándoles una variable y de este modo poder imprimir los datos requeridos
def main():
    phn = int(input("Introduzca su paga por hora normal trabajada: "))
    hnt = int(input("Introduzca el número de horas normales laboradas: "))
    het = int(input("Introduzca el número de horas extra trabajdas: "))
    pagoHoraNormal = calcularPagoNormal(phn, hnt)
    pagoHoraExtra = calcularPagoExtra(phn, het)
    pagoTotal = calcularPagoTotal(pagoHoraNormal, pagoHoraExtra)
    print("Su pago por horas normales laboradas es de:", pagoHoraNormal, "pesos")
    print("Su pago por horas extras laboradas es de:", pagoHoraExtra, "pesos")
    print ("Su pago total es de:", pagoTotal, "pesos")

main()
