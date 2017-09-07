#encoding: UTF-8
#Especificaciones del programa: Programa que Calcula cual es el rendimiento de la gasolina en cada litro y cuantos litros de gasolina gasta en determinados kilometros.
#Autor: Ernesto Ibhar Guevara Gomez
#Matricua: A01746121
def Leerkilometrosrecorridos():
    kilometrosrecorridos= float(input ("Teclea el numero de km recorridos: "))
    return kilometrosrecorridos
def Leergasolinautilizada():
    gasolinautilizada= float(input("Teclea el numero de litros: "))
    return gasolinautilizada
def Rendimientokm(kilometrosrecorridos, gasolinautilizada):
    rendimientokm= kilometrosrecorridos / gasolinautilizada
    return rendimientokm
def Rendimientoenmillas(rendimientokm):
    rendimientomil=(rendimientokm)/(0.264172051*1.609344)
    return rendimientomil
def Leerkilometrosporrecorrer():
    kilometrosporrecorrer=float(input("¿Cuantos kilometros vas a recorrer?"))
    return kilometrosporrecorrer
def Calcularlitros(gasolinautilizada,kilometrorecorridos,kilometrosporrecorrer):
    litros= (kilometrosporrecorrer * gasolinautilizada) / kilometrorecorridos
    return litros
def main():
    numerodekmrecorridos= Leerkilometrosrecorridos()
    numerodelitrosgasolinausados= Leergasolinautilizada()
    print("Si recorres ", numerodekmrecorridos,"km con",numerodelitrosgasolinausados,"litros de gasolina, el rendimiento es: ")
    rendimientoenkm= Rendimientokm(numerodekmrecorridos, numerodelitrosgasolinausados)
    print("%.2f"%rendimientoenkm,"km/l")
    rendimientoenmillas= Rendimientoenmillas(rendimientoenkm)
    print("%.2f"%rendimientoenmillas,"mi/gal")
    kilometrosporrecorrer= Leerkilometrosporrecorrer()
    calcularlitross= Calcularlitros(numerodelitrosgasolinausados,numerodekmrecorridos,kilometrosporrecorrer)
    print("Para recorrer",kilometrosporrecorrer,"km. necesitas %.2f"%calcularlitross,"litros de gasolina.")

main()
