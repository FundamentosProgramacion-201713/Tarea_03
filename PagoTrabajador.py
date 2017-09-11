#Autor: Gabriela Mariel Vargas Franco A01745775
#encoding: UTF-8
#Calcular el pago normal y el pago extra semanal de un trabajador.
def pagoNormal(hnormalesTrabajadas, pagoHora):
    #Calcula y guarda en la variable pagoNormal el pago semanal
    pagoNormal=(hnormalesTrabajadas*pagoHora)

    #Regresar totalPago
    return pagoNormal

def pagoExtra(pagoHora,hExtrasTrabajadas):
    #Calcula y guarda en la variable pagoExtra
    pagoExtra=(hExtrasTrabajadas*(pagoHora*1.5))
    return pagoExtra

def pagoTotal(hExtrasTrabajadas,pagoHora,hnormalesTrabajadas):
    pagoTotal=(hExtrasTrabajadas*(pagoHora*1.5))+(hnormalesTrabajadas*pagoHora)
    return pagoTotal
def main():
    hNormalesT=int(input("Teclea las horas normales trabajadas:"))
    hExtrasT=int(input("Teclea las horas extras trabajadas:"))
    pagoHr=int(input("Teclea el pago por hora:"))
    pN=pagoNormal(hNormalesT,pagoHr)
    print("Pago normal:$",format(pN,".2f"))
    pE=pagoExtra(hExtrasT,pagoHr)
    print("Pago extra:$",format(pE,".2f"))
    pT=pagoTotal(hExtrasT,pagoHr,hNormalesT)
    print("Pago total:$",format(pT,".2f"))


main()



