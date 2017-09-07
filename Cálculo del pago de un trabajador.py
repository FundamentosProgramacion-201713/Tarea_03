# UFT-8
#Autor: Javier León Alcántara
# Calcula el pago normal,extra y total de un trabajador

def calcularPagoNormal(horasNormales,pago):   #Calcula pago normal
     pagoNormal = horasNormales*pago
     return pagoNormal


def calculoPagoExtra(horasExtras, pago):     #Calcula pago extra
     pagoExtra = horasExtras * (pago * 1.5)
     return pagoExtra


def main():                  #Pide los datos y calcula con las funciones los resultados
     horasNormales = float(input("Teclea las horas normales trabajadas: "))
     horasExtras = float(input("Teclea las horas extras trabajadas: "))
     pago = float(input("Teclea el pago por hora: "))

     pagoNormal = calcularPagoNormal(horasNormales,pago)
     pagoExtra = calculoPagoExtra(horasExtras,pago)
     total = pagoNormal + pagoExtra

     print("")
     print("Pago normal:","$%.2f"%(pagoNormal))
     print("Pago extra:","$%.2f"%(pagoExtra))
     print("-----------------------")
     print("Pago total:","$%.2f"%(total))

main()