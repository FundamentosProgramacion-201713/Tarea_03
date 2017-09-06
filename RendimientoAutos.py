#Autor: Gabriela Mariel Vargas Franco A01745775
#encoding: UTF-8
#Calcular el rendimiento de un auto dependiendo el número de kilometros y litros recorridos/utilizados. .
def kmLitro (km, litro):
    #Calcula y guarda en la variable kmLitro el rendimiento del automovil
    kmLitro=(km/litro)

    #Regresar kmLitro
    return kmLitro

def millGalon(kmReco,litGas):
    #Calcula y guarda en la variable millGalon el rendimiento del automovil
    millGalon=(kmReco/1.609344)/(litGas*0.264172051)
    return millGalon

def paraRecorrer(cuantosKm,km,litro):
    paraRecorrer=(cuantosKm/(km/litro))
    return paraRecorrer
def main():
    kmRecorridos=int(input("Teclea el número de km recorridos:"))
    cantGasolina=int(input("Teclea el número de litros de gasolina usados:"))

    kL=kmLitro(kmRecorridos,cantGasolina)
    print("Si recorres %d kms con %.0f litros de gasolina, el rendimiento es:" %(kmRecorridos,cantGasolina))
    print(format(kL,".2f"),"km/l")
    mG=millGalon(kmRecorridos,cantGasolina)
    print(format(mG,".2f"),"mi/gal")
    kmARecorrer=int(input("¿Cuántos kilometros vas a recorrer:?"))
    pR=paraRecorrer(kmARecorrer,kmRecorridos,cantGasolina)
    print("Para recorrer %d km. necesitas %.2f litros de gasolina" %(kmARecorrer,pR))


main()
