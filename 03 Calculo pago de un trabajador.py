##encoding: UTF-8

# Autor: Edgar Alexis González Amador, A01746540
# Descripcion: Calcular el pago normal, extra y total de un trabajador segun las horas trabajadas


#Funcción que permite calcular el pago por las horas normales
def calcularPagoNormal(horasNormales, pagoHora):
    pagoNormal = horasNormales * pagoHora
    return pagoNormal

#Función que permite generar el pago por las horas extras
def calcularPagoExtra(horasExtras, pagoHora):
    pagoExtra = horasExtras * (pagoHora*1.5)
    return pagoExtra

#Main, función principal en la que se llama a las funciones anteriores y se piden e imprimen datos.
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal(horasNormales, pagoHora)
    pagoExtra = calcularPagoExtra(horasExtras, pagoHora)
    pagoTotal = pagoNormal + pagoExtra
    print("")
    print("Pago normal: $%.2f"%(pagoNormal))
    print("Pago extra: $%.2f"%(pagoExtra))
    print("----------------------")
    print("Pago total: $%.2f"%(pagoTotal))

main()