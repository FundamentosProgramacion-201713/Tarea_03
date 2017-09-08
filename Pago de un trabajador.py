#encodong: UTF-8
#Luis Fernando Figueroa Rendon, A01746139

#Calcular el pago por horas de un trabajador.

def main():
    horasN= float(input("Teclea las horas normales trabajadas: "))
    horasE= float(input("Teclea las horas extras trabajadas: "))
    pago= float(input("Teclea el pago por hora: "))

#Funcion que recibe el numero de horas trabajadas, calcula el pago por dichas horas.
    def calcularPagoN(normales):
        pn=pago*normales
        return pn

#Funcion que recibe el numero de horas extras trabajadas, calcula el pago por dichas horas extras.
    def calcularPagoE(extra):
        pe= extra*((pago*150)/100)
        return pe

#Funcion que recibe el pago de las horas normales y de las extras, calcula el pago total.
    def calcularTotal(totalN, totalE):
        tp=totalN+totalE
        return tp

    print()
    print("Pago normal: $ %.2f" %(calcularPagoN(horasN)))
    print("Pago extra: $ %.2f" %(calcularPagoE(horasE)))
    print("-------------------------")
    print("Pago total: $ %.2f" %(calcularTotal(calcularPagoN(horasN), calcularPagoE(horasE))))

main()