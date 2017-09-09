#encoding: UTF-8
#Autor: Eduardo Roberto Müller Romero, A01745219
#Escribe un programa que lea los kilometros recorridos y la gasolina, después pregunta los kilometros que recorrerá y calcula la gasolina que necesitará

def main():
    km = int(input("Km recorridos: "))
    gas = int(input("Gasolina usada: "))
    rendimientoenkm = calcularrendimiento(km, gas)
    rendimientoenmi = calcularrendimiento1(km, gas)
    print("Si recorres", km, "km con", gas, "el rendimiento es: ")
    print("%.2f" %rendimientoenkm, "km/l")
    print("%.2f" %rendimientoenmi, "mi/gal")
    kilometrosarecorrer = int(input("Kilometros que se van a recorrer: "))
    futurorendimiento = calcularlonecesario(kilometrosarecorrer, rendimientoenkm)
    print("para recorrer", kilometrosarecorrer, "se necesitarán: ", "%.2f" %futurorendimiento, "litros de gasolina")

#calcula el rendimiento en km/l
def calcularrendimiento(km, gas):
    rendimiento = km / gas
    return rendimiento

#convierte km en mi y calcula el rendimiento
def calcularrendimiento1(km, gas):
    mi = km * 1.609344
    rendimiento = mi / gas
    return  rendimiento

#calcula los litros que se necesitarán, para n numero de km
def calcularlonecesario(kilometrosarecorrer, rendimientoenkm):
    rendimiento = rendimientoenkm
    necesita = kilometrosarecorrer / rendimiento
    return necesita

main()
