#Javier Pascal Flores A01375925

def main ():

    seatsA =int(input("Cuantos boletos clase A? "))
    seatsB =int(input("Cuantos boletos clase B? "))
    seatsC =int(input("Cuantos boletos clase C? "))

    print( "Numero de boletos de Clase A: ", seatsA)
    print("Numero de boletos de Clase B: ", seatsB)
    print("Numero de boletos de Clase C: ", seatsC)

    def calcularPago(seatsA, seatsB, seatsC):
            pagoA=seatsA*400
            pagoB=seatsB*250
            pagoC=seatsC*135
            total=pagoC+pagoB+pagoA
            return total

    print("Tu total a pagar es: ", calcularPago(seatsA, seatsB, seatsC))
main()

