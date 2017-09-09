#Encoding: UTF-8
#Autor:Luis Daniel Rivera Salinas
#Matricula: A01374997
#Descripcion: calcula cuantos asientos de diferntes precios van a comprar, imprime el numero de cada asiento y la suma del gasto total

def CuantosBoletosA(boletosA): #Multiplica el precio de los boletos A por el numero de boletos a comprar, regresa el costo a la funcion
    totalBoletosA = boletosA*400
    return totalBoletosA

def CuantosBoletosB(boletosB): #Multiplica el precio de los Boletos B por el numero de boletos a comprar, regresa el costo a la funcion
    totalBoletosB = boletosB*250
    return totalBoletosB

def CuantosBoletosC(boletosC): #Multiplica el precio de los Boletos C por el numero de boletos a comprar, regresa el costo a la funcion
    totalBoletosC = boletosC*135
    return totalBoletosC

def main():  #Ingresa el numero de cada tipo de boletos e imprime el precio total de los boletos
    boletosA = int(input("Número de boletos para A: "))
    boletosB = int(input("Número de boletos para B: "))
    boletosC = int(input("Número de boletos para C: "))
    calcularpagototal=CuantosBoletosA(boletosA)+CuantosBoletosB(boletosB)+CuantosBoletosC(boletosC)
    print("El costo total es: $", "%.2f"%calcularpagototal)

main()
