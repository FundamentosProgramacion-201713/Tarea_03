#encoding: utf-8
#written by Jordan González Bustamante
#Este programa calcula el pago correspondiente a un trabajador, según las horas trabajadas, ya sean normales, o extra (que se pagan 50% más).

#En ésta función calculamos los pagos parciales, y totales, según los datos ingresados.
def calcularPago(horasTotales, horasExtra, pagoPorHora):
    pagoNormales = horasTotales * pagoPorHora
    pagoExtra = (horasExtra * pagoPorHora) + ((horasExtra * pagoPorHora)/2)
    pagoTotal = pagoExtra + pagoNormales
    return pagoNormales, pagoExtra, pagoTotal

#En main, pedimos el total de horas trabajas, normales y extras, además de requerir el pago por hora para
# llamar a la función anterior y obtener todos los pagos correspondientes.
def main():
    horasT = int(input("Teclea las horas normales trabajadas : "))
    horasE = int(input("Teclea las horas extras trabajadas   : "))
    pagoH = float(input("Teclea el pago por hora : "))
    pagoN, pagoE, pagoT = calcularPago(horasT, horasE, pagoH)
    print("Pago normal : $ %.2f" % pagoN)
    print("Pago extra  : $ %.2f" % pagoE)
    print("----------------------------")
    print("Pago total  : $ %.2f" % pagoT)
main()
