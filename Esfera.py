#Javier Pascal Flores A01345925

def main():
    radio=float(input("Dame el radio "))
    return radio

def hacer_diametro(radio):
        diametro=radio*2
        return float(diametro)
def hacer_volumen(radio):
        volumen=float((4/3)*3.14*radio**3)
        return round(volumen, 2)
def hacer_area(radio):
        area=float(4*3.14*radio**2)
        return round(area,2)
radio=main()
print("Radio de la esfera: ", radio)
print("Diametro de la esfera: ", hacer_diametro(radio))
print("Area de la esfera: ", hacer_area(radio))
print("Volumend de la esfera: ", hacer_volumen(radio))
