#encoding: UTF-8

#gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que calcula el pago nomal, el extra y el total de un trabajador

def horasNormales(horastrabajadas, pagoporhora):
    pagoNormales = horastrabajadas * pagoporhora
    return  pagoNormales

def horasExtra(horasETrabajadas, pagoporhora):
    pagoExtras = (horasETrabajadas * pagoporhora) +((pagoporhora*.50)*horasETrabajadas)
    return pagoExtras

def main():
    horasNormal = float(input("Teclea las horas normales trabajadas: "))
    horasEx = float(input("Teclea las horas extra trabajadas: "))
    pagoHora = float(input("Teclea el pago por hora: "))
    pagonormal= horasNormales(horasNormal,pagoHora)
    print("Pago normal: $%.2f" % pagonormal)
    pagoextra = horasExtra(horasEx, pagoHora)
    print("Pago extra: $%.2f" % pagoextra)
    print("--------------------")
    pagototal = pagonormal + pagoextra
    print("Pago total: $%.2f" % pagototal)

main()
