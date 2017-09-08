# Autor: Saúl Rodrigo Toral Luna
# Matrícula: A01745007
# Preguntar al usuario cuántos boletos quiere comprar para cada tipo de asiento e imprimir el total a pagar.

# Calcular el pago de cada zona, sumar sus totales y guardar el valor
def calcularPago(asientosA, asientosB, asientosC):
    asientos_Clase_A = 400 * asientosA
    asientos_Clase_B = 250 * asientosB
    asientos_Clase_C = 135 * asientosC
    totalPago = asientos_Clase_A + asientos_Clase_B + asientos_Clase_C
    return totalPago

def main():
    #Ingresar la cantidad de boletos de cada clase
    boletos_ClaseA = int(input("Número de boletos clase A: "))
    boletos_ClaseB = int(input("Número de boletos clase B: "))
    boletos_ClaseC = int(input("Número de boletos clase C: "))

    # Imprimir el resultado de la función calcularPago()
    print("El costo total es de: $%.2f " % calcularPago(boletos_ClaseA, boletos_ClaseB, boletos_ClaseC))

main()
