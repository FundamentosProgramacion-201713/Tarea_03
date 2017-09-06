#encoding: utf-8
#written by Jordan González Bustamante
#Este programa calcula el rendimiento de un automovil en km/L y mi/gal, además de calcular los litros necesarios para recorrer cierta cantidad ingresada por el usuario.

#La función calcula el rendimiento del carro según los datos ingresados, entrega el rendimiento en km/L y mi/gal
def calcularRendimiento(kmRecorridos, liUsados):
    global kmL
    kmL = kmRecorridos / liUsados
    kmRecorridos *= 0.621371
    liUsados *= 0.264172051
    miGal = kmRecorridos / liUsados
    return kmL, miGal

#Calcula el total de litros necesarios según el rendimiento de la función anterior
def calcularLitrosN(kmARecorrer):
    litN = kmARecorrer / kmL
    return litN

#Pedimos al usuario que ingrese los km requeridos, litros utilizados y, al llamar a la primera función y obtener
# el rendimiento, requerimos los km a recorrer, para mostrarle cuantos litros utilizará según su rendimiento.
def main():
    kmR = float(input("Teclea el número de km recorridos             : "))
    liU = float(input("Teclea el número de litros de gasolina usados : "))
    kmL, miGal = calcularRendimiento(kmR, liU)
    print("""Si recorres %.2f kms con %.2f litros de gasolina, el rendimiento es : 
    %.2f km/L
    %.2f mi/gal
    """ % (kmR, liU, kmL, miGal))
    kmAR = float(input("¿Cuántos kilómetros vas a recorrer? : "))
    litN = calcularLitrosN(kmAR)
    print("Para recorrer %.2f km, necesitas %.2f litros de gasolina" % (kmAR, litN))

main()
