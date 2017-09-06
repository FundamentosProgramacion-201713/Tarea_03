#AUTOR: JOSÉ HEINZ MÖLLER SANTOS
#el programa calcula el pago normal de un trabajador, sus horas extras y el total

#calcula el pago normal, multiplica horas por el salario
def calcularPagoNormal(horasNormales, pagoHora):
    pNormal = horasNormales*pagoHora
    return pNormal

#calcula el pago extra, multiplica horas extra por el salario con un plus de 50% del mismo
def calcularPagoExtra(horasExtra, pagoHora):
    porcentaje = pagoHora * 0.5
    pExtra = (pagoHora + porcentaje) * horasExtra
    return pExtra

#calcula el total sumando todos los datos sacados anteriormente
def calcularTotal(pagoNormal,pagoExtra):
    pTotal = pagoNormal + pagoExtra
    return pTotal

#Es la función principal, lee los datos e imprime los resultados.
def main():
    horasNormales = float(input("Horas trabajadas: "))
    horasExtra = float(input("Horas extra trabajadas: "))
    pagoHora = float(input("Salario por hora de trabajo: "))

    pagoNormal = float(calcularPagoNormal(horasNormales,pagoHora))
    pagoExtra = float(calcularPagoExtra(horasExtra,pagoHora))
    sumaPagos = float(calcularTotal(pagoNormal,pagoExtra))
    print("     ")
    print("Pago normal es de $%.2f"%pagoNormal)
    print("Pago extra es de $%.2f"%pagoExtra)
    print("------------------------------")
    print("Pago total es de $%.2f"%sumaPagos)

main()