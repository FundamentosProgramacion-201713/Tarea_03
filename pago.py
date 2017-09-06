#ecoding:UTF-8
#Autor: Angel Ramírez Martínez
#Descripción: Calcula el pago de un trabajador a partir de sus horas de trabajo


# Calcula el pago por horas normales del trabajador a partir de las horas normales ingresadas y el pago por horas
# que se reciben como parámetro.
def calcularpagoNormal(horas, pago):
    pagoN = horas * pago
    return pagoN


# Calcula el pago por horas extras del trabajador a partir de las horas extras ingresadas y el pago
# multiplicado 1.5 (50% más) que se reciben como parámetro.
def calcularpagoExtra(xHoras, pago):
    pagoEx = xHoras * (pago * 1.5)
    return pagoEx


# Calcula el pago total a partir del pago de horas normales y pago de horas extras que recibe como parámetros.
def calcularpagototal(pago1, pago2):
    pagoTotal = pago1+pago2
    return pagoTotal

# Esta función main llama a las funciones anteriores e imprime el pago normal, el pago extra y el pago total.
def main():
    horasN = int(input('Teclea las horas normales trabajadas: '))
    horasEx = int(input('Teclea las horas extras trabajadas: '))
    pago = int(input('Teclea el pago por hora: '))
    pago1 = calcularpagoNormal(horasN,pago)
    pago2 = calcularpagoExtra(horasEx,pago)
    pagoTotal = calcularpagototal(pago1,pago2)
    print('')
    print('Pago normal: $%.2f' %(pago1))
    print('Pago extra: $%.2f' %(pago2))
    print('-----------------------')
    print('Pago total: $%.2f' %(pagoTotal))


main()
