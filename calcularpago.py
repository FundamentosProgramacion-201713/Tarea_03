#Autor: Mónica Monserrat Palacios Rodríguez
# Calcular Pago

def calcularPago (asientosA, asientosB, asientosC):
    totalPago=((asientosA*400)+(asientosB*250)+(asientosC*135)) #Multiplicación de número de boletos por su precio respectivo
    return totalPago #Se obtiene el valor de la suma

def main():
    numeroBoletosA = int(input("Número de boletos de clase A: ", )) #Se pide al usuario que introduzca el número de boletos por zona
    numeroBoletosB = int(input("Número de boletos de clase B: ", ))
    numeroBoletosC = int(input("Número de boletos de clase C: ", ))
    totalPago = calcularPago (numeroBoletosA, numeroBoletosB, numeroBoletosC) #Se llama a la función para que se realice el procedimiento
    print("El costo total es: $","{0:.2f}".format(totalPago)) #Se imprimer el resultado al usuario


main() #Se llama a la función main para ejecutar el programa
