#encoding: UTF-8
#Autor: Aaron Tonatiuh Villanueva Guzmán
#Este programa calcula el pago de un trabajador a partir de sus horas normales trabajadas así como las extra las cuales pagan 50% más

#Esta función permite calcular el pago a partir de las horas trabajadas y el pago por hora.
def calculopagoNormal(horasN, pagoH):
    pagoN=horasN*pagoH
    return(pagoN)

#Esta función calcula el pago extra del trabajador suponiendo que cada hora extra es pagada con un 50% adicional.
def calculopagoExtra(horasE, pagoH):
    pagoE=horasE* (pagoH*1.5)
    return(pagoE)

#Esta función Main lee las horas normales, horas extra y el pago por hora para calcular el pago total por horas normales, horas extra y el pago total por ambas.
def Main():
    horasNormales=int(input("Teclea las horas normales trabajadas: "))
    horasExtra=int(input("Teclea las horas extra trabajadas: "))
    pagoHora=float(input("Teclea el pago por hora: "))
    pagoNormalTotal=calculopagoNormal(horasNormales,pagoHora)
    pagoExtraTotal=calculopagoExtra(horasExtra,pagoHora)
    pagototal=pagoNormalTotal+pagoExtraTotal
    print("")
    print("Pago normal: $%.2f "% pagoNormalTotal)
    print("Pago extra: $%.2f "% pagoExtraTotal)
    print("-----------------------")
    print("Pago total: $%.2f "% pagototal)

Main()
