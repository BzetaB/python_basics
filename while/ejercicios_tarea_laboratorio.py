"""
Realiza una funcion que reciba dos parámetros reales a y b, que representen semiejes mayor y menor de una elipse, respectivamente. La funcion debe calcular el perímetro aproximádo de la elipse usando la fórmula de Ramanujan. Considera que a y b siempre serán mayores a 0.
"""
from math import pi
def pregunta_1(a:float, b:float):
    perimetro = pi * (3 * (a + b) -  ((3 * a  + b) * (a + 3 * b))**0.5)
    return round(perimetro, 2)

"""
Cree una funcion que reciba una temperatura en grados Celsius y retorne un mensaje
que describa el clima:
• Si la temperatura es menor a 0: ”Congelado”
• Si esta desde 0 hasta 10: ”Muy frio”
• Si esta desde 11 hasta 20: ”Frio”
• Si esta desde 21 hasta 30: ”Templado”
• Si es mayor a 30: ”Caluroso”
"""
def pregunta_2(temperatura:int):
    if temperatura < 0:
        return "Congelado"
    elif temperatura <= 10:
        return "Muy frio"
    elif temperatura <= 20:
        return "Frio"
    elif temperatura <= 30:
        return "Templado"
    else:
        return "Caluroso"


"""
Implementa una función que reciba dos parámetros:
- Monto inicial de la deuda (entero)
- Monto fijo que se paga cada mes

Se necesita hallar cuántos meses demorará para pagar la deuda de acuerdo a los pagos fijos
"""
def pregunta_3(monto_inicial: int, monto_fijo_paga: int):
    if monto_inicial % monto_fijo_paga > 0:
        return monto_inicial // monto_fijo_paga + 1
    return monto_inicial // monto_fijo_paga

"""
Implementa una función que reciba dos parámetros:
- Incicio de rango (entero)
- Fin de rango (entero)

Se necesita hallar la cantida de múltiplos de 4 dentro del rango definido por dos números.
"""

def pregunta_4(inicio_rango: int, fin_rango: int):
    multiplos = 0
    while inicio_rango <= fin_rango:
        if inicio_rango % 4 == 0:
            multiplos += 1
        inicio_rango += 1
    
    return multiplos