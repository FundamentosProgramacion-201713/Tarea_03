#Autor: Juan Sebastián Lozano Derbez

def calcboletosa(cantidada, cantidadb, cantidadc):
    total = 400*(cantidada) + 250*(cantidadb) + 135*(cantidadc)
    return total

def main():
    cantidada = int(input("Cuántos boletos A?: "))
    cantidadb = int(input("Cuántos boletos B?: "))
    cantidadc = int(input("Cuántos boletos C?: "))

    total = calcboletosa(cantidada, cantidadb, cantidadc)
    print("Total: ", total)
main()