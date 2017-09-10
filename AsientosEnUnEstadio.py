# encoding UTF-8
# Autor: Siham El Khoury Caviedes, A01374764

# Descripción: Cálculo de total a pagar por boletos de clase A, B y C.

# Calcular y guardar en la variable totalPago el total a pagar.
def calcularPago(asientosA, asientosB, asientosC):
    totalAsientosA = asientosA * 400                                   # Calcula y guarda en la variable asientosA el costo de los asientos de clase A.
    totalAsientosB = asientosB * 250                                   # Calcula y guarda en la variable asientosB el costo de los asientos de clase B.
    totalAsientosC = asientosC * 135                                   # Calcula y guarda en la variable asientosC el costo de los asientos de clase C.
    totalPago = totalAsientosA + totalAsientosB + totalAsientosC       # Calcula y guarda en la variable totalPago el total a pagar.
    return totalPago                                                   # Regresa totalPago (el total a pagar).


# Función principal.
def main():
    asientosA = int(input("Número de boletos de clase A: "))           # Lee el número de boletos de clase A.
    asientosB = int(input("Número de boletos de clase B: "))           # Lee el número de boletos de clase B.
    asientosC = int(input("Número de boletos de clase C: "))           # Lee el número de boletos de clase C.
    totalPago = calcularPago(asientosA, asientosB, asientosC)          # Llama a la función calcularPago.
    print ("El costo total es: %.2f" % totalPago)                      # Imprime totalPago (el total a pagar).

main()                                                                 # Ejecutar la función main.
