#Debido al aumento de la gasolina, los automovilistas están preocupados por el rendimiento de su auto. Los datos que
#tienen es el número de kilómetros que recorrieron y la cantidad de litros de gasolina que utilizaron.
#Escribe un programa que lea el número de kilómetros recorridos y la cantidad de gasolina utilizada, y que imprima lo
#siguiente:
#1) El rendimiento del automóvil en:
#a. kilómetros/litro.
#b. millas/galón. (1 milla = 1.609344 kilómetros, 1 litro = 0.264172051 galones)
#2) Después, el programa pregunta cuántos kilómetros va a viajar e imprime los litros de gasolina que necesitará.
#Debes usar funciones. Utiliza tantas como sean necesarias de acuerdo a tu diseño.


#Raul Ortiz Mateos

def calcularKilometroMilla(k,M):
    kilometroEntreMilla=k/M
    return kilometroEntreMilla

def calculaMillasGalon(k,M):
    MillasGalon=(k/1.609344)/(M*0.264172051)
    return MillasGalon

def calcularkilometrosquevasarecorrer(K,l,q):
    kilometrosVasArecorrer=(q*l)/K
    return kilometrosVasArecorrer

def main():
    kilometros= float(input("Cuantos kilometros llevas a recorridos?: "))
    gasolina=float(input("cuantos litros de gasolina llevas utilizados?"))
    print("si recorres ", kilometros, "km con", gasolina, "litros de gasolina, el rendimiento es:")
    print("%.2f"% calcularKilometroMilla(kilometros,gasolina),"km/l")
    print("%.2f"% calculaMillasGalon(kilometros,gasolina),"mi/gal")
    cuantosKilometros = float(input("cuantos kilometros en total vas a recorrer: "))
    print("para recorrer",cuantosKilometros,"necesitas %.2f"% calcularkilometrosquevasarecorrer(kilometros,gasolina,cuantosKilometros),"litros de gasolina")

main()

