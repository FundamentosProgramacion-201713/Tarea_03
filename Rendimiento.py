#Javier Pascal Flores A01375925

def medir_rendimiento(kilometros, gasolina):
        rendimiento=float(kilometros/gasolina)
        return rendimiento
def medir_rendimiento_Imperial(kilometros,gasolina):
    rendimiento_imperial = float(( kilometros/ 1.60934) / (0.264172 * gasolina))
    return rendimiento_imperial

def medir_Futuro(rendimiento, km):
    litros=float(km/rendimiento)
    return litros

def main():
    kilometros = int(input("Cuántos kilometros recorriste? "))
    gasolina = int(input("Cuanta gasolina gastaste en litros? "))
    rendimiento=medir_rendimiento(kilometros, gasolina)
    rendimiento_imperial=medir_rendimiento_Imperial(kilometros,gasolina)
    print("\nSi recorres %d kms con %d litros de gasolina, el rendimiento es:\n%.2f km/l\n%.2f mi/gal\n" % (
    kilometros, gasolina, rendimiento, rendimiento_imperial))
    kilometros_futuro=int(input("Cuantos km quieres viajar? "))
    litros_futuro=round(medir_Futuro(rendimiento, kilometros_futuro),2)
    print("\nPara recorrer ",kilometros_futuro,"kms necesitas ",litros_futuro," litros de gasolina")
main()