#Raul Ortiz Mateos

#2. Datos de una esfera. (25 puntos)
#Escribe un programa que lea el radio de una esfera y que imprima:
#- Diámetro.
#- Volumen.
#- Área.


def calcularDiametro(radio):
    diametro=2*radio
    return diametro

def calcularVolumen(radio):
    volumen=4/3*3.1416*radio**3
    return volumen

def Calculararea(radio):
    area=4*3.1416*radio**2
    return area

def main():
    r=float(input("¿cual es el radio de la circunferencia?: "))
    print("El radio de tu circunferencia es:",r)
    print("el diametro de la circunferencia es:%.2f"% calcularDiametro(r))
    print("el volumen de la circunferencia es:%.2f"% calcularVolumen(r))
    print("el area de la circunferencia es:%.2f"% Calculararea(r))


main()