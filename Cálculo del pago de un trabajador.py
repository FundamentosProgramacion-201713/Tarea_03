#enconding: UTF-8
#Alejandro Chávez Campos, A01374974
#Este es para calcular el pago semanal de un trabajador a partir de sus horas normales, horas extras y el pago por hora.

def calcularPago(horasNormales, pago): #Calcula el pago de las horas normales
    pagoNormal= horasNormales*pago
    return pagoNormal


def calcularPagoExtra(horasExtras, pago): #Calcula el pago de las horas extras
    pagoExtra=horasExtras*(pago*1.5)
    return pagoExtra


def main(): #Programa principal
    horasNormales=float(input("Teclea las horas normales trabajadas: "))
    horasExtras= float(input ("Teclea las horas extras trabajadas: "))
    pago=float(input("Teclea el pago por hora: "))
    pagoNormal= calcularPago(horasNormales,pago)
    pagoExtra= calcularPagoExtra(horasExtras, pago)
    pagoTotal= pagoNormal+pagoExtra #Calcula el pago total sumando el pago normal y el extra
    print ()
    print("Pago normal: $%.2f"%pagoNormal)
    print("Pago extra: $%.2f"%pagoExtra)
    print("-----------------------")
    print ("Pago total: $%.2f"%pagoTotal)
main()
