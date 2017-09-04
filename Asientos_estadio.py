#Autor: Maria Fernanda Torres Velazquez A01746537
#El siguiente programa, pregunta al usuario la cantidad de cada tipo de boletos para el acceso a un estadio de futbol y regresa el total a pagar

#Funcion que recibe como parametros la cantidad de asientos de cada tipo y regresa el total a pagar.
def calcularPago (asientosA, asientosB, asientosC):
    a= asientosA*400
    b= asientosB*250
    c= asientosC*135
    totalPago= a+b+c
    return totalPago

#Funcion principal en la que se introducen la cantidad de boletos para cada tipo de asiento y los envia a la funcion calcularPago,
# para que esta regrese el total a pagar y se imprima el resultado.

def main ():
    a = int (input("Numero de boletos clase A: "))
    b = int (input("Numero de boletos clase B: "))
    c = int (input("Numero de boletos clase C: "))
    total= calcularPago (a,b,c)
    print ("El total a pagar es: $%.2f" %(total))


#Llamar a la funcion main (programa principal)

main()

