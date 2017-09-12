# encoding:  UTF-8

# Autor: Jean Paul Esquivel Lobato     A01376152
# Descripción: Cálcula rendimiento de un auto.


# Cálcular el rendimiento 1 del auto

def calcularRendimientoKmXLt(km,litros):
    rendimiento = km/litros
    return rendimiento

# Operación de conversión a partir del rendimiento

def calcularMillasPorGalon(km,litros):
    millas = km / 1.609344
    galones = litros * .264172051
    rendimiento2 = millas / galones
    return rendimiento2

# Función principal.

def main():
    kilometrosRecor = int(input("Teclea el número de km recorridos: "))
    litrosRecor = int(input("Teclea el número de litros de gasolina usados: "))
    millasGalon = calcularMillasPorGalon (kilometrosRecor, litrosRecor)
    kilomeLit =  calcularRendimientoKmXLt (kilometrosRecor, litrosRecor)
    print (" ")
    print ("Si recorres %d kms con %.0f litros de gasolina, el rendimeinto es de:" % (kilometrosRecor, litrosRecor))
    print ("%.2f" % kilomeLit, ("km/l"))
    print("%.2f" % millasGalon, ("mi/gal"))
    kmR = int(input("¿Cuántos kilómetros vas a recorrer? "))
    litrosNece = kmR / kilomeLit


    print ("Para recorrer %d km necesitas %.2f litros de gasolina"""% (kmR,litrosNece))

main()
