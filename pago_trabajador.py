#encoding: UTF-8

#Gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que calcula el pago normal, el pago extra y el total de un trabajador

#Función que calcula el pago de horas normales trabajadas
def calcularhorasNormales(horastrabajadas, pagoporhora):
    pagoNormales = horastrabajadas * pagoporhora
    return  pagoNormales

#Función que calcula el pago por horas extras trabajadas
def calcularhorasExtra(horasETrabajadas, pagoporhora):
    pagoExtras = (horasETrabajadas * pagoporhora) +((pagoporhora*.50)*horasETrabajadas)
    return pagoExtras

#Funcion que suma el pago por horas extra y normales
def calcularpagototal(normal, extra):
    total = normal + extra
    return  total

#Función principal main que lee inputsn, llama a las demas funciones e imprim
def main():
    horasNormal = float(input("Teclea las horas normales trabajadas: "))
    horasEx = float(input("Teclea las horas extra trabajadas: "))
    pagoHora = float(input("Teclea el pago por hora: "))
    pagonormal= calcularhorasNormales(horasNormal,pagoHora)
    print("Pago normal: $%.2f" % pagonormal)
    pagoextra = calcularhorasExtra(horasEx, pagoHora)
    print("Pago extra: $%.2f" % pagoextra)
    print("--------------------")
    pagototal = calcularpagototal(calcularhorasNormales(horasNormal,pagoHora),calcularhorasExtra(horasEx, pagoHora) )
    print("Pago total: $%.2f" % pagototal)

main()
