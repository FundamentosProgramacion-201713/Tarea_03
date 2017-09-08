#encoding: UTF-8
#Autor: Luis Fernando Figueroa Rendon, A01746139

#Calcular el volumen, diametro y area de una esfera, solo con el radio proporcionado.

def main():
   radio= float(input("Radio de la esfera: " ))
   PI= 3.1416

#Funcion que recibe el valor del radio para sacar el diametro de la esfera.
   def calcularDiametro(radio):
       diametro= 2*radio
       return diametro

#Funcion que recibe el valor del radio para sacar el volumen de la esfera.
   def calcularVolumen(radio):
       volumen= 4/3*PI*radio**3
       return volumen

# Funcion que recibe el valor del radio para sacar el area de la esfera.
   def calcularArea(radio):
       area= 4*PI*radio**2
       return area

   print("Esfera con radio: ", radio)
   print("Diametro: %.2f" %(calcularDiametro(radio)))
   print("Volumen:  %.2f" %(calcularVolumen(radio)))
   print("Area:  %.2f" %(calcularArea(radio)))

main()
