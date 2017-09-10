# encoding UTF-8
# Autor: Siham El Khoury Caviedes, A01374764

# Descripción: Cálculo del rendimiento de un auto.

# Calcular y guardar en la variable kilometrosPorLitros el rendimiento del carro en km/l.
def calcularKilometrosPorLitro(kilometros, litros):
    kilometrosPorLitro = kilometros / litros                                                                    # Calcular y guardar en la variable kilometrosPorLitros el rendimiento del carro en km/l.
    return kilometrosPorLitro                                                                                   # Regresar kilometrosPorLitro.


# Calcular y guardar en la variable millasPorGalon el rendimiento del carro en mi/gal.
def calcularMillasPorGalon(kilometrosPorLitro):
    millasPorGalon = kilometrosPorLitro * 2.362023653                                                           # Calcular y guardar en la variable millasPorGalon el rendimiento del carro en mi/gal.
    return millasPorGalon                                                                                       # Regresar millasPorGalon.


# Calcular y guardar en la variable litrosNecesitados los litros que necesarios para recorrer ciertos kilómetros.
def calcularLitrosNecesitados(kmPorRecorrer, kilometrosPorLitro):
    litrosNecesitados = kmPorRecorrer / kilometrosPorLitro                                                      # Calcular y guardar en la variable litrosNecesitados los litros que necesarios para recorrer ciertos kilómetros.
    return litrosNecesitados                                                                                    # Regresar litrosNecesitados.


# Función principal.
def main():
    kilometros = int(input("Teclea el número de km recorridos: "))                                              # Leer y guardar en la variable kilometros los kilómetros recorridos.
    litros = int(input("Teclea el número de litros de gasolina usados: "))                                      # Leer y guardar en la variable litros los litros de gasolina usados.
    print (" ")                                                                                                 # Imprimir espacio.
    print ("Si recorres", kilometros, "kms con", litros, "litros de gasolina, el rendimiento es:")              # Imprimir los kilómetros recorridos y litros usados.
    kilometrosPorLitro = calcularKilometrosPorLitro (kilometros, litros)                                        # Llamar a la función calcularKilometrosPorLitro.
    millasPorGalon = calcularMillasPorGalon (kilometrosPorLitro)                                                # Llamar a la función calcularMillasPorGalón.
    print ("%.2f km/l" % kilometrosPorLitro)                                                                    # Imprimir el rendimiento en km/l.
    print ("%.2f mi/gal" % millasPorGalon)                                                                      # Imprimir el rendimiento en mi/gal.
    print (" ")                                                                                                 # Imprimir espacio.
    kmPorRecorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))                                          # Leer y guardar en la variable kmPorRecorrer los kilómetros por recorrer.
    litrosNecesitados = calcularLitrosNecesitados (kmPorRecorrer, kilometrosPorLitro)                           # Llamar a la función calcularLitrosNecesitados.
    print ("Para recorrer", kmPorRecorrer, "km. necesitas %.2f litros de gasolina" % litrosNecesitados)         # Imprimir los kilómetros a recorrer y los litros necesitados.

main()                                                                                                          # Ejecutar la función main.
