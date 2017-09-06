#encoding: UTF-8
#Autor: Angel Roberto Pesado Bartolo
#Elaboración de un programa que reciba los boletos de diferentes clases e imprimar el costo total por lo boletos recibidos.
def calcularPago(asientosa, asientosb, asientosc):  #Definimos la función calcularPago
    total= (asientosa*400)+(asientosb*250)+(asientosc*135) #dentro de la función hacemos la operación para calcular el total por cada clase y después se suman todas las clases
    return total #regresamos a la función el total
def main(): #Definimos la función main
    clasea= int(input("Numero de boletos de clase A: ")) #Pedimos al usuario los boletos de la clase a
    claseb = int(input("Numero de boletos de clase B: ")) #Pedimos al usuario los boletos de la clase b
    clasec = int(input("Numero de boletos de clase C: ")) #Pedimos al usuario los boletos de la clase c
    total= calcularPago(clasea,claseb,clasec) #Mandamos los datos ingresados por el usuario a la función calulcarPago para obtener el total
    print("El total a pagar es:$", total) #imprimir el total a pagar

main() #llamamos a la función main para que se ejecute lo que esta dentro de ella.
