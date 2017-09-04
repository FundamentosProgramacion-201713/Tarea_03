#encoding: UTF-8
#Autor: Omar Israel Galván García A01745810
#Este programa pregunta al usuario cuantos boletos quiere comprar de cada tipo e imprime el total a pagar.

def calcularPago(asientosA, asientosB, asientosC):  # esta funcion toma los valores de A,B,C y los multiplica por el costo
    totalPago = (asientosA * 400) + (asientosB * 250) + (asientosC * 135)

    return totalPago

def main():    # la funcion main lee los datos e imprime los resultados
    numeroBoletosA = int(input("Número de boletos de clase A: "))
    numeroBoletosB = int(input("Número de boletos de clase B: "))
    numeroBoletosC = int(input("Número de boletos de clase C: "))
    total =  calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)
    print("El costo total es: $%.2f"%(total))


main()  # se ejecuta la funcion main