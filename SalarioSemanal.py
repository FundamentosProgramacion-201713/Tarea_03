#encoding: UTF-8
#Autor: Dora Gabriela Lizárraga González A01229599
#Con este programa se puede calcular el salario de un trabajadpr con las horas extras que trabaje

#Esta función calcula el salario de un empleado con respecto a las horas dentro de su horario que trabajó
def horasNormales (normal,pagoPhora):
    pagoNormales = normal*pagoPhora
    return pagoNormales

#Esta función calcula el salario de un empleado con respecto a las horas extra que trabajó
def horasExtra (extra,pagoPhora):
    pagoExtra = (extra*(pagoPhora+(pagoPhora*.5)))
    return pagoExtra

#Esta función calcula el total que se le tiene que pagar al empleado
def pagoTotal (pagoNormales,pagoExtra):
    salarioSemanal = pagoNormales+pagoExtra
    return salarioSemanal

#Esta función lee los valores de las variables, ejecuta las otras funciones e imprime el resultado
def main():
    normal = float(input('Teclea las horas normales trabajadas: '))
    extra = float(input('Teclea las horas extra trabajadas: '))
    pagoPhora = float(input('Teclea el pago por hora: $'))
    print()
    normalesTotal = horasNormales(normal,pagoPhora)
    extrasTotal = horasExtra(extra,pagoPhora)
    salarioTotal = pagoTotal(normalesTotal,extrasTotal)
    print('Pago normal: $',normalesTotal)
    print('Pago extra: $',extrasTotal)
    print('---------------------')
    print('Pago Total: $', salarioTotal)

main()