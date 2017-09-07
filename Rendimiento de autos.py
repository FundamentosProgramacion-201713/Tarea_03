# UFT-8
#Autor: Javier León Alcántara
# Muestra el rendimiento de un automovil y calcula los litros de gasolina para viajar

def calcularRendimiento (km,lt):    #Calcula el rendimiento
     rendimiento= km/lt
     return rendimiento


def calcularRendimientoMiGal (km,lt):    #Calcula el rendimiento en millas/ galones
     mi = km/1.609344
     gal = lt * 0.264172051
     rendimientoMiGal = mi/gal
     return rendimientoMiGal


def CalcularLitros(kmRecorrer,rendimiento):  #Calcula los litros necesarios
     lt= kmRecorrer/rendimiento
     return lt


def main():                    #Pide los datos, calcula con las funciones e imprime el resultado
     km = float(input("Teclea el número de kilómetros recorridos : "))
     lt = float(input("Teclea el número de litros de gasolina usados : "))

     rendimiento = calcularRendimiento (km,lt)
     rendimientoMiGal= calcularRendimientoMiGal(km,lt)

     print("")
     print ("Si recorres %.2f kms con %.2f litros de gasolina el rendimiento es:" %(km,lt))
     print ("%.2f km/l"%(rendimiento))
     print ("%.2f mi/gal" %rendimientoMiGal)
     print ("")

     kmRecorrer = float(input("¿Cuántos kilómetros vas a recorrer?: "))

     litros = CalcularLitros (kmRecorrer,rendimiento)

     print ("Para recorrer %.2f km. necesitas %.2f litros de gasolina" %(kmRecorrer,litros))

main()