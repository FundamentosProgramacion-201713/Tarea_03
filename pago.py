#encoding UTF-8
#Anaid Fernanda Labat González A01746289
#Descripción: Calcular el pago normal, extra y total de un trabajador

def horasN(horasT,pagoH):
    pagoN=horasT*pagoH
    return pagoN
def horasE (horasES, pagoHS, horasNS):
    pagoE=(horasES*pagoHS)+((pagoHS*.50)*horasES)
    return pagoE
def main():
    horasNS=int(input("Teclea las horas normales trabajadas:"))
    horasES=int(input("Teclea las horas extra trabajadas:"))
    pagoHS=int(input("Teclea el pago por hora:"))
    pagoNS=horasN(horasNS,pagoHS)
    print("Pago normal: $%.2f" % pagoNS)
    pagoE=horasE(horasES,pagoHS, horasNS)
    print ("Pago extra:$%.2f"% pagoE)
    print("-------------------------------")
    pagoT=pagoNS+pagoE
    print ("Pago total: $%.2f"% pagoT)

main()
