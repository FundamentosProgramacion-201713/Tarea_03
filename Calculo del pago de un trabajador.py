# encoding:  UTF-8

# Autor: Jean Paul Esquivel Lobato     A01376152
# Descripción: Cálcular el pago de un trabajador



#Cálcular el pago por horas normales

def pagoNormal (horas, pago):
    normal = horas*pago
    return normal


#Cálcular el pago por horas extras

def pagoExtra (horas, pago):
    extra = horas *pago
    ex = extra * .50
    e = extra + ex
    return e


#Función principal

def main ():
    hN = int(input ("Teclea las horas normales trabajadas: "))
    hE = int(input("Teclea las horas extras trabajadas: "))
    paga = int(input("Teclea el pago por hora: "))
    pagoNor = pagoNormal(hN,paga)
    print ("Pago normal: $%.2f"% (pagoNor))
    pagoExt = pagoExtra(hE,paga)
    print("Pago extra: $%.2f" % (pagoExt))
    print ("----------------------")
    pagoTotal = pagoNor+pagoExt
    print("Pago Total: $%.2f" % (pagoTotal))


main()