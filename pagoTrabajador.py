 #uncoding: UTF-8
#Autor: Ana María López Soto
#Descripción: Este programa calcúla el pago total de un trabajador

#Calcúla el pago total de las horas normales
def pagoNormal(horasTrabajadas, pagoHora):
    pagoTotalNormal = horasTrabajadas * pagoHora
    return pagoTotalNormal


#Calcúla el pago total de las Horas extras
def pagoHorasExtra(horasExtraTrabajadas,pagoHora):
    pagoTotalExtras = horasExtraTrabajadas * (pagoHora * 1.5)
    return pagoTotalExtras


def main():
    horasTrabajadas = int(input("Teclea las horas normales trabajadas: "))
    horasExtraTrabajadas = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = float(input("Teclea el pago por hora: "))
    print(     )
    print("Pago normal:$", pagoNormal(horasTrabajadas, pagoHora))
    print("Pago extra:$", pagoHorasExtra(horasExtraTrabajadas, pagoHora))
    print("-----------------------------")
    print("Pago total:$", (pagoNormal(horasTrabajadas, pagoHora)) + (pagoHorasExtra(horasExtraTrabajadas, pagoHora)))

main()

