##encoding: UTF-8

# Autor: Edgar Alexis González Amador, A01746540
# Descripcion: Realiza un programa que permita conocer el rendimiento de un automovil en kilometros/litro y millas/galon.
# Y que permita concer la cantidad de litros de gasolina necesarios para recorrer una determinada distancia.



#Función para calcular el primer resultado del rendimiento, con los kilometros y los litros
def calcularRendimientoKmLt(kmRecorridos, ltUsados):
    rendimiento1 = kmRecorridos / ltUsados
    return rendimiento1

#Función para realizar la conversión de km/lt a mi/gal a partir del resultado obtenido en la funcion anterior
def calcularRendimientoMiGal(rendimiento1):
    rendimiento2 = rendimiento1 / 1.609344 / 0.26417051
    return rendimiento2

#Función para calcular la cantidad de Litros necesarios para realizar el recorrido, a partir del resultado del rendimiento
def calcularLtParaRecorrido(kmPorRecorrer, rendimiento):
    ltParaRecorrido = kmPorRecorrer / rendimiento
    return ltParaRecorrido

#Main, función principal en la que se llama a las funciones anteriores y se piden e imprimen datos.
def main():
    kmRecorridos = int(input("Teclea el número de km recorridos: "))
    ltUsados = int(input("Teclea el número de litros de gasolina usados: "))
    Rendimiento1 = calcularRendimientoKmLt(kmRecorridos, ltUsados)
    Rendimiento2 = calcularRendimientoMiGal(Rendimiento1)
    print("")
    print("Si recorres %d kms con %d litos de gasolina, el rendimiento es:"%(kmRecorridos,ltUsados))
    print("%.2f km/l"%(Rendimiento1))
    print("%.2f mi/gal"%(Rendimiento2))
    print("")
    kmPorRecorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))
    ltParaRecorrido = calcularLtParaRecorrido(kmPorRecorrer, Rendimiento1)
    print("")
    print("Para recorrer %d km. necesitas %.2f litros de gasolina"%(kmPorRecorrer,ltParaRecorrido))

main()