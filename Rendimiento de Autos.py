#encoding: UTF-8
#Omar Israel Galván García A01745810
#Este programa lee el número de kilómetros recorridos y la cantidad de gasolina utilizada e imprime:
#kilómetros / litro || millas / galón || litros de gasolina que necesitará para recorrer cierta cantidad


milla = 1.609344      # se definen constantes para evitar problemas con los números
galon = 0.264172051

def rendimientoKm(kilometrosRecorridos, litrosGasolina):        # se crea la funcion rendimientoKm que al dividir los km
    rendimientokmLi = (kilometrosRecorridos / litrosGasolina)   # recorridos entre los litros de gasolina, se obtiene el rendimiento
    return rendimientokmLi                                      # en km/l

def rendimientoMi(kilometrosRecorridos, litrosGasolina):        #se crea la funcion rendimientoMi que convierte km a millas y lt a galones
    rendimientoMiGal = (kilometrosRecorridos/milla) / (litrosGasolina * galon) # divide estas dos conversiones y se obtiene su
    return rendimientoMiGal                                                    #rendimiento en mi/gal

def distanciaR (distancia, rendimientokm):                       # se crea la funcion distanciaR que calcula la cantidad de
    distanciaRecorrer = (distancia / rendimientokm)              #gasolina necesaria
    return distanciaRecorrer

def main():                                                     #la funcion main se encarga de leer todos los valores e imprimir los resultados
    kilometrosRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosGasolina = int(input("Teclea el número de litros de gasolina usados: "))
    rKm = rendimientoKm(kilometrosRecorridos,litrosGasolina)
    rMi = rendimientoMi(kilometrosRecorridos,litrosGasolina)
    print("Si recorres %i"%(kilometrosRecorridos),"kms con %i"%(litrosGasolina),"litros de gasolina, el rendimiento es:")
    print("%.2f"%(rKm),"km/l")
    print("%.2f"%(rMi),"mi/gal")  # no me salieron los mismos decimales profe :/
    recorrerKm = int(input("¿Cuántos kilómetros vas a recorrer? "))
    gasolinaNecesaria = distanciaR(recorrerKm,rKm)
    print("Para recorrer %i"%(recorrerKm),"km. necesitas %.2f"%(gasolinaNecesaria),"litros de gasolina")




main()
