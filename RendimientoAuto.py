#encoding: UTF-8
#Autor: Dora Gabriela Lizárraga González A01229599
#Este programa le indica al usuario el rendimiento de la gasolina en su auto

#Esta función calcula el rendimiento entre kilometros y litros
def rendimientoKL (km,lit):
    rendKL = km/lit
    rendKL = round(rendKL,2)
    return rendKL

#Esta función calcula la conversión en millas y galones y después el rendimiento entre estas
def rendimientoMG (km,lit):
    millas = km/1.609344
    galones = lit*0.264172051
    rendMG = millas/galones
    rendMG = round(rendMG,2)
    return rendMG

#Esta función calcula la gasolina necesaria tomando en cuenta el rendimiento calculado anteriormente
def rendimientoGas (rendKL,km2):
    gasNecesario = km2/rendKL
    return gasNecesario

#Esta función lee los valores de las variables, ejecuta las otras funciones e imprime el resultado
def main():
    km = float(input('Teclea el número de km recorridos: '))
    lit = float(input('Teclea el número de litros de gasolina usados: '))
    kmLit = rendimientoKL(km,lit)
    miGal = rendimientoMG(km,lit)
    print()
    print('Si recorres ',km,'km. con',lit,'de gasolina, el rendimiento es:')
    print(kmLit,' km/l')
    print(miGal,' mi/gal')
    print()
    km2 = float(input('¿Cuántos kilómetros vas a recorrer? '))
    gas = rendimientoGas(kmLit,km2)
    print('Para recorrer ',km2,' km. necesitas ',gas,' litros de gasolina.')

main()