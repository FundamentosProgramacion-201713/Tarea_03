# coding: UTF-8
# autor: Eduardo Gallegos Solís
# Calcula el rendimiento de gasolina de un automivil

def calcuarRendimientoKilometros (kilometros, litros):
    #calcula el rendimiento del automovil en kilómetros y litros
    rendimientoKilometros = kilometros / litros
    return rendimientoKilometros

def calcularRendimientoMillas (rendimientoKilometros):
    # calcula el rendimiento del automovil en millas y galones
    rendimientoMillas = rendimientoKilometros * 2.352648728
    return rendimientoMillas

def calcularLitrosNecesitados (kilometrosARecorrer, kilometros, litros):
    # calcula los litros que se necesitan para recorrer cierta distancia, con respecto al rendimiento antes calculado
    litrosNecesitados = (kilometrosARecorrer * litros) / kilometros
    return litrosNecesitados

def main():
    kilometros = int(input("Teclea el número de km recorridos:"))
    litrosGasolina = int(input("Teclea el número de litros de gasolina usados:"))
    rendimientoKilometros = calcuarRendimientoKilometros(kilometros, litrosGasolina)
    rendimientoMillas = calcularRendimientoMillas(rendimientoKilometros)
    print("")
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es:" %(kilometros,litrosGasolina))
    print("%.2f km/l" %(rendimientoKilometros))
    print("%.2f mi/gal" %(rendimientoMillas))
    print("")
    kilometrosARecorrer = int(input("¿Cuántos kilómetos vas a recorrer?"))
    litrosNecesitados = calcularLitrosNecesitados(kilometrosARecorrer, kilometros, litrosGasolina)
    print("Para recorrer %d km. necesitas %.2f litros de gasolina" %(kilometrosARecorrer, litrosNecesitados))

main()