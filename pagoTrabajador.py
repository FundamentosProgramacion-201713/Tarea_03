#Autor: Andrea Montero Rivas, A01374496
# Este programa ayuda a calcular el pago de un trabajador

def calculaPagoHoras(horas,pago):
    pagoHoras = horas * pago
    return pagoHoras

def calculaPagoHorasExtras(horasExtras,pago):
    pagoHorasExtras = horasExtras * (1.5*pago)
    return pagoHorasExtras

def main():
    horasTrabajadas = int(input("teclea las horas trabajadas:",))
    horasExtrasTrabajadas = int(input("teclea las horas extras trabajadas:",))
    pagoPorHora = int(input("teclea el pago por hora:",))
    pagoHoras = calculaPagoHoras(horasTrabajadas, pagoPorHora)
    pagoHorasExtra = calculaPagoHorasExtras(horasExtrasTrabajadas, pagoPorHora)
    pagototal=pagoHoras + pagoHorasExtra
    print(" %d de horas trabajadas, %d de horas extras trabajadas" % (pagoHoras,pagoHorasExtra))
    print("pago en total:", pagototal)

main()
