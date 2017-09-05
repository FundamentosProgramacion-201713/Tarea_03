#AUTOR: PEDRO CORTÉS SOBERANES A01371919
#FUNCIÓN: CALCULAR CUANTO DEBE PAGAR EL USUARIO POR SUS ASIENTOS

#Función: Sirve para calcular el precio total de los asientos
def calcularPago (asientosA, asientosB, asientosC ):
    aA = asientosA*400
    aB = asientosB*250
    aC = asientosC*135
    total= aA+aB+aC
    return total

def main():
    asA = int(input("¿Cuantos asientos clase A quieres comprar? "))
    asB = int(input("¿Cuantos asientos clase B quieres comprar? "))
    asC = int(input("¿Cuantos asientos clase C quieres comprar? "))
    costoTotal = calcularPago(asA,asB,asC)
    print("Número de boletos de clase A: ", asA)
    print("Número de boletos de clase B: ", asB)
    print("Número de boletos de clase c: ", asC)
    print("El costo total es: $",costoTotal)

main()