#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: con los valores de hrs normales, extras trabajadas y el pago por hora, se va a calcular su pago normal, el exta y el pago total que obtendra


def pagoNormal(hrsNormales, pagoHora):
    normal = hrsNormales * pagoHora
    return normal


def pagoExtra(hrsExtras, pagoHora):
    extra = (hrsExtras*(pagoHora * .50)) + hrsExtras * pagoHora
    return extra


def pagoTotal(normal, extra):
    total = normal + extra
    return total


def main () :
    hrsNormales = float(input("Teclea las horas normales trabajadas:"))
    hrsExtras = float(input("Teclea las horas extras trabajadas:"))
    pagoHora = float(input("Teclea el pago por hora:"))
    print("Pago normal: %.2f" % pagoNormal(hrsNormales, pagoHora))
    print("Pago extra: %.2f" % pagoExtra(hrsExtras, pagoHora))
    print("----------------")
    print("Pago total: %.2f" % pagoTotal(pagoNormal(hrsNormales, pagoHora), pagoExtra(hrsExtras, pagoHora)))

main ()