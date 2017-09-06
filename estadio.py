#encoding: utf-8
#written by Jordan González Bustamante
#Este programa calcula el precio total de los asientos seleccionados según la zona escogida en un estadio.

#Esta función calcula el precio por asientos pedidos y el precio total a pagar de todos los asientos requeridos.
def calcularPrecioAsientos(precioAsientosA, precioAsientosB, precioAsientosC):
    precioAsientosA *= 400
    precioAsientosB *= 250
    precioAsientosC *= 135
    precioTotal = precioAsientosA + precioAsientosB + precioAsientosC
    return precioTotal
#Función main donde pedimos el número de asientos por clase.
def main():
    print("""     Costo de asientos
-------------------------------------
    | Clase A  |   B   |  C   |
-------------------------------------
    |   $400   | $250  | $135 |
-------------------------------------""")
    asientosA = int(input("Número de asientos de la clase A : "))
    asientosB = int(input("Número de asientos de la clase A : "))
    asientosC = int(input("Número de asientos de la clase A : "))
    precioTotal = calcularPrecioAsientos(asientosA, asientosB, asientosC)
    print("El costo total es : $ %d.00" % precioTotal)
main()