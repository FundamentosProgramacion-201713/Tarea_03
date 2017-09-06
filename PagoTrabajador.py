#encoding:UTF-8
#Autor: Carlos Pano Hernández

#Descripción: Este programa calcula el pago total del trabajador de acuerdo a las horas extra trabajadas, incluyendo el pago de hora actual y horas normales trabajadas.

#PagoNormal
def calcularPagoNormal(horasNormales,pagoHora):
    pagoNormal=horasNormales*pagoHora

    return pagoNormal

#PagoExtra
def calcularPagoExtra(horasExtra,pagoHora):
    pagoExtra=(horasExtra*pagoHora)+((horasExtra*pagoHora)/2)
    return pagoExtra

#PagoTotalConExtra
def calcularPagoTotal(normal,extra):
    total=normal+extra
    return total

#FunciónMain
def main():
    horasNormales=int(input("Teclea las horas normales trabajadas:"))
    horasExtra=int(input("Teclea las horas extras trabajadas:"))
    pagoHora=float(input("Teclea el pago por hora:"))

    pagoN=calcularPagoNormal(horasNormales,pagoHora)
    pagoE=calcularPagoExtra(horasExtra,pagoHora)
    pagoT=calcularPagoTotal(pagoN,pagoE)

    print("")
    print("Pago normal: $%.2f"%(pagoN))
    print("Pago extra: $%.2f"%(pagoE))
    print("-----------------------------")
    print("Pago total: $%.2f"%(pagoT))

#Principal
main()
