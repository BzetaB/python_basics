"""
Realiza una función que de acuerdo al capital, tiempo y tasa de interes, devuelva el interés compuesto.
"""
def pregunta_1(c:float, r:float, t:float):
    m = c * (1 + r) ** t
    return round(m,3)

"""
Realiza una función que de acuerdo al valor de temperatura de un objeto identifique el estado.
Considera:
-Si temperatura es menor a 300 es estable
-Si temperatura es menor o igual a 800 es inestable
-Si temperatura es mayor a 800 es critico
"""
def pregunta_2(temp:float):
    if temp < 300:
        return "Estable"
    elif temp <= 800:
        return "Inestable"
    else:
        return "Critico"

"""
Realiza una función que de acuerdo a las estadisticas de una partida, devuelva el logro del jugador
-Si tiene 0 vidas, su logro es game over
-Si logro una estrella y monedas mayor o igual a 50, fue invencible y bonus
-Si logro una estrella sin monedas, fue invencible
-Si logro más de 100 menedas, pero ninguna estrella, su logro fue vida extra
-Si logro más de 50 monedas, pero ninguna estrella, su logro fue bonus
-En otro caso solo retornar continuar
"""
def pregunta_3(monedas: int, estrella:bool, vidas:int):
    if vidas == 0:
        return "Game Over"
    elif estrella == True and monedas >= 50:
        return "Invencible y Bonus"
    elif estrella == True:
        return "Invencible"
    elif monedas >= 100:
        return "Vida Extra"
    elif monedas >= 50:
        return "Bonus"
    else:
        return "Continuar"

"""
Realiza una función que calcule los años necesarios para lograr el objetivo de pollos de acuerdo a la cantidad inicial y su factor de cambio anualmente.
"""
def pregunta_4(p_inicial: int, p_objetivo:int, factor:float):
    anios = 0
    while p_inicial < p_objetivo:
        p_inicial =  p_inicial * factor
        anios += 1

    return anios