#encoding: UTF-8
#Nazdira Abigail Cerda del Prado A01375428
#Descripción: Diseño TopDown para calcular rendimiento de autos tomano en cuenta los km recorridos y la gasolina consumida,
#  además calcula la gasolina necesaria para los km que el usuario desee.

def calcularRendimKmL(kilom,lgas):
    rendimkl=(kilom/lgas)
    return rendimkl

def calcularRendimMiGal (rendimkl):
    rendimmigal=(rendimkl)/(0.264172051*1.609344)
    return rendimmigal

def main():
    kilom=float(input("Km recorridos:"))
    lgas=float(input("Litros de gasolina usados:"))
    rendimientokml=float(calcularRendimKmL(kilom,lgas))
    rendimientomigal=float(calcularRendimMiGal(rendimientokml))
    print("Si recorres", kilom ,"km con", lgas,"litros de gasolina, el rendimiento es de:")
    print(format(rendimientokml,".2f"), "km/l")
    print(format(rendimientomigal,".2f"), "mi/gal")

main()

def calcularGasKmRec(kmrecorrer):
    gaskmrec=kmrecorrer*0.06571428571
    return gaskmrec

def main():
    kmrecorrer=float(input("Km que desea recorrer:"))
    gasolinanecesaria=float(calcularGasKmRec(kmrecorrer))
    print("Para recorrer", kmrecorrer ,"km necesitas" , format(gasolinanecesaria,".2f"),"litros de gasolina")

main()