#Javier Pascal Flores A01375925

def main (): #Funcion main
#Inputs
    seatsA =int(input("Cuantos boletos clase A? "))
    seatsB =int(input("Cuantos boletos clase B? "))
    seatsC =int(input("Cuantos boletos clase C? "))
#Prints

    def calcularPago(seatsA, seatsB, seatsC): #Funcion de calcular pago
            pagoA=seatsA*400
            pagoB=seatsB*250
            pagoC=seatsC*135
            total=float(pagoC+pagoB+pagoA)
            return total #regresar el total


    print("Tu total a pagar es: $ %d.00 " % calcularPago(seatsA, seatsB, seatsC)) #Imprimir el total de pago

main()


