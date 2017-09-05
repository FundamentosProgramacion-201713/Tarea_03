#AUTOR: PEDRO CORTÉS SOBERANES A01371919
#FUNCIÓN: CALCULAR PAGOS DE UN TRABAJADOR


#Función: Sirve para calcular el pago por horas normales
def pagoN (horas, pago):
    nor = horas*pago
    return nor

#Función: Sirve para calcular el pago por horas extras
def pagoE (horas, pago):
    extra = horas *pago
    ex = extra * .50
    e = extra + ex
    return e

def main ():
    hN = int(input ("Teclea las horas normales trabajadas: "))
    hE = int(input("Teclea las horas extras trabajadas: "))
    paga = int(input("Teclea el pago por hora: "))
    pagoNOR = pagoN(hN,paga)
    print ("Pago normal: $%.2f"% (pagoNOR))
    pagoEXT = pagoE(hE,paga)
    print("Pago extra: $%.2f" % (pagoEXT))
    print ("----------------------")
    pagoT = pagoNOR+pagoEXT
    print("Pago Total: $%.2f" % (pagoT))


main()


