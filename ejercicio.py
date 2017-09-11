# Autor: LuisMiguel Baqueiro
# Matricula: 1745997
def calcularPago(A, B, C):
    totalPago = float((A * 400) + (B * 250) + (C * 135))
    return(totalPago)
def main():
    numeroBoletosA = int(input("Número de boletos de clase A: "))
    numeroBoletosB = int(input("Número de boletos de clase B: "))
    numeroBoletosC = int(input("Número de boletos de clase C: "))
    print("El costot otla es: $", calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC))
main()