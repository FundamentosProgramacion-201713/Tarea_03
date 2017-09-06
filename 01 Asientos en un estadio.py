##encoding: UTF-8

# Autor: Edgar Alexis González Amador, A01746540
# Descripcion: Realizar un programa por medio de funciones que calcule el total a pagar por la compra de 3 tipos de boletos.



#Función que realiza la operación que determina el pago total que se realizara por la compra de los boletos
def calcularPago (asientosA, asientosB, asientosC):
    totalPago = (asientosA*400) + (asientosB*250) + (asientosC*135)
    return totalPago

#Main, función principal en la que se llama a las funciones anteriores y se piden e imprimen datos.
def main():
    numeroBoletosA = int(input("Numero de boletos de clase A: "))
    numeroBoletosB = int(input("Numero de boletos de clase B: "))
    numeroBoletosC = int(input("Numero de boletos de clase C: "))
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $ %.2f"%totalPago)

main()