#Autor: Maria Fernanda Torres Velazquez A01746537
#El siguiente programa, calcula el rendimiento de un automovil en km/litro y millas/galon

#Funcion que recibe como parametro los kilometros recorridos y los litros de gasolina utilizados y regresa el rendimiento en km/lt
def CalcularRendimiento (km,litros):
    rendimiento= km/litros
    return rendimiento

#Funcion que recibe como parametro los kilometros recorridos y los litros de gasolina utilizados, los transforma a millas y galones
# y regresa el rendimiento en millas/gal
def CalcularRendimientoMiGal (km,litros):
    millas= km/1.609344
    galones= litros*0.264172051
    rendimientoMiGal= millas/galones
    return rendimientoMiGal

#Funcion que recibe como parametro los kilometros que se desean recorrer y devuelve los litros de gasolina necesarios
def CalcularLitros(kilometros,rendimiento):
    lt= kilometros/rendimiento
    return lt

#Funcion principal en la que se introducen los kilometros recorridos y los litros gastados, asi como los kilometros que se desean recorrer,
# y lo envia a cada una de las funciones para calcular el rendimiento en km/lt y millas/gal y para calcular los litros para recorrer n kilometros
def main():
    km= float(input("Introduce los kilometros recorridos     : "))
    lt=float(input("Introduce los litros de gasolina usados : "))
    ren= CalcularRendimiento (km,lt)
    renMiGal= CalcularRendimientoMiGal(km,lt)
    print ("")
    print ("El rendimiento del automovil si recorres %.2f kilometros con %.2f litros de gasolina es:" %(km,lt))
    print ("   %.2f km/l"%(ren))
    print ("   %.2f mi/gal" %renMiGal)
    print ("-----------------------")
    print ("")
    kilometros = float(input("Introduce los kilometros que deseas recorrer: "))
    litros= CalcularLitros (kilometros,ren)
    print ("Para recorrer %.2f km, necesitas %.2f litros de gasolina"%(kilometros,litros))

#Llama a la funcion main (programa principal)
main()




