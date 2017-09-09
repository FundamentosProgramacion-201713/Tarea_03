#Encoding: UTF-8
#Autor:Luis Daniel Rivera Salinas
#Matricula: A01374997
#Descripcion: dadas las horas trabajadas y las horas extra, calcular el total a pagar de horas trabajadas y horas extra, y la suma de ambos

def PagoNormal(horas,pago): #
    pagoNormalTotal = (horas*pago)
    return pagoNormalTotal

def PagoExtra(horasextra,pago):        # Se mete el pago * el numero de horas extra mas eso mismo *.5, que es el 50%extra que se gana
    pagoExtra = (horasextra*pago)+((horasextra*pago)*.5)
    return pagoExtra

def PagoTotal(horas,horasextra,pago):                   #la suma del pago de las horas normales mas las horas extras
    total = ((horas*pago)+(horasextra*pago)+((horasextra*pago)*.5))
    return total

def main():  #Ingresa las horas normales trabajadas, extra y el pago por hora, e imprime el pago por hora, pago por hora extra y la suma total de ambos pagos
    horas = float(input("Teclea las horas normales trabajadas: "))
    horasExtra = float(input("Teclea las horas extras trabajadas: "))
    pago = float(input("Teclea el pago por hora: "))
    normal = PagoNormal(horas,pago)
    print("Pago normal: $""%.2f"%normal)
    extra = PagoExtra(horasExtra,pago)
    print("Pago extra: $""%.2f"%extra)
    print("----------------------------")
    totalt = PagoTotal(horas,horasExtra,pago)
    print("Pago Total: $""%.2f"%totalt)

main()