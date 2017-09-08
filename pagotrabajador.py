#encoding: UTF-8
#Nazdira Abigail Cerda del Prado A01375428
#Descripción: Diseño TopDown para calcular pago total de un trabajador preguntando horas normales y horas extras
# que laboró.

def calcularNormal(pagohora,horasnormales):
    normal=pagohora*horasnormales
    return normal

def calcularExtra(pagohora,horasextra):
    extras=(horasextra)*((pagohora*0.50)+pagohora)
    return extras

def calcularTotal(extras,normal):
    total=extras+normal
    return total

def main():
    pagohora=float(input("Ingrese pago por hora:"))
    horasnormales=float(input("Horas normales trabajadas:"))
    horasextra=float(input("Horas extras trabajadas:"))
    pagonormales=float(calcularNormal(pagohora,horasnormales))
    pagoextras=float(calcularExtra(pagohora,horasextra))
    pagototal=float(calcularTotal(pagonormales,pagoextras))
    print("Pago por horas normales:", pagonormales)
    print("Pago por horas extras:", pagoextras)
    print("Pago total:", pagototal)

main()