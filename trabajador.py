#encoding: UTF-8
#Autor: Rodrigo Rivera Salinas A01375000
#Descripcion: Calcular el pago de las horas normales de un trabajador mas el pago por las horas extras

def PagoNormal(horas,pago):   # Se pone en la formula los datos dados por el usuario de horas*pago para saber cuanto va a ganar el trabajador normalmente y se regresa en el pagonorma
    pagonorma=(horas*pago)
    return pagonorma
def PagoExtra(horasextra,pago):        # Se mete el pago * el numero de horas extra mas eso mismo *.5, que es el 50%extra que se gana
    pagoextra=(horasextra*pago)+((horasextra*pago)*.5)
    return pagoextra
def PagoTotal(horas,horasextra,pago):                   #la suma del pago de las horas normales mas las horas extras
    total=((horas*pago)+(horasextra*pago)+((horasextra*pago)*.5))
    return total
def main():   #pide datos al usuario, imprime lo que se le pide y llama a las funciones para guardarlas en una variable
    horas = float(input("dar las horas normales trabajadas: "))
    horasext = float(input("dar  las horas extras trabajadas "))
    pagos = float(input("dar el pago por hora: "))
    normal=PagoNormal(horas,pagos)
    print("Pago normal: $",normal)
    extra=PagoExtra(horasext,pagos)
    print("Pago extra: $",extra)
    print("----------------------------")
    totalt=PagoTotal(horas,horasext,pagos)
    print("Pago Total: $",totalt)
main()
