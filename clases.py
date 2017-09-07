#encoding: UTF-8
#Autor: Rodrigo Rivera Salinas A01375000
#Descripcion: Hay 3 localizaciones para poder comprar boletos cada una con su costo diferente, calcula el numero de boletos por area y el costo total

def numerodeboletosA(boletosA):    #agarra los boletosA dados por el usuario y los multilpica por el valor, despues de eso el valor se regresa a la funcion
    tboletosA=boletosA*400
    return tboletosA
def numerodeboletosB(boletosB):    #agarra los boletosB dados por el usuario y los multilpica por el valor, despues de eso el valor se regresa a la funcion
    tboletosB=boletosB*250
    return tboletosB
def numerodeboletosC(boletosC):    #agarra los boletosC dados por el usuario y los multilpica por el valor, despues de eso el valor se regresa a la funcion
    tboletosC=boletosC*135
    return tboletosC
def main():    #pide datos al usuario, imprime lo que se le pide y llama a las funciones para guardarlas en una variable
    boletosA = int(input("numero de boletos para A"))
    boletosB = int(input("numero de boletos para B"))
    boletosC = int(input("numero de boletos para C"))
    calcularpagototal=numerodeboletosA(boletosA)+numerodeboletosB(boletosB)+numerodeboletosC(boletosC)
    print("El costo total es: ",  calcularpagototal)
main()
