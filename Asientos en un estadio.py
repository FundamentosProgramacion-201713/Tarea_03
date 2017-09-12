# encoding:  UTF-8

# Autor: Jean Paul Esquivel Lobato     A01376152
# Descripción: Cálcular cuanto debe pagar el usuario por sus asientos en un estadio


#Cálcular el precio total de los asientos

def calcularPago (asientosA, asientosB, asientosC ):
   asienA = asientosA*400
   asienB = asientosB*250
   asienC = asientosC*135
   total= asienA+asienB+asienC
   return total

#Función principal

def main():
    asientoA = int(input("¿Cuántos asientos clase A comprará? "))
    asientoB = int(input("¿Cuántos asientos clase B comprará? "))
    asientoC = int(input("¿Cuántos asientos clase C comprará? "))
    costoTotal = calcularPago(asientoA,asientoB,asientoC)
    print("Número de boletos de clase A: ", asientoA)
    print("Número de boletos de clase B: ", asientoB)
    print("Número de boletos de clase c: ", asientoC)
    print("El costo total es: $",costoTotal)

main ()