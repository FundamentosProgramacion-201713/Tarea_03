#encoding UTF-8
#Autor: Joaquin Rios Corvera A01375441

#Calcula la eficiencia en km/l de un automóvil
def calcularKilometrosPorLitro(kilometros, litros):
    eficiencia = kilometros / litros
    return eficiencia

#Calcula la eficiencia en mi/gal de un automóvil
def calcularMillasPorGalon(kilometros, litros):
    eficiencia = (kilometros/1.609344)/(litros*0.264172051)
    return eficiencia

#Calcula cuánta gasolina se necesita para recorrer ciertos kilómetros
def calcularGasolinaRequerida(kilometros, kilometrosPorLitro):
    requerida = kilometros/kilometrosPorLitro
    return requerida

def main():
    kilometros = int(input("Tecela el número de km recorridos: "))
    litros = int(input("Teclea el número de litros de gasolina usados: "))

    kilometrosPorLitro = calcularKilometrosPorLitro(kilometros, litros)
    millasPorGalon = calcularMillasPorGalon(kilometros, litros)

    print("")
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es: " %(kilometros, litros))
    print("%.2f km/l" %kilometrosPorLitro)
    print("%.2f mi/gal" %millasPorGalon)
    print("")

    kilometrosRecorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))
    gasolinaRequerida = calcularGasolinaRequerida(kilometrosRecorrer, kilometrosPorLitro)
    print("Para recorrer %d km. necesitas %.2f litros de gasolina" %(kilometrosRecorrer, gasolinaRequerida))

main()