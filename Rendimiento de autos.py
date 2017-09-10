#enconding: UTF-8
#Alejandro Chávez Campos, A01374974
#Este programa es para calcular el rendimiento del automóvil expresado en kilómetros/litro, y en millas/galón. También para expresar los litros de gasolina necesitados para recorrer una determinada cantidad de kilómetros.
def calcularRendimientoKms(kmRecorridos, litrosUsados): #Calcula el rendimiento de kms/lts.
    rendimientoKmsLts = kmRecorridos/litrosUsados
    return rendimientoKmsLts


def calcularRendimientoMiGal(kmRecorridos, litrosUsados): #Convierte el rendimiento de km/lts a mi/gal.
    rendimientoMiGal=(kmRecorridos/1.609344)/(litrosUsados*0.264172051)
    return rendimientoMiGal


def calcularLitrosNecesitados(rendimientoKmsLts, kmsPorRecorrer): #Calcula los litros necesitados en base al rendimiento.
    litrosRendimiento= kmsPorRecorrer/rendimientoKmsLts
    return litrosRendimiento


def main(): #Programa principal
    strKmRecorridos =input("Teclea el número de km recorridos: ")
    strLitrosUsados =input("Teclea el número de litros usados: ")
    print ()
    print ("Si recorres", strKmRecorridos, "kms con", strLitrosUsados,"litros de gasolina, el rendimiento es:")
    kmRecorridos=float(strKmRecorridos)
    litrosUsados=float(strLitrosUsados)
    rendimientoKmsLts=calcularRendimientoKms(kmRecorridos, litrosUsados)
    rendimientoMiGal=calcularRendimientoMiGal(kmRecorridos, litrosUsados)
    print ("%.2f km/l"%rendimientoKmsLts)
    print("%.2f mi/gal"%rendimientoMiGal)
    print ()
    strKmsPorRecorrer=input ("¿Cuántos kilómetros vas a recorrer? ")
    kmsPorRecorrer=float(strKmsPorRecorrer)
    litrosNecesitados= calcularLitrosNecesitados(rendimientoKmsLts,kmsPorRecorrer)
    print ()
    print ("Para recorrer {} km. necesitas {:.2f} litros de gasolina".format(strKmsPorRecorrer,litrosNecesitados))
main()
