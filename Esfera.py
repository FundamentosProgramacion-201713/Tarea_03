#Javier Pascal Flores A01345925

def main():
    radio=int(input("Dame el radio "))

    def hacer_diametro(radio):
        diametro=radio*2
        return diametro
    def hacer_volumen(radio):
        volumen=float((4/3)*3.14*radio**3)
        return volumen
    def hacer_area(radio):
        area=4*3.14*radio
        return radio

    print("Radio de la esfera: ", radio)
    print("Diametro de la esfera: ", hacer_diametro(radio))
    print("Area de la esfera: ", hacer_area(radio))
    print("Volumend de la esfera: ", hacer_volumen(radio))
main()