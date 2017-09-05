#AUTOR: PEDRO CORTÉS SOBERANES A01371919
#FUNCIÓN: CALCULAR PAGOS DE UN TRABAJADOR


#Función: Sirve para calcular el rendimiento del auto en km/l
def kmxlitro ( km,litros):
    rendimiento = km/litros
    return rendimiento

#Función: Sirve para calcular el rendimiento del auto en mi/gal
def millasxgalon(km, litros):
    millas = km/1.609344
    galones = litros*.264172051
    rendimiento2 = millas / galones
    return rendimiento2



def main ():
    kmR = int(input("Teclea el número de km recorridos: "))
    litU = int(input("Teclea el número de litros de gasolina usados"))
    mixgal = millasxgalon(kmR,litU)
    kmxl = kmxlitro(kmR,litU)
    print ("""
Si recorres %d kms con %.0f litros de gasolina, el rendimeinto es de:""" % (kmR,litU))
    print ("%.2f" % kmxl, ("km/l"))
    print("%.2f" % mixgal, ("mi/gal"))
    kmVasR = int(input("""
¿Cuántos kilómetros vas a recorrer? """))
    litrosNecesarios = kmVasR/kmxl
    print ("""
Para recorrer %d km necesitas %.2f litros de gasolina"""% (kmVasR,litrosNecesarios))


main ()