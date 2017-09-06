#encoding: UTF-8
#Autor: Aaron Tonatiuh Villanueva Guzmán

def calculopagoNormal(horasN, pagoH):
    pagoN=horasN*pagoH
    return(pagoN)

def calculopagoExtra(horasE, pagoH):
    pagoE=horasE* (pagoH*1.5)
    return(pagoE)

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