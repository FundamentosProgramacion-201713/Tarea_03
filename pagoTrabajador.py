#gbt-8
# autor: viviana Osorio Nieto
def calcularPagoN (hn, C):
    #el pago por hora se especifica con costo en main
    pagoN = hn * C
    return pagoN

def calcularPagoE (he ,C):
    #el pago por hora extra es 50% mas por lo que multiplique por 1.5 el costo por hora normal
    pagoE = he *(1.5*C)
    return pagoE

def calcularTotal (pagoNormal, pagoExtra):
    #el total es la suma de los pagos
    total = pagoExtra + pagoNormal
    return total

def main():
    # para leer los datos
    strH = input("cuantas horas normales trabajaste?: ")
    # para guardas los datos:
    hn = int(strH)

    # para leer los datos
    strE = input("cuantas horas extra trabajaste?: ")
    # para guardas los datos:
    he = int(strE)

    # para leer los datos
    strC = input("cual es el pago por hora?: ")
    # para guardas los datos:
    C = int(strC)
#llamar e imprimit todos las funciones, resultados.
    pagoNormal = calcularPagoN(hn,C)
    print ("total pago normal:" ,pagoNormal)
    pagoExtra = calcularPagoE (he, C)
    print ("total pago extra: ", pagoExtra)
    pagoTotal = calcularTotal (pagoNormal,pagoExtra)
    print ("el total es: ",pagoTotal)
#llamar a main
main()