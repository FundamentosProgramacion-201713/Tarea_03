#encode: UTF-8

#Autor: Natalia Meraz Tostado   A01745008
#Descripción: desarrollar un programa que imprima el rendimiento del auto en km/l, mi/gal y los litros de gasolina necesarios

milla = float(1.609344)
litro = float(0.264172051)

kmRecorridos = float(input("Teclea el número de km recorridos: "))
gasolina = float(input("Teclea el número de litros de gasolina usados: "))
kmRecorrer = float(input("¿Cuántos kilómetros vas a recorrer? "))

def kilometrosEntreLitros(kmRecorridos, gasolina):              #Calcula el rendimiento del auto en km/l
    kml = kmRecorridos / gasolina
    return kml

def millasEntreGalon(milla, litro, kml):                        #Calcula el rendimiento del auto en mi/gal
    migal = kml / (milla * litro)
    return migal

def kmPorRecorrer(kmRecorrer, gasolina, kmRecorridos):              #calcula la gasolina que va a necesitar para ciertos km
    litrosGas = (kmRecorrer * gasolina) / kmRecorridos
    return litrosGas

def main():
    kml = kilometrosEntreLitros(kmRecorridos, gasolina)
    migal = millasEntreGalon(milla, litro, kml)
    litrosGas = kmPorRecorrer(kmRecorrer, gasolina, kmRecorridos)
    print("")
    print("Si recorres",kmRecorridos, "kms con", gasolina, "litros de gasolina, el rendimiento es:")
    print("%.2f km/l" % kml)
    print("%.2f mi/gal" % migal)
    print("")
    print("Para recorrer", kmRecorrer, "km. necesitas %.2f litros de gasolina" %  litrosGas)

main()
