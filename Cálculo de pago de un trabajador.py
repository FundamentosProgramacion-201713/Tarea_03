#encoding: UTF-8

#Autor: Javier Martínez Hernández  A01375496
#Descripción: Se calculara el pago semanal de un trabajador, incluyendo sus horas extras

def calcularElPagoExtra(horasExtras, pagoPorHora):              #Se calculará el pago por horas extra del trabajador
    pagoPorHoraExtra=pagoPorHora*.5
    montoExtra=pagoPorHoraExtra+pagoPorHora
    pagoSemanalExtra=horasExtras*montoExtra
    return pagoSemanalExtra

def calcularElPagoNormal(horasNormales, pagoPorHora):           #Se calculará el pago por horas normales del trabajador
    pagoSemanalNormal=horasNormales*pagoPorHora
    return pagoSemanalNormal


def main():
    horasNormales=int(input("Teclea las horas normales trabajadas: "))
    horasExtras=int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora=int(input("Teclea el pago por hora: "))
    pagoSemanalNormal=calcularElPagoNormal(horasNormales,pagoPorHora)
    pagoSemanalExtra=calcularElPagoExtra(horasExtras,pagoPorHora)
    pagoTotalSemanal=pagoSemanalNormal+pagoSemanalExtra
    print("Pago normal: $%.2f \nPago extra: $%.2f \n---------------------- \nPago total: $%.2f" %(pagoSemanalNormal,pagoSemanalExtra,pagoTotalSemanal))
main()