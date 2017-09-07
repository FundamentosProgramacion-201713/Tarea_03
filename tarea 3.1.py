# gbt-8
# 'Autor:vivianaosorionieto'

def calcularPago (A,B,C):
    #los boletos tipo a cuestan 400 por lo que se multiplican por la cantidad especificada en main y lo mismo con B y C
    total= (400*A) + (250*B) + (135*C)
    return total

def main ():
    #para imprimir los costos de los boletos
    print ("boleto A: 400, Boleto B: 250, Boleto C : 135. ")
    #para leer el munero de boletos A
    strA = input("cuantos boletos A quieres comprar?: ")
    #guardar la cantidad de boletos tipo A
    A = int(strA)
    # leer la cantidadde boletos tipo B
    strB = input("cuantos boletos B quieres comprar?: ")
    #guardar la cantidad de boletos tipo B
    B = int(strB)
    #leer el numero de boletos tipo C
    strC = input("cuantos boletos C quieres comprar?: ")
    #guardar la cantidad de boletos tipo C
    C = int(strC)
    #llamr la funcion para calcular el tptal
    total = calcularPago (A,B,C)
    print("su total es: ", total)

#llamar la funcion main1
main()




