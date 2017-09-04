#encoding: UTF-8

#Gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que calcula el pago nomal, el extra y el total de un trabajador

def calcularhorasNormales(horastrabajadas, pagoporhora):
    pagoNormales = horastrabajadas * pagoporhora
    return  pagoNormales

def calcularhorasExtra(horasETrabajadas, pagoporhora):
    pagoExtras = (horasETrabajadas * pagoporhora) +((pagoporhora*.50)*horasETrabajadas)
    return pagoExtras

def main():
    horasNormal = float(input("Teclea las horas normales trabajadas: "))
    horasEx = float(input("Teclea las horas extra trabajadas: "))
    pagoHora = float(input("Teclea el pago por hora: "))
    pagonormal= calcularhorasNormales(horasNormal,pagoHora)
    print("Pago normal: $%.2f" % pagonormal)
    pagoextra = calcularhorasExtra(horasEx, pagoHora)
    print("Pago extra: $%.2f" % pagoextra)
    print("--------------------")
    pagototal = pagonormal + pagoextra
    print("Pago total: $%.2f" % pagototal)

main()
