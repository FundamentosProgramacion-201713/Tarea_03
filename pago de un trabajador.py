#Yerish Valdes Bernes A01375755
#pago de trabajador
def calculo_regular(salario,horasR):
    pagoR=salario*horasR
    return pagoR

def calculo_extra(salario,horasE):
    pagoE=salario*1.5*horasE
    return pagoE

def calculo_total(horasR,horasE):
    pagoT=horasR+horasE
    return pagoT

def main():
    pago=float(input("Pago por hora:"))
    regular = float(input("Numero de horas regulares:"))
    extra = float(input("Numero de horas extras:"))
    pago_regular=calculo_regular(pago,regular)
    pago_extra=calculo_extra(pago,extra)
    pago_total=calculo_total(pago_regular,pago_extra)
    print("\nPago por horas regulares:%.2f\nPago por horas extra:%.2f\nPago total:%.2f"%(pago_regular,pago_extra,pago_total))
main()