#AUTOR: JOSÉ HEINZ MÖLLER SANTOS
#el programa calcula el rendimiento de un auto y luego te da la cantidad de gasolina que le debes de meter para recorrer cierta distancia

#calcula el rendimiento en km y litros
def calcularRendimientoKmLi(kmRecorridos, litrosGasolina):
    kmL = kmRecorridos / litrosGasolina
    return kmL

#calcula el rendimiento de millas por galon
def calcularRendimientoMiGal(kmRecorridos, litrosGasolina):
    millas = kmRecorridos * 0.6213
    galones = litrosGasolina * 0.2641
    miGal = millas / galones
    return miGal

#calcula los litros de gasoliina a utilizar en x cantidad de kilometros
def calcularGasolinaEnKm(kmARecorrer, kmLitro):
    litrosUsar = (kmARecorrer)/kmLitro
    return litrosUsar

#Es la función principal, lee los datos e imprime los resultados.
def main():
    kmRecorridos = int(input("Kilometros recorridos: "))
    litrosGasolina = int(input("Litros de gasolina usados: "))
    kmLitro = float(calcularRendimientoKmLi(kmRecorridos,litrosGasolina))
    milesGal = float(calcularRendimientoMiGal(kmRecorridos, litrosGasolina))

    print("  ")
    print("Si recorres %d kilometros con %d litros de gasolina, el rendimiento es:" %(kmRecorridos, litrosGasolina))
    print ("%.2f kilometros por litro"%kmLitro)
    print("%.2f millas por galon"%milesGal)
    print("   ")
    kmARecorrer = int(input("Cuantos km va a recorrer?: "))
    print("    ")
    gasolinaAUsar = float(calcularGasolinaEnKm(kmARecorrer, kmLitro))

    print("Para recorrer %d kilometros se necesitan %.2f litros de gasolina" %(kmARecorrer, gasolinaAUsar))

main()