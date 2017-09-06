#encoding:UTF-8
#Autor: Carlos Pano Hernández

#Descripción: Este programa calcula el rendimiento de tu coche, así como la gasolina necesaria para recorrer cierta cantidad de Km. El programa da dos equivalencias del rendimiento.


def calcularRendimientoKM(kmR,lU):
    rendimiento=kmR/lU
    return rendimiento

def calcularRendimientoMI(kmR,lU):
    rendimiento=((kmR/lU)/1.609344)*(1/0.264172051)
    return rendimiento

def calcularLitrosNecesarios(kmPR,kmR,lU):
    litrosNecesarios=(kmPR*lU)/kmR
    return litrosNecesarios


def main():
    kmRecorridos=int(input("Teclea el número de km recorridos:"))
    litrosUsados=int(input("Teclea el número de litos de gasolina usados:"))

    print("")
    print("Si recorres %d kms con %d litos de gasolina, el rendimiento es:"%(kmRecorridos,litrosUsados))

    rendimientoKM=calcularRendimientoKM(kmRecorridos,litrosUsados)
    print ("%.2f km/l"%(rendimientoKM))

    rendimientoMI=calcularRendimientoMI(kmRecorridos,litrosUsados)
    print("%.2f mi/Gal"%(rendimientoMI))

    print("")
    kmPorRecorrer=float(input("¿Cuántos kilómetros vas a recorrer?"))
    print("")
    gasolinaNecesaria=calcularLitrosNecesarios(kmPorRecorrer,kmRecorridos,litrosUsados)
    print("Para recorrer %d km. necesitas %.2f litros de gasolina"%(kmPorRecorrer,gasolinaNecesaria))

main()

