#Raul Ortiz Mateos

def calcularPago(a,b,c):
    totalPago=(400*a)+(250*b)+(135*c)
    return totalPago

def main():
    boletoA=int(input("¿Cuantos boletas de la clase A vas a comprar? "))
    boletoB=int(input("¿Cuantos boletas de la clase B vas a comprar? "))
    Boletoc=int(input("¿Cuantos boletas de la clase C vas a comprar? "))
    totaldeboletos=calcularPago(boletoA,boletoB,Boletoc)
    print("el costoto total de todos los boletos son:",totaldeboletos)

main()