#encoding: UTF-8
#Autor: Angel Roberto Pesado Bartolo
#Elaboración de un programa que calcule el diametro, area  y volumen de una esfera a partir del radio que nos de el usuario.
def calcularArea(radio): #definimos la función calcularArea
    area= (4*3.14)*(radio**2) #Obtenemos el area a partir de la formula 4pi por radio al cuadrado, con el radio dado por el usuario
    return area #Regresamos area a la función
def calcularVolumen(radio): #definimos la función calcularVolumen
    volumen= ((4/3)*3.14)*(radio**3)#Obtenemos el volumen a partir de la formula 4/3pi por radio al cubo, con el radio dado por el usuario
    return volumen #Regresamos volumen a la función
def calcularDiametro(radio): #definimos la función calcularDiametro
    diametro= (radio*2) #definimos el diametro a partir de la formula radio  por 2, con el radio dado por el usuario
    return diametro #Regresamos diametro a la función

def main(): #Definimos la función main
    radiot= float(input("Dame el radio de la esfera: "))#Pedimos al usuario el radio
    areat= calcularArea(radiot)  #Mandamos los datos ingresados por el usuario a la función calularArea para obtener el area de la esfera
    diametrot = calcularDiametro(radiot)  #Mandamos los datos ingresados por el usuario a la función calularDiametro para obtener el diametro
    volumentto = calcularVolumen(radiot)  #Mandamos los datos ingresados por el usuario a la función calularVolumen para obtener el volumen de la esfera
    print("El diametro de la esfera es: %.2f"%(diametrot)) #imprimimos el diametro
    print("El area de la esfera es: %.2f "%(areat)) #imprimimos el area con 2 decimales
    print("El volumen de la esfera es: %.2f"%(volumentto))#imprimimos el volumen con 2 decimales



main() #llamamos a la función main para que se ejecute lo que esta dentro de ella.

