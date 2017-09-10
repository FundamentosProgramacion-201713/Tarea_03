#uncoding: UTF-8
#Autor: Ana María López Soto
#Descripción: Este programa calcúla el rendimiento de la gasolina de un auto.

#Cálculo del rendimiento de km/l
def litrosKilometro(litrosConsumidos,kilometrosRecorridos):
    rendimientoKilometro =  kilometrosRecorridos / litrosConsumidos
    return rendimientoKilometro

#Cálculo del redimiento de Milla/Gálon
def galonesMillas(litrosConsumidos,kilometrosRecorridos):
    rendimientoMillas = (kilometrosRecorridos / 1.609344) / (litrosConsumidos * 0.264172051)
    return rendimientoMillas

#Cálculo de Litros consumidos por cierto kilometraje por recorrer
def calculoLitros(litrosConsumidos, kilometrosRecorridos, kilometrosParaRecorrer):
    litrosPorConsumir = (litrosConsumidos / kilometrosRecorridos) * kilometrosParaRecorrer
    return litrosPorConsumir

def main():
    kilometrosRecorridos = float(input("Teclea el número de km recorridos: "))
    litrosConsumidos = float(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKilometros = litrosKilometro(litrosConsumidos, kilometrosRecorridos)
    rendimientoMillas = galonesMillas(litrosConsumidos, kilometrosRecorridos)
    print(  )
    print("Si recorres", kilometrosRecorridos,"kms con",litrosConsumidos,"litros de gasolina, elrendimiento es:")
    print("{:.2f}".format(rendimientoKilometros), "km/l")
    print("{:.2f}".format(rendimientoMillas), "mi/gal")
    print(       )
    kilometrosParaRecorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))
    print(      )
    print("Para recorrer",kilometrosParaRecorrer, "km. necesitas", ("{:.2f}".format(calculoLitros(litrosConsumidos,kilometrosRecorridos,kilometrosParaRecorrer))),"litros de gasolina")

main()