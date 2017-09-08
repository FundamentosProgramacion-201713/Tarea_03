# Autor: Saúl Rodrigo Toral Luna
# Matrícula: A01745007

# Leer las horas normales y extras de un trabajador, asi como el pago por hora
# Imprimir su pago semanal y y el pago extra

# Calcular el pago normal y regresar el resultado de la operación
def calcularPagoNormal(horaNormal, paga):
    pagoNormal = horaNormal * paga
    return pagoNormal

# Calcular el pago extra y regresar el resultado de la operación
def calcularPagoExtra(horaExtra, paga):
    pagoExtra = (horaExtra * (paga + (paga * 0.50)))
    return pagoExtra

def main():
# Ingresar las horas normales y extras del trabajador asi como el salario por hora
    print("")
    horas_Normales = int(input("Teclea las horas normales trabajadas: "))
    horas_Extras = int(input("Teclea las horas extras trabajadas: "))
    pago_Por_Hora = float(input("Teclea el pago por hora: "))
# Imprimir el pago normal y el pago extra, de acuerdo a las funciones anteriores
    print("")
    print("Pago normal: $%.2f " % calcularPagoNormal(horas_Normales, pago_Por_Hora))
    print("Pago extra: $%.2f " % calcularPagoExtra(horas_Extras, pago_Por_Hora))
    print("-----------------------")
# Imprimir el pago total, que es la suma del pago extra más el pago normal
    print("Pago total: $", (calcularPagoExtra(horas_Extras, pago_Por_Hora) + calcularPagoNormal(horas_Normales, pago_Por_Hora)))
main()
