#Autor: Andrea Montero Rivas, A01374496
# Este programa ayuda a calcular el rendimento del auto

def calcularRendimintoSi(km,l):
    rendimiento = km/l
    return rendimiento

def convertirMillasGal(km,l):
    milla=km/1.609344
    gal = l * 0.264172051
    conversion= milla/gal
    return conversion

def calcularLitros(km,rendimiento):
    litros = km / rendimiento
    return litros

def main():
    kmRecorridos= float(input("teclea el numero de km recorridos:",))
    lgasUsados = float(input("teclea los L de gasolina usados:",))
    rendimiento = calcularRendimintoSi(kmRecorridos,lgasUsados)
    conversion = convertirMillasGal(kmRecorridos, lgasUsados)
    print ("Si recorres %.2f kms con %.2f litros de gasolina, el rendimento es:" %(kmRecorridos, lgasUsados))
    print ("%.2f" %(rendimiento), "km/l")
    print ("%.2f" %(conversion), "mi/gal")

    kmProximamenteRecorridos = float(input("cuantos km vas a recorrer:", ))
    litros = calcularLitros(kmProximamenteRecorridos, rendimiento)
    print("Para recorrer %.2f km. Necesitas %.2f litros de gasolina" %(kmProximamenteRecorridos, litros))




main()