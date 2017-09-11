#Autor: Gabriela Mariel Vargas Franco A01745775
#encoding: UTF-8
#Calcula e imprime el costo total y el número de boletos seleccionados para cada clase
def calcularPago(asientosA, asientosB, asientosC):
    #Calcula y guarda en la variable totalPago el total a pagar
    totalPago=(asientosA*400)+(asientosB*250)+(asientosC*135)

    #Regresar totalPago
    return totalPago

def main():
    numeroBoletosA=int(input("Número de boletos clase A:"))
    numeroBoletosB=int(input("Número de boletos clase B:"))
    numeroBoletosC=int(input("Número de boletos clase C:"))
    tP=calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es:$",format(tP,".2f"))



main()


