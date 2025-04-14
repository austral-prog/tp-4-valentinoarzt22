import math

def line():
    cofA = float(input('Ingrese el coeficiente A: '))
    cofB = float(input('Ingrese el coeficiente B: '))
    cofX1 = float(input('Ingrese el coeficiente X1: '))
    cofX2 = float(input('Ingrese el coeficiente X2: '))
    y1 = cofA * cofX1 + cofB
    y2 = cofA * cofX2 + cofB
    distancia = math.sqrt((cofX2 - cofX1) ** 2 + (y2 - y1) ** 2)
    print(f'El coeficiente A de su ecuación de la recta es: {cofA}')
    print(f'El coeficiente B de su ecuación de la recta es: {cofB}')
    print(f'El coeficiente X1 de su ecuación de la recta es: {cofX1}')
    print(f'El coeficiente X2 de su ecuación de la recta es: {cofX2}\n')
    print(f'Para la siguiente ecuación:\n\tY = {cofA}X + {cofB}\n')
    print(f'Dados los siguientes puntos:\n\tP1 ({cofX1}, {y1})\n\tP2 ({cofX2}, {y2})\n')
    print(f'La distancia entre ellos es: {distancia}')
