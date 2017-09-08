#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: con los datos tecleados del usuario nos da el rendimiento  que tendra el auto en cuestion y depsues si deseamos saber cuanta gasolina necesitamos para recorrer ciertos km nos la va a dar

#con base a los datos de klometrof y gasolinag se crea la operación para calcular kilometros / litros
def calcKilometroSobreLitro(kilometrosf, gasolinag):
    kmsSobrel = kilometrosf / gasolinag
    return kmsSobrel

#con base a los datos de klometrof y gasolinag se crea la operación para calcular millas / galones
def calcMillasSobreGalon(kilometrosf, gasolinag):
    milla = kilometrosf / 1.609344
    galon = gasolinag * 0.264172051
    miSobregal = milla / galon
    return miSobregal

#con base a los datos de kmsobrel  y misobregal de las funciones calcKilometroSobreLitro(kilometrosf, gasolinag) y calcMillasSobreGalon(kilometrosf, gasolinag) se crea la operación para calcular los litros de gasolina necesarios para cierto numero de kilometros
def calcLitrosDeGasolina(kmRecorrerf, kmSobrel):
    lGasolina = kmRecorrerf / kmSobrel
    return lGasolina

# se leen los kilometros recorridos, los litros de gasolina usados y Cuántos kilómetros va a recorrer dados por el usuario, despues se imprime km/l, mi/gal y los litros de gasolina cesesarios, los cuales se obtendran llamando a las funciónes calcKilometroSobreLitro(kilometrosf, gasolinag), calcMillasSobreGalon(kilometrosf, gasolinag),calcLitrosDeGasolina(kmRecorrerf, kmSobrel)
def main () :
    kilometros = int(input("Teclea el número de km recorridos: "))
    gasolina = int(input("Teclea el número de litros de gasolina usados: "))
    kilometrosf = float(kilometros)
    gasolinag = float(gasolina)
    print("Si recorres", kilometros, "kms con", gasolina, "litros de gasolina, el rendimiento es:")
    print("%.2f" % calcKilometroSobreLitro(kilometrosf,gasolinag), "km/l")
    print("%.2f" % calcMillasSobreGalon(kilometrosf, gasolinag), "mi/gal")
    kmRecorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))
    kmRecorrerf = float(kmRecorrer)
    print("Para recorrer", kmRecorrer, "km. necesitas %.2f" % calcLitrosDeGasolina(kmRecorrerf, calcKilometroSobreLitro(kilometrosf, gasolinag)), "litros de gasolina")

#llama a la función main
main()