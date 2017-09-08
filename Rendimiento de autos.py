#encoding: UTF-8
#Luis Fernando Figueroa Rendon, A01746139

#Calcular el rendimiento de los autos.
def main():
   kilometros=float(input("Teclea el numero de km recorridos: "))
   litrosgasolina= float(input("Teclea el numero de litros de gasolina utilizados: "))

#Funcion que recibe los kilometros y litros de gasolina, calcula el rendimiento del auto en km/lt.
   def calcularRendimiento(km, lt):
       rendimiento=km/lt
       return rendimiento

#Funcion que convierte de km/lt a milla/galon.
   def calcularConversion(km, lt):
       millas=km/1.609344
       galones=lt*0.264172051
       conversion=millas/galones
       return conversion
#Funcion que determina cuantos litros se necesitan para recorrer cierta distancia.
   def calcularLitros(km):
       litros=km/rendimiento
       return litros

   print()
   print("Si recorres ", kilometros, "kms con", litrosgasolina, "litros de gasolina, el rendimiento es: ")
   print("%.2f" %calcularRendimiento(kilometros, litrosgasolina), "km/lt")
   print("%.2f" %calcularConversion(kilometros, litrosgasolina), "mi/gal")
   print()
   kmrecorridos= float(input("¿Cuantos kilometros vas a recorrer?"))
   rendimiento=calcularRendimiento(kilometros, litrosgasolina)
   print()
   print("Para recorrer %.2f" %kmrecorridos, "km necesitas %.2f" %calcularLitros(kmrecorridos),"litros de gasolina.")

main()
