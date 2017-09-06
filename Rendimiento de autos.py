#encoding: UTF-8
#Autor: Aaron Tonatiuh Villanueva Guzmán

def kmporlitro(km,litro):
  rendimiento=km/litro
  return(rendimiento)

def conversionaUnidadesInglesas(km,litro):
  millas= km/1.609344
  galones= litro/.264172051
  return(millas,galones)

def milporgalon(ml,gal):
  rendimiento=ml/gal
  return(rendimiento)

def gasolinanecesaria(km,rendimiento):
  gasolina=km/rendimiento
  return(gasolina)
  
def Main():
  kmrecorridos=int(input("Teclea el número de km recorridos: "))
  gasolinausada=int(input("Teclea el número de litros de gasolina usados: "))
  kmporlitroprint=kmporlitro(kmrecorridos, gasolinausada)
  millas,galones=conversionaUnidadesInglesas(kmrecorridos, gasolinausada)
  millasporgalon=milporgalon(millas,galones)
  print("Si recorres 350 kms con 23 litros de gasolina, el rendimiento es:")
  print(kmporlitroprint,"km/l")
  print(millasporgalon,"mi/gal")
  kmarecorrer=int(input("¿Cuántos kilómetros vas a recorrer?"))
  gasolinanecesariaprint=gasolinanecesaria(kmarecorrer,kmporlitroprint)
  print("Para recorrer", kmarecorrer, "km. necesitas", gasolinanecesariaprint, "litros de gasolina")
  
Main()
