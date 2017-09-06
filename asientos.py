#ecoding:UTF-8
#Autor: Angel Ramírez Martínez
#Descripción: A partir del número de asientos de cada clase se calcula el total a pagar


# Calcula y regresa la variable totalPago que es el total a pagar a partir del número de asientos de cada
# clase que recibe como parámetro.
def calcularPago(asientosA, asientosB, asientosC):
    costoA = asientosA * 400
    costoB = asientosB * 250
    costoC = asientosC * 135
    totalPago = costoA + costoB + costoC
    return (totalPago)

# Esta función main llama a las funciones anteriores e imprime el total a pagar por los diferentes tipos de asientos.
def main():
    numeroBoletosA = int(input('Número de boletos de clase A: '))
    numeroBoletosB = int(input('Número de boletos de clase B: '))
    numeroBoletosC = int(input('Número de boletos de clase C: '))
    totalPago= calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)
    print('El costo total es: $%.2f' %(totalPago))


main()
