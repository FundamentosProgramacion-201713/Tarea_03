#encoding-UTF-8
#AUTOR: José Antonio Vázquez Gabián
#Este programa calcula el pago de una trabajador por horas normales, horas extras y el total de pago.

#En esta funcion calculamos los pagos de un trabajador en jornada normal
def calcularpagoNormal(horasN, pago):
    pagoNormal = horasN * pago
    return pagoNormal
 # Calcula el pago por horas extras del trabajador
def calcularpagoExtra(HorasE, pago):
    pagoExtra = HorasE * (pago * 1.5)
    return pagoExtra
# Calcula el pago total
def calcularpagototal(pagoN, pagoE):
    pagoTotal = pagoN+pagoE
    return pagoTotal
# Esta función main llama a las funciones anteriores e imprime el pago normal, el pago extra y el pago total.
def main():
   horasN = float(input("Teclea las horas normales trabajadas: "))
   horasEx = float(input("Teclea las horas extras trabajadas: "))
   pago = float(input("Teclea el pago por hora: "))
   pagoNormal = calcularpagoNormal(horasN,pago)
   pagoExtra = calcularpagoExtra(horasEx,pago)
   pagoTotal = calcularpagototal(pagoNormal,pagoExtra)
   print("")
   print("Pago normal: $%.2f" %(pagoNormal))
   print("Pago extra: $%.2f" %(pagoExtra))
   print("-----------------------")
   print("Pago total: $%.2f" %(pagoTotal))
main()