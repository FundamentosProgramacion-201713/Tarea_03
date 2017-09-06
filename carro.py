#encoding: UTF-8
#Autor: Angel Roberto Pesado Bartolo
#Elaboración de un programa que pregunte al usuario cuantos kilimetros y cuantos litros de gasolina lleva gastados para obtener el rendimiento
#Después preguntar al usuario cuanta distancia va a recorrer y obtener cuantos litros de gasolina gastará.

def calcularRendimientoK(kilometros, gasolina): #Definimos la función caluclarRendimientoK
    renk=(kilometros/gasolina) #Obtenemos el rendimiento en kilometros por litro a partir de dividir los kilometros entre la gasolina con los datos dados por el usuario.
    return renk #regresamos rendimiento en kilometros por litro
def calcularRendimientoM(kilometros, gasolina):#Definimos la función caluclarRendimientoM
    renm=((kilometros/1.609344)/(gasolina*.264172051))#Obtenemos el rendimiento en millas por galon para eso tenemos que hacer la conversión km a millas y litros a galones para finalemnte dividir millas entre galon
    return renm #regresamos rendimientos en millas por galon
def calcularDistanciaK(kilometrosd,kilometros,gasolina): #Definimos la función calcularDistanciaK
    kilometrosr=(kilometrosd/(kilometros/gasolina)) #Obtenemos los litros que recorerá con la distancia que nos indique el usuario entre los kilometros que esta dividido or la gasolina
    return kilometrosr #regresamos los litros que ncesita
def main(): #definimos la función main
    km=int(input("Escribe el número de km recorridos:")) #Pedimos al usuario los kilometros
    gas=int(input("Escribe el numero de litros gastados:"))#peddimos al usuario los litros de gasolina utilizados
    ren=calcularRendimientoK(km,gas)#Mandamos los datos ingresados por el usuario a la función caclularRendimientoK para obtener el rendimiento en km/litros
    renm=calcularRendimientoM(km,gas)#Mandamos los datos ingresados por el usuario a la función caclularRendimientoM para obtener el rendimiento en m/gal
    print("Si recorres",km,"kms con",gas,"litros de gasolina, el rendimiento es de %.2f "%(ren),"km/h")#imprimimos el rendimiento en km/litros
    print("%.2f"%(renm),"mi/h") #imprimimos el rendimiento en m/gal
    dis=int(input("¿Cuántos kilometros vas a recorrer?: "))#pedimos al usuario cuantos kilometros va  a recorrer
    rect=calcularDistanciaK(dis,km,gas) #Mandamos los datos ingresados por el usuario a la función caclularDistanciaK para obtener los litros que necesita para recorrer la distancia indicada por el usuario
    print("Pare recorrer",dis,"km. Necesitas %.2f"%(rect),"litros de gasolina")#imprimimos los litros que necesita para recorrer esa distancia

main() #llamamos a la función main para que se ejecute lo que esta dentro de ella.


