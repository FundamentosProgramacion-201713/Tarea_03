# encoding UTF-8
# Autor: Siham El Khoury Caviedes, A01374764

# Descripción: Cálculo del pago total de un trabajador.

# Calular y guardar en la variable pagoNormal el pago por las horas normales de un trabajador.
def calcularPagoNormal(horasNormales, pago):
    pagoNormal = horasNormales * pago                                               # Calular y guardar en la variable pagoNormal el pago por las horas normales de un trabajador.
    return pagoNormal                                                               # Regresar pagoNormal.


# Calular y guardar en la variable pagoTotal el pago por las horas normales y extras de un trabajador.
def calcularPagoTotal(pagoNormal, pagoExtra):
    pagoTotal = pagoNormal + pagoExtra                                              # Calular y guardar en la variable pagoTotal el pago por las horas normales y extras de un trabajador.
    return pagoTotal                                                                # Regresar pagoTotal.

# Función principal.
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))            # Leer y guardar en la variable horasNormales las horas normales trabajadas.
    horasExtras = int(input("Teclea las horas extras trabajadas: "))                # Leer y guardar en la variable horasExtras las horas extras trabajadas.
    pago = float(input("Teclea el pago por hora: "))                                # Leer y guardar en la variable pago el pago por hora.
    pagoNormal = calcularPagoNormal(horasNormales, pago)                            # Llamar a la funcion calcularPagoNormal.
    pagoExtra = horasExtras * (pago*1.5)                                            # Calcular y guardar en la variable pagoExtra el pago por las horas extras trabajadas.
    pagoTotal = calcularPagoTotal(pagoNormal, pagoExtra)                            # Llamar a la función calcularPagoTotal.
    print (" ")                                                                     # Imprimir espacio.
    print ("Pago normal: %.2f" % pagoNormal)                                        # Imprimir el pago normal.
    print ("Pago extra: %.2f" % pagoExtra)                                          # Imprimir el pago extra.
    print ("--------------------")                                                  # Imprimir separación con guiones.
    print ("Pago total: %.2f" % pagoTotal)                                          # Imprimir el pago total.

main()                                                                              # Ejecutar la función main.
