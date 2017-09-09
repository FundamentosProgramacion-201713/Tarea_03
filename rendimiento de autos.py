#Encoding: UTF-8
#Autor:Luis Daniel Rivera Salinas
#Matricula: A01374997
#Descripcion:

def rendimiento1(km,litros):  #Calcula el rendimiento de kilometros entre litros
    rendimiento = km/litros
    return rendimiento

def rendimiento2(km,litros):  #Calcula el rendimiento de millas entre galones
    rendimientoB = ((km/1.609344)/(litros*0.264172051))
    return rendimientoB

def litrosrequeridos(kmrecorridos,litros,km):  #Calcula en base a los kilometros a recorrer, los litros requeridos
    litrosrequeridos1 = (kmrecorridos*litros)/km
    return litrosrequeridos1

def main(): #Ingresa el numero de kilometros recorridos y litros utilizados utilizados, e imprime el rendimiento en km/litros y mi/gal,
    km = int(input("Teclea el número de km recorridos: "))
    litros = int(input("Teclea el número de litros de gasolina utilizados: "))
    print("    ")
    print("Si recorres ",km, "kms con ", litros, "litros de gasolina, el rendimiento es: ")
    print("%.2f"%rendimiento1(km,litros), "km/l")
    print("%.2f"%rendimiento2(km,litros), "mi/gal")
    print("    ")
    kmrecorridos = int(input("¿Cuántos kilómetros vas a recorrer? "))
    print("Para recorrer", kmrecorridos, "km. necesitas ", "%.2f"%litrosrequeridos(kmrecorridos,litros,km), "litros de gasolina")

main()
