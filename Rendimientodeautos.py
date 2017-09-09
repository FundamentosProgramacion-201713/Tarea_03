#Encoding: UTF-8

#Autor: Alberto López Reyes
'''Descripción: Este programa calcula e imprime el rendimiento de un auto en km/l, mi/l, y la cantidad de litros necesarios
al ser otorgado los km recorridos, los litros usados, y los km a recorrer.'''

    #Se declaran las constantes universales, porque nunca deberían cambiar, de la conversión de litros a galones y
    #km a millas.
fltLiTOGa = .264172051
fltKmTOMi = (1/1.609344)

    #Esta función calcula el rendimiento del auto en km/l al recibir los km recorridos y litros usados.
def calcularRendimientoKmL(fltKmRecorridos, fltLitrosUsados):
    fltRendimientoKmL = fltKmRecorridos / fltLitrosUsados
    return fltRendimientoKmL

    #Esta función calcula el rendimiento del auto en mi/l al recibir y multiplicar por sus conversiones respectivamente
    #los km recorridos y litros usados.
def calcularRendimientoMiL(fltKmRecorridos, fltLitrosUsados):
    global fltLiTOGa, fltKmTOMi
    fltRendimientoMiL = (fltKmRecorridos * fltKmTOMi) / (fltLitrosUsados * fltLiTOGa)
    return fltRendimientoMiL

    #Esta función calcula los litros que se deben usar para recorrer los km a recorrer recibiendo esta cantidad junto
    #los km recorridos y los litros usados previamente.
def calcularKilometrosARecorrer(fltKmRecorridos, fltLitrosUsados, fltKmRecorrer):
    fltLiARecorrer = fltKmRecorrer * fltLitrosUsados / fltKmRecorridos
    return fltLiARecorrer

    #Esta función principal recibe los km recorridos, litros usados, y km a recorrer de un auto para otorgárselos a las
    #funciones "calcularRendimientoKmL", "calcularRendimientoMiL", y "calcularKilometrosARecorrer". Estas tres funciones
    #devolverán el rendimiento en km/l, el rendimiento en mi/l, y los litros que se necesitan respectivamente. Estas tres
    #magnitudes después serán impresas.
def main():
    strKmRecorridos = input("Teclea el número de km recorridos: ")
    fltKmRecorridos = float(strKmRecorridos)
    strLitrosUsados = input("Teclea el número de litros de gasolina usados: ")
    fltLitrosUsados = float(strLitrosUsados)

    fltRendimientoKmL = calcularRendimientoKmL(fltKmRecorridos, fltLitrosUsados)
    fltRendimientoMiL = calcularRendimientoMiL(fltKmRecorridos, fltLitrosUsados)

    print("""""")
    print("Si recorres "+strKmRecorridos+" kms con "+strLitrosUsados+" litros de gasolina, el redimiento es: ")
    print(format(fltRendimientoKmL, '.2f')+" km/l")
    print(format(fltRendimientoMiL, '.2f')+" mi/gal")

    print("""""")
    strKmRecorrer = input("¿Cuántos kilómetros vas a recorrer? ")
    fltKmRecorrer = float(strKmRecorrer)

    fltLiARecorrer = calcularKilometrosARecorrer(fltKmRecorridos, fltLitrosUsados, fltKmRecorrer)

    print("""""")
    print("Para recorrer "+strKmRecorrer+" km. necesitas "+format(fltLiARecorrer, '.2f')+" litros de gasolina")

#Se acciona la función "main".
main()
