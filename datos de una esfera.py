# gbt-8
# autor:vivianaOsorioNieto

def calcularDiametro (R):
    #para calcular el diametro se usa la formula:
    diametro = 2*(R)
    return diametro

def calcularVolumen (R):
    # para calcular el volumen se usa la formula:
    volumen = ((4/3)*3.1416) * ((R)**3)
    return volumen

def calcularArea (R):
    # para calcular el area se usa la formula:
    area = (4*3.1416)*((R)**2)
    return area

def main():
    #para leer los datos
    strR = input("cual es el radio de la esfera?: ")
    #para guardas los datos:
    R = int(strR)
    diametro = calcularDiametro(R)
    volumen =calcularVolumen(R)
    area =calcularArea(R)
    # para imprimir, mostrar los resultados
    print ('el diametro es: ', diametro)
    print ("el volumen es: ", volumen)
    print("el area es: ", area)
#para llamar a la funcion:
main()