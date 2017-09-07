#Autor: Juan Sebastián Lozano Derbez

def rendimientokm(kilom, gaso):
    rendkm = kilom/gaso
    return rendkm

def rendimientomi(kilom, gaso):
    rendmil = (kilom/1.609344)/(gaso*.264172051)
    return rendmil

def main():
    kilom = int(input("Teclea el número de km recorridos: "))
    gaso = int(input("Teclea el número de litros de gasolina usados: "))

    rendkim = rendimientokm(kilom, gaso)
    rendmil = rendimientomi(kilom, gaso)

    print("Si recorres", kilom, "km con", gaso, "litros de gasolina, el rendimiento es:" )
    print('%.2f' % rendkim, "km/l")
    print('%.2f' % rendmil, "mi/gal")
    print(" ")

    kmreco = int(input("Cuántos km vas a recorrer?: "))
    recorrer = kmreco/rendkim
    print('Necesitarás %.2f' % recorrer, "litros de gasolina")

main()