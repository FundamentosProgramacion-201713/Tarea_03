#encoding: UTF-8

#Autor: Roberto Téllez Perezyera
"""
Este programa calcula y muestra al usuario (trabajador) su pago por horas normales trabajadas, pago por horas extra
trabajadas y el total de ambos.
"""


#Se calcula el pago por horas normales trabajadas.
def calcularPagoNormal (normalH, pagoHr) :
    pNormal = (normalH * pagoHr)
    return pNormal


#Se calcula el pago por horas extra trabajadas.
def calcularPagoExtra (extraH, pagoHr) :
    extraHours = (pagoHr + (pagoHr * 0.5))
    pExtra = (extraH * extraHours)
    return pExtra


#Se calcula el gran total al que el empleado es acreedor, en función de las horas normales y extra trabajadas;
# así como el pago por hora de cada una.
def calcularPagoTotal (pagoNormal, pagoExtra) :
    pTotal = pagoNormal + pagoExtra
    return pTotal


def main() :
    normalH = int(input("Teclea las horas normales trabajadas: "))
    extraH = int(input("Teclea las horas extra trabajadas: "))
    pagoHr = float(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal (normalH, pagoHr)
    pagoExtra = calcularPagoExtra (extraH, pagoHr)
    pagoTotal = calcularPagoTotal (pagoNormal, pagoExtra)
    print("Pago normal: $", "%.2f" % (pagoNormal))
    print("Pago extra: $", "%.2f" % (pagoExtra))
    print("-----------------------")
    print("Pago total: $", "%.2f" % (pagoTotal))


#Llamamos a main para que imprima las instrucciones, capture los datos, haga cálculos A TRAVÉS DE LAS FUNCIONES e
#imprima los resultados
main()
