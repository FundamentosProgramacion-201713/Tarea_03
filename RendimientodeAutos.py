#encoding UTF-8
#Autor: Leonardo Castillejos Vite
#Descripción: Un programa que lee los litros usados,los kilometros recorridos y lo kilometros a recorrer e imprime el
# rendimiento en km/l y mi/gal

def calcularRendimientoKm (kmRecorridos, litrosUsados):
    redimientoInter = kmRecorridos/litrosUsados
    return redimientoInter

def calcularRendimientoMil (kmRecorridos, litrosUsados):
    milRecorridos = kmRecorridos * 0.621371
    gallRecorridos = litrosUsados * 0.264
    rendimientoImp = milRecorridos/gallRecorridos
    return rendimientoImp

def calcularGasAUsar (kilometrosARecorrer, rendimientoInter):
    gasolinaUsada = kilometrosARecorrer / rendimientoInter
    return gasolinaUsada

def main():
    kmRe = int(input("Teclea el número de km recorridos: "))
    gasUsa = int(input("Teclea el número de litros de gasolina usados: "))
    print("")
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es:" % (kmRe, gasUsa))
    rendimientoInter = calcularRendimientoKm(kmRe, gasUsa )
    rendimientoImp = calcularRendimientoMil(kmRe, gasUsa)
    print("%.2f km/l" % (rendimientoInter))
    print("%.2f mi/gal" % (rendimientoImp))
    print("")
    kmARecorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))
    gasAUtilizar = calcularGasAUsar(kmARecorrer, rendimientoInter)
    print("")
    print("Para recorrer %d km. necesitas %.2f litros de gasolina" % (kmARecorrer, gasAUtilizar))




main()
