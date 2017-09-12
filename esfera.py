#Yerish Valdes Bernes A01375755
#calcular las caracteristicas de una esfera
import math
def calcular_diametro(radio):
    diametro=radio*2
    return diametro

def calcular_volumen(radio):
    volumen=(4*math.pi*(radio**3))/3
    return volumen

def calcular_area(radio):
    area=4*math.pi*radio**2
    return area



def main():
    radio=float(input("Pon el radio de la esfera:"))
    diametro=calcular_diametro(radio)
    volumen=calcular_volumen(radio)
    area=calcular_area(radio)
    print("\nDiametrode de la esfera:%.2f\nVolumen de la esfera:%.2f\nArea de la esfera:%.2f\n"%(diametro,volumen,area))
main()