#Encoding: UTF-8

#Autor: Alberto López Reyes
'''Descripción: Esta función calcula e imprime el pago normal, el pago extra, y el pago total resultante de la sumatoria de
las dos a partir de las horas normales y horas extras laboradas, y el pago por hora otorgados.'''

    #Esta función calcula el pago normal al recibir la cantidad de horas normales laboradas y el pago por hora.
def calcularPagoNormal(intHoras, intPagoHora):
    intPagoNormal = intHoras * intPagoHora
    return intPagoNormal

    #Esta función calcula el pago extra al recibir la cantidad de horas extra laboradas y el pago por hora. Este último se
    #magnifica al %150.
def calcularPagoExtra(intHorasExtra, intPagoHora):
    intPagoExtra = intHorasExtra * (intPagoHora*1.5)
    return intPagoExtra

    #Esta función calcula el pago total al recibir el pago normal y el pago extra.
def calcularPagoTotal(intPagoNormal, intPagoExtra):
    intPagoTotal = intPagoNormal + intPagoExtra
    return intPagoTotal

    #Esta función principal pide el número de horas normales y horas extra laboradas, y el pago por hora para otorgárselas
    #a la función "calcularPagoNormal" y "calcularPagoExtra" y así recibir el pago normal y el pago extra. Estas dos
    #últimas son otorgadas a la función "calcularPagoTotal" para recibir el pago total. Las tres cantidades recibidas
    #son posteriormente impresas.
def main():
    intHoras = int(input("Teclea las horas normales trabajadas: "))
    intHorasExtra = int(input("Teclea las horas extras trabajadas: "))
    intPagoHora = int(input("Teclea el pago por hora: "))

    intPagoNormal = calcularPagoNormal(intHoras, intPagoHora)
    intPagoExtra = calcularPagoExtra(intHorasExtra, intPagoHora)
    intPagoTotal = calcularPagoTotal(intPagoNormal, intPagoExtra)

    print("""""")
    print("Pago normal: $"+format(intPagoNormal, '.2f'))
    print("Pago extra: $"+format(intPagoExtra, '.2f'))
    print("-----------------------")
    print("Pago total: $"+format(intPagoTotal, '.2f'))

    #Se acciona la función "main".
main()
