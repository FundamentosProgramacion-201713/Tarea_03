#encoding UTF-8
#Anaid Fernanda Labat González A01746289
#Descripción: Calcular km/l, millas7galón, litros de gasolina necesarios

def rendimientoKm(km,l):
    rendimientoKmL=km/l
    return rendimientoKmL
def conversionAMilla(km):
    kmAMilla=km/1.609344
    return kmAMilla
def conversionAGalon(l):
    litroAGalon=l*0.264172051
    return litroAGalon
def rendimientoMi (Mi,Gal):
    rendimientoMillaGalon=Mi/Gal
    return rendimientoMillaGalon
def litrosN(kmL,l,kmr):
    litrosNS=(kmr*l)/kmL
    return litrosNS

def main():
    km=int(input("Teclea los kilómetros recorridos:"))
    l=int(input("Teclea los litros utilizados:"))
    print(" ")
    print ("Si recorres %i kms con %i litros de gasolina, el rendimiento es:" % (km,l))

    rendiKmL= rendimientoKm (km,l)
    print("%.2f km/l" % rendiKmL)

    millas=conversionAMilla(km)
    galones=conversionAGalon(l)
    rendiMigal=rendimientoMi(millas,galones)
    print("%.2f Mi/gal"% rendiMigal)

    print(" ")
    kmR= int(input("¿Cuántos kilómetros va a recorrer?:"))
    print(" ")
    litrosNeS=litrosN (km,l, kmR)
    print("Para recorrer %i kilómetros usted necesita %.2f litros de gasolina" % (kmR, litrosNeS))

main()




