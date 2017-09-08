#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: te indica el total a pagar por el numero y clase de los asienntos que quieres comprar


#con base a los datos de los asientos A, B y C se crea la operación con respecto a su clase, para despúes sumar todos los boletos y regresar el totalPago
def calcularPago(asientosA, asientosB, asientosC) :
    a = asientosA * 400
    b = asientosB * 250
    c = asientosC * 135
    totalPago = a + b +c
    return totalPago



# se leen el número de boletos clase A, B y C dados por el usuario y se imprime elcosto total llamando a la función calcularPago(asientosA, asientosB, asientosC)
def main () :
    asientosA = float(input("Número de boletos de clase A: "))
    asientosB = float(input("Número de boletos de clase B: "))
    asientosC = float(input("Número de boletos de clase C: "))

    print("El costo total es: $%.2f" % calcularPago(asientosA, asientosB, asientosC))

#llama a la función main
main()