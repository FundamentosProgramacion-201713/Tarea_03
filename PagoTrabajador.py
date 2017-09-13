# encode UFT-8
# Autor: Luis Enrique Neri Pérez
# Programa que permita calcular el pago a un trabajador en base al costo por hora, horas trabajadas y hras extras trabajadas

def costoHora (horasNormales, pago): #Esta función calcula el monto a pagar por las horas de trabajo normales
    pagoHoraNormal = horasNormales * pago
    return pagoHoraNormal

def costoHoraExtra(horasExtras, pago): #Esta función calcula en monto a pagar por las horas de trabajo extras
    pagoHoraExtra = 1.5 * horasExtras * pago
    return pagoHoraExtra

def totalPago(costoHoras, costoHoraExtras): #Esta función calcula el pago total de horas de tranbajo normales y extras
    pagoTotal = costoHoras + costoHoraExtras
    return pagoTotal

def main(): #Esta función solicita el número de horas normales, número de horas extras y el costo por hora, posteriormente llama a las funciones costoHoras, costoHoraExtras, pagoTotal e imprime los reultados
    horasNormales = int(input("Ingrese el númeo de horas trabajadas: "))
    horasExtras = int(input("Ingrese el número de horas extras trabajadas: "))
    pago = float(input("Ingrese es pago por hora: "))
    costoHoras= costoHora(horasNormales, pago)
    costoHoraExtras = costoHoraExtra(horasExtras, pago)
    pagoTotal = totalPago(costoHoras,costoHoraExtras)
    print("")
    print("Pago Normal: $%.2f" % costoHoras)
    print("Pago Extra: $%.2f" % costoHoraExtras)
    print("---------------------------------------")
    print("PAGO TOTAL: $%.2f" % pagoTotal)
main()
