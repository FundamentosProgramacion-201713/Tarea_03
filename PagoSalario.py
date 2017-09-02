#encoding UTF-8
#Autor: Leonardo Castillejos Vite
#Descripción: Lee las horas, horas extras y el pago por hora de un  trabajador e imprime lo que le pagan a este en total

def pagoNormal (horasNormal, pagoHora):
    pagoNormalT = horasNormal * pagoHora
    return pagoNormalT

def pagoExtra (horasExtra, pagoHora):
    pagoExtraT = horasExtra * (pagoHora * 1.5)
    return pagoExtraT

def main():
    horaNormal = int(input("Teclea las horas normales trabajadas: "))
    horaExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    pagoNorm = pagoNormal(horaNormal, pagoHora)
    pagoExt = pagoExtra(horaExtra, pagoHora)
    pagoTotal = pagoNorm + pagoExt
    print("Pago normal: $%.2f" % (pagoNorm))
    print("Pago extra: $%.2f" % (pagoExt))
    print("------------------------------------")
    print("Pago total: $%.2f" % (pagoTotal))

main()



