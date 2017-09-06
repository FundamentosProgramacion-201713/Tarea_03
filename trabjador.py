#encoding: UTF-8
#Autor: Angel Roberto Pesado Bartolo
#Elaboración de un programa que calcule el dinero que gana un trabajador a partir de las horas y el pago que indique el usuario, además
#calcular el bono que que gana por horas extras que trabaja.

def calcularPagoNormal(horas,pago): #definimos la función calcularPagoNormal
    pagon=(horas*pago) #Obtenemos el pago normal a partir de las horas y el pago que nos indique el usuario
    return pagon #regresamos pago normal
def calcularPagoExtra(horase,pago): #definimos la función calcularPagoExtra
    pagoe=(horase*pago)+((horase*pago)*.5) #obtenemos el pago extra a partir de las horas extras y pago que nos indique el usuario
    return pagoe #regresamos pago extra
def calcularPagoTotal(horas,horase,pago): #definimos la función calcularPagoTotal
    total=((horas*pago)+(horase*pago)+((horase*pago)*.5)) #Obtenemos la suma del pago normal y el pago pago extra
    return total #regresamos total
def main():
    horast= float(input("Ingresa las horas normales trabajadas: ")) #Pedimos al usuario las horas trabajadas
    horastx = float(input("Ingresa las horas extras trabajadas ")) #Pedimos al usuario las horas extras trabajadas
    pagos = float(input("Ingresa el pago por hora: ")) #Pedimos al usuario cual será el pago
    pagono=calcularPagoNormal(horast,pagos)  #Mandamos los datos ingresados por el usuario a la función calularPagoNormal para obtener el pago normal del trabajador
    print("Pago normal: $",pagono)#Imprimimos pago normal
    pagoex=calcularPagoExtra(horastx,pagos) #Mandamos los datos ingresados por el usuario a la función calularPagoExtra para obtener el pago extra del trabajador
    print("Pago extra: $",pagoex) #imprimimos pago extra
    totalt=calcularPagoTotal(horast,horastx,pagos)#Mandamos los datos ingresados por el usuario a la función calularPagoTotal para obtener el pago total del trabajador
    print("Pago Total: $",totalt) #imprimimos pago total

main() #llamamos a la función main para que se ejecute lo que esta dentro de ella.
