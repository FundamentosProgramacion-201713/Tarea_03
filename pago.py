#encode:UTC-8
#Autor: José Antonio Gómez Mora
#Lee horas normales, horas extra y pago por hora e imprime pago semanal y datos.

#calcula el pago de las horas normales trabajadas con los parametros de horas normales y pago
def calculoNormales(hNormales,pago):
    normales=hNormales*pago
    return normales

#calcula el pago de horas extras trabajadas con los parametros de horas extras trabajadas y pago
def calculoExtra(hExtras, pago):
    extras=hExtras*(pago*1.5)
    return extras

#función main
def main():
    hNormales=int(input("Ingresa las horas normales trabajadas: "))
    hExtras=int(input("Ingresa las horas extras trabajadas: "))
    pago=int(input("Ingresa el pago por hora: "))

    pagoNormales=calculoNormales(hNormales,pago)
    pagoExtras=calculoExtra(hExtras,pago)
    total=pagoNormales+pagoExtras

    print("Pago normal:","$%d"%(pagoNormales))
    print("Pago extra:","$%d"%(pagoExtras))
    print("Pago total:","$%d"%(total))

main()
