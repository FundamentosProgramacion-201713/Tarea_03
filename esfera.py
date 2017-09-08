# encoding UTF-8
# Autor: Jaime Orlando López Ramos, A01374696
# Descripción: Un programa que lea el radio de una esfera y calcue diámetro, área y volumen para luego imprimirlos


# Crear una función que calcule el diámetro tomando el radio como parámetro, multiplicando el radio por 2
def calcularDiametro(radio):
    dm = 2 * radio
    return dm


#Crear una función que calcule el área tomando el radio como parámetro. Usando la fórmula área = 4(pi)(radio)**2
def calcularArea(radio):
    a = 4 * 3.1416 * (radio**2)
    return a


#  Crear una función que calcule el voumen, tomando el radio como parámetro.
#  Usando la fórmula volumen = (4/3)(pi)(radio)**3
def calcularVolumen(radio):
    v = (4/3)* 3.1416 * (radio**3)
    return v


# Crear una función main que lea el radio de la esfera y posteriormente
# llame a las funciones previamente creadas para darle una variable a cada uno de los valores
# que las funciones regresaron, para así imprimir los datos requeridos
def main():
    r= float(input("Introduzca el radio de la esfera: "))
    dm = calcularDiametro(r)
    a = calcularArea(r)
    v = calcularVolumen(r)
    print("Esfera con radio:", r)
    print("Diámetro: %.2f" % (dm))
    print("Área: %.2f" % (a))
    print("Volumen: %.2f" % (v))

main()