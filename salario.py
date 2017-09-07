#Autor: Juan Sebastián Lozano Derbez

def pagonor(pagoporhora):
    horasnor = float(input("Cúantas horas normales trabajaste?: "))
    normal = horasnor * pagoporhora
    return normal

def pagoex(pagoporhora):
    horasex = float(input("Cúantas horas extra trabajaste?: "))
    extra = (horasex * pagoporhora) + ((horasex * pagoporhora*50)/100)
    return extra

def main():

    pagoporhora = float(input("Cuánto ganas por hora?: "))
    total = (pagonor(pagoporhora)) + (pagoex(pagoporhora))

    print('Ganaste %.2f' % total)

main()