# encode UFT-8
# Autor: Luis Enrique Neri Pérez
# Programa que permita determinar el rendimiento de la gasolina en km/l y mi/gal con la informació que el ususario ingrese: además determine cuantos litros necesitará el usuario para su próximo viaje

def rendimientoKm(kilometros, litros): #Esta función calcula el rendimiento en Km/L
    rendimientoKmL = kilometros / litros
    return rendimientoKmL

def rendimientoMi(kilometros, litros): #Esta función calula el rendimiento en Mi/Gal
    millas = kilometros / 1.609344
    galones = 	0.264172051 * litros
    rendimientoMiGal = millas / galones
    return rendimientoMiGal

def litrosNecesitados(rendimientoKms, kilometros2): #Esa función calcula cuantos litros necesitará, en relación al rendimiento de su vehículo, para recorrer la cantidad que el usuario indica
    litrosNec = kilometros2 / rendimientoKms
    return litrosNec

def main (): #Esta función lee los kilometros y litros que un vehículo utiliza, llama a las funciones rendimientoKms y rendimientoMis y posterirmente lee los kilometros que el usuario recorerá para indicarle cuantos kilometros utilizará
    kilometros = float(input("Ingrese el número de Kilometros recorridos: "))
    litros = float(input("Ingrese el número de litros de gasolina usados: "))
    rendimientoKms = rendimientoKm(kilometros, litros)
    rendimientoMis = rendimientoMi(kilometros, litros)
    print("")
    print("Si recorres %.2f kilómetros y utilizas %.2f litros, el rendimiento de tu vehículo es: " % (kilometros, litros))
    print("%.2f Km/L" % (rendimientoKms))
    print("%.2f Mi/Gal" % (rendimientoMis))
    print("")
    kilometros2 = float(input("¿Cuántos kilómetros recorerás en tu próximo viaje?: "))
    litrosNece = litrosNecesitados(rendimientoKms, kilometros2)
    print("Si recorrerás %.2f kilómetros necesitas %.2f litros de gasolina" % (kilometros2, litrosNece))


main()