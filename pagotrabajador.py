#Autor: Mónica Monserrat Palacios Rodríguez
# Cálculo del pago de un trabajdor
#include<stdio.h>

def pagoNormal(horasN, pagoH):
    pagoNormalTotal = (horasN * pagoH) #Se multiplica el número de horas trabajadas por el pago
    return (pagoNormalTotal)

def pagoExtra(horasE, pagoH):
    pagoExraTotal = (horasE * pagoH) #Se multiplica el número de horas extra trabajadas por el pago
    pagoExraTotal = (pagoExraTotal/2)+pagoExraTotal #Se divide el pagoExtraTotal entre dos y se suma al último valor guardado
    return (pagoExraTotal)

def main():
    hN = int(input("Teclea las horas normales trabajadas: ", )) #Se pide al usuario que teclee las horas normales trabajadas
    hE = int(input("Teclea las horas extras trabajadas: ", )) #Se pide al usuario que teclee las horas extras trabajadas
    pH = int(input("Teclea el pago por hora: ", )) #Se pide al usuario que teclee el pago por hora
    pagoNormalTotal = pagoNormal(hN,pH) #Se llama a la función para calcular el pago por las horas normales
    pagoExtraTotal = pagoExtra(hE, pH) #Se llama a la función para calcular el pago por las horas extras
    print(" ")
    print("Pago normal: $","{0:.2f}".format(pagoNormalTotal)) #Se imprime el pago por horas normales
    print("Pago extra: $", "{0:.2f}".format(pagoExtraTotal)) #Se imprime el pago por horas extras
    print("----------------------------")
    print("Pago total: $","{0:.2f}".format((pagoNormalTotal+pagoExtraTotal))) #Se imprime el pago total, es decir, la suma de ambos resultados

main() #Se llama a la función main