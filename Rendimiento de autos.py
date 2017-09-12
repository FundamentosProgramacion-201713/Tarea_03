#encoding UTF-8
#Autor:Pablo Garcia Morales
#Programa que lea el número de kilómetros recorridos y la cantidad de gasolina utilizada, y que imprima:

def calcula_kilolitro(numeroKilo, numeroGas):
    kilolitro = numeroKilo / numeroGas
    return kilolitro


def calcula_millagal(numeroKilo, numeroGas):
    millagalon= (numeroKilo/1.609344)  / (numeroGas*0.264172051)
    return millagalon


def main():
    numeroKilo=int(input(("Teclea el número de km recorridos: ")))
    numeroGas=int(input(("Teclea el número de litros de gasolina usados: ")))
    kilometroentrelitro=calcula_kilolitro(numeroKilo,numeroGas)
    millaentregal= calcula_millagal(numeroKilo, numeroGas)
    print("Si recorres", numeroKilo, "kms con " ,numeroGas, "litros de gasolina el rendimiento es: ")
    print("%.2f" % kilometroentrelitro, "km/l")
    print("%.2f" % millaentregal, "mi/gal ")
    kilometrosr=int(input("¿Cuántos kilómetros vas a recorrer? "))

    print(("Para recorrer %d km. necesitas a 32.86 litros de gasolina" % (kilometrosr)))
main()


