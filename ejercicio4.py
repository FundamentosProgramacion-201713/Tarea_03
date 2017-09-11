# Autor: LuisMiguel Baqueiro
# Matricula: 1745997
def rendimiento(nK, nL):
    total = nK / nL
    return total
def convercion(nK, nL):
    total = (nK / 1.609344) / (nL * 0.264172051)
    return total
def calcularLitros(kml, kilometros):
    total = kilometros / kml
    return total
def main():
    nK = int(input("Teclea el número de km recorridos: "))
    nL = int(input("Teclea el número de litros de gasolina usados: "))
    print("")
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es:" % (nK, nL))
    print("%.2f km/l" % rendimiento(nK, nL))
    print("%.2f mi/gal" %convercion(nK, nL)) #este valor me da distinto pero segun el convertidor de google, esta bien el resultado
    print("")
    kilometros = int(input("¿Cuántos kilómetros vas a recorrer?"))
    print("")
    print("Para recorrer %d km. necesitas %.2f litros de gasolina" % (kilometros, calcularLitros(rendimiento(nK, nL), kilometros)))

main()