#ecoding:UTF-8
#Autor: Angel Ramírez Martínez
#Descripción: Calcula el rendimiento de un automóvil y calcula cuantos litros se utilizarán en un viaje

# Se calcula el rendimiento en kilometros por litro, ambas variables se reciben como parámetros.
def rendimientoKm(km,l):
    rendKm = km/l
    return rendKm


# Se calculan las millas equivalentes a los kilometros que se reciben como parámetro.
def conversionmi (km):
    millas = km/1.609344
    return millas


# Se calculan los galones equivalentes a los litros que se reciben como parámetro.
def conversiongal (l):
    galones = l * 0.264172051
    return galones


# Se llama a las funciones conversionmi y conversiongal para obtener las millas y galones equvalentes a los kilometros y litros
# que se reciben como parámetro para obtener el rendimiento de millas por galón.
def rendimientogal (km, l):
    mi = conversionmi(km)
    gal = conversiongal(l)
    rendMi = mi/gal
    return rendMi


# Se calculan los litros que se van a necesitar a partir de los kilometros y el rendimiento en kilometros por litro que
# se reciben como parámetro.
def calculalitros (km,rendimiento):
    litros = km/rendimiento
    return litros



def main ():
    km = int(input('Teclea el número de km recorridos: '))
    l = int(input('Teclea el número de litros de gasolina usados: '))
    rendimiento1 = rendimientoKm(km, l)
    rendimiento2 = rendimientogal(km,l)
    print('')
    print('Si recorres %i kms con %i litros de gasolina, el rendimiento es: ' %(km,l))
    print('%.2f km/l' %(rendimiento1))
    print('%.2f mi/gal' %(rendimiento2))
    print('')
    kilometrosV = int(input('¿Cuántos kilómetros vas a recorrer? '))
    litrosV = calculalitros(kilometrosV,rendimiento1)
    print('')
    print('Para recorrer %i km. Necesitas %.2f litros de gasolina' %(kilometrosV,litrosV))
main()
