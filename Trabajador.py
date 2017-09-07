#Javier Pascal Flores A01375925
def main(): # define la fucnion main
    horas_N=float(input("Dame las horas normales "))
    horas_E=float(input("Dame las horas extra "))
    pago_H=float(input("Dame el pago por hora "))
    return horas_E,horas_N, pago_H
def pagar_horasN(horas,pago_H):
    pago_N=horas*pago_H
    return pago_N #regresar el pago de las horas normales
def paqar_horasE(horas, pago_H):
    pago_E=horas*(pago_H*1.5)
    return float(pago_E) #regresar el pao de las horas extras
def pagar_Total(pago_E,pago_N):
    pago_Total=pago_E+pago_N
    return pago_Total #Regresar el pago normal
horas_E, horas_N, pago_H= main()
pago_N=pagar_horasN(horas_N, pago_H)
pago_E=paqar_horasE(horas_E, pago_H)
pago_Total=pagar_Total(pago_E, pago_N)

print("Pago normal: $", pago_N)
print("Pago Extra:  $", pago_E)
print("Pago total:  $", pago_Total)

