# encoding UTF-8
# Autor: Jaime Orlando López Ramos
# Descripción: Un programa que lea la cantidad de kilómetros que recorrido un auto y los litros que ha utilizado de
# gasolina, para poder calcular cuántos kilómetros rinde por litro, para posteriormente convertir dicha cantidad a
# millas/galón e imprimirlo. Después calcular cuántos litros de gasolina necesita el vehículo para recorrer "X" cantidad
# de kilómetros ingresados por el usuario e imprimir la cantidad de litros requeridos.


# Crear una función que calcule los kilómetros por litro que rinde un vehículo tomando como parámetros los
# kilómetros recorridos y los litros ultilizados. Para calcular, la función divide la candidad de kilómetros recorridos
# sobre los litros utilizados y regresa el valor calculado
def calcularKl(kR, lU):
    kL = kR / lU
    return kL


# Una función que calcule las millas por galón que recorre ese mismo vehículo tomando como parámetro los Km/l que rinde
# el auto. El cálculo se efectua multiplicando los km/l por 2.35 y al final regresa el valor calculado
def calcularMPG(kL):
    mPG = kL * 2.35
    return mPG



# Una función que calcule el número de litros que requiere el vehículo para recorrer cierta distancia. La funcion
# toma como parámetro la cantidad de km. que el usuario desea recorrer y los km/l que rinde el vehículo.
# Para el cálculo, la función divide los kilómetros que el usuario desea recorrer entre los Km/l que rinde el auto
# Al final regresa el valor calculado
def calcularLRequeridos(kM, kL):
    lRequeridos = kM / kL
    return lRequeridos



# Una funcíon main que lea los kilómetros que ha recorrido el auto y los litro utilizados para recorrerlos
# Llamar a las función Km/l y otorgarle una variable. Después llamar a la función que calcula las millas por galón,
# Usando la variable de la función anterior y darle una variable a esta también
# Luego de esto, leer la cantidad de kilómetros que el usuario desea recorrer
# y llamar a la función que calcula cuántos litros necesita y dándole una variable a esta.
# Finalmente, imprimir lo requrido.
def main():
    kR = int(input("Ingrese la cantidad de kilómetros que su auto ha recorrido: "))
    lU = int(input("Ingrese la cantidad de litros que su auto ha utilizado: "))
    kL = calcularKl(kR, lU)
    mPG = calcularMPG(kL)
    kM = int(input("Ingrese la cantidad de kilómetros que desea recorrer: "))
    lR = calcularLRequeridos(kM, kL)
    print("Si recorres %.2f km. con %d litros, el rendimiento es" % (kM, lU))
    print("%.2f km/l" % (kL))
    print("%.2f mpg" % (mPG))
    print("Para recorrer %d kilómetros, requieres %.2f litros" % (kM, lR))


main()