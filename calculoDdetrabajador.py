#encoding: UTF-8

#Raul Ortiz Mateos A01375407
#El pago semanal de un trabajador se calcula multiplicando las horas normales trabajadas por la cantidad que se paga por
#hora. Las horas extras se pagan un 50% más que las normales.
#Escribe un programa que lea las horas normales, las horas extras y el pago por hora de un trabajador. Calcula e imprime
#los datos del trabajador incluyendo su pago semanal.
#Usa una función para calcular el pago normal y otra función para calcular el pago extra.

def CalcularPagoNormal(pagoPorHora, pagoHorasTrabajadas):#Calcular Pago normal multiplicacion
    pagoNormal = pagoPorHora * pagoHorasTrabajadas
    return pagoNormal

def calcularHorasExtra(pagoPorhora,HorasExtra):#Sumar y multiplicar
    pagoExtra= (pagoPorhora+25)*HorasExtra
    return pagoExtra

def CalcularTotal(pagoExtra,pagoNormal):#pago extra suma pago normal
    Total=pagoExtra+pagoNormal
    return Total


def main():
    ht=float(input("Teclea las horas trabajadas: "))
    he=float(input("teclea las horas extra: "))
    ph=float(input("teclea el pago por hora: "))
    print("Tu pago normal es de:%.2f"% CalcularPagoNormal(ph,ht))
    print("tu pago Extra es de:%.2f"% calcularHorasExtra(ph,he))
    print ("La suma total de tus horas trabajadas y las horas extra es de:%.2f"%CalcularTotal(calcularHorasExtra(ph,he),CalcularPagoNormal(ph,ht)))

main()




