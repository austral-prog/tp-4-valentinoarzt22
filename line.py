import math

def line():
    cofA = float(input('Ingrese el coeficiente A: '))
    cofB = float(input('Ingrese el coeficiente B: '))
    cofX1 = float(input('Ingrese el coeficiente X1: '))
    cofX2 = float(input('Ingrese el coeficiente X2: '))
    y1 = cofA * cofX1 + cofB
    y2 = cofA * cofX2 + cofB
    distancia = math.sqrt((cofX2 - cofX1) ** 2 + (y2 - y1) ** 2)
    print(f"""El coeficiente A de su ecuación de la recta es: {cofA}
    El coeficiente B de su ecuación de la recta es: {cofB}
    El coeficiente X1 de su ecuación de la recta es: {cofX1}
    El coeficiente X2 de su ecuación de la recta es: {cofX2}
    """)
    
    print(f"""Para la siguiente ecuación:
    Y = {cofA} + {cofB}
    
    Dado los siguientes puntos
           P1 ({cofX1}, {y1})
           P2 ({cofX2}, {y2})
           
    La distancia entre ellos es: {distancia}""")
