"""
Realiza una función que reciba la velocidad inicial, velocidad final y el tiempo transcurrido, y calcula la acelaración
"""
def pregunta_1(v_final:float, v_inicial:float, tiempo:float):
    aceleracion = (v_final - v_inicial) / tiempo
    return round(aceleracion, 1)


"""
Realiza una función que reciba un punto de coordenas (x,y) y verifique si el punto se encuentra dentro deL anillo de dos círculos con radio 6 y radio 4 respectivamente. Considera que el centro del círculo se encuentra en 0
"""
def pregunta_2(coordenada_X:int, coordenada_y:int):
    
    distancia_euclidiana_coordenadas = (coordenada_X **2 + coordenada_y **2) ** 0.5

    if(distancia_euclidiana_coordenadas >= 4 and distancia_euclidiana_coordenadas <=6 ):
        return "ESTA DENTRO"
    else:
        return "NO ESTA DENTRO"
    
"""
Realiza una función que devuelva el resultado de la suma de raíces cuadradas desde el número 1 hasta el número que recibe la función
"""
from math import sqrt

def pregunta_3(numero:int):
    contador = 1
    suma = 0
    while contador <= numero:
        suma += sqrt(contador)
        contador += 1

    return round(suma,3)

"""
Desarrolla una función que reciba un número y un dígito, y cuente cuantas veces aparece ese dígito en el número. Considera que el números siempre tiene más de un dígito y que nunca tendrá 0 a la izquierda del número.
"""

def pregunta_4(numero:int, digito:int):
    cantidad_veces = 0
    
    while numero > 0:
        if digito == (numero % 10):
            cantidad_veces += 1
        numero = numero // 10
    return cantidad_veces