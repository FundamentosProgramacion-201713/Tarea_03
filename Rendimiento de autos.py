#encoding: UTF-8
#Autor: Aaron Tonatiuh Villanueva Guzmán
#Este programa calcula e imprime información acerca del rendimiento de un auto. A partir de datos como los km recorridos y la gasolina, es capaz de calcular el rendimiento e incluso, si se le proporciona una distancia a recorrer, puede indicar la gasolina necesaria.

#Esta funcióm calcula el rendimiento del vehículo a partir de ambos datos de entrada.
def kmporlitro(km,litro):
  rendimiento=km/litro
  return(rendimiento)

#Esta función permite convertir los datos de entrada en unidades inglesas a partir de constantes prestablecidas.
#La conversión de galon a litro de Internet es que un galon equivale a 4.54609 litros. Por lo tanto, la constante debería ser 0.2199692483 en lugar de la indicada en el ejercicio. Debido a esta variación, el resultado de esta función no es igual al del ejemplo.
def conversionaUnidadesInglesas(km,litro):
  millas= km/1.609344
  galones= litro*.264172051
  return(millas,galones)

#Esta función calcula el rendimiento del vehículo en unidades inglesas a partir de la información de la función de coversión.
def milporgalon(ml,gal):
  rendimiento=ml/gal
  return(rendimiento)

#Esta función calcula la gasolina necesaria para recorrer una distancia a partir de datos de entrada.
def gasolinanecesaria(km,rendimiento):
  gasolina=km/rendimiento
  return(gasolina)

#Esta función Main lee los datos de entrada y ejecuta las funciones pertienentes además de imprimir resultados con el formato indicado.
def Main():
  kmrecorridos=int(input("Teclea el número de km recorridos: "))
  gasolinausada=int(input("Teclea el número de litros de gasolina usados: "))
  kmporlitroprint=kmporlitro(kmrecorridos, gasolinausada)
  millas,galones=conversionaUnidadesInglesas(kmrecorridos, gasolinausada)
  millasporgalon=milporgalon(millas,galones)
  print("Si recorres 350 kms con 23 litros de gasolina, el rendimiento es:")
  print("%.2f km/l"% kmporlitroprint)
  print("%.2f mi/gal"% millasporgalon)
  kmarecorrer=int(input("¿Cuántos kilómetros vas a recorrer?"))
  gasolinanecesariaprint=gasolinanecesaria(kmarecorrer,kmporlitroprint)
  print("Para recorrer %.2f km. necesitas %.2f litros de gasolina"%(millasporgalon, gasolinanecesariaprint))
  
Main()
