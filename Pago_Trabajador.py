#Autor: Maria Fernanda Torres Velazquez A01746537
#El siguiente programa, calcula el pago semanal de un trabajador

#Funcion que recibe como parametro las horas trabajadas y el pago por hora y regresa el pago normal
def CalcularPagoNormal (horast,pagoh):
    pagoN= horast*pagoh
    return pagoN

#Funcion que recibe como parametro las horas extra trabajadas y el pago por hora y regresa el pago extra
def CalcularPagoExtra (horasExtra,pagoh):
    pagoExtra= horasExtra*(pagoh + (pagoh/2))
    return pagoExtra

#Funcion principal en la que se introducen las horas normales, extra y pago por hora y lo envia a las funciones calcularPagoNormal, calcularPagoExtra
# para que estas regresen pago normal y extra y al final se calcule el pago total.
def main():
    horasN = float(input("Introduce las horas normales trabajadas: "))
    horasE = float(input("Introduce las horas extra trabajadas   : "))
    pago =   float(input("Introduce el pago por hora             : "))
    pagoN= CalcularPagoNormal(pago,horasN)
    pagoE = CalcularPagoExtra(pago,horasE)
    total = pagoN+pagoE
    print("")
    print("Pago normal: $%.2f" % (pagoN))
    print("Pago extra : $%.2f" % (pagoE))
    print("------------------------------")
    print("Pago total : $%.2f" % (total))

#Llama a la funcion main (programa principal)
main()
