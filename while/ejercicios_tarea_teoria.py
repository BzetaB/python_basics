"""
Pregunta 1:
Desarrolla una función que mida el índice de efectividad en partido de Quidditch, recibiendo tres valores:
g: goles marcados
v: velocidad promedio de escoba 
d: distancia promedio al aro

"""
def pregunta_1(g: int, v: int, d: int)->int:
    indice_efectividad = (g * v) // d + (g + v) % d 
    return indice_efectividad


"""
Pregunta 2:
Desarrolla una función que reciba una nota entera n donde n puede ser 0 <= n <= 100, y retorne la calificación correspondiente según la tabla del sistema de calificaciones O. W. L (Ordinary Wizarding Levels)
"""
def pregunta_2(nota: int):
    if nota < 30:
        return "Troll (T)"
    elif nota <45:
        return "Espantoso (D)"
    elif nota < 60:
        return "Pobre (P)"
    elif nota < 75:
        return "Aceptable (A)"
    elif nota < 90:
        return "Supera las Expectativas (E)"
    elif nota < 100:
        return "Sobresaliente (O)"
    else:
        return "Magia Perfecta!"


"""
Pregunta 3:
Desarrolla una función que a partir de 3 números enteros positivos retorne mensajes de acuerdo a los valores que se ingresen:
Condicionales:
- Si los tres valores son iguales: "Pocion de Transformacion".
- Si exactamente dos valores son iguales y corresponden al valor máximo: "Pocion de Fuerza".
- Si exactamente dos valores son iguales y corresponden al valor mínimo:
"Pocion de Debilidad".
- Si los tres valores son distintos y su suma es menor a 100: "Pocion Explosiva"
- Si no cumple con ninguna condición: "Pocion de Equilibrio" 
"""
def pregunta_3(a: int, b:int, c:int):
    if a == b and b == c:
        return "Pocion de Transformacion"
    elif a == b:
        if a > c:
            return "Pocion de Fuerza"
        if a < c:
            return "Pocion de Debilidad"
    elif a == c:
        if a > b:
            return "Pocion de Fuerza"
        if a < b:
            return "Pocion de Debilidad"
    elif b == c:
        if b > a:
            return "Pocion de Fuerza"
        if b < a:
            return "Pocion de Debilidad"
    elif a + b + c > 100:
        return "Pocion Explosiva"
    else:
        return "Pocion de Equilibrio"

"""
Pregunta 4:
Desarrolla una función que reciba los valores:
g: saldo inicial
t: objetivo
Y calcule los números de años necesarios para que el saldo alcance o supere el objetivo por primera vez, teniendo en cuenta que al saldo inicial se le aplica una tasa anual de acuerdo a la siguiente información:
- Si saldo es mayor o igual a 1000, gana interés de tasa anual de 3%
- Si saldo es menor a 1000 y mayor igual a 500, gana un interés de tasa anual de 6%
- Si saldo es menor a 500, gana un interés de tasa anual de 10%
"""
def pregunta_4(g:int, t:int):
    contador_anios = 0
    while g < t:
        if g < 500:
            interes_ganado = (g * 10) // 100
        elif g < 1000:
            interes_ganado = (g * 6) // 100
        else:
            interes_ganado = (g * 3) // 100

        g += interes_ganado
        contador_anios += 1
    return contador_anios

print(pregunta_4(1000, 1400))