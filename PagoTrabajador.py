#encoding: UTF-8
# Autor: Daniel Sahuer
# Calcula horas de trabajo normales y extras de un trabajador


def calcularPagoNormal(normal,hora): #Calcula el pago normal
    totalPagoNormal = normal * hora
    return totalPagoNormal #Regresar


def calcularPagoExtra(extra,hora): #Calcula el pago extra
    totalPagoExtra = extra * (hora + ((hora * 50)/100))
    return totalPagoExtra #Regresar


def calcularPagoTotal(normal,extra): #Calcula el pago total sumando el pago normal y el extra
    totalPagoTotal = normal + extra
    return totalPagoTotal #Regresar

def main():
    numeroHorasNormales = int(input("Teclea las horas normales trabajadas: "))
    numeroHorasExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))

    pagoNormal = calcularPagoNormal(numeroHorasNormales,pagoHora)
    pagoExtra = calcularPagoExtra(numeroHorasExtra,pagoHora)
    pagoTotal = calcularPagoTotal(pagoNormal,pagoExtra)

    print("\nPago normal: $%.2f\nPago extra: $%.2f\n--------------------------\nPago total: $%.2f" %(pagoNormal,pagoExtra,pagoTotal))

main()