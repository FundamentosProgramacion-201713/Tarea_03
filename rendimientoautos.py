#Autor: Mónica Monserrat Palacios Rodríguez
#Rendimiento de Autos
#include<stdio.h>

def rendimientoKm(km,l):
    rendimientoKmTotal = (km/l) #Cálculo del rendimiento en kilómetros y litros
    return rendimientoKmTotal

def rendimientoMi(km,l):
    rendimientoMiTotal =((km/1.609344)/(l*0.264172051)) #Se convierten los kilómetros a millas y los litros a galones
    return rendimientoMiTotal

def litrosNecesarios(km, rendimientoKmTotal): #Se dividem los kilómetros entre el rendimiento y acalculado
    litrosTotales = (km/rendimientoKmTotal)
    return litrosTotales

def main():
    kilometros = int(input("Teclea el número de km recorridos: ", )) #Se pide al usuario que teclee los kilómetros
    litros = int(input("Teclea el número de litros de gasolina usados: ", )) #Se pide que teclee los litros
    rendimientoKmTotal = rendimientoKm(kilometros,litros) #Se llama a la función de rendimientoKm para hacer el cálculo con lo valores asignados
    rendimientoMiTotal = rendimientoMi(kilometros, litros) #Se llama a la función rendimientoMi para hacer el cálculo con lo valores asignados
    print(" ")
    print("Si recorres", kilometros, "kms con", litros, "litros de gasolina, el rendimiento es: ")
    print("{0:.2f}".format(rendimientoKmTotal),"km/l") #Se imprime el rendimiento en kilómetros/litros
    print("{0:.2f}".format(rendimientoMiTotal), "mi/gal") #Se imprime el rendimiento en millas/galones
    print(" ")

    kilometros2 = int(input("¿Cuántos kilómetros vas a recorrer? ", ))#Se pide al usuario los kilómetros que gustaría recorrer
    litrosTotales = litrosNecesarios(kilometros2, rendimientoKmTotal) #Se llama a la función litrosNecesarios con lo valores asignados
    print("Para recorrer", kilometros2, "km. necesitas", "{0:.2f}".format(litrosTotales), "de gasolina") #Se imprime el resutado de los litros totales calculados de acuerdo a los kilómetros asignados

main() #Se llama a la función main