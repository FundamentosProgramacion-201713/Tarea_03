#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: con los valores de hrs normales, extras trabajadas y el pago por hora, se va a calcular su pago normal, el exta y el pago total que obtendra


#con base a los datos de hrNormales y pagoHora se crea la operación para calcular el normal (pago normal) y regresar el extra (pago normal)
def pagoNormal(hrsNormales, pagoHora):
    normal = hrsNormales * pagoHora
    return normal

#con base a los datos de hrsExtra y pagoHora se crea la operación para calcular el extra (pago extra) y regresar el extra (pago extra)
def pagoExtra(hrsExtras, pagoHora):
    extra = (hrsExtras*(pagoHora * .50)) + hrsExtras * pagoHora
    return extra


#con base a los datos de normal y extra de las funciones pagoNormal y pagoExtra se crea la operación para calcular el total (pago total) y regresar el total (pago total)
def pagoTotal(normal, extra):
    total = normal + extra
    return total


# se leen las horas trabajadas, las  horas extras y el pago por hora dados por el usuario y se imprime el pago normal, el extra, una linea de separación  y el pago total que se obtendra llamando a las funciónes pagoNormal (hrsNormales, pagoHora), pagoExtra(hrsExtras, pagoHora) y pagoTotal(normal, extra)
def main () :
    hrsNormales = float(input("Teclea las horas normales trabajadas:"))
    hrsExtras = float(input("Teclea las horas extras trabajadas:"))
    pagoHora = float(input("Teclea el pago por hora:"))
    print("Pago normal: %.2f" % pagoNormal(hrsNormales, pagoHora))
    print("Pago extra: %.2f" % pagoExtra(hrsExtras, pagoHora))
    print("----------------")
    print("Pago total: %.2f" % pagoTotal(pagoNormal(hrsNormales, pagoHora), pagoExtra(hrsExtras, pagoHora)))

#llama a la función main
main ()