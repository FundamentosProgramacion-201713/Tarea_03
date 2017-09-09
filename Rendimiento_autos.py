#encoding: UTF-8
#Autor: Neftalí Rodríguez Martínez, A01375808.
#Calcula el rendimiento de un auto, de acuerdo con los datos leídos.


def calcularRendimientokm(km_recorridos, gasolina_usada): #Calcula el rendimiento en km/l
    rendimiento_km = float(km_recorridos / gasolina_usada)
    return rendimiento_km


def convertirKm(km_recorridos): #Convierte km a mi.
    mi_recorridas = km_recorridos * 0.621371
    return mi_recorridas


def convertirL(gasolina_usada): #Convierte l a gal.
    gal_usados = gasolina_usada * 0.264172
    return gal_usados

def calcularRendimientomi(mi_recorridas, gal_usados): #Calcula el rendimiento en mi/gal.
    rendimiento_mi = mi_recorridas / gal_usados
    return rendimiento_mi


#Calcula los litros de gasolina a usar dependiendo de la cantidad de kilometros que el usuario deseé recorrer.
def calcularLitros(km_a_recorrer_float, gasolina_usada, km_recorridos):
    litros_a_usar = (km_a_recorrer_float * gasolina_usada) / km_recorridos
    return litros_a_usar


def main (): #Programa principal.

    km_recorridos = input("Teclea el número de km recorridos: ")
    gasolina_usada = input("Teclea el número de litros de gasolina usados: ")

    print("\r")

    print("Si recorres", km_recorridos, "kms con", gasolina_usada, "litros de gasolina, el rendimiento es:")

    km_recorridos = float(km_recorridos)
    gasolina_usada = float(gasolina_usada)

    mi_recorridas = convertirKm(km_recorridos)
    gal_usados = convertirL(gasolina_usada)

    rendimiento_km = calcularRendimientokm(km_recorridos, gasolina_usada)
    print("%.2f" % rendimiento_km, "km/l")

    rendimiento_mi = calcularRendimientomi(mi_recorridas, gal_usados)
    print("%.2f" % rendimiento_mi, "mi/gal")

    print("\r")

    km_a_recorrer_str = input("¿Cuántos kilómetros vas a recorrer?: ")

    print("\r")

    km_a_recorrer_float = float(km_a_recorrer_str)
    litros_a_usar = calcularLitros(km_a_recorrer_float, gasolina_usada, km_recorridos)
    print("Para recorrer", km_a_recorrer_str, "km. necesitas %.2f" % litros_a_usar, "litros de gasolina")

main()