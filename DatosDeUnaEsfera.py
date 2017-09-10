# encoding UTF-8
# Autor: Siham El Khoury Caviedes, A01374764

# Descripción: Cálculo del diámetro, volumen y área de una esfera.

# Calcular y guardar en la variable diametro el diámetro de la esfera.
def calcularDiametro(radio):
    diametro = radio * 2                                            # Calcular y guardar en la variable diametro el diámetro de una esfera.
    return diametro                                                 # Regresar diametro.


# Calcular y guardar en la variable volumen el volumen de la esfera.
def calcularVolumen(radio):
    volumen = (4/3) * 3.1416 * (radio**3)                           # Calcular y guardar en la variable volumen el volumen de una esfera.
    return volumen                                                  # Regresar volumen.


# Calcular y guardar en la variable area el area de la esfera.
def calcularArea(radio):
    area = 4 * 3.1416 * (radio**2)                                  # Calcular y guardar en la variable area el área de una esfera.
    return area                                                     # Regresar area.

# Función principal.
def main():
    radio = float(input("Escribe el radio de la esfera: "))         # Leer y guardar en la variable radio el radio de la esfera.
    print ("Esfera con radio:", radio)                              # Imprimir el radio de la esfera.
    diametro = calcularDiametro(radio)                              # Llamar a la función calcularDiametro.
    volumen = calcularVolumen(radio)                                # Llamar a la función calcularVolumen.
    area = calcularArea(radio)                                      # Llamar a la función calcularArea.
    print ("Diametro: %.2f" % diametro)                             # Imprimir el diametro de la esfera.
    print ("Volumen: %.2f" % volumen)                               # Imprimir el volumen de la esfera.
    print ("Area: %.2f" % area)                                     # Imprimir el area de la esfera.

main()                                                              # Ejecutar main.
