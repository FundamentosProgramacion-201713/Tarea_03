#encoding: UTF-8
#Especificaciones del programa: Programa que Calcula el pago normal, pago extra y pago total de un trabajdor a la semana.
#Autor: Ernesto Ibhar Guevara Gomez
#Matricua: A01746121
def Leerhorasnormales():
    horasnormales=int(input("Teclea las horas normales trabajadas: "))
    return horasnormales
def Leerhorasextras():
    horasextras=int(input("Teclea las horas extras trabajadas: "))
    return horasextras
def LeerPagoporhora():
    pagohora=int(input("Teclea el pago por hora: "))
    return pagohora
def PorcentajePago(pagohora):
    porcentajepago=pagohora * (.50)
    return porcentajepago
def Pagonormal(horasnormales,pagohora):
    pagonormal=horasnormales * pagohora
    return pagonormal
def Pagoextra(horasextras,pagohora,porcentajepago):
    pagoextra= horasextras * (pagohora + porcentajepago)
    return pagoextra
def Totalsemana(pagoextra,pagonormal):
    totalsemana=pagoextra + pagonormal
    return totalsemana
def main():
    horasnormaless= Leerhorasnormales()
    horasextrass= Leerhorasextras()
    pagohoras= LeerPagoporhora()
    porcentajepagoo= PorcentajePago(pagohoras)
    pagonormall= Pagonormal(horasnormaless,pagohoras)
    pagoextras= Pagoextra(horasextrass,pagohoras,porcentajepagoo)
    totall= Totalsemana(pagonormall,pagoextras)
    print("Pago normal: %.2f"% pagonormall)
    print("Pago extra: %.2f"% pagoextras)

    print("Pago total: %.2f"% totall)
main()