#gbt-8
#Autor : Viviana oSORIO nIETO
#caulcular el rendimiento n kilometros, litros
def calcularRenKL(R, G):
    KL = R/G
    return KL
#calcular el rendimiento en millas, galeones
def calcularRenMG(R, G):
    mi = 1.609 * R
    gal = (G / 0.26417)
    MG = mi / gal
    return MG
#calcular los litros que se necesitan dependiendo de los valores previos
def Calcularlitros (K, R ,G):
    litros = (K * G)/R
    return litros

def main ():
#leer datos de kilometros, litros
    strR = input("cuantos kilometros recorriste?: ")
    R =int(strR)

    strG = input("cuantos litros de gasolina utilizaste?: ")
    G = int(strG)
#imprimir resultados
    renKL = calcularRenKL(R, G)
    renMG = calcularRenMG(R, G)
    print ("si recorriste", R ,"kilometros con" ,G , "litros de gasolina, tu rendimiento es: ")
    print (renKL, "km/L")
    print (renMG, "mi/gal")
#leer datos de los kilometros que se quieren recorrer
    strK = input ("Cuantos kilometros quieres recorrer?: ")
    K = int(strK)
#imprimir los litros que se necesitara
    lit = Calcularlitros (K, R ,G)
    print ("los litros que vas a usar son:", lit)
#llamar a la funcion main
main()