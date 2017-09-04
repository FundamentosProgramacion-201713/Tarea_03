#encoding: UTF-8
#Omar Israel Galván García A01745810
#Este programa lee las horas normales, extras y el pago por hora. Imprime su pago semanal

def pagoNormal(horasNormales,pagoPorHora):     # esta función calcula el pago normal de un trabajador multuplicando sus horas normales por el pago por hora
    pagoNormal = horasNormales * pagoPorHora
    return pagoNormal

def pagoExtra(horasExtra, pagoPorHora):     # esta función calcula el pago extra de un trabajador multiplicando las oras extras por el
    pagoE = (horasExtra * pagoPorHora)     # pago por hora y sumando un 50% de las horas trabajadas
    pagoE = pagoE + (pagoE * 0.50)
    return pagoE

def main():                                     #la función principal lee los datos del usuario e imprime los resultados.
    print("")
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = int(input("Teclea el pago por hora: "))
    print("")
    pagoN  = pagoNormal(horasNormales,pagoPorHora)
    pagoEx = pagoExtra(horasExtra,pagoPorHora)
    pagoTotal = pagoEx + pagoN
    print("Pago normal: $%.2f"%(pagoN))
    print("Pago extra: $%.2f"%(pagoEx))
    print("--------------------------")
    print("Pago total: $%.2f"%(pagoTotal))


main()
