#encoding: UTF-8
#Autor: Eduardo Roberto Müller Romero, A01745219
#Escribe un programa que calcule el pago a un trabajador

def main():
    horasextras = int(input("Horas Extras Trabajadas: "))
    horasnormales = int(input("Horas Normales Trabajadas: "))
    pago = int(input("pago por hora: "))
    pagonormal = calcularpagodehorasnormales(horasnormales, pago)
    pagoextra = calcularpagoporhorasextras(horasextras, pago)
    pago = pagonormal + pagoextra
    print("pago por hora:", pago)
    print("horas normales trabajadas:", horasnormales)
    print("horas extras trabajadas:", horasextras)
    print("pago por horas normales:", pagonormal)
    print("pago por horas extras:", pagoextra)
    print("total a pagar:", pago)

#multiplica las horas normales por el pago por hora
def calcularpagodehorasnormales(horasnormales, pago):
    pagoporhora = horasnormales * (pago)
    return pagoporhora

#multiplica el pago por hora por 1.5 y luego por las horas extras laboradas
def calcularpagoporhorasextras(horasextras, pago):
    pagoporhorasextras = horasextras * (pago * 1.5)
    return pagoporhorasextras

main()