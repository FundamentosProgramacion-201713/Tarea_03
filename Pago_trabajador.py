#encoding: UTF-8
#Autor: Neftalí Rodríguez Martínez, A01375808.
#Calcula el pago de un trabajor de acuerdo a horas normales y horas extras de trabajo.


def calcularPnormal(horas_normales, pago_hora): #Calcula el pago por horas normales.
    pago_normal = horas_normales * pago_hora
    return pago_normal

def calcularPextra(horas_extras, pago_hora): #Calcula el pago por horas extras.
    pago_extra = horas_extras * (pago_hora * 1.5)
    return pago_extra

def main (): #Programa principal.

    horas_normales = float(input("Teclea las horas normales trabajadas: "))
    horas_extras = float(input("Teclea las horas extra trabajadas: "))
    pago_hora = float(input("Teclea el pago por hora: "))
    print("\r")

    pago_normal = calcularPnormal(horas_normales, pago_hora)
    print("Pago normal: $%.2f" % pago_normal)
    pago_extra = calcularPextra(horas_extras, pago_hora)
    print("Pago extra: $%.2f" % pago_extra)

    print("-----------------------")
    pagototal = pago_normal + pago_extra
    print("Pago total: $%.2f" % pagototal)

main()