#encoding: UTF-8

#Autor: Javier Martínez Hernández  A01375496
#Descripción: se calculara el rendimiento del auto y con ello se sacara cuantos litros tienes que usar para recorrer cierta distancia

def calcularRendimientoAuto(kmRecorridos, gasUsed):          #se calcuara el rendimiento del auto en KM/L
    rendimientoKML=kmRecorridos/gasUsed
    return rendimientoKML

def calcularMillas(kmRecorridos):               #se hara la conversion de KM a millas
    milla=kmRecorridos/1.609344
    return milla
def calcularGalones(gasUsedL):                 #se hara la conversion de Litros a Galones
    galones= gasUsedL*0.264172051
    return galones


def calcularRendimientoAutoMpGal(kmRecorridos, gasUsedL):       #se calcuara el rendimiento del auto en MI/Gal
    millas=calcularMillas(kmRecorridos)
    galones=calcularGalones(gasUsedL)
    rendimientoMiGal=millas/galones
    return rendimientoMiGal


def main():
    kmRecorridos=int(input("Teclea el número de km recorridos: "))
    gasUsedL=int(input("Teclea el número de litros de gasolina usados: "))
    rendimientoDelAutoKmL=calcularRendimientoAuto(kmRecorridos,gasUsedL)
    rendimientoDelAutoMpGal=calcularRendimientoAutoMpGal(kmRecorridos,gasUsedL)
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es: \n%.2f km/l \n%.2f mi/gal"%(kmRecorridos,gasUsedL,rendimientoDelAutoKmL,rendimientoDelAutoMpGal) )
    kmPorRecorrer=int(input("¿Cuántos kilómetros vas a recorrer? "))
    gasNecesitada=kmPorRecorrer/rendimientoDelAutoKmL
    print("Para recorrer %d km. Necesitas %.2f litros de gasolina" % (kmPorRecorrer,gasNecesitada))


main()