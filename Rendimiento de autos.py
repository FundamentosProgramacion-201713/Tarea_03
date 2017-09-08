# Autor: Saúl Rodrigo Toral Luna
# Matrícula: A01745007

# Leer el número de kilómetros recorridos y cantidad de gasolina utilizada e imprimir el rendimiento del automóvil en:
#1.-    #a) kilómetros/litro.
        #b) Millas/galón.
# (1 milla = 1.609344 kilómetros, 1 litro = 0.264172051 galones)

#2.- Preguntar cuántos kilómetros viajará e imprimir los litros de gasolina que necesitará.

# Definir las equivalencias como constantes
MI = 1.609344
LITRO = 0.264172051

# La función calcula rendimiento del carro en km/lt
def calcularKilometrosSobreLitro(kilometros, litros):
    rendimiento_carro = (kilometros / litros)
    return rendimiento_carro

# La función calcula el rendimiento del carro en mi/gal
def calcularMillasSobreGalon(kilometros,litros):
    mi_entre_gal = (kilometros / MI) / (litros * LITRO)
    return mi_entre_gal

# La función determina la cantidad de litros que necesita para recorrer una distancia conocida
def calcularLitrosDeGas(kilometros, rendimiento):
    litros_Gas = kilometros / rendimiento
    return  litros_Gas

def main():
# Ingresar los datos para calcular los rendimientos
    kilometros_Recorridos = float(input("Teclea el número de km recorridos: "))
    litros_de_Gas_Usada = float(input("Teclea el número de litros de gasolina usados: "))
# Imprimir los datos ingresados para mostrar los resultados
    print("")
    print("Si recorres", kilometros_Recorridos, "kms con",litros_de_Gas_Usada, "litros de gasolina, el rendimiento es: ")
# Imprimir el rendimiento del auto en km/lt y en mi/gal
    print("%.2f km/l" % calcularKilometrosSobreLitro(kilometros_Recorridos, litros_de_Gas_Usada))
    print("%.2f mi/gal" % calcularMillasSobreGalon(kilometros_Recorridos, litros_de_Gas_Usada))
    print("")
# Ingresar los kilometros que recorrera y en base al rendmiento anterior calcular los litro de gas a utilizar
    kilometros_A_Recorrer = float(input("¿Cuántos kilómetros vas a recorrer?: "))
    rendimiento = calcularKilometrosSobreLitro(kilometros_Recorridos, litros_de_Gas_Usada)
    print("")
# Imprimir los litros de gasolina que necesitará en base al rendimiento
    print("Para recorrer", kilometros_A_Recorrer,  "km. Necesitas %.2f litros de gasolina" % calcularLitrosDeGas(kilometros_A_Recorrer, rendimiento))
main()
