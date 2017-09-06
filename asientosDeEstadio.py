#AUTOR: JOSÉ HEINZ MÖLLER SANTOS
#Este programa te calcula el pago total de diferentes tipos de asientos preguntandote cuántos vas a ocupar de clase A, B y C

#Calcula el precio del numero de los asientos A elegidos
def calcularElPrecioAsientosA(asientosA):
    A = 400*asientosA
    return A

#Calcula el precio del numero de los asientos B elegidos
def calcularElPrecioAsientosB(asientosB):
    B = 250*asientosB
    return B

#Calcula el precio del numero de los asientos  C elegidos
def calcularElPrecioAsientosC(asientosC):
    C = 135*asientosC
    return C

#Calcula el precio total sumando A, B y C
def calcularElPrecioTotal(asA,asB,asC):
    precioTotal = asA+asB+asC
    return precioTotal

#Es la función principal, lee los datos e imprime los resultados.
def main():
    asientosA = float(input("Numero de asientos en clase A: "))
    asientosB = float(input("Numero de asientos en clase B: "))
    asientosC = float(input("Numero de asientos en clase C: "))

    asA = float(calcularElPrecioAsientosA(asientosA))
    asB = float(calcularElPrecioAsientosB(asientosB))
    asC = float(calcularElPrecioAsientosC(asientosC))
    precioT = float(calcularElPrecioTotal(asA,asB,asC))

    print("El precio total es de $%.2f"%precioT)

main()