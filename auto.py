#Yerish Valdes Bernes A01375755
#consumo de un auto y estimado de gasolina
def rendimiento(litros,km):
    rendimiento= km/litros
    return rendimiento

def conversion(litros,km):
    galones=litros*0.264172051
    millas=km/1.609344
    convercion_total=millas/galones
    return convercion_total

def gasolina_requerida(rendimiento_total,estimado):
    gasolina_total=estimado/rendimiento_total
    return gasolina_total

def main():
    litros=float(input("Total de litros ocupados:"))
    km=float(input("Total de Km recorridos:"))
    rendimiento_total=rendimiento(litros, km)
    convercion_rendimiento=conversion(litros,km)
    print("Si recorres %.2f kms con %.2f litros de gasolina, el rendimiento es:\nkm/litros:%.2f\nmillas/galones:%.2f"%(km,litros,rendimiento_total,convercion_rendimiento))
    estimado=float(input("¿Cuántos kilómetros vas a recorrer?:"))
    gasolina_total= gasolina_requerida(rendimiento_total, estimado)
    print("Para recorrer %.2f km. necesitas %.2f litros de gasolina"%(estimado,gasolina_total))

main()